---
source_id: 148
bibtex_key: qi2017pointnet
title: PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation
year: 2017
domain_theme: Fusi Multimodal
verified_pdf: 148_PointNet.pdf
char_count: 116934
---

PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation
                                                                                                                               Input Point Cloud (point set representation)

                                                               Charles R. Qi*       Hao Su*      Kaichun Mo                     Leonidas J. Guibas
                                                                                         Stanford University

                                                                      Abstract                                                           PointNet
arXiv:1612.00593v2 [cs.CV] 10 Apr 2017

                                            Point cloud is an important type of geometric data                        mug?
                                         structure. Due to its irregular format, most researchers
                                         transform such data to regular 3D voxel grids or collections                 table?
                                         of images. This, however, renders data unnecessarily
                                         voluminous and causes issues. In this paper, we design a                     car?
                                         novel type of neural network that directly consumes point          Classification                                 Semantic Segmentation
                                                                                                                                    Part Segmentation
                                         clouds, which well respects the permutation invariance of
                                                                                                            Figure 1. Applications of PointNet. We propose a novel deep net
                                         points in the input. Our network, named PointNet, pro-
                                                                                                            architecture that consumes raw point cloud (set of points) without
                                         vides a unified architecture for applications ranging from         voxelization or rendering. It is a unified architecture that learns
                                         object classification, part segmentation, to scene semantic        both global and local point features, providing a simple, efficient
                                         parsing. Though simple, PointNet is highly efficient and           and effective approach for a number of 3D recognition tasks.
                                         effective. Empirically, it shows strong performance on
                                         par or even better than state of the art. Theoretically,
                                         we provide analysis towards understanding of what the              still has to respect the fact that a point cloud is just a
                                         network has learnt and why the network is robust with              set of points and therefore invariant to permutations of its
                                         respect to input perturbation and corruption.                      members, necessitating certain symmetrizations in the net
                                                                                                            computation. Further invariances to rigid motions also need
                                                                                                            to be considered.
                                         1. Introduction                                                        Our PointNet is a unified architecture that directly
                                                                                                            takes point clouds as input and outputs either class labels
                                                                                                            for the entire input or per point segment/part labels for
                                            In this paper we explore deep learning architectures            each point of the input. The basic architecture of our
                                         capable of reasoning about 3D geometric data such as               network is surprisingly simple as in the initial stages each
                                         point clouds or meshes. Typical convolutional architectures        point is processed identically and independently. In the
                                         require highly regular input data formats, like those of           basic setting each point is represented by just its three
                                         image grids or 3D voxels, in order to perform weight               coordinates (x, y, z). Additional dimensions may be added
                                         sharing and other kernel optimizations. Since point clouds         by computing normals and other local or global features.
                                         or meshes are not in a regular format, most researchers                Key to our approach is the use of a single symmetric
                                         typically transform such data to regular 3D voxel grids or         function, max pooling. Effectively the network learns a
                                         collections of images (e.g, views) before feeding them to          set of optimization functions/criteria that select interesting
                                         a deep net architecture. This data representation transfor-        or informative points of the point cloud and encode the
                                         mation, however, renders the resulting data unnecessarily          reason for their selection. The final fully connected layers
                                         voluminous — while also introducing quantization artifacts         of the network aggregate these learnt optimal values into the
                                         that can obscure natural invariances of the data.                  global descriptor for the entire shape as mentioned above
                                            For this reason we focus on a different input rep-              (shape classification) or are used to predict per point labels
                                         resentation for 3D geometry using simply point clouds              (shape segmentation).
                                         – and name our resulting deep nets PointNets. Point                    Our input format is easy to apply rigid or affine transfor-
                                         clouds are simple and unified structures that avoid the            mations to, as each point transforms independently. Thus
                                         combinatorial irregularities and complexities of meshes,           we can add a data-dependent spatial transformer network
                                         and thus are easier to learn from. The PointNet, however,          that attempts to canonicalize the data before the PointNet
                                            * indicates equal contributions.                                processes them, so as to further improve the results.

                                                                                                        1
   We provide both a theoretical analysis and an ex-             their operations are still on sparse volumes, it’s challenging
perimental evaluation of our approach. We show that              for them to process very large point clouds. Multiview
our network can approximate any set function that is             CNNs: [23, 18] have tried to render 3D point cloud or
continuous. More interestingly, it turns out that our network    shapes into 2D images and then apply 2D conv nets to
learns to summarize an input point cloud by a sparse set of      classify them. With well engineered image CNNs, this
key points, which roughly corresponds to the skeleton of         line of methods have achieved dominating performance on
objects according to visualization. The theoretical analysis     shape classification and retrieval tasks [21]. However, it’s
provides an understanding why our PointNet is highly             nontrivial to extend them to scene understanding or other
robust to small perturbation of input points as well as          3D tasks such as point classification and shape completion.
to corruption through point insertion (outliers) or deletion     Spectral CNNs: Some latest works [4, 16] use spectral
(missing data).                                                  CNNs on meshes. However, these methods are currently
   On a number of benchmark datasets ranging from shape          constrained on manifold meshes such as organic objects
classification, part segmentation to scene segmentation,         and it’s not obvious how to extend them to non-isometric
we experimentally compare our PointNet with state-of-            shapes such as furniture. Feature-based DNNs: [6, 8]
the-art approaches based upon multi-view and volumetric          firstly convert the 3D data into a vector, by extracting
representations. Under a unified architecture, not only is       traditional shape features and then use a fully connected net
our PointNet much faster in speed, but it also exhibits strong   to classify the shape. We think they are constrained by the
performance on par or even better than state of the art.         representation power of the features extracted.
   The key contributions of our work are as follows:
  • We design a novel deep net architecture suitable for
    consuming unordered point sets in 3D;
                                                                 Deep Learning on Unordered Sets From a data structure
  • We show how such a net can be trained to perform             point of view, a point cloud is an unordered set of vectors.
    3D shape classification, shape part segmentation and         While most works in deep learning focus on regular input
    scene semantic parsing tasks;                                representations like sequences (in speech and language
  • We provide thorough empirical and theoretical analy-         processing), images and volumes (video or 3D data), not
    sis on the stability and efficiency of our method;           much work has been done in deep learning on point sets.
  • We illustrate the 3D features computed by the selected          One recent work from Oriol Vinyals et al [25] looks
    neurons in the net and develop intuitive explanations        into this problem. They use a read-process-write network
    for its performance.                                         with attention mechanism to consume unordered input sets
                                                                 and show that their network has the ability to sort numbers.
    The problem of processing unordered sets by neural nets
                                                                 However, since their work focuses on generic sets and NLP
is a very general and fundamental problem – we expect that
                                                                 applications, there lacks the role of geometry in the sets.
our ideas can be transferred to other domains as well.

2. Related Work
                                                                 3. Problem Statement
Point Cloud Features Most existing features for point
cloud are handcrafted towards specific tasks. Point features        We design a deep learning framework that directly
often encode certain statistical properties of points and are    consumes unordered point sets as inputs. A point cloud is
designed to be invariant to certain transformations, which       represented as a set of 3D points {Pi | i = 1, ..., n}, where
are typically classified as intrinsic [2, 24, 3] or extrinsic    each point Pi is a vector of its (x, y, z) coordinate plus extra
[20, 19, 14, 10, 5]. They can also be categorized as local       feature channels such as color, normal etc. For simplicity
features and global features. For a specific task, it is not     and clarity, unless otherwise noted, we only use the (x, y, z)
trivial to find the optimal feature combination.                 coordinate as our point’s channels.
                                                                    For the object classification task, the input point cloud is
Deep Learning on 3D Data 3D data has multiple popular            either directly sampled from a shape or pre-segmented from
representations, leading to various approaches for learning.     a scene point cloud. Our proposed deep network outputs
Volumetric CNNs: [28, 17, 18] are the pioneers applying          k scores for all the k candidate classes. For semantic
3D convolutional neural networks on voxelized shapes.            segmentation, the input can be a single object for part region
However, volumetric representation is constrained by its         segmentation, or a sub-volume from a 3D scene for object
resolution due to data sparsity and computation cost of          region segmentation. Our model will output n × m scores
3D convolution. FPNN [13] and Vote3D [26] proposed               for each of the n points and each of the m semantic sub-
special methods to deal with the sparsity problem; however,      categories.
                      Classification Network
                               input             mlp (64,64)                  feature          mlp (64,128,1024)                 max                    mlp
                            transform                                       transform
       input points

                                                                                                                                 pool 1024           (512,256,k)

                                                                                        nx64
                                                               nx64
                      nx3

                                           nx3
                                                  shared                                            shared         nx1024
                                                                                                                                    global feature             k
                                                                                                                                                     output scores
                                                                                                                            point features

                                                                                                                                                                   output scores
                                     3x3                               64x64
                            T-Net                          T-Net
                                     transform                         transform

                                                                                                                                 nx128

                                                                                                                                                         nxm
                                                                                               n x 1088            shared                  shared
                                     matrix                            matrix
                                    multiply                          multiply

                                                                                                             mlp (512,256,128)           mlp (128,m)
                                                                                    Segmentation Network
Figure 2. PointNet Architecture. The classification network takes n points as input, applies input and feature transformations, and then
aggregates point features by max pooling. The output is classification scores for k classes. The segmentation network is an extension to the
classification net. It concatenates global and local features and outputs per point scores. “mlp” stands for multi-layer perceptron, numbers
in bracket are layer sizes. Batchnorm is used for all layers with ReLU. Dropout layers are used for the last mlp in classification net.

4. Deep Learning on Point Sets                                                                    all the points, a local and global information combination
                                                                                                  structure, and two joint alignment networks that align both
   The architecture of our network (Sec 4.2) is inspired by                                       input points and point features.
the properties of point sets in Rn (Sec 4.1).
                                                                                                      We will discuss our reason behind these design choices
4.1. Properties of Point Sets in Rn                                                               in separate paragraphs below.

    Our input is a subset of points from an Euclidean space.
It has three main properties:                                                                     Symmetry Function for Unordered Input In order
                                                                                                  to make a model invariant to input permutation, three
  • Unordered. Unlike pixel arrays in images or voxel                                             strategies exist: 1) sort input into a canonical order; 2) treat
    arrays in volumetric grids, point cloud is a set of points                                    the input as a sequence to train an RNN, but augment the
    without specific order. In other words, a network that                                        training data by all kinds of permutations; 3) use a simple
    consumes N 3D point sets needs to be invariant to N !                                         symmetric function to aggregate the information from each
    permutations of the input set in data feeding order.                                          point. Here, a symmetric function takes n vectors as input
  • Interaction among points. The points are from a space                                         and outputs a new vector that is invariant to the input
    with a distance metric. It means that points are not                                          order. For example, + and ∗ operators are symmetric binary
    isolated, and neighboring points form a meaningful                                            functions.
    subset. Therefore, the model needs to be able to                                                  While sorting sounds like a simple solution, in high
    capture local structures from nearby points, and the                                          dimensional space there in fact does not exist an ordering
    combinatorial interactions among local structures.                                            that is stable w.r.t. point perturbations in the general
                                                                                                  sense. This can be easily shown by contradiction. If
  • Invariance under transformations. As a geometric                                              such an ordering strategy exists, it defines a bijection map
    object, the learned representation of the point set                                           between a high-dimensional space and a 1d real line. It
    should be invariant to certain transformations. For                                           is not hard to see, to require an ordering to be stable w.r.t
    example, rotating and translating points all together                                         point perturbations is equivalent to requiring that this map
    should not modify the global point cloud category nor                                         preserves spatial proximity as the dimension reduces, a task
    the segmentation of the points.                                                               that cannot be achieved in the general case. Therefore,
                                                                                                  sorting does not fully resolve the ordering issue, and it’s
4.2. PointNet Architecture
                                                                                                  hard for a network to learn a consistent mapping from
   Our full network architecture is visualized in Fig 2,                                          input to output as the ordering issue persists. As shown in
where the classification network and the segmentation                                             experiments (Fig 5), we find that applying a MLP directly
network share a great portion of structures. Please read the                                      on the sorted point set performs poorly, though slightly
caption of Fig 2 for the pipeline.                                                                better than directly processing an unsorted input.
   Our network has three key modules: the max pooling                                                 The idea to use RNN considers the point set as a
layer as a symmetric function to aggregate information from                                       sequential signal and hopes that by training the RNN
with randomly permuted sequences, the RNN will become                Joint Alignment Network The semantic labeling of a
invariant to input order. However in “OrderMatters” [25]             point cloud has to be invariant if the point cloud undergoes
the authors have shown that order does matter and cannot be          certain geometric transformations, such as rigid transforma-
totally omitted. While RNN has relatively good robustness            tion. We therefore expect that the learnt representation by
to input ordering for sequences with small length (dozens),          our point set is invariant to these transformations.
it’s hard to scale to thousands of input elements, which is             A natural solution is to align all input set to a canonical
the common size for point sets. Empirically, we have also            space before feature extraction. Jaderberg et al. [9]
shown that model based on RNN does not perform as well               introduces the idea of spatial transformer to align 2D
as our proposed method (Fig 5).                                      images through sampling and interpolation, achieved by a
    Our idea is to approximate a general function defined on         specifically tailored layer implemented on GPU.
a point set by applying a symmetric function on transformed             Our input form of point clouds allows us to achieve this
elements in the set:                                                 goal in a much simpler way compared with [9]. We do not
                                                                     need to invent any new layers and no alias is introduced as in
         f ({x1 , . . . , xn }) ≈ g(h(x1 ), . . . , h(xn )),   (1)   the image case. We predict an affine transformation matrix
                  N
                                                                     by a mini-network (T-net in Fig 2) and directly apply this
where f : 2R    → R, h : RN → RK and g :                             transformation to the coordinates of input points. The mini-
  K          K
R × · · · × R → R is a symmetric function.                           network itself resembles the big network and is composed
|     {z     }
        n                                                            by basic modules of point independent feature extraction,
   Empirically, our basic module is very simple: we                  max pooling and fully connected layers. More details about
approximate h by a multi-layer perceptron network and                the T-net are in the supplementary.
g by a composition of a single variable function and a                  This idea can be further extended to the alignment of
max pooling function. This is found to work well by                  feature space, as well. We can insert another alignment net-
experiments. Through a collection of h, we can learn a               work on point features and predict a feature transformation
number of f ’s to capture different properties of the set.           matrix to align features from different input point clouds.
   While our key module seems simple, it has interesting             However, transformation matrix in the feature space has
properties (see Sec 5.3) and can achieve strong performace           much higher dimension than the spatial transform matrix,
(see Sec 5.1) in a few different applications. Due to the            which greatly increases the difficulty of optimization. We
simplicity of our module, we are also able to provide                therefore add a regularization term to our softmax training
theoretical analysis as in Sec 4.3.                                  loss. We constrain the feature transformation matrix to be
                                                                     close to orthogonal matrix:
Local and Global Information Aggregation The output
from the above section forms a vector [f1 , . . . , fK ], which                         Lreg = kI − AAT k2F ,                   (2)
is a global signature of the input set. We can easily
train a SVM or multi-layer perceptron classifier on the              where A is the feature alignment matrix predicted by a
shape global features for classification. However, point             mini-network. An orthogonal transformation will not lose
segmentation requires a combination of local and global              information in the input, thus is desired. We find that by
knowledge. We can achieve this by a simple yet highly                adding the regularization term, the optimization becomes
effective manner.                                                    more stable and our model achieves better performance.
    Our solution can be seen in Fig 2 (Segmentation Net-             4.3. Theoretical Analysis
work). After computing the global point cloud feature vec-
tor, we feed it back to per point features by concatenating          Universal approximation We first show the universal
the global feature with each of the point features. Then we          approximation ability of our neural network to continuous
extract new per point features based on the combined point           set functions. By the continuity of set functions, intuitively,
features - this time the per point feature is aware of both the      a small perturbation to the input point set should not
local and global information.                                        greatly change the function values, such as classification or
    With this modification our network is able to predict            segmentation scores.
per point quantities that rely on both local geometry and                Formally, let X = {S : S ⊆ [0, 1]m and |S| = n}, f :
global semantics. For example we can accurately predict              X → R is a continuous set function on X w.r.t to Hausdorff
per-point normals (fig in supplementary), validating that the        distance dH (·, ·), i.e., ∀ > 0, ∃δ > 0, for any S, S 0 ∈ X ,
network is able to summarize information from the point’s            if dH (S, S 0 ) < δ, then |f (S) − f (S 0 )| < . Our theorem
local neighborhood. In experiment session, we also show              says that f can be arbitrarily approximated by our network
that our model can achieve state-of-the-art performance on           given enough neurons at the max pooling layer, i.e., K in
shape part segmentation and scene segmentation.                      (1) is sufficiently large.
                                                                                                                                      input     #views   accuracy   accuracy
                                                 mug
                                                                                skateboard                                                               avg. class  overall
               table

                                                                     bag
                                                                                                               SPH [11]                mesh       -        68.2         -
                                                                                    pistol                     3DShapeNets [28] volume            1        77.3       84.7
          motorbike
                                        guitar
                                                                                                  earphone
                                                                                                               VoxNet [17]           volume      12        83.0       85.9
                        car
                                 lamp                        knife
                                                                                       rocket                  Subvolume [18]        volume      20        86.0       89.2
                                                                                                               LFD [28]               image      10        75.5         -
                                                                                                laptop
        airplane                                                                                               MVCNN [23]             image      80        90.1         -
                                             chair           cap
                                                                                                               Ours baseline           point      -        72.6       77.4
                       Partial Inputs                                      Complete Inputs
                                                                                                               Ours PointNet           point      1        86.2       89.2
Figure 3. Qualitative results for part segmentation. We                                                      Table 1. Classification results on ModelNet40. Our net achieves
visualize the CAD part segmentation results across all 16 object                                             state-of-the-art among deep nets on 3D input.
categories. We show both results for partial simulated Kinect scans
(left block) and complete ShapeNet CAD models (right block).
                                                                                                                We explain the implications of the theorem. (a) says that
                                                                                                             f (S) is unchanged up to the input corruption if all points
Theorem 1. Suppose f : X → R is a continuous
                                                                                                             in CS are preserved; it is also unchanged with extra noise
set function w.r.t Hausdorff distance dH (·, ·). ∀ >
                                                                                                             points up to NS . (b) says that CS only contains a bounded
0, ∃ a continuous function h and a symmetric function
                                                                                                             number of points, determined by K in (1). In other words,
g(x1 , . . . , xn ) = γ ◦ MAX, such that for any S ∈ X ,
                                                                                                             f (S) is in fact totally determined by a finite subset CS ⊆ S
                                                                                                           of less or equal to K elements. We therefore call CS the
                   f (S) − γ MAX {h(xi )} <                                                                 critical point set of S and K the bottleneck dimension of f .
                                                     xi ∈S
                                                                                                                Combined with the continuity of h, this explains the
where x1 , . . . , xn is the full list of elements in S ordered                                              robustness of our model w.r.t point perturbation, corruption
arbitrarily, γ is a continuous function, and MAX is a vector                                                 and extra noise points. The robustness is gained in analogy
max operator that takes n vectors as input and returns a                                                     to the sparsity principle in machine learning models.
new vector of the element-wise maximum.                                                                      Intuitively, our network learns to summarize a shape by
                                                                                                             a sparse set of key points. In experiment section we see
   The proof to this theorem can be found in our supple-                                                     that the key points form the skeleton of an object.
mentary material. The key idea is that in the worst case the
network can learn to convert a point cloud into a volumetric                                                 5. Experiment
representation, by partitioning the space into equal-sized
voxels. In practice, however, the network learns a much                                                         Experiments are divided into four parts. First, we show
smarter strategy to probe the space, as we shall see in point                                                PointNets can be applied to multiple 3D recognition tasks
function visualizations.                                                                                     (Sec 5.1). Second, we provide detailed experiments to
                                                                                                             validate our network design (Sec 5.2). At last we visualize
Bottleneck dimension and stability Theoretically and                                                         what the network learns (Sec 5.3) and analyze time and
experimentally we find that the expressiveness of our                                                        space complexity (Sec 5.4).
network is strongly affected by the dimension of the max                                                     5.1. Applications
pooling layer, i.e., K in (1). Here we provide an analysis,
which also reveals properties related to the stability of our                                                    In this section we show how our network can be
model.                                                                                                       trained to perform 3D object classification, object part
   We define u = MAX{h(xi )} to be the sub-network of f                                                      segmentation and semantic scene segmentation 1 . Even
                                 xi ∈S
                                                                                                             though we are working on a brand new data representation
which maps a point set in [0, 1]m to a K-dimensional vector.
                                                                                                             (point sets), we are able to achieve comparable or even
The following theorem tells us that small corruptions or
                                                                                                             better performance on benchmarks for several tasks.
extra noise points in the input set are not likely to change
the output of our network:
                                                                                                             3D Object Classification Our network learns global
Theorem 2. Suppose u : X → RK such that u =                                                                  point cloud feature that can be used for object classification.
MAX{h(xi )} and f = γ ◦ u. Then,                                                                             We evaluate our model on the ModelNet40 [28] shape
xi ∈S
                                                                                                             classification benchmark. There are 12,311 CAD models
(a) ∀S, ∃ CS , NS ⊆ X , f (T ) = f (S) if CS ⊆ T ⊆ NS ;                                                      from 40 man-made object categories, split into 9,843 for
(b) |CS | ≤ K                                                                                                   1 More application examples such as correspondence and point cloud

                                                                                                             based CAD model retrieval are included in supplementary material.
            mean     aero   bag   cap   car     chair ear      guitar knife lamp laptop motor mug pistol rocket skate table
                                                       phone                                                              board
 # shapes             2690 76      55     898 3758 69          787 392 1547 451            202    184 283 66              152   5271
 Wu [27]        -     63.2 -       -      -     73.5 -         -      -      74.4 -        -      -      -      -         -     74.8
 Yi [29]      81.4    81.0 78.4 77.7 75.7 87.6 61.9 92.0 85.4 82.5 95.7 70.6 91.9 85.9 53.1 69.8 75.3
 3DCNN        79.4    75.1 72.8 73.3 70.0 87.2 63.5 88.4 79.6 74.4 93.9 58.7 91.8 76.4 51.2 65.3 77.1
 Ours         83.7    83.4 78.7 82.5 74.9 89.6 73.0 91.5 85.9 80.8 95.3 65.2 93.0 81.2 57.9 72.8 80.6
Table 2. Segmentation results on ShapeNet part dataset. Metric is mIoU(%) on points. We compare with two traditional methods [27]
and [29] and a 3D fully convolutional network baseline proposed by us. Our PointNet method achieved the state-of-the-art in mIoU.

training and 2,468 for testing. While previous methods               correspondences between shapes, as well as our own
focus on volumetric and mult-view image representations,             3D CNN baseline. See supplementary for the detailed
we are the first to directly work on raw point cloud.                modifications and network architecture for the 3D CNN.
    We uniformly sample 1024 points on mesh faces accord-               In Table 2, we report per-category and mean IoU(%)
ing to face area and normalize them into a unit sphere.              scores. We observe a 2.3% mean IoU improvement and our
During training we augment the point cloud on-the-fly by             net beats the baseline methods in most categories.
randomly rotating the object along the up-axis and jitter the           We also perform experiments on simulated Kinect scans
position of each points by a Gaussian noise with zero mean           to test the robustness of these methods. For every CAD
and 0.02 standard deviation.                                         model in the ShapeNet part data set, we use Blensor Kinect
    In Table 1, we compare our model with previous works             Simulator [7] to generate incomplete point clouds from six
as well as our baseline using MLP on traditional features            random viewpoints. We train our PointNet on the complete
extracted from point cloud (point density, D2, shape contour         shapes and partial scans with the same network architecture
etc.). Our model achieved state-of-the-art performance               and training setting. Results show that we lose only 5.3%
among methods based on 3D input (volumetric and point                mean IoU. In Fig 3, we present qualitative results on both
cloud). With only fully connected layers and max pooling,            complete and partial data. One can see that though partial
our net gains a strong lead in inference speed and can be            data is fairly challenging, our predictions are reasonable.
easily parallelized in CPU as well. There is still a small
gap between our method and multi-view based method
                                                                     Semantic Segmentation in Scenes Our network on part
(MVCNN [23]), which we think is due to the loss of fine
                                                                     segmentation can be easily extended to semantic scene
geometry details that can be captured by rendered images.
                                                                     segmentation, where point labels become semantic object
                                                                     classes instead of object part labels.
3D Object Part Segmentation Part segmentation is a                      We experiment on the Stanford 3D semantic parsing data
challenging fine-grained 3D recognition task. Given a 3D             set [1]. The dataset contains 3D scans from Matterport
scan or a mesh model, the task is to assign part category            scanners in 6 areas including 271 rooms. Each point in the
label (e.g. chair leg, cup handle) to each point or face.            scan is annotated with one of the semantic labels from 13
   We evaluate on ShapeNet part data set from [29], which            categories (chair, table, floor, wall etc. plus clutter).
contains 16,881 shapes from 16 categories, annotated with               To prepare training data, we firstly split points by room,
50 parts in total. Most object categories are labeled with           and then sample rooms into blocks with area 1m by 1m.
two to five parts. Ground truth annotations are labeled on           We train our segmentation version of PointNet to predict
sampled points on the shapes.
   We formulate part segmentation as a per-point classifi-
cation problem. Evaluation metric is mIoU on points. For                                          mean IoU overall accuracy
                                                                               Ours baseline        20.12           53.19
each shape S of category C, to calculate the shape’s mIoU:
                                                                               Ours PointNet        47.71           78.62
For each part type in category C, compute IoU between
                                                                     Table 3. Results on semantic segmentation in scenes. Metric is
groundtruth and prediction. If the union of groundtruth and          average IoU over 13 classes (structural and furniture elements plus
prediction points is empty, then count part IoU as 1. Then           clutter) and classification accuracy calculated on points.
we average IoUs for all part types in category C to get mIoU
for that shape. To calculate mIoU for the category, we take                                 table    chair     sofa board mean
average of mIoUs for all shapes in that category.                      # instance            455     1363       55   137
   In this section, we compare our segmentation version                Armeni et al. [1] 46.02 16.15 6.78            3.91     18.22
PointNet (a modified version of Fig 2, Segmentation                    Ours                46.67 33.80        4.76 11.72 24.24
Network) with two traditional methods [27] and [29] that             Table 4. Results on 3D object detection in scenes. Metric is
both take advantage of point-wise geometry features and              average precision with threshold IoU 0.5 computed in 3D volumes.
                                                                        rnn            rnn               rnn

                                                                                                                  MLP
                                                                        cell           cell
                                                                                              ...        cell

                                                                       MLP             MLP               MLP
      Input

                                                                      (1,2,3)     (2,3,4)     ...       (1,3,1)
                                                                                 sequential model
                                                                     sorted
                                                                     (1,2,3)                  (1,2,3)       MLP

                                                                     (1,3,1)                  (2,3,4)       MLP

                                                                                 MLP

                                                                                                                        MLP
                                                                                              ...
                                                                     ...
                                                                     (2,3,4)                  (1,3,1)       MLP
      Output

                                                                       sorting                  symmetry function

                                                                     Figure 5. Three approaches to achieve order invariance. Multi-
                                                                     layer perceptron (MLP) applied on points consists of 5 hidden
                                                                     layers with neuron sizes 64,64,64,128,1024, all points share a
Figure 4. Qualitative results for semantic segmentation. Top
                                                                     single copy of MLP. The MLP close to the output consists of two
row is input point cloud with color. Bottom row is output semantic
                                                                     layers with sizes 512,256.
segmentation result (on points) displayed in the same camera
viewpoint as input.
                                                                     points as n×3 arrays, RNN model that considers input point
per point class in each block. Each point is represented by          as a sequence, and a model based on symmetry functions.
a 9-dim vector of XYZ, RGB and normalized location as                The symmetry operation we experimented include max
to the room (from 0 to 1). At training time, we randomly             pooling, average pooling and an attention based weighted
sample 4096 points in each block on-the-fly. At test time,           sum. The attention method is similar to that in [25], where
we test on all the points. We follow the same protocol as [1]        a scalar score is predicted from each point feature, then the
to use k-fold strategy for train and test.                           score is normalized across points by computing a softmax.
   We compare our method with a baseline using hand-                 The weighted sum is then computed on the normalized
crafted point features. The baseline extracts the same 9-            scores and the point features. As shown in Fig 5, max-
dim local features and three additional ones: local point            pooling operation achieves the best performance by a large
density, local curvature and normal. We use standard MLP             winning margin, which validates our choice.
as the classifier. Results are shown in Table 3, where
our PointNet method significantly outperforms the baseline           Effectiveness of Input and Feature Transformations In
method. In Fig 4, we show qualitative segmentation results.          Table 5 we demonstrate the positive effects of our input
Our network is able to output smooth predictions and is              and feature transformations (for alignment). It’s interesting
robust to missing points and occlusions.                             to see that the most basic architecture already achieves
   Based on the semantic segmentation output from our                quite reasonable results. Using input transformation gives
network, we further build a 3D object detection system               a 0.8% performance boost. The regularization loss is
using connected component for object proposal (see sup-              necessary for the higher dimension transform to work.
plementary for details). We compare with previous state-             By combining both transformations and the regularization
of-the-art method in Table 4. The previous method is based           term, we achieve the best performance.
on a sliding shape method (with CRF post processing) with
SVMs trained on local geometric features and global room             Robustness Test We show our PointNet, while simple
context feature in voxel grids. Our method outperforms it            and effective, is robust to various kinds of input corruptions.
by a large margin on the furniture categories reported.              We use the same architecture as in Fig 5’s max pooling
5.2. Architecture Design Analysis                                    network. Input points are normalized into a unit sphere.
                                                                     Results are in Fig 6.
   In this section we validate our design choices by control            As to missing points, when there are 50% points missing,
experiments. We also show the effects of our network’s               the accuracy only drops by 2.4% and 3.8% w.r.t. furthest
hyperparameters.                                                     and random input sampling. Our net is also robust to outlier

Comparison with Alternative Order-invariant Methods                                   Transform              accuracy
As mentioned in Sec 4.2, there are at least three options for                         none                      87.1
consuming unordered set inputs. We use the ModelNet40                                 input (3x3)               87.9
shape classification problem as a test bed for comparisons                            feature (64x64)           86.9
of those options, the following two control experiment will                           feature (64x64) + reg.    87.4
also use this task.                                                                   both                      89.2
   The baselines (illustrated in Fig 5) we compared with             Table 5. Effects of input feature transforms. Metric is overall
include multi-layer perceptron on unsorted and sorted                classification accuracy on ModelNet40 test set.
               100                                                      100                                                         90
                90                                                       90
                                                                         80
                                                                                                                                    80                                    5.4. Time and Space Complexity Analysis
Accuracy (%)

                                                         Accuracy (%)

                                                                                                                     Accuracy (%)
                80
                                                                         70                                                         70
                70
                                                                         60                                                         60
                60
                         Furthest                                        50         XYZ                                             50
                                                                                                                                                                             Table 6 summarizes space (number of parameters in
                50                                                       40
                40       Random                                          30
                                                                                    XYZ+density                                     40                                    the network) and time (floating-point operations/sample)
                30                                                       20                                                         30
                     0    0.2   0.4    0.6     0.8   1                        0.1    0.2       0.3       0.4   0.5                       0           0.05           0.1   complexity of our classification PointNet. We also compare
                             Missing data ratio                                            Outlier ratio                                     Perturbation noise std
                                                                                                                                                                          PointNet to a representative set of volumetric and multi-
 Figure 6. PointNet robustness test. The metric is overall
                                                                                                                                                                          view based architectures in previous works.
 classification accuracy on ModelNet40 test set. Left: Delete
 points. Furthest means the original 1024 points are sampled with                                                                                                            While MVCNN [23] and Subvolume (3D CNN) [18]
 furthest sampling. Middle: Insertion. Outliers uniformly scattered                                                                                                       achieve high performance, PointNet is orders more efficient
 in the unit sphere. Right: Perturbation. Add Gaussian noise to                                                                                                           in computational cost (measured in FLOPs/sample: 141x
 each point independently.                                                                                                                                                and 8x more efficient, respectively). Besides, PointNet
                                                                                                                                                                          is much more space efficient than MVCNN in terms of
                                                                                                                                                                          #param in the network (17x less parameters). Moreover,
 points, if it has seen those during training. We evaluate two                                                                                                            PointNet is much more scalable – it’s space and time
 models: one trained on points with (x, y, z) coordinates; the                                                                                                            complexity is O(N ) – linear in the number of input points.
 other on (x, y, z) plus point density. The net has more than                                                                                                             However, since convolution dominates computing time,
 80% accuracy even when 20% of the points are outliers.                                                                                                                   multi-view method’s time complexity grows squarely on
 Fig 6 right shows the net is robust to point perturbations.                                                                                                              image resolution and volumetric convolution based method
                                                                                                                                                                          grows cubically with the volume size.
 5.3. Visualizing PointNet                                                                                                                                                   Empirically, PointNet is able to process more than
    In Fig 7, we visualize critical point sets CS and upper-                                                                                                              one million points per second for point cloud classifica-
 bound shapes NS (as discussed in Thm 2) for some sample                                                                                                                  tion (around 1K objects/second) or semantic segmentation
 shapes S. The point sets between the two shapes will give                                                                                                                (around 2 rooms/second) with a 1080X GPU on Tensor-
 exactly the same global shape feature f (S).                                                                                                                             Flow, showing great potential for real-time applications.
    We can see clearly from Fig 7 that the critical point
 sets CS , those contributed to the max pooled feature,                                                                                                                                                #params     FLOPs/sample
 summarizes the skeleton of the shape. The upper-bound                                                                                                                          PointNet (vanilla)     0.8M        148M
 shapes NS illustrates the largest possible point cloud that                                                                                                                    PointNet               3.5M        440M
 give the same global shape feature f (S) as the input point                                                                                                                    Subvolume [18]         16.6M       3633M
 cloud S. CS and NS reflect the robustness of PointNet,                                                                                                                         MVCNN [23]             60.0M       62057M
 meaning that losing some non-critical points does not                                                                                                                    Table 6. Time and space complexity of deep architectures for
 change the global shape signature f (S) at all.                                                                                                                          3D data classification. PointNet (vanilla) is the classification
    The NS is constructed by forwarding all the points in a                                                                                                               PointNet without input and feature transformations. FLOP
                                                                                                                                                                          stands for floating-point operation. The “M” stands for million.
 edge-length-2 cube through the network and select points p
                                                                                                                                                                          Subvolume and MVCNN used pooling on input data from multiple
 whose point function values (h1 (p), h2 (p), · · · , hK (p)) are
                                                                                                                                                                          rotations or views, without which they have much inferior
 no larger than the global shape descriptor.                                                                                                                              performance.

                                                                                                                                                                          6. Conclusion
                         Original Shape

                                                                                                                                                                             In this work, we propose a novel deep neural network
                                                                                                                                                                          PointNet that directly consumes point cloud. Our network
                         Critical Point Sets

                                                                                                                                                                          provides a unified approach to a number of 3D recognition
                                                                                                                                                                          tasks including object classification, part segmentation and
                                                                                                                                                                          semantic segmentation, while obtaining on par or better
                                                                                                                                                                          results than state of the arts on standard benchmarks. We
                         Upper-bound Shapes

                                                                                                                                                                          also provide theoretical analysis and visualizations towards
                                                                                                                                                                          understanding of our network.

 Figure 7. Critical points and upper bound shape. While critical                                                                                                          Acknowledgement. The authors gratefully acknowledge
 points jointly determine the global shape feature for a given shape,                                                                                                     the support of a Samsung GRO grant, ONR MURI N00014-
 any point cloud that falls between the critical points set and the                                                                                                       13-1-0341 grant, NSF grant IIS-1528025, a Google Fo-
 upper bound shape gives exactly the same feature. We color-code                                                                                                          cused Research Award, a gift from the Adobe corporation
 all figures to show the depth information.                                                                                                                               and hardware donations by NVIDIA.
References                                                          [16] J. Masci, D. Boscaini, M. Bronstein, and P. Vandergheynst.
                                                                         Geodesic convolutional neural networks on riemannian man-
 [1] I. Armeni, O. Sener, A. R. Zamir, H. Jiang, I. Brilakis,            ifolds. In Proceedings of the IEEE International Conference
     M. Fischer, and S. Savarese. 3d semantic parsing of                 on Computer Vision Workshops, pages 37–45, 2015. 2
     large-scale indoor spaces. In Proceedings of the IEEE
                                                                    [17] D. Maturana and S. Scherer. Voxnet: A 3d convolutional
     International Conference on Computer Vision and Pattern
                                                                         neural network for real-time object recognition. In IEEE/RSJ
     Recognition, 2016. 6, 7
                                                                         International Conference on Intelligent Robots and Systems,
 [2] M. Aubry, U. Schlickewei, and D. Cremers. The wave                  September 2015. 2, 5, 10, 11
     kernel signature: A quantum mechanical approach to shape       [18] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas.
     analysis. In Computer Vision Workshops (ICCV Workshops),            Volumetric and multi-view cnns for object classification on
     2011 IEEE International Conference on, pages 1626–1633.             3d data. In Proc. Computer Vision and Pattern Recognition
     IEEE, 2011. 2                                                       (CVPR), IEEE, 2016. 2, 5, 8
 [3] M. M. Bronstein and I. Kokkinos. Scale-invariant heat          [19] R. B. Rusu, N. Blodow, and M. Beetz. Fast point feature
     kernel signatures for non-rigid shape recognition.        In        histograms (fpfh) for 3d registration. In Robotics and
     Computer Vision and Pattern Recognition (CVPR), 2010                Automation, 2009. ICRA’09. IEEE International Conference
     IEEE Conference on, pages 1704–1711. IEEE, 2010. 2                  on, pages 3212–3217. IEEE, 2009. 2
 [4] J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun. Spectral         [20] R. B. Rusu, N. Blodow, Z. C. Marton, and M. Beetz. Align-
     networks and locally connected networks on graphs. arXiv            ing point cloud views using persistent feature histograms.
     preprint arXiv:1312.6203, 2013. 2                                   In 2008 IEEE/RSJ International Conference on Intelligent
 [5] D.-Y. Chen, X.-P. Tian, Y.-T. Shen, and M. Ouhyoung. On             Robots and Systems, pages 3384–3391. IEEE, 2008. 2
     visual similarity based 3d model retrieval. In Computer        [21] M. Savva, F. Yu, H. Su, M. Aono, B. Chen, D. Cohen-Or,
     graphics forum, volume 22, pages 223–232. Wiley Online              W. Deng, H. Su, S. Bai, X. Bai, et al. Shrec16 track large-
     Library, 2003. 2                                                    scale 3d shape retrieval from shapenet core55. 2
 [6] Y. Fang, J. Xie, G. Dai, M. Wang, F. Zhu, T. Xu, and           [22] P. Y. Simard, D. Steinkraus, and J. C. Platt. Best practices for
     E. Wong. 3d deep shape descriptor. In Proceedings                   convolutional neural networks applied to visual document
     of the IEEE Conference on Computer Vision and Pattern               analysis. In ICDAR, volume 3, pages 958–962, 2003. 13
     Recognition, pages 2319–2328, 2015. 2                          [23] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller.
 [7] M. Gschwandtner, R. Kwitt, A. Uhl, and W. Pree. BlenSor:            Multi-view convolutional neural networks for 3d shape
     Blender Sensor Simulation Toolbox Advances in Visual                recognition. In Proc. ICCV, to appear, 2015. 2, 5, 6, 8
     Computing. volume 6939 of Lecture Notes in Computer            [24] J. Sun, M. Ovsjanikov, and L. Guibas. A concise and
     Science, chapter 20, pages 199–208. Springer Berlin /               provably informative multi-scale signature based on heat
     Heidelberg, Berlin, Heidelberg, 2011. 6                             diffusion. In Computer graphics forum, volume 28, pages
 [8] K. Guo, D. Zou, and X. Chen. 3d mesh labeling via                   1383–1392. Wiley Online Library, 2009. 2
     deep convolutional neural networks. ACM Transactions on        [25] O. Vinyals, S. Bengio, and M. Kudlur.              Order mat-
     Graphics (TOG), 35(1):3, 2015. 2                                    ters: Sequence to sequence for sets.           arXiv preprint
 [9] M. Jaderberg, K. Simonyan, A. Zisserman, et al. Spatial             arXiv:1511.06391, 2015. 2, 4, 7
     transformer networks. In NIPS 2015. 4                          [26] D. Z. Wang and I. Posner. Voting for voting in online point
[10] A. E. Johnson and M. Hebert. Using spin images for efficient        cloud object detection. Proceedings of the Robotics: Science
     object recognition in cluttered 3d scenes. IEEE Transactions        and Systems, Rome, Italy, 1317, 2015. 2
     on pattern analysis and machine intelligence, 21(5):433–       [27] Z. Wu, R. Shou, Y. Wang, and X. Liu. Interactive shape co-
     449, 1999. 2                                                        segmentation via label propagation. Computers & Graphics,
[11] M. Kazhdan, T. Funkhouser, and S. Rusinkiewicz. Rotation            38:248–254, 2014. 6, 10
     invariant spherical harmonic representation of 3 d shape de-   [28] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and
     scriptors. In Symposium on geometry processing, volume 6,           J. Xiao. 3d shapenets: A deep representation for volumetric
     pages 156–164, 2003. 5                                              shapes. In Proceedings of the IEEE Conference on Computer
[12] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-           Vision and Pattern Recognition, pages 1912–1920, 2015. 2,
     based learning applied to document recognition. Proceed-            5, 11
     ings of the IEEE, 86(11):2278–2324, 1998. 13                   [29] L. Yi, V. G. Kim, D. Ceylan, I.-C. Shen, M. Yan, H. Su,
[13] Y. Li, S. Pirk, H. Su, C. R. Qi, and L. J. Guibas. Fpnn:            C. Lu, Q. Huang, A. Sheffer, and L. Guibas. A scalable active
     Field probing neural networks for 3d data. arXiv preprint           framework for region annotation in 3d shape collections.
     arXiv:1605.06240, 2016. 2                                           SIGGRAPH Asia, 2016. 6, 10, 18
[14] H. Ling and D. W. Jacobs. Shape classification using the
     inner-distance. IEEE transactions on pattern analysis and
     machine intelligence, 29(2):286–299, 2007. 2
[15] L. v. d. Maaten and G. Hinton. Visualizing data using t-sne.
     Journal of Machine Learning Research, 9(Nov):2579–2605,
     2008. 15
                                                                              PointNet VoxNet
                                                                          0         87.1      86.3
                                                                        0.5         83.3       46
                                                                       0.75           74      18.5
                                                                     0.875          59.2      13.3
                                                                    0.9375          33.2      10.2

Supplementary                                                                                  100

                                                                                                80
A. Overview

                                                                                Accuracy (%)
                                                                                                60
    This document provides additional quantitative results,
technical details and more qualitative test examples to the                                     40
main paper.                                                                                              PointNet
    In Sec B we extend the robustness test to compare                                           20
                                                                                                         VoxNet
PointNet with VoxNet on incomplete input. In Sec C                                               0
we provide more details on neural network architectures,                                             0   0.2      0.4   0.6   0.8   1
training parameters and in Sec D we describe our detection                                      Missing Data Ratio
pipeline in scenes. Then Sec E illustrates more applications       Figure 8. PointNet v.s. VoxNet [17] on incomplete input data.
of PointNet, while Sec F shows more analysis experiments.          Metric is overall classification accurcacy on ModelNet40 test set.
Sec G provides a proof for our theory on PointNet. At last,        Note that VoxNet is using 12 viewpoints averaging while PointNet
we show more visualization results in Sec H.                       is using only one view of the point cloud. Evidently PointNet
                                                                   presents much stronger robustness to missing points.
B. Comparison between PointNet and VoxNet
    (Sec 5.2)
                                                                   transformation network has the same architecture as the first
    We extend the experiments in Sec 5.2 Robustness Test           one except that the output is a 64 × 64 matrix. The matrix
to compare PointNet and VoxNet [17] (a representative              is also initialized as an identity. A regularization loss (with
architecture for volumetric representation) on robustness to       weight 0.001) is added to the softmax classification loss to
missing data in the input point cloud. Both networks are           make the matrix close to orthogonal.
trained on the same train test split with 1024 number of               We use dropout with keep ratio 0.7 on the last fully
points as input. For VoxNet we voxelize the point cloud            connected layer, whose output dimension 256, before class
to 32 × 32 × 32 occupancy grids and augment the training           score prediction. The decay rate for batch normalization
data by random rotation around up-axis and jittering.              starts with 0.5 and is gradually increased to 0.99. We use
    At test time, input points are randomly dropped out            adam optimizer with initial learning rate 0.001, momentum
by a certain ratio. As VoxNet is sensitive to rotations,           0.9 and batch size 32. The learning rate is divided by 2
its prediction uses average scores from 12 viewpoints of           every 20 epochs. Training on ModelNet takes 3-6 hours to
a point cloud. As shown in Fig 8, we see that our                  converge with TensorFlow and a GTX1080 GPU.
PointNet is much more robust to missing points. VoxNet’s
accuracy dramatically drops when half of the input points
                                                                   PointNet Segmentation Network The segmentation net-
are missing, from 86.3% to 46.0% with a 40.3% difference,
                                                                   work is an extension to the classification PointNet. Local
while our PointNet only has a 3.7% performance drop. This
                                                                   point features (the output after the second transformation
can be explained by the theoretical analysis and explanation
                                                                   network) and global feature (output of the max pooling)
of our PointNet – it is learning to use a collection of critical
                                                                   are concatenated for each point. No dropout is used for
points to summarize the shape, thus it is very robust to
                                                                   segmentation network. Training parameters are the same
missing data.
                                                                   as the classification network.
C. Network Architecture and Training Details                          As to the task of shape part segmentation, we made
                                                                   a few modifications to the basic segmentation network
    (Sec 5.1)
                                                                   architecture (Fig 2 in main paper) in order to achieve best
PointNet Classification Network As the basic archi-                performance, as illustrated in Fig 9. We add a one-hot
tecture is already illustrated in the main paper, here we          vector indicating the class of the input and concatenate it
provides more details on the joint alignment/transformation        with the max pooling layer’s output. We also increase
network and training parameters.                                   neurons in some layers and add skip links to collect local
    The first transformation network is a mini-PointNet that       point features in different layers and concatenate them to
takes raw point cloud as input and regresses to a 3 × 3            form point feature input to the segmentation network.
matrix. It’s composed of a shared M LP (64, 128, 1024)                While [27] and [29] deal with each object category
network (with layer output sizes 64, 128, 1024) on each            independently, due to the lack of training data for some
point, a max pooling across points and two fully connected         categories (the total number of shapes for all the categories
layers with output sizes 512, 256. The output matrix is            in the data set are shown in the first line), we train our
initialized as an identity matrix. All layers, except the last     PointNet across categories (but with one-hot vector input to
one, include ReLU and batch normalization. The second              indicate category). To allow fair comparison, when testing
                                                                                                                                                                 batch normalization are used for all layers except the last
                          input points

                                         T1         FC          FC            FC           T2               FC              FC                2048

                                                                                                                                   nx2048
                                                                     nx128

                                                                                   nx128

                                                                                                  nx128

                                                                                                                    nx512
                                                         nx64
                              nx3

                                                                                                                                                                 one. The network is trained across categories, however, in
                                              nx3

                                                                                                                                                                 order to compare with other baseline methods where object
                                                                                                                                                                 category is given, we only consider output scores in the
                                                                                                                                       MLP

                                                                                                                                                   part scores
                                                                                                                                   (256,256,128)                 given object category.

                                                                                                            nx512
                                                                               nx128
                                                                                       nx128
                                                                                               nx128

                                                                                                                                                     nx50
                                                                       nx64

                                                                                                                                 one-hot
                                                                                                                                                                 D. Details on Detection Pipeline (Sec 5.1)
                                                                                               n x 3024
                            Figure 9. Network architecture for part segmentation. T1 and                                                              We build a simple 3D object detection system based on
                            T2 are alignment/transformation networks for input points and                                                         the semantic k segmentation results and our object classifica-
                            features. FC is fully connected layer operating on each point. MLP                                                    tion PointNet.
                            is multi-layer perceptron on each point. One-hot is a vector of size                                                      We use connected component with segmentation scores
               Classification Network

                                                                                                                                                                              output scores
                            16 indicating category of the input shape.
                        input           mlp (64,128,128)                  feature             mlp  (64,128,1024)                      max         to  get  object
                                                                                                                                                           mlp      proposals in scenes. Starting from a random

                                                                                                                                                                        nxm
                     transform                                          transform
input points

                                                                                                                                      pool 1024point(512,256,k)
                                                                                                                                                          in the scene, we find its predicted label and use
                                            32 filters          32 filters           32 filters           32 filters
                                                                                                          nx64
                                                                     nx64
               nx3

                                     nx3

                                            of shared
                                               stride 1         of stride 1          of stride 1          of stride 1 nx1024
                                                                                                      shared                                      BFS to search nearby points with the same label, with
                                                                                                                                         global feature
                                                                                                                                                  a search radius of 0.2 meter. If the resulted cluster has
                                                                                                                                                  moreoutput
                                                                                                                                                          thanscores
                                                                                                                                                                 200 points (assuming a 4096 point sample in
                                      5                  5                      5                  5                    3
                                                                                                                               point features a 1m by 1m area), the cluster’s bounding box is marked
                              3x3                                  64x64
                      T-Net        32
                              transform                32 T-Net    transform 32                  32                  32       32 filters          as one object proposal. For each proposed object, it’s
                                                                                                                                                         nx128

                                                                                             n x 1088                         of stride 1
                             matrix                               matrix                                               shared                     detection score is computed as the average point score for
                                                                                                                                                shared
                            multiply                             multiply
                                                                                                                                                  that category. Before evaluation, proposals with extremely
                                                                                                               mlp (512,256,128)             mlp small
                                                                                                                                                  (128,m) areas/volumes are pruned. For tables, chairs and
                                                        1                     1                     1                     1
                                                                                   Segmentation Network
                                                                                                                                                  sofas, the bounding boxes are extended to the floor in case
                                                                                                32       64 filters 32
                                  32 in-category 32 50 filters              32    64 filters                                                      the legs are separated with the seat/surface.
                                        prediction           of stride 1          of stride 1            of stride 1
                                                                                                                                                      We observe that in some rooms such as auditoriums
                            Figure 10. Baseline 3D CNN segmentation network. The
                            network is fully convolutional and predicts part scores for each
                                                                                                                                                  lots  of objects (e.g. chairs) are close to each other, where
                            voxel.                                                                                                                connected     component would fail to correctly segment out
                                                                                                                                                  individual ones. Therefore we leverage our classification
                                                                                                                                                  network and uses sliding shape method to alleviate the
                            these two models, we only predict part labels for the given                                                           problem for the chair class. We train a binary classification
                            specific object category.                                                                                             network for each category and use the classifier for sliding
                                   As to semantic segmentation task, we used the architec-                                                        window detection. The resulted boxes are pruned by
                            ture as in Fig 2 in the main paper.                                                                                   non-maximum suppression. The proposed boxes from
                                   It takes around six to twelve hours to train the model on                                                      connected component and sliding shapes are combined for
                            ShapeNet part dataset and around half a day to train on the                                                           final evaluation.
                            Stanford semantic parsing dataset.                                                                                        In Fig 11, we show the precision-recall curves for object
                                                                                                                                                  detection. We trained six models, where each one of them
                                                                                                                                                  is trained on five areas and tested on the left area. At test
                            Baseline 3D CNN Segmentation Network In ShapeNet                                                                      phase, each model is tested on the area it has never seen.
                            part segmentation experiment, we compare our proposed                                                                 The test results for all six areas are aggregated for the PR
                            segmentation version PointNet to two traditional methods                                                              curve generation.
                            as well as a 3D volumetric CNN network baseline. In
                            Fig 10, we show the baseline 3D volumetric CNN network
                                                                                                                                                  E. More Applications (Sec 5.1)
                            we use. We generalize the well-known 3D CNN architec-
                            tures, such as VoxNet [17] and 3DShapeNets [28] to a fully                                                            Model Retrieval from Point Cloud Our PointNet learns
                            convolutional 3D CNN segmentation network.                                                                            a global shape signature for every given input point cloud.
                                   For a given point cloud, we first convert it to the volu-                                                      We expect geometrically similar shapes have similar global
                            metric representation as a occupancy grid with resolution                                                             signature. In this section, we test our conjecture on the
                            32 × 32 × 32. Then, five 3D convolution operations each                                                               shape retrieval application. To be more specific, for every
                            with 32 output channels and stride of 1 are sequentially                                                              given query shape from ModelNet test split, we compute
                            applied to extract features. The receptive field is 19 for each                                                       its global signature (output of the layer before the score
                            voxel. Finally, a sequence of 3D convolutional layers with                                                            prediction layer) given by our classification PointNet and
                            kernel size 1 × 1 × 1 is appended to the computed feature                                                             retrieve similar shapes in the train split by nearest neighbor
                            map to predict segmentation label for each voxel. ReLU and                                                            search. Results are shown in Fig 12.
Figure 11. Precision-recall curves for object detection in 3D        Figure 13. Shape correspondence between two chairs. For the
point cloud. We evaluated on all six areas for four categories:      clarity of the visualization, we only show 20 randomly picked
table, chair, sofa and board. IoU threshold is 0.5 in volume.        correspondence pairs.
  Query                       Top-5 Retrieval CAD Models
Point Cloud

                                                                     Figure 14. Shape correspondence between two tables. For the
                                                                     clarity of the visualization, we only show 20 randomly picked
                                                                     correspondence pairs.

                                                                     64 to 1024 results in a 2−4% performance gain. It indicates
Figure 12. Model retrieval from point cloud. For every               that we need enough point feature functions to cover the 3D
given point cloud, we retrieve the top-5 similar shapes from the     space in order to discriminate different shapes.
ModelNet test split. From top to bottom rows, we show examples          It’s worth notice that even with 64 points as input
of chair, plant, nightstand and bathtub queries. Retrieved results   (obtained from furthest point sampling on meshes), our
that are in wrong category are marked by red boxes.                  network can achieve decent performance.

                                                                                          88
Shape Correspondence In this section, we show that                                        87                                            #points
                                                                           Accuracy (%)

point features learnt by PointNet can be potentially used                                 86                                              64

to compute shape correspondences. Given two shapes, we                                    85                                              128
                                                                                          84
compute the correspondence between their critical point                                                                                   512
                                                                                          83
sets CS ’s by matching the pairs of points that activate                                  82                                              1024
the same dimensions in the global features. Fig 13 and                                    81                                              2048
Fig 14 show the detected shape correspondence between                                          0   200   400    600        800   1000
two similar chairs and tables.                                                                           Bottleneck size
                                                                     Figure 15. Effects of bottleneck size and number of input
                                                                     points. The metric is overall classification accuracy on Model-
F. More Architecture Analysis (Sec 5.2)
                                                                     Net40 test set.
Effects of Bottleneck Dimension and Number of Input
Points Here we show our model’s performance change
with regard to the size of the first max layer output as             MNIST Digit Classification While we focus on 3D point
well as the number of input points. In Fig 15 we see that            cloud learning, a sanity check experiment is to apply our
performance grows as we increase the number of points                network on a 2D point clouds - pixel sets.
however it saturates at around 1K points. The max layer                 To convert an MNIST image into a 2D point set we
size plays an important role, increasing the layer size from         threshold pixel values and add the pixel (represented as a
point with (x, y) coordinate in the image) with values larger
than 128 to the set. We use a set size of 256. If there are
more than 256 pixels int he set, we randomly sub-sample it;
if there are less, we pad the set with the one of the pixels in
the set (due to our max operation, which point to use for the
padding will not affect outcome).
    As seen in Table 7, we compare with a few baselines
including multi-layer perceptron that considers input image
as an ordered vector, a RNN that consider input as sequence
from pixel (0,0) to pixel (27,27), and a vanilla version CNN.
While the best performing model on MNIST is still well
engineered CNNs (achieving less than 0.3% error rate),
it’s interesting to see that our PointNet model can achieve
reasonable performance by considering image as a 2D point
set.
                                        input       error (%)
    Multi-layer perceptron [22]        vector          1.60
    LeNet5 [12]                        image           0.80
    Ours PointNet                     point set        0.78
Table 7. MNIST classification results. We compare with vanilla
versions of other deep architectures to show that our network based
on point sets input is achieving reasonable performance on this
traditional task.
                                                                              Prediction                    Ground-truth
                                                                      Figure 16. PointNet normal reconstrution results. In this figure,
Normal Estimation In segmentation version of PointNet,                we show the reconstructed normals for all the points in some
local point features and global feature are concatenated              sample point clouds and the ground-truth normals computed on
in order to provide context to local points. However,                 the mesh.
it’s unclear whether the context is learnt through this
concatenation. In this experiment, we validate our design
                                                                      we illustrate the segmentation results for the given input
by showing that our segmentation network can be trained
                                                                      point clouds S (the left-most column), the critical point sets
to predict point normals, a local geometric property that is
                                                                      CS (the middle column) and the upper-bound shapes NS .
determined by a point’s neighborhood.
    We train a modified version of our segmentation Point-
Net in a supervised manner to regress to the ground-                  Network Generalizability to Unseen Shape Categories
truth point normals. We just change the last layer of our             In Fig 18, we visualize the critical point sets and the upper-
segmentation PointNet to predict normal vector for each               bound shapes for new shapes from unseen categories (face,
point. We use absolute value of cosine distance as loss.              house, rabbit, teapot) that are not present in ModelNet or
    Fig. 16 compares our PointNet normal prediction results           ShapeNet. It shows that the learnt per-point functions are
(the left columns) to the ground-truth normals computed               generalizable. However, since we train mostly on man-
from the mesh (the right columns).          We observe a              made objects with lots of planar structures, the recon-
reasonable normal reconstruction. Our predictions are                 structed upper-bound shape in novel categories also contain
more smooth and continuous than the ground-truth which                more planar surfaces.
includes flipped normal directions in some region.
                                                                      G. Proof of Theorem (Sec 4.3)
Segmentation Robustness As discussed in Sec 5.2 and                      Let X = {S : S ⊆ [0, 1] and |S| = n}.
Sec B, our PointNet is less sensitive to data corruption and             f : X → R is a continuous function on X w.r.t to
missing points for classification tasks since the global shape        Hausdorff distance dH (·, ·) if the following condition is
feature is extracted from a collection of critical points from        satisfied:
the given input point cloud. In this section, we show that the           ∀ > 0, ∃δ > 0, for any S, S 0 ∈ X , if dH (S, S 0 ) < δ,
robustness holds for segmentation tasks too. The per-point            then |f (S) − f (S 0 )| < .
part labels are predicted based on the combination of per-               We show that f can be approximated arbitrarily by
point features and the learnt global shape feature. In Fig 17,        composing a symmetric function and a continuous function.
                                                                                     order,

                                                                                     Proof. By the continuity of f , we take δ so that |f (S) −
                                                                                     f (S 0 )| <  for any S, S 0 ∈ X if dH (S, S 0 ) < δ .
                                                                                        Define K = d1/δ e, which split [0, 1] into K intervals
                                                                                     evenly and define an auxiliary function that maps a point to
                                                                                     the left end of the interval it lies in:
                                                                                                                           bKxc
                                                                                                                σ(x) =
                                                                                                                            K

                                                                                     Let S̃ = {σ(x) : x ∈ S}, then

                                                                                                              |f (S) − f (S̃)| < 

                                                                                     because dH (S, S̃) < 1/K ≤ δ .
                                                                                                                  k−1 k
                      Input Point Cloud   Critical Point Sets   Upper-bound Shapes      Let hk (x) = e−d(x,[ K , K ]) be a soft indicator function
Figure 17. The consistency of segmentation results. We                               where d(x, I) is the point to set (interval) distance. Let
illustrate the segmentation results for some sample given point                      h(x) = [h1 (x); . . . ; hK (x)], then h : R → RK .
clouds S, their critical point sets CS and upper-bound shapes NS .                      Let vj (x1 , . . . , xn ) = max{h̃j (x1 ), . . . , h̃j (xn )}, indi-
We observe that the shape family between the CS and NS share a                       cating the occupancy of the j-th interval by points in S.
consistent segmentation results.                                                     Let v = [v1 ; . . . ; vK ], then v : R × . . . × R → {0, 1}K
                                                                                                                          |      {z         }
                                                                                                                                      n
                                                                                     is a symmetric function, indicating the occupancy of each
Original Shape

                                                                                     interval by points in S.
                                                                                        Define τ : {0, 1}K → X as τ (v) = { k−1     K : vk ≥ 1},
                                                                                     which maps the occupancy vector to a set which contains
                                                                                     the left end of each occupied interval. It is easy to show:
Critical Point Sets

                                                                                                            τ (v(x1 , . . . , xn )) ≡ S̃

                                                                                     where x1 , . . . , xn are the elements of S extracted in certain
Upper-bound Shapes

                                                                                     order.
                                                                                        Let γ : RK → R be a continuous function such that
                                                                                     γ(v) = f (τ (v)) for v ∈ {0, 1}K . Then,

                                                                                                      |γ(v(x1 , . . . , xn )) − f (S)|
Figure 18. The critical point sets and the upper-bound shapes
for unseen objects. We visualize the critical point sets and the                                  =|f (τ (v(x1 , . . . , xn ))) − f (S)| < 
upper-bound shapes for teapot, bunny, hand and human body,
which are not in the ModelNet or ShapeNet shape repository to                           Note that γ(v(x1 , . . . , xn )) can be rewritten as follows:
test the generalizability of the learnt per-point functions of our
PointNet on other unseen objects. The images are color-coded                             γ(v(x1 , . . . , xn )) =γ(MAX(h(x1 ), . . . , h(xn )))
to reflect the depth information.                                                                               =(γ ◦ MAX)(h(x1 ), . . . , h(xn ))

                                                                                     Obviously γ ◦ MAX is a symmetric function.
Theorem 1. Suppose f : X → R is a continuous
set function w.r.t Hausdorff distance dH (·, ·). ∀ >                                  Next we give the proof of Theorem 2. We define
0, ∃ a continuous function h and a symmetric function                                u = MAX{h(xi )} to be the sub-network of f which
                                                                                              xi ∈S
g(x1 , . . . , xn ) = γ◦MAX, where γ is a continuous function,
                                                                                     maps a point set in [0, 1]m to a K-dimensional vector. The
MAX is a vector max operator that takes n vectors as input
                                                                                     following theorem tells us that small corruptions or extra
and returns a new vector of the element-wise maximum,
                                                                                     noise points in the input set is not likely to change the output
such that for any S ∈ X ,
                                                                                     of our network:
                          |f (S) − γ(MAX(h(x1 ), . . . , h(xn )))| < 
                                                                                     Theorem 2. Suppose u : X → RK such that u =
where x1 , . . . , xn are the elements of S extracted in certain                     MAX{h(xi )} and f = γ ◦ u. Then,
                                                                                     xi ∈S
(a) ∀S, ∃ CS , NS ⊆ X , f (T ) = f (S) if CS ⊆ T ⊆ NS ;              Scene Semantic Parsing Visualization We give a visual-
                                                                     ization of semantic parsing in Fig 24 where we show input
(b) |CS | ≤ K                                                        point cloud, prediction and ground truth for both semantic
                                                                     segmentation and object detection for two office rooms and
Proof. Obviously, ∀S ∈ X , f (S) is determined by u(S).              one conference room. The area and the rooms are unseen in
So we only need to prove that ∀S, ∃ CS , NS ⊆ X , f (T ) =           the training set.
f (S) if CS ⊆ T ⊆ NS .
    For the jth dimension as the output of u, there exists at        Point Function Visualization Our classification Point-
least one xj ∈ X such that hj (xj ) = uj , where hj is the           Net computes K (we take K = 1024 in this visualization)
jth dimension of the output vector from h. Take CS as the            dimension point features for each point and aggregates
union of all xj for j = 1, . . . , K. Then, CS satisfies the         all the per-point local features via a max pooling layer
above condition.                                                     into a single K-dim vector, which forms the global shape
    Adding any additional points x such that h(x) ≤ u(S) at          descriptor.
all dimensions to CS does not change u, hence f . Therefore,            To gain more insights on what the learnt per-point
TS can be obtained adding the union of all such points to            functions h’s detect, we visualize the points pi ’s that
NS .                                                                 give high per-point function value f (pi ) in Fig 19. This
                                                                     visualization clearly shows that different point functions
                                                                     learn to detect for points in different regions with various
                                                                     shapes scattered in the whole space.

Figure 19. Point function visualization. For each per-point
function h, we calculate the values h(p) for all the points p in a
cube of diameter two located at the origin, which spatially covers
the unit sphere to which our input shapes are normalized when
training our PointNet. In this figure, we visualize all the points
p that give h(p) > 0.5 with function values color-coded by the
brightness of the voxel. We randomly pick 15 point functions and
visualize the activation regions for them.

H. More Visualizations
Classification Visualization We use t-SNE[15] to embed
point cloud global signature (1024-dim) from our classifica-
tion PointNet into a 2D space. Fig 20 shows the embedding
space of ModelNet 40 test split shapes. Similar shapes are
clustered together according to their semantic categories.

Segmentation Visualization We present more segmenta-
tion results on both complete CAD models and simulated
Kinect partial scans. We also visualize failure cases with
error analysis. Fig 21 and Fig 22 show more segmentation
results generated on complete CAD models and their
simulated Kinect scans. Fig 23 illustrates some failure
cases. Please read the caption for the error analysis.
Figure 20. 2D embedding of learnt shape global features. We use t-SNE technique to visualize the learnt global shape features for the
shapes in ModelNet40 test split.
                                                                      knife   guitar    earphone chair   car     cap     bag airplane                                                                         knife   guitar    earphone chair   car     cap     bag airplane

                                                                                                 motor   skate
                                                                      lamp     laptop   mug      bike    board   table   pistol   rocket                                                                                                 motor   skate
                                                                                                                                                                                                               lamp    laptop   mug      bike    board   table   pistol   rocket

                                                                                                                                           Figure 21. PointNet segmentation results on complete CAD models.

Figure 22. PointNet segmentation results on simulated Kinect scans.
(a)                                                                        (d)

(b)                                                                        (e)

(c)                                                                        (f)

Figure 23. PointNet segmentation failure cases. In this figure, we summarize six types of common errors in our segmentation application.
The prediction and the ground-truth segmentations are given in the first and second columns, while the difference maps are computed and
shown in the third columns. The red dots correspond to the wrongly labeled points in the given point clouds. (a) illustrates the most
common failure cases: the points on the boundary are wrongly labeled. In the examples, the label predictions for the points near the
intersections between the table/chair legs and the tops are not accurate. However, most segmentation algorithms suffer from this error. (b)
shows the errors on exotic shapes. For examples, the chandelier and the airplane shown in the figure are very rare in the data set. (c) shows
that small parts can be overwritten by nearby large parts. For example, the jet engines for airplanes (yellow in the figure) are mistakenly
classified as body (green) or the plane wing (purple). (d) shows the error caused by the inherent ambiguity of shape parts. For example,
the two bottoms of the two tables in the figure are classified as table legs and table bases (category other in [29]), while ground-truth
segmentation is the opposite. (e) illustrates the error introduced by the incompleteness of the partial scans. For the two caps in the figure,
almost half of the point clouds are missing. (f) shows the failure cases when some object categories have too less training data to cover
enough variety. There are only 54 bags and 39 caps in the whole dataset for the two categories shown here.
Figure 24. Examples of semantic segmentation and object detection. First row is input point cloud, where walls and ceiling are hided
for clarity. Second and third rows are prediction and ground-truth of semantic segmentation on points, where points belonging to different
semantic regions are colored differently (chairs in red, tables in purple, sofa in orange, board in gray, bookcase in green, floors in blue,
windows in violet, beam in yellow, column in magenta, doors in khaki and clutters in black). The last two rows are object detection with
bounding boxes, where predicted boxes are from connected components based on semantic segmentation prediction.
