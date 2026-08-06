---
source_id: 080
bibtex_key: lenz2015grasp
title: Deep Learning for Detecting Robotic Grasps
year: 2015 (preprint 2013)
domain_theme: Grasp Robotik
verified_pdf: 80_Deep Learning Robotic Grasps (Lenz dkk.).pdf
char_count: 109231
---

Deep Learning for Detecting Robotic Grasps
                                                                                     Ian Lenz,† Honglak Lee,∗ and Ashutosh Saxena†
                                                                                † Department of Computer Science, Cornell University.
                                                                             ∗ Department of EECS, University of Michigan, Ann Arbor.

                                                             Email: ianlenz@cs.cornell.edu, honglak@eecs.umich.edu, asaxena@cs.cornell.edu

                                                                                                                           However, most work in deep learning has been applied in
                                           Abstract—We consider the problem of detecting robotic grasps                 the context of recognition. Grasping is inherently a detection
                                        in an RGB-D view of a scene containing objects. In this work,                   problem, and previous applications of deep learning to detec-
                                        we apply a deep learning approach to solve this problem, which
arXiv:1301.3592v6 [cs.LG] 21 Aug 2014

                                        avoids time-consuming hand-design of features. This presents two                tion have typically focused on specific vision applications such
                                        main challenges. First, we need to evaluate a huge number of                    as face detection [45] and pedestrian detection [57]. Our goal
                                        candidate grasps. In order to make detection fast and robust,                   is not only to infer a viable grasp, but to infer the optimal grasp
                                        we present a two-step cascaded system with two deep networks,                   for a given object that maximizes the chance of successfully
                                        where the top detections from the first are re-evaluated by                     grasping it, which differs significantly from the problem of
                                        the second. The first network has fewer features, is faster to
                                        run, and can effectively prune out unlikely candidate grasps.                   object detection. Thus, the first major contribution of our work
                                        The second, with more features, is slower but has to run                        is to apply deep learning to the problem of robotic grasping, in
                                        only on the top few detections. Second, we need to handle                       a fashion which could generalize to similar detection problems.
                                        multimodal inputs effectively, for which we present a method                       The second major contribution of our work is to propose
                                        that applies structured regularization on the weights based on                  a new method for handling multimodal data in the context
                                        multimodal group regularization. We show that our method
                                        improves performance on an RGBD robotic grasping dataset,                       of feature learning. The use of RGB-D data, as opposed
                                        and can be used to successfully execute grasps on two different                 to simple 2D image data, has been shown to significantly
                                        robotic platforms. 1                                                            improve grasp detection results [28, 14, 56]. In this work, we
                                                                                                                        present a multimodal feature learning algorithm which adds a
                                        Keywords: Robotic Grasping, deep learning, RGB-D multi-                         structured regularization penalty to the objective function to
                                        modal data, Baxter, PR2, 3D feature learning.                                   be optimized during learning. As opposed to previous works
                                                                                                                        in deep learning, which either ignore modality information at
                                                                  I. I NTRODUCTION                                      the first layer (i.e., encourage all features to use all modalities)
                                           Robotic grasping is a challenging problem involving percep-                  [59] or train separate first-layer features for each modality
                                        tion, planning, and control. Some recent works [54, 56, 28, 67]                 [43, 61], our approach allows for a middle-ground in which
                                        address the perception aspect of this problem by converting it                  each feature is encouraged to use only a subset of the input
                                        into a detection problem in which, given a noisy, partial view                  modalities, but is not forced to use only particular ones.
                                        of the object from a camera, the goal is to infer the top loca-                    We also propose a two-stage cascaded detection system
                                        tions where a robotic gripper could be placed (see Figure 1).                   based on deep learning. Here, we use fewer features for the
                                        Unlike generic vision problems based on static images, such                     first pass, providing faster, but only approximately accurate
                                        robotic perception problems are often used in closed loop with                  detections. The second pass uses more features, giving more
                                        controllers, so there are stringent requirements on performance                 accurate detections. In our experiments, we found that the
                                        and computational speed. In the past, hand-designing features                   first deep network, with fewer features, was better at avoiding
                                        has been the most popular method for several robotic tasks                      overfitting but less accurate. We feed the top-ranked rectangles
                                        [40, 32]. However, this is cumbersome and time-consuming,                       from the first layer into the second layer, leading to robust
                                        especially when we must incorporate new input modalities                        early rejection of false positives. Unlike manually designed
                                        such as RGB-D cameras.                                                          two-step features as in [28], our method uses deep learning,
                                           Recent methods based on deep learning [1] have demon-                        which allows us to learn detectors that not only give higher
                                        strated state-of-the-art performance in a wide variety of tasks,                performance, but are also computationally efficient.
                                        including visual recognition [35, 60], audio recognition [39,                      We test our approach on a challenging dataset, where
                                        41], and natural language processing [12]. These techniques                     we show that our algorithm improves both recognition and
                                        are especially powerful because they are capable of learning                    detection performance for grasping rectangle data. We also
                                        useful features directly from both unlabeled and labeled data,                  show that our two-stage approach is not only able to match
                                        avoiding the need for hand-engineering.                                         the performance of a single-stage system, but, in fact, improves
                                                                                                                        results while significantly reducing the computational time
                                          1 Parts of this work were presented at ICLR 2013 as a workshop paper,
                                                                                                                        needed for detection.
                                        and at RSS 2013 as a conference paper. This version includes significantly
                                        extended related work, algorithmic descriptions, and extensive robotic exper-
                                                                                                                           In summary, the contributions of this paper are:
                                        iments which were not present in previous versions.                                • We present a deep learning algorithm for detecting
Fig. 1: Detecting robotic grasps: Left: A cluttered lab scene labeled with rectangles corresponding to robotic grasps for objects in the
scene. Green lines correspond to robotic gripper plates. We use a two-stage system based on deep learning to learn features and perform
detection for robotic grasping. Center: Our Baxter robot “Yogi” successfully executing a grasp detected by our algorithm. Right: The grasp
detected for this case, in the RGB (top) and depth (bottom) images obtained from Kinect.

      robotic grasps. To the best of our knowledge, this is the       [34, 44, 49] focused on testing for form- and force-closure,
      first work to do so.                                            and synthesizing grasps fulfilling these properties according to
   • In order to handle multimodal inputs, we present a new           some hand-designed “quality score” [17]. More recent works
      way to apply structured regularization to the weights to        have refined these definitions [50]. These works assumed full
      these inputs based on multimodal group regularization.          knowledge of object shape and physical properties.
   • We present a multi-step cascaded system for detection,
                                                                      Grasping Given 3D Model: Fast synthesis of grasps for
      significantly reducing its computational cost.                  known 3D models remains an active research topic [14, 20,
   • Our method outperforms the state-of-the-art for rectangle-
                                                                      65], with recent methods using advanced physical simulation
      based grasp detection, as well as previous deep learning        to find optimal grasps. Gallegos et al. [18] performed opti-
      algorithms.                                                     mization of grasps given both a 3D model of the object to be
   • We implement our algorithm on both a Baxter and a
                                                                      grasped and the desired contact points for the robotic gripper.
      PR2 robot, and show success rates of 84% and 89%,               Pokorny et al. [48] define spaces of graspable objects, then
      respectively, for executing grasps on a highly varied set       map new objects to these spaces to discover grasps. However,
      of objects.                                                     these works are only applicable when the full 3D model of
   The rest of the paper is organized as follows: We discuss          the object is exactly known, which may not be the case when
related work in Section II. We present our two-step cascaded          a robot is interacting with a new environment. We note that
detection system in Section III, and some additional details          some of these physics-based approaches might be combined
in Section IV. We then describe our feature learning algo-            with our approach in a multi-pass system, discussed further in
rithm and structured regularization method in Section V. We           Sec. IX.
present our experiments in Section VI, and discuss results in         Sensing for Grasping: In a real-world robotic setting, a robot
Section VII. We then present experiments on both Baxter and           will not have full knowledge of the 3D model and pose of an
PR2 robots in Section VIII. We present several interesting            object to be grasped, but rather only incomplete information
directions for future work in Section IX, then conclude in            from some set of sensors such as color or depth cameras,
Section X.                                                            tactile sensors, etc. This makes the problem of grasping
                      II. R ELATED W ORK                              significantly more challenging [4], as the algorithm must use
                                                                      more limited and potentially noisier information to detect a
A. Robotic Grasping                                                   good grasp. While some works [10, 46] simply attempt to
   In this section, we will focus on perception- and learning-        estimate the poses of known objects and then apply full-model
based approaches for robotic grasping. For a more complete            grasping algorithms based on these results, others avoid this
review of the field, we refer the reader to review papers by          assumption, functioning on novel objects which the algorithm
Bohg et al. [4], Sahbani et al. [53], Bicchi and Kumar [2] and        has not seen before.
Shimoga [58].                                                            Such works often made use of other simplifying assump-
   Most works define a “grasp” as an end-effector config-             tions, such as assuming that objects belong to one of a
uration which achieves partial or complete form- or force-            set of primitive shapes [47, 6], or are planar [42]. Other
closure of a given object. This is a challenging problem              works produced impressive results for specific cases, such as
because it depends on the pose and configuration of the robotic       grasping the corners of towels [40]. While such works escape
gripper as well as the shape and physical properties of the           the assumption of a fully-known object model, hand-coded
object to be grasped, and typically requires a search over a          grasping rules have a hard time dealing with the wide range
large number of possible gripper configurations. Early works          of objects seen in real-world human environments, and are
difficult and time-consuming to create.                            more robust features for RGB-D and other multimodal data.
Learning for Grasping: Machine learning methods have
                                                                   B. Deep Learning
proven effective for a wide range of perception problems
[64, 22, 38, 59, 3], allowing a perception system to learn            Deep learning approaches have demonstrated the ability to
a mapping from some feature set to various visual proper-          learn useful features directly from data for a wide variety of
ties. Early work by Kamon et al. [31] showed that learning         tasks. Early work by Hinton and Salakhutdinov [22] showed
approaches could also be applied to the problem of grasping        that a deep network trained on images of hand-written digits
from vision, introducing a learning component to grasp quality     will learn features corresponding to pen-strokes. Later work
scores.                                                            using localized convolutional features [38] showed that these
   Recent works have employed richer features and learning         networks learn features corresponding to object parts when
methods, allowing robots to grasp known objects which might        trained on natural images. This demonstrates that even the
be partially occluded [27] or in an unknown pose [13] as           basic features learned by these systems will adapt to the data
well as fully novel objects which the system has not seen          given. In fact, these approaches are not restricted to the visual
before [54]. Here, we will address the latter case. Earlier        domain, but rather have been shown to learn useful features for
work focused on detecting only a single grasping point from        a wide range of domains, such as audio [39, 41] and natural
2D partial-view data, using heuristic methods to determine         language data [12].
a gripper pose based on this point. [55]. The use of 3D            Deep Learning for Detection: However, the vast majority
data was shown to significantly improve these results [56]         of work in deep learning focuses on classification problems.
thanks to giving direct physical information about the object      Only a handful of previous works have applied these methods
in question. With the advent of low-cost RGB-D sensors such        to detection problems [45, 37, 9]. For example, Osadchy et al.
as the Kinect, the use of depth data for robotic grasping has      [45] and LeCun et al. [37] applied a deep energy-based model
become ubiquitous.                                                 to the problem of face detection, Sermanet et al. [57] applied
   Several other works attempted to use the learning algorithm     a convolutional neural network for pedestrian detection, and
to more fully constrain the detected grasps. Ekvall and Kragic     Coates et al. [9] used a deep learning approach to detect text in
[15] and Huebner and Kragic [23] used shape-based approxi-         images. Girshick et al. [19] used learned convolutional features
mations as bases for learning algorithms which directly gave       over image regions for object detection, while Szegedy et al.
an approach vector. Le et al. [36] treated grasp detection as a    [62] used a multi-scale approach based on deep networks for
ranking problem over sets of contact points in image space.        the same task.
Jiang et al. [28] represented a grasp as a 2D oriented rectangle      All these approaches focused on object detection and similar
in image space, with two edges corresponding to the gripper        problems, in which the goal is to find a bounding box
plates, using surface normals to determine the grasp approach      which tightly contains the item to be detected, and for each
vector. These approaches allow the detection algorithm to          item, all valid bounding boxes will be similar. However, in
detect more exactly the gripper pose which should be used          robotic grasp detection, there may be several valid grasps for
for grasping. In this work, we will follow the rectangle-based     an object in different regions, making it more important to
method.                                                            select the one with the highest chance success. In addition,
   Learning-based approaches have shown impressive results         orientation matters much more to robotic grasp detection, as
in grasping novel objects, showing that learning some param-       most grasps will only be viable for a small subset of the
eters of the detection system can outperform human tuning.         possible gripper orientations. Our approach to grasp detection
However, these approaches still require a significant degree of    will also generalize across object classes, and even to classes
hand-engineering in the form of designing good input features.     never seen before by the system, as opposed to the class-
Other Applications with RGBD Data. Due to the avail-               specific nature of object detection.
ability of inexpensive depth sensors, RGB-D data has been a        Multimodal Deep Learning: Recent works in deep learning
significant research focus in recent years for various robotics    have extended these methods to handle multiple modalities
applications. For example, Jiang et al. [30] consider robotic      of input data, such as audio and video [43], text and image
placement of objects, while Teuliere and Marchand [63] used        data [61], and even RGB-D data [59, 3]. However, all of these
RGB-D data for visual servoing. Several works, including           approaches have fallen into two camps - either learning com-
those of Endres et al. [16] and Whelan et al. [66] have ex-        pletely separate low-level features for each modality [43, 61],
tended and improved Simultaneous Localization and Mapping          or simply concatenating the modalities [59, 3]. The former
(SLAM) for RGB-D data. Object detection and recognition            approaches have proven effective for data where the basic
has been a major focus in research on RGB-D data [11, 33, 7].      modalities differ significantly, such as the aforementioned case
Most such works use hand-engineered features such as [52].         of text and images, while the latter is more effective in cases
The few works that perform feature learning for RGB-D data         where the modalities are more similar, such as RGB-D data.
[59, 3] largely ignore the multimodal nature of the data, not         For some new combinations of modalities and tasks, it
distinguishing the color and depth channels. Here, we present      may not be clear which of these approaches will give better
a structured regularization approach which allows us to learn      performance. In fact, in the ideal feature set, different features
Fig. 2: Detecting and executing grasps: From left to right: Our system obtains an RGB-D image from a Kinect mounted on the robot,
and searches over a large space of possible grasps, for which some candidates are shown. For each of these, it extracts a set of raw features
corresponding to the color and depth images and surface normals, then uses these as inputs to a deep network which scores each rectangle.
Finally, the top-ranked rectangle is selected and the corresponding grasp is executed using the parameters of the detected rectangle and the
surface normal at its center. Red and green lines correspond to gripper plates, blue in RGB-D features indicates masked-out pixels.

may use different subsets of the modalities. In this work, we           candidate grasp, then used to score that grasp. Our approach
will give a structured regularization method which guides the           will include a structured multimodal regularization method
learning algorithm to select such subsets, without imposing             which improves the quality of the features learned from
hard constraints on network structure.                                  RGB-D data without constraining network structure.
Structured Learning and Structured Regularization: Sev-                    In our system for robotic grasping, as shown in Fig. 2, the
eral approaches have been proposed which attempt to use a               robot first obtains an RGB-D image of the scene containing
specially-designed regularization function to impose structure          objects to be grasped. A small deep network is used to score
on a set of learned parameters without directly enforcing it.           potential grasps in this image, and a small candidate set of the
Jalali et al. [26] used a group regularization function in the          top-ranked grasps is provided to a larger deep network, which
multitask learning setting, where one set of features is used for       yields a single best-ranked grasp.
multiple tasks. This function applies high-order regularization            In this work, we will represent potential grasps using
separately to particular groups of parameters. Their function           oriented rectangles in the image plane as seen on the left in
regularized the number of features used for each task in a set of       Fig. 2, with one pair of parallel edges corresponding to the
multi-class classification tasks solved by softmax regression.          robotic gripper [28]. Each rectangle is thus parameterized by
Intuitively, this encodes the belief that only some subset of           the X and Y coordinates of its upper-left corner, its width,
the input features will be useful for each task, but this set of        height, and orientation in the image plane, giving a five-
useful features might vary between tasks.                               dimensional search space for potential grasps. Grasps will be
   A few works have also explored the use of structured                 ranked based on features extracted from the RGB-D image
regularization in deep learning. The Topographic ICA algo-              region contained inside their corresponding rectangle, aligned
rithm [24] is a feature-learning approach that applies a similar        to the gripper plates, as seen in the center of Fig. 2.
penalty term to feature activations, but not to the weights                To translate a rectangle such as that shown on the right in
themselves. Coates and Ng [8] investigate the problem of                Fig. 2 into a gripper pose for grasping we find the point with
selecting receptive fields, i.e., subsets of the input features         the minimum depth inside the central third (horizontally) of
to be used together in a higher-level feature. The structure            the rectangle. We then use the averaged surface normal around
of the network is learned first, then fixed before learning the         this point to determine the approach vector for the gripper.
parameters of the network.                                              The orientation of the detected rectangle is translated to a
                                                                        rotation around this vector to orient the gripper. We use the
       III. D EEP L EARNING FOR G RASP D ETECTION :                     X-Y coordinates of the rectangle center along with the depth
                    S YSTEM AND M ODEL                                  of the closest point to determine a grasping point in the robot’s
   In this work, we will present an algorithm for robotic grasp         coordinate frame. We compute a pre-grasp position by shifting
detection from a single RGB-D view. Our approach will be                10 cm back from the grasping point along this approach vector
based on machine learning, but distinguish itself from previous         and position the gripper at this point. We then approach the
approaches by learning not only the weights used to rank                object along the approach vector and grasp it.
prospective grasps, but also the features used to rank them,               Using a standard feature learning approach such as sparse
which were previously hand-engineered.                                  auto-encoder [21], a deep network can be trained for the
   We will do this using deep learning methods, learning a              problem of grasping rectangle recognition (i.e., does a given
set of RGB-D features which will be extracted from each                 rectangle in image space correspond to a valid robotic grasp?).
Fig. 3: Illustration of our two-stage detection process: Given an image of an object to grasp, a small deep network is used to exhaustively
search potential rectangles, producing a small set of top-ranked rectangles. A larger deep network is then used to find the top-ranked rectangle
from these candidates, producing a single optimal grasp for the given object.

                                                                         detections for the second stage. Using deep learning allows us
                                                                         to circumvent the costly manual design of features by simply
                                                                         training networks of two different sizes, using the smaller for
                                                                         the exhaustive first pass, and the larger to re-rank the candidate
                                                                         detection results.
                                                                         Model: To detect robotic grasps from the rectangle repre-
                                                                         sentation, we model the probability of a rectangle G(t) , with
                                                                         features x(t) ∈ RN being graspable, using a random variable
                                                                         ŷ (t) ∈ {0, 1} which indicates whether or not we predict G(t) to
                                                                         be graspable. We use a deep network, as shown in Fig. 4-left,
                                                                         with two layers of sigmoidal hidden units h[1] and h[2] , with
                                                                         K1 and K2 units per layer, respectively. A logistic classifier
Fig. 4: Deep network and auto-encoder: Left: A deep network
with two hidden layers, which transform the input representation,        over the outputs of the second-layer hidden units then predicts
and a logistic classifier at the top layer, which uses the features      P (ŷ (t) |x(t) ; Θ), so chosen because ground-truth graspability is
from the second hidden layer to predict the probability of a grasp       represented as binary. Each layer ` will have a set of weights
being feasible. Right: An auto-encoder, used for pretraining. A set of   W [`] mapping from its inputs to its hidden units, so the param-
weights projects input features to a hidden layer. The same weights      eters of our model are Θ = {W [1] , W [2] , W [3] }. Each hidden
are then used to project these hidden unit outputs to a reconstruction
of the inputs. In the sparse auto-encoder (SAE) algorithm, the hidden    unit forms output by a sigmoid σ(a) = 1/(1 + exp(−a)) over
unit activations are also penalized.                                     its weighted input:
                                                                                                                   N
                                                                                                                                !
                                                                                                       [1](t)         (t)   [1]
                                                                                                                  X
                                                                                                     hj       =σ     xi Wi,j
However, in a real-world robotic setting, our system needs to                                                     i=1
perform detection (i.e., given an image containing an object,                                                     K1
                                                                                                                                       !
                                                                                                    [2](t)               [1](t)  [2]
                                                                                                                  X
how should the robot grasp it?). This task is significantly more                                   hj      =σ           hi      Wi,j
challenging than simple recognition.                                                                              i=1
                                                                                                                                       !
                                                                                                                  K2
Two-stage Cascaded Detection: In order to perform detec-                                                                 [2](t)  [3]
                                                                                                                  X
                                                                                    P (ŷ (t) = 1|x(t) ; Θ) = σ         hi      Wi          (1)
tion, one naive approach could be to consider each possible                                                       i=1
oriented rectangle in the image (perhaps discretized to some
level), and evaluate each rectangle with a deep network                  A. Inference and Learning
trained for recognition. However, such near-exhaustive search
                                                                            During inference, our goal is to find the single grasping
of possible rectangles (based on positions, sizes, and orienta-
                                                                         rectangle with the maximum probability of being graspable for
tions) can be quite expensive in practice for real-time robotic
                                                                         some new object. With G representing a particular grasping
grasping.
                                                                         rectangle position, orientation, and size, we find this best
   Motivated by multi-step cascaded approaches in previous
                                                                         rectangle as:
work [28, 64], we instead take a two-stage approach to
detection: First, we use a reduced feature set to determine                             G∗ = arg max P (ŷ (t) = 1|φ(G); Θ)                 (2)
a set of top candidates. Then, we use a larger, more robust                                        G

feature set to rank these candidates.                                    Here, the function φ extracts the appropriate input representa-
   However, these approaches require the design of two sepa-             tion for rectangle G.
rate sets of features. In particular, it can be difficult to manually       During learning, our goal is to learn the parameters Θ that
design a small set of first-stage features which is both quick to        optimize the recognition accuracy of our system. Here, input
compute and robust enough to produce a good set of candidate             data is given as a set of pairs of features x(t) ∈ RN and
ground-truth labels y (t) ∈ {0, 1} for t = 1, . . . , M . As in most
deep learning works, we use a two-phase learning approach.
   In the first phase, we will use unsupervised feature learning
to initialize the hidden-layer weights W [1] and W [2] . Pre-
training weights this way is critical to avoid overfitting. We                  Fig. 5: Preserving aspect ratio: Left: a pair of sunglasses with
will use a variant of a sparse auto-encoder (SAE) [21], as                      a potential grasping rectangle. Red edges indicate gripper plates.
illustrated in Fig. 4-right. We define g(h) as a sparsity penalty               Center: image taken from the rectangle and rescaled to fit a square
function over hidden unit activations, with λ controlling its                   aspect ratio. Right: same image, padded and centered in the receptive
weight. With f (W ) as a regularization function, weighted                      field. Blue areas indicate masked-out padding. When rescaled, the
                                                                                rectangle incorrectly appears graspable. Preserving aspect ratio and
by β, and x̂(t) as the reconstruction of x(t) , SAE solves the                  padding allows the rectangle to correctly appear non-graspable.
following to initialize hidden-layer weights:
                     M                                K
                                                               (t)
                     X                                X
W ∗ = arg min              (||x̂(t) − x(t) ||22 + λ         g(hj )) + βf (W )
           W         t=1                              j=1
        N
 (t)       (t)
       X
hj = σ(   xi Wi,j )
          i=1
        K
 (t)
        X      (t)                                                              Fig. 6: Improvement from mask-based scaling: Left: Result with-
x̂i =         hj Wi,j                                                    (3)    out mask-based scaling. Right: Result with mask-based scaling.
        j=1

We first use this algorithm to initialize W [1] to reconstruct x.
We then fix W [1] and learn W [2] to reconstruct h[1] .                         The first three channels are the image in YUV color space,
                                                                                used because it represents image intensity and color separately.
   During the supervised phase of the learning algorithm, we
                                                                                The next is simply the depth channel of the image. The last
then jointly learn classifier weights W [3] and fine-tune hidden
                                                                                three are the X, Y, and Z components of surface normals
layer weights W [1] and W [2] for recognition. We maximize the
                                                                                computed based on the depth channel. These are computed
log-likelihood of the data along with regularization penalties
                                                                                after the image is aligned to the gripper so that they are always
on hidden layer weights:
                                                                                relative to the gripper plates.
                                M
                                X
         Θ∗ = arg max                 log P (ŷ (t) = y (t) |x(t) ; Θ)          A. Data Pre-Processing
                      Θ         t=1                                                Whitening data is critical for deep learning approaches to
                                   − β1 f (W [1] ) − β2 f (W [2] )       (4)    work well, especially in cases such as multimodal data where
                                                                                the statistics of the input data may vary greatly. While PCA-
Two-stage Detection Model: During inference for two-stage                       based approaches have been shown to be effective [25], they
detection, we will first use a smaller network to produce a set                 are difficult to apply in cases such as ours where large portions
of the top T rectangles with the highest probability of being                   of the data may be masked out.
graspable according to network parameters Θ1 . We will then                        Depth data, in particular, can be difficult to whiten because
use a larger network with a separate set of parameters Θ2 to                    the range of values may be very different for different patches
re-rank these T rectangles and obtain a single best one. The                    in the image. Thus, we first whiten each depth patch indi-
only change to learning for the two-stage model is that these                   vidually, subtracting the patch-wise mean and dividing by the
two sets of parameters are learned separately, using the same                   patch-wise standard deviation, down to some minimum.
approach.                                                                          For multimodal data, the statistics of the data for each
                                                                                modality should match as closely as possible, to avoid learning
                        IV. S YSTEM D ETAILS
                                                                                features which are biased towards or away from using partic-
   In this section, we will define the set of raw features which                ular modes. This is particularly important when regularizing
our system will use, forming x in the equations above, and how                  each modality separately, as in our approach. Thus, we drop
they are extracted from an RGB-D image. Some examples of                        mean values for each feature separately, but scale the data for
these features are shown in Fig 2.                                              each channel by dividing by the standard deviation of all its
   Our algorithm uses only local information - specifically, we                 features combined.
extract the RGB-D sub-image contained within each rectangle,
and use this to generate features for that rectangle. This image                B. Preserving Aspect Ratio.
is rotated so that its left and right edges correspond to the                      It is important for to preserve aspect ratio when feeding
gripper plates, and then re-scaled to fit inside the network’s                  features into the network. This is because distorting image fea-
receptive field.                                                                tures may cause non-graspable rectangles to appear graspable,
   From this 24x24 pixel image, seven channels’ worth of                        as shown in Fig. 5. However, padding with zeros can cause
features are extracted, giving 24x24x7 = 4032 input features.                   rectangles with less padding to receive higher graspability
Fig. 7: Three possible models for multimodal deep learning: Left: fully dense model—all visible features are concatenated and modality
information is ignored. Middle: modality-specific sparse model - separate first layer features are trained for each modality. Right: group-sparse
model—a structured regularization term encourages features to use only a subset of the input modes.

scores, as the network will have more nonzero inputs. It is               scaling factor for each mode. In practice, we found it necessary
important to account for this because in many cases the ideal             to limit the scaling factor to a maximum of some value c, as
                                                                             (t)          (t)
grasp for an object might be represented by a thin rectangle              Ψ0 r = min(Ψr , c).
which would thus contain many zero values in its receptive                   As shown in Table III our mask-based scaling technique at
field from padding.                                                       the visible layer improves grasping results by over 25% for
   To address this problem, we scale up the magnitude of the              both metrics. As seen in Figure 6, it removes the network’s
available input for each rectangle based on the fraction of               inherent bias towards square rectangles, exhibiting a much
the rectangle which is masked out. In particular, we define a             wider range of aspect ratios that more closely matches that
multiplicative scaling factor for the inputs from each modality,          of the ground-truth data.
based on the fraction of each mode which is masked out, since
each mode may have a different mask.                                                 V. S TRUCTURED R EGULARIZATION FOR
   In the multimodal setting, we assume that the input data x is                              F EATURE L EARNING
known to come from R distinct modalities, for example audio                  A naive way of applying feature learning to multimodal
and video data, or depth and RGB data. We define the modality             data is to simply take x (as a concatenated vector) as input
matrix S as an RxN binary matrix, where each element Sr,i                 to the model described above, ignoring information about
indicates membership of visible unit xi in a particular modality          specific modalities, as seen on the lefthand side of Figure 7.
r, such as depth or image intensity. The scaling  factor for mode
                                                 P                      This approach may either 1) prematurely learn features which
                           (t)     PN               N          (t)
r is then defined as: Ψr =            i=1 Sr,i /    i=1 S r,i µi     ,    include all modalities, which can lead to overfitting, or 2) fail
         (t)            (t)                                               to learn associations between modalities with very different
where µi is 1 if xi is masked in, 0 otherwise. The scaling
                       (t)   PR
factor for case i is: ψi = r=1 Sr,i Ψr .
                                        (t)                               underlying statistics.
   We could simply scale up each value of x by its correspond-               Instead of concatenating multimodal input as a vector,
                                                (t)     (t) (t)           Ngiam et al. [43] proposed training a first layer representation
ing scale factor when training our model, as x0 i = ψi xi .
However, since our sparse autoencoder penalizes squared error,            for each modality separately, as shown in Figure 7-middle.
scaling x linearly will scale the error for the corresponding             This approach makes the assumption that the ideal low-level
cases quadratically, causing the learning algorithm to lend               features for each modality are purely unimodal, while higher-
increased significance to cases where more data is masked out.            layer features are purely multimodal. This approach may work
Instead, we can use the scaled x0 as input to the network, but            better for some problems where the modalities have very
penalize reconstruction based on the original x, only scaling             different basic representations, such as the video and audio
after the squared error has been computed:                                data (as used in [43]), so that separate first layer features
                                                                        may give better performance. However, for modalities such
                 M      N                         K
                X      X    (t) (t)    (t)
                                                 X       (t)              as RGB-D data, where the input modes represent different
 W ∗ = arg min            ψi (x̂i − xi )2 + λ       g(hj )
           W
                                                                          channels of an image, learning low-level correlations can lead
                  t=1     i=1                          j=1
                                                                          to more robust features – our experiments in Section VI show
                                                                   (5)
                                                                          that simply concatenating the input modalities significantly
We redefine the hidden units to use the scaled visible input:             outperforms training separate first-layer features for robotic
                                                                          grasp detection from RGB-D data.
                             N
                                         !
                   (t)           0 (t)
                            X
                 hj = σ         x i Wi,j                   (6)               For many problems, it may be difficult to tell which of these
                                 i=1                                      approaches will perform better, and time-consuming to tune
This approach is equivalent to adding additional, potentially             and comparatively evaluate multiple algorithms. In addition,
fractional, ‘virtual’ visible units to the model based on the             the ideal feature set for some problems may contain features
             (a) Features corresponding to positive grasps.                          (b) Features corresponding to negative grasps.

Fig. 8: Features learned from grasping data: Each feature contains seven channels - from left to right, depth, Y, U, and V image channels,
and X, Y, and Z surface normal components. Vertical edges correspond to gripper plates. Left: eight features with the strong positive
correlations to rectangle graspability. Right: similar, but negative correlations. Group regularization eliminates many modalities from many
of these features, making them more robust.

which use some, but not all, of the input modalities, a case           lower-valued ones. This also means that forming a high-valued
which neither of these approaches are designed to handle.              weight in a group with other high-valued weights will accrue
   To solve these problems, we propose a new algorithm for             a lower additional penalty than doing so for a group with
feature learning for multimodal data. Our approach incorpo-            only low-valued weights. At the limit (p → ∞), this group
rates a structured penalty term into the optimization problem          regularization becomes equivalent to the infinity (or max)
to be solved during learning. This technique allows the model          norm:
to learn correlated features between multiple input modalities,                                XK X R
but regularizes the number of modalities used per feature                             f (W ) =        max Sr,i |Wi,j |            (8)
                                                                                                                 i
(hidden unit), discouraging the model from learning weak                                           j=1 r=1
correlations between modalities. With this regularization term,        which penalizes only the maximum weight from each mode to
the algorithm can specify how mode-sparse or mode-dense the            each feature. In practice, the infinity norm is not differentiable
features should be, representing a continuum between the two           and therefore is difficult to apply gradient-based optimization
extremes outlined above.                                               methods; in this paper, we use the log-sum-exponential as a
Regularization in Deep Learning: In a typical deep learn-              differentiable approximation to the max norm.
ing model, L2 regularization (i.e., f (W ) = ||W ||22 ) or L1             In experiments, this regularization function produces first-
regularization (i.e., f (W ) = ||W ||1 ) are commonly used in          layer weights concentrated in fewer modes per feature. How-
training (e.g., as specified in Equations (3) and (4)). These are      ever, we found that at values of β sufficient to induce the
often called a “weight cost” (or “weight decay”), and are left         desired mode-wise sparsity patterns, penalizing the maximum
implicit in many works.                                                also had the undesirable side-effect of causing many of the
   Applying regularization is well known to improve the gen-           weights for other modes to saturate at their mode’s maximum,
eralization performance of feature learning algorithms. One            suggesting that the features were overly constrained. In some
might expect that a simple L1 penalty would eliminate weak             cases, constraining the weights in this manner also caused
correlations in multimodal features, leading to features which         the algorithm to learn duplicate (or redundant) features, in
use only a subset of the modes each. However, we found that in         effect scaling up the feature’s contribution to reconstruction to
practice, a value of β large enough to cause this also degraded        compensate for its constrained maximum. This is obviously an
the quality of features for the remaining modes and lead to            undesirable effect, as it reduces the effective size (or diversity)
decreased task performance.                                            of the learned feature set.
Multimodal Regularization: Structured regularization, such                This suggests that the max-norm may be overly con-
as in [26], takes a set of groups of weights, and applies              straining. A more desirable sparsity function would penalize
some regularization function (typically high-order) separately         nonzero weight maxima for each mode for each feature
to each group. In our structured multimodal regularization             without additional penalty for larger values of these maxima.
algorithm, each modality will be used as a regularization group        We can achieve this effect by applying the L0 norm, which
separately for each hidden unit. For example, a group-wise p-          takes a value of 0 for an input of 0, and 1 otherwise, on top
norm would be applied as:                                              of the max-norm from above:
                                                                                             K X
                                                                                               R
                                               !1/p                                          X
                      K X
                      X   R    X N                                                f (W ) =             I{(max Sr,i |Wi,j |) > 0}        (9)
                                           p                                                                 i
            f (W ) =               Sr,i |Wi,j |              (7)                             j=1 r=1
                        j=1 r=1     i=1
                                                                       where I is the indicator function, which takes a value of 1
where Sr,i is 1 if feature i belongs to group r and 0 otherwise.       if its argument is true, 0 otherwise. Again, for a gradient-
Using a high value of p allows us to penalize higher-valued            based method, we used an approximation to the L0 norm,
weights from each mode to each feature more strongly than              such as log(1 + x2 ). This regularization function now encodes
                                                                       TABLE I: Recognition results for Cornell grasping dataset.
                                                                                Algorithm                           Accuracy (%)
                                                                                Chance                                        50
                                                                                Jiang et al. [28]                           84.7
                                                                                Jiang et al. [28] + FPFH                    89.6
                                                                                Sparse AE, separate layer-1 feat.           92.8
                                                                                Sparse AE                                   93.7
                                                                                Sparse AE, group reg.                       93.7

                                                                     exhaustive search using this network, then used the 200-unit
                                                                     network to re-rank the 100 highest-ranked rectangles found by
Fig. 9: Example objects from the Cornell grasping dataset: [28].     the 50-unit network.
This dataset contains objects from a large variety of categories.
                                                                     B. Baselines
                                                                        We compare our recognition results in the Cornell grasping
a direct penalty on the number of modes used for each                dataset with the features from [28], as well as the combination
weight, without further constraining the weights of modes with       of these features and Fast Point Feature Histogram (FPFH)
nonzero maxima.                                                      features [51]. We used a linear SVM for classification, which
   Figure 8 shows features learned from the unsupervised stage       gave the best results among all other kernels. We also report
of our group-regularized deep learning algorithm. We discuss         chance performance, obtained by randomly selecting a label
these features, and their implications for robotic grasping, in      in the recognition case, and randomly assigning scores to
Section VII.                                                         rectangles in the detection case.
                                                                        We also compare our algorithm to other deep learning
                      VI. E XPERIMENTS                               approaches. We compare to a network trained only with
A. Dataset                                                           standard L1 regularization, and a network trained in a manner
   We used the extended version of the Cornell grasping              similar to [43], where three separate sets of first layer features
dataset for our experiments. This dataset, along with code for       are learned for the depth channel, the combination of the Y,
this paper, is available at http://pr.cs.cornell.edu/                U, and V channels, and the combination of the X, Y, and Z
deepgrasping. We note that this is an updated version                surface normal components.
of the dataset used in [28], containing several more complex
                                                                     C. Metrics for Detection
objects, and thus results for their algorithms will be different
from those in [28]. This dataset contains 1035 images of                For detection, we compare the top-ranked rectangle for
280 graspable objects, several of which are shown in Fig. 9.         each method with the set of ground-truth rectangles for each
Each image is annotated with several ground-truth positive           image. We present results using two metrics, the “point” and
and negative grasping rectangles. While the vast majority of         “rectangle” metric.
possible rectangles for most objects will be non-graspable, the         For the point metric, similar to Saxena et al. [55], we com-
dataset contains roughly equal numbers of graspable and non-         pute the center point of the predicted rectangle, and consider
graspable rectangles. We will show that this is useful for an        the grasp a success if it is within some distance from at least
unsupervised learning algorithm, as it allows learning a good        one ground-truth rectangle center. We note that this metric
representation for graspable rectangles even from unlabeled          ignores grasp orientation, and therefore might overestimate the
data.                                                                performance of an algorithm for robotic applications.
   We performed five-fold cross-validation, and present results         For the rectangle metric, similar to Jiang et al. [28], let G be
for splits on per image (i.e., the training set and the validation   the top-ranked grasping rectangle predicted by the algorithm,
set do not share the same image) and per object (i.e., the           and G∗ be a ground-truth rectangle. Any rectangles with
training set and the validation set do not share any images          an orientation error of more than 30o from G are rejected.
from the same object) basis. Hyper-parameters were selected          From the remaining set, we use the common bounding box
by validating performance on a separate set of 300 grasps not        evaluation metric of intersection divided by union - i.e.
used in any of the cross-validation splits.                          Area(G ∩ G∗ )/Area(G ∪ G∗ ). Since a ground-truth rectangle
   We take seven 24x24 pixel channels as described in Sec-           can define a large space of graspable rectangles (e.g., covering
tion IV as input, giving 4032 input features to each network.        the entire length of a pen), we consider a prediction to be
We trained a deep network with 200 hidden units each at              correct if it scores at least 25% by this metric.
the first and second layers using our learning algorithm as                         VII. R ESULTS AND D ISCUSSION
described in Sections III and V. Training this network took
roughly 30 minutes. For trials involving our two-pass system,        A. Deep Learning for Robotic Grasp Detection
we trained a second network with 50 hidden units at each               Figure 8 shows the features learned by the unsupervised
layer in the same manner. During inference we performed an           phase of our algorithm which have a high correlation to
 Positive
 Negative

Fig. 10: Learned 3D depth features: 3D meshes for depth channels of the four features with strongest positive (top) and negative(bottom)
correlations to rectangle graspability. Here X and Y coordinates corresponds to positions in the deep network’s receptive field, and Z
coordinates corresponds to weight values to the depth channel for each location. Feature shapes clearly correspond to graspable and non-
graspable structures, respectively.

                                                                     TABLE II: Recognition results for different modalities, for a deep
positive and negative grasping cases. Many of these features
                                                                     network pre-trained using SAE.
show non-zero weights to the depth channel, indicating that
it learns the correlation of depths to graspability. We can see                  Modes                         Accuracy (%)
                                                                                 Chance                                  50
that weights to many of the modalities for these features have                   RGB                                   90.3
been eliminated by our structured regularization approach. In                    Depth                                 92.4
particular, many of these features lack weights to the U and V                   Surf. Normals                         90.3
                                                                                 Depth + Surf. Normals                 92.8
(3rd and 4th ) channels, which correspond to color, allowing                     RGB + Depth + Surf. Normals           93.7
the system to be more robust to different-colored objects.
   Figure 10 shows 3D meshes for the depth channels of
the four features with the strongest positive and negative
correlations to valid grasps. Even without any supervised infor-     information improves results over either alone, indicating that
mation, our algorithm was able to learn several features which       they give non-redundant information.
correlate strongly to graspable cases and non-graspable cases.          The highest accuracy is still obtained by using all the
The first two positive-correlated features represent handles,        input modalities. This shows that combining depth and color
or other cases with a raised region in the center, while the         information leads to a system which is more robust than
second two represent circular rims or handles. The negatively-       either modality alone. This is due to the fact that some
correlated features represent obviously non-graspable cases,         graspable cases (rims of monochromatic objects, etc.) can only
such as ridges perpendicular to the gripper plane and “valleys”      be detected using depth information, while in others, the depth
between the gripper plates. From these features, we can see          channel may be extremely noisy, requiring the use of color
that even during unsupervised feature learning, our approach         information. From this, we can see that integrating multimodal
is able to learn a representation useful for the task at hand,       information, a major focus of this work, is important in
thanks purely to the fact that the data used is composed of          recognizing good robotic grasps.
half graspable and half non-graspable cases.                            Table III shows that the performance gains from deep learn-
   From Table I, we see that the recognition performance is          ing for recognition carry over to detection, as well. Once mask-
significantly improved with deep learning methods, improving         based scaling has been applied, all deep learning approaches
9% over the features from [28] and 4.1% over those features          except for training separate first-layer features outperform the
combined with FPFH features. Both L1 and group regulariza-           hand-engineered features from [28] by up to 13% for the point
tion performed similarly for recognition, but training separate      metric and 17% for the rectangle metric, while also avoiding
first layer features decreased performance slightly. This shows      the need to design task-specific features. Without mask-based
that learned features, in addition to avoiding hand-design, are      scaling, the system performs poorly, due to the bias illustrated
able to improve performance significantly over the state of          in Fig. 6. Separate first-layer features also give weak detection
the art. It demonstrates that a deep network is able to learn        performance, indicating that the relative scores assigned by
the concept of “graspability” in a way that generalizes to new       this form of network are less robust than those learned using
objects it hasn’t seen before.                                       our structured regularization approach.
   Table II shows that even using any one of the three input            Using structured multimodal regularization also improves
modalities (RGB, depth, or surface normals), our algorithm           results over standard L1 regularization by up to 1.8%, showing
is able to learn features which outperform hand-engineered           that our method also learns more robust features than standard
ones for recognition. Depth gives the highest performance            approaches which ignore modality information. Even though
of any single-mode network. Combining depth and normal               using the first-pass network alone underperforms the second-
TABLE III: Detection results for point and rectangle metrics, for
various learning algorithms.
                                         Image-wise split   Object-wise split
 Algorithm
                                         Point    Rect      Point     Rect
 Chance                                   35.9     6.7      35.9       6.7
 Jiang et al. [28]                        75.3    60.5      74.9      58.3
 SAE, no mask-based scaling               62.1    39.9      56.2      35.4
 SAE, separate layer-1 feat.              70.3    43.3      70.7      40.0
 SAE, L1 reg.                             87.2    72.9      88.7      71.4
 SAE, struct. reg., 1st pass only         86.4    70.6      85.2      64.9
 SAE, struct. reg., 2nd pass only         87.5    73.8      87.6      73.2
 SAE, struct. reg. two-stage              88.4    73.9      88.1      75.6
                                                                                Fig. 12: Improvements from group regularization: Cases where
                                                                                our group regularization approach produces a viable grasp (shown
 Thin gripper Wide gripper

                                                                                in green and yellow), while a network trained only with simple L1
                                                                                regularization does not (shown in blue and red). Top: RGB image,
                                                                                bottom: depth channel. Green and blue edges correspond to gripper.

                             0 degrees      45 degrees          90 degrees

Fig. 11: Visualization of grasping scores for different grippers:
Red indicates maximum score for a grasp with left gripper plane
centered at each point, blue is similar for the right plate. Best-scoring
rectangle shown in green/yellow.

pass network alone by up to 8.3%, integrating both in our two-
pass system outperforms the solo second-pass network by up                      Fig. 13: Improvements from two-stage system: Example cases
                                                                                where the two-stage system produces a viable grasp (shown in green
to 2.4%. This shows that the two-pass system improves not                       and yellow), while the single-stage system does not (shown in blue
only efficiency, but accuracy as well. The performance gains                    and red). Top: RGB image, bottom: depth channel. Green and blue
from multimodal regularization and the two-pass system are                      edges correspond to gripper.
discussed in detail below.
   Our system outperforms all baseline approaches by all
metrics except for the point metric in the object-wise split                       Figure 12 shows typical cases where a network trained using
case. However, we can see that the chance performance is                        our group regularization finds a valid grasp, but a network
much higher for the point metric than for the rectangle metric.                 trained with L1 regularization does not. In these cases, the
This shows that the point metric can overstate performance,                     grasp chosen by the L1 -regularized network appears valid for
and the rectangle metric is a better indicator of the accuracy                  some modalities – the depth channel for the sunglasses and nail
of a grasp detection system.                                                    polish bottle, and the RGB channels for the scissors. However,
                                                                                when all modalities are considered, the grasp is clearly invalid.
Adaptability: One important advantage of our detection                          The group-regularized network does a better job of combining
system is that we can flexibly specify the constraints of the                   information from all modalities and is more robust to noise and
gripper in our detection system. This is particularly important                 missing data in the depth channel, as seen in these cases.
for a robot like Baxter, where different objects might require
different gripper settings to grasp. We can constrain the                       C. Two-stage Detection System
detectors to handle this. Figure 11 shows detection scores                         Using our two-pass system enhanced both computational
for systems constrained based on two different settings of                      performance and accuracy. The number of rectangles the full-
Baxter’s gripper, one wide and one thin. The implications of                    size network needed to evaluate was reduced by roughly a
these results for other types of grippers will be discussed in                  factor of 1000. Meanwhile, detection performance increased
Section IX.                                                                     by up to 2.4% as compared to a single pass with the large-
                                                                                size network, even though using the small network alone
B. Multimodal Group Regularization                                              significantly underperforms the larger network. In most cases,
   Our group regularization term improves detection accuracy                    the top 100 rectangles from the first pass contained the top-
over simple L1 regularization. The improvement is more                          ranked rectangle from an exhaustive search using the second-
significant for the object-wise split than for the image-wise                   stage network, and thus results were unaffected.
split because the group regularization helps the network to                        Figure 13 shows some cases where the first-stage network
avoid overfitting, which will tend to occur more when the                       pruned away rectangles corresponding to weak grasps which
learning algorithm is evaluated on unseen objects.                              might otherwise be chosen by the second-stage network. In
                                                                        PR2: Our second platform was our PR2 robot, “Kodiak.”
                                                                        Similar to Baxter, PR2 has two 7-DoF arms with approx-
                                                                        imately 1 m reach, and we used only the left for these
                                                                        experiments. PR2’s grippers open to a width of 8 cm, and
                                                                        are capable of closing completely from that span, so we did
                                                                        not need to use two settings as with Baxter. We augmented
                                                                        PR2’s gripper friction with gaffer tape on the fingertips.
                                                                           For the experiments on PR2, we used the Kinect already
                                                                        mounted to Kodiak’s head, and used ROS’s built-in function-
                                                                        ality to obtain 3D locations from that Kinect and transform
                                                                        these to Kodiak’s body frame for manipulation. Control was
Fig. 14: Robotic experiment objects: Several of the objects used
in experiments, including challenging cases such as an oddly-shaped
                                                                        performed using the ee cart stiffness controller [5] with tra-
RC car controller, a cloth towel, plush cat, and white ice cube tray.   jectories provided by our own custom MATLAB code.
                                                                        Experimental Setup: For each experiment, we placed a
                                                                        single object within a 25 cm x 25 cm square on the ta-
these cases, the grasp chosen by the single-stage system might          ble, approximately 1.2 m below the mounting point of the
be feasible for a robotic gripper, but the rectangle chosen by          Kinect. This square was chosen to be well-contained within
the two-stage system represents a grasp which would clearly             each robot’s workspace, allowing objects to be reached from
be successful.                                                          most approach vectors. Object positions and orientations were
   The two-stage system also significantly increases the com-           varied between trials, although objects were always placed in
putational efficiency of our detection system. Average infer-           configurations in which at least one viable grasp was visible
ence time for a MATLAB implementation of the deep network               and accessible to the robot.
was reduced from 24.6s/image for an exhaustive search using                When using Baxter, due to the limited stroke (span from
the larger network to 13.5s/image using the two-stage system.           open to closed) of its gripper, we pre-selected one of the
                VIII. ROBOTIC E XPERIMENTS                              two gripper settings discussed above for each object. We
                                                                        constrained the search space as illustrated in Fig. 11 to find
   In order to evaluate the performance of our algorithms in the        grasps for that particular setting.
real world, we ran an extensive series of robotic experiments.             To detect grasps, we first took an RGB-D image from the
To explore the generalizability and effect of the robot on              Kinect with no objects in the scene as a background image.
the success rate of our algorithms, we performed experiments            The depth channel of this image was used to segment objects
on two different robotic platforms, a Baxter Research Robot             from the scene, and to correct for the slant of the Kinect. Once
(“Yogi”) and a PR2 (“Kodiak”).                                          an object was segmented, we used our algorithm, as described
Baxter: The first platform used is our Baxter Research Robot,           above, to obtain a single best-ranked grasping rectangle.
which we call “Yogi.” Baxter has two arms with seven degrees               The search space for the first-pass network progressed in 15-
of freedom each and a maximum reach of 104 cm, although we              degree increments from 15 to 180 degrees (angles larger than
used only the left arm for these experiments. The end-effector          180 being mirror-images of grasps already tested), searching
for this arm is a two-finger parallel gripper. We augmented the         over 10-pixel increments across the image for the X and Y
gripper tips using rubber bands for additional friction. Baxter’s       coordinates of the upper-left corner of the rectangle. For the
grippers are interchangable, and we used two settings for these         thin gripper setting, rectangle widths and heights from 10 to
experiments - a “wide” setting with an open width of 8 cm               40 pixels in 10-pixel increments were searched, while for the
and closed width of 4 cm, and a “thin” setting with an open             thick setting these ranged from 40 pixels to 100 pixels in
width of 4 cm and a closed width of 0 cm (completely closed,            20-pixel increments. In both cases, rectangles taller than they
gripper tips touching).                                                 were wide were ignored. Once a single best-scoring grasp was
   To detect grasps, we mounted a Kinect sensor to Yogi’s               detected, we translated it to a robotic grasp consisting of a
head, approximately 1.75 m above the ground. angled down-               grasping point and an approach vector using the rectangle’s
wards at roughly a 75o angle towards a table in front of it.            parameters and the surface normal at the rectangle’s center as
The Kinect gives RGB-D images at a resolution of 640x480                described above.
pixels. We calibrated the transformation between the Kinect’s              To execute the grasp, we first positioned the gripper at
and Yogi’s coordinate frames by marking four points corre-              a location 10 cm back from the grasping point along the
sponding to a set of 3D axes, and obtaining the coordinates             approach vector. The gripper was oriented to the approach
of these points in both Kinect’s and Yogi’s frames.                     vector, and rotated around it based on the orientation of the
   All control for Baxter was done by specifying an end-                detected grasping rectangle.
effector position and orientation, and using the inverse kine-             Since Baxter’s arms are highly compliant, slight impreci-
matics provided with Baxter to determine a set of joint angles          sions in end-effector positioning are to be expected – we found
for this pose. Baxter’s built-in control systems were used to           that errors of up to 2 cm were typical. Thus, we implemented a
drive the arm to these new joint angles.                                visual servoing system using its hand camera, which provides
               TABLE IV: Results for robotic experiments for Baxter, sorted by object category, for a total of 100 trials.
                       Tr. indicates number of trials, Acc. indicates accuracy (in terms of success percentage.)
      Kitchen tools               Lab tools                     Containers                           Toys                         Others
 Object       Tr. Acc.    Object         Tr.   Acc.   Object               Tr.   Acc.   Object            Tr.   Acc.   Object            Tr.   Acc.
 Can opener    3    100   Kinect           5   100    Colored cereal box    3    100    Plastic whale      4     75    Electric shaver    3    100
 Knife         3    100   Wire bundle      3   100    White cereal box      4     50    Plastic elephant   4    100    Umbrella           4     75
 Brush         3    100   Mouse            3   100    Cap-shaped bowl       3    100    Plush cat          4     75    Desk lamp          3    100
 Tongs         3    100   Hot glue gun     3    67    Coffee mug            3    100    RC controller      3     67    Remote control     5    100
 Towel         3    100   Quad-rotor       4    75    Ice cube tray         3    100    XBox controller    4     50    Metal bookend      3     33
 Grater        3    100   Duct tape roll   4   100    Martini glass         3      0    Plastic frog       3     67    Glove              3    100
 Average            100   Average               90    Average                     75    Average                  72    Average                  85
 Overall            84

                 TABLE V: Results for robotic experiments for PR2, sorted by object category, for a total of 100 trials.
                        Tr. indicates number of trials, Acc. indicates accuracy (in terms of success percentage.)
      Kitchen tools               Lab tools                     Containers                           Toys                         Others
 Object       Tr. Acc.    Object         Tr.   Acc.   Object               Tr.   Acc.   Object            Tr.   Acc.   Object            Tr.   Acc.
 Can opener    3    100   Kinect           5   100    Colored cereal box    3    100    Plastic whale      4     75    Electric shaver    3    100
 Knife         3    100   Wire bundle      3   100    White cereal box      4    100    Plastic elephant   4    100    Umbrella           4    100
 Brush         3    100   Mouse            3   100    Cap-shaped bowl       3    100    Plush cat          4    100    Desk lamp          3    100
 Tongs         3    100   Hot glue gun     3    67    Coffee mug            3    100    RC controller      3     67    Remote control     5    100
 Towel         3    100   Quad-rotor       4   100    Ice cube tray         3    100    XBox controller    4     25    Metal bookend      3     67
 Grater        3    100   Duct tape roll   4   100    Martini glass         3      0    Plastic frog       3     67    Glove              3    100
 Average            100   Average               95    Average                     83    Average                  72    Average                  95
 Overall            89

Fig. 15: Robots executing grasps: Our robots grasping several objects from the experimental dataset. Top row: Baxter grasping a quad-rotor
casing, coffee mug, ice cube tray, knife, and electric shaver. Middle row: Baxter grasping a desk lamp, cheese grater, umbrella, cloth towel,
and hot glue gun. Bottom row: PR2 grasping a plush cat, RC car controller, cereal box, toy elephant, and glove.
RGB images at a resolution of 320x200 pixels. We used color         underperforming our system.
segmentation to separate the object from the background, and           On Baxter, our algorithm sometimes detected a grasp which
used its lateral position in image space to drive Yogi’s end-       was not realizable by the current setting of its gripper, but
effector to center the object. We did not implement visual          might be executable by others. For example, our algorithm
servoing for PR2 because its gripper positioning was found to       detected grasps across the leg of the plush cat, and the region
be precise to within 0.5 cm.                                        between the handle and body of the umbrella, both too thin
    After visual servoing was completed, we drove the gripper       for the wide setting of Baxter’s gripper to grasp since it has
14 cm forwards from its current position along the approach         a minimum span of 4 cm. Since PR2’s gripper can close
vector, so that the grasping point was well-contained within        completely from any position, it did not encounter these issues
it. We then closed the gripper, grasping the object, and moved      and thus achieved a 100% success rate for both these objects.
it 30 cm upwards. A grasp was determined to be successful if           The XBox controller proved to be a very difficult object for
it was sufficient to lift the object and hold it for one second.    either robot to grasp. From a top-down angle, there is only a
                                                                    small space of viable grasps with a span of less than 8 cm, but
Objects to be Grasped: For our robotic experiments, we
                                                                    many which have either a slightly larger span (making them
collected a diverse set of 35 objects within a size of .3 m x .3
                                                                    non-realizable by either gripper), or are subtly non-viable (e.g.
m x .3 m and weighing at most 2.5 kg (although most were
                                                                    grasps across the two “handles,” which tend to slip off.) All
less than 1 kg) from our offices, homes, and lab. Many of them
                                                                    viable grasps are very near to the 8 cm span of both grippers,
are shown in Fig. 14. Most of these objects were not present
                                                                    meaning that even slight imprecision in positioning can lead to
in the training dataset, and thus were completely new to the
                                                                    failure. Due to this, Baxter achieved a higher success rate for
grasp detection algorithm.
                                                                    the XBox controller thanks to visual servoing, succeeding in
   Due to the physical limitations of the robots’ grippers,
                                                                    50% of cases as compared to the 25% success rate for PR2.
we found that five of these objects were not graspable even
                                                                       Our algorithm was able to consistently detect and execute
when given a hand-chosen grasp. The small pair of pliers
                                                                    valid grasps for a red cereal box, but had some failures on a
was too low to the table to grip properly. The spray paint
                                                                    white and yellow one. This is because the background for all
can was too smooth for the gripper to get enough friction
                                                                    objects in the dataset is white, leading the algorithm to learn
to lift it. The weight of the hammer was too imbalanced,
                                                                    features relating white areas at the edges of the gripper region
causing the hammer to rotate and slip out of the gripper when
                                                                    to graspable cases. However, it was able to detect and execute
grasped. Similar problems were encountered with the bicycle
                                                                    correct grasps for an all-white ice cube tray, and so does not
U-lock. The bevel spatula’s handle was too close to the thin-
                                                                    fail for all white objects. This could be remedied by extending
set size of Baxter’s gripper, so that we could not position
                                                                    the dataset to include cases with different background colors.
it precisely enough to grasp it reliably. We did not consider
                                                                    Interestingly, even though the parameters of grasps detected
these objects for purposes of our experimental results, since
                                                                    for the white box were similar for PR2 and Baxter, PR2 was
our focus was on evaluating the performance of our grasp
                                                                    able to succeed in every case while Baxter succeeded only
detection algorithm.
                                                                    half the time. This is because PR2’s increased gripper strength
Results: Table IV shows the results of our robotic experiments      allowed it to execute grasps across corners of the box, crushing
on Baxter for the remaining 30 objects, a total of 100 trials.      it slightly in the process.
Using our algorithm, Yogi was able to successfully execute a           Other failures were due to the limitations of the Kinect
grasp in 84% of the trials. Figure 15 shows Yogi executing          sensor. We were never able to properly grasp the martini glass
several of these grasps. In 8% of the trials, our algorithm         because its glossy finish prevented Kinect from returning any
detected a valid grasp which was not executed correctly by          depth estimates for it. Even if a valid grasp were detected
Yogi. Thus, we were able to successfully detect a good grasp        using color information only, there was no way to infer a
in 92% of the trials. Video of some of these trials is available    proper grasping position without depth information. Grasps
at http://pr.cs.cornell.edu/deepgrasping.                           for the metal bookend failed for similar reasons, but it was
   PR2 yielded a higher success rate as seen in Table V,            not as glossy as the martini glass, and gave enough returns
succeeding in 89% of trials. This is largely due to the much        for some to succeed.
wider span of PR2’s gripper from open to closed and its ability        However, our algorithm also had many noteworthy suc-
to fully close from its widest position, as well as PR2’s ability   cesses. It was able to consistently detect and execute grasps for
to apply a larger gripping force. Some specific instances where     a crumpled cloth towel, a complex and irregular case which
PR2 and Baxter’s performance differed are discussed below.          bore little resemblance to any object in the dataset. It was also
   For comparison purposes, we ran a small set of control           able to find and grasp the rims of objects such as the plastic
experiments for 16 of the objects in the dataset. The control       baseball cap and coffee mug, cases where there is little visual
algorithm simply returned a fixed-size rectangle centered at the    distinction between the rim and body of the object. These
object’s center of mass, as determined by depth segmentation        objects underscore the importance of the depth channel for
from the background. The rectangle was aligned so that the          robotic grasping, as none of these grasps would be detectable
gripper plates ran parallel to the object’s principal axis. This    without depth information.
algorithm was only successful in 31% of cases, significantly           Our algorithm was also able to successfully detect and
execute many grasps for which the approach vector was non-           Adding a term modeling the probability of each region of
vertical. The grasps shown for the coffee mug, desk lamp,            the image being a semantically-appropriate area to grasp the
cereal box, RC car controller, and toy elephant shown in             object would allow us to incorporate this information. This
Fig. 15 were all executed by aligning the gripper to such an         term could be computed once for the entire image, then added
approach vector. Indeed, many of these grasps may have failed        to each local detection score, keeping detection efficient.
had the gripper been aligned vertically. This shows that our            In this work, our visual-servoing algorithm was purely
algorithm is not restricted to detecting top-down grasps, but        heuristic, simply attempting to center the segmented object
rather encodes a more general notion of graspability which           underneath the hand camera. However, in future work, a simi-
can be applied to grasps from many angles, albeit within the         lar feature-learning approach might be applied to hand camera
constraints of visibility from a single-view perspective.            images of graspable and non-graspable regions, improving the
   While a few failures occurred, our algorithm still achieved       visual servoing system’s ability to fine-tune gripper position
a high rate of accuracy for other oddly-shaped objects such          to ensure a good grasp.
as the quad-rotor casing, RC car controller, and glue gun.              Many robotics problems require the use of perceptual infor-
For objects with clearly defined handles, such as the cheese         mation, but can be difficult and time-consuming to engineer
grater, kitchen tongs, can opener, and knife, our algorithm was      good features for, particularly when using RGB-D data. In
able to detect and execute successful grasps in every trial,         future work, our approach could be extended to a wide range
showing that there is a wide range of objects which it can           of such problems. Our system could easily be applied to
grasp extremely consistently.                                        other detection problems such as object detection or obstacle
                                                                     detection. However, it could also be adapted to other similar
           IX. D ISCUSSION AND F UTURE W ORK                         problems, such as object tracking and visual servoing.
   Our algorithm focuses on the problem of grasp detection for          Multimodal data has become extremely important for
a two-fingered parallel-plate style gripper. It would be directly    robotics, due both to the advent of new sensors such as the
applicable to other grippers with fixed configurations, simply       Kinect and the application of robots to more challenging tasks
requiring new training data labeled with grasps for the gripper      which require multiple modalities of information to perform
in question. Our system would allow even the basic features          well. However, it can be very difficult to design features which
used for grasp detection to adapt to the gripper. This might be      do a good job of integrating many modalities. While our
useful in cases such as jamming grippers [29], or two-fingered       work focuses on color, depth, and surface normals as input
grippers with differently-shaped contact surfaces, which might       modes, our structured multimodal regularization algorithm
require different features to determine a graspable area.            might also be applied to others. This approach could improve
   Our detection algorithm does not directly address the prob-       performance while allowing roboticists to focus on other
lem of 3D orientation of the gripper – this orientation is           engineering challenges.
determined only after an optimal rectangle has been detected,
orienting the grasp based on the object’s surface normals.                                 X. C ONCLUSIONS
However, just as our approach here considers aligns a 2D                We presented a system for detecting robotic grasps from
feature window to the gripper, an extension of this work might       RGB-D data using a deep learning approach. Our method
align a 3D window – using voxels, rather than pixels, as its         has several advantages over current state-of-the-art methods.
basic unit of representation for input features to the network.      First, using deep learning allows us to avoid hand-engineering
This would allow the system to search across the full 6-DoF          features, learning them instead. Second, our results show that
3D pose of the gripper, while still leveraging the power of          deep learning methods significantly outperform even well-
feature learning.                                                    designed hand-engineered features from previous work.
   Our system gives only a gripper pose as output, but multi-           We also presented a novel feature learning algorithm for
fingered reconfigurable hands also require a configuration of        multimodal data based on group regularization. In extensive
the fingers in order to grasp an object. In this case, our           experiments, we demonstrated that this algorithm produces
algorithm could be used as a heuristic to find one or more           better features for robotic grasp detection than existing deep
locations likely to be graspable (similar to the first pass in our   learning approaches to multimodal data. Our experiments and
two-pass system), greatly reducing the search space needed to        results, both offline and on real robotic platforms, show that
find an optimal gripper configuration.                               our two-stage deep learning system with group regularization
   Our algorithm also depends only on local features to de-          is capable of robustly detecting grasps for a wide range of
termine grasping locations. However, many household objects          objects, even those previously unseen by the system.
may have some areas which are strongly preferable to grasp
over others - for example, a knife might be graspable by                                ACKNOWLEDGEMENTS
the blade, or a hot glue gun by the barrel, but both should             We would like to thank Yun Jiang and Marcus Lim for
actually be grasped by their respective handles. Since these         useful discussions and help with baseline experiments. This
regions are more likely to be labeled as graspable in the            research was funded in part by ARO award W911NF-12-1-
data, our system already weakly encodes this, but some may           0267, Microsoft Faculty Fellowship and NSF CAREER Award
not be readily distinguishable using only local information.         (Saxena), and Google Faculty Research Award (Lee).
                        R EFERENCES                                    The Columbia grasp database. In ICRA, 2009.
                                                                  [21] I. Goodfellow, Q. Le, A. Saxe, H. Lee, and A. Y. Ng.
 [1] Y. Bengio. Learning deep architectures for AI. FTML,              Measuring invariances in deep networks. In NIPS, 2009.
     2(1):1–127, 2009.                                            [22] G. Hinton and R. Salakhutdinov. Reducing the dimen-
 [2] A. Bicchi and V. Kumar. Robotic grasping and contact:             sionality of data with neural networks. Science, 313
     a review. In ICRA, 2000.                                          (5786):504–507, 2006.
 [3] L. Bo, X. Ren, and D. Fox. Unsupervised Feature              [23] K. Huebner and D. Kragic. Selection of Robot Pre-
     Learning for RGB-D Based Object Recognition. In ISER,             Grasps using Box-Based Shape Approximation. In IROS,
     2012.                                                             2008.
 [4] J. Bohg, A. Morales, T. Asfour, and D. Kragic. Data-         [24] A. Hyvärinen, P. O. Hoyer, and M. Inki. Topographic
     driven grasp synthesis - a survey. accepted.                      independent component analysis. Neural computation,
 [5] M. Bollini, J. Barry, and D. Rus. Bakebot: Baking                 13(7):1527–1558, 2001.
     cookies with the pr2. In IROS PR2 Workshop, 2011.            [25] A. Hyvärinen, J. Karhunen, and E. Oja. Principal
 [6] D. Bowers and R. Lumia. Manipulation of unmodeled                 Component Analysis and Whitening, chapter 6, pages
     objects using intelligent grasping schemes. IEEE Trans            125–144. John Wiley & Sons, Inc., 2002.
     Fuzzy Sys, 11(3), 2003.                                      [26] A. Jalali, P. Ravikumar, S. Sanghavi, and C. Ruan. A
 [7] C. Cadena and J. Kosecka. Semantic parsing for priming            dirty model for multi-task learning. In NIPS, 2010.
     object detection in rgb-d scenes. In ICRA Workshop on        [27] N. R. Jared Glover, Daniela Rus. Probabilistic models
     Semantic Perception, Mapping and Exploration, 2013.               of object geometry for grasp planning. In RSS, 2008.
 [8] A. Coates and A. Y. Ng. Selecting receptive fields in        [28] Y. Jiang, S. Moseson, and A. Saxena. Efficient grasping
     deep networks. In NIPS, 2011.                                     from RGBD images: Learning using a new rectangle
 [9] A. Coates, B. Carpenter, C. Case, S. Satheesh, B. Suresh,         representation. In ICRA, 2011.
     T. Wang, D. J. Wu, and A. Y. Ng. Text detection and          [29] Y. Jiang, J. R. Amend, H. Lipson, and A. Saxena. Learn-
     character recognition in scene images with unsupervised           ing hardware agnostic grasps for a universal jamming
     feature learning. In ICDAR, 2011.                                 gripper. In ICRA, 2012.
[10] A. Collet Romea, D. Berenson, S. Srinivasa, and D. Fer-      [30] Y. Jiang, M. Lim, C. Zheng, and A. Saxena. Learning to
     guson . Object recognition and full pose registration from        place new objects in a scene. IJRR, 31(9), 2012.
     a single image for robotic manipulation. In ICRA, 2009.      [31] I. Kamon, T. Flash, and S. Edelman. Learning to grasp
[11] A. Collet Romea, M. Martinez Torres, and S. Srinivasa.            using visual information. In ICRA, 1996.
     The moped framework: Object recognition and pose             [32] D. Kragic and H. I. Christensen. Robust visual servoing.
     estimation for manipulation. IJRR, 30(10):1284 – 1306,            IJRR, 2003.
     2011.                                                        [33] K. Lai, L. Bo, X. Ren, and D. Fox. A large-scale
[12] R. Collobert, J. Weston, L. Bottou, M. Karlen,                    hierarchical multi-view rgb-d object dataset. In ICRA,
     K. Kavukcuoglu, and P. Kuksa. Natural language pro-               2011.
     cessing (almost) from scratch. JMLR, 12:2493–2537,           [34] K. Lakshminarayana. Mechanics of form closure. ASME,
     2011.                                                             1978.
[13] R. Detry, E. Baseski, M. Popovic, Y. Touati, N. Kruger,      [35] Q. Le, M. Ranzato, R. Monga, M. Devin, K. Chen,
     O. Kroemer, J. Peters, and J. Piater. Learning object-            G. Corrado, J. Dean, and A. Ng. Building high-level
     specific grasp affordance densities. In ICDL, 2009.               features using large scale unsupervised learning. In
[14] M. Dogar, K. Hsiao, M. Ciocarlie, and S. Srinivasa.               ICML, 2012.
     Physics-based grasp planning through clutter. In RSS,        [36] Q. V. Le, D. Kamm, A. F. Kara, and A. Y. Ng. Learning
     2012.                                                             to grasp objects with multiple contact points. In ICRA,
[15] S. Ekvall and D. Kragic. Learning and evaluation of               2010.
     the approach vector for automatic grasp generation and       [37] Y. LeCun, F. Huang, and L. Bottou. Learning methods
     planning. In ICRA, 2007.                                          for generic object recognition with invariance to pose and
[16] F. Endres, J. Hess, J. Sturm, D. Cremers, and W. Burgard.         lighting. In CVPR, 2004.
     3d mapping with an RGB-D camera. International               [38] H. Lee, R. Grosse, R. Ranganath, and A. Y. Ng. Convo-
     Journal of Robotics Research (IJRR), 2013.                        lutional deep belief networks for scalable unsupervised
[17] C. Ferrari and J. Canny. Planning optimal grasps. ICRA,           learning of hierarchical representations. In ICML, 2009.
     1992.                                                        [39] H. Lee, Y. Largman, P. Pham, and A. Y. Ng. Unsu-
[18] C. R. Gallegos, J. Porta, and L. Ros. Global optimization         pervised feature learning for audio classification using
     of robotic grasps. In RSS, 2011.                                  convolutional deep belief networks. In NIPS, 2009.
[19] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich      [40] J. Maitin-shepard, M. Cusumano-towner, J. Lei, and
     feature hierarchies for accurate object detection and             P. Abbeel. Cloth grasp point detection based on multiple-
     semantic segmentation. In CVPR, 2014.                             view geometric cues with application to robotic towel
[20] C. Goldfeder, M. Ciocarlie, H. Dang, and P. K. Allen.             folding. In ICRA, 2010.
[41] A.-R. Mohamed, G. Dahl, and G. E. Hinton. Acoustic            [63] C. Teuliere and E. Marchand. Direct 3d servoing using
     modeling using deep belief networks. IEEE Trans Audio,             dense depth maps. In IROS, 2012.
     Speech, and Language Processing, 20(1):14–22, 2012.           [64] P. Viola and M. Jones. Rapid object detection using a
[42] A. Morales, P. J. Sanz, and Àngel P. del Pobil. Vision-           boosted cascade of simple features. In CVPR, 2001.
     based computation of three-finger grasps on unknown           [65] J. Weisz and P. K. Allen. Pose error robust grasping from
     planar objects. In IROS, 2002.                                     contact wrench space metrics. In ICRA, 2012.
[43] J. Ngiam, A. Khosla, M. Kim, J. Nam, H. Lee, and A. Y.        [66] T. Whelan, H. Johannsson, M. Kaess, J. Leonard, and
     Ng. Multimodal deep learning. In ICML, 2011.                       J. McDonald. Robust real-time visual odometry for dense
[44] V. Nguyen. Constructing stable force-closure grasps. In            RGB-D mapping. In ICRA, 2013.
     ACM Fall joint computer conf, 1986.                           [67] L. Zhang, M. Ciocarlie, and K. Hsiao. Grasp evaluation
[45] M. Osadchy, Y. LeCun, and M. Miller. Synergistic face              with graspable feature matching. In RSS Workshop on
     detection and pose estimation with energy-based models.            Mobile Manipulation, 2011.
     JMLR, 8:1197–1215, 2007.
[46] C. Papazov, S. Haddadin, S. Parusel, K. Krieger, and
     D. Burschka. Rigid 3d geometry matching for grasping
     of known objects in cluttered scenes. IJRR, 31(4):538–
     553, Apr. 2012.
[47] J. H. Piater. Learning visual features to predict hand
     orientations. In ICML, 2002.
[48] F. T. Pokorny, K. Hang, and D. Kragic. Grasp moduli
     spaces. In RSS, 2013.
[49] J. Ponce, D. Stam, and B. Faverjon. On computing two-
     finger force-closure grasps of curved 2D objects. IJRR,
     12(3):263, 1993.
[50] A. Rodriguez, M. Mason, and S. Ferry. From caging to
     grasping. In RSS, 2011.
[51] R. B. Rusu, N. Blodow, and M. Beetz. Fast point feature
     histograms (FPFH) for 3D registration. In ICRA, 2009.
[52] R. B. Rusu, G. Bradski, R. Thibaux, and J. Hsu. Fast
     3D recognition and pose using the viewpoint feature
     histogram. In IROS, 2010.
[53] A. Sahbani, S. El-Khoury, and P. Bidaud. An overview
     of 3d object grasp synthesis algorithms. Robot. Auton.
     Syst., 60(3):326–336, Mar. 2012.
[54] A. Saxena, J. Driemeyer, J. Kearns, and A. Ng. Robotic
     grasping of novel objects. In NIPS, 2006.
[55] A. Saxena, J. Driemeyer, and A. Y. Ng. Robotic grasping
     of novel objects using vision. IJRR, 27(2):157–173,
     2008.
[56] A. Saxena, L. L. S. Wong, and A. Y. Ng. Learning grasp
     strategies with partial shape information. In AAAI, 2008.
[57] P. Sermanet, K. Kavukcuoglu, S. Chintala, and Y. Le-
     Cun. Pedestrian detection with unsupervised multi-stage
     feature learning. In CVPR. 2013.
[58] K. B. Shimoga. Robot grasp synthesis algorithms: A
     survey. IJRR, 15(3):230–266, June 1996.
[59] R. Socher, B. Huval, B. Bhat, C. D. Manning, and A. Y.
     Ng. Convolutional-recursive deep learning for 3D object
     classification. In NIPS, 2012.
[60] K. Sohn, D. Y. Jung, H. Lee, and A. Hero III. Efficient
     learning of sparse, distributed, convolutional feature rep-
     resentations for object recognition. In ICCV, 2011.
[61] N. Srivastava and R. Salakhutdinov. Multimodal learning
     with deep Boltzmann machines. In NIPS, 2012.
[62] C. Szegedy, A. Toshev, and D. Erhan. Deep neural
     networks for object detection. In NIPS. 2013.
