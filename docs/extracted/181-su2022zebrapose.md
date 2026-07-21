---
source_id: 181
bibtex_key: su2022zebrapose
title: ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation
year: 2022
domain_theme: Pose 6D
verified_pdf: 181_ZebraPose.pdf
char_count: 92036
---

ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation

                                                          Yongzhi Su1,2*              Mahdi Saleh3*         Torben Fetzer2             Jason Rambach1
                                                          Nassir Navab3              Benjamin Busam3       Didier Stricker1,2        Federico Tombari3,4
                                                 1                                                                                               2
                                                     German Research Center for Artificial Intelligence (DFKI)                                       TU Kaiserslautern
                                                                    3                                                               4
                                                                      Technische Universität München                                  Google
arXiv:2203.09418v2 [cs.CV] 29 Mar 2022

                                                             {yongzhi.su; jason.rambach; torben.fetzer; didier.stricker}@dfki.de
                                                                  {m.saleh; b.busam; nassir.navab}@tum.de, tombari@in.tum.de

                                                                      Abstract

                                            Establishing correspondences from image to 3D has
                                         been a key task of 6DoF object pose estimation for a long                                                                             …
                                         time. To predict pose more accurately, deeply learned dense
                                         maps replaced sparse templates. Dense methods also im-
                                         proved pose estimation in the presence of occlusion. More                                       3D Hierarchical groupings
                                         recently researchers have shown improvements by learning                                                                       0110
                                         object fragments as segmentation. In this work, we present
                                         a discrete descriptor, which can represent the object surface
                                         densely. By incorporating a hierarchical binary grouping,
                                         we can encode the object surface very efficiently. Moreover,
                                         we propose a coarse to fine training strategy, which enables
                                         fine-grained correspondence prediction. Finally, by match-                   Object CAD model                        Binary Coding
                                         ing predicted codes with object surface and using a PnP
                                         solver, we estimate the 6DoF pose. Results on the public              Figure 1. ZebraPose assigns a discrete code to each surface ver-
                                                                                                               tex hierarchically. We project the code as binary black and white
                                         LM-O and YCB-V datasets show major improvement over
                                                                                                               values (top) and learn them using deep neural networks. Our bi-
                                         the state of the art w.r.t. ADD(-S) metric, even surpassing
                                                                                                               nary descriptor allows one-to-one correspondence for the problem
                                         RGB-D based methods in some cases.                                    of 6DoF object pose efficiently.

                                         1. Introduction                                                       computer vision. While finding correspondences across the
                                                                                                               same domain is more straightforward, estimating the 6DoF
                                             Augmented reality and robotics are two of the main ap-
                                                                                                               object pose requires 2D-3D correspondences. In earlier ob-
                                         plication fields of 3D computer vision. In many augmented
                                                                                                               ject pose estimation research, depth maps came to help to
                                         reality applications, the location and pose of an object of in-
                                                                                                               match image pixels to 3D surface points [28, 65]. Due to
                                         terest has to be determined at a high precision [46,55]. Sim-
                                                                                                               cost and setup complications, the detection of 6DoF pose
                                         ilarly, object grasping and manipulation is needed for many
                                                                                                               without depth information can be advantageous. However,
                                         robotic applications (e.g. automatic manufacturing [51], co-
                                                                                                               RGB approaches typically achieve a lower accuracy with
                                         operative assistance [9, 21]), and also demands accurate 6
                                                                                                               respect to their depth-based counterparts [16, 26].
                                         Degree-of-Freedom (6DoF) object pose information. As the
                                                                                                                  Driven by the recent developments in deep learning and
                                         crucial element in both application domains, estimating the
                                                                                                               Convolutional Neural Networks (CNNs), various methods
                                         6DoF object pose has received increasing attention from the
                                                                                                               were proposed, which make 6DoF pose estimation from
                                         computer vision research community.
                                                                                                               a single RGB image feasible [10, 34, 54, 62, 70]. In a
                                             The correspondence problem is a classical problem in
                                                                                                               correspondence-based setting, to estimate the object pose,
                                            * The authors contributed equally to this paper                    Perspective-n-Points (PnP) algorithms require at least 4 2D-
                                            Code: https://github.com/suyz526/ZebraPose                         3D point matches [39]. Therefore, sparse methods are ap-

                                                                                                           1
plied to extract points of interest [48, 53]. However such                 matically adjust the weights of each code position.
methods might fail to find object landmarks under view-
point changes, occlusion, or lack of texture. With the suc-           Extensive experiments on LM-O [3] and YCB-V [11]
cess of deep neural networks in image synthesis problems,             datasets show that our proposed approach achieves state of
researchers use such tools to generate dense correspondence           the art results.
maps. For instance, several methods learn UV [72] or UVW
[49, 68] values in object local coordinates. Since the net-           2. Related Work
work produces dense smooth results, certain low-level ge-                We limit our in-depth discussion of related work to the
ometry is lost. Moreover, neural networks tend to achieve a           most relevant methods to our work, i.e. RGB-based 6DoF
higher performance in classification tasks [34].                      pose estimation, and object surface encoding techniques.
    To this aim, we propose a dense correspondence pipeline
that combines the concepts of handcrafted features and im-            2.1. RGB-based 6DoF Pose Estimation
age segmentation in a hierarchical fashion for RGB-based
                                                                          Traditional Methods. With the development of the
6DoF pose estimation. In order to design a descriptor that
                                                                      feature descriptor [43], the object pose problem could be
encodes surfaces efficiently, we use the binary numeral sys-
                                                                      solved by feeding estimated 2D-3D correspondences into a
tem. Binary-based descriptors are applied in ORB [57] and
                                                                      RANSAC/PnP framework. However, dealing with texture-
are still in use in robust SLAM applications [12]. In our
                                                                      less objects remained a challenge. To overcome the lack
work, we split the surface into halves in multiple iterations
                                                                      of keypoints, Hinterstoisser et al. [25] proposed to utilize
and define our vertex encoding by stacking the assigned
                                                                      the image gradient information and formulate the pose es-
group labels. By leveraging a hierarchical discrete represen-
                                                                      timation task within a template matching pipeline. Later
tation, we guarantee a compact mapping and simple learn-
                                                                      advances [5] avoided the template searching time by apply-
ing objective as a multi-label classification problem [29,34].
                                                                      ing a statistical learning-based framework to regress object
Moreover, learning how to encode a full sequence at once
                                                                      coordinates and object labels jointly. However, the accu-
might be challenging for neural networks. Therefore, we
                                                                      racy that handcrafted methods can achieve is far from that
propose a coarse to fine learning scheme. By design, our
                                                                      of deep learning methods nowadays.
encodings on the coarse levels are continuously shared in
                                                                          End-to-End Methods. PoseNet [35] was the first work
wider object regions. As the network learns to differentiate
                                                                      that attempted to regress the camera viewpoint with a CNN.
coarse splits, we focus on finer encoding positions. With a
                                                                      Following works usually concatenated an object detector
coarse to fine loss and training strategy, we then manage to
                                                                      with the pose regression, making multi-object pose esti-
predict fine-grained surface correspondences.
                                                                      mation possible [70]. Finding a suitable rotation represen-
    In contrast to previous works where there is no guaran-
                                                                      tation for pose regression was a problem at that time and
teed putative correspondence [49,50,68], our encoding pro-
                                                                      typical rotation parametrization did not populate Euclidean
motes direct pixel-to-surface matching just by means of a
                                                                      spaces [8]. SSD6D [34] avoided complex parameters by
look-up table. With a simple matching and PnP-RANSAC
                                                                      discretization of the rotation space thus treating the rota-
scheme of Progressive-X [2], we outperform the state of the
                                                                      tion estimation as a classification problem. Zhou et.al [74]
art in 6DoF pose on the most commonly used benchmarks
                                                                      proposed a continuous 6-dimensional rotation representa-
w.r.t. ADD(-S) metric.
                                                                      tion that shows advantages over quaternions [44, 45] or Lie
    In summary, we propose ZebraPose, a two-stage RGB-
                                                                      algebra [20,61] parametrization for neural network training.
based approach that defines the matching of dense 2D-3D
                                                                      This representation is utilized in several direct regression
correspondence as a hierarchical classification task. We di-
                                                                      works [19, 37, 67].
vide the general two-stage approach for 6DoF object pose
                                                                          In parallel, several efforts have been made to integrate
estimation into three components: 1) assigning a unique de-
                                                                      RANSAC and PnP modules to pose learning frameworks.
scriptor to the 3D vertex; 2) predicting a dense correspon-
                                                                      [4,6,7] propose differentiable RANSAC variants, which are
dence between the 2D pixels and 3D vertices; 3) solving the
                                                                      not applicable to object pose estimation as they require a
object pose using the predicted correspondences. We can
                                                                      good initialization and complex training strategy. [30] pro-
summarize our proposed contributions in this paper related
                                                                      poses a network to solve the PnP problem, with a loss func-
to the first two components:
                                                                      tion reflecting pose metrics. At the same time, a new branch
   • A novel coarse to fine surface encoding method as-               of methods has been developed with the growth of neural
     signing the dense vertex descriptor in an efficient way,         renderers [15, 33, 42]. [32] is able to define the loss accord-
     which also fully exploits traditional outlier filters used       ing to the texture colour on pixel level. [59, 66] used a dif-
     in computer vision task.                                         ferentiable depth map and achieved self-supervised network
                                                                      fine-tuning with unlabeled RGB-D data. In an effort to com-
   • A novel hierarchical training loss and strategy to auto-         bine correspondence-based methods with direct regression

                                                                  2
of 6DoF parameters, [67] used correspondence maps as an              that predict local coordinates space [68, 72] in 2D or 3D
intermediate geometric representation to regress the pose.           grid, we encode the object surface in a coarse to fine man-
[19] further enhances [67] by employing self-occlusion in-           ner. Moreover, unlike EPOS [29] that divides the object
formation that provides richer information to predict the ob-        surface into multiple coarse bins at once, we divide the ob-
ject pose with the predicted 2D-3D correspondences.                  ject surface iteratively until the fragments are fine enough
    Indirect Methods with Deep Learning. While end-to-               to define the unique 3D corresponding point. This allows
end methods have evolved through time by integrating dif-            for gradual refinement of the correspondence through the
ferentiable modules, the performance of such methods are             hierarchical levels.
normally below geometrical and indirect methods. Combin-
ing learning features and geometrical fitting, [69] uses met-        3. Method: ZebraPose
ric learning to learn an implicit pose representation through
                                                                        In this section, we present our approach for the problem
triplet loss and finally looks for nearest neighbors in pose
                                                                     of 6DoF object pose, which involves the entire process from
space. AAE [62] learns to generate a latent vector based on
                                                                     our surface encoding to the final pose estimation.
the visual information of the object in discrete viewpoints.
At inference stage, the rotation is obtained by comparing            3.1. Coarse to Fine Surface Encoding
the latent code with the pre-generated rotation-latent code
                                                                        Given a surface CAD model of an object and its vertices
lookup table. The rest of the indirect methods usually esti-
                                                                     vi ∈ R3 , where i stands for the vertex id, we want to rep-
mate the 2D-3D correspondence, and solve the object pose
                                                                     resent each vi with vertex code ci ∈ Nd , where d is the
using RANSAC/PnP. BB8 [53] firstly defines the 3D ob-
                                                                     length of the vertex code. We need to define such encoding
ject bounding box corners as the keypoints and PVNet [50]
                                                                     based on vertices’ position relative to the given 3D object
reaches high recall rate in LM [27] dataset by predicting the
                                                                     surface to enable coarse to fine learning. To enable this, we
keypoints with a dense pixel-wise voting for sampled key-
                                                                     construct our codes in a non-decimal numeral system.
points on the object. The main drawback of such sparse
                                                                        Defining our encoding in a numeral system with lower
2D-3D correspondence methods is that the prediction of
                                                                     radix makes the representation very efficient and provides
keypoints in the occluded area lacks in accuracy. Hybrid-
                                                                     easier grounds for coarse to fine grouping of the points. For
Pose [60] proposed to leverage multiple geometric infor-
                                                                     a code of length d, we perform d iterations of grouping of
mation to tackle this issue while other methods [29, 49, 72]
                                                                     the vertices. The collection of groups Gj in the j-th iter-
predict pixel-wise dense 2D-3D correspondences.
                                                                     ation (j ∈ {0, ..., d} ⊂ N) consist of rj groups. G0 de-
2.2. Surface Encoding                                                fines the initial group, including only one group, i.e. the
                                                                     entire object vertices. Gj with j > 1 is obtained by split-
    The binary surface encoding technique has been success-          ting each group in Gj−1 into r groups. In a grouping itera-
fully used in the field of structured light reconstruction for       tion, each vertex vi is assigned with a class id mi,j , where
many years [47,52,58,64]. For this purpose, a video projec-          mi,j ∈ {0, ..., r − 1} ⊂ N based on the group it belongs
tor illuminates the scene with several successively refined          to in the j-th grouping. Finally, each vertex is assigned to
binary fringe patterns. The composition of the different             a vertex code with d digits by stacking the class id of each
stripe patterns provides an encoding of the surface points.          grouping operation. This representation is stored and fixed
Surface coding using multiple classification problems has            for every 3D object. The vertices in each group share the
proven to be highly reliable and competitive [22]. Since             same code. We build the lookup table to map a code to
neural networks are ideally suited for solving classification        the centroid of the each group in Gd , which is further used
problems, a transfer of the approach as we presented in this         to build 2D-3D correspondence and solve the pose as de-
work constitutes a logical step.                                     scribed in Sec. 3.6. In this paper, we used k-means for the
    In pose estimation domain, to estimate the dense 2D-3D           grouping, more details are in Sec. 4.1. We illustrate this pro-
correspondence, each 3D corresponding point must be as-              cess in Fig. 2 with r = 2 and break down the CAD model
signed a unique descriptor. Pix2Pose [49] simply treats the          surface into discrete and equally sized groups.
3D vertex coordinates as this descriptor. DPOD [72] tex-
tures the object with a 2-channel UV-map with discrete val-          3.2. Choice of the Radix for Vertex Code
ues to learn the correspondences. EPOS [29] divides the                 Following our grouping described in Sec. 3.1, we would
object surface into multiple fragments, and estimates the            have K total number of classes, where K = rd . In a classi-
corresponding points by combining fragment segmentation              fication problem we learn these maps using o logits, where
and local fragments coordinates prediction. Although most            o = r ·d. To minimize the number of outputs while learning
of these encodings are limited to local object coordinates,          the most number of classes we have:
we propose a method that learns dense 2D-3D correspon-
dence through a handcrafted code. Compared to methods                    omin = min r · d = min r · logr K = 2 · log2 K.        (1)
                                                                                   r            r

                                                                 3
                 𝐺1            𝐺2              𝐺3   𝐺4 … 𝐺𝑑   Input Image
                                                                                                                               3D Surface
                                                                                                                               Code Table
  𝐺0

 Original mesh

                                                                                                                                  Matching + PnP   𝑅, 𝑡
                                                               2D Detector
                                                                                                                          Predicted Code

                                                                                                                                    …
                                                              Cropped ROI

                  3D surface code generation                                       Code prediction and 6DoF pose estimation

Figure 2. Left: Our hierarchical encoding is defined by grouping surface vertices in several iterations. In each iteration, object vertices are
split into equally sized groups. In a binary setting, vertices are classified into two groups, 0 (white) and 1 (black). This process happens
offline and the generated mapping between vertex code and the corresponding 3D vertex is stored in a look-up table. Right: Our training
framework uses a detector to crop the object ROI and predicts a multi-layer code using a fully convolutional neural network. The predicted
code is then matched to the 3D surface vertex and passed to RANSAC and PnP modules for pose estimation.

The best positive integer choice of r to minimize the num-                   encoder-decoder network generates d + 1 outputs with a
ber of network layers are 2 and 4. Since a value is classified               single decoder. We round the final output probabilities to
either as positive or negative, we do not need to use the cross              represent our discrete vertex codes.
entropy loss with 2 explicit output layers for the binary clas-                 The entire process from input images to the predicted
sification. So we can reach log2 K as the optimal number of                  pose is presented in Fig. 2. To predict the code per pixel in
output layers with r = 2.                                                    the frame with fine granularity, we process only a Region of
    Besides the advantages of reduced GPU memory re-                         Interest (ROI) around object pixels. Following the pipeline
quirement, we show later in the ablation study (see Sec. 4.2)                similar to [37, 41, 67], we focus on the object pose and use
that using the binary vertex code yields the most accurately                 the available 2D detector predictions to find the ROIs. We
predicted pose. Thus we choose a binary base for the vertex                  crop and resize the ROI from the prediction to a fixed di-
code.                                                                        mension H×W, and apply the exact process to the target
                                                                             vertex code maps during training. Our goal is to predict
3.3. Rendering the Training Labels                                           multiple labels per frame in the ROI.
    Each object pixel in the image corresponds to a 3D object
vertex. The network predicts the class id that is assigned to                3.5. Hierarchical Learning
this vertex in each grouping operation. Therefore, we still                      Predicting correspondences directly from object pixels is
need to render the class id into the 2D image plane with a                   a fine-grained task. On the other side, deep neural networks
given pose for the training. For this purpose, we transfer the               are commonly used for coarse level predictions. This means
class id of vertices into the class id of the mesh faces using               features predicted per pixel are very similar in a small vicin-
the following criteria: if two vertices of a face have the same              ity. As our encoding is also hierarchical by design, we learn
class id, the face is assigned with this class id. Otherwise,                the codes in a coarse to fine manner. Therefore, the predic-
the face has the class id of its first vertex. We repeat this                tions are learned in different stages, from coarse groupings
rendering process for d times until the training label class                 to fine ones. We use an error histogram for each position
id for each grouping is generated.                                           on hierarchical level and weight our Hamming-based loss
                                                                             given the error to design this.
3.4. Network Architecture
                                                                                 Mask loss. Firstly, we predict the visible mask to seg-
   In Sec. 3.2 we justify our choice of r = 2. In this regard,               ment the object area from the background. Here, we simply
our goal is to classify 2d regions with only d binary values.                pass the predicted probability to the sigmoid function and
   During training, we use the object pose annotations to                    use L1 loss as Lmask . It is worth noting, for the binary ver-
render the labels as layered black and white maps to im-                     tex code prediction in the following, we only calculate loss
age coordinates. This way, our objective learning maps are                   of the pixels within the predicted object mask.
d + 1 binary labels (d for the binary vertex code and 1 for                      Hamming distance: The CNN outputs the binary ver-
the object mask) for code and visible mask prediction. An                    tex code probabilities p̂ ∈ Rd for a pixel within a ROI, we

                                                                       4
obtain the predicted discrete binary code b̂ by rounding p̂.                 Total loss to train the CNN. We weight the Lmask and
Given b̂ and its known ground truth binary vertex code b,                 Lhier with a hyper-parameter α (α set as 0 for pixels pre-
the Hamming distance Hamm is defined by counting the                      dicted as background), the total per pixel loss can be math-
number of bits b̂ which are different from b. This formula-               ematically expressed as
tion does not favor any of the positions and calculates the
error without considering any hierarchical information ex-                               Ltotal = Lmask + α · Lhier .               (6)
plicitly. As a common practice in deep learning, we use
                                                                          3.6. Pose estimation
binary cross-entropy as an activation function for the dis-
tance:                                                                        In previous sections, we discussed how to generate our
                  d                                                       descriptor and learn to predict them using a fully convo-
                                                                          lutional neural network. Now we incorporate the predicted
                  X
  Hamm(b, p̂) =         bj log pˆj + (1 − bj ) log(1 − pˆj ), (2)
                  j=1                                                     code and visible mask and the reference 3D model encoding
                                                                          to match correspondences. Different from common dense
where bj stands for the j-th bit in b (the j-th bit is generated          correspondences such as [49,67,68], this compact represen-
in the j-th vertices grouping).                                           tation also enables a bijective correspondence between the
    Active bits. Lower bits in binary vertex code b hold                  surface vertices and the descriptor space. That means, un-
coarse correspondences, and higher bits define finer esti-                like the regressed 3D point which can be off the object sur-
mates. During the initial training phase, the network fo-                 face, our estimated 3D correspondences always refers to a
cuses on learning the coarse splits and has a higher error on             vertex on the object model, which eases the matching stage
fine bits. Therefore we adaptively weight the coarse bits by              for the pose solver. For the matching, we use a look-up table
looking at the histogram of error of all bits. As the train-              that extracts the corresponding 2D and 3D points. Follow-
ing proceeds and coarser predictions become more robust,                  ing that, we use Progressive-X [2] solver to calculate the
finer bits are induced with more weights. We define our his-              rotation R and translation t.
togram at training step t by looking at the error at different
bits:                                                                     4. Experiments
                              t                       t−1
 Hj (t) = avg(λ(btj − bˆj ) + (1 − λ)(bt−1
                                       j   − bˆj            )), (3)           In this section, we firstly introduce the implementation
          t                                                               details, the datasets and metrics used for the evaluation.
where bˆj defines the predicted binary vertex code bˆj at                 Subsequently, we present ablation study experiments on the
training step t, and λ is a constant. With the avg operator,              LM-O [5] dataset. Finally, we compare our experimental
we get the error ratio by calculating the average difference              results with state of the art methods on the LM-O [5] and
              t
in btj and bˆj of all pixels within the predicted object mask             YCB-V [70] datasets. Please refer to supplementary mate-
in a mini-batch. During training we update the histogram                  rials for more qualitative results.
given the previous histogram in training step t − 1 and the
current error histogram. We show how to define a hierarchi-               4.1. Experiments Setup
cal loss based on the histogram in the following.                             Implementation Details. In order to have the same
    Hierarchical loss. We compute a weighting coefficient                 number of classes as DPOD [72] (K = 2562 ), we firstly
based on the error histogram, and use it on top of a Ham-                 upsample the mesh by subdivision of each face using the
ming distance to form our hierarchical loss with                          edge’s midpoint [14] until the mesh has more than 2562 ver-
                                                                          tices. Subsequently, we group the 3D vertices of the object
       wj (t) = exp(σ · min{Hj (t), 0.5 − Hj (t)}),             (4)
                                                                          model as we described in Sec. 3.1 with r = 2 and d = 16.
where the function w uses an exponential term to softly de-               After several iterations of the grouping operation, a group
fine a weight for n-th bit at training step t, σ is a constant.           could contain fewer points than 2 and cannot be grouped
All object pixels in the mini-batch share the same weight-                further. To avoid this, we modified the k-means++ cluster-
ing coefficients. We normalize the weights across all bits.               ing algorithm [1], to force both output groups of points to
We then define our hierarchical loss based on the weighting               have equal sizes.
function of active bits and Hamming distance as below:                        We modified Deeplabv3 [13] by adding skip connections
                                                                          and used Resnet34 [23] as the backbone. The input ROI is
                        d
                        X                                                 resized to the shape of 256×256×3, and the CNN output
             Lhier =          wj · Hamm(bj , pˆj ).             (5)
                                                                          has a height and width of 128. We applied the same dy-
                        j=1
                                                                          namic zoom-in strategy as CDPN [41] to generate the noisy
With this loss we focus mainly on active bits which                       ROI for the training. The parameter λ used in the histogram
automatically change from coarse to fine during training.                 is 0.05. The parameter σ used in the hierarchical loss is 0.5,
                                                                          and α has been set as 3 to balance the training for mask and

                                                                      5
vertex code prediction. The CNN has been trained 380k               4.2. Ablation Study on LM-O
steps using the Adam optimizer [36] with a batch size of
                                                                        In this section, we present the results of several ablation
32 and a fixed learning rate of 2e-4. During the inference
                                                                    studies as follows:
stage, we utilize the detected bounding box with Faster R-
                                                                        Length of Binary Vertex Code. The object 3D surface
CNN [56] and FCOS [63] provided by CDPNv2 [41]. If
                                                                    is encoded through iterative k-means++ clustering until the
not specified, we used detected bounding box from Faster
                                                                    size of the segmented cluster is small enough so that we
R-CNN in the ablation study.
                                                                    can map the vertex code to the centroid of each cluster. We
   Additionally, by changing any bit in the vertex code, the        used the same total number of classes as DPOD [72], which
code refers to another 3D point, possibly even to a vertex on       means each binary vertex code has 16 bits. However, if the
the other side of the object. To maintain the topology pre-         objects are small or the distance of the object to the cam-
sented with the ground truth correspondence map, we dis-            era is too large, different clusters in the fine level could be
abled the interpolation during the rendering when we gen-           rendered into the same pixel when we generate the ground
erated the ground truth. The resizing of ground truth is also       truth data. This makes the binary code in the fine levels (the
done with nearest neighbourhood interpolation in the train-         last few bits) redundant. Due to the distance variation of the
ing stage.                                                          object to the camera, we can not determine which bits are
   Datasets. The reported recall rate in LM [28] dataset            redundant.
has lately been higher than 95% and quite saturated, there-             In this ablation study, we research which bits are the re-
fore we focus on the more challenging LM-O [5] and YCB-             dundant bits. The models are trained without the hierarchi-
V [70] dataset in this paper. LM-O consist of 1214 images           cal training strategy, and we use Progressive-X [2] to solve
and is only used as test images. LM-O annotated 8 objects           the pose. We ignore the last few bits of the predicted bi-
poses in the images under partial occlusion, making pose            nary code in the inference stage. The new binary vertex
estimation more challenging. About 1.2k images per ob-              code with fewer bits refers to a larger point cloud group (see
ject in LM are used as the real training images for LM-O.           Fig. 2 left). We calculated the new centroid of the group and
Compared to LM-O, YCB-V is a large dataset containing               reassigned the centroid as the corresponding 3D points for
21 objects. Although YCB-V provides more real training              the binary vertex code with fewer bits. From Fig. 3 b) we
images, the objects are strongly occluded in the scene, and         can see that using 10-bit code is already sufficient to yield
many of the objects are geometrically symmetric.                    an accurate prediction for the objects in LM-O, indicating
                                                                    the last 6 bits are redundant for those objects. The results
    Since the LM-O dataset includes only a limited num-             fluctuated a bit when we applied the redundant bits, which
ber of training images, [34, 50] additionally render a large        indicates that for some objects the best results is achieved
number of synthetic images for training. However, due               by not using the full 16-bit code. However, in the follow-
to the domain gap between the synthetic and real images,            ing experiment, we always report the results with the full
the performance of the methods also heavily depends on              predicted vertex code.
the domain randomization and domain adaptation tech-                    Radix used in Vertex Code. The number of the clusters
nique [62, 71]. As the physically-based rendering (pbr)             in each iteration decides the radix of the generated vertex
training images [18] for both datasets are publicly acces-          code that describes the 3D vertex. Since our CNN predicts
sible now, using pbr images to support the training can help        the vertex code, it is meaningful to compare which radix
us focus on the pose estimation CNN itself. We use the pbr          in vertex code suits the representation better. We do not
images together with the real images for the training in the        need to generate all the vertex codes used in this ablation
same manner as [19, 29, 67].                                        study from scratch. More specifically, by merging every
   Error Metrics. We selected the ADD(-S) error metric              log2 r bit of a vertex code, we get a code with a radix r. For
as the most commonly used metric for the 6DoF pose es-              instance, a vertex with a binary code {11111110 11111111}
timation task. This metric calculates the average distance          can be transformed to {254 255} using 256 as the radix. We
of model points projected to the camera domain using the            will get exactly the same code for this vertex if we split the
predicted pose to the same model points projected using             object into 256 groups and split each group again into 256
the ground truth pose. For symmetric objects, the metric            groups. We use a fix wj = 1 (see eq. 4) for all positions
matches the closest model points projected with the ground          so the loss is essentially a binary cross entropy when r = 2,
truth pose instead of the same model point. In all the exper-       and cross-entropy loss for other radixes.
iments in this paper, if ADD(-S) error is smaller than 10%              We present the comparison results in Tab. 1. If
(most commonly used threshold) of the object diameter, the          RANSAC/PnP is used to solve the pose, the results with
predicted pose is considered to be correct For YCB-V, we            different radices are quite similar. There is no clear indi-
also reported the AUC (area under curve) of ADD(-S) with            cation whether using the small or large radix is better. If
a maximum threshold of 10 cm [70].                                  we switch the pose solver to Progressive-X [2], the code

                                                                6
a)                                             b)                  100                                                                                c)
     000…        G0          G1         G2                                                                                                                                         0,5
                                                                   90                                                                                                      0,45
                                                                   80                                                                                                              0,4

                                                                                                                                                           Average Hamming Error
                                                                   70                                                                                                      0,35

                                                ADD Metric Score
                                                                   60                                                                                                              0,3
                                                                   50                                                                                                      0,25
                                                                   40                                                                                                              0,2
     100…      010 …       001 …      011 …
                                                                   30                                                                                                      0,15
                                                                   20                                                                                                              0,1
                                                                   10                                                                                                      0,05
                                                                    0                                                                                                               0
                                                                         6     7         8       9     10     11    12      13     14   15   16                                           1    2    3    4    5    6    7    8 9 10 11 12 13 14 15 16
                                                                                             Number of bits used in the inference                                                                                         bit position
                                                                   ape   can       cat        duck      driller    eggbox        glue   holepuncher                                      ape       can       cat       duck     driller glue holepuncher

Figure 3. a) In the first row, a yellow dot has the ground truth binary vertex code beginning with 000, and the yellow circle refers to the
neighborhood vertex of this yellow dot. If the vertex code has been predicted as 100 (the first bit is wrong, marked as red in the figure)
during the inference stage, the estimated yellow dot lies somewhere on the head of the drill (marked in blue). The estimated 3D vertex
is far away from its original neighborhood and can be easily found by checking the spatial coherency. We show four similar cases in this
figure. b) We calculated ADD pose metrics only on the first j bits of the predicted code to build the 2D-3D correspondence. Here we
observe from which bit the predictions are stable. c) We present the average error rate at different bit positions on the LM-O dataset [5].

with small radix improves the most and yields the best ac-                                                               Method                   RANSAC/ Pnp [39]                                                           Progressive-X [2]
curacy. Progressive-X solver includes a spatial coherence
filter that checks neighboring 3D points with respect to its                                                        2 as radix                                                            73.06                                 75.23 (+2.17)
assigned 2D correspondences based on label cost energy                                                              4 as radix                                                            72.94                                 74.59 (+1.65)
minimization as introduced in [17]. It can therefore deal                                                          16 as radix                                                            73.04                                 74.98 (+1.94)
particularly well with the type of outliers, from our method                                                       256 as radix                                                           73.25                                 74.52 (+1.27)
as we mentioned in Fig. 3. We show in the Fig. 3 a), if the
                                                                                                                  Table 1. Ablation study on LM-O [5]. We tested the use of
CNN predicts the first few bits wrong for the yellow dot,
                                                                                                                  different radices to encode the vertices, and using different solvers
the estimated corresponding 3D points is far away from the                                                        to calculate the pose. The results are presented in terms of average
ground truth position and totally incoherent with its orig-                                                       recall of ADD(-S) in %.
inal neighbourhood. Assuming that most predictions are
correct, most neighbourhood vertices are posed within the
yellow circle in the figure. In this case, this false estimated                                                                                                                     Method                                              ADD
3D corresponding can be easily filtered by calculating the                                                                        2 as radix                                                                                            75.23
coherency with its neighbourhood. This spatial coherency                                                                          2 as radix + Hierarchical Learning                                                                    75.86
filter can not detect outliers well if the wrong prediction is                                                                    2 as radix + Hierarchical Learning
in the last few bits, and the same for 256 as radix, as divide                                                                                                                                                                          76.91
                                                                                                                                  + Faster R-CNN [56] → FCOS [63]
the vertices into 256 groups is already a fine grouping. Nev-
ertheless, the Fig. 3 b) already shows that the last few bits                                                     Table 2. Ablation study on LM-O [5]. We compare the result
do not affect the solved pose. So we argue that the binary                                                        with and w/o applying our hierarchical loss, as well as the impact
vertex code suits this task the best. Moreover, the predic-                                                       of the prior object detector. The results are presented with average
tion of binary codes requires the least RAM in GPU, as we                                                         recall of ADD(-S) in %.
discussed in Sec. 3.1.
    Effectiveness of Hierarchical Training. According to
the first ablation study, the last few bits are redundant and                                                     ing box with FCOS [63] instead of the one from Faster R-
may not be trainable (see Fig. 3c)). During the training, we                                                      CNN [56], the recall rate improved 1.05%.
can recognize redundant bits based on the error histogram
                                                                                                                  4.3. Comparison to State of the Art
and focus on the decisive bits as described in Sec. 3.5.
Tab. 2 shows that the results are further improved by our                                                            We use 2 as radix, i.e. binary vertex code and apply
proposed hierarchical training.                                                                                   the hierarchical training strategy and Progressive-X pose
    Influence of 2D detection. The CNN estimates the pose                                                         solver [2] in our proposed ZebraPose to compare to state
with the cropped ROI from the detected bounding box. The                                                          of the art on LM-O [5] and YCB-V [70] datasets. The de-
object pose estimation is meaningless with a false-positive                                                       tected bounding box of FCOS [63] detector are provided by
detection, also the pose is not even estimated in the case of                                                     CDPNv2 [41].
false-negative detection. By leveraging the detected bound-                                                          Results on LM-O. We report the recall of ADD(-S) met-

                                                                                                        7
                                                RGB Input                                                  RGB-D Input
   Method
                HybridPose [60]      RePose [32] GDR-Net [67]             SO-Pose [19]      Ours      PR-GCN [73] FFB6D [24]
     ape               20.9              31.1              46.8               48.4          57.9          40.2            47.2
     can               75.3              80.0              90.8               85.8          95.0          76.2            85.2
     cat               24.9              25.6              40.5               32.7          60.6          57.0            45.7
   driller             70.2              73.1              82.6               77.4          94.8          82.3            81.4
    duck               27.9              43.0              46.9               48.9          64.5          30.0            53.9
  eggbox*              52.4              51.7              54.2               52.4          70.9          68.2            70.2
   glue*               53.8              54.3              75.8               78.3          88.7          67.0            60.1
holepuncher            54.2              53.6              60.1               75.3          83.0          97.2            85.9
   mean                47.5              51.6              62.2               62.3          76.9           65             66.2

Table 3. Comparison with State of the Art on LM-O [5]. We report the Recall of ADD(-S) in % and compare with state of the art. (*)
denotes symmetric objects.

ric in Tab. 3. We ordered the methods according to the in-                                                 AUC of     AUC of
put modality. HybridPose [60] and RePose [32] have been                  Method               ADD(-S)
                                                                                                           ADD-S      ADD(-S)
trained with synthetic and real images. GDR-Net [67] also
reported their recall of 53% when trained with synthetic                 SegDriven [31]            39.0       -           -
and real images. Therefore, GDR-Net outperforms Hybrid-                  SingleStage [30]          53.9       -           -
Pose and RePose. In our Tab.3, we report the best results                CosyPose [37]              -        89.8        84.5
that GDR-Net and SO-Pose [19] presented, which are also                  RePose [32]               62.1      88.5        82.0
trained with pbr and real images. GDR-Net used faster                    GDR-Net [67]              60.1      91.6        84.4
R-CNN [56] as the detector, ZebraPose yields a recall of                 SO-Pose [19]              56.8      90.9        83.9
75.86% with faster R-CNN (see Tab. 2), which can be seen                 Ours                      80.5      90.1        85.3
as a more fair comparison with GDR-Net.
                                                                      Table 4. Comparison with State of the Art on YCB-V [70]. We
    To summarize, our ZebraPose outperforms state of the
                                                                      compare our ZebraPose with state of the art w.r.t ADD(-S), AUC
art RGB based methods with a large margin on this dataset.            of ADD(-S) and AUC of ADD-S in %. (-) denotes results missing
Additionally, we found that our ZebraPose also outperforms            from the original paper.
state of the art RGB-D based methods [24,73]. Most objects
in the LM-O dataset are texture-less, meaning that RGB-
D based methods should have more advantage in feature                 5. Conclusion
extraction on the objects with the help of depth image. Even
in this case, our results still exceed theirs.                           In this work, we proposed a novel coarse to fine surface
    Results on YCB-V. We compare ZebraPose with other                 encoding technique to provide 2D-3D correspondences for
approaches in the YCB-V dataset in Tab. 4. The AUC re-                6DoF object pose estimation. We also designed a specific
ported in Tab. 4 has been calculated using all-points interpo-        hierarchical training strategy that maximizes the prediction
lation. Tab. 4 shows that ZebraPose is still better than state        accuracy for our proposed binary vertex code. Solving the
of the art w.r.t. ADD(-S) and AUC of ADD(-S) metrics and              object pose using a PnP solver based on our vertex code sur-
comparable to them w.r.t. the AUC of ADD-S metric.                    passes the state of the art on different benchmarks, proving
                                                                      our approach’s effectiveness. In the future, we would like to
4.4. Runtime Analysis                                                 extend our vertex code solution to the problem of category-
   We tested the runtime on a desktop with an Intel                   level object pose [40].
3.50GHz CPU and an Nvidia 2080Ti GPU. The CNN run-
time plus the time to build the 2D-3D correspondence                  Acknowledgements
is about 52 ms. The FCOS detector [63] takes 55 ms.
                                                                        This work was partially funded by the Federal
RANSAC/PnP [39] needs only 4 ms to solve the pose, while              Ministry of Education and Research of the Federal Re-
Progressive-X [2] requires 150 ms to obtain the pose. So for          public of Germany (BMBF), under grant agreements
ZebraPose used in Sec.4.3, it totally needs about 250 ms to           16SV8732 (GreifbAR) and 01IW21001 (DECODE).
estimate the object pose. If we use RANSAC/PnP to solve               We are thankful to Rene Schuster, Fangwen Shu, Yaxu
the pose, the runtime reduces to 110 ms, while with about             Xie and Ghazal Ghazaei for proofreading the paper.
2.6% recall drop on LM-O dataset.

                                                                  8
References                                                                     tic image segmentation. arXiv preprint arXiv:1706.05587,
                                                                               2017. 5
 [1] David Arthur and Sergei Vassilvitskii. k-means++: The                [14] Qi Chen and Hartmut Prautzsch. General midpoint subdivi-
     advantages of careful seeding. Technical report, Stanford,                sion. arXiv preprint arXiv:1208.3794, 2012. 5
     2006. 5                                                              [15] Wenzheng Chen, Huan Ling, Jun Gao, Edward Smith,
 [2] Daniel Barath and Jiri Matas. Progressive-x: Efficient, any-              Jaakko Lehtinen, Alec Jacobson, and Sanja Fidler. Learn-
     time, multi-model fitting algorithm. In Proceedings of the                ing to predict 3d objects with an interpolation-based differ-
     IEEE/CVF International Conference on Computer Vision,                     entiable renderer. Advances in Neural Information Process-
     pages 3780–3788, 2019. 2, 5, 6, 7, 8, 12                                  ing Systems, 32:9609–9619, 2019. 2
 [3] Eric Brachmann, Alexander Krull, Frank Michel, Stefan                [16] Alvaro Collet, Manuel Martinez, and Siddhartha S Srinivasa.
     Gumhold, Jamie Shotton, and Carsten Rother. Learning                      The moped framework: Object recognition and pose estima-
     6d object pose estimation using 3d object coordinates. In                 tion for manipulation. The international journal of robotics
     European conference on computer vision, pages 536–551.                    research, 30(10):1284–1306, 2011. 1
     Springer, 2014. 2                                                    [17] Andrew Delong, Anton Osokin, Hossam N Isack, and Yuri
 [4] Eric Brachmann, Alexander Krull, Sebastian Nowozin,                       Boykov. Fast approximate energy minimization with label
     Jamie Shotton, Frank Michel, Stefan Gumhold, and Carsten                  costs. International journal of computer vision, 96(1):1–27,
     Rother. Dsac-differentiable ransac for camera localization.               2012. 7
     In Proceedings of the IEEE Conference on Computer Vision             [18] Maximilian Denninger, Martin Sundermeyer, Dominik
     and Pattern Recognition, pages 6684–6692, 2017. 2                         Winkelbauer, Youssef Zidan, Dmitry Olefir, Mohamad El-
 [5] Eric Brachmann, Frank Michel, Alexander Krull, Michael                    badrawy, Ahsan Lodhi, and Harinandan Katam. Blender-
     Ying Yang, Stefan Gumhold, and others. Uncertainty-driven                 proc. arXiv preprint arXiv:1911.01911, 2019. 6
     6d pose estimation of objects and scenes from a single rgb           [19] Yan Di, Fabian Manhardt, Gu Wang, Xiangyang Ji, Nassir
     image. In Proceedings of the IEEE Conference on Computer                  Navab, and Federico Tombari. So-pose: Exploiting self-
     Vision and Pattern Recognition, pages 3364–3372, 2016. 2,                 occlusion for direct 6d pose estimation. In Proceedings of
     5, 6, 7, 8, 12, 13, 14                                                    the IEEE/CVF International Conference on Computer Vi-
 [6] Eric Brachmann and Carsten Rother. Learning less is more-                 sion, pages 12396–12405, 2021. 2, 3, 6, 8
     6d camera localization via 3d surface regression. In Proceed-        [20] T Do, Trung Pham, Ming Cai, and Ian Reid. Real-time
     ings of the IEEE Conference on Computer Vision and Pattern                monocular object instance 6d pose estimation. 2019. 2
     Recognition, pages 4654–4662, 2018. 2                                [21] Ghazal Ghazaei, Iro Laina, Christian Rupprecht, Federico
 [7] Eric Brachmann and Carsten Rother. Neural-guided ransac:                  Tombari, Nassir Navab, and Kianoush Nazarpour. Deal-
     Learning where to sample model hypotheses. In Proceedings                 ing with ambiguity in robotic grasping via multiple predic-
     of the IEEE/CVF International Conference on Computer Vi-                  tions. In Asian Conference on Computer Vision, pages 38–
     sion, pages 4322–4331, 2019. 2                                            55. Springer, 2018. 1
                                                                          [22] Silvio Giancola, Matteo Valenti, and Remo Sala. A sur-
 [8] Benjamin Busam, Tolga Birdal, and Nassir Navab. Camera
                                                                               vey on 3D cameras: Metrological comparison of time-of-
     pose filtering with local regression geodesics on the rieman-
                                                                               flight, structured-light and active stereoscopy technologies.
     nian manifold of dual quaternions. In Proceedings of the
                                                                               Springer, 2018. 3
     IEEE International Conference on Computer Vision Work-
     shops, pages 2436–2445, 2017. 2                                      [23] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
                                                                               Deep residual learning for image recognition. In Proceed-
 [9] Benjamin Busam, Marco Esposito, Simon Che’Rose, Nas-
                                                                               ings of the IEEE conference on computer vision and pattern
     sir Navab, and Benjamin Frisch. A stereo vision approach
                                                                               recognition, pages 770–778, 2016. 5
     for cooperative robotic movement therapy. In Proceedings
                                                                          [24] Yisheng He, Haibin Huang, Haoqiang Fan, Qifeng Chen, and
     of the IEEE International Conference on Computer Vision
                                                                               Jian Sun. Ffb6d: A full flow bidirectional fusion network for
     Workshops, pages 127–135, 2015. 1
                                                                               6d pose estimation. In Proceedings of the IEEE/CVF Con-
[10] Benjamin Busam, Hyun Jun Jung, and Nassir Navab. I like                   ference on Computer Vision and Pattern Recognition, pages
     to move it: 6d pose estimation as an action decision process.             3003–3013, 2021. 8
     arXiv preprint arXiv:2009.12678, 2020. 1                             [25] Stefan Hinterstoisser, Cedric Cagniart, Slobodan Ilic, Peter
[11] Berk Calli, Arjun Singh, Aaron Walsman, Siddhartha Srini-                 Sturm, Nassir Navab, Pascal Fua, and Vincent Lepetit. Gra-
     vasa, Pieter Abbeel, and Aaron M Dollar. The ycb object and               dient response maps for real-time detection of textureless ob-
     model set: Towards common benchmarks for manipulation                     jects. IEEE transactions on pattern analysis and machine
     research. In Advanced Robotics (ICAR), 2015 International                 intelligence, 34(5):876–888, 2011. 2
     Conference on, pages 510–517. IEEE, 2015. 2                          [26] Stefan Hinterstoisser, Cedric Cagniart, Slobodan Ilic, Peter
[12] Carlos Campos, Richard Elvira, Juan J Gómez Rodrı́guez,                  Sturm, Nassir Navab, Pascal Fua, and Vincent Lepetit. Gra-
     José MM Montiel, and Juan D Tardós. Orb-slam3: An accu-                 dient response maps for real-time detection of textureless ob-
     rate open-source library for visual, visual–inertial, and mul-            jects. IEEE Transactions on Pattern Analysis and Machine
     timap slam. IEEE Transactions on Robotics, 2021. 2                        Intelligence, 34(5):876–888, 2012. 1
[13] Liang-Chieh Chen, George Papandreou, Florian Schroff, and            [27] Stefan Hinterstoisser, Stefan Holzer, Cedric Cagniart, Slobo-
     Hartwig Adam. Rethinking atrous convolution for seman-                    dan Ilic, Kurt Konolige, Nassir Navab, and Vincent Lepetit.

                                                                      9
     Multimodal templates for real-time detection of texture-less              pose estimation. In Proceedings of the IEEE/CVF Confer-
     objects in heavily cluttered scenes. In 2011 international                ence on Computer Vision and Pattern Recognition, pages
     conference on computer vision, pages 858–865. IEEE, 2011.                 3706–3715, 2020. 8
     3                                                                    [41] Zhigang Li, Gu Wang, and Xiangyang Ji.                   Cdpn:
[28] Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic, Ste-               Coordinates-based disentangled pose network for real-time
     fan Holzer, Gary Bradski, Kurt Konolige, and Nassir Navab.                rgb-based 6-dof object pose estimation. In Proceedings of
     Model based training, detection and pose estimation of                    the IEEE/CVF International Conference on Computer Vi-
     texture-less 3d objects in heavily cluttered scenes. In Asian             sion, pages 7678–7687, 2019. 4, 5, 6, 7
     conference on computer vision, pages 548–562. Springer,              [42] Matthew M Loper and Michael J Black. Opendr: An ap-
     2012. 1, 6                                                                proximate differentiable renderer. In European Conference
[29] Tomas Hodan, Daniel Barath, and Jiri Matas. Epos: Esti-                   on Computer Vision, pages 154–169. Springer, 2014. 2
     mating 6d pose of objects with symmetries. In Proceedings            [43] David G Lowe. Distinctive image features from scale-
     of the IEEE/CVF conference on computer vision and pattern                 invariant keypoints. International journal of computer vi-
     recognition, pages 11703–11712, 2020. 2, 3, 6                             sion, 60(2):91–110, 2004. 2
[30] Yinlin Hu, Pascal Fua, Wei Wang, and Mathieu Salzmann.               [44] Fabian Manhardt, Diego Martin Arroyo, Christian Rup-
     Single-stage 6d object pose estimation. In Proceedings of                 precht, Benjamin Busam, Tolga Birdal, Nassir Navab, and
     the IEEE/CVF conference on computer vision and pattern                    Federico Tombari. Explaining the ambiguity of object detec-
     recognition, pages 2930–2939, 2020. 2, 8, 15                              tion and 6d pose from visual data. In Proceedings of the
[31] Yinlin Hu, Joachim Hugonot, Pascal Fua, and Mathieu Salz-                 IEEE/CVF International Conference on Computer Vision,
     mann. Segmentation-driven 6d object pose estimation. In                   pages 6841–6850, 2019. 2
     Proceedings of the IEEE/CVF Conference on Computer Vi-               [45] Fabian Manhardt, Wadim Kehl, Nassir Navab, and Federico
     sion and Pattern Recognition, pages 3385–3394, 2019. 8,                   Tombari. Deep model-based 6d pose refinement in rgb. In
     15                                                                        Proceedings of the European Conference on Computer Vi-
[32] Shun Iwase, Xingyu Liu, Rawal Khirodkar, Rio Yokota, and                  sion (ECCV), pages 800–815, 2018. 2
     Kris M Kitani. Repose: Fast 6d object pose refinement via            [46] Eric Marchand, Hideaki Uchiyama, and Fabien Spindler.
     deep texture rendering. In Proceedings of the IEEE/CVF                    Pose estimation for augmented reality: a hands-on survey.
     International Conference on Computer Vision, pages 3303–                  IEEE transactions on visualization and computer graphics,
     3312, 2021. 2, 8, 15                                                      22(12):2633–2651, 2016. 1
                                                                          [47] Michihiko MIMOU, Takeo Kanade, and Toshiyuki SAKAI.
[33] Hiroharu Kato, Yoshitaka Ushiku, and Tatsuya Harada. Neu-
                                                                               A method of time-coded parallel planes of light for
     ral 3d mesh renderer. In Proceedings of the IEEE conference
                                                                               depth measurement. IEICE TRANSACTIONS (1976-1990),
     on computer vision and pattern recognition, pages 3907–
                                                                               64(8):521–528, 1981. 3
     3916, 2018. 2
                                                                          [48] Markus Oberweger, Mahdi Rad, and Vincent Lepetit. Mak-
[34] Wadim Kehl, Fabian Manhardt, Federico Tombari, Slobodan
                                                                               ing Deep Heatmaps Robust to Partial Occlusions for 3D Ob-
     Ilic, and Nassir Navab. SSD-6D: Making RGB-based 3D
                                                                               ject Pose Estimation. pages 2–4. 2
     detection and 6D pose estimation great again. In Proceedings
                                                                          [49] Kiru Park, Timothy Patten, and Markus Vincze. Pix2pose:
     of the International Conference on Computer Vision (ICCV
                                                                               Pixel-wise coordinate regression of objects for 6d pose esti-
     2017), Venice, Italy, pages 22–29, 2017. 1, 2, 6
                                                                               mation. In Proceedings of the IEEE/CVF International Con-
[35] Alex Kendall, Matthew Grimes, and Roberto Cipolla.                        ference on Computer Vision, pages 7668–7677, 2019. 2, 3,
     Posenet: A convolutional network for real-time 6-dof cam-                 5
     era relocalization. In Proceedings of the IEEE international
                                                                          [50] Sida Peng, Yuan Liu, Qixing Huang, Xiaowei Zhou, and Hu-
     conference on computer vision, pages 2938–2946, 2015. 2
                                                                               jun Bao. Pvnet: Pixel-wise voting network for 6dof pose
[36] Diederik P Kingma and Jimmy Ba. Adam: A method for                        estimation. In Proceedings of the IEEE/CVF Conference
     stochastic optimization. arXiv preprint arXiv:1412.6980,                  on Computer Vision and Pattern Recognition, pages 4561–
     2014. 6                                                                   4570, 2019. 2, 3, 6
[37] Yann Labbé, Justin Carpentier, Mathieu Aubry, and Josef             [51] Luis Pérez, Íñigo Rodr\’\iguez, Nuria Rodr\’\iguez, Rubén
     Sivic. Cosypose: Consistent multi-view multi-object 6d pose               Usamentiaga, and Daniel Garc\’\ia. Robot guidance us-
     estimation. In European Conference on Computer Vision,                    ing machine vision techniques in industrial environments: A
     pages 574–591. Springer, 2020. 2, 4, 8, 16                                comparative review. Sensors, 16(3):335, 2016. 1
[38] Vincent Lepetit, Francesc Moreno-Noguer, and Pascal Fua.             [52] Jeffrey L Posdamer and MD Altschuler. Surface measure-
     Epnp: An accurate o (n) solution to the pnp problem. Inter-               ment by space-encoded projected beam systems. Computer
     national journal of computer vision, 81(2):155, 2009. 12                  graphics and image processing, 18(1):1–17, 1982. 3
[39] Vincent Lepetit, Francesc Moreno-Noguer, and Pascal Fua.             [53] Mahdi Rad and Vincent Lepetit. BB8: A scalable, accu-
     EPnP: An Accurate O(n) Solution to the PnP Problem. In-                   rate, robust to partial occlusion method for predicting the 3D
     ternational Journal of Computer Vision, 81(2):155–166, 2                  poses of challenging objects without using depth. In ICCV,
     2009. 1, 7, 8                                                             2017. 2, 3
[40] Xiaolong Li, He Wang, Li Yi, Leonidas J Guibas, A Lynn               [54] Jason Rambach, Chengbiao Deng, Alain Pagani, and Didier
     Abbott, and Shuran Song. Category-level articulated object                Stricker. Learning 6dof object poses from synthetic single

                                                                     10
     channel images. In 2018 IEEE International Symposium                 [68] He Wang, Srinath Sridhar, Jingwei Huang, Julien Valentin,
     on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct),                   Shuran Song, and Leonidas J Guibas. Normalized object
     pages 164–169. IEEE, 2018. 1                                              coordinate space for category-level 6d object pose and size
[55] Jason Rambach, Alain Pagani, Michael Schneider, Olek-                     estimation. In Proceedings of the IEEE/CVF Conference
     sandr Artemenko, and Didier Stricker. 6dof object tracking                on Computer Vision and Pattern Recognition, pages 2642–
     based on 3d scans for augmented reality remote live support.              2651, 2019. 2, 3, 5
     Computers, 7(1):6, 2018. 1                                           [69] Paul Wohlhart and Vincent Lepetit. Learning descriptors for
[56] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.                    object recognition and 3d pose estimation. In Proceedings
     Faster r-cnn: Towards real-time object detection with region              of the IEEE Conference on Computer Vision and Pattern
     proposal networks. In Advances in neural information pro-                 Recognition, pages 3109–3118, 2015. 3
     cessing systems, pages 91–99, 2015. 6, 7, 8                          [70] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and
[57] Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary                     Dieter Fox. Posecnn: A convolutional neural network for
     Bradski. ORB: An efficient alternative to SIFT or SURF. In                6d object pose estimation in cluttered scenes. arXiv preprint
     2011 International Conference on Computer Vision, pages                   arXiv:1711.00199, 2017. 1, 2, 5, 6, 7, 8, 12, 16, 17
     2564–2571. IEEE, 11 2011. 2                                          [71] Sergey Zakharov, Wadim Kehl, and Slobodan Ilic. Decep-
[58] Joaquim Salvi, Jordi Pages, and Joan Batlle. Pattern codifi-              tionnet: Network-driven domain randomization. In Proceed-
     cation strategies in structured light systems. Pattern recog-             ings of the IEEE/CVF International Conference on Com-
     nition, 37(4):827–849, 2004. 3                                            puter Vision, pages 532–541, 2019. 6
[59] Juil Sock, Guillermo Garcia-Hernando, Anil Armagan, and              [72] Sergey Zakharov, Ivan S. Shugurov, and Slobodan Ilic.
     Tae-Kyun Kim. Introducing pose consistency and warp-                      Dpod: 6d pose object detector and refiner. 2019 IEEE/CVF
     alignment for self-supervised 6d object pose estimation in                International Conference on Computer Vision (ICCV), pages
     color images. In 2020 International Conference on 3D Vi-                  1941–1950, 2019. 2, 3, 5, 6
     sion (3DV), pages 291–300. IEEE, 2020. 2                             [73] Guangyuan Zhou, Huiqun Wang, Jiaxin Chen, and Di
[60] Chen Song, Jiaru Song, and Qixing Huang. Hybridpose: 6d                   Huang. Pr-gcn: A deep graph convolutional network with
     object pose estimation under hybrid representations. In Pro-              point refinement for 6d pose estimation. In Proceedings of
     ceedings of the IEEE/CVF conference on computer vision                    the IEEE/CVF International Conference on Computer Vi-
     and pattern recognition, pages 431–440, 2020. 3, 8                        sion, pages 2793–2802, 2021. 8
[61] Yongzhi Su, Jason Rambach, Alain Pagani, and Didier                  [74] Yi Zhou, Connelly Barnes, Jingwan Lu, Jimei Yang, and
     Stricker. Synpo-net—accurate and fast cnn-based 6dof                      Hao Li. On the continuity of rotation representations in neu-
     object pose estimation using synthetic training. Sensors,                 ral networks. In Proceedings of the IEEE/CVF Conference
     21(1):300, 2021. 2                                                        on Computer Vision and Pattern Recognition, pages 5745–
[62] Martin Sundermeyer, Zoltan-Csaba Marton, Maximilian                       5753, 2019. 2
     Durner, Manuel Brucker, and Rudolph Triebel. Implicit 3d
     orientation learning for 6d object detection from rgb images.
     In Proceedings of the European Conference on Computer Vi-
     sion (ECCV), pages 699–715, 2018. 1, 3, 6
[63] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. Fcos:
     Fully convolutional one-stage object detection. In Proceed-
     ings of the IEEE/CVF international conference on computer
     vision, pages 9627–9636, 2019. 6, 7, 8, 12, 14, 17
[64] Marjan Trobina. Error model of a coded-light range sensor.
     Technical report, 1995. 3
[65] Joel Vidal, Chyi-Yeu Lin, and Robert Mart\’\i. 6D pose
     estimation using an improved method based on point pair
     features. In 2018 4th International Conference on Control,
     Automation and Robotics (ICCAR), pages 405–409. IEEE,
     2018. 1
[66] Gu Wang, Fabian Manhardt, Jianzhun Shao, Xiangyang
     Ji, Nassir Navab, and Federico Tombari. Self6d: Self-
     supervised monocular 6d object pose estimation. In Eu-
     ropean Conference on Computer Vision, pages 108–125.
     Springer, 2020. 2
[67] Gu Wang, Fabian Manhardt, Federico Tombari, and Xi-
     angyang Ji. Gdr-net: Geometry-guided direct regression net-
     work for monocular 6d object pose estimation. In Proceed-
     ings of the IEEE/CVF Conference on Computer Vision and
     Pattern Recognition, pages 16611–16621, 2021. 2, 3, 4, 5,
     6, 8, 15, 16

                                                                     11
6. Supplementary Material                                              original images. The presented confidence scores are from
                                                                       the 2D object detection with FCOS detector [63].
6.1. Hyper-parameters in the Pose Solver
   For RANSAC/PnP [38], we set the threshold value for
reprojection error as 2 pixels, and execute 150 iterations.
For Progressive-X [2], we also set the threshold value for
the reprojection error as 2 pixels, and execute 400 iterations.
The additional parameters for Progressive-X are ”neigh-
borhood ball radius=20”, ”spatial coherence weight=0.1”,
”maximum tanimoto similarity=0.9”.
6.2. BOP Challenge
   We submitted the results on 4 datasets of the BOP chal-
lenge and will test our method on the rest 3 datasets. The
results are online in BOP Leaderboards with the submission
name ”zebrapose”.
6.3. YCB-V Evaluation per Object
    We present a more detailed result on the YCB-V
dataset [70] in Tab. 5 and Tab. 6. As the Tab. 5 shows, in
the evaluation of the estimate pose w.r.t ADD(-S) metric,
we show major improvement over the state of the art.
    In Tab. 6, we carefully calculated the AUC with all-
points interpolation algorithm with the maximum threshold
of 10 cm. If we calculate the AUC with 11-points interpo-
lation, we will reach AUC of ADD-S of 94%, and AUC of
ADD(-S) of 89.8%.
6.4. Qualitative Results
6.4.1   Vertex Code Prediction LM-O
We visualized the predicted binary code of the ”duck” ob-
ject in LM-O dataset [5] with a few examples in Fig. 4. Due
to the size limits, we only show the predicted binary code
till the 11-th bits. We render the object with the predicted
pose on top of the original input ROI. To make the predicted
pose more visible in the figure, we set the colour of the ob-
ject model as red just for this figure. So the duck appears
with the orange colour (red + yellow) in the last row. We
can see that the rendered object overlapped the object in the
original image quite well, indicating that our predicted pose
is very accurate.

6.4.2   Pose Prediction LM-O
Qualitative Results on LM-O [5] can be found in Fig. 5. We
render the objects with estimated pose on top of the original
images. The presented confidence scores are from the 2D
object detection with FCOS detector [63].

6.4.3   Pose Prediction YCB-V
Qualitative Results on YCB-V [70] are available in Fig. 6.
We render the objects with estimated pose on top of the

                                                                  12
    ROI input

    𝐺0

    𝐺1

    𝐺2

    𝐺3

    𝐺4

    𝐺5

    𝐺6

    𝐺7

      𝐺8

      𝐺9

    𝐺10

    𝐺11
    pred. pose

Figure 4. We visualized the predicted binary code of the ”duck” in LM-O dataset [5] with a few examples. Due to the size limits, we only
show the predicted binary code till the 11-th bit. We set the colour of the object model as red and render the object with the predicted pose
on the top of the input ROI. We can see that the rendered object overlaps the object in the image quite well.

                                                                     13
Figure 5. Qualitative Results on LM-O [5]: We render the objects with estimated pose on top of the original images. The presented
confidence score are from the 2D object detection with FCOS detector [63].

                                                               14
          Method                      SegDriven [31]      Single-Stage [30]    RePose [32]      GDR-Net [67]      Ours
          002 master chef can               33.0                  -                  -               41.5          62.6
          003 cracker box                   44.6                  -                  -               83.2          98.5
          004 sugar box                     75.6                  -                  -               91.5          96.3
          005 tomato soup can               40.8                  -                  -               65.9          80.5
          006 mustard bottle                70.6                  -                  -               90.2         100.0
          007 tuna fish can                 18.1                  -                  -               44.2          70.5
          008 pudding box                   12.2                  -                  -                2.8          99.5
          009 gelatin box                   59.4                  -                  -               61.7          97.2
          010 potted meat can               33.3                  -                  -               64.9          76.9
          011 banana                        16.6                  -                  -               64.1          71.2
          019 pitcher base                  90.0                  -                  -               99.0         100.0
          021 bleach cleanser               70.9                  -                  -               73.8          75.9
          024 bowl*                         30.5                  -                  -               37.7          18.5
          025 mug                           40.7                  -                  -               61.5          77.5
          035 power drill                   63.5                  -                  -               78.5          97.4
          036 wood block*                   27.7                  -                  -               59.5          87.6
          037 scissors                      17.1                  -                  -                3.9          71.8
          040 large marker                   4.8                  -                  -                7.4          23.3
          051 large clamp*                  25.6                  -                  -               69.8          87.6
          052 extra large clamp*             8.8                  -                  -               90.0          98.0
          061 foam brick*                   34.7                  -                  -               71.9          99.3
          mean                              39.0                 53.9               62.1             60.1          80.5

Table 5. Comparison with State of the Art on YCB-V. We report the Average Recall of ADD(-S) in % and compare with state of the art.
(*) denotes symmetric objects, (-) denotes the results missing from the original paper.

                                                                15
   Method                       PoseCNN [70]           CosyPose [37]           GDR-Net [67]                 Ours
                              AUC of    AUC of       AUC of       AUC of    AUC of     AUC of      AUC of      AUC of
   Metric
                              ADD-S     ADD(-S)      ADD-S        ADD(-S)   ADD-S      ADD(-S)     ADD-S       ADD(-S)
   002 master chef can         84.0        50.9        -            -         96.3       65.2        93.7          75.4
   003 cracker box             76.9        51.7        -            -         97.0       88.8        93.0          87.8
   004 sugar box               84.3        68.6        -            -         98.9       95.0        95.1          90.9
   005 tomato soup can         80.9        66.0        -            -         96.5       91.9        94.4          90.1
   006 mustard bottle          90.2        79.9        -            -         100        92.8        96.0          92.6
   007 tuna fish can           87.9        70.4        -            -         99.4       94.2        96.9          92.6
   008 pudding box             79.0        62.9        -            -         64.6       44.7        97.2          95.3
   009 gelatin box             87.1        75.2        -            -         97.1       92.5        96.8          94.8
   010 potted meat can         78.5        59.6        -            -         86.0       80.2        91.7          83.6
   011 banana                  85.9        72.3        -            -         96.3       85.8        92.6          84.6
   019 pitcher base            76.8        52.5        -            -         99.9       98.5        96.4          93.4
   021 bleach cleanser         71.9        50.5        -            -         94.2       84.3        89.5          80.0
   024 bowl*                   69.7        69.7        -            -         85.7       85.7        37.1          37.1
   025 mug                     78.0        57.7        -            -         99.6       94.0        96.1          90.8
   035 power drill             72.8        55.1        -            -         97.5       90.1        95.0          89.7
   036 wood block*             65.8        65.8        -            -         82.5       82.5        84.5          84.5
   037 scissors                56.2        35.8        -            -         63.8       49.5        92.5          84.5
   040 large marker            71.4        58.0        -            -         88.0       76.1        80.4          69.5
   051 large clamp*            49.9        49.9        -            -         89.3       89.3        85.6          85.6
   052 extra large clamp*      47.0        47.0        -            -         93.5       93.5        92.5          92.5
   061 foam brick*             87.8        87.8        -            -         96.9       96.9        95.3          95.3
   mean                        75.9        61.3       89.8         84.5       91.6       84.3        90.1          85.3

Table 6. Comparison with State of the Art on YCB-V. We report the Average Recall w.r.t AUC of ADD(-S) and AUC of ADD-S in %
and compare with state of the art. (*) denotes symmetric objects, (-) denotes the results missing from the original paper.

                                                             16
Figure 6. Qualitative Results on YCB-V [70]: We render the objects with estimated pose on top of the original images. The presented
confidence score are from the 2D object detection with FCOS detector [63].

                                                                17
