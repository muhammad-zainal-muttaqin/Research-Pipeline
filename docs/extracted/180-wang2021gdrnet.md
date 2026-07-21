---
source_id: 180
bibtex_key: wang2021gdrnet
title: GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation
year: 2021
domain_theme: Pose 6D
verified_pdf: 180_GDR-Net.pdf
char_count: 231017
---

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                                   1

                                                      GDRNPP: A Geometry-guided and Fully
                                                      Learning-based Object Pose Estimator
                                                                        Xingyu Liu† , Ruida Zhang† , Chenyangguang Zhang, Gu Wang ,
                                                                         Jiwen Tang, Zhigang Li, and Xiangyang Ji, Member, IEEE

                                               Abstract—6D pose estimation of rigid objects is a long-standing and challenging task in computer vision. Recently, the emergence of
                                               deep learning reveals the potential of Convolutional Neural Networks (CNNs) to predict reliable 6D poses. Given that direct pose
                                               regression networks currently exhibit suboptimal performance, most methods still resort to traditional techniques to varying degrees.
                                               For example, top-performing methods often adopt an indirect strategy by first establishing 2D-3D or 3D-3D correspondences followed
arXiv:2102.12145v5 [cs.CV] 22 Mar 2025

                                               by applying the RANSAC-based PnP or Kabsch algorithms, and further employing ICP for refinement. Despite the performance
                                               enhancement, the integration of traditional techniques makes the networks time-consuming and not end-to-end trainable. Orthogonal
                                               to them, this paper introduces a fully learning-based object pose estimator. In this work, we first perform an in-depth investigation of
                                               both direct and indirect methods and propose a simple yet effective Geometry-guided Direct Regression Network (GDRN) to learn the
                                               6D pose from monocular images in an end-to-end manner. Afterwards, we introduce a geometry-guided pose refinement module,
                                               enhancing pose accuracy when extra depth data is available. Guided by the predicted coordinate map, we build an end-to-end
                                               differentiable architecture that establishes robust and accurate 3D-3D correspondences between the observed and rendered RGB-D
                                               images to refine the pose. Our enhanced pose estimation pipeline GDRNPP (GDRN Plus Plus) conquered the leaderboard of the BOP
                                               Challenge for two consecutive years, becoming the first to surpass all prior methods that relied on traditional techniques in both
                                               accuracy and speed. The code and models are available at https://github.com/shanice-l/gdrnpp bop2022.

                                               Index Terms—Object Pose Estimation, Geometry-guided, Iterative Refinement, Direct Regression Network.

                                                                                                                        ✦

                                         1    I NTRODUCTION
                                                                                                                            compared with approaches that instead rely on establishing 2D-

                                         E    STIMATING      the 6D pose, i.e., the 3D rotation and 3D
                                               translation, of objects in the camera frame is a fundamental
                                         problem in computer vision. It has wide applicability to many real-
                                                                                                                            3D [24], [25] or 3D-3D correspondences [20], [21], [26] to
                                                                                                                            estimating the 6D pose.
                                                                                                                                Differently, this latter class of methods usually involves solv-
                                         world tasks such as robotic manipulation [1], [2], [3], augmented                  ing the 6D pose through traditional techniques like PnP or Kabsch,
                                         reality [4], [5] and autonomous driving [6], [7]. In the pre-deep                  and they oftentimes employ Iterative Closest Point (ICP) algorithm
                                         learning era, methods can be roughly categorized into feature-                     for further depth refinement. While such a paradigm provides
                                         based [8], [9], [10] and template-based [11], [12], [13] approaches.               good estimates, it also suffers from several drawbacks. First,
                                         Among these, the most representative branch of work is based                       these methods are usually trained with a surrogate objective for
                                         on point pair features (PPFs), which is proposed by Drost et                       correspondence regression, which does not necessarily reflect the
                                         al. [14] and still achieves competitive results in recent years [15].              actual 6D pose error after optimization. In practice, two sets of
                                         Nonetheless, with the advent of deep learning, methods based on                    correspondences can have the same average error while describing
                                         neural networks become dominant in instance-level object pose                      completely different poses. Second, correspondence-based meth-
                                         estimation [16], [17], [18], [19], [20], [21].                                     ods are sensitive to outliers, rendering the algorithms not robust
                                              Given the CAD model of objects, different strategies for                      and prone to being trapped in local minima. Therefore, they often
                                         predicting 6D pose from monocular or depth data have been                          resort to non-differentiable filtering algorithms like RANSAC,
                                         proposed. An intuitive approach is to directly regress 6D poses                    which limits their applicability in tasks requiring differentiable
                                         from neural networks [22], [19], [23]. Unfortunately, due to the                   poses. For instance, these methods cannot be coupled with self-
                                         lack of geometric prior, such as 2D-3D or 3D-3D correspondences,                   supervised learning from unlabeled real data [27], [28], [29], [30]
                                         these methods currently exhibit suboptimal performance when                        or joint optimization of 3D reconstruction and poses for scene
                                                                                                                            understanding [31], as they require the computation of the pose
                                         ●   Xingyu Liu, Ruida Zhang, Chenyangguang Zhang, Zhigang Li, and                  to be fully differentiable in order to obtain a signal between data
                                             Xiangyang Ji are with the Department of Automation, Tsinghua                   and pose. Besides, the whole process can be very time-consuming
                                             University, Beijing 100084, China, and also with BNRist, Beijing 100084,
                                             China. E-mail: {liuxy21,zhangrd23,zcyg22}@mails.tsinghua.edu.cn,               when dealing with dense correspondences.
                                             lzg.matrix@gmail.com, xyji@tsinghua.edu.cn.                                        To summarize, while correspondence-based methods currently
                                         ●   Gu Wang is with the Lab for High Technolodgy, Tsinghua University,             dominate the field, the incorporation of traditional techniques
                                             Beijing 100084, China. E-mail: guwang12@gmail.com.                             renders the pipelines time-consuming and non-end-to-end train-
                                         ●   Jiwen Tang is with the School of Information Engineering, China Uni-
                                             versity of Geosciences Beijing, Beijing 100084, China. E-mail: Rain-           able. To tackle this problem, we seek to build a geometry-guided
                                             bowend@163.com.                                                                and fully learning-based object pose estimator in this work, as
                                         †: Xingyu Liu and Ruida Zhang have equally contributed.                            illustrated in Fig. 1.
                                           : Corresponding authors.                                                             Firstly, to circumvent the non-differentiable and lengthy
                                         ©2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including
                                         reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or
                                         reuse of any copyrighted component of this work in other works. DOI: 10.1109/TPAMI.2025.3553485
2                                                                      IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

              RGB
                                                                        RANSAC, thus leading to a substantial performance boost.
                                                    Surface Regions
                                                                            The overall pipeline, which we dub GDRNPP (GDRN Plus
                                                                        Plus), offers a flexible framework that adapts to the availability
                                     CNN

                                     A
                                                                        of either RGB or depth modality, ensuring accurate and robust
                                                                        6D pose estimation. To sum up, our technical contributions are
                                                                        threefold:
            6D Pose
             6D Pose                  3D Model        2D-3D Corr.             ●    We construct a fully learning-based object pose estimation
                                                                                   pipeline, achieving state-of-the-art performance among
                                                                                   existing 6D pose estimation methods in both RGB and

                                      A
                                                                                   RGB-D settings.
                               Patch-P P                                      ●    We propose a simple yet effective Geometry-guided Direct
                                                                                   Regression Network (GDRN) to boost the performance
                                                                                   of monocular-based 6D pose estimation by leveraging
                                                                                   the geometric guidance from dense correspondence-based
                                 3D Optical Flow Estimator
                                                                                   features.
             Depth
                                                                              ●    We further devise a geometry-guided refinement module,
                       3D-3D Corr.                                                 enhancing pose accuracy when extra depth data is acces-
                                                      Refined Pose
                                                                                   sible. The predicted object coordinates are leveraged to
                                                                                   set up more elaborated 3D-3D dense correspondences be-
                                                                                   tween the observed and rendered RGB-D images, leading
                                                                                   to more precise pose estimation.
                                                                        Notably, GDRNPP conqured the leaderboard on the Benchmark
               Observed                  Rendered                       for 6D Object Pose Estimation (BOP) Challenge in 2022 and
               Image                     Image
                                                                        2023 [34], [35], winning most of pose and detection awards. The
                                                                        whole pipeline was recognized as “The Overall Best Method” for
Fig. 1: Illustration of GDRNPP. Firstly, we directly regress            two consecutive years. For the first time in the BOP Challenge,
the 6D object pose from a single RGB using a CNN and the                the deep-learning-based method distinctly surpassed traditional
learnable Patch-PnP by leveraging the guidance of intermediate          methods leveraging PPFs or ICP in both accuracy and speed.
geometric features including 2D-3D dense correspondences and                Compared to the former version of this work (GDR-Net)
surface region attention. Moreover, when depth information is           published in CVPR 2021 [36], the revised GDRNPP makes the
available, the network predicts the 3D optical flow to establish 3D-    following improvements. First, we conduct a series of exploratory
3D correspondences between the observed and rendered RGB-D              analyses to strengthen GDRN, including more accurate detection,
image to refine the pose. The details are elaborated in Fig. 2 and      improved augmentation and enhanced model architecture, yielding
Fig. 3.                                                                 substantial improvements to our baseline. Second, we devise a
                                                                        geometry-guided pose refinement module that predicts 3D-3D
                                                                        dense correspondences between the observed and rendered images
PnP/RANSAC process, our network establishes 2D-3D corre-                to refine the pose when depth is available. The refinement proce-
spondences whilst computing the final 6D pose estimate in a fully       dure not only boosts performance but also raises the versatility
differentiable way. In its core, we propose to learn the PnP opti-      of our pipeline, enabling it to flexibly accommodate either RGB
mization from intermediate geometric representations, exploiting        or RGB-D modalities. Moreover, in contrast to [36], GDRNPP
the fact that the correspondences are organized in image space,         demonstrates enhanced capability in generating reliable poses
which gives a significant boost in performance, outperforming all       in challenging circumstances, especially with the T-LESS and
prior monocular-based works.                                            ITODD datasets characterized by numerous symmetric objects
    Additionally, when depth information is accessible, we extend       with a conspicuous absence of texture.
our pipeline to incorporate the extra modality by introducing
a trainable geometry-guided pose refinement module. Drawing             2     R ELATED W ORK
inspiration from [32], we adopt the “render and compare” strategy
                                                                        In this section, we review some prominent pioneer works in the
and predict the 3D optical flow between the rendered image
                                                                        field of 6D pose estimation. These works can be roughly divided
and observed image to establish 3D-3D dense correspondences
                                                                        into three categories which are indirect methods, direct methods
to solve the pose. Previous methods [33], [32] mostly rely on
                                                                        and differentiable indirect methods. Subsequently, we introduce
RGB images to estimate optical flow. While effective in many
                                                                        several commonly employed strategies for pose refinement.
cases, these methods face limitations when there are significant
discrepancies between the rendered and observed images, such
as variations in lighting conditions or object materials. To address    2.1       Indirect Methods
this, our approach incorporates domain-invariant coordinates as an      The most popular approach is to establish 2D-3D or 3D-3D
additional input, enhancing robustness and mitigating such chal-        correspondences, which are then leveraged to solve for the 6D
lenges when they arise. Thanks to the learning-based refinement         pose using a variant of the RANSAC-based PnP/Kabsch algo-
module and the domain-invariant information in the coordinate           rithm. For instance, BB8 [37] and YOLO6D [38] compute the
map, the correspondences are robust and accurate without re-            2D projections of a set of fixed control points (e.g.the 3D corners
lying on the traditional non-differentiable filtering method like       of the encapsulating bounding box). To enhance the robustness,
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                               3

PVNet [17] additionally conducts segmentation coupled with                     or truncation. Moreover, PPP-Net [59] leverages polarized RGB
voting for each correspondence. HybridPose [39] extends PVNet                  images to effectively handle transparent or reflective objects.
by predicting edges and axes of symmetries at the same time.
König et al. [40] develop a fast point pair voting approach for               2.3     Differentiable Indirect Methods
improvement of efficiency. Moreover, PVN3D [20] extends the
                                                                               Recently, there has been an emerging trend of attempting to
idea of keypoint voting to 3D space, leveraging a deep Hough
                                                                               make PnP/RANSAC differentiable. In [60], [61], and [62], the
voting network to detect 3D keypoints, while RCVPose [41]
                                                                               authors introduce a novel differentiable way to apply RANSAC
devises a radial keypoint voting strategy to improve voting ac-
                                                                               via sharing of hypotheses based on the predicted distribution.
curacy. Meanwhile, FFB6D [21] works on the fusion of color
                                                                               Nonetheless, these approaches require a complex training strategy,
and depth features, introducing a full flow bidirectional fusion
                                                                               as they expect a good initialization for the scene coordinates. More
network for 3D keypoints prediction. However, the recent trend
                                                                               recently, ∇-RANSAC [63] proposes to learn inlier probabilities
goes towards predicting dense rather than sparse correspondences,
                                                                               as an objective and incorporates Gumbel Softmax [64] relaxation
including DPOD [42], DPODv2 [26], CDPN [24], SurfEmb [43],
                                                                               to estimate gradients within the sampling distribution. As for
and SDFlabel [44]. They follow the assumption that a larger
                                                                               PnP, BPnP [65] employs the Implicit Function Theorem [66] to
number of correspondences will mitigate the problem of their
                                                                               enable the computation of analytical gradients w.r.t. the pose loss.
inaccuracies and will result in more precise poses. There are
                                                                               Yet, it is computationally expensive especially given too many
also effective endeavors developed in order to construct more
                                                                               correspondences since PnP/RANSAC is still needed for both
robust dense correspondences. Pixel2Pose [45] leverages a GAN
                                                                               training and inference. Instead, Single-Stage Pose [67] attempts to
on top of dense correspondences to increase stability. EPOS [25]
                                                                               learn the PnP stage with a PointNet-based architecture [56] which
makes use of fragments in order to account for ambiguities in
                                                                               learns to infer the 6D pose from a fixed set of sparse 2D-3D
pose. Recently, ZebraPose [46] leverages a binary surface code
                                                                               correspondences. More recently, EPro-PnP [68] makes the PnP
for enhanced efficiency to set up 2D-3D correspondences in a
                                                                               layer differentiable by translating the output from the deterministic
coarse-to-fine manner. Compared to the aforementioned methods,
                                                                               pose to a distribution of pose.
GDRN predicts intermediate geometric features including 2D-3D
dense correspondences, meanwhile differentiably predicting the
6DoF pose.                                                                     2.4     Pose Refinement Methods
    Another orthogonal line of work aims at learning a latent                  Several studies have delved into the realm of refinement methods
embedding of pose which can be utilized for retrieval during                   to improve pose accuracy, as it is challenging to obtain accurate
inference. These embeddings are commonly either grounded on                    pose estimates in a single shot. As for monocular methods,
metric learning employing a triplet loss [47], or via training of an           DeepIM [69] is a representative approach that introduces the
Auto-Encoder [48], [49], [50].                                                 iterative “render-and-compare” strategy to CNN-based pose re-
                                                                               finement. In each iteration, DeepIM renders the 3D model using
2.2 Direct Methods                                                             the current pose estimate and then regresses a pose residual by
Indirect methods leveraging correspondences have natural flaws                 comparing the rendered image with the observed image. Building
in employing many tasks, which require the pose estimation                     upon this concept, CosyPose [18] further leverages the multi-view
to be differentiable [27], [30]. Hence, some methods directly                  information to match each individual objects and jointly refine a
regress the 6D pose, either leveraging a point matching loss [51],             single global scene. RePose [70] and RNNPose [71] formulate
[52] or employing separate loss terms for each component [22],                 the pose refinement as an optimization problem based on feature
[53], [19]. Other methods discretize the pose space and conduct                alignment or the estimated correspondence field.
classification rather than regression [54]. A few methods also try                  As for depth-based methods, the Iterative Closest Point (ICP)
to solve a proxy task during optimization. Thereby, Manhardt                   algorithm [72] and its variants [73], [74], [75], [76], [77] stand out
et al. [55] propose to employ an edge-alignment loss using the                 as the predominant traditional pose refinement algorithms. They
distance transform, while Self6D [27] and Self6D++ [30] harness                have broad applications in monocular [18], [24] or depth [19],
differentiable rendering to allow training on unlabeled samples.               [20], [21] based pose estimation methods. Starting from an initial
Although direct regression methods seem simple and straight-                   estimate, they repeatedly identify point-level correspondences and
forward, they oftentimes perform worse than indirect methods                   refine the pose based on these correspondences. However, due to
due to the lack of 3D geometric knowledge. Therefore, some                     the lack of prior knowledge of the object, the correspondences
methods attempt to eliminate this problem by introducing depth                 often contain multiple outliers and lead to the algorithm being
data. For example, DGECN [52] estimates depth and leverages                    trapped by local minima. More recently, learning-based meth-
it to guide the predictions of pose using an edge convolutional                ods adopt the “render-and-compare” strategy to utilize the 3D
network from correspondences. DenseFusion [19] leverages CNN                   model information of the objects to enhance the robustness of
and PointNet [56] separately to extract color and depth features               the correspondences. In these methods, given an initial pose, a
and fuse them by matching each point, and further predicts pixel-              synthetic image and depth map are rendered based on the object’s
wise poses with a neural network. In contrast, Uni6D [23] direct               pose, then compared to the observed image to iteratively update
concatenates RGB and depth with positional encoding and feeds                  the pose until convergence. For example, se(3)-TrackNet [78]
them to an end-to-end network based on Mask-RCNN [57].                         utilizes two different networks to extract the features of the
    GDR-Net [36], the conference version of this paper, introduces             observed and rendered RGB-D images, and directly regresses the
a Patch-PnP module to replace PnP/RANSAC and make the                          relative pose in se(3). Some approaches like PFA [33] predict
monocular pose estimation pipeline differentiable. Building on                 2D optical flow between the rendered and observed images to
this concept, SO-Pose [58] utilizes multiple geometry represen-                establish dense correspondences, thereby enhancing robustness.
tations for 6D object pose estimation in scenes with occlusion                 However, a critical challenge arises when a corresponding point in
4                                                                       IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

one image does not precisely align with a pixel in the other image       in Euclidean space. When regressing a rotation, this introduces
but instead falls between several pixels. In such cases, the depth       an error close to the discontinuities which becomes often signifi-
value of the corresponding point must be interpolated, inevitably        cantly large. To overcome this limitation, [84] proposed a novel
introducing errors due to discrepancies between the interpolated         continuous 6-dimensional representation for R in SO(3), which
depth and the true depth. These errors can significantly impact          has proven promising [84], [18]. Specifically, the 6-dimensional
pose estimation accuracy, especially near object edges, where            representation R6d is defined as the first two columns of R
interpolation can result in pronounced depth estimation errors. To
                                                                                                                                 \label {eq:r6} \rot _{\text {6d}} = \left [\rot _{\boldsymbol {\cdot }1} ~|~ \rot _{\boldsymbol {\cdot }2}\right ].                                                                                                                                                               (1)
address these challenges, Coupled Iterative Refinement (CIR) [32]
introduces a 3D optical flow estimator [79] that explicitly esti-        Given a 6-dimensional vector R6d = [r1 ∣r2 ], the rotation matrix
mates the depth of corresponding points by leveraging RGB and            R = [R⋅1 ∣R⋅2 ∣R⋅3 ] can be computed according to
depth information from both images. This approach enables more                                    \begin {cases} \rot _{\boldsymbol {\cdot }1} = \phi (\mathbf {r}_1) \\ \rot _{\boldsymbol {\cdot }3} = \phi (\rot _{\boldsymbol {\cdot }1} \times \mathbf {r}_2) \\ \rot _{\boldsymbol {\cdot }2} = \rot _{\boldsymbol {\cdot }3} \times \rot _{\boldsymbol {\cdot }1} \\ \end {cases}, \label {eq:r6_to_rot} 
accurate depth computations, thereby enhancing pose estimation
precision. Inspired by [32], we further utilize the predicted object                                                                                                                                                                                                                                                                                                                                               (2)
coordinates from GDRN as prior knowledge to establish more
accurate correspondences and enhance pose refinement.                    where ϕ(●) denotes the vector normalization operation.
                                                                             Given the advantages of this representation, in this work we
3     M ETHODS                                                           employ R6d to parameterize the 3D rotation. Nevertheless, in
Given an RGB(-D) image I and a set of L objects O = { Oi ∣               contrast to [84], [18], we propose to let the network predict the
i = 1, ⋯, L } together with their corresponding 3D CAD models            allocentric representation [85] of rotation. This representation is
M = { Mi ∣ i = 1, ⋯, L }, our goal is to estimate the 6D pose            favored as it is viewpoint-invariant under 3D translations of the
P = [R∣t] w.r.t. the camera for each object present in I. Notice         object. Hence, it is more suitable to deal with zoomed-in RoIs.
that R describes the 3D rotation and t denotes the 3D translation        Note that the egocentric rotation can be easily converted from
of the detected object.                                                  allocentric rotation given 3D translation and camera intrinsics K
    Fig. 2 and Fig. 3 present a schematic overview of the proposed       following [85].
methodology. In the core, we first detect all objects of interest        Parameterization of 3D Translation. Since directly regressing
using an off-the-shelf object detector, such as [80], [81], [82]. For    the translation t = [tx , ty , tz ]⊺ ∈ R3 in 3D space does not work
each detection, we then zoom in on the corresponding Region              well in practice, previous works usually decouple the translation
of Interest (RoI) and feed it to our network to predict several          into the 2D location (ox , oy ) of the projected 3D centroid and
intermediate geometric feature maps, i.e., dense correspondences         the object’s distance tz towards the camera. Given the camera
maps and surface region attention maps. Thereby, we directly             intrinsics K, the translation can be calculated via back-projection
regress the associated 6D object pose from the intermediate                                           \trans = \mathbf {K}^{-1} t_z\left [o_x, o_y, 1\right ]^\top . \label {eq:t_bp}                                                                                                                                                                                                                              (3)
geometric features. Additionally, when depth information is ac-
cessible, we predict the 3D optical flow between observed and            Exemplary, [54], [48] approximate (ox , oy ) as the bounding box
rendered RGB-D images and build accurate and robust 3D-3D                center (cx , cy ) and estimate tz using a reference camera distance.
dense correspondences to refine the pose.                                PoseCNN [51] directly regresses (ox , oy ) and tz . Nonetheless,
    In the following, we first (Sec. 3.1) revisit the key ingre-         this is not suitable for dealing with zoomed-in RoIs, since it is
dients of direct 6D object pose estimation methods. Afterwards           essential for the network to estimate position and scale invariant
(Sec. 3.2), we illustrate a simple yet effective Geometry-Guided         parameters.
Direct Regression Network (GDRN) which unifies regression-                   Therefore, in our work we utilize a Scale-Invariant representa-
based direct methods and geometry-based indirect methods, thus           tion for Translation Estimation (SITE) [24]. Concretely, given the
harnessing the best of both worlds. Finally (Sec. 3.3), we introduce     size so = max{w, h} and center (cx , cy ) of the detected bounding
the geometry-guided pose refinement module which leverages               box and the ratio r = szoom /so w.r.t. the zoom-in size szoom ,
depth information to further boost the accuracy.                         the network regresses the scale-invariant translation parameters
                                                                         tSITE = [δx , δy , δz ]⊺ , where
3.1   Revisiting Direct 6D Object Pose Estimation                                                         \begin {cases} \delta _x = (o_x - c_x) / w \\ \delta _y = (o_y - c_y) / h \\ \delta _z = t_z / r \\ \end {cases}. \label {eq:t_site} 
Direct 6D pose estimation methods usually differ in one or more                                                                                                                                                                                                                                                                                                                                                    (4)
of the following components. Firstly, the parameterization of the
rotation R and translation t, and secondly, the employed loss
                                                                         Finally, the 3D translation can be solved according to Eq. 3.
for pose. In this section, we investigate different commonly used
                                                                         Disentangled 6D Pose Loss. Apart from the parameterization of
parameterizations and demonstrate that appropriate choices have
                                                                         rotation and translation, the choice of loss function is also crucial
a significant impact on the 6D pose estimates.
                                                                         for 6D pose optimization. Instead of directly utilizing distances
Parameterization of 3D Rotation. Several different parameter-
                                                                         based on rotation and translation (e.g., angular distance, L1 or
izations can be employed to describe 3D rotations. Since many
                                                                         L2 distances), most works employ a variant of Point-Matching
representations exhibit ambiguities, i.e. Ri and Rj describe the
                                                                         loss [69], [51], [18] based on the ADD(-S) metric [13], [86] in an
same rotation with Ri ≠ Rj , most works rely on parametrizations
                                                                         effort to couple the estimation of rotation and translation.
that are unique to help training. Therefore, common choices are
                                                                             Inspired by [87], [18], we employ a novel variant of disentan-
unit quaternions [51], [55], [69], log quaternions [83], or Lie
                                                                         gled 6D pose loss via individually supervising the rotation R, the
algebra-based vectors [53].
                                                                         scale-invariant 2D object center (δx , δy ), and the distance δz .
    Nevertheless, it is well-known that all representations with
four or fewer dimensions for 3D rotation have discontinuities                                  \loss _{\text {Pose}} = \loss _\rot + \loss _{\text {center}} + \loss _{z}. \label {eq:loss_pose}                                                                                                                                                                                                                   (5)
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                                                                                                                                                                                                                                                                                                                                                                   5

                                                                                                        Zoomed-In RoI                                                                                                                                                                                                                                                                Geometric Feature Regression                                                          Patch-P𝑛P

                                                                                                                                                                                                                                                                                                                                                                                              Backbone                           𝑀#'(
                                                                                                                                                                                                                                                                                                                                                                                                                  65×64×64

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                𝐑!"

                                                                                                                                                                                                                                                                                                                                                                                                                                                                 FC 1024
                                                                     Training: Dynamic Zoom-In

                                                                                                                                                                                                                                                                                                                                                                                                                                                                  FC 256
                                                                                                                                                                                                                                                                                                                                                                                                                                              C
                                                                                                  Testing: Detector                                                                                                                                                                                                                                                                                         8                       𝑀,-./-                                     𝐭#$%&
                                                                                                                                                                                                                                                                                                                                                                                                          8×                                                 8
                                                                                                                                                                                                                                                                                                                                                                                                        2×                                                 8×
                                                                                                                                                                                                                                                                                                                                                                                                      51          3×64×64          2×64×64               8×
                                                                                                                                                                                                                                                                                                                                                                                                                                                       12

              40                                                                                                                                                                                                                                                                                                                                                                                                                  𝑀012"03
            ×6
         480                                                                                                                                                                                                                                                                                                                                                                                                    2×64×64
       3×                                                                                                                                                                                                                                                                                                                                                                                                                        𝑀)*+
                                                                                                                          3×256×256

                                                                                                                                                                              Conv-BN-ReLU                                                                                                                                                    Conv Block                                     DeConv             Up-Sample    Conv/2-GN-ReLU       C Concatenation

Fig. 2: Framework of GDRN. Given an RGB image I , our GDRN takes the zoomed-in RoI (Dynamic Zoom-In for training, off-the-
shelf detections for testing) as input and predicts several intermediate geometric features. Then the Patch-PnP directly regresses the 6D
object pose from Dense Correspondences (M2D-3D ) and Surface Region Attention (MSRA ).

Thereby,                                                                                                                                                                                                                                                                                                                                                                                                        the 3D rotation R parameterized as R6d (Eq. 1) and 3D translation
                     \begin {cases} \loss _\rot &= \underset {\mathbf {x} \in \mathcal {M}}{\avg } \| \hat {\rot } \mathbf {x} - \bar {\rot } \mathbf {x} \|_1 \\ \loss _{\text {center}} &= \| (\hat {\delta }_x - \bar {\delta }_x, \hat {\delta }_y - \bar {\delta }_y) \|_1 \\ \loss _{z} &= \| \hat {\delta }_z - \bar {\delta }_z \|_1 \end {cases}, \label {eq:loss_pose_detail}                         t parameterized as tSITE (Eq. 4), respectively.
                                                                                                                                                                                                                                                                                                                                                                                                                Dense Correspondences Maps (M2D-3D ). In order to compute
                                                                                                                                                                                                                                                                                                                                                                                                      (6)
                                                                                                                                                                                                                                                                                                                                                                                                                the Dense Correspondences Maps M2D-3D , we first estimate the
                                                                                                                                                                                                                                                                                                                                                                                                                underlying Dense Coordinates Maps (MXYZ ). M2D-3D can then
                                                                                                                                                                                                                                                                                                                                                                                                                be derived by stacking MXYZ onto the corresponding 2D pixel
where ˆ● and ¯● denote prediction and ground truth, respectively.                                                                                                                                                                                                                                                                                                                                               coordinates. In particular, given the CAD model of an object,
To account for symmetric objects, given R̄, the set of all possible                                                                                                                                                                                                                                                                                                                                             MXYZ can be obtained by rendering the model’s 3D object
ground-truth rotations under symmetry, we further extend our loss                                                                                                                                                                                                                                                                                                                                               coordinates given the associated pose. Similar to [24], [89], we
to a symmetry-aware formulation LR,sym = minLR (R̂, R̄).                                                                                                                                                                                                                                                                                                                                                        let the network predict a normalized representation of MXYZ .
                                                                                                                                                                                                                                                                                                                     R̄∈R̄
                                                                                                                                                                                                                                                                                                                                                                                                                Concretely, each channel of MXYZ is normalized within [0, 1]
                                                                                                                                                                                                                                                                                                                                                                                                                by (lx , ly , lz ), which is the size of the corresponding tight 3D
3.2   Geometry-guided Direct Regression Network                                                                                                                                                                                                                                                                                                                                                                 bounding box of the CAD model.
In this section, we present our Geometry-guided Direct Re-                                                                                                                                                                                                                                                                                                                                                           Notice that M2D-3D does not only encode the 2D-3D cor-
gression Network, which we dub GDRN. Harnessing dense                                                                                                                                                                                                                                                                                                                                                           respondences, but also explicitly reflects the geometric shape
correspondence-based geometric features, we directly regress 6D                                                                                                                                                                                                                                                                                                                                                 information of objects. Moreover, as previously mentioned, since
object pose. Thereby, GDRN unifies approaches based on dense                                                                                                                                                                                                                                                                                                                                                    M2D-3D is regular w.r.t. the image, we are capable of learning
correspondences and direct regression.                                                                                                                                                                                                                                                                                                                                                                          the 6D object pose via a simple 2D convolutional neural network
Network Architecture. As shown in Fig. 2, we feed the GDRN                                                                                                                                                                                                                                                                                                                                                      (Patch-PnP).
with a zoomed-in RoI of size 256 × 256 and predict three                                                                                                                                                                                                                                                                                                                                                        Surface Region Attention Maps (MSRA ). Inspired by [25],
intermediate geometric feature maps with the spatial size of                                                                                                                                                                                                                                                                                                                                                    we let the network predict the surface regions as additional
64 × 64, which are composed of the Dense Correspondences                                                                                                                                                                                                                                                                                                                                                        ambiguity-aware supervision. However, instead of coupling them
Map (M2D-3D ), the Surface Region Attention Map (MSRA ) and                                                                                                                                                                                                                                                                                                                                                     with RANSAC, we use them within our Patch-PnP framework.
the Visible Object Mask (Mvis ). Especially, for heavily obstructed                                                                                                                                                                                                                                                                                                                                                  Essentially, the ground-truth regions MSRA can be derived
datasets, we additionally predict the full Amodal Object Mask                                                                                                                                                                                                                                                                                                                                                   from MXYZ employing farthest points sampling.
(Mamodal ) to improve the capability to reason about occlusions.                                                                                                                                                                                                                                                                                                                                                     For each pixel we classify the corresponding regions, thus
    Our network is inspired by CDPN [24], a state-of-the-art                                                                                                                                                                                                                                                                                                                                                    the probabilities in the predicted MSRA implicitly represent the
dense correspondence-based method for indirect pose estimation.                                                                                                                                                                                                                                                                                                                                                 symmetry of an object. For instance, if a pixel is assigned to
In essence, we keep the layers for regressing MXYZ and Mvis ,                                                                                                                                                                                                                                                                                                                                                   two potential fragments due to a plane of symmetry, minimizing
while removing the disentangled translation head. Additionally,                                                                                                                                                                                                                                                                                                                                                 this assignment will return a probability of 0.5 for each fragment.
we append the channels required by MSRA to the output layer.                                                                                                                                                                                                                                                                                                                                                    Therefore, the probability distribution of MSRA reflect the sym-
Since these intermediate geometric feature maps are all organized                                                                                                                                                                                                                                                                                                                                               metries of objects. Moreover, leveraging MSRA not only mitigates
2D-3D correspondences w.r.t. the image, we employ a simple yet                                                                                                                                                                                                                                                                                                                                                  the influence of ambiguities but also acts as an auxiliary task on
effective 2D convolutional Patch-PnP module to directly regress                                                                                                                                                                                                                                                                                                                                                 top of M3D . In other words, it eases the learning of M3D by
the 6D object pose from M2D-3D and MSRA .                                                                                                                                                                                                                                                                                                                                                                       first locating coarse regions and then regressing finer coordinates.
    The Patch-PnP module consists of three convolutional layers                                                                                                                                                                                                                                                                                                                                                 We utilize MSRA as symmetry-aware attention input to guide the
with kernel size 3×3 and stride = 2, each followed by Group                                                                                                                                                                                                                                                                                                                                                     learning of Patch-PnP.
Normalization [88] and ReLU activation. Two Fully Connected                                                                                                                                                                                                                                                                                                                                                     Geometry-guided 6D Object Pose Regression. The presented
(FC) layers are then applied to the flattened feature, reducing the                                                                                                                                                                                                                                                                                                                                             image-based geometric feature patches, i.e., M2D-3D and MSRA ,
dimension from 8192 to 256. Finally, two parallel FC layers output                                                                                                                                                                                                                                                                                                                                              are then utilized to guide our proposed Patch-PnP for direct 6D
6                                                                                                                                                                                                                        IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

                                                                                                                                                                                                                                                 I𝟎𝟎                                       I𝟎𝟎
                                                                                 Mask

                                                                                                                                                                                                                                                         (𝒇𝒇𝒇𝒇𝒇𝒇𝒇𝒇,𝒕𝒕)     (𝒇𝒇𝒇𝒇𝒇𝒇𝒇𝒇,𝒕𝒕)           (𝒑𝒑𝒑𝒑𝒑𝒑𝒑𝒑,𝒕𝒕)     (𝒑𝒑𝒑𝒑𝒑𝒑𝒑𝒑,𝒕𝒕)
         Observed RGB-D Image                                                                                            𝐈𝐈𝟎𝟎 , 𝐃𝐃𝟎𝟎                                                              𝑪𝑪𝟎𝟎                                                 𝒙𝒙𝟎𝟎→𝒊𝒊           𝒙𝒙𝒊𝒊→𝟎𝟎                 𝒙𝒙𝟎𝟎→𝒊𝒊           𝒙𝒙𝒊𝒊→𝟎𝟎

                                                                                                                                                                                                                                                 I𝒊𝒊                                       I𝒊𝒊
           (𝟎𝟎)             Perturb                                           Render
         𝑷𝑷𝟎𝟎                                               𝑷𝑷𝒊𝒊                                                                                                                                                                  3D optical
                                                                                                                                                                                                                                flow estimator
                    Initialize
           (𝒕𝒕)                                                                                                          𝐈𝐈𝒊𝒊 , 𝐃𝐃𝒊𝒊                                                               𝑪𝑪𝒊𝒊
         𝑷𝑷𝟎𝟎
                                                                                                                        Update                                                                                       (𝒕𝒕+𝟏𝟏)               Optimize
                                                                                                                                                                                                               𝑷𝑷𝟎𝟎                                                            Align

                                                                                                                                                                                                                                     (0)
Fig. 3: Framework of the Refinement Module. Starting with an initial pose P0 , perturbations are applied to generate a set of object
poses {Pi ∣ i = 1, 2, . . . , n}. Correspondences between the observed image I0 and the rendered images {Ii } are established in two
                                                                                         (f low,t)       (f low,t)
parallel ways: (1) using a coordinate-guided 3D optical flow estimator to obtain x0→i              and xi→0        , and (2) using the predicted
                 (pose,t)          (pose,t)                                                                                       (t)     (t+1)
pose to derive x0→i          and xi→0       . By aligning these correspondences, the pose P0 is iteratively refined, updating P0 to P0          .
This optimization is repeated for T = 10 iterations (inner loop), after which a new set of poses {Pi } is generated, and the corresponding
images are rendered. The entire process is repeated Nout = 4 times (outer loop) to achieve the final result.

object pose regression as                                                                                                                                                                                                 3.3   Geometry-guided Pose Refinement
                                                                                                                                                                                                                          To improve pose accuracy when depth information is available, we
                                                     \label {eq:patch_pnp} \pose = \text {Patch-P}n\text {P}(\Mcorr , \Msra ).                                                                                (7)         propose a novel pose refinement module. Despite the advantages
                                                                                                                                                                                                                          of the CIR [32] mentioned in Sec. 2.4, it faces limitations when the
We employ L1 loss for normalized MXYZ , visible masks Mvis and                                                                                                                                                            rendered and observed images differ significantly due to variations
amodal masks Mamodal , and cross-entropy loss (CE ) for MSRA .                                                                                                                                                            in lighting conditions or object materials. These domain mis-
                                                                                                                                                                                                                          matches can impair the performance of the optical flow estimator.
  \begin {split} \loss _{\text {Geom}} =~& \| \Mvisgt \odot (\Mxyzest - \Mxyzgt ) \|_1 + \| \Mvisest - \Mvisgt \|_1 \\ +~& \lambda \| \Mfullest - \Mfullgt \|_1 + CE(\Mvisgt \odot \Msraest , \Msragt ). \end {split}     To mitigate this issue, we incorporate the predicted coordinate
                                                                                                                                                                                                                          map MXYZ from GDRN as an additional input to the optical flow
                                                                                                                                                                                                                          estimator. Specifically, we utilize the coordinate map inferred from
                                                                                                                                                                                                              (8)         the input image and compare it with the coordinate map rendered
                                                                                                                                                                                                                          based on the predicted pose to establish correspondences. This
Thereby, ⊙ denotes element-wise multiplication and we only                                                                                                                                                                strategy provides domain-invariant information, improving robust-
supervise MXYZ and MSRA using the visible region. Specifically,                                                                                                                                                           ness and mitigating the adverse effects of domain mismatches.
for occluded datasets such as LM-O, we set λ = 1, while for                                                                                                                                                                    A straightforward approach to incorporate this information is
occlusion-free datasets like LM, we set λ = 0.                                                                                                                                                                            directly concatenating the predicted coordinate map with images
    The overall loss for GDRN can be summarized as LGDR =                                                                                                                                                                 from other modalities as input. However, as demonstrated in our
LPose + LGeom . Notice that our GDRN can be trained end-to-end,                                                                                                                                                           experiments, this method does not consistently lead to perfor-
without requiring any three-stage training strategy as in [24].                                                                                                                                                           mance improvement. This limitation is primarily due to the possi-
Decoupling Detection and 6D Object Pose Estimation. Similar                                                                                                                                                               bility of inaccuracies in the predicted coordinate map, which can
to [24], [18], we mainly focus on the network for 6D object pose                                                                                                                                                          degrade overall performance. To address this issue, we propose a
estimation and make use of an existing 2D object detector to obtain                                                                                                                                                       more effective solution: instead of using the raw coordinate map
the zoomed-in input RoIs. This allows us to directly make use of                                                                                                                                                          directly, we extract features from the coordinate maps and assign
the advances in runtime [90], [91], [82] and accuracy [80], [81]                                                                                                                                                          a confidence weight to these features. The confidence weight is
within the rapidly growing field of 2D object detection, without                                                                                                                                                          determined based on the discrepancy between the predicted and
having to change or re-train the pose network. Therefore, we adopt                                                                                                                                                        rendered coordinates maps. This approach enables the model to
a simplified Dynamic Zoom-In (DZI) [24] to decouple the training                                                                                                                                                          leverage the coordinate map effectively when it is accurate, while
of our GDRN and object detectors. During training, we first                                                                                                                                                               maintaining robustness in scenarios where the coordinate map
uniformly shift the center and scale of the ground-truth bounding                                                                                                                                                         contains errors.
boxes by a ratio of 25%. We then zoom in the input RoIs with a                                                                                                                                                            Problem formulation. Given the observed image I0 = I, depth
ratio of r = 1.5 while maintaining the original aspect ratio. This                                                                                                                                                        map D0 , and the outputs of GDRN, including 1) the pose predic-
                                                                                                                                                                                                                                  (0)
ensures that the area containing the object is approximately half                                                                                                                                                         tion P0 , 2) the predicted object coordinate map C0 = MXYZ ,
the RoI. DZI can also circumvent the need of dealing with varying                                                                                                                                                         and 3) the predicted object masks M0 = Mvis , the goal of the
object sizes.                                                                                                                                                                                                             refinement module is to refine the pose iteratively, and to yield a
                                                                                                                                                                                                                                                   (T )
    Noteworthy, although we employ a two-stage approach, one                                                                                                                                                              final pose prediction P0 after T steps.
could also implement GDRN on top of any object detector and                                                                                                                                                               Overview. Fig. 3 presents a schematic overview of the proposed
                                                                                                                                                                                                                                                                                   (0)
train it in an end-to-end manner.                                                                                                                                                                                         methodology. In each iteration, given the initial pose P0 , we add
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     7
                  (0)
perturbations on P0 to generate a set of poses {Pi ∣i = 1, 2, .., n}                                                                                                                                                                                                                                                                                 (*)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Corr. Feat. 𝒔!→#                                                                Depth Feat.
                                                                                                                                                                                                                                                                                                                                                   𝐏!
by adding or subtracting an angle θ from either roll, pitch, or yaw.                                                                                                                                                                                                                                                                                                                                                                                               𝜔/                                                                                 Context Feat.
For each pose Pi , we render the image Ii , depth map Di , object                                                                                                                                                                                                                                                                                                                                    𝐂
                                                                                                                                                                                                                                                                                                                                                                                                    𝑪𝒊 #
mask Mi and coordinate map Ci of the object.                                                                                                                                                                                                                                                                                                      (%&'(, *)                                                                                                                                                                  GRU Update
                                                                                                                                                                                                                                                                                                                                                                  Sample & Mask                                                                                                                                                                                  (*01)
                                                                                                                                                                                                                                                                                                                                                 𝐱 !→#                                                                                                                                                                                                      𝐡!→#
    In each iteration t, we refine the object pose by aligning the                                                                                                                                                                                                                                                                                                                                                                                                                                                             Module

correspondences between I0 and {Ii } solved in two parallel ways                                                                                                                                                                                                                                                                                                                                                                              Coor. Feat. 𝒄!→#
following [32]. For each point xi in the rendered image Ii , we
compute its corresponding point xi→0 in the observed image I0                                                                                                                                                                                                                                                                                                                                       𝐂!4
                                                                                                                                                                                                                                                                                                                                                                                                    𝑪𝟎 ’
                                               (t)
by (a) the previous object pose prediction P0 or (b) predicted                                                                                                                                                                                                                                                                                             𝐂!                                               Mask                                             CNN 𝚲                                                𝐱 !→#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       (,-&.,*)                            (*)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         𝐡!→#
3D optical flows. Similarly, we compute the corresponding points
x0→i in Ii of each point in I0 . We formulate the differences                                                                                                                                                                                                                                                                                                                                     Concatenation                                                                 Multiplication

between (a) and (b) as the optimization objective and use the
                                                               (t+1)
Gauss-Newton algorithm to optimize the pose prediction P0                                                                                                                                                                                                                                                                                     Fig. 4: Overview of the 3D optical flow estimator. We first use
for the next iteration. We repeat this optimization for T = 10                                                                                                                                                                                                                                                                                the correspondences inferred from the previous pose prediction
iterations (inner loop). Subsequently, a new set of poses {Pi } is                                                                                                                                                                                                                                                                            to sample the rendered coordinate map Ci and get C′0 . Then
generated, and the corresponding new image set is rendered. This                                                                                                                                                                                                                                                                              we concatenate the predicted coordinate map C0 and C′0 and
refinement process is repeated Nout = 4 times (outer loop).                                                                                                                                                                                                                                                                                   mask the visible region. The coordinate feature c0→i is extracted
Correspondences from the previous pose prediction. We des-                                                                                                                                                                                                                                                                                    by a convolutional network Λ and weighted dynamically by ωc
ignate the 3D coordinate of a point as x = [x, y, d]⊺ , where                                                                                                                                                                                                                                                                                 according to the quality of the coordinate map. The weighted
x, y are the image coordinates normalized by K−1 and d is the                                                                                                                                                                                                                                                                                 coordinate feature, context feature, depth feature, the correlation
inverse depth value. For a point x0 in the observed image I0 ,                                                                                                                                                                                                                                                                                feature s0→i , along with the hidden state h0→i are fed into the
its corresponding point x0→i in the rendered image Ii can be                                                                                                                                                                                                                                                                                  GRU-based update module, which outputs the correspondences
computed by the previous pose prediction Pt0 as                                                                                                                                                                                                                                                                                               x0(flow
                                                                                                                                                                                                                                                                                                                                                 →i
                                                                                                                                                                                                                                                                                                                                                     ,t)                              (t)
                                                                                                                                                                                                                                                                                                                                                          and a new hidden state h0→i . The correspondences
                                                                                                                                                                                                                                                                                                                                                     ,t)
                  \point _{0\rightarrow i}^{(\text {pose}, t)} = \Pi (\pose _i (\pose _0^{(t)})^{-1} \Pi ^{-1}(\point _0)).                                                                                                                                                                                                             (9)
                                                                                                                                                                                                                                                                                                                                              xi(flow
                                                                                                                                                                                                                                                                                                                                                 →0      are calculated in a symmetric manner.

where t is the number of iterations, Π and Π−1 are the depth-
augmented pinhole projection functions that convert coordinates                                                                                                                                                                                                                                                                               Using the lookup operator, we retrieve the correlation feature s0→i
                                                                                                                                                                                                                                                                                                                                                         (pose,t)
of a point between the world frame X = [X, Y, Z ]⊺ and the                                                                                                                                                                                                                                                                                    where x0→i          serves as the index.
normalized image frame x = [x, y, d]⊺ as                                                                                                                                                                                                                                                                                                           During each iteration, the update module is fed with the
                                                                                                                                                                                                                                                                                                                                              correlation feature s0→i , the weighted coordinate feature ωc c0→i
                                                                                                                                                                                                                                                                                                                                                                                                     (t−1)
                                                             \begin {split} \Pi (X) &= \frac {1}{Z}[X, Y, 1]^\top , \\ \Pi ^{-1}(\point ) &= \frac {1}{d}[x, y, 1]^\top . \end {split}                                                                                                                                                        (introduced below), the previous hidden state h0→i , and the
                                                                                                                                                                                                                                                                                                                                       (10)                                                              (0)
                                                                                                                                                                                                                                                                                                                                              context and depth features. The initial hidden state h0→i as well
                                                                                                                                                                                                                                                                                                                                              as the context and depth features are computed in accordance with
                                                                                                                                                                                                                                                                                                                                                                                                             (t)
                                                                                                                                                                                                                                                                                                                                              CIR. The update module outputs a new hidden state h0→i , the
Analogously, for xi in the rendered image Ii , its corresponding                                                                                                                                                                                                                                                                                                           (t)                                   (t)
                                                                                                                                                                                                                                                                                                                                              optical flow residuals r0→i , and a dense confidence map w0→i .
point in I0 is
                                                                                                                                                                                                                                                                                                                                              The confidence map dynamically identifies outliers, improving the
                  \point _{i\rightarrow 0}^{(\text {pose},t)} = \Pi (\pose _0^{(t)} (\pose _i)^{-1} \Pi ^{-1}(\point _i)).                                                                                                                                                                                                             (11)   robustness of correspondences. Similarly, the same update module
                                                                                                                                                                                                                                                                                                                                              is applied in the reverse direction, using si→0 and ci→0 to predict
Correspondences from optical flows. Our goal is to refine the                                                                                                                                                                                                                                                                                    t)          (t)
                                                                                                                                                                                                                                                                                                                                              r(i→ 0 and wi→0 .
previous pose prediction by establishing accurate and robust 3D-                                                                                                                                                                                                                                                                              Leveraging coordinate map for optical flow estimation. We
3D correspondences. To this end, we predict 3D optical flow with                                                                                                                                                                                                                                                                              encode the predicted coordinates from GDRN into coordinate
the guidance of the coordinate map. We define the 3D optical                                                                                                                                                                                                                                                                                  features to provide domain-invariant information. Since C0 and
flow as ∆x = [∆x, ∆y, ∆d]⊺ in this paper, which consists of the                                                                                                                                                                                                                                                                               Ci belong to the same domain, it is unnecessary to set up a
traditional 2D optical flow and the motion of the inverse depth.                                                                                                                                                                                                                                                                              correlation volume or use a lookup operator to retrieve features
The overview of the 3D optical flow estimator is shown in Fig. 4.                                                                                                                                                                                                                                                                             as done for RGB images. Instead, we bilinearly sample Ci using
           (pose,t)                           (flow,t)                                                                                                                                                                                                                                                                                               ,t)
We use x0→i         as the initialization of x0→i , and refine the                                                                                                                                                                                                                                                                            x(pose      as the index to generate a coordinate map C′0 . This map
                                                          (t)                                                                                                                                                                                                                                                                                   0→i
correspondences by predicting 3D optical flow residuals r0→i and                                                                                                                                                                                                                                                                              transforms Ci into C0 based on the current predicted optical flow.
  (t)
ri→0 , denoted as                                                                                                                                                                                                                                                                                                                             By comparing C′0 with C0 , we can assess the accuracy of the
                                                                                                                                                                                                                                                                                                                                              optical flow prediction and further refine it.
                                 \begin {split} \point _{0\rightarrow i}^{(\text {flow}, t)} = \point _{0\rightarrow i}^{(\text {pose}, t)} + \mathbf {r}_{0\rightarrow i}^{(t)}, \\ \point _{i\rightarrow 0}^{(\text {flow}, t)} = \point _{i\rightarrow 0}^{(\text {pose}, t)} + \mathbf {r}_{i\rightarrow 0}^{(t)}. \end {split}                However, since some points in I0 are not visible in Ii and
                                                                                                                                                                                                                                                                                                                                       (12)
                                                                                                                                                                                                                                                                                                                                              therefore lack valid correspondences, it is necessary to isolate the
                                                                                                                                                                                                                                                                                                                                              object regions visible under both poses and mask out outliers. To
                                                                                                                                                                                                                                                                                                                                                                                                (pose,t)
3D optical flow estimator. We provide an overview of the optical                                                                                                                                                                                                                                                                              achieve this, we sample the mask Mi using x0→i             to generate
                                                                                                                                                                                                                                                                                                                                                                               ′
flow estimator in Fig. 4. Built upon RAFT [79], we propose a                                                                                                                                                                                                                                                                                  a corresponding mask M0 . To guide the prediction of optical
coordinate-augmented RAFT to predict the optical flow residuals                                                                                                                                                                                                                                                                               flow residuals, we use a convolutional network Λ to encode the
r(0t→) i , r(i→
              t)                                                                                                                                                                                                                                                                                                                              difference of C′0 and C0 into a coordinate feature c0→i . The
                0 along with their confidence weight maps.
      Following CIR [32], a GRU-based update module is employed                                                                                                                                                                                                                                                                               coordinate feature c0→i is computed as follows,
for iterative optical flow estimation. Given an image-render pair                                                                                                                                                                                                                                                                                                 \mathbf {c}_{0\rightarrow i} = \Lambda ( \mathbf {M}'_0 \odot \mathbf {M}_0 \odot (\coor '_0~ \text {\scriptsize \sffamily \textcopyright }~ \coor _{0})), \label {eq:coor_feat}                 (13)
{I0 , Ii }, we first extract features from I0 and Ii using a con-
volutional network and set up a correlation pyramid, as in RAFT.                                                                                                                                                                                                                                                                              where © is the concatenation operator and ⊙ is the element-
8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

wise production. We use M0 and M′0         to ensure that only the                                                                                                                                                                                                                                                                                                                                                                                                                                                                     0.40       RANSAC EPnP                             0.40       RANSAC EPnP
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       0.30       Single-Stage                            0.30       Single-Stage
object regions visible under both poses contribute to the feature                                                                                                                                                                                                                                                                                                                                                                                                                                                                      0.20       Ours                                    0.20       Ours
computation, while outliers are effectively masked out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                0.15                                               0.15
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       0.10                                               0.10

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          pose error

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             pose error
    The quality of the coordinate C0 predicted by GDRN sig-
nificantly influences the quality of c0→i and the precision of the                                                                                                                                                                                                                                                                                                                                                                                                                                                                     0.05                                               0.05
pose prediction. Inaccuracies in the predicted coordinate map can                                                                                                                                                                                                                                                                                                                                                                                                                                                                      0.03                                               0.03
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       0.02                                               0.02
degrade overall performance. To ensure robustness, we introduce a
confidence weight for the coordinate feature c0→i . The confidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                     0.01                                               0.01
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              0.01 0.02 0.03 0.04 0.05                           0.01 0.02 0.03 0.04 0.05
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 noise level (outlier=10%)                          noise level (outlier=30%)
weight ωc is defined as
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         (a)                                              (b)                   (c)
                                                                 \omega _c = \mathbbm {1}(\text {avg}(\mathbf {M}'_0 \odot \mathbf {M}_0 \odot |\mathbf {C}'_0 - \mathbf {C}_0|) < \gamma ), \label {eq:weight}                                                                                                                                                                                                                                                                                            (14)                                    (a)                                                     (b)                   (c)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Fig. 5: Results of PnP variants on Synthetic Sphere. (a, b):
where 1(●) is the indicator function, avg(●) computes the average                                                                                                                                                                                                                                                                                                                                                                                                                                                         We compare our Patch-PnP module with the traditional RANSAC
error between C′0 and C0 , and γ is a threshold hyperparameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                           EPnP [92] and another learning-based PnP [67]. The pose error
If the average error exceeds the threshold γ , the coordinate is                                                                                                                                                                                                                                                                                                                                                                                                                                                          is reported as relative ADD error w.r.t. the sphere’s diameter (y-
deemed unreliable and ωc is set to 0. Otherwise, ωc = 1. The                                                                                                                                                                                                                                                                                                                                                                                                                                                              axis in log-scale). (c): Zoomed-In (64 × 64) synthetic examples for
weighted coordinate feature is then computed as ωc c0→i , ensuring                                                                                                                                                                                                                                                                                                                                                                                                                                                        Patch-PnP.
that only reliable coordinate features contribute to the optical
flow refinement process, thereby enhancing the robustness of the
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          synthetic toy dataset, which clearly demonstrates the benefit of
overall system.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          our Patch-PnP compared to the classic optimization-driven PnP.
Optimization. The optimization objective is defined as follows
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Additionally, we demonstrate the effectiveness of our individual
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          components by performing ablative studies on LM [13] and LM-
      \begin {split} \mathop {\arg \min }\limits _{\pose _0^{(t)} \in SE(3)} \mathcal {E}(\pose _0^{(t)})= \sum _{i=1}^{n} \sum _{\point _0 \in \mask _0} \mathbf {w}_{0\rightarrow i}^{(t)} \|\point _{0\rightarrow i}^{(\text {flow},t)} - \point _{0\rightarrow i}^{(\text {pose},t)} \|^2 \\ + \sum _{i=1}^{n} \sum _{\point _i \in \mask _i} \mathbf {w}_{i\rightarrow 0}^{(t)} \|\point _{i\rightarrow 0}^{(\text {flow},t)} - \point _{i\rightarrow 0}^{(\text {pose},t)} \|^2 , \end {split} \label {eq:goal} 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          O [86]. Finally, we compare our method with state-of-the-art
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          methods on the BOP benchmark [34], which contains seven core
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          datasets including LM-O [86], YCB-V [51], T-LESS [93], TUD-
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          L [94], IC-BIN [95], ITODD [96] and HB [97].
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           (15)
where ∥ ● ∥ is the Euclidean distance and Mi is the object mask                                                                                                                                                                                                                                                                                                                                                                                                                                                           4.1                 Experimental Setup
of Ii .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Implementation Details. All our experiments are implemented
    The objective defined in Eq. 15 aims to find camera poses P0                                                                                                                                                                                                                                                                                                                                                                                                                                                          using PyTorch [98]. We train the GDRN(PP) end-to-end using
                                      (pose)     (pose)
that result in reprojected points xi→0 , x0→i that align with                                                                                                                                                                                                                                                                                                                                                                                                                                                             the Ranger optimizer [99], [100], [101] which combines the
                                 (f low)     (f low)                                                                                                                                                                                                                                                                                                                                                                                                                                                                      RAdam [99] optimizer with Lookahead [100] and Gradient Cen-
the revised correspondences xi→0 , x0→i . We compute the
               (t)     (pose,t)
gradient of P0 in x0→i , xi→0
                                 (pose,t)
                                          and perform three steps of                                                                                                                                                                                                                                                                                                                                                                                                                                                      tralization [101] on a single NVIDIA 3090 GPU. On the LM
                                      (t+1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               dataset, we set the total training epoch to 160 with a batch size
Gauss-Newton updates to obtain P0           .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          of 24 and a base learning rate of 10−4 , which we anneal at 72 %
Training. For supervision, we evaluate the predicted optical flow
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          of the training phase using a cosine schedule [102]. While for
and refined pose estimates from all update iterations in the forward
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the BOP datasets, we train GDRN for 40 epochs under the one
pass. Specifically, we use LPose in Eq. 5 to supervise the estimated
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          model per dataset setting, and 100 epochs under the one model
pose and employ the L1 endpoint error as the loss to supervise the
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          per object setting, with a batch size of 36 and a base learning rate
optical flow. During training, we introduce random perturbations
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          of 8 × 10−4 . The refinement module is trained from scratch using
to the ground-truth rotation and translation for pose initialization.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the AdamW [103] optimizer for 200k steps with batch size 12 for
We generate the input coordinate by first rendering the coordinate
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          each dataset on 2 NVIDIA 3090 GPUs. We adopt an exponential
map with a perturbed pose and then adding Gaussian noise. We
                                                               (0)                                                                                                                                                                                                                                                                                                                                                                                                                                                        learning rate schedule with a linear increase to 3 × 10−4 over the
perform one outer iteration and render only one image for P0 at
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          first 10k steps and a 50 % drop for every 20k steps afterwards, and
each training step.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the weight decay is set to 10−5 .
Handling symmetry. For symmetric objects, the coordinate map
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Datasets. We conduct our experiments on nine datasets: Synthetic
rendered by the predicted pose might be inconsistent with the
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Sphere [92], [67], LM [13] and seven core datasets included in
predicted coordinate map. Therefore, given the set of all possible
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the BOP benchmark [104]. The Synthetic Sphere dataset contains
poses under symmetry P, we select the pose with the most
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          20k samples for training and 2k for testing, created by randomly
similar rendered coordinate map before feeding it to the refinement
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          capturing a unit sphere model using a virtual calibrated camera
module. Concretely, the selected pose is
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          with a focal length of 800, resolution 640×480, and the principal
                                                                                                  \pose _0^{(0)} = \underset {\pose \in \mathcal {P}}{\arg \min }(\text {avg}|\Theta (\pose ) - \coor _0|), \label {eq:sym_pose}                                                                                                                                                                                                                                                                           (16)           point located at the image center. The Rotations and translations
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          are uniformly sampled in 3D space, and within an interval of
where Θ is the rendering function to get the rendered coordinate                                                                                                                                                                                                                                                                                                                                                                                                                                                          [−2, 2] × [−2, 2] × [4, 8], respectively. LM dataset consists of
map given an object pose.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 13 sequences, each containing ≈ 1.2k images with ground-truth
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          poses for a single object with clutter and mild occlusion. We
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          follow [16] and employ ≈15 % of the RGB images for training
4        E XPERIMENTS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     and 85 % for testing. We additionally use 1k rendered RGB images
In this section, we first introduce our experimental setup and then                                                                                                                                                                                                                                                                                                                                                                                                                                                       for each object during training as in [24]. LM-O consists of 1214
present the evaluation results for several commonly employed                                                                                                                                                                                                                                                                                                                                                                                                                                                              images from an LM sequence, where the ground-truth poses of
benchmark datasets. Thereby, we first present experiments on a                                                                                                                                                                                                                                                                                                                                                                                                                                                            8 visible objects with more occlusion are provided for testing.
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                                  9

YCB-V is a very challenging dataset exhibiting strong occlusion,               4.3          Ablation Study on LM
clutter and several symmetric objects. It comprises over 110k real             We present several ablation experiments for the widely used LM
images captured with 21 objects, both with and without texture. T-             dataset [13]. We train a single model for all objects for 160
LESS contains 30 industry-relevant objects that lack significant               epochs without applying any color augmentation. For fairness in
texture or discriminative color. It is quite challenging due to                evaluation, we leverage the detection results from Faster R-CNN
object symmetries and mutual similarities between objects. TUD-                as provided by [24].
L comprises three moving objects captured under diverse lighting               Number of Regions in MSRA . In Table 1a, we show results
conditions and varying degrees of occlusion. IC-BIN provides                   for different numbers of regions in MSRA . Thereby, without
a comprehensive collection of cluttered scenes involving two                   our attention MSRA (number of regions = 0), the accuracy is
objects with heavy occlusion, specifically designed for evaluating             deliberately good, which suggests the effectiveness and versatility
pose estimation in the bin-picking scenario. ITODD comprises                   of Patch-PnP. Nevertheless, the overall accuracy can be further
grayscale images captured in realistic industrial scenarios, featur-           improved with increasing number of regions in MSRA , despite
ing a diverse collection of 28 textureless objects. HB consists of             starting to saturate around 64 regions. Thus, we use 64 regions for
33 objects captured in 13 scenes, each exhibiting varying levels               MSRA in all other experiments as a trade-off between accuracy
of complexity. For all the seven BOP core datasets, we also                    and memory.
leverage the publicly available synthetic data using physically-               Effectiveness of Patch-PnP. We demonstrate the effectiveness of
based rendering (pbr) [104] for training.                                      the image-like geometric features (M2D-3D , MSRA ) by comparing
Evaluation Metrics. We use three common metrics for 6D object                  our Patch-PnP with traditional PnP/RANSAC [24], the PointNet-
pose evaluation, i.e. ADD(-S) [13], [105], n°, n cm [106] and                  like [56] PnP from [67], and a differentiable PnP (BPnP [65]).
the BOP metric [94], [104], [34]. The ADD metric measures                      For PointNet-like PnP, we extend the PointNet in [67] to account
whether the average deviation of the transformed model points                  for dense correspondences. Specifically, we utilize PointNet to
is less than 10 % of the object’s diameter (0.1d). For symmetric               pointwisely transform the spatially flattened geometric features
objects, the ADD-S metric is employed to measure the error                     (M2D-3D and MSRA ) and directly predict the 6D pose with global
as the average distance to the closest model point [13], [105].                max pooling followed by two FC layers. Since the correspon-
The n°, n cm metric measures whether the rotation error is                     dences are explicitly encoded in M2D-3D , no special attention is
less than n° and the translation error is below n cm. Notice                   needed for the keypoint orders as in [67]. For BPnP [65], we
that to account for symmetries, n°, n cm is computed w.r.t. the                replace the Patch-PnP in our framework with their implementation
smallest error for all possible ground-truth poses [69]. The BOP               of BPnP† . As BPnP was originally designed for sparse keypoints,
metric is a symmetry-aware comprehensive metric, which is                      we further adapt it appropriately to deal with dense coordinates.
calculated as the mean of the Average Recall of three metrics:                     As shown in Table 1b, Patch-PnP is more accurate than tradi-
ARBOP = (ARMSPD + ARMSSD + ARVSD )/3. Please refer to [104] for a              tional PnP/RANSAC (B0 v.s. A0), PointNet-like PnP (B0 v.s. C0)
detailed explanation of these metrics.                                         and BPnP (B0 v.s. C1) in estimating the 6D pose. Furthermore, in
                                                                               terms of rotation, our Patch-PnP outperforms PointNet-like PnP
                                                                               by a large margin, which proves the importance of exploiting the
4.2   Toy Experiment on Synthetic Sphere                                       ordering within the correspondences. Noteworthy, Patch-PnP is
                                                                               much faster in inference and up to 4× faster in training than BPnP,
We conduct a toy experiment comparing our approach with                        since the latter relies on PnP/RANSAC for both phases.
PnP/RANSAC and [67] on the Synthetic Sphere dataset. We                        Parameterization of 6D Pose. In Table 1b, we illustrate the
generate MXYZ from the provided poses and feed them to our                     impact of our proposed 6D pose parameterization. In particular,
Patch-PnP. For fairness, MSRA is excluded from the input. Fol-                 the 6-dimensional R6d (Eq. 1) achieves a much more accurate
lowing [67], during training, we randomly add Gaussian noise                   estimate of R than commonly used representations such as unit
N (0, σ 2 ) with σ ∈ U[0, 0.03] to each point of the dense coordi-             quaternions [51], [69], log quaternions [83] and the Lie algebra-
nates maps. Since the coordinates maps are normalized in [0, 1],               based vectors [53] (c.f. B0 v.s. D1-D3, and G0 v.s. G2). Moreover,
we choose 0.03 as it reflects approximately the same level of noise            we can deduce that the allocentric representation is significantly
as in [67]. Additionally, we randomly generated 0 % to 30 % of                 stronger than the egocentric formulation (B0 v.s. D0).
outliers for MXYZ (Fig. 5c). During testing, we report the relative                Similarly, the parameterization of the 3D translation is of high
ADD error w.r.t. the sphere’s diameter on the test set with different          importance. Essentially, directly predicting t in 3D space leads
levels of noise and outliers.                                                  to worse results than leveraging the scale-invariant formulation
Comparison with PnP/RANSAC and [67]. In Fig. 5, we                             tSITE (E0 v.s. B0). Additionally, replacing the scale-invariant δz in
demonstrate the effectiveness and robustness of our approach                   tSITE with the absolute distance tz or directly regressing the object
by comparing Patch-PnP with the traditional RANSAC-based                       center (ox , oz ) leads to inferior poses w.r.t. translation (B0 v.s. E1,
EPnP [92] and the learning-based PnP from [67]). As depicted                   E2). Hence, when dealing with zoomed-in RoIs, it is essential to
in Fig. 5, while RANSAC-based EPnP* is more accurate when                      parameterize the 3D translation in a scale-invariant fashion.
noise is unrealistically minimal, learning-based PnP methods are               Ablation on Pose Loss. As mentioned in Section 3.1, the loss
much more accurate and robust as the level of noise increases.                 function has an impact on direct 6D pose regression. In TA-
Moreover, Patch-PnP is significantly more robust than Single-                  BLE 1b, we compare our disentangled LPose to a simple angular
Stage [67] w.r.t. to noise and outliers, thanks to our geometrically           loss and the Point-Matching loss [69] (F0). Furthermore, we
rich and dense correspondences maps.                                           present its disentangled versions following [87]. As shown in (B0
                                                                               and F0-F4), all variants of the PM loss are clearly better than the
    * We follow the state-of-the-art method CDPN [24] for the implementation
                                                                                       †
and hyper-parameters of PnP/RANSAC in all our experiments.                                 https://github.com/BoChenYS/BPnP
10                                                                                   IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

TABLE 1: Ablation study on LM. (a): Ablation of number of regions in MSRA . (b): Ablation of PnP type, the parameterization of R
and t, loss type and geometric guidance.

               100                                                                                                 ADD(-S)
                                                    Row Method                                                                  2°, 2 cm 2° 2 cm MEAN
                   90                                                                                         0.02d 0.05d 0.1d
                                                    A0   CDPN [24]                                              -     -    89.9     -     -   92.8  -
                   80                               B0   GDRN (Ours)                                           35.5 76.3 93.7     62.1   63.2 95.5 71.0
accuracy (%)

                   70                               B1   B0: → Test with PnP/RANSAC                            31.0 72.1 92.2     67.1   68.9 94.5 71.0
                                                    B2   B0: → Patch-PnP for t; PnP/RANSAC for R               35.6 76.0 93.6     67.1   69.0 95.5 72.8
                   60                               C0   B0: Patch-PnP → PointNet-like PnP                     29.2 72.6 92.3     44.5   45.8 94.3 63.1
                   50                               C1   B0: Patch-PnP → BPnP [65]                             34.3 72.6 92.0     64.3   66.0 94.4 70.6
                                                    D0   B0: Allocentric R6d → Egocentric R6d                  36.1 75.7 93.2     60.4   61.5 95.3 70.4
                   40                               D1   B0: Allocentric R6d → Allocentric quaternion          24.8 67.4 90.5     35.5   36.9 92.2 57.9
                   30                               D2   B0: Allocentric R6d → Allocentric log quaternion      22.7 64.6 88.9     33.7   35.4 90.9 56.0
                        0 1 4 8 16 32 64 128 256    D3   B0: Allocentric R6d → Allocentric Lie algebra vector 23.0 66.3 89.7      33.8   35.3 91.4 56.6
                            number of regions
                   74                               E0   B0: tSITE → t                                         28.3 72.0 92.4     61.6   63.2 94.6 68.7
                                                    E1   B0: tSITE → (ox , oy ); tz                            31.4 73.7 93.3     50.4   51.6 94.7 65.8
                                                    E2   B0: δz → tz                                           32.8 73.5 93.3     63.3   64.8 94.9 70.4
                   72
                                                    F0   B0: LPose → LPM = avg ∥(R̂x + t̂) − (R̄x + t̄)∥1      33.7 76.5 94.1     47.4   48.2 95.8 65.9
                                                                            x∈M
                                                         F0: LPM → Disentangling R; t
    accuracy (%)

                   70                               F1                                                      30.8   71.1   91.8   64.6   66.8   93.5   69.8
                                    ADD(-S) 0.02d   F2   F0: LPM → Disentangling R; (tx , ty ); tz          32.2   73.9   93.6   63.8   65.3   94.8   70.6
                                    ADD(-S) 0.05d   F3   B0: LR → Angular loss                              32.4   75.5   93.8   40.2   40.9   95.7   63.1
                   68               ADD(-S) 0.1d    F4   B0: LR → LR,sym                                    35.5   75.8   93.9   61.6   62.7   95.4   70.8
                                    2°, 2 cm
                                    2°              G0   B0: LGDR → w/o LGeom                               30.8   72.7   92.2   45.9   46.8   94.1   63.7
                   66
                                    2 cm            G1   G0: → w/o M2D                                      18.6   60.1   85.6   26.0   27.8   87.6   51.0
                                    MEAN            G2   G0: Ra6d → Allocentric quaternion                   6.7   40.6   73.2    6.2    7.4   75.6   34.9
                   64                                    B0: Faster R-CNN [80] → YOLOv3 [90]
                      0 1 4 8 16 32 64 128 256      H0                                                      33.9   75.6   93.7   60.9   62.1   95.2   70.2
                          number of regions                                                          (b)
                             (a)

angular loss in terms of rotation estimation. In addition, disentan-                   TABLE 2: Ablation study on LM-O for GDRN. We report the
gling the rotation R and distance tz in LPM largely enhances the                       Average Recall (%) of the BOP metric. Note that only synthetic
rotation accuracy. Nonetheless, the overall performance is slightly                    data is used for training.
inferior to our disentangled formulation LPose , which disentangles                     Row    Method                        MSPD MSSD VSD ARBOP
tSITE rather than the 3D translation t. It is worth noting that LR,sym                  A0     baseline                       80.8 55.6 43.6 60.0
has a rather insignificant contribution compared with LR . This can                     B0     A0: Faster RCNN → YOLOv4       81.7 56.6 44.5 60.9
be accounted to the lack of severe symmetries in LM and to our                          B1     A0: Faster RCNN → YOLOX        83.5 57.2 44.8 61.8
proposed surface region attention MSRA .                                                C0     B1: w/ background change       83.7 57.5 44.9 62.0
Effectiveness of Geometry-Guided Direct Regression. Further-                            C1     C0: w/ color augmentation      83.8 57.4 45.2 62.1
more, we train GDRN leveraging only our pose loss LPose by                              D0     C1: ResNet-34 → ResNeSt-50d    84.7 60.0 47.3 64.0
discarding the geometric supervision LGeom . Surprisingly, even                         D1     C1: ResNet-34 → ConvNeXt-base 86.3  62.7 49.4 66.1
the simple version outperforms CDPN [24] w.r.t. ADD(-S) 0.1d,                           D2     D1: w/ amodal mask             86.6 65.7 51.2 67.8
when employing R6d for rotation (TABLE 1b G0 v.s. A0). Yet,                             D3     D2: w/ class-aware head        87.5 66.5 51.8 68.6
we clearly outperform our baseline using GDRN with explicit                             D4     D2: One model per object       88.7 70.1 54.9 71.3
geometric guidance. If we predict the rotation as allocentric
quaternions, the accuracy decreases (G2 v.s. G0), which can
partially account for the weak performance of previous direct                          YOLOv3 detections from [24], the overall accuracy only drops
methods [51], [53]. Moreover, when we remove the guidance of                           slightly while the accuracy for ADD(-S) 0.1d almost remains
M2D , the accuracy drops significantly (G0 v.s. G1). Based on these                    unchanged (TABLE 1b H0).
results, we can see that appropriate geometric guidance is essential
for direct 6D pose regression.                                                         4.4    Ablation Study on LM-O
    Direct pose regression also enhances the learning of geometric                     The BOP Challenge [94], [104] has recently become the de-facto
features as the error signal from the pose can be backpropagated.                      benchmark in object pose estimation. Therefore, to enhance our
TABLE 1b (B1, B2) shows that when evaluating GDRN with                                 baseline method (TABLE 1b B0) for the BOP setup, we make
PnP/RANSAC from the predicted M2D-3D , the overall perfor-                             several improvements and present the ablative results on the LM-
mance exceeds CDPN [24]. Similar to CDPN, we run tests using                           O dataset in TABLE 2 and TABLE 3.
PnP/RANSAC for R and Patch-PnP for t, which achieves the                               Effectiveness of Detection. Due to the decoupling of the detector
overall best accuracy (B2). This demonstrates that our unified                         and pose estimator in our method, we can leverage the state-
GDRN can leverage the best of both worlds, namely, geometry-                           of-the-art detectors without re-training the network. As a result,
based indirect methods and direct methods.                                             we evaluate GDRN with more recently developed detectors such
Effectiveness of Detection and Pose Decoupling. Similar to                             as YOLOv4 [91] and YOLOX [82]. The results presented in
CDPN [24], we decouple the detector and GDRN by means                                  TABLE 2 (B0, B1) demonstrate that the pose accuracy can be
of Dynamic Zoom-In (DZI). When evaluating GDRN with the                                further enhanced by utilizing these more powerful detectors.
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                             11

TABLE 3: Ablation on LM-O for refinement module. We report
the Average Recall (%) of the BOP metric.

   Row     Coor. Mask F. W. Sym.         MSPD MSSD VSD            ARBOP
   Init.     -    -      -    -           88.7 70.1 54.9           71.3
    A       ✗     ✗     ✗    ✗            87.2 82.2 62.9           77.5
    B       ✓     ✗     ✗    ✗            77.7 73.6 57.9           69.7
    C       ✓     ✓     ✗    ✗            80.5 76.4 61.5           72.8
    D       ✓     ✓     ✓    ✗            89.5 84.9 65.4           79.9
    E       ✓     ✗     ✓    ✓            88.6 83.7 65.0           79.1
    F       ✓     ✓     ✓    ✓            90.0 85.2 66.4           80.5
   The row Init. is the initial pose from GDRN.
   Coor. denotes whether the coordinate feature is used in the refinement
  module. Mask denotes whether the coordinate map is masked before
  extracting the coordinate feature as in Eq. 13. F.W. denotes whether the
  coordinate feature is weighted as in Eq. 14. Sym. denotes whether the
  initial pose of the symmetric object is selected as in Eq. 16.

TABLE 4: Comparison with other refinement methods on
LM-O. We report the Average Recall (%) of the BOP metric.

        Method             Modality    MSPD      MSSD      VSD     ARBOP       Fig. 6: Efficiency v.s. accuracy with varying inner and outer
     GDRN (Init.)           RGB         88.7      70.1     54.9     71.3
                                                                               loop iterations for the refinement module on LM-O. The bubble
     CosyPose [18]          RGB         86.8      66.7     52.2     68.5       size represents the inner loop number, while the color indicates the
       ICP [72]              D          76.1      70.9     53.0     66.7       outer loop number.
  FoundationPose [107]     RGB-D        86.0      82.0     63.7     77.2
          Ours             RGB-D        90.0      85.2     66.4     80.5
                                                                               feature weighting, the average recall reaches 79.9 %, which is
                                                                               2.1 % higher than the baseline (TABLE 3 D v.s. A). It reveals
Effectiveness of Image Augmentation. Considering that only                     that feature weighting is essential in improving the robustness
synthetic data are available during training on the LM-O dataset,              against error in the input coordinate and preventing performance
image augmentation plays a vital role in enhancing the generaliza-             degradation. By comparing TABLE 3 (D, F), it can be seen that
tion capability of object pose estimation methods, as demonstrated             selecting a proper initial pose of the symmetric objects as in Eq. 16
in [18], [111]. During the training process, for each image, we                brings 0.6 % performance gain. TABLE 2 (E v.s. F) proves that
randomly change the background to an image selected from the                   masking the input coordinate map as in Eq. 13 is also important
VOC dataset [112] with a probability of 0.5 (TABLE 2 C0).                      since it filters out the outliers dynamically.
Additionally, color augmentation techniques, including dropout,                    Fig. 6 illustrates the trade-off between efficiency and accuracy
Gaussian blur, Gaussian noise, and sharpness enhancement, are                  w.r.t. the refinement module. When the inner loop number (T
applied to augment 80 % of the images in the training phrase                   defined in Sec. 3.3) is set to 2 and the outer loop number (Nout
following [18], [111] (TABLE 2 C1).                                            in Sec. 3.3) to 1, the average recall decreases by 0.5%, while
Ablation on Network Architecture. With the rapid growth of                     the inference time drops significantly from 2.48 s to 0.25 s.
data amount (15,375 on LM v.s. 349,693 on LM-O), GDRN needs                    The optimal values for the inner and outer loop numbers can
a more powerful backbone with more parameters to increase the                  be selected based on the specific requirements of the real-world
model’s capacity. TABLE 2 (D0, D1) shows that ResNeSt [113]                    application.
and ConvNeXt [114] outperform the basic ResNet [115] by a large
margin. Moreover, TABLE 2 (D2 v.s. D1) reveals that predicting
the amodal mask can effectively assist the network in dealing with             4.5     Comparison with State of the Arts
occlusions, as mentioned in Section 3.2.                                       We compare our depth refinement module with several state-of-
    We experiment with two class-ware settings and present the re-             the-art refinement methods [72], [18], [107], and present the re-
sults in TABLE 2 (D3, D4). Specifically, we first attempt to modify            sults in TABLE 4. As shown in the table, our proposed geometry-
the output of the geometric head in a class-aware manner, where                guided depth refinement method outperforms all other methods,
different object classes are assigned to individual output chan-               achieving the highest accuracy. The results also indicate that
nels. This strategy allows the network to capture object-specific              the performance of ICP [72] and CosyPose [18] shows a slight
information, resulting in a noticeable performance improvement                 decline compared to the initial predictions. The reliance on a
(68.6 % v.s. 67.8 %). Additionally, we conduct experiments by                  single modality for refinement, i.e. CosyPose using RGB and ICP
training a separate model for each object, which surpasses all                 using only depth, constrains their performance. Notably, the novel
previous results, achieving a remarkable performance of 71.3 %                 object pose refinement method FoundationPose [107] achieves a
w.r.t. ARBOP metric leveraging pure RGB data.                                  performance closest to ours.
Ablation on Refinement Module. The ablation on the refinement                      TABLE 5 compares our enhanced approach (GDRNPP) with
module is listed in TABLE 3. Without the coordinate map as input,              state-of-the-art methods on the seven core datasets included in
the baseline (TABLE 3 A) improves the average recall from 71.3 %               the BOP benchmark. Remarkably, GDRNPP significantly out-
to 77.5 %. As shown in TABLE 3 (B, C), by solely integrating                   performs all other state-of-the-art methods like PFA [33] Zebra-
the coordinate feature, the performance drops significantly due                Pose [46], SurfEmb [43], CPDNv2 [24], CosyPose [18], CIR [32],
to the erroneous coordinate map prediction. However, by adding                 and RCVPose3D [110] across various data modalities (RGB and
12                                                                    IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

TABLE 5: Comparison with State of the Arts on the seven BOP core datasets. We report the Average Recall (%) of the BOP
metric. The results for other methods are obtained from https://bop.felk.cvut.cz/leaderboards/. For each column, we denote the best
score in bold and the second best score in italics. GDRNPP (BOP22) is the BOP Challenge 2022 version of GDRNPP, which utilizes
[32] for depth refinement. Compared to GDRNPP (BOP23), i.e. GPose2023 in the leaderboard, which utilizes YOLOv8 [108] as its
detector, GDRNPP (YOLOX) employs YOLOX [82] for detection. S.M. denotes if the method trains a single model for all objects on
each dataset.

 Method                  Modality    Real    S.M.    LM-O      T-LESS     TUD-L     IC-BIN     ITODD      HB        YCB-V   Avg    time(s)
 GDRNPP (Ours)            RGB         ✗        ✗      71.3       79.6      75.2      62.3        44.8     86.9       71.3   70.2     0.28
 PFA [33]                 RGB         ✗       ✓       74.5       71.9      73.2      60.0        35.3     84.1       64.8   66.3     3.50
 ZebraPose [46]           RGB         ✗        ✗      72.1       72.3      71.7      54.5        41.0     88.2       69.1   67.0       -
 SurfEmb [43]             RGB         ✗       ✓       65.6       74.1      71.5      58.5        38.7     79.3       65.3   64.7     8.89
 EPOS [25]                RGB         ✗       ✓       54.7       46.7      55.8      36.3        18.6     58.0       49.9   45.7     1.87
 CDPNv2 [24]              RGB         ✗        ✗      62.4       40.7      58.8      47.3        10.2     72.2       39.0   47.2     0.98
 DPODv2 [26]              RGB         ✗        ✗      58.4       63.6       -          -          -       72.5        -      -         -
 CosyPose [18]            RGB         ✗        ✗      63.3       64.0      68.5      58.3        21.6     65.6       57.4   57.0     0.48
 GDRNPP (Ours)            RGB         ✓        ✗      71.3       78.6      83.1      62.3        44.8     86.9       82.5   72.8     0.23
 GDRNPP (S.M.)            RGB         ✓       ✓       68.6       77.6      82.7      61.7        26.0     80.9       76.8   67.8     0.23
 PFA [33]                 RGB         ✓       ✓       74.5       77.8      83.9      60.0        35.3     84.1       80.6   70.9     3.02
 ZebraPose [46]           RGB         ✓        ✗      72.1       80.6      85.0      54.5        41.0     88.2       83.0   72.0     0.25
 SurfEmb [43]             RGB         ✓       ✓       65.6       77.0      80.5      58.5        38.7     79.3       71.8   67.3     8.89
 CRT-6D [109]             RGB         ✓       ✓       66.0       64.4      78.9      53.7        20.8     60.3       75.2   59.9     0.06
 Pix2Pose [45]            RGB         ✓        ✗      36.3       34.4      42.0      22.6        13.4     44.6       45.7   34.2     1.22
 CDPNv2 [24]              RGB         ✓        ✗      62.4       47.8      77.2      47.3        10.2     72.2       53.2   52.9     0.94
 CosyPose [18]            RGB         ✓       ✓       63.3       72.8      82.3      58.3        21.6     65.6       82.1   63.7     0.45
 GDRNPP (BOP23)          RGB-D        ✗        ✗      79.4       89.0      93.1      73.7        70.4     95.0       90.1   84.4     2.69
 GDRNPP (YOLOX)          RGB-D        ✗        ✗      80.5       88.4      92.7      73.4        68.7     94.4       91.0   84.2     4.58
 GDRNPP (BOP22)          RGB-D        ✗        ✗      77.5       85.2      92.9      72.2        67.9     92.6       90.6   82.7     6.26
 PFA [33]                RGB-D        ✗       ✓       79.7       80.2      89.3      67.6        46.9     86.9       82.6   76.2     2.63
 SurfEmb [43]            RGB-D        ✗       ✓       75.8       82.8      85.4      65.6        49.8     86.7       80.6   75.2     9.05
 RCVPose3D [110]         RGB-D        ✗       ✓       72.9       70.8      96.6      73.3        53.6     86.3       84.3   76.8     1.34
 Drost [14]              RGB-D        *        -      51.5       50.0      85.1      36.8        57.0     67.1       37.5   55.0    87.57
 Vidal Sensors [15]        D          *        -      58.2       53.8      87.6      39.3        43.5     70.6       45.0   56.9     3.22
 GDRNPP (BOP23)          RGB-D        ✓        ✗      79.4       91.4      96.4      73.7        70.4     95.0       92.8   85.6     2.67
 GDRNPP (YOLOX)          RGB-D        ✓        ✗      80.5       89.5      96.6      73.4        68.7     94.4       92.9   85.1     4.58
 GDRNPP (BOP22)          RGB-D        ✓        ✗      77.5       87.4      96.6      72.2        67.9     92.6       92.1   83.7     6.26
 PFA [33]                RGB-D        ✓       ✓       79.7       85.0      96.0      67.6        46.9     86.9       88.8   78.7     2.32
 ZebraPose [46]          RGB-D        ✓        ✗      75.2       72.7      94.8      65.2        52.7     88.3       86.6   76.5     0.50
 SurfEmb [43]            RGB-D        ✓       ✓       75.8       83.3      93.3      65.6        49.8     86.7       82.4   76.7     9.05
 CIR [32]                RGB-D        ✓       ✓       73.4       77.6      96.8      67.6        38.1     75.7       89.3   74.1       -
 CosyPose [18]           RGB-D        ✓       ✓       71.4       70.1      93.9      64.7        31.3     71.2       86.1   69.8    13.74
 Koenig-Hybrid [40]      RGB-D        ✓       ✓       63.1       65.5      92.0      43.0        48.3     65.1       70.1   63.9     0.63
 Pix2Pose [45]           RGB-D        ✓        ✗      58.8       51.2      82.0      39.0        35.1     69.5       78.0   59.1     4.84

“Real” means whether the method uses real-world data for training on T-LESS, TUD-L and YCB-V datasets.
“-” denotes the results are unavailable and “*” denotes the method does not use the provided images for training.

RGB-D) and domains (synthetic and real). Specifically, utilizing            Utilizing RGB-D images, our method achieves an average
only synthetic RGB data for training, our method achieves an            recall of 85.6 % with real data and 84.4 % with only synthetic
average recall of 70.2 % w.r.t. the ARBOP metric, exceeding the         data. The BOP22 version of GDRNPP, incorporating [32] for pose
second top-performing method ZebraPose [46] by 3.2 %. Fur-              refinement, significantly outperforms other competitors and wins
thermore, when real data is available on T-LESS, TUD-L, and             “The Overall Best Method” of the BOP 2022 Challenge [34].
YCB-V datasets, the performance increases to 72.8 % without             By adopting the geometry-guided pose refinement module and a
any refinement. Our single model for each dataset (67.8 %) is           more powerful detector [108], the average recall further improves
also comparable with other methods. Noteworthy, our pure RGB-           upon [32] by 1.9 % with real data and 1.7 % without real data,
based method even surpasses the RGB-D based method CosyPose             winning us “The Overall Best Method” of the BOP 2023 Chal-
relying on ICP for refinement (72.8 % v.s. 69.8 %), which is            lenge [35]. Remarkably, the current version of GDRNPP achieves
the previously top-performing method in the BOP 2020 Chal-              state-of-the-art performance on five out of the seven BOP core
lenge [104].                                                            datasets.
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                           13

                        LM-O                                              YCB-V                                      T-LESS

                      RAW                     Ours                      RAW                  Ours                  RAW                  Ours

                       PFA                CosyPose                       PFA              CosyPose                  PFA             CosyPose

                       ITODD                                              IC-BIN                                      HB

                      RAW                     Ours                      RAW                   Ours                 RAW                  Ours

                       PFA                CosyPose                       PFA              CosyPose                  PFA             CosyPose

Fig. 7: Qualitative results on six datasets. We compare our method with PFA [33] and CosyPose [18], maintaining a consistent
experimental setup using depth and real images. For each image, we visualize the predicted 6D poses by rendering the 3D models and
overlaying them onto the grayscale image. Predicted poses are demonstrated in Green contours and ground-truth poses are demonstrated
in Blue contours (if have).

    We highlight the effect of the detector by comparing                           Compared with indirect methods which rely on 2D-3D or 3D-
YOLOX [82] and YOLOv8 [108] and present the results in                         3D correspondence like [24], [45], our method offers a com-
TABLE 5. Even with YOLOX as the detector, GDRNPP still                         pelling combination of real-time performance and accurate pose
exhibits competitive results on the BOP benchmark, which shows                 estimation. This achievement is attributed to our fully learning-
the robustness of the pose estimator. Generally, a more accurate               based strategy, eliminating the time-consuming and inaccurate
detector would lead to more precise pose estimation (YOLOv8                    PnP/RANSAC procedure. Specifically, GDRN runs at the av-
85.6 % v.s. YOLOX 85.1 % with real data). Nevertheless, the                    erage speed of 0.23s per RGB image, gains 97 % and 92 %
prominent improvements of GDRNPP are in the enhancements                       leap forward against SurfEmb [43] (8.89s) and PFA [33] (3.02s)
to the pose estimator and refiner parts rather than the stronger               respectively, which are the two most competitive methods towards
detector.                                                                      GDRN w.r.t. the BOP metric. When considering depth refinement,
    Fig. 7 illustrates some additional qualitative results for LM-             GDRNPP runs slightly slower at 2.67s, but achieves significantly
O, YCB-V, T-LESS, ITODD, IC-BIN, and HB. Compared to                           higher accuracy at 85.6%. Compared to other methods with faster
PFA [33] and CosyPose [18], GDRNPP shows superior perfor-                      inference speeds like ZebraPose (0.5s), Koenig-Hybrid (0.63s),
mance with fewer missing and falsely detected objects, while also              and PFA (2.32s), GDRNPP excels in terms of pose estimation
producing more precise pose estimations. Notably, GDRNPP also                  accuracy.
demonstrates its versatility in intricate scenarios exhibiting clutter,
occlusion, and varying lighting conditions.
                                                                                5      C ONCLUSION
4.6 Runtime Analysis                                                           In this work, we have proposed a geometry-guided and fully
Fig. 8 depicts the average runtime of our algorithm, along with                learning-based pose estimator to eliminate the drawbacks of in-
current state-of-the-art methods in the BOP Challenge leader-                  direct pipelines. To directly regress 6D poses from monocular im-
board. We plot ARBOP (%) versus inference time (second) to                     ages, we exploit the intermediate geometric features regarding 2D-
intuitively show the performance of each method trained with real-             3D correspondences organized regularly as image-like 2D patches,
world data.                                                                    and utilize a learnable 2D convolutional Patch-PnP to replace the
14                                                                            IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

                                                                               R EFERENCES
     ARBOP   80
                       Ours                                                    [1]    A. Collet, M. Martinez, and S. S. Srinivasa, “The MOPED Framework:
                        ★               PFA                                           Object Recognition and Pose Estimation for Manipulation,” Int. J.
                      ZebraPose                              SurfEmb                  Robot. Res., vol. 30, no. 10, pp. 1284–1306, 2011. 1
                      CosyPose                                                 [2]    M. Zhu, K. G. Derpanis, Y. Yang, S. Brahmbhatt, M. Zhang, C. Phillips,
                                                                                      M. Lecce, and K. Daniilidis, “Single Image 3D Object Detection and
             60             CRT-6D                                                    Pose Estimation for Grasping,” in Proc. IEEE Int. Conf. Robot. Automat.
                                                                                      IEEE, 2014, pp. 3936–3943. 1
                        CDPNv2                                                 [3]    J. Tremblay, T. To, B. Sundaralingam, Y. Xiang, D. Fox, and S. Birch-
                                                                                      field, “Deep Object Pose Estimation for Semantic Robotic Grasping of
                                                                                      Household Objects,” in Proc. Conf. Robot Learn., 2018, pp. 306–316. 1
             40                                                                [4]    E. Marchand, H. Uchiyama, and F. Spindler, “Pose Estimation for
                            Pix2Pose                                                  Augmented Reality: a Hands-on Survey,” IEEE Trans. Vis. Comput.
                                                                                      Graph., vol. 22, no. 12, pp. 2633–2651, 2015. 1
                                                                               [5]    F. Tang, Y. Wu, X. Hou, and H. Ling, “3D Mapping and 6D Pose
                                                                                      Computation for Real Time Augmented Reality on Cylindrical Objects,”
                                                                                      IEEE Trans. Circ. Syst. Vid. Tech., 2019. 1
             20                                                                [6]    F. Manhardt, W. Kehl, and A. Gaidon, “ROI-10D: Monocular Lifting of
                        0           2         4       6      8 Runtime(s)
                                                                                      2D Detection to 6D Pose and Metric Shape,” in Proc. IEEE/CVF Conf.
     ARBOP

                                                                                      Comput. Vis. Pattern Recognit., 2019, pp. 2069–2078. 1
             90                                                                [7]    D. Wu, Z. Zhuang, C. Xiang, W. Zou, and X. Li, “6D-VNet: End-To-
                             Ours                                                     End 6-DoF Vehicle Pose Estimation From Monocular RGB Images,” in
                                ★                                                     Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshop, June
                                                                                      2019. 1
             80              PFA                                               [8]    Y. Guo, M. Bennamoun, F. Sohel, M. Lu, and J. Wan, “3d object
                                                  SurfEmb                             recognition in cluttered scenes with local surface features: A survey,”
                      ZebraPose                                                       IEEE Trans. Pattern Anal. Mach. Intell., vol. 36, no. 11, pp. 2270–2287,
                                                                                      2014. 1
                                                            CosyPose           [9]    A. Aldoma, M. Vincze, N. Blodow, D. Gossow, S. Gedikli, R. B. Rusu,
             70
                                                                                      and G. Bradski, “Cad-model recognition and 6dof pose estimation using
                      Koenig-Hybrid                                                   3d cues,” in Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshop. IEEE,
                                                                                      2011, pp. 585–592. 1
                                    Pix2Pose                                   [10]   R. B. Rusu, G. Bradski, R. Thibaux, and J. Hsu, “Fast 3d recognition
             60                                                                       and pose using the viewpoint feature histogram,” in Proc. IEEE Int.
                                                                                      Conf. Robot. Syst. IEEE, 2010, pp. 2155–2162. 1
                                                                               [11]   S. Hinterstoisser, V. Lepetit, S. Ilic, P. Fua, and N. Navab, “Dominant
                                                                                      orientation templates for real-time detection of texture-less objects,” in
             50                                                                       Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. IEEE, 2010,
                  0         2       4     6       8   10    12    14                  pp. 2257–2264. 1
                                                                 Runtime(s)
                                                                               [12]   S. Hinterstoisser, S. Holzer, C. Cagniart, S. Ilic, K. Konolige, N. Navab,
                                                                                      and V. Lepetit, “Multimodal templates for real-time detection of texture-
Fig. 8: Runtime analysis under RGB (upper) and RGB-D                                  less objects in heavily cluttered scenes,” in Proc. IEEE/CVF Int. Conf.
(lower) modality using real data for training. We report the                          Comput. Vis. IEEE, 2011, pp. 858–865. 1
Average Recall (%) of BOP metric w.r.t. the average runtime (sec-              [13]   S. Hinterstoisser, V. Lepetit, S. Ilic, S. Holzer, G. Bradski, K. Konolige,
                                                                                      and N. Navab, “Model based Training, Detection and Pose Estimation
ond) obtained from https://bop.felk.cvut.cz/leaderboards/. Results                    of Texture-less 3D Objects in Heavily Cluttered Scenes,” in Proc. Asian
show that our method gains the highest score while maintaining a                      Conf. Comput. Vis., 2012, pp. 548–562. 1, 4, 8, 9
fast inference speed.                                                          [14]   B. Drost, M. Ulrich, N. Navab, and S. Ilic, “Model globally, match
                                                                                      locally: Efficient and robust 3d object recognition,” in Proc. IEEE/CVF
                                                                                      Conf. Comput. Vis. Pattern Recognit., 2010, pp. 998–1005. 1, 12
                                                                               [15]   J. Vidal, C.-Y. Lin, X. Lladó, and R. Martı́, “A Method for 6D Pose
PnP/RANSAC stage. Furthermore, we harness depth to refine                             Estimation of Free-form Rigid Objects Using Point Pair Features on
                                                                                      Range Data,” Sensors, vol. 18, no. 8, p. 2678, 2018. 1, 12
the pose by establishing 3D-3D dense correspondences between
                                                                               [16]   E. Brachmann, F. Michel, A. Krull, M. Ying Yang, S. Gumhold, and
observed and rendered RGB-D images. With geometric guidance,                          C. Rother, “Uncertainty-driven 6D Pose Estimation of Objects and
the network dynamically removes outliers, thereby enabling us to                      Scenes from a Single RGB Image,” in Proc. IEEE/CVF Conf. Comput.
solve the pose in a differentiable fashion. Our fully learning-based                  Vis. Pattern Recognit., 2016, pp. 3364–3372. 1, 8
                                                                               [17]   S. Peng, Y. Liu, Q. Huang, X. Zhou, and H. Bao, “PVNet: Pixel-wise
pipeline shows competitive performance in various challenging
                                                                                      Voting Network for 6DoF Pose Estimation,” in Proc. IEEE/CVF Conf.
scenarios while maintaining a fast inference speed. In the future,                    Comput. Vis. Pattern Recognit., 2019, pp. 4561–4570. 1, 3
we want to extend our work to more challenging scenarios, such                 [18]   Y. Labbé, J. Carpentier, M. Aubry, and J. Sivic, “CosyPose: Consistent
as the lack of annotated real data [30] and unseen object categories                  Multi-view Multi-object 6D Pose Estimation,” in Proc. Eur. Conf.
                                                                                      Comput. Vis., 2020. 1, 3, 4, 6, 11, 12, 13
or instances [89], [83].
                                                                               [19]   C. Wang, D. Xu, Y. Zhu, R. Martı́n-Martı́n, C. Lu, L. Fei-Fei, and
                                                                                      S. Savarese, “DenseFusion: 6D Object Pose Estimation by Iterative
                                                                                      Dense Fusion,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recog-
                                                                                      nit., 2019, pp. 3343–3352. 1, 3
                                                                               [20]   Y. He, W. Sun, H. Huang, J. Liu, H. Fan, and J. Sun, “Pvn3d: A
ACKNOWLEDGEMENTS                                                                      deep point-wise 3d keypoints voting network for 6dof pose estimation,”
                                                                                      in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020, pp.
This work was supported in part by the National Natural Science                       11 632–11 641. 1, 3
Foundation of China under Grant No. 62406169, and in part                      [21]   Y. He, H. Huang, H. Fan, Q. Chen, and J. Sun, “Ffb6d: A full
                                                                                      flow bidirectional fusion network for 6d pose estimation,” in Proc.
by the China Postdoctoral Science Foundation under Grant No.                          IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2021, pp. 3003–3013.
2024M761673.                                                                          1, 3
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                                          15

[22]   F. Manhardt, D. Arroyo, C. Rupprecht, B. Busam, T. Birdal, N. Navab,       [44]   S. Zakharov, W. Kehl, A. Bhargava, and A. Gaidon, “Autolabeling
       and F. Tombari, “Explaining the Ambiguity of Object Detection and 6D              3d objects with differentiable rendering of sdf shape priors,” in Proc.
       Pose From Visual Data,” in Proc. IEEE/CVF Int. Conf. Comput. Vis.,                IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020, pp. 12 224–
       2019, pp. 6841–6850. 1, 3                                                         12 233. 3
[23]   X. Jiang, D. Li, H. Chen, Y. Zheng, R. Zhao, and L. Wu, “Uni6d:            [45]   K. Park, T. Patten, and M. Vincze, “Pix2Pose: Pixel-Wise Coordinate
       A unified cnn framework without projection breakdown for 6d pose                  Regression of Objects for 6D Pose Estimation,” in Proc. IEEE/CVF Int.
       estimation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.,              Conf. Comput. Vis., 2019, pp. 7668–7677. 3, 12, 13
       2022, pp. 11 174–11 184. 1, 3                                              [46]   Y. Su, M. Saleh, T. Fetzer, J. Rambach, N. Navab, B. Busam, D. Stricker,
[24]   Z. Li, G. Wang, and X. Ji, “CDPN: Coordinates-Based Disentangled                  and F. Tombari, “Zebrapose: Coarse to fine surface encoding for 6dof
       Pose Network for Real-Time RGB-Based 6-DoF Object Pose Estima-                    object pose estimation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
       tion,” in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2019, pp. 7678–7687.            Recognit., 2022, pp. 6738–6748. 3, 11, 12
       1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13                                        [47]   P. Wohlhart and V. Lepetit, “Learning Descriptors for Object Recogni-
[25]   T. Hodan, D. Barath, and J. Matas, “EPOS: Estimating 6D Pose of                   tion and 3D Pose Estimation,” in Proc. IEEE/CVF Conf. Comput. Vis.
       Objects with Symmetries,” in Proc. IEEE/CVF Conf. Comput. Vis.                    Pattern Recognit., 2015, pp. 3109–3118. 3
       Pattern Recognit., 2020, pp. 11 703–11 712. 1, 3, 5, 12                    [48]   M. Sundermeyer, Z.-C. Marton, M. Durner, M. Brucker, and R. Triebel,
[26]   I. Shugurov, S. Zakharov, and S. Ilic, “Dpodv2: Dense correspondence-             “Implicit 3D Orientation Learning for 6D Object Detection from RGB
       based 6 dof pose estimation,” IEEE Trans. Pattern Anal. Mach. Intell.,            Images,” in Proc. Eur. Conf. Comput. Vis., 2018, pp. 699–715. 3, 4
       vol. 44, no. 11, pp. 7417–7435, 2021. 1, 3, 12                             [49]   M. Sundermeyer, M. Durner, E. Y. Puang, Z.-C. Marton, N. Vaskevicius,
[27]   G. Wang, F. Manhardt, J. Shao, X. Ji, N. Navab, and F. Tombari,                   K. O. Arras, and R. Triebel, “Multi-Path Learning for Object Pose
       “Self6D: Self-Supervised Monocular 6D Object Pose Estimation,” in                 Estimation Across Domains,” in Proc. IEEE/CVF Conf. Comput. Vis.
       Proc. Eur. Conf. Comput. Vis., August 2020. 1, 3                                  Pattern Recognit., June 2020. 3
[28]   F. Manhardt, G. Wang, B. Busam, M. Nickel, S. Meier, L. Minciullo,         [50]   Z. Li and X. Ji, “Pose-guided auto-encoder and feature-based refinement
       X. Ji, and N. Navab, “CPS++: Improving Class-level 6D Pose and Shape              for 6-dof object pose regression,” in Proc. IEEE Int. Conf. Robot.
       Estimation From Monocular Images With Self-Supervised Learning,”                  Automat. IEEE, 2020, pp. 8397–8403. 3
       arXiv preprint arXiv:2003.05848, 2020. 1                                   [51]   Y. Xiang, T. Schmidt, V. Narayanan, and D. Fox, “PoseCNN: A Con-
[29]   D. Beker, H. Kato, M. A. Morariu, T. Ando, T. Matsuoka, W. Kehl, and              volutional Neural Network for 6D Object Pose Estimation in Cluttered
       A. Gaidon, “Monocular Differentiable Rendering for Self-Supervised                Scenes,” Robot. Sci. Syst., 2018. 3, 4, 8, 9, 10
       3D Object Detection,” in Proc. Eur. Conf. Comput. Vis., 2020. 1            [52]   T. Cao, F. Luo, Y. Fu, W. Zhang, S. Zheng, and C. Xiao, “Dgecn:
[30]   G. Wang, F. Manhardt, X. Liu, X. Ji, and F. Tombari, “Occlusion-aware             A depth-guided edge convolutional network for end-to-end 6d pose
       self-supervised monocular 6d object pose estimation,” IEEE Trans.                 estimation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.,
       Pattern Anal. Mach. Intell., 2024. 1, 3, 14                                       2022, pp. 3783–3792. 3
[31]   C. Zhang, Z. Cui, Y. Zhang, B. Zeng, M. Pollefeys, and S. Liu, “Holistic   [53]   T. Do, T. Pham, M. Cai, and I. Reid, “LieNet: Real-time Monocular
       3d scene understanding from a single image with implicit representa-              Object Instance 6D Pose Estimation,” in Briti. Mach. Vis. Conf., 2018.
       tion,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., June               3, 4, 9, 10
       2021, pp. 8833–8842. 1                                                     [54]   W. Kehl, F. Manhardt, F. Tombari, S. Ilic, and N. Navab, “SSD-
[32]   L. Lipson, Z. Teed, A. Goyal, and J. Deng, “Coupled iterative refine-             6D: Making RGB-based 3D Detection and 6D Pose Estimation Great
       ment for 6d multi-object pose estimation,” in Proc. IEEE/CVF Conf.                Again,” in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2017, pp. 1521–
       Comput. Vis. Pattern Recognit., 2022, pp. 6728–6737. 2, 4, 6, 7, 11, 12           1529. 3, 4
[33]   Y. Hu, P. Fua, and M. Salzmann, “Perspective flow aggregation for          [55]   F. Manhardt, W. Kehl, N. Navab, and F. Tombari, “Deep Model-based
       data-limited 6d object pose estimation,” in Proc. Eur. Conf. Comput.              6D Pose Refinement in RGB,” in Proc. Eur. Conf. Comput. Vis., 2018,
       Vis. Springer, 2022, pp. 89–106. 2, 3, 11, 12, 13                                 pp. 800–815. 3, 4
[34]   M. Sundermeyer, T. Hodaň, Y. Labbe, G. Wang, E. Brachmann,                [56]   C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “PointNet: Deep learning on
       B. Drost, C. Rother, and J. Matas, “Bop challenge 2022 on detection,              Point Sets for 3D Classification and Segmentation,” in Proc. IEEE/CVF
       segmentation and pose estimation of specific rigid objects,” in Proc.             Conf. Comput. Vis. Pattern Recognit., 2017, pp. 652–660. 3, 9
       IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshop, 2023, pp.          [57]   K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask R-CNN,” in Proc.
       2784–2793. 2, 8, 9, 12                                                            IEEE/CVF Int. Conf. Comput. Vis., 2017, pp. 2961–2969. 3
[35]   T. Hodan, M. Sundermeyer, Y. Labbe, V. N. Nguyen, G. Wang,                 [58]   Y. Di, F. Manhardt, G. Wang, X. Ji, N. Navab, and F. Tombari, “So-
       E. Brachmann, B. Drost, V. Lepetit, C. Rother, and J. Matas, “Bop                 pose: Exploiting self-occlusion for direct 6d pose estimation,” Proc.
       challenge 2023 on detection segmentation and pose estimation of seen              IEEE/CVF Int. Conf. Comput. Vis., pp. 12 376–12 385, 2021. 3
       and unseen rigid objects,” in Proc. IEEE/CVF Conf. Comput. Vis.            [59]   D. Gao, Y. Li, P. Ruhkamp, I. Skobleva, M. Wysocki, H. Jung, P. Wang,
       Pattern Recognit. Workshop, 2024, pp. 5610–5619. 2, 12                            A. Guridi, and B. Busam, “Polarimetric pose prediction,” in Proc. Eur.
[36]   G. Wang, F. Manhardt, F. Tombari, and X. Ji, “Gdr-net: Geometry-                  Conf. Comput. Vis. Springer, 2022, pp. 735–752. 3
       guided direct regression network for monocular 6d object pose estima-      [60]   E. Brachmann and C. Rother, “Learning Less is More-6D Camera
       tion,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2021,              Localization via 3D Surface Regression,” in Proc. IEEE/CVF Conf.
       pp. 16 611–16 621. 2, 3                                                           Comput. Vis. Pattern Recognit., 2018, pp. 4654–4662. 3
[37]   M. Rad and V. Lepetit, “BB8: A Scalable, Accurate, Robust to Partial       [61]   E. Brachmann, A. Krull, S. Nowozin, J. Shotton, F. Michel, S. Gumhold,
       Occlusion Method for Predicting the 3D Poses of Challenging Objects               and C. Rother, “DSAC-Differentiable RANSAC for Camera Localiza-
       without Using Depth,” in Proc. IEEE/CVF Int. Conf. Comput. Vis.,                  tion,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2017,
       2017, pp. 3828–3836. 2                                                            pp. 6684–6692. 3
[38]   B. Tekin, S. N. Sinha, and P. Fua, “Real-Time Seamless Single Shot 6D      [62]   E. Brachmann and C. Rother, “Neural-guided ransac: Learning where
       Object Pose Prediction,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern             to sample model hypotheses,” in Proc. IEEE/CVF Int. Conf. Comput.
       Recognit., 2018, pp. 292–301. 2                                                   Vis., 2019, pp. 4322–4331. 3
[39]   C. Song, J. Song, and Q. Huang, “HybridPose: 6D Object Pose Estima-        [63]   T. Wei, Y. Patel, A. Shekhovtsov, J. Matas, and D. Barath, “Generalized
       tion Under Hybrid Representations,” in Proc. IEEE/CVF Conf. Comput.               differentiable ransac,” in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2023.
       Vis. Pattern Recognit., 2020, pp. 431–440. 3                                      3
[40]   R. König and B. Drost, “A hybrid approach for 6dof pose estimation,”      [64]   E. Jang, S. Gu, and B. Poole, “Categorical reparameterization with
       in Proc. Eur. Conf. Comput. Vis. Springer, 2020, pp. 700–706. 3, 12               gumbel-softmax,” arXiv preprint arXiv:1611.01144, 2016. 3
[41]   Y. Wu, M. Zand, A. Etemad, and M. Greenspan, “Vote from the center:        [65]   B. Chen, A. Parra, J. Cao, N. Li, and T.-J. Chin, “End-to-End Learnable
       6 dof pose estimation in rgb-d images by radial keypoint voting,” in              Geometric Vision by Backpropagating PnP Optimization,” in Proc.
       Proc. Eur. Conf. Comput. Vis. Springer, 2022, pp. 335–352. 3                      IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2020, pp. 8100–8109.
[42]   S. Zakharov, I. Shugurov, and S. Ilic, “DPOD: 6D Pose Object Detector             3, 9, 10
       and Refiner,” in Proc. IEEE/CVF Int. Conf. Comput. Vis., 2019, pp.         [66]   S. G. Krantz and H. R. Parks, The Implicit Function Theorem: History,
       1941–1950. 3                                                                      Theory, and Applications. Springer Science & Business Media, 2012.
[43]   R. L. Haugaard and A. G. Buch, “Surfemb: Dense and continuous                     3
       correspondence distributions for object pose estimation with learnt        [67]   Y. Hu, P. Fua, W. Wang, and M. Salzmann, “Single-Stage 6D Object
       surface embeddings,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern                 Pose Estimation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
       Recognit., 2022, pp. 6749–6758. 3, 11, 12, 13                                     Recognit., 2020, pp. 2930–2939. 3, 8, 9
16                                                                                  IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE

[68]   H. Chen, P. Wang, F. Wang, W. Tian, L. Xiong, and H. Li, “Epro-pnp:           [92]  V. Lepetit, F. Moreno-Noguer, and P. Fua, “EPnP: An Accurate O(n)
       Generalized end-to-end probabilistic perspective-n-points for monoc-                Solution to the PnP Problem,” Int. J. Comput. Vis., vol. 81, no. 2, p.
       ular object pose estimation,” in Proc. IEEE/CVF Conf. Comput. Vis.                  155, 2009. 8, 9
       Pattern Recognit., 2022, pp. 2781–2790. 3                                     [93] T. Hodan, P. Haluza, Š. Obdržálek, J. Matas, M. Lourakis, and X. Zab-
[69]   Y. Li, G. Wang, X. Ji, Y. Xiang, and D. Fox, “DeepIM: Deep Iterative                ulis, “T-less: An rgb-d dataset for 6d pose estimation of texture-less
       Matching for 6D Pose Estimation,” Int. J. Comput. Vis., pp. 1–22, 2019.             objects,” in IEEE Wint. Conf. Appli. Vis., 2017, pp. 880–888. 8
       3, 4, 9                                                                       [94] T. Hodan, F. Michel, E. Brachmann, W. Kehl, A. GlentBuch, D. Kraft,
[70]   S. Iwase, X. Liu, R. Khirodkar, R. Yokota, and K. M. Kitani, “Repose:               B. Drost, J. Vidal, S. Ihrke, X. Zabulis et al., “BOP: Benchmark for 6D
       Fast 6d object pose refinement via deep texture rendering,” in Proc.                Object Pose Estimation,” in Proc. Eur. Conf. Comput. Vis., 2018, pp.
       IEEE/CVF Int. Conf. Comput. Vis., 2021, pp. 3303–3312. 3                            19–34. 8, 9, 10
[71]   Y. Xu, K.-Y. Lin, G. Zhang, X. Wang, and H. Li, “Rnnpose: Recurrent 6-        [95] A. Doumanoglou, R. Kouskouridas, S. Malassiotis, and T.-K. Kim,
       dof object pose refinement with robust correspondence field estimation              “Recovering 6d object pose and predicting next-best-view in the crowd,”
       and pose optimization,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern                in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2016, pp.
       Recognit., 2022, pp. 14 880–14 890. 3                                               3583–3592. 8
                                                                                     [96] B. Drost, M. Ulrich, P. Bergmann, P. Hartinger, and C. Steger, “Intro-
[72]   Z. Zhang, “Iterative point matching for registration of free-form curves
                                                                                           ducing mvtec itodd-a dataset for 3d object recognition in industry,” in
       and surfaces,” Int. J. Comput. Vis., vol. 13, no. 2, pp. 119–152, 1994. 3,
                                                                                           Proc. IEEE/CVF Int. Conf. Comput. Vis. Workshop, 2017, pp. 2200–
       11
                                                                                           2208. 8
[73]   J. Zhang, Y. Yao, and B. Deng, “Fast and robust iterative closest point,”     [97] R. Kaskman, S. Zakharov, I. Shugurov, and S. Ilic, “HomebrewedDB:
       IEEE Trans. Pattern Anal. Mach. Intell., vol. 44, no. 7, pp. 3450–3466,             RGB-D dataset for 6d pose estimation of 3d objects,” in Proc.
       2022. 3                                                                             IEEE/CVF Int. Conf. Comput. Vis. Workshop, 2019. 8
[74]   D. Chetverikov, D. Svirko, D. Stepanov, and P. Krsek, “The trimmed            [98] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
       iterative closest point algorithm,” in Proc. Int. Conf. Pattern Recog.,             T. Killeen, Z. Lin, N. Gimelshein, L. Antiga et al., “PyTorch: An
       vol. 3. IEEE, 2002, pp. 545–548. 3                                                  Imperative Style, High-performance Deep Learning Library,” in Proc.
[75]   S. Bouaziz, A. Tagliasacchi, and M. Pauly, “Sparse iterative closest                32nd Int. Conf. Neural Inf. Process. Syst., 2019, pp. 8026–8037. 8
       point,” in Comput. Graph. Forum, vol. 32, no. 5. Wiley Online Library,        [99] L. Liu, H. Jiang, P. He, W. Chen, X. Liu, J. Gao, and J. Han, “On the
       2013, pp. 113–123. 3                                                                Variance of the Adaptive Learning Rate and Beyond,” in Proc. Int. Conf.
[76]   D. Chetverikov, D. Stepanov, and P. Krsek, “Robust euclidean alignment              Learn. Representations, April 2020. 8
       of 3d point sets: the trimmed iterative closest point algorithm,” Image       [100] M. Zhang, J. Lucas, J. Ba, and G. E. Hinton, “Lookahead Optimizer:
       and Vis. Comput., vol. 23, no. 3, pp. 299–309, 2005. 3                              k Steps Forward, 1 Step Back,” in Proc. 32nd Int. Conf. Neural Inf.
[77]   S. Du, N. Zheng, S. Ying, and J. Liu, “Affine iterative closest point al-           Process. Syst., 2019, pp. 9593–9604. 8
       gorithm for point set registration,” Pattern Recognition Letters, vol. 31,    [101] H. Yong, J. Huang, X. Hua, and L. Zhang, “Gradient-Centralization: A
       no. 9, pp. 791–799, 2010. 3                                                         New Optimization Technique for Deep Neural Networks,” in Proc. Eur.
[78]   B. Wen, C. Mitash, B. Ren, and K. E. Bekris, “se (3)-tracknet: Data-                Conf. Comput. Vis., 2020. 8
       driven 6d pose tracking by calibrating image residuals in synthetic           [102] F. H. Ilya Loshchilov, “SGDR: Stochastic Gradient Descent with Warm
       domains,” in Proc. IEEE Int. Conf. Robot. Syst. IEEE, 2020, pp.                     Restarts,” in Proc. Int. Conf. Learn. Representations, 2017. 8
       10 367–10 373. 3                                                              [103] I. Loshchilov and F. Hutter, “Decoupled weight decay regularization,”
[79]   Z. Teed and J. Deng, “Raft: Recurrent all-pairs field transforms for                in Proc. Int. Conf. Learn. Representations, 2019. 8
       optical flow,” in Proc. Eur. Conf. Comput. Vis. Springer, 2020, pp.           [104] T. Hodan, M. Sundermeyer, B. Drost, Y. Labbe, E. Brachmann,
       402–419. 4, 7                                                                       F. Michel, C. Rother, and J. Matas, “BOP Challenge 2020 on 6D Object
                                                                                           Localization,” Proc. Eur. Conf. Comput. Vis. Workshop, 2020. 8, 9, 10,
[80]   S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards Real-
                                                                                           12
       Time Object Detection with Region Proposal Networks,” in Proc. 28th
                                                                                     [105] T. Hodaň, J. Matas, and Š. Obdržálek, “On Evaluation of 6D Object
       Int. Conf. Neural Inf. Process. Syst., 2015. 4, 6, 10
                                                                                           Pose Estimation,” Proc. Eur. Conf. Comput. Vis. Workshop, pp. 606–
[81]   Z. Tian, C. Shen, H. Chen, and T. He, “FCOS: Fully Convolutional                    619, 2016. 9
       One-Stage Object Detection,” in Proc. IEEE/CVF Int. Conf. Comput.             [106] J. Shotton, B. Glocker, C. Zach, S. Izadi, A. Criminisi, and A. Fitzgib-
       Vis., 2019, pp. 9627–9636. 4, 6                                                     bon, “Scene Coordinate Regression Forests for Camera Relocalization
[82]   Z. Ge, S. Liu, F. Wang, Z. Li, and J. Sun, “Yolox: Exceeding yolo series            in RGB-D Images,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
       in 2021,” arXiv preprint arXiv:2107.08430, 2021. 4, 6, 10, 12, 13                   Recognit., June 2013. 9
[83]   K. Park, A. Mousavian, Y. Xiang, and D. Fox, “LatentFusion: End-to-           [107] B. Wen, W. Yang, J. Kautz, and S. Birchfield, “FoundationPose: Unified
       End Differentiable Reconstruction and Rendering for Unseen Object                   6d pose estimation and tracking of novel objects,” in Proc. IEEE/CVF
       Pose Estimation,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern                      Conf. Comput. Vis. Pattern Recognit., 2024. 11
       Recognit., 2020, pp. 10 710–10 719. 4, 9, 14                                  [108] G. Jocher, A. Chaurasia, and J. Qiu, “Ultralytics yolov8,” 2023.
[84]   Y. Zhou, C. Barnes, J. Lu, J. Yang, and H. Li, “On the Continuity                   [Online]. Available: https://github.com/ultralytics/ultralytics 12, 13
       of Rotation Representations in Neural Networks,” in Proc. IEEE/CVF            [109] P. Castro and T.-K. Kim, “Crt-6d: Fast 6d object pose estimation with
       Conf. Comput. Vis. Pattern Recognit., 2019, pp. 5745–5753. 4                        cascaded refinement transformers,” in IEEE Wint. Conf. Appli. Vis.,
[85]   A. Kundu, Y. Li, and J. M. Rehg, “3D-RCNN: Instance-level 3D Object                 2023, pp. 5746–5755. 12
       Reconstruction via Render-and-Compare,” in Proc. IEEE/CVF Conf.               [110] Y. Wu, A. Javaheri, M. Zand, and M. Greenspan, “Keypoint cascade
       Comput. Vis. Pattern Recognit., 2018, pp. 3559–3568. 4                              voting for point cloud based 6dof pose estimation,” in Int. Conf. 3D Vis.
[86]   E. Brachmann, A. Krull, F. Michel, S. Gumhold, J. Shotton, and                      IEEE, 2022, pp. 176–186. 11, 12
       C. Rother, “Learning 6D Object Pose Estimation Using 3D Object                [111] M. Sundermeyer, Z.-C. Marton, M. Durner, M. Brucker, and R. Triebel,
       Coordinates,” in Proc. Eur. Conf. Comput. Vis., 2014, pp. 536–551.                  “Implicit 3d orientation learning for 6d object detection from rgb
       4, 8                                                                                images,” in Proc. Eur. Conf. Comput. Vis., 2018, pp. 699–715. 11
[87]   A. Simonelli, S. Rota Bulo, L. Porzi, M. Lopez-Antequera, and                 [112] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisser-
       P. Kontschieder, “Disentangling Monocular 3D Object Detection,” in                  man, “The pascal visual object classes (voc) challenge,” Int. J. Comput.
       Proc. IEEE/CVF Int. Conf. Comput. Vis., 2019. 4, 9                                  Vis., pp. 303–338, 2010. 11
                                                                                     [113] H. Zhang, C. Wu, Z. Zhang, Y. Zhu, H. Lin, Z. Zhang, Y. Sun, T. He,
[88]   Y. Wu and K. He, “Group Normalization,” in Proc. Eur. Conf. Comput.
                                                                                           J. Mueller, R. Manmatha et al., “Resnest: Split-attention networks,” in
       Vis., 2018, pp. 3–19. 5
                                                                                           Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., 2022, pp. 2736–
[89]   H. Wang, S. Sridhar, J. Huang, J. Valentin, S. Song, and L. J. Guibas,              2746. 11
       “Normalized Object Coordinate Space for Category-Level 6D Object              [114] Z. Liu, H. Mao, C.-Y. Wu, C. Feichtenhofer, T. Darrell, and S. Xie, “A
       Pose and Size Estimation,” in Proc. IEEE/CVF Conf. Comput. Vis.                     convnet for the 2020s,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
       Pattern Recognit., 2019. 5, 14                                                      Recognit., 2022, pp. 11 976–11 986. 11
[90]   J. Redmon and A. Farhadi, “YOLOv3: An Incremental Improvement,”               [115] K. He, X. Zhang, S. Ren, and J. Sun, “Deep Residual Learning for
       arXiv preprint arXiv:1804.02767, 2018. 6, 10                                        Image Recognition,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
[91]   A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, “YOLOv4: Op-                         Recognit., 2016, pp. 770–778. 11
       timal Speed and Accuracy of Object Detection,” arXiv preprint
       arXiv:2004.10934, 2020. 6, 10
Liu et al.: GDRNPP: A Geometry-guided and Fully Learning-based Object Pose Estimator                                                               17

                        Xingyu Liu is currently a Ph.D. student in the                                Zhigang Li received the B.E. degree in the
                        Department of Automation, at Tsinghua Univer-                                 School of Automation Science and Electrical En-
                        sity supervised by Xiangyang Ji. She received                                 gineering from Beihang University, in 2015, and
                        her B.E. degree from the Department of Automa-                                the PhD degree in the Department of Automation
                        tion, Beihang University, Beijing, China, in 2021.                            from Tsinghua University, in 2021. His research
                        Her research interests lie in 3D computer vision                              interests are computer vision, deep learning,
                        and robotic vision.                                                           and object pose estimation.

                        Ruida Zhang received the B.E. degree from the
                        Department of Automation, Tsinghua University,
                        Beijing, China, in 2021. He is working toward a
                        Ph.D. degree at Tsinghua University, under the
                        supervision of Xiangyang Ji. His research inter-
                        ests include 3D computer vision and robotics.

                        Chenyangguang Zhang is currently a M.S. stu-
                        dent in the Department of Automation, at Ts-
                        inghua University, supervised by Xiangyang Ji.
                        He received a B.E. degree from the Depart-
                        ment of Automation, Tsinghua University, Bei-
                        jing, China, in 2022. His research interests lie in
                        3D computer vision and deep learning.
                                                                                                      Xiangyang Ji received the B.E. degree in ma-
                                                                                                      terials science and the M.S. degree in computer
                                                                                                      science from the Harbin Institute of Technology,
                                                                                                      Harbin, China, in 1999 and 2001, respectively,
                                                                                                      and the Ph.D. degree in computer science from
                                                                                                      the Institute of Computing Technology, Chinese
                                                                                                      Academy of Sciences, Beijing, China. He joined
                                                                                                      Tsinghua University, Beijing, in 2008, where he
                                                                                                      is currently a Professor at the Department of
                        Gu Wang received B.E. and Ph.D. degrees from
                                                                                                      Automation, School of Information Science and
                        Department of Automation, Tsinghua University,
                                                                                                      Technology. He has authored more than 200
                        Beijing, China, in 2016 and 2022, respectively.
                                                                               refereed conference and journal papers. His current research interests
                        He was a visiting scholar at Technical University
                                                                               include signal processing, computer vision and computational photogra-
                        of Munich from 2019 to 2020. He was a Doctoral
                                                                               phy.
                        Management Trainee at JD.com from 2022 to
                        2023, working on calibration, localization and
                        mapping in autonomous driving. He is currently a
                        postdoctoral researcher at Tsinghua University,
                        Beijing. His research interests include 3D com-
                        puter vision, and vision in robotics.

                       Jiwen Tang received the B.E. degree from
                       Wuhan University, Wuhan, China, in 2014 and
                       the Ph.D. degree from Aerospace Information
                       Research Institute, Chinese Academy of Sci-
                       ences, Beijing, China, in 2021. From 2021 to
                       2024, he was a postdoctoral fellow with the
                       Department of Automation, Tsinghua University,
                       Beijing, China. In 2024, he joined China Uni-
                       versity of Geosciences Beijing, where he is cur-
                       rently a lecturer with the School of Information
                       Engineering. His research interests lie in com-
puter vision and deep learning.
