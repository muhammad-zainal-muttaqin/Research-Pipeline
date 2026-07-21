---
source_id: 183
bibtex_key: sundermeyer2021contactgraspnet
title: Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes
year: 2021
domain_theme: Grasp Robotik
verified_pdf: 183_Contact-GraspNet.pdf
char_count: 52029
---

Contact-GraspNet: Efficient 6-DoF Grasp Generation
                                                                          in Cluttered Scenes
                                                    Martin Sundermeyer1,2,3               Arsalan Mousavian1               Rudolph Triebel2,3                Dieter Fox1,4

                                            Abstract— Grasping unseen objects in unconstrained, clut-
                                         tered environments is an essential skill for autonomous robotic
                                         manipulation. Despite recent progress in full 6-DoF grasp
                                         learning, existing approaches often consist of complex sequen-
                                         tial pipelines that possess several potential failure points and
arXiv:2103.14127v1 [cs.RO] 25 Mar 2021

                                         run-times unsuitable for closed-loop grasping. Therefore, we
                                         propose an end-to-end network that efficiently generates a
                                         distribution of 6-DoF parallel-jaw grasps directly from a depth
                                         recording of a scene. Our novel grasp representation treats
                                         3D points of the recorded point cloud as potential grasp
                                         contacts. By rooting the full 6-DoF grasp pose and width in
                                         the observed point cloud, we can reduce the dimensionality
                                         of our grasp representation to 4-DoF which greatly facilitates
                                         the learning process. Our class-agnostic approach is trained on
                                         17 million simulated grasps and generalizes well to real world
                                         sensor data. In a robotic grasping study of unseen objects in
                                         structured clutter we achieve over 90% success rate, cutting
                                         the failure rate in half compared to a recent state-of-the-art
                                         method. Video of the real world experiments and code are avail-
                                         able at https://research.nvidia.com/publication/                         Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in
                                         2021-03_Contact-GraspNet%3A--Efficient.                                  cluttered scenes while avoiding collisions.

                                                                I. I NTRODUCTION
                                            The ability to grasp objects is one of the fundamen-                  space of possible grasps to planar grasping, where grasps
                                         tal capabilities required in most robot manipulation tasks.              are represented by oriented rectangles around each pixel
                                         Grasping involves reasoning about the 3D geometry and                    that define the grasp frame [7, 8, 9]. Such a representation
                                         physics properties of the object such as mass and friction, and          needs the camera to view the scene perpendicularly and
                                         also reasoning about complex contact physics. It is studied              thus limits 3D reasoning and applications significantly. A
                                         in two main directions: Model-based grasping where the                   large number of possible grasps and the full kinematic
                                         3D model or category of the object is known and model-                   capabilities of the robot are also neglected. To address the
                                         free grasping where there is no prior knowledge about the                limitations of planar grasping, there has been a recent interest
                                         object. Model-based grasping circumvents reasoning about                 in tackling the problem of 6-DoF grasping of unknown
                                         the physics of contact and grasp generation by pre-defining              objects [10, 11, 12, 13, 14]. In this paper, we tackle 6-DoF
                                         a set of grasps in the object frame and transform those grasps           grasping of unknown objects in cluttered space from a partial
                                         according to the 6-DoF object pose [1, 2, 3, 4] or detected              point cloud observation of the scene.
                                         keypoints of the objects [5, 6]. The downside of model-based                Grasping objects from cluttered scenes with structure
                                         approaches is that they only work on a limited subset of                 introduces extra challenges. The target objects must be
                                         known objects or categories, and any errors in detecting 6-              grasped successfully, while at the same time any collision
                                         DoF object pose or object keypoints degrade the grasping                 with other objects must be avoided to prevent damages or
                                         performance.                                                             transformations into other undesired states. This is particu-
                                            Model-free approaches do not make any strong assump-                  larly important in home robotics and healthcare applications.
                                         tions about the category or shape of the object, and they                Additionally, it is crucial to generate a diverse set of grasps
                                         learn a shared representation for all object shapes and sizes.           for the object due to robot kinematic constraints. Depending
                                         However, having one shared representation for all objects                on the relative pose between the object and the robot, a
                                         in addition to the large SE(3) space for the grasp poses                 different subset of grasps is kinematically feasible.
                                         makes the learning problem quite challenging. As a result,                  Our method is closely related to the work of Murali et
                                         a large body of work in data-driven grasping constraints the             al. [12], where the goal is to generate collision-free diverse
                                                                                                                  grasps for a designated target object from a partial point
                                            ∗ This work is done while the first author was an intern at NVIDIA.
                                         1 NVIDIA (amousavian,dieterf)@nvidia.com, 2 German
                                                                                                                  cloud of the scene, and the objects are segmented using
                                         Aerospace Center (DLR) <first>.<last>@dlr.de, 3 Technical                a pre-trained unknown object instance segmentation model
                                         University of Munich (TUM), 4 University of Washington                   [15, 16]. Murali et al. [12] use a multi-stage process that
synthesizes grasps for the target objects from the segmented       constructions are often ambiguous, coarse and require class-
object point cloud with no context around it, and then filters     conditioning [24, 25, 26]. Multiple views for 3D scanning
out the colliding grasps using another learned model. This         are beneficial [27] but not always obtainable, take additional
leads to three issues: 1) Sensitivity to instance segmentation     time and typically assume a static scene. In our approach a
errors. 2) Grasps are generated just from the target object        full explicit 3D reconstruction is not required.
point cloud and do not leverage geometric cues in the              Discriminative methods: Discriminative methods for grasp-
scene such as table points and surrounding object points. 3)       ing train a classifier that evaluates the quality of existing
Grasps are predicted in the large, unconstrained 6-DoF pose        grasps [28, 29, 7]. They use different sampling strategies
space. To address these issues, our method instead directly        to generate potential candidates. For planar grasping, cross
processes a full scene point cloud or a local region around a      entropy is widely used since it can converge to the final grasp
target object. Therefore, the quality of our generated grasps      location by iteratively evaluating the quality of grasps in dif-
is not depending on an accurate mask and collisions can            ferent locations [7]. However, the cross-entropy method does
be directly taken into account during generation. Instance         not work well in the higher dimensional 6-DoF grasp space.
segmentation can then subsequently be used to filter grasps        To overcome the sampling complexity issue, grasp locations
belonging to a target object. Thus, our main contributions         are often sampled using geometric heuristics [10, 29].
are the following:                                                 Generative methods: Learning-based generative grasp
   • A new end-to-end method for 6-DoF grasping of un-             methods aim to overcome the limitations of geometric heuris-
     known objects in cluttered real world scenes where we         tics and generate meaningful 6-DoF grasps often from expe-
     achieve 90% grasp success rate. This is 10% higher than       rience in a physics simulator [11, 12]. The main challenge
     [12] in equal settings.                                       is the large, multi-modal search space of 6-DoF grasps.
   • A new grasp pose representation that projects 6-DoF           Instead of sampling some potential candidates using heuris-
     grasps to their contact points in an observed point cloud.    tics and ranking them, these models directly predict a per-
     Our representation has only 4-DoF which facilitates the       point graspability score and approach direction in SO(3)
     learning problem significantly.                               space [30, 14, 31]. One problem with predicting approach
   • Comprehensive ablation studies in a physics simulator         directions is that they cannot easily capture high curvature
     to evaluate the effects of different loss functions and       areas such as mug rims or handles and also can not rep-
     training data.                                                resent grasps encompassing hollow structures. Furthermore,
                                                                   successful approach directions are quite ambiguous to learn
                    II. R ELATED W ORK                             as multiple ones are possible for a single contact. Instead
   As a fundamental problem in robotics, grasping has been         we propose to predict 6-DoF grasps densely projected to
studied for decades [17, 18, 19, 20]. We review related            their much less ambiguous contact points. While grasps
literature in the context of data-driven methods.                  without full surface contact are plausible, e.g. through the
End-to-end policy learning: One line of work for grasping          handle of a mug, the knowledge about the object state and
and manipulation of objects employs an end-to-end pol-             therefore the ability to steadily place the object again is
icy that learns to generate actions from raw input pixel           lost. Therefore, in this work we are aiming to generate
values [21, 22]. This results in a monolithic model that           stable grasps for unknown objects with full surface contact.
concurrently reasons about perception, planning, grasping,         Our novel loss formulation further improves convergence
and controlling the robot. A large group of these works learn      by accounting for the discontinuities, imbalance and multi
from interactions of the robot with the environment through        modality of the grasp distribution. Unlike other methods [31],
reinforcement learning. These approaches have mostly shown         our proposed method is independent of category labels and
promise in bin picking, in (quasi-) planar grasping and in         has no assumption of grasps being always perpendicular to
small, insensible workspaces that do not require complicated       a surface. Instead we learn a grasp semantic purely from a
motion planning in the robot configuration space. Few works        wide variety of grasp annotated training shapes [32].
[23] have demonstrated iterative 6-DoF grasping approaches
with a monolithic policy by combining imitation learning                                   III. M ETHOD
and reinforcement learning. A common drawback of these                We consider the problem of generating 6-DoF grasps from
methods is the limited generalization to novel environments,       any viewpoint on structured clutter consisting of unknown
because the perception and control are learned indirectly at       objects. Our approach takes in a raw depth image, optionally
the same time. In addition, these methods are not easily           with object masks, and generates 6-DoF grasp proposals
steerable towards grasping a specific object as the reward         together with corresponding grasp widths. Our goal is to
function encourages grasping any object. In contrast, our          predict grasps that are robust, diverse and non-colliding from
method learns to generate diverse 6-DoF grasps on novel            an only partially observable scene.
objects and scenes for specifiable target objects while just us-      From a learning perspective, generating the distribution
ing simulated training data. Additionally, it can be integrated    of successful 6-DoF grasps is quite challenging, because
with other perception and motion planning algorithms.              the distribution is multi-modal, discontinuous, imbalanced
3D reconstruction: A complete 3D reconstruction enables            and ambiguous due to (self-) occlusions. Furthermore, direct
traditional grasp planning. However, learned single-view re-       regression in high dimensional output spaces like SE(3) has
Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes.
Grasp poses that produce gripper model collisions are removed. Resulting grasps are mapped to their contacts on the mesh surface. During training, we
sample virtual cameras to render point clouds from the scenes. We consider recorded points (yellow) as positive contacts if there exists a mesh contact
(blue) in a 5mm radius and associate the grasp transformation belonging to the closest mesh contact to them. These per-point annotations are used to
supervise the Contact Grasp Network.

                                                                             learning problem to estimating the 3-DoF grasp rotation
                                                                             Rg ∈ R3×3 and grasp width w ∈ R of a parallel-yaw gripper.
                                                                                Starting from a contact point c ∈ R3 , where the gripper
                                                                             baseline intersects the mesh, we depict a 6-DoF grasp pose
                                                                             g ∈ G defined by (Rg , tg ) ∈ SE(3) and grasp width w ∈ R
                                                                             as
                                                                                                                 w
                                                                                                      tg = c +      b + da                         (1)
                                                                                                                  2
                                                                                                                          
                                                                                                         |          |    |
                                                                                                   Rg = b       a × b a ,                        (2)
                                                                                                         |          |    |
                                                                             where a ∈ R3 , ||a|| = 1 is the approach vector, b ∈
                                                                             R3 , ||b|| = 1 is the grasp baseline vector, and d ∈ R is the
Fig. 3. Our grasp representation: c depicts an observed contact point. a     constant distance from the gripper baseline to the gripper
and b constitute the 3-DoF rotation, w is the predicted grasp width, d the
distance from baseline to base frame. In pink we show the five gripper
                                                                             base. Our grasp representation is depicted in Figure 3.
points v that we used in the ladd−s loss.                                       The reduced dimensionality greatly facilitates the learning
                                                                             process compared to methods that estimate grasp poses in
                                                                             unconstrained SE(3) space. It also increases the pose accu-
been shown to be difficult in grasping [11] and also in related              racy of predicted grasps as they are bound to the geometry
fields such as object pose estimation [33].                                  of the observed scene. In contrast to axis-angle representa-
                                                                             tions, our rotation representation has neither ambiguities nor
A. Grasp Representation                                                      discontinuities. Moreover, at test time we can sample grasp
                                                                             proposals by sampling contact points that cover the whole
   For these reasons, finding an efficient grasp representation              observable surface of the scene/object and thus represent the
is crucial to solve this task using learning-based methods.                  modes of the 6-DoF grasp distribution well. While a 3D
This representation should generalize well to unseen objects                 view on the scene is preferable, even a frontal view on a
and handle the high-dimensional output space well.                           box produces reasonable grasps due to the radial mapping.
   Contact Grasp Representation: We observe that for                            Point Set Networks such as PointNet++ [34] effectively
most predictable two-finger grasps at least one of the two                   process point clouds and hierarchically aggregate points
contacts is visible prior to grasping. In contrast, grasps                   and their feature representations in local 3D neighborhoods.
without any visible contact are often ambiguous or do not                    Their predictions can be directly associated to 3D points in
preserve the initial object pose after grasping. Therefore, we               the input point cloud and our proposed grasp representation
map a distribution of successful 6-DoF ground truth grasps                   exploits this ability.
g ∈ G to their corresponding contact points c ∈ R3 . Since
visible contact points are bound to lie on surfaces that we                  B. Data Generation
can observe with a depth sensor, we can represent their 3D                      To learn the full distribution of stable 6-DoF grasps,
location by nearby points in a recorded point cloud.                         diverse and dense grasp pose annotations are required. We
   Given that we can predict whether observed points are                     used the ACRONYM dataset [32], which consists of 8872
suitable grasp contacts, we can thus reduce the 6-DoF grasp                  meshes from the Shapenet dataset [35] and 17.7 million
simulated grasps under varying friction. An overview of our       D. Target Losses
offline and online training data generation is given in Fig. 2.      The contact grasp success predictions ŝ ∈ R are evaluated
   During training we render a scene point cloud P =              at all output points pi ∈ R3 : ∀i ∈ [0, m] using binary cross
{p1 , . . . , pn } ⊂ R3 and assign a point-wise grasp success     entropy. We only backpropagate the top-k point predictions
                              (                                   with the largest errors lbce,k , with k=512, to counteract data
                                1 minj ||pi − cj ||2 < r          imbalance. The other predictions concerning the geometry
       ∀i = 1, . . . , n si =                               (3)
                                0 otherwise,                      of grasps are only evaluated at positive contact points p+   i .
                                                                  Instead of supervising all network heads in isolation, we
where cj ∈ P are the mesh contact points of non-colliding         propose to combine the predictions to the 6-DoF grasp pose
ground truth grasps gj ∈ G in camera coordinates and r ∈ R        ĝ ∈ G given in Eq. (1) and (2) already during training.
is their maximum propagation radius. Thus, P can be split         We define five 3D points v ∈ R5×3 representing the 6-DoF
into points P − := {pi |si = 0}, where no feasible grasp          gripper pose, as shown in Fig. 3, and transform these using
contact is found within a radius of r = 5mm, and P + :=           all ground truth and predicted grasp poses defined in Eq. (4)
{pi |si = 1}, containing points suitable for a contact. To the
latter ones p+
             i ∈P
                    +
                      we assign the closest grasp as                     vigt =vRg,i
                                                                                 T
                                                                                     + tg,i         vipred = vR̂g,i
                                                                                                                T
                                                                                                                    + t̂g,i   (7)
                                                                    We formulate the 6-DoF grasp loss ladd−s as a weighted
              
               wg,i
                          
                              wg,j
                                                                 minimum average distance between gripper points vgt and
              Rg,i  =      Rg,j                         (4)   vpred where we take the symmetry of the gripper into
                              wj                                  account.
               tg,i      p+
                          i + 2 jb + daj
                                                                                           n+
with                                                                                 1 X
                                                                            ladd−s = +   sˆi min ||vipred − vugt ||2 ,        (8)
                                                                                    n  i
                                                                                              u
                    j = arg min || p+
                                    i − ck ||2              (5)
                           k                                      where n+ is the size of P + . We weight each distance to the
                                                                  closest ground truth grasp points with the predicted contact
   Given sufficient coverage we can thereby project the           success confidence ŝi .
ground truth distribution of 6-DoF grasps densely on the             Our proposed loss formulation has several advantages:
recorded point cloud.                                             (1) We can learn the different modes of the ground truth
                                                                  grasp distribution, e.g. different predicted grasp approach
C. Network                                                        directions â can produce a small error. (2) The point-wise
   We employ the set abstraction and feature propagation lay-     weighting with ŝi couples the contact point classification
ers proposed in PointNet++ [34] to build an asymmetric U-         with the grasp pose predictions. Contact confidence can only
shaped network. The network takes n=20000 random points           increase if the network predicts a 6-DoF grasp pose close to
p ∈ R20000×3 as input and predicts grasps for only m=2048         a ground truth pose. (3) Wrongly predicted grasps in regions
farthest points of the input to make sure the inference fits      far away from any ground truth grasp, e.g. at artificial edges
in GPU memory and predicted grasps have good coverage             from occlusions, produce a high loss and are thus avoided.
over the scene. The network has four heads with two 1D-              On the grasp width bin predictions, we optimize a
Conv layers each and per-point outputs s ∈ R, z1 ∈ R3 , z2 ∈      weighted, multi-label binary cross entropy loss lwidth . Since
R3 , o ∈ R10 , from which we form our grasp representation.       small grasp widths are highly over-represented, we weight
The predicted grasp width ŵi ∈ [0, wmax ] is split into 10       the bin losses anti-proportional to bin size. Our total loss is
equidistant grasp width bins ô ∈ R10 to counteract data          l = αlbce,k + βladd−s + γlwidth with α = 1, β = 10, γ = 1.
imbalance. Then, ŵi is represented by the center value of the    E. Implementation Details
bin(s) with the highest confidence. The approach direction
                                                                     We use the Adam optimizer with an initial learning
a ∈ R3 and the baseline direction b ∈ R3 are orthonormal by
                                                                  rate of 0.001 and a step-wise decay to 0.0001. Our set
definition. We inject this property into training by coupling
                                                                  abstraction layers have 3 parallel branches with query ball
the predictions â, b̂ through an in-network Gram Schmidt
                                                                  radii [0.02,0.04,0.08], [0.04,0.08.0.16] and [0.08,0.16,0.32].
orthonormalization
                                                                  For inference the point cloud is centered at its mean in
                                                                  camera coordinates. For training we generate 10000 table
                   z1                   z2 − hb̂, z2 ib̂          top scenes by placing 8-12 grasp annotated ShapeNet models
          b̂ =                   â =                       (6)   [32] at random stable poses. We use rejection sampling to
                 ||z1 ||                    ||z2 ||
                                                                  avoid collisions. We train with a batch size of 3 for 144.000
Thus, we perform a projection and only predict â as the          iterations which takes ∼ 40 hours on a single Nvidia V100
component that is orthonormal to b̂. The orthonormalization       GPU. Convergence is significantly faster than on previous
further reduces the dimensionality of our predicted grasp         methods [12, 14, 11] which take up to one week on a single
representation and facilitates the regression of 3D rotations     GPU for training. This also reflects the effectiveness of our
[36].                                                             proposed grasp representation.
                                                                                   }
                                                        Contact GraspNet

                                                                                         Grasp Contact
                                                                                            Filtering

                                                    optional region of interest

                                                 Unknown Object Segmentation

Fig. 4. Full Inference Pipeline: We segment unknown objects from an RGB-D image using [15]. Our Contact-GraspNet processes the full scene point
cloud or a local region of interest around a target object. Predicted 6-DoF grasps are then associated to object segments by filtering their contact points.
On the right we show the predicted 6-DoF grasp distribution and, in bold, the most confident grasp per segment.

                                                                                                         IV. E XPERIMENTAL E VALUATION
                                       Simulator Success-Coverage
                                                                                             We evaluate our method in a grasping study with a Franka
                        1
                                                                                          robot where we pick unknown objects in cluttered scenes. We
                                                                                          also compare different variations of our method and of our
                       0.8                                                                data by executing a large number of predicted grasps in the
                                                                                          FleX physics simulator [37].
        Success Rate

                       0.6
                                                                                          A. Inference
                       0.4                                                                   Our inference pipeline is shown and described in Fig.
                                                                                          4. The Contact-GraspNet can also be applied to raw depth
                                                            Contact GraspNet
                       0.2
                                                            w/o ladd−s
                                                                                          images by itself, but most robotic tasks require some kind
                                                            w/o binned lwidth             of instance detection/segmentation to specify a target.
                        0                                                                    Local regions of interest can be optionally extracted
                             0   0.1      0.2     0.3        0.4       0.5         0.6    around the 3D centroid of point cloud segments in order
                                                Coverage                                  to maximize the number of potential contact points. In our
Fig. 5. Loss Ablations: Without weighted binning in the grasp width                       experiments, we extract cubes with an edge length set to
loss lwidth both, success rate and coverage decrease. The ladd−s loss                     twice the largest spanning dimension, but at least 0.3m and
leads to increased success rates at high confidence contacts (Coverage                    at most 0.6m.
∈ [0, 0.1]) and to slightly decreased success rate in the low-confidence
regime. This confidence calibration is important, since it determines which                  Run time: The Contact-GraspNet has a run time of 0.28s
grasp is eventually executed.                                                             for a full scene or ∼ 0.19s for a local region around a target
                                                                                          object. Compared to other 6-DoF grasp generation methods
                                       Simulator Success-Coverage
                                                                                          this is quite fast and enables applications requiring reactive
                        1                                                                 closed loop grasping.
                                                                                             Grasp Selection: At test time we select grasps by setting
                       0.8                                                                a contact confidence threshold of 0.23 and then use farthest
                                                                                          point sampling on the (filtered) contact points to ensure broad
                       0.6                                                                grasp coverage. If the number of predicted grasps for an
        Success

                                                                                          object is too low, we reduce the confidence threshold to
                       0.4                                 Contact GraspNet               0.19. In the end we execute the most confident grasp that is
                                                           w/ noise σ = 0.001             kinematically reachable and where the robot does not collide
                                                           w/o local regions
                       0.2
                                                           ours trained on [11]
                                                                                          with the scene [38].
                                                            [12] trained on [11]
                        0
                                                                                          B. Evaluation Metrics
                             0   0.1      0.2     0.3        0.4       0.5         0.6       In our robotic experiments we report the number of
                                                Coverage                                  successful grasps and the number of trials. The latter is
Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor-                  often disregarded when picking small objects from a bin.
mance in simulation but helps generalization to noisy sensor data. Predicting             However, grasping in only one or two trials is crucial in
grasps directly on full scenes without extracting local regions yields a similar          cluttered scenes (e.g. in households) with large, densely
average success rate, but significantly lowers grasp coverage. Training on the
small grasp dataset from [11] with 5 categories is not sufficient to generalize           packed objects where collisions should be avoided and stable
to arbitrary objects and shows the importance of ACRONYM [32]                             grasp opportunities can vanish after objects tip over. We
                                                                                                          TABLE I
                                                                              C LUTTERED S CENE G RASPING : W E ACHIEVE A CLEAR IMPROVEMENT
                                                                                    OVER RECENT STATE - OF - THE - ART GRASPING PIPELINES

                                                                                                          Success   First attempt   #Attempts
                                                                                6-DOF GraspNet [11]        62.7           -             -
                                                                                [11] +CollisionNet [12]    80.39       68.63           67
                                                                                  Contact-GraspNet        90.20        84.31           59

Fig. 7. One advantage of our method is that it does not rely on an accurate
segmentation of unknown objects. Here, successful grasp contacts are still
found on the driller despite severe under-segmentation.
                                                                              Weighting also performs better than oversampling in our
                                                                              experiments. The average distance loss ladd−s improves the
                                                                              success rate of high confidence contacts which is important
limit ourselves to a maximum of two grasp trials per object                   because most grasps that we execute lie in the first decimal
without rearrangements and report the success rate after a                    of coverage. The connection of contact confidence with the
single trial as well.                                                         grasp pose results in an overall improved calibration.
   Our simulator experiments allow us to also evaluate the                       Data: In Fig. 6 we examine the effects of different training
diversity of grasps and ablate variations of our method. Here,                and test data. Zooming into local regions allows the network
we evaluate the success rate and coverage of the generated                    to concentrate potential contact points on the object and thus
grasps following [11]. A grasp is considered successful if                    increases coverage. We also show the importance of a large
(1) the open gripper does not collide with the object/scene                   and diverse grasp dataset like ACRONYM [32]. Training on
and (2) the object is still in the gripper after grasping and                 a small grasp datasets with 110 objects from 5 categories
a shaking motion. This is a conservative measure, as most                     [11] is not sufficient for out-of-category generalization irre-
real world grasps can slightly collide and do not undergo a                   spective of the method.
shaking motion. Coverage is the percentage of ground truth                       Failure Cases: We observe some failure cases for thick
grasps (including occluded ones) whose base coordinates are                   objects that only allow grasps almost at maximum grasp
within 2cm of any of the generated grasps.                                    width. Here, grasp predictions are less confident presumably
                                                                              because of the discontinuous decision boundary. Injecting
C. Real robot grasp experiments                                               noise during training reduces this effect. Finally, small ob-
   Setup: Our physical setup consists of a 7-DoF Franka                       jects sometimes have contact points with low confidence
Panda robot with a parallel-jaw gripper. We closely replicate                 possibly because of their small impact on the total loss.
the 9 cluttered scenes defined in [12] with a total of 51
unseen objects. The task is to pick the objects from the
cluttered scene and place them into a bin. We manually select                                        V. C ONCLUSIONS
target objects and grasp them in the same random order as
in [12]. In our experiments, we use the Intel Realsense L515                     We considered the fundamental problem of grasping un-
LiDAR camera mounted on a tripod for both RGB and depth                       known objects in structured clutter with a parallel jaw
data. Robot motions are generated using [38].                                 gripper. We proposed an efficient, accurate and simplifying
   Results: Table I shows our grasp evaluation results on the                 6-DoF grasp generation method called Contact-GraspNet. By
robot. We observe a significantly higher grasp success rate of                transforming the hardly tractable 6-DoF grasp estimation
our method compared to [11] and [12] which themselves out-                    problem into a grasp contact point classification and a
perform other learning-based methods and analytic/heuristic                   grasp rotation estimate, we greatly limit the predicted pose
baselines. Furthermore, our method strongly improves the                      space and facilitate the learning process. Through tailored
grasp success at first trial and thereby reduces the number of                optimization targets that take into account the multi-modality,
re-grasps. We also addressed the shortcomings of cropping                     imbalance and sparsity of the 6-DoF grasp distribution, our
objects from the point cloud using potentially imprecise                      network learns to generate diverse grasps covering the whole
segmentation masks. Fig. 7 shows an imprecise segmentation                    graspable surface in a recorded scene. Gripper collisions
example where cropping would be catastrophic but where our                    are effectively avoided by considering them during training
grasp filtering method can still extract successful grasps.                   and by predicting grasps directly in scenes. Our approach
                                                                              can incorporate segmentation predictions as well but is not
D. Ablations                                                                  dependent on accurate masks itself. It is also complementary
   Optimization Targets: In Fig. 5 we first investigate the                   to grasp ranking methods that use gripper and/or robot
effect of our loss targets. The weighted loss on the grasp                    models as input. Grasping successfully with a single attempt
width bins lwidth is crucial to deal with the imbalanced                      is crucial in sensible environments. Our method showed
widths in our grasp dataset. Without weighting the bins,                      strong advances in that regard and is a step towards reaching
the predictions mostly collapse into narrow grasp widths.                     the required grasp reliability.
                             R EFERENCES                                             tional Conference on Intelligent Robots and Systems (IROS). IEEE,
                                                                                     2018, pp. 4238–4245.
 [1] X. Deng, A. Mousavian, Y. Xiang, F. Xia, T. Bretl, and D. Fox,             [24] X. Yan, M. Khansari, J. Hsu, Y. Gong, Y. Bai, S. Pirk, and H. Lee,
     “Poserbpf: A rao-blackwellized particle filter for 6d object pose               “Data-efficient learning for sim-to-real robotic grasping using deep
     tracking,” in Robotics: Science and Systems (RSS), 2019.                        point cloud prediction networks,” 2019.
 [2] M. Sundermeyer, Z.-C. Marton, M. Durner, and R. Triebel, “Aug-             [25] X. Yan, J. Hsu, M. Khansari, Y. Bai, A. Pathak, A. Gupta, J. Davidson,
     mented autoencoders: Implicit 3d orientation learning for 6d object             and H. Lee, “Learning 6-dof grasping interaction via deep geometry-
     detection,” International Journal of Computer Vision, vol. 128, no. 3,          aware 3d representations,” 2018.
     pp. 714–729, 2020.                                                         [26] W. Agnew, C. Xie, A. Walsman, O. Murad, C. Wang, P. Domingos,
 [3] X. Deng, Y. Xiang, A. Mousavian, C. Eppner, T. Bretl, and D. Fox,               and S. Srinivasa, “Amodal 3d reconstruction for robotic manipulation
     “Self-supervised 6d object pose estimation for robot manipulation,” in          via stability and connectivity,” 2020.
     International Conference on Robotics and Automation (ICRA), 2020.          [27] M. Breyer, J. J. Chung, L. Ott, R. Siegwart, and J. Nieto, “Volumetric
 [4] C. Wang, D. Xu, Y. Zhu, R. Martı́n-Martı́n, C. Lu, L. Fei-Fei, and              grasping network: Real-time 6 dof grasp detection in clutter,” 2021.
     S. Savarese, “Densefusion: 6d object pose estimation by iterative dense    [28] D. Fischinger, A. Weiss, and M. Vincze, “Learning grasps
     fusion,” 2019.                                                                  with topographic features,” The International Journal of Robotics
 [5] L. Manuelli, W. Gao, P. Florence, and R. Tedrake, “kpam: Keypoint               Research, vol. 34, no. 9, pp. 1167–1194, 2015. [Online]. Available:
     affordances for category-level robotic manipulation.” International             https://doi.org/10.1177/0278364915577105
     Symposium on Robotics Research (ISRR), 2019.                               [29] H. Liang, X. Ma, S. Li, M. Görner, S. Tang, B. Fang, F. Sun, and
 [6] K. Fang, Y. Zhu, A. Garg, A. Kuryenkov, V. Mehta, L. Fei-Fei,                   J. Zhang, “PointNetGPD: Detecting grasp configurations from point
     and S. Savarese, “Learning task-oriented grasping for tool manipula-            sets,” in IEEE International Conference on Robotics and Automation
     tion from simulated self-supervision,” Robotics: Science and Systems            (ICRA), 2019.
     (RSS), 2018.                                                               [30] Y. Qin, R. Chen, H. Zhu, M. Song, J. Xu, and H. Su, “S4g: Amodal
 [7] J. Mahler, J. Liang, S. Niyaz, M. Laskey, R. Doan, X. Liu, J. A. Ojea,          single-view single-shot se (3) grasp detection in cluttered scenes,” in
     and K. Goldberg, “Dex-net 2.0: Deep learning to plan robust grasps              Conference on robot learning. PMLR, 2020, pp. 53–65.
     with synthetic point clouds and analytic grasp metrics,” RSS, 2017.        [31] P. Ni, W. Zhang, X. Zhu, and Q. Cao, “Pointnet++ grasping: Learning
 [8] J. Mahler, M. Matl, V. Satish, M. Danielczuk, B. DeRose, S. McKinley,           an end-to-end spatial grasp generation algorithm from sparse point
     and K. Goldberg, “Learning ambidextrous robot grasping policies,”               clouds,” arXiv preprint arXiv:2003.09644, 2020.
     Science Robotics, vol. 4, no. 26, p. eaau4984, 2019.                       [32] C. Eppner, A. Mousavian, and F. Dieter, “Acronym: A large-scale
 [9] I. Lenz, H. Lee, and A. Saxena, “Deep learning for detecting robotic            grasp dataset based on simulation,” IEEE International Conference on
     grasps,” IJRR, 2015.                                                            Robotics and Automation (ICRA), 2021.
[10] A. ten Pas, M. Gualtieri, K. Saenko, and R. Platt, “Grasp pose             [33] M. Sundermeyer, Z.-C. Marton, M. Durner, M. Brucker, and
     detection in point clouds,” The International Journal of Robotics               R. Triebel, “Implicit 3D orientation learning for 6D object detection
     Research, vol. 36, no. 13-14, pp. 1455–1473, 2017.                              from RGB images,” in ECCV, 2018.
[11] A. Mousavian, C. Eppner, and D. Fox, “6-dof graspnet: Variational          [34] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “Pointnet++: Deep
     grasp generation for object manipulation,” in Proceedings of the IEEE           hierarchical feature learning on point sets in a metric space,” Neural
     International Conference on Computer Vision, 2019, pp. 2901–2910.               Information Processing Systems (NeurIPS), 2017.
[12] A. Murali, A. Mousavian, C. Eppner, C. Paxton, and D. Fox, “6-dof          [35] A. X. Chang, T. Funkhouser, L. Guibas, P. Hanrahan, Q. Huang,
     grasping for target-driven object manipulation in clutter,” in 2020 IEEE        Z. Li, S. Savarese, M. Savva, S. Song, H. Su, et al.,
     International Conference on Robotics and Automation (ICRA). IEEE,               “Shapenet: An information-rich 3d model repository,” arXiv preprint
     2020, pp. 6232–6238.                                                            arXiv:1512.03012, 2015.
[13] S. Song, A. Zeng, J. Lee, and T. Funkhouser, “Grasping in the wild:        [36] Y. Zhou, C. Barnes, J. Lu, J. Yang, and H. Li, “On the continuity
     Learning 6dof closed-loop grasping from low-cost demonstrations,”               of rotation representations in neural networks,” in Proceedings of the
     Robotics and Automation Letters, 2020.                                          IEEE Conference on Computer Vision and Pattern Recognition, 2019,
[14] H.-S. Fang, C. Wang, M. Gou, and C. Lu, “Graspnet-1billion: A large-            pp. 5745–5753.
     scale benchmark for general object grasping,” in Proceedings of the        [37] M. Macklin, M. Müller, N. Chentanez, and T.-Y. Kim, “Unified particle
     IEEE/CVF Conference on Computer Vision and Pattern Recognition,                 physics for real-time applications,” ACM Transactions on Graphics
     2020, pp. 11 444–11 453.                                                        (TOG), vol. 33, no. 4, pp. 1–12, 2014.
[15] Y. Xiang, C. Xie, A. Mousavian, and D. Fox, “Learning rgb-d feature        [38] M. Danielczuk, A. Mousavian, C. Eppner, and D. Fox, “Object
     embeddings for unseen object instance segmentation,” Conference on              rearrangement using learned implicit collision functions,” in 2021
     Robotic Learning(CORL), 2020.                                                   IEEE International Conference on Robotics and Automation (ICRA),
                                                                                     2021.
[16] C. Xie, Y. Xiang, A. Mousavian, and D. Fox, “The best of both
     modes: Separately leveraging rgb and depth for unseen object instance
     segmentation,” in Conference on Robot Learning (CoRL), 2019.
[17] D. Prattichizzo and J. J. Trinkle, Grasping, 01 2008, pp. 671–700.
[18] A. Bicchi and V. Kumar, “Robotic grasping and contact: a review,” in
     Proceedings 2000 ICRA. Millennium Conference. IEEE International
     Conference on Robotics and Automation. Symposia Proceedings (Cat.
     No.00CH37065), vol. 1, 2000, pp. 348–353 vol.1.
[19] K. Hang, J. A. Stork, and D. Kragic, “Hierarchical fingertip space for
     multi-fingered precision grasping,” in 2014 IEEE/RSJ International
     Conference on Intelligent Robots and Systems, 2014, pp. 1641–1648.
[20] G. Du, K. Wang, S. Lian, and K. Zhao, “Vision-based robotic grasp
     detection from object localization, object pose estimation to grasp
     estimation: A review,” arXiv preprint arXiv:1905.06658, 2019.
[21] S. Levine, P. Pastor, A. Krizhevsky, and D. Quillen, “Learning
     hand-eye coordination for robotic grasping with deep learning and
     large-scale data collection,” International Symposium on Experimental
     Robotics (ISER), 2016.
[22] D. Kalashnikov, A. Irpan, P. Pastor, J. Ibarz, A. Herzog, E. Jang,
     D. Quillen, E. Holly, M. Kalakrishnan, V. Vanhoucke, and S. Levine,
     “Qt-opt: Scalable deep reinforcement learning for vision-based robotic
     manipulation,” Conference on Robot Learning, 2018.
[23] A. Zeng, S. Song, S. Welker, J. Lee, A. Rodriguez, and T. Funkhouser,
     “Learning synergies between pushing and grasping with self-
     supervised deep reinforcement learning,” in 2018 IEEE/RSJ Interna-
