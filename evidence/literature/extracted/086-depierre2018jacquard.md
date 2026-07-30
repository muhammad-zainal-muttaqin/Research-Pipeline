---
source_id: 086
bibtex_key: depierre2018jacquard
title: Jacquard: A Large Scale Dataset for Robotic Grasp Detection
year: 2018
domain_theme: Grasp Robotik
verified_pdf: 86_Jacquard Dataset.pdf
char_count: 43836
---

Jacquard: A Large Scale Dataset for Robotic Grasp Detection
                                                                       Amaury Depierre1,2 , Emmanuel Dellandréa2 and Liming Chen2

                                            Abstract— Grasping skill is a major ability that a wide
                                         number of real-life applications require for robotisation. State-
                                         of-the-art robotic grasping methods perform prediction of
                                         object grasp locations based on deep neural networks. However,
                                         such networks require huge amount of labeled data for training
                                         making this approach often impracticable in robotics. In this
arXiv:1803.11469v2 [cs.RO] 28 Sep 2018

                                         paper, we propose a method to generate a large scale synthetic
                                         dataset with ground truth, which we refer to as the Jacquard
                                         grasping dataset. Jacquard is built on a subset of ShapeNet, a
                                         large CAD models dataset, and contains both RGB-D images
                                         and annotations of successful grasping positions based on
                                         grasp attempts performed in a simulated environment. We
                                         carried out experiments using an off-the-shelf CNN, with three
                                         different evaluation metrics, including real grasping robot
                                         trials. The results show that Jacquard enables much better
                                         generalization skills than a human labeled dataset thanks to
                                         its diversity of objects and grasping positions. For the purpose
                                         of reproducible research in robotics, we are releasing along
                                         with the Jacquard dataset a web interface for researchers to
                                         evaluate the successfulness of their grasping position detections
                                         using our dataset.
                                                              I. INTRODUCTION
                                            Despite being a very simple and intuitive action for a hu-          Fig. 1.     Jacquard dataset contains a large diversity of objects, each
                                         man, grasp planning is quite a hard task for a robotic system.         with multiple labeled grasps on realistic images. Grasps are drawn as 2D
                                                                                                                rectangles on the image, darker sides indicate the position of the jaws.
                                         Detecting potential grasp for a parallel plate gripper from
                                         images involves segmenting the image into objects, under-
                                         standing their shapes and mass distributions and eventually
                                                                                                                accurate, are very time-consuming and therefore cannot be
                                         sending coordinates to the robot’s actuator. As the whole
                                                                                                                easily used to generate very large datasets. The last two,
                                         trajectory of the arm and its end position depend on these
                                                                                                                on the other hand, can be used quite easily to generate
                                         coordinates, precision is critical and an error of one pixel
                                                                                                                millions of labeled data, but generally require to match the
                                         in the prediction can make the difference between success
                                                                                                                CAD model to the position of the object in the image to be
                                         and failure of the grasping. Because of these difficulties
                                                                                                                efficient.
                                         and despite the progress made recently, performance for this
                                         task is still far from what we could expect for real-case                 In this paper, we present an approach to automatize
                                         applications.                                                          the generation of labeled images for robotic grasping by
                                            State-of-the-art methods to predict a grasping position for         simulating an environment as close as possible of a physical
                                         a parallel plate gripper from visual data rely on deep neural          setup. With this environment, we created the Jacquard dataset
                                         networks trained either to directly predict a grasp [1] or to          containing more than one million unique grasp locations on
                                         evaluate the quality of previously generated candidates and            a large diversity of objects. Fig. 1 shows some examples of
                                         select the best one [2]. These methods rely on supervised              annotated images from Jacquard dataset. We also introduce a
                                         training based on labeled data, which may be obtained                  novel criterion, namely simulated grasp trial (SGT), to judge
                                         through one of the following techniques: human labeling,               the goodness of a grasp location prediction based on physic
                                         physical trials with robots [3] [4], analytic computation              grasp simulation. This criterion comes in contrast to the
                                         where a model is used to predict the effect of external forces         distance-based metrics traditionally used for the evaluation of
                                         applied on the model [5] and physics simulation for which              grasp prediction and sticks with the fact that a single object
                                         the grasp is performed in a computer simulation of the real            can depict a large number of grasping positions, including
                                         world [6]. The first two methods, despite being the most               those which are not necessarily previously annotated. Using
                                                                                                                three different evaluation metrics, including SGT and assess-
                                           1 Siléane, Saint-Etienne, France a.depierre@sileane.com
                                                                                                                ment through a real grasping robot trials, we show that this
                                           2 University of Lyon, Ecole         Centrale   de   Lyon,   LIRIS,   novel dataset, despite being synthetic, can be used to train
                                         CNRS      UMR    5205, France        {emmanuel.dellandrea,
                                         liming.chen}@ec-lyon.fr                                                a deep neural network (DNN), for grasp detection from a
                                           Preprint version, accepted at IEEE/RSJ IROS 2018                     simple image of the scene and achieve much better prediction
of grasp locations, in particular for unseen objects, than the
same DNN when it is trained using a grasp dataset with
human labeled data.
   This paper is organized as follows. Section II overviews
the related work. Section III states the modelisation we used
to describe a grasp. Section IV presents the method used
                                                                                              w
to generate Jacquard dataset. Section V discusses the experi-
mental results using the Jacquard dataset in comparison with                                                      θ
the Cornell dataset. Section VI concludes the paper.                                               (x, y)
                  II. RELATED WORK
   Early research in grasp prediction assumed the robot to
have a perfect knowledge of its environment and aimed to
plan grasps based on a 3D model of the object [7] [8]. Using
                                                                               h
this technique, Goldfeder et al. [9] created the Columbia
Grasp Database, containing more than 230k grasps. With this
type of approach, the notion of image is not present, only
the CAD models of the gripper and objects are used. At test
                                                                 Fig. 2. Parametrization of a grasp for a parallel-plate gripper. A grasp
time, a query object is matched with an object within the        is described as a five dimensional vector: two values for the position of
database and a grasp is generated using the similarity of the    the center, two for its size and one for its orientation with respect to the
CAD models. With this approach, both the model and the           horizontal axis. Green sides represent the inner sides of the parallel jaws,
                                                                 yellow sides show the opening of the gripper.
position of the object have to be known at test time, which
is generally not the case for real-world applications.
   Recent development of deep learning [10] and more
                                                                 depth image, but they did not release their data publicly.
particularly of the Convolutional Neural Networks (CNN)
                                                                 In comparison, our Jacquard dataset contains more than
have inspired many researchers to work directly on images
                                                                 11k objects with both RGB and realistic depth information
instead of 3D CAD models. The simultaneous apparition
                                                                 created through stereo-vision.
of cheaper sensors as the Kinect, also helped by providing
                                                                    The dataset most similar to our work is the Cornell Grasp-
additional depth information to the RGB image. This led
                                                                 ing Dataset 1 . It is composed of 885 RGB-D images of 240
to the development of datasets based on physical trials. In
                                                                 different objects with 8019 hand-labeled grasp rectangles.
[11] a method to share the knowledge of different robots
                                                                 As shown in [1], this dataset enables the training of a neural
was developed in order to collect a large collection of data,
                                                                 network to detect grasps in images. However a dataset with
in [3] a Baxter robot has been used to collect 50k data,
                                                                 885 images is quite small compared to the ones traditionally
while in [4] the authors collected over 800k datapoints
                                                                 used in deep learning and may lead to bad performance when
(image, grasp position and outcome) using 14 robotic arms
                                                                 generalizing on different images or object configurations.
running during two months. In the last two cases, a CNN
                                                                 Human labeling can also be biased to grasps that are easily
was successfully trained to detect grasp positions from the
                                                                 performed with a human hand but not necessarily with a
collected data. However, these approaches are either material
                                                                 parallel plate gripper. Comparatively, the proposed Jacquard
or time consuming or and can not be fully automatized:
                                                                 dataset is more than 50 times bigger with various objects
human intervention is still needed to position the objects in
                                                                 and grasps sizes and shapes. A summary of the properties of
front of the robot. Moreover, these methods only generate
                                                                 public grasp datasets can be found in Table I.
one single grasp annotation whereas there are generally
several positions which could be good for robotic grasping.                 III. MODELLING ROBOTIC GRASP
   To overcome the issue of time-consuming data generation,
Mahler et al. [2] created Dexnet-2.0, a synthetic dataset with      In this work, we are interested in finding a good grasp
6.7 millions depth images annotated with the success of the      from a RGB-D image of a single object laying on a plane.
grasp performed at the center of the image. They trained         A grasp is considered good when the object is successfully
a Grasp Quality CNN with these data and achieved a 93%           lifted and moved away from the table by a robot with a
success rate when predicting the outcome of a grasp. The         parallel-plate gripper. As shown in Fig. 2, a grasp can be
GQ-CNN has good performance, but it can not be trained           described as:
end-to-end to predict grasp positions: it only takes grasp                             g = {x, y, h, w, θ}               (1)
candidates generated by another method as an input and rank
                                                                   where (x, y) is the center of a rectangle, (h, w) its size
them.
                                                                 and θ its orientation relative to the horizontal axis of the
   In [12], Johns et al. used a similar approach: they sim-
                                                                 image. This representation differs from the one of seven
ulated grasp attempts on 1000 objects and trained a neural
network to predict a score over a predefined grid of pos-          1 http://pr.cs.cornell.edu/grasping/rect_data/
sible positions for the gripper. The network’s input was a       data.php
                                                               TABLE I
                                   S UMMARY OF THE PROPERTIES OF PUBLICLY AVAILABLE GRASP DATASETS

                       Number of              Number of    Multiple gripper   Multiple grasps    Grasp     Number of   Automatized
       Dataset                     Modality
                        objects                images           sizes           per image       location    grasps      generation
   Levine et al. [4]       -        RGB-D       800k             No                 No            Yes        800k          No
   Mahler et al. [2]     1500       Depth       6.7M             No                 No             No        6.7M          Yes
   Cornell                240       RGB-D       1035             Yes                Yes           Yes        8019          No
   Jacquard (ours)        11k       RGB-D        54k             Yes                Yes           Yes        1.1M          Yes

dimensions described in [13] but Lenz et al. show in [14]            projected pattern and applied an off-the-shelf stereo-vision
that it works well in practice. The main advantage of this           algorithm [19] on them, giving a noisy depth. This approach
representation is that the grasp can be simply expressed             has been shown to produce depth images very close to real
in the image coordinates’ system, without any information            ones in [20]. A binary mask separating the object and the
about the physical scene: z position of the parallel plates          background is also created.
and approach vector are determined from the depth image.
When the grasp is performed by a real robot, h and w are             C. Annotation generation
respectively fixed and bounded by the shape of the gripper.             To generate grasp annotations, we used the real-time
                                                                     physics library pyBullet. As for the rendering module, the ob-
                  IV. JACQUARD DATASET
                                                                     ject model is loaded into the pyBullet environment, however,
   To solve the problem of data starvation, we designed a new        to speed up calculations, collisions are not computed directly
method to get images and ground truth labels from CAD                on the mesh but on a volumetric hierarchical approximate
models through simulation. Then we applied this process              convex decomposition [21] of it. Different grippers with
to a subset of ShapeNet [15], namely ShapeNetSem [16],               parallel-jaws are simulated. They all have a max opening
resulting in a new dataset with more than 50k images of              of 10 cm and a jaw size in {1, 2, 3, 4, 6} cm. The different
11k objects and 1 million unique successful grasp positions          jaw sizes for the gripper combined with the varied scales of
annotated. These data are made available to the research             objects ensure that our simulated gripper can perform grasps
community 2 . The main pipeline we used for data generation          in a wide range of different configurations.
is illustrated on Fig. 3. Physics simulation were performed             Grasp annotations are generated in three steps. First, we
using pyBullet library [17] and Blender [18] was used to             generate thousands of random grasp candidates covering the
render the images through its Cycles Renderer.                       whole area under the camera. Then, all these grasp candidates
A. Scene creation                                                    are tested through rigid body simulation using a gripper with
                                                                     a jaw size of 2 cm. And finally all the successful positions of
   Scenes are all created in the same way. A plane with a
                                                                     the previous step are tested again with all the gripper sizes.
white texture is created, the texture being randomly rotated
                                                                     The result is a set of successful grasp locations, each having
and translated to avoid constant background. Then we select
                                                                     between 1 and 5 jaw sizes.
an object from a pool of CAD models. As the objects in
                                                                        To perform simulated grasps, the approach vector is set to
ShapeNet have a wide range of scales, we rescale the model
                                                                     the normal at the center of the grasp and the orientation
so the longest side of its bounding box has a length between
                                                                     and opening of the gripper are defined by the rectangle
8 and 90 cm. We also give the object a mass depending on
                                                                     coordinates as described in section III. A grasp is considered
its size (80 g for a 8 cm object and 900 g for a 90 cm one)
                                                                     successful if the object is correctly lifted, moved away and
before dropping it from a random position and orientation
                                                                     dropped at a given location by the simulated robot. Once
above the plane. Once the object is in a stable position, the
                                                                     all the random candidates have been tested, a last pass is
scene configuration is saved.
                                                                     performed on good grasps to remove the ones which are too
   This scene description is sent to two independent modules:
                                                                     close from each other. This last step is necessary to ensure
one to render the images and one with a physics simulator
                                                                     that all the grasps are annotated only once.
to generate the grasp annotations. For the Jacquard dataset,
                                                                        As the number of possible grasps for one image is very
we created up to five scenes for each object. This number
                                                                     large, we used a non-uniform probability distribution: can-
was chosen in order to have different views of the objects,
                                                                     didates are generated more frequently in the most promising
but can be increased without any change in the process if
                                                                     areas. Theoretically, candidates could be generated with a
necessary.
                                                                     uniform distribution, but in this case many grasps would
B. Image rendering                                                   fall in an empty area without the object. For the Jacquard
  RGB and true depth images are rendered with Blender.               dataset, we used a simple heuristic looking for aligned
To stick as close as possible to real scene images, instead          edges in the image and generating the probability distribution
of adding Gaussian noise to the perfect depth image as in            from the density of such edges. However, our experiments
[12], we rendered two more RGB synthetic images with a               showed us that any reasonable heuristic lead to a similar
                                                                     final grasps distribution in the image, at the cost of more
 2 http://jacquard.liris.cnrs.fr                                     random trials. With this method, we can reduce the number
                          Random grasps

                                                                               Grasps simulation                                 Successful grasps

                          Scene creation
                                                            RGB            True            Stereo           Object
                                                           image           depth           depth            mask
3D Models database                                                                 Rendering

Fig. 3. The pipeline we used to generate annotated images from 3D models. Random grasps are generated from a probability map obtained with a simple
heuristic algorithm before being tested in the simulation environment. In the rendering part, a synthetic camera renders the different images.

of grasp attempts necessary to annotate a scene by orders
of magnitudes, while keeping a diversity in grasp locations.
Such a diversity is very important for deep learning oriented
methods.
D. Assessment criterion of successful grasp predictions
   With the Cornell Grasp Dataset, the criterion used to
determine whether a grasp prediction is correct or not is
a rectangle-based metrics. With this criterion, a grasp is
considered to be correct if both:
   • The angle between the prediction and the ground-truth
      grasp is smaller than a threshold (a typical value is 30◦ )
   • The intersection over union ratio between the prediction
      and the ground-truth grasp is over a threshold (typically            Fig. 4. Example of misclassifications with the rectangle metrics. Prediction
      25%)                                                                 is in yellow and green, ground truth is in red and purple. Top row shows
                                                                           false positives, bottom row shows false negatives.
   This criterion can however produce a lot of “visually”
false-positives, i.e., grasps that, from our human expertise,
look bad, but that the rectangle metrics predict as good,                  interface allowing researchers to send grasp requests on our
as well as false-negatives, i.e., grasps that, from our human              simulator and receive the corresponding grasp outcome.
expertise, look good, but that the rectangle metrics predict
bad. Fig. 4 shows some examples of such misclassifications.                            V. EXPERIMENTS AND RESULTS
   With the Jacquard dataset, we propose a new criterion                     In order to evaluate the effectiveness of the proposed
based on simulation, subsequently called simulated grasp                   simulated Jacquard grasp dataset, we carried out two series
trial-based criterion (SGT). Specifically, when a new grasp                of experiments: 1) cross-dataset grasp prediction with the
should be evaluated as successful or not, the corresponding                Cornell and Jacquard datasets (section V-B); 2) evaluation
scene is rebuilt in the simulation environment and the grasp               of grasp predictions using a real grasping robot (section V-
is performed by the simulated robot, in the exact same                     C). We start by explaining the training setup.
conditions as during the generation of the annotations. If
the outcome of the simulated grasp is a success, i.e., the                 A. Training setup
object is successfully lifted and moved away by the simulated                 In all our experiments, we used an off-the-shelf CNN,
robot using the predicted grasp location, the prediction is                i.e., AlexNet[22]. The network’s convolution weights have
then considered as a good grasp. This novel SGT criterion                  been pre-trained on ImageNet [23] while the fully connected
is much closer than the rectangle metrics to real-world                    layers are trained from scratch. To use AlexNet with RGB-D,
situations where a single object can have many successful                  we simply normalize the depth image to get values close to
grasp locations, including successful grasp locations which                color channels and duplicate the blue filters in the first pre-
are not previously annotated. For the purpose of reproducible              trained convolution layers. The network is trained through
research, we are releasing along with the dataset a web                    Stochastic Gradient Descent algorithm for 100k iterations
                       TABLE II
  ACCURACY OF THE NETWORK TRAINED ON DIFFERENT DATASETS

                          Rectangle Metrics          SGT
 Training Dataset
                        Cornell       Jacquard     Jacquard
      Cornell       86.88% ± 2.57 54.28% ± 1.22 42.76% ± 0.91
  Jacquard (ours)   81.92% ± 1.95 74.21% ± 0.71 72.42% ± 0.80

with a learning rate of 0.0005, a momentum of 0.9 and a
weight decay of 0.001. The learning rate is set to 0.00005
after the first 75k iterations. To compute the error of the
network, the Euclidean distance between the prediction and
the closest annotation is used:
                                        2
                       L = min kg − ĝk                    (2)
                            g∈G

   Where G is the set of all the annotations for the image
and ĝ is the network prediction.
   Before training, we perform data augmentation by translat-
ing, rotating and mirroring the images. For synthetic data, we   Fig. 5. Our physical setup to test grasp predictions. The camera is located
also use the object’s mask to replace the default background     above the grasping area.
with different textures (cardboard, paper, wood, grass ...) to
generate more variabilities.
                                                                 which records a performance decrease of 20 points in
B. Cross-dataset evaluation                                      comparison with its baseline performance. As for the other
   This series of experiments aims to show that: 1) our          training, part of this gap could be explained by the misclassi-
Jacquard grasp dataset, despite being synthetic, can be used     fications of the rectangle metrics. However, this performance
to train DNNs to predict grasp locations on real images;         decrease is confirmed by our criterion based on simulated
2) The diversity of objects and grasp locations is important     grasp trials (SGT): Alexnet trained on Cornell only displays
for a trained CNN to generalize on unseen objects. For this      a grasp prediction accuracy of 42.76% which is 30 points
purpose, the Cornell dataset with its 885 RGB-D images on        behind the 72.42% accuracy of the same CNN trained on
240 objects and 8019 hand labeled grasp locations is used        Jacquard.
along with a portion of Jacquard which contains 15k RGB-            All these figures thus suggest that Jacquard can be used
D images on a selected 3k objects and 316k different grasp       to train CNN, for an effective prediction of grasp locations.
positions. To highlight 1), Alexnet is trained on Jacquard       Furthermore, thanks to the diversity of objects and grasp
and tested on Cornell; for 2) it is trained on Cornell and       locations, Jacquard enables a much better generalization
tested on Jacquard. For comparison, we also display a            skills of the trained CNN.
baseline performance with Alexnet trained and tested on the
same dataset, i.e., Cornell or Jacquard. For this purpose,       C. Evaluation of grasp predictions using a real grasping
we performed training and testing of the network with 5-         robot
fold cross validation for Cornell or Jacquard, leading to           How good is a grasp predicted by a trained deep neural
5 variants of Alexnet with slightly different accuracies on      network, in real? To answer this question of possible reality
each dataset. Each variant trained on Cornell (Jacquard,         gap, we used a parallel plate gripper mounted on a Fanuc’s
respectively) is then tested on the whole Jacquard dataset       M-20iA robotic arm and a set of various objects. To ensure
(Cornell, respectively) to evidence 1).                          a wide variability in shapes, materials and scales, we used
   Table II summarizes the experimental results evaluated        15 everyday objects (toys and furnitures) and 13 industrial
by both rectangle metrics and SGT criterion. As can be           components. Fig. 5 shows the robot performing a predicted
seen from Table II, when Alexnet is trained on our simu-         grasp on one of the testing objects. Our criterion of a
lated Jacquard dataset and tested on Cornell, it achieves a      successful grasp was the same as in the simulator but this
grasp prediction accuracy of 81.92% which is quite close         time using the aforementioned real grasping robot instead
to the baseline performance of 86.88%. Furthermore, we           of the simulated one: the grasp of an object is considered
also noticed that the networks trained on synthetic data         successful only if the object is lifted, moved away and
tended to predict grasps which were visually correct despite     correctly dropped. For this test, we compared Alexnet trained
being classified as wrong by the rectangle metrics. Typical      on the Cornell dataset and the same network trained on a
examples are shown on the bottom line of Fig. 4.                 subset of 2k objects from the Jacquard dataset.
   In contrast, when Alexnet is trained on Cornell and tested       The experimental results show that the grasp predictor
on Jacquard with a much wider diversity of objects and           with Alexnet trained on the Jacquard dataset displays a grasp
grasps, it depicts a grasp prediction accuracy of 54.28%         successful rate of 78.43% which is even 6 points higher than
                                                                                 [2] J. Mahler, J. Liang, S. Niyaz, M. Laskey, R. Doan, X. Liu, J. A. Ojea,
                                                                                     and K. Goldberg, “Dex-net 2.0: Deep learning to plan robust grasps
                                                                                     with synthetic point clouds and analytic grasp metrics,” arXiv preprint
                                                                                     arXiv:1703.09312, 2017.
                                                                                 [3] L. Pinto and A. Gupta, “Supersizing self-supervision: Learning to
                                                                                     grasp from 50k tries and 700 robot hours,” in Robotics and Automation
                                                                                     (ICRA), 2016 IEEE International Conference on. IEEE, 2016, pp.
                                                                                     3406–3413.
                                                                                 [4] S. Levine, P. Pastor, A. Krizhevsky, J. Ibarz, and D. Quillen, “Learning
                                                                                     hand-eye coordination for robotic grasping with deep learning and
                                                                                     large-scale data collection,” The International Journal of Robotics
                                                                                     Research, 2016.
                                                                                 [5] A. Rodriguez, M. T. Mason, and S. Ferry, “From caging to grasping,”
                                                                                     The International Journal of Robotics Research, vol. 31, no. 7, pp.
                                                                                     886–900, 2012.
                                                                                 [6] A. T. Miller and P. K. Allen, “Graspit! a versatile simulator for robotic
                                                                                     grasping,” IEEE Robotics & Automation Magazine, vol. 11, no. 4, pp.
                                                                                     110–122, 2004.
Fig. 6. Samples of grasp predictions on our real setup for the network           [7] A. T. Miller, S. Knoop, H. I. Christensen, and P. K. Allen, “Automatic
trained on the Cornell dataset (top row) and the one trained on our synthetic        grasp planning using shape primitives,” in Robotics and Automa-
Jacquard data (bottom row).                                                          tion, 2003. Proceedings. ICRA’03. IEEE International Conference on,
                                                                                     vol. 2. IEEE, 2003, pp. 1824–1829.
                                                                                 [8] J. Bohg and D. Kragic, “Learning grasping points with shape context,”
the grasp accuracy displayed by Alexnet when it was trained                          Robotics and Autonomous Systems, vol. 58, no. 4, pp. 362–377, 2010.
                                                                                 [9] C. Goldfeder, M. Ciocarlie, H. Dang, and P. K. Allen, “The columbia
and tested on the subset of 3k objects of Jacquard (see Table                        grasp database,” in Robotics and Automation, 2009. ICRA’09. IEEE
II) using the SGT criterion. This generalization skill of the                        International Conference on. IEEE, 2009, pp. 1710–1716.
trained grasp predictor can be explained by the large diversity                 [10] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol.
                                                                                     521, no. 7553, pp. 436–444, 2015.
of objects and grasp locations in the Jacquard dataset. For                     [11] J. Oberlin, M. Meier, T. Kraska, and S. Tellex, “Acquiring Object
most of the failed cases, the grasp was not stable enough: the                       Experiences at Scale,” in AAAI-RSS Special Workshop on the 50th
rectangle in the image was visually coherent and the object                          Anniversary of Shakey: The Role of AI to Harmonize Robots and
                                                                                     Humans, 2015, blue Sky Award.
was successfully lifted but dropped during the movement of                      [12] E. Johns, S. Leutenegger, and A. J. Davison, “Deep learning a grasp
the robot.                                                                           function for grasping under gripper pose uncertainty,” in Intelligent
   Now with the the same network trained on Cornell, the                             Robots and Systems (IROS), 2016 IEEE/RSJ International Conference
                                                                                     on. IEEE, 2016, pp. 4461–4468.
robot succeeded only 60.46% of the predicted grasps, mostly                     [13] Y. Jiang, S. Moseson, and A. Saxena, “Efficient grasping from rgbd
due to bad rectangle localization in the image. Fig. 6 shows                         images: Learning using a new rectangle representation,” in Robotics
some examples of the objects for which the network trained                           and Automation (ICRA), 2011 IEEE International Conference on.
                                                                                     IEEE, 2011, pp. 3304–3311.
on Cornell failed to predict a good grasp while the one                         [14] I. Lenz, H. Lee, and A. Saxena, “Deep learning for detecting robotic
trained on Jacquard succeeded.                                                       grasps,” The International Journal of Robotics Research, vol. 34, no.
                                                                                     4-5, pp. 705–724, 2015.
                   VI. CONCLUSIONS                                              [15] A. X. Chang, T. Funkhouser, L. Guibas, P. Hanrahan, Q. Huang, Z. Li,
                                                                                     S. Savarese, M. Savva, S. Song, H. Su, J. Xiao, L. Yi, and F. Yu,
   In this work, we presented a method to generate realistic                         “ShapeNet: An Information-Rich 3D Model Repository,” Stanford
RGB-D data with localized grasp annotations from sim-                                University — Princeton University — Toyota Technological Institute
ulation. Using this method, we built a large scale grasp                             at Chicago, Tech. Rep. arXiv:1512.03012 [cs.GR], 2015.
                                                                                [16] M. Savva, A. X. Chang, and P. Hanrahan, “Semantically-Enriched 3D
dataset with simulated data, namely Jacquard, and we suc-                            Models for Common-sense Knowledge,” CVPR 2015 Workshop on
cessfully used it to train a deep neural network to predict                          Functionality, Physics, Intentionality and Causality, 2015.
grasp positions in images. The grasp predictor trained using                    [17] E. Coumans and Y. Bai, “pybullet, a python module for physics simu-
                                                                                     lation for games, robotics and machine learning,” http://pybullet.org/,
Jacquard shows a much better generalization skill than the                           2016–2017.
same network when trained with a small hand labeled grasp                       [18] Blender Online Community, Blender - a 3D modelling and rendering
dataset. Our future work will focus on the quality assessment                        package, Blender Foundation, Blender Institute, Amsterdam, 2016.
                                                                                     [Online]. Available: http://www.blender.org
of grasp predictions and on extending this method to more                       [19] H. Hirschmuller, “Stereo processing by semiglobal matching and
complexe scenes, for example with multiple objects.                                  mutual information,” IEEE Transactions on pattern analysis and
                                                                                     machine intelligence, vol. 30, no. 2, pp. 328–341, 2008.
                 ACKNOWLEDGMENT                                                 [20] R. Brégier, F. Devernay, L. Leyrit, and J. L. Crowley, “Symmetry
   This work was in part supported by the EU FEDER,                                  aware evaluation of 3d object detection and pose estimation in scenes
                                                                                     of many parts in bulk,” in Proceedings of the IEEE International
Saint-Etienne Métropole and Région Auvergne-Rhône-Alpes                           Conference on Computer Vision, 2017, pp. 2209–2218.
fundings through the FUI PIKAFLEX project and in part by                        [21] K. Mamou, “Volumetric hierarchical approximate convex decomposi-
the French National Research Agency, l’Agence Nationale de                           tion,” in Game Engine Gems 3, E. Lengyel, Ed. A K Peters, 2016,
                                                                                     pp. 141–158.
Recherche (ANR), through the ARES labcom project under                          [22] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification
grant ANR 16-LCV2-0012-01.                                                           with deep convolutional neural networks,” in Advances in neural
                                                                                     information processing systems, 2012, pp. 1097–1105.
                             R EFERENCES                                        [23] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei,
                                                                                     “ImageNet: A Large-Scale Hierarchical Image Database,” in CVPR09,
 [1] J. Redmon and A. Angelova, “Real-time grasp detection using convo-              2009.
     lutional neural networks,” in Robotics and Automation (ICRA), 2015
     IEEE International Conference on. IEEE, 2015, pp. 1316–1322.
