---
source_id: 127
bibtex_key: kang2020strawberry
title: Fruit Detection, Segmentation and 3D Visualisation of Environments in Apple Orchards
year: 2020
domain_theme: Pertanian
verified_pdf: 127_Fruit Detection & 3D Visualisation (Kang & Chen).pdf
char_count: 39002
---

Fruit Detection, Segmentation and 3D Visualisation
                                                 of Environments in Apple Orchards
                                                               Hanwen Kang and Chao Chen∗
arXiv:1911.12889v1 [cs.CV] 28 Nov 2019

                                                                             Abstract
                                                  Robotic harvesting of fruits in orchards is a challenging task, since
                                              high density and overlapping of fruits and branches can heavily impact
                                              the success rate of robotic harvesting. Therefore, the vision system is
                                              demanded to provide comprehensive information of the working envi-
                                              ronment to guide the manipulator and gripping system to successful
                                              detach the target fruits. In this study, a deep learning based one-stage
                                              detector DaSNet-V2 is developed to perform the multi-task vision sens-
                                              ing in the working environment of apple orchards. DaSNet-V2 com-
                                              bines the detection and instance segmentation of fruits and semantic
                                              segmentation of branch into a single network architecture. Meanwhile,
                                              a light-weight backbone network LW-net is utilised in the DaSNet-V2
                                              model to improve the computational efficiency of the model. In the
                                              experiment, DaSNet-V2 is tested and evaluated on the RGB-D images
                                              of the orchard. From the experiment results, DaSNet-V2 with light-
                                              weight backbone achieves 0.844, 0.858, and 0.795 on the F1 score of
                                              the detection, and mean intersection of union on the instance segmen-
                                              tation of fruits and semantic segmentation of branches, respectively.
                                              To provide a direct-viewing of the working environment in orchards,
                                              the obtained sensing results are illustrated by 3D visualisation . The
                                              robustness and efficiency of the DaSNet-V2 in detection and segmenta-
                                              tion are validated by the experiments in the real-environment of apple
                                              orchard.

                                              Keywords: fruit detection; fruit segmentation; branch seg-
                                              mentation; deep learning; robotic harvesting.

                                         1    Introduction
                                         Nowadays, with the increasing cost and difficulty in availability of the labour
                                         resource (ABARES, 2018), agriculture industry requires transformation from
                                         the labour-intensive industry to the technology-intensive industry. Robotic
                                         technology has shown a promising prospect in terms of improving the ef-
                                         ficiency and yield of agriculture production. Different from the traditional
                                         autonomous equipment which has been widely applied in the harvesting of
                                         commercial crops such as wheat and soybean, to design a robotic system

                                                                                 1
for automatic harvesting of fruits is a more challenge task (Vasconez et al.,
2019). The vision system is the key to the harvesting since it senses the
working environment and guides the manipulator to detach fruits. Moreover,
due to the complex conditions in fruit orchards, such as ’free growth’ and
densely arranged branches and fruits, fruit harvesting robots are required to
understand the working environment to increase the rate of success during
the operation (Zhao et al., 2016). Meanwhile, other environmental factors,
including illumination variance and occlusion, can also heavily affect the
performance of the vision system.
    This work developed a multi-function Deep Convolution Neural Network
DaSNet-V2 to perform the vision sensing of working environment in apple
orchards. DaSNet-V2 adopts one-stage detector architecture to perform the
detection and instance segmentation of fruits. Meanwhile, a semantic seg-
mentation branch is grafted to the network to segment branches in orchards.
To ensure the computational availability of the network model on the em-
bedded computing devices, a light-weight backbone based on the residual
network is developed and utilised in the DaSNet-V2. DaSNet-v2 is evaluated
in the data which is collected from apple orchards, 3D visualisation of pro-
cessed orchard environments by means of the DaSNet-v2 is also illustrated
in the experiments.
    The rest of paper is organised as follow. Section 2 reviews the related
works. Sections 3 and 4 introduce the methodology and experiment of the
work, respectively. In section 5, the conclusions and future work are pre-
sented.

2    Literature Review
Vision sensing in fruit orchards has been extensively studied in previous
studies. There are currently two classes of approaches: traditional machine
learning based algorithm and deep learning based algorithms. Traditional
machine learning based algorithms use image features extracted from the
2D image space or 3D geometry space and machine learning based classifier
to classify, detect, and segment the elements in the images (Kapach et al.,
2012). A number of work of applying traditional machine learning based al-
gorithm on vision sensing in agriculture environment. Nguyen et al. (2016)
applied descriptor of colour and geometry features to describe the appear-
ance of red apples, and a clustering algorithm based on Euclidean distance
in feature space to segment and detect the fruits in the images. The similar
processing techniques of performing segmentation and detection in vision
sensing in orchard environment are also presented in the works of (Zhou
et al., 2012, McCool et al., 2016, Lin et al., 2019a, Liu et al., 2018). Wang
and Xu (2018) applied multiple image features and Latent Dirichlet Al-
location (LDA) model to perform unsupervised segmentation of the plant

                                     2
and fruits in the greenhouse environment, showing that traditional machine
learning based algorithm can be used in generating labelling data for deep
learning based algorithms. More approaches which applied traditional ma-
chine learning based algorithm to perform vision sensing in orchards can
also be found in the reviews of (Vibhute and Bodhe, 2012) and (Zhao et al.,
2016).
     Deep learning based algorithm is developed more recently. Compared
to the traditional machine learning based algorithm, deep learning based
algorithm achieved superior accuracy and generalisation ability in classi-
fication, detection, and segmentation (Han et al., 2018). Deep learning
based detection algorithm can be classified into two class: two-stage detec-
tor and one-stage detector (Lin et al., 2017). The representative work of the
two-stage detector is Region Convolution Neural Network (RCNN), which
include Fast/Faster-RCNN (Girshick, 2015, Ren et al., 2015) and Mask-
RCNN (He et al., 2017). Faster-RCNN applies Region Proposal Network
(RPN) and Region of Interest (RoI) pooling to combine the RoI search-
ing and classification into a single network architecture, which increases the
computational efficiency of the model. Mask-RCNN further combines mask
segmentation branch into the model, which allows the network to segment
the corresponding area for each object within the images. The representa-
tive work of the one-stage detector is YOLO (Redmon and Farhadi, 2018).
Different from RCNN predict the possible RoI from feature maps, YOLO
predicts the object on each grid of feature maps. Compared to the RCNN,
YOLO achieves equally performance with much improved computational ef-
ficiency. Also, Single Pixel Reconstruction Network (SPRNet) (Yao et al.,
2019), which combines the instance segmentation branch into the architec-
ture of the one-stage detector, achieving the same function compared to the
Mask-RCNN. The work of (Sa et al., 2016) and (Bargoti and Underwood,
2017) applied Faster-RCNN in the detection of fruits, accurate detection
performance was reported from both works. Yu et al. (2019) applied Mask-
RCNN for strawberry harvesting robot in a non-structured environment.
Tian et al. (2019) and Koirala et al. (2019) applied YOLO-V3 in the mon-
itoring of fruit growth in the apple orchard and mango orchard. Kang and
Chen (2019) combined the semantic segmentation and detection into a one-
stage detector, to perform the fruit detection and branch segmentation in
the apple orchard for robotic harvesting. Other deep learning based algo-
rithms such as Fully Convolution Network (FCN) (Long et al., 2015) are also
being studied and applied in performing vision sensing in the agriculture en-
vironments, such as the works of (Lin et al., 2019b) and (Xu et al., 2019).
More works of using deep learning based algorithm in the in-field vision sens-
ing can also be found in the recent review (Kamilaris and Prenafeta-Boldú,
2018).

                                      3
Figure 1: Network architecture of the DaSNet-V2.DaSNet-V2 is comprised
by detection and instance segmentation branch and semantic segmentation
   branch. The detection and instance segmentation branch detect and
 segment the fruits, while the instance segmentation branch segments the
                                 branches.

3     Methodologies and Materials
3.1     Network Architecture
3.1.1    Detection and Instance Segmentation
DaSNet-V2 utilises one-stage detector to perform the detection and instance
segmentation of fruits. In the previous work, two-stage detectors such as
Mask-RCNN utilises the RPN and ROI pooling /align layer to predict and
segment the corresponding area of objects on feature maps to perform the
instance segmentation and detection. Recently, one-stage detector SPRNet
applies ASPP to cover the corresponding area of objects and encode the
multi-scale information to perform the instance segmentation on each grid
of feature maps. DaSNet-V2 adopts the principle of the SPRNet, applying a
mask branch on the output branch of each level of the gated-Feature Pyra-
mid Network (FPN), to perform the instance segmentation and detection of
fruits.
    The architecture of the DaSNet-V2 is shown in Figure 1. DaSNet-V2
utilises a 3-level gated-FPN structure to fuse the information from the dif-
ferent level of feature maps. The architecture of the gated-FPN is shown
in Figure 3. For feature maps from the different level, gated-FPN utilise
a channel-wise multiplication layer with tanh activation to choose and re-
adjust feature maps which are passed into the gated-FPN. Gated-FPN ap-
plied in the DaSNet-V2 receives feature maps from the C3, C4 and C5 level
of the backbone and the fusion of feature maps between different level of
gated-FPN is performed by using adding operation.

                                     4
  Figure 2: Design of the output branch of the DaSNet-V2. The output
    branch of the DaSNet-V2 comprises three subnets for object mask
 segmentation, object boundary box regression, and objects classification.

    On each level of the gated-FPN in the DaSNet-V2, an Atrous Spatial
Pyramid Pooling (ASPP) is utilised to encode the multi-scale information
of objects on feature maps into the output tensor. The applied ASPP utilise
three dilation convolution kernels with dilation rate equal to 1, 2 and 4 and
a 1 × 1 convolution kernel to cover the corresponding area of objects within
feature maps. The output tensor of each ASPP is used to predict the class,
boundary box, and mask of the objects, which is shown in Figure 2. The
mask of objects is reconstructed by up-sampling of the feature tensor on
each grid of feature maps, from the size of 1 × 1 × N (N is the channel
number of the corresponding feature map) to the size of 32 × 32 × 2. The
reconstructed object masks will be rescaled to the boundary box size based
on the prediction of the DaSNet-V2. Each level of gated-FPN in the DaSNet-
V2 has two preset anchor boxes, as experiment results show that six preset
anchor boxes can properly predict and cover the range of possible shape of
fruits in orchards.

3.1.2   Semantic Segmentation
The detection branch of the DaSNet-V2 detects and segments the fruits
within images to locate and track the targets. However, such information is
limited to guide the manipulator to perform a successful detachment of the
target fruit, as there are many other factors presented within the working
environment, such as densely arranged branches. Such factors lead to the
failure of the detachment operation and even damage the gripper and ma-
nipulator system. To provide more information about the working scene, a
semantic segmentation branch is developed and utilised in the DaSNet-V2
to perform the segmentation of branches.
    In the DaSNet-V1, three different architecture designs of semantic seg-

                                     5
Figure 3: (a) Design of the gate layer in the gated-FPN of the DaSNet-V2.
       (b) Design of the ASPP which is utilised in the DaSNet-V2.

Figure 4: (a),(b), and (c) of figure (i) and (ii) are the RGB images, depth
            images, and cloud point in 3D space, respectively.

mentation branch were developed and evaluated. The architecture of the
semantic segmentation branch of the DaSNet-V2 follows the design strat-
egy of the DaSNet-V1, which is shown in Figure 1. Semantic segmentation
branch receives feature maps from the C3, C4, and C5 level of the gated-
FPN of the DaSNet-V2. To keep the consistency of size of feature tensors,
feature maps from C3, C4 are 4 × and 2 × upsampled to match the size
of the feature map from C5, respectively. The fusion between feature maps
is achieved by using the concatenate operation, and three convolution lay-
ers are further applied after concatenating operation to process the feature
information within feature maps. The output tensor of the semantic seg-
mentation branch is 8 × upsampled to match the size of the input image.
Different from the DaSNet-V1, the semantic segmentation branch of the
DaSNet-V2 is designed to segment branches and no longer applied to seg-
ment the fruit, since the segmentation of fruits has been included in the
detection and instance segmentation branch.

                                     6
3.2     3D Visualisation
In the traditional fruit orchards, the arrangement of the trees, branches and
fruits are presented in random and complex behaviours. Such arrangement
of branches and fruits could affect the performance of the harvesting robot
to a large extent. Densely arranged branches may obstruct the path of the
detachment and damage the manipulator and gripper system. Meanwhile,
densely arranged fruits and different types of the stem-branch joint of fruits
may also affect the success rate of fruit detachment. Some fruits can be
easily picked while other fruits are difficult to be detached by the gripper.
To provide more information for guiding the operation of the manipulator
and gripper system, modelling and understanding the working scene from
the 3D aspect is important.
    DaSNet-V2 can detect and segment each fruit and segment branches
within the working scene. For the fruit class, different colours are assigned
to the detected fruits to stand their shape and corresponding area. For
the branch class, a unified colour is assigned to the pixels which have been
classified as the branch. Other classes such as ground, fence and leaves are
presented in black pixel. The segmentation of the leaves is not included in
the DaSNet-V2 since previous in-field experiment results suggest that leaves
only slightly affect the harvesting performance. In this work, PPTK tool-kit
(Heremaps, 2018) is utilised to visualise the 3D point cloud of the working
scene, a sample of 3D visualisation of the orchard environment is shown in
Figure 4.

3.3     Implementation details
3.3.1    Training details
Data augmentation plays an important role in improving the performance
of the trained model in deep learning. Training of the DaSNet-V2 follows
the same strategy in training of the DaSNet-V1, a two-level object scale
amplifier algorithm for minimising the uneven distribution of the object
scale is utilised. Meanwhile, to cover more variance of objects appearance in
fruit and branch class during the training, the ground truth of the instance
segmentation and semantic segmentation are utilised to adjust the HSV,
brightness and contrast of the pixels within the area of objects. Other
augmentation measurements such as flip and rotation are also included in
the training.
    Focal loss is utilised in the training of the detection of the DaSNet-
V2 to balance the uneven distribution of the foreground class objects and
background class objects, the cross-entropy is utilised in the training of the
instance segmentation and semantic segmentation task. Adam-optimizer is
applied in the network training, the learning rate and decay rate are set as
0.01 and 0.9 based on the previous experiment results, respectively.

                                      7
 Figure 5: Architecture of the Lw-net. LW-net is comprised by 8 Resnet
 blocks and 5 down-sampling blocks. The design of the Resnet block and
  down-sampling block can be referred to the previous work (Kang and
                               Chen, 2019).

3.3.2    Implementation details
The programming of the DaSNet-V2 is achieved by using slim tool-kit within
the Tensorflow API-1.11 in Ubuntu 16.04. 3D visualisation of the point
cloud is achieved by using PPTK tool-kit. The DaSNet-V2 is trained on the
Nvidia GTX-1080Ti and be evaluated in the Intel CPU-i5 and Jetson TX2
in Ubuntu 16.04 and Nvidia GTX-1080Ti in Windows 10. Depth camera
Intel RealSense D-435 is utilised in the experiment, and it is controlled by
using ROS-kinetic in Ubuntu 16.04.
    To ensure the computation availability and real-time performance of the
DaSNet-V2 on the embedded computation device such as Jetson-TX2, a
customised light-weight residual network ’LW-net’ which was developed and
evaluated in the DaSNet-V1 is utilised to serve as the backbone of the net-
work. Meanwhile, other classification networks, including Resnet-101 and
Darknet-53 are utilised to serve as the backbone of the network. The im-
plemented code and ImageNet pre-trained weights of the Resnet-101 and
Darknet-53 in Tensorflow were from the Github publicly code library, while
the LW-net is pre-trained with Cifar-10/100 dataset. More details of the
architecture and training of the LW-net is shown in Figure 5.

4     Experiment and Discussion
4.1     Data collection and Evaluation Methods
The RGBD image data were collected from the apple orchard, which is lo-
cated in Qingdao, China. The collection time of the image data was from
10:00 to 16:00 through the day by using the Intel RealSense D-435 depth
camera. The image data was collected at the distance of 0.5-1.5m from
the apple trees, which is the distance from the camera to the fruits in the
harvesting. There are 300 RGB-D images and another 800 RGB images col-

                                     8
lected from the orchard. 500 out of these 1100 images were used to perform
the training and rest of the images were used to perform the evaluation.
    The evaluation of the DaSNet-V2 comprises three tasks, including the
evaluation of the detection performance, instance segmentation quality and
semantic segmentation quality. To evaluate the detection performance of
the DaSNet-V2, F1 score and Intersection of Union (IoU) are applied. F1
combines the performance evaluation of the recall and precision of the
detection; hence it has been widely applied as the evaluation index in many
previous studies of the fruit detection. The expression of the precision,
recall and F1 are presented as follow:
                                     T rueP ositive(T P )
          P recision =                                                     (1)
                         T rueP ositive(T P ) + F alseP ositive(F P )
                                          TP
                   Recall =                                                (2)
                              T P + F alseN egative(F N )
                           2 × P recision × Recall
                       F1 =                                            (3)
                              P recision + Recall
The IoU measures the intersection area of the predicted object boundary
box and the ground truth, to evaluate the location accuracy of the pre-
dicted boundary box of the prediction. On another hand, Mean Intersection
of Union (MIoU) is used to evaluate the performance of the instance seg-
mentation and semantic segmentation of the DaSNet-V2. The definition of
the IoU and MIoU can be referred to the work (Garcia-Garcia et al., 2017).

4.2     Comparison to State of the Art
4.2.1    Evaluation on Detection and Instance Segmentation
This experiment compares the detection performance between the DaSNet-
V2 and the DaSNet-V1, YOLO-V3, YOLO-V3(tiny), Faster-RCNN and the
Mask-RCNN. Meanwhile, the comparison of the performance in instance
segmentation between the DaSNet-V2 and the Mask-RCNN is also included
in the experiment. The evaluation results of the comparison between differ-
ent models are shown in Table as follow.
    YOLO-V3 and Faster-RCNN are the representative works of the one-
stage detector and the two-stage detector, respectively. YOLO-Tiny is the
light-weight version of the YOLO-V3 network. LedNet and DaSNet-V1 are
the previous work of the DaSNet-V2. DaSNet-V1 and LedNet adopt same
architecture design on fruit detection while DaSNet-V1 further applied a se-
mantic segmentation branch in the model to perform the semantic segmenta-
tion of fruits and branches. In the experiment results 1,2 and 3, the detection
performance of the DaSNet-V2 is improved compared to the DaSNet-V1 and
LedNet. Experiment results 3-7 compare the detection performance of the
DaSNet-V2, YOLO and Faster/Mask-RCNN. DaSNet-V2 achieves similar

                                       9
        Table 1: Comparison of performance of detection and instance
               segmentation between different network models

   Index             Model                F1      IoU    MIoU     Time
     1         LedNet (Resnet-101)       0.834   0.872     −     46ms
     2       DaSNet-V1 (Resnet-101)      0.834   0.872     −     72ms
     3       DaSNet-V2 (Resnet-101)      0.856   0.881   0.862    65ms
     4        YOLO-V3 (Darknet-53)       0.797   0.843     −     45ms
     5       YOLO-Tiny (Darknet-18)      0.787   0.836     −     30ms
     6       Faster-RCNN (VGG-16)        0.814   0.863     −     145ms
     7       Mask-RCNN (Resnet-101)      0.835   0.865   0.871   137ms

 Table 2: Comparison of performance of the DaSNet-V2 in detection and
            instance segmentation with different backbones

    Index            Model                F1      IoU    MIoU    Time
      1        DaSNet-V2 (LW-net)        0.844   0.868   0.858   30ms
      2       DaSNet-V2 (Darknet-53)     0.848   0.872   0.863   45ms
      3       DaSNet-V2 (Resnet-101)     0.856   0.881   0.862   65ms

performance on fruit detection compared to the Faster/Mask-RCNN when
same backbone Restnet-101 is applied, and better performance on fruit de-
tection compared to the one-stage detector YOLO-V3 and YOLO-V3(Tiny).
On the performance of the instance segmentation of fruits, DaSNet-V2
achieves a similar score compared to the Mask-RCNN, which are 0.862 and
0.871, respectively.
    From the experiment results, DaSNet-V2 shows a better detection perfor-
mance compared to the One-stage detector YOLO-V3 and YOLO-V3(Tiny).
Compared to the two-stage detector Mask-RCNN, DaSNet-V2 achieves a
better performance on the detection and an equal performance on instance
segmentation. The experiment result shows that ASPP can improve the de-
tection performance of the model and ensure the working of the mask branch.
In terms of the computational efficiency, one-stage detector YOLO and
DaSNet-V2 are faster than the two-stage detector. The computational time
of model to process an image by using YOLO-V3 (Detection), LedNet (De-
tection), DaSNet-V2 (Detection+Instance Segmentation), and Mask-RCNN
(Detection+Instance Segmentation) are 45ms, 46ms, 65ms, and 137ms, re-
spectively.

4.2.2    Evaluation on Semantic Segmentation
This experiment compares the performance of semantic segmentation be-
tween the DaSNet-V2, DaSNet-V1 and the FCN-8s. The evaluation results
of the comparison between different models are shown in Table as follow.

                                    10
      Table 3: Comparison of performance of the DaSNet-V2 in semantic
                   segmentation with different backbones

           Index          Model               MIoUbranch     Time
             1     DaSNet-V1 (Resnet-101)       0.772        72ms
             2     DaSNet-V2 (Resnet-101)       0.802        65ms
             3      FCN-8s (Resnet-101)          733         61ms

 Table 4: Comparison of performance of semantic segmentation between
                       different network models

           Index          Model                MIoUbranch    Time
             1      DaSNet-V2 (LW-net)           0.795       30ms
             2     DaSNet-V2 (Darknet-53)        0.797       45ms
             3     DaSNet-V2 (Resnet-101)        0.802       60ms

    From the experimental results shown in Table 3, the semantic segmenta-
tion performance of the DaSNet-V2 is improved compared to the DaSNet-
V1, which are 0.802 and 0.772, respectively. Compared to the DaSNet-V1,
DaSNet-V2 utilised new architecture design of the ASPP and new aug-
mentation methods, which can improve the generalisation of the network.
Compared to the FCN-8s, the score of semantic segmentation achieved by
DaSNet-V2 is 7% higher, which are 0.733 (FCN-8s) and 0.802 (DaSNet-V2),
respectively. In terms of the computational efficiency, the computational
time of DaSNet-V2 to process an image is slightly less than DaSNet-V1, as
the architecture design of the gated-FPN in DaSNet-V2 is simplified and
optimised compared to the DaSNet-V1.
    Table 4 compares the performance of the DaSNet-V2 in semantic seg-
mentation of branch with different backbones. From the experiment results,
DaSNet-V2 with Resnet-101 outperforms in the comparison. The DaSNet-
V2 with Darknet-53 and LW-net achieves similar performance, which is 0.797
and 0.795, respectively. In terms of the computational efficiency, DaSNet-
V2 with LW-net requires 30ms for an image, while the DaSNet-V2 with
Darknet-53 and Resnet-101 requires 45ms and 60ms to process an image,
respectively.

4.3     Visual Sensing in Orchards
In traditional orchards, there are several issues that may affect the perfor-
mance of automatic harvesting. Firstly, overlapping of fruits or occlusion
between fruits, leaves and branches can affect the accuracy of the detection.
Secondly, ’free-growth’ and densely arranged branches can obstruct the de-
tach path of the manipulator. This experiment evaluates the performance
of the DaSNet-V2 in the real environment within the apple orchards. The

                                     11
Figure 6: Detection and segmentation results in the apple orchard by using
                            the DaSNet-V2.

experiment results, which are processed by using the DaSNet-V2 are shown
in Figure 6.
    From the figures shown in results, DaSNet-V2 can accurately detect the
fruit and segment the corresponding area of fruits from the background.
Meanwhile, the segmentation results of the branch are also presented in
fine and smooth detail. Also, DaSNet-V2 shows a robust performance to
segment the fruits in the overlapping and occlusion conditions. Consider-
ing limited computation resource is available in orchard environments, the
DaSNet-V2 is tested on the Jetson-TX2 to evaluate its computational avail-
ability. The computational efficiency of the DaSNet-V2 on GTX-1080Ti and
Jetson-TX2 are listed in Table 5. It can be seen that the one-stage detec-
tor such as YOLO and DaSNet have obvious advantages to be deployed on
the embedded computational device compared to the two-stage detector in
terms of the computational efficiency.

4.4   3D Visualisation of Environments
Fruit detection and instance segmentation, and branch segmentation in 2D
image space is a straightforward way of understanding the working environ-
ments in guiding the manipulator to detach the fruits. DaSNet-V2 is further
evaluated to perform the work on the RGB-D images which are collected
from the apple orchard. The 3D visualisation of the orchard environment,
which are processed by using the DaSNet-V2 are shown in Figure 7.
   Orchard environment in 3D presentation form can clearly describe the
working environment of the fruit harvesting robot. The orientation and

                                    12
    Table 5: Comparison of performance of semantic segmentation between
                          different network models

       Device               Model                 Weight Size      Time
     GTX-1080Ti      DaSNet-V2 (LW-net)              8.1 M          30ms
     GTX-1080Ti      DaSNet-V1 (LW-net)             12.8 M          32ms
     GTX-1080Ti     YOLO-Tiny (Darknet-18)          35.4 M          30ms
     GTX-1080Ti     Faster-RCNN (VGG-16)            533 M          145ms
     GTX-1080Ti     Mask-RCNN (Resnet-101)          244 M          137ms
     Jetson-TX2      DaSNet-V2 (LW-net)              8.1 M         278ms
     Jetson-TX2      DaSNet-V1 (LW-net)             12.8 M         326ms
     Jetson-TX2     YOLO-Tiny (Darknet-18)          35.4 M         265ms
     Jetson-TX2     Faster-RCNN (VGG-16)            533 M            1.3s
     Jetson-TX2     Mask-RCNN (Resnet-101)          244 M           1.21s

shape of fruits, the structure of trees, and the possible orientation and loca-
tion of the stem-branch joint of fruits can be seen or estimated from the 3D
scene. Such information and scene can be further used to guide the detach-
ment of the fruits or reconstruct and modelling the working environment
of the fruit harvesting robot. From the 3D visualisation results which are
shown in Figure, it can be seen that DaSNet-V2 can robustly and efficiently
perform the multi-function work in the real orchard environment.

5      Conclusion and Future Work
In this study, a multi-function one-stage detector DaSNet-V2 was developed
and evaluated. DaSNet-V2 comprises a detection and instance segmentation
branch to perform the detection, segmentation, and localisation of the fruits
and a semantic segmentation branch to perform the semantic segmentation
of the branch within orchards. DaSNet-V2 adopts gated-FPN and ASPP
to improve the detection performance of the model, a light-weight backbone
LW-net was also developed and utilised in the DaSNet-V2 to improve the
computational availability of the model on the embedded computational de-
vice. In the experiment, DaSNet-V2 shows accurate detection and segmen-
tation performance. DaSNet-V2 with Resnet-101 achieved 0.856, 0.862, and
0.802 on detection, fruit segmentation, and branch segmentation, respec-
tively. DaSNet-V2 with LW-net achieved 0.844, 0.858, and 0.795 on detec-
tion, fruit segmentation, and branch segmentation, respectively. The com-
putational time of DaSNet-V2 with LW-net on GTX-1080Ti and Jetson-TX2
are 30ms and 265ms, respectively. From the experiment results, DaSNet-
V2 showed robust and efficient performance to perform the vision sensing
in orchards. Future work will focus on developing the orchard reconstruc-
tion algorithm based on the DaSNet-V2, corresponding control strategy for

                                      13
   Figure 7: 3D visualisation of the orchard environment by using the
DaSNet-V2 and PPTK tool-kit. The apples are presented in colour mask,
  branches are presented by its original colour, and the other elements
             within the image are presented in black colour.

guiding the automatic robotic fruit harvesting will also be included.

Acknowledgement
This work is supported by ARC ITRH IH150100006 and THOR TECH PTY
LTD. We acknowledge Zijue Chen and Hongyu Zhou for their assistance in
the data collection. And we also acknowledge Zhuo Chen for her assistance
in preparation of this work.

References
ABARES. Australian vegetable growing farms: an economic survey, 2016-17
 and 2017-18. Australian Bureau of Agricultural and Resource Economics
 (ABARE): Canberra, 2018.

Suchet Bargoti and James Underwood. Deep fruit detection in orchards.
  In 2017 IEEE International Conference on Robotics and Automation
  (ICRA), pages 3626–3633. IEEE, 2017.

Alberto Garcia-Garcia, Sergio Orts-Escolano, Sergiu Oprea, Victor Villena-
  Martinez, and Jose Garcia-Rodriguez.        A review on deep learn-
  ing techniques applied to semantic segmentation.        arXiv preprint
  arXiv:1704.06857, 2017.

                                     14
Ross Girshick. Fast r-cnn. In Proceedings of the IEEE international confer-
  ence on computer vision, pages 1440–1448, 2015.

Junwei Han, Dingwen Zhang, Gong Cheng, Nian Liu, and Dong Xu. Ad-
  vanced deep-learning techniques for salient and category-specific object
  detection: a survey. IEEE Signal Processing Magazine, 35(1):84–100,
  2018.

Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Girshick. Mask r-cnn.
 In Proceedings of the IEEE international conference on computer vision,
 pages 2961–2969, 2017.

Heremaps.   heremaps/pptk, Oct 2018.          URL https://github.com/
  heremaps/pptk.

Andreas Kamilaris and Francesc X Prenafeta-Boldú. Deep learning in agri-
 culture: A survey. Computers and electronics in agriculture, 147:70–90,
 2018.

Hanwen Kang and Chao Chen. Fruit detection and segmentation for apple
 harvesting using visual sensor in orchards. Sensors, 19(20):4599, 2019.

Keren Kapach, Ehud Barnea, Rotem Mairon, Yael Edan, and Ohad Ben-
 Shahar. Computer vision for fruit harvesting robots–state of the art and
 challenges ahead. International Journal of Computational Vision and
 Robotics, 3(1/2):4–34, 2012.

A Koirala, KB Walsh, Z Wang, and C McCarthy. Deep learning for real-
  time fruit detection and orchard fruit load estimation: Benchmarking of
  mangoyolo. Precision Agriculture, pages 1–29, 2019.

Guichao Lin, Yunchao Tang, Xiangjun Zou, Juntao Xiong, and Yamei Fang.
 Color-, depth-, and shape-based 3d fruit detection. Precision Agriculture,
 pages 1–17, 2019a.

Guichao Lin, Yunchao Tang, Xiangjun Zou, Juntao Xiong, and Jinhui Li.
 Guava detection and pose estimation using a low-cost rgb-d sensor in the
 field. Sensors, 19(2):428, 2019b.

Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár.
  Focal loss for dense object detection. In Proceedings of the IEEE interna-
  tional conference on computer vision, pages 2980–2988, 2017.

Xiaoyang Liu, Weikuan Jia, Chengzhi Ruan, Dean Zhao, Yuwan Gu, and
  Wei Chen. The recognition of apple fruits in plastic bags based on block
  classification. Precision agriculture, 19(4):735–749, 2018.

                                    15
Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully convolutional
  networks for semantic segmentation. In Proceedings of the IEEE confer-
  ence on computer vision and pattern recognition, pages 3431–3440, 2015.

Christopher McCool, Inkyu Sa, Feras Dayoub, Christopher Lehnert, Tristan
 Perez, and Ben Upcroft. Visual detection of occluded crop: For automated
 harvesting. In 2016 IEEE International Conference on Robotics and Au-
 tomation (ICRA), pages 2506–2512. IEEE, 2016.

Tien Thanh Nguyen, Koenraad Vandevoorde, Niels Wouters, Erdal Kaya-
  can, Josse G De Baerdemaeker, and Wouter Saeys. Detection of red and
  bicoloured apples on tree with an rgb-d camera. Biosystems Engineering,
  146:33–44, 2016.

Joseph Redmon and Ali Farhadi. Yolov3: An incremental improvement.
  arXiv preprint arXiv:1804.02767, 2018.

Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. Faster r-cnn:
  Towards real-time object detection with region proposal networks. In
  Advances in neural information processing systems, pages 91–99, 2015.

Inkyu Sa, Zongyuan Ge, Feras Dayoub, Ben Upcroft, Tristan Perez, and
  Chris McCool. Deepfruits: A fruit detection system using deep neural
  networks. Sensors, 16(8):1222, 2016.

Yunong Tian, Guodong Yang, Zhe Wang, Hao Wang, En Li, and Zize Liang.
  Apple detection during different growth stages in orchards using the im-
  proved yolo-v3 model. Computers and electronics in agriculture, 157:
  417–426, 2019.

Juan P Vasconez, George A Kantor, and Fernando A Auat Cheein. Human–
  robot interaction in agriculture: A survey and current challenges. Biosys-
  tems engineering, 179:35–48, 2019.

Anup Vibhute and SK Bodhe. Applications of image processing in agricul-
 ture: a survey. International Journal of Computer Applications, 52(2),
 2012.

Yi Wang and Lihong Xu. Unsupervised segmentation of greenhouse plant
  images based on modified latent dirichlet allocation. PeerJ, 6:e5036, 2018.

Hui Xu, Guodong Chen, Zhenhua Wang, Lining Sun, and Fan Su. Rgb-
 d-based pose estimation of workpieces with semantic segmentation and
 point cloud registration. Sensors, 19(8):1873, 2019.

Jinghan Yao, Zhou Yu, Jun Yu, and Dacheng Tao.          Single pixel
  reconstruction for one-stage instance segmentation. arXiv preprint
  arXiv:1904.07426, 2019.

                                     16
Yang Yu, Kailiang Zhang, Li Yang, and Dongxing Zhang. Fruit detection
  for strawberry harvesting robot in non-structural environment based on
  mask-rcnn. Computers and Electronics in Agriculture, 163:104846, 2019.

Yuanshen Zhao, Liang Gong, Yixiang Huang, and Chengliang Liu. A review
  of key techniques of vision-based control for harvesting robot. Computers
  and Electronics in Agriculture, 127:311–323, 2016.

Rong Zhou, Lutz Damerow, Yurui Sun, and Michael M Blanke. Using colour
  features of cv.galaapple fruits in an orchard in image processing to predict
  yield. Precision Agriculture, 13(5):568–580, 2012.

                                     17
