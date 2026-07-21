---
source_id: 004
bibtex_key: bochkovskiy2020yolov4
title: YOLOv4: Optimal Speed and Accuracy of Object Detection
year: 2020
domain_theme: Fondasi RGB
verified_pdf: 4_YOLOv4.pdf
char_count: 104326
---

YOLOv4: Optimal Speed and Accuracy of Object Detection

                                             Alexey Bochkovskiy∗                       Chien-Yao Wang∗                             Hong-Yuan Mark Liao
                                             alexeyab84@gmail.com              Institute of Information Science               Institute of Information Science
                                                                                  Academia Sinica, Taiwan                        Academia Sinica, Taiwan
                                                                                  kinyiu@iis.sinica.edu.tw                        liao@iis.sinica.edu.tw
arXiv:2004.10934v1 [cs.CV] 23 Apr 2020

                                                                 Abstract

                                            There are a huge number of features which are said to
                                         improve Convolutional Neural Network (CNN) accuracy.
                                         Practical testing of combinations of such features on large
                                         datasets, and theoretical justification of the result, is re-
                                         quired. Some features operate on certain models exclusively
                                         and for certain problems exclusively, or only for small-scale
                                         datasets; while some features, such as batch-normalization
                                         and residual-connections, are applicable to the majority of
                                         models, tasks, and datasets. We assume that such universal
                                         features include Weighted-Residual-Connections (WRC),
                                         Cross-Stage-Partial-connections (CSP), Cross mini-Batch
                                         Normalization (CmBN), Self-adversarial-training (SAT)
                                         and Mish-activation. We use new features: WRC, CSP,
                                         CmBN, SAT, Mish activation, Mosaic data augmentation,
                                         CmBN, DropBlock regularization, and CIoU loss, and com-             Figure 1: Comparison of the proposed YOLOv4 and other
                                         bine some of them to achieve state-of-the-art results: 43.5%        state-of-the-art object detectors. YOLOv4 runs twice faster
                                         AP (65.7% AP50 ) for the MS COCO dataset at a real-                 than EfficientDet with comparable performance. Improves
                                         time speed of ∼65 FPS on Tesla V100. Source code is at              YOLOv3’s AP and FPS by 10% and 12%, respectively.
                                         https://github.com/AlexeyAB/darknet.
                                                                                                                The main goal of this work is designing a fast operating
                                                                                                             speed of an object detector in production systems and opti-
                                         1. Introduction                                                     mization for parallel computations, rather than the low com-
                                                                                                             putation volume theoretical indicator (BFLOP). We hope
                                             The majority of CNN-based object detectors are largely          that the designed object can be easily trained and used. For
                                         applicable only for recommendation systems. For example,            example, anyone who uses a conventional GPU to train and
                                         searching for free parking spaces via urban video cameras           test can achieve real-time, high quality, and convincing ob-
                                         is executed by slow accurate models, whereas car collision          ject detection results, as the YOLOv4 results shown in Fig-
                                         warning is related to fast inaccurate models. Improving             ure 1. Our contributions are summarized as follows:
                                         the real-time object detector accuracy enables using them
                                         not only for hint generating recommendation systems, but             1. We develope an efficient and powerful object detection
                                         also for stand-alone process management and human input                 model. It makes everyone can use a 1080 Ti or 2080 Ti
                                         reduction. Real-time object detector operation on conven-               GPU to train a super fast and accurate object detector.
                                         tional Graphics Processing Units (GPU) allows their mass             2. We verify the influence of state-of-the-art Bag-of-
                                         usage at an affordable price. The most accurate modern                  Freebies and Bag-of-Specials methods of object detec-
                                         neural networks do not operate in real time and require large           tion during the detector training.
                                         number of GPUs for training with a large mini-batch-size.
                                         We address such problems through creating a CNN that op-             3. We modify state-of-the-art methods and make them
                                         erates in real-time on a conventional GPU, and for which                more effecient and suitable for single GPU training,
                                         training requires only one conventional GPU.                            including CBN [89], PAN [49], SAM [85], etc.

                                                                                                         1
                                                     Figure 2: Object detector.

2. Related work                                                        In addition to the above models, some researchers put their
                                                                       emphasis on directly building a new backbone (DetNet [43],
2.1. Object detection models                                           DetNAS [7]) or a new whole model (SpineNet [12], HitDe-
                                                                       tector [20]) for object detection.
    A modern detector is usually composed of two parts,
                                                                          To sum up, an ordinary object detector is composed of
a backbone which is pre-trained on ImageNet and a head
                                                                       several parts:
which is used to predict classes and bounding boxes of ob-
jects. For those detectors running on GPU platform, their                • Input: Image, Patches, Image Pyramid
backbone could be VGG [68], ResNet [26], ResNeXt [86],
or DenseNet [30]. For those detectors running on CPU plat-               • Backbones: VGG16 [68], ResNet-50 [26], SpineNet
form, their backbone could be SqueezeNet [31], MobileNet                   [12], EfficientNet-B0/B7 [75], CSPResNeXt50 [81],
[28, 66, 27, 74], or ShuffleNet [97, 53]. As to the head part,             CSPDarknet53 [81]
it is usually categorized into two kinds, i.e., one-stage object         • Neck:
detector and two-stage object detector. The most represen-
tative two-stage object detector is the R-CNN [19] series,                    • Additional blocks: SPP [25], ASPP [5], RFB
including fast R-CNN [18], faster R-CNN [64], R-FCN [9],                        [47], SAM [85]
and Libra R-CNN [58]. It is also possible to make a two-                      • Path-aggregation blocks: FPN [44], PAN [49],
stage object detector an anchor-free object detector, such as                   NAS-FPN [17], Fully-connected FPN, BiFPN
RepPoints [87]. As for one-stage object detector, the most                      [77], ASFF [48], SFAM [98]
representative models are YOLO [61, 62, 63], SSD [50],
and RetinaNet [45]. In recent years, anchor-free one-stage               • Heads::
object detectors are developed. The detectors of this sort are                • Dense Prediction (one-stage):
CenterNet [13], CornerNet [37, 38], FCOS [78], etc. Object                        ◦ RPN [64], SSD [50], YOLO [61], RetinaNet
detectors developed in recent years often insert some lay-                          [45] (anchor based)
ers between backbone and head, and these layers are usu-
                                                                                  ◦ CornerNet [37], CenterNet [13], MatrixNet
ally used to collect feature maps from different stages. We
                                                                                    [60], FCOS [78] (anchor free)
can call it the neck of an object detector. Usually, a neck
is composed of several bottom-up paths and several top-                       • Sparse Prediction (two-stage):
down paths. Networks equipped with this mechanism in-                             ◦ Faster R-CNN [64], R-FCN [9], Mask R-
clude Feature Pyramid Network (FPN) [44], Path Aggrega-                             CNN [23] (anchor based)
tion Network (PAN) [49], BiFPN [77], and NAS-FPN [17].                            ◦ RepPoints [87] (anchor free)

                                                                   2
2.2. Bag of freebies                                                   to one-stage object detector, because this kind of detector
                                                                       belongs to the dense prediction architecture. Therefore Lin
    Usually, a conventional object detector is trained off-
                                                                       et al. [45] proposed focal loss to deal with the problem
line. Therefore, researchers always like to take this advan-
                                                                       of data imbalance existing between various classes. An-
tage and develop better training methods which can make
                                                                       other very important issue is that it is difficult to express the
the object detector receive better accuracy without increas-
                                                                       relationship of the degree of association between different
ing the inference cost. We call these methods that only
                                                                       categories with the one-hot hard representation. This rep-
change the training strategy or only increase the training
                                                                       resentation scheme is often used when executing labeling.
cost as “bag of freebies.” What is often adopted by object
                                                                       The label smoothing proposed in [73] is to convert hard la-
detection methods and meets the definition of bag of free-
                                                                       bel into soft label for training, which can make model more
bies is data augmentation. The purpose of data augmenta-
                                                                       robust. In order to obtain a better soft label, Islam et al. [33]
tion is to increase the variability of the input images, so that
                                                                       introduced the concept of knowledge distillation to design
the designed object detection model has higher robustness
                                                                       the label refinement network.
to the images obtained from different environments. For
                                                                           The last bag of freebies is the objective function of
examples, photometric distortions and geometric distortions
                                                                       Bounding Box (BBox) regression. The traditional object
are two commonly used data augmentation method and they
                                                                       detector usually uses Mean Square Error (MSE) to di-
definitely benefit the object detection task. In dealing with
                                                                       rectly perform regression on the center point coordinates
photometric distortion, we adjust the brightness, contrast,
                                                                       and height and width of the BBox, i.e., {xcenter , ycenter ,
hue, saturation, and noise of an image. For geometric dis-
                                                                       w, h}, or the upper left point and the lower right point,
tortion, we add random scaling, cropping, flipping, and ro-
                                                                       i.e., {xtop lef t , ytop lef t , xbottom right , ybottom right }. As
tating.
                                                                       for anchor-based method, it is to estimate the correspond-
    The data augmentation methods mentioned above are all
                                                                       ing offset, for example {xcenter of f set , ycenter of f set ,
pixel-wise adjustments, and all original pixel information in
                                                                       wof f set , hof f set } and {xtop lef t of f set , ytop lef t of f set ,
the adjusted area is retained. In addition, some researchers
                                                                       xbottom right of f set , ybottom right of f set }. However, to di-
engaged in data augmentation put their emphasis on sim-
                                                                       rectly estimate the coordinate values of each point of the
ulating object occlusion issues. They have achieved good
                                                                       BBox is to treat these points as independent variables, but
results in image classification and object detection. For ex-
                                                                       in fact does not consider the integrity of the object itself. In
ample, random erase [100] and CutOut [11] can randomly
                                                                       order to make this issue processed better, some researchers
select the rectangle region in an image and fill in a random
                                                                       recently proposed IoU loss [90], which puts the coverage of
or complementary value of zero. As for hide-and-seek [69]
                                                                       predicted BBox area and ground truth BBox area into con-
and grid mask [6], they randomly or evenly select multiple
                                                                       sideration. The IoU loss computing process will trigger the
rectangle regions in an image and replace them to all ze-
                                                                       calculation of the four coordinate points of the BBox by ex-
ros. If similar concepts are applied to feature maps, there
                                                                       ecuting IoU with the ground truth, and then connecting the
are DropOut [71], DropConnect [80], and DropBlock [16]
                                                                       generated results into a whole code. Because IoU is a scale
methods. In addition, some researchers have proposed the
                                                                       invariant representation, it can solve the problem that when
methods of using multiple images together to perform data
                                                                       traditional methods calculate the l1 or l2 loss of {x, y, w,
augmentation. For example, MixUp [92] uses two images
                                                                       h}, the loss will increase with the scale. Recently, some
to multiply and superimpose with different coefficient ra-
                                                                       researchers have continued to improve IoU loss. For exam-
tios, and then adjusts the label with these superimposed ra-
                                                                       ple, GIoU loss [65] is to include the shape and orientation
tios. As for CutMix [91], it is to cover the cropped image
                                                                       of object in addition to the coverage area. They proposed to
to rectangle region of other images, and adjusts the label
                                                                       find the smallest area BBox that can simultaneously cover
according to the size of the mix area. In addition to the
                                                                       the predicted BBox and ground truth BBox, and use this
above mentioned methods, style transfer GAN [15] is also
                                                                       BBox as the denominator to replace the denominator origi-
used for data augmentation, and such usage can effectively
                                                                       nally used in IoU loss. As for DIoU loss [99], it additionally
reduce the texture bias learned by CNN.
                                                                       considers the distance of the center of an object, and CIoU
    Different from the various approaches proposed above,              loss [99], on the other hand simultaneously considers the
some other bag of freebies methods are dedicated to solving            overlapping area, the distance between center points, and
the problem that the semantic distribution in the dataset may          the aspect ratio. CIoU can achieve better convergence speed
have bias. In dealing with the problem of semantic distri-             and accuracy on the BBox regression problem.
bution bias, a very important issue is that there is a problem
of data imbalance between different classes, and this prob-
lem is often solved by hard negative example mining [72]
or online hard example mining [67] in two-stage object de-
tector. But the example mining method is not applicable

                                                                   3
2.3. Bag of specials                                                     In terms of feature integration, the early practice is to use
                                                                      skip connection [51] or hyper-column [22] to integrate low-
    For those plugin modules and post-processing methods
                                                                      level physical feature to high-level semantic feature. Since
that only increase the inference cost by a small amount
                                                                      multi-scale prediction methods such as FPN have become
but can significantly improve the accuracy of object detec-
                                                                      popular, many lightweight modules that integrate different
tion, we call them “bag of specials”. Generally speaking,
                                                                      feature pyramid have been proposed. The modules of this
these plugin modules are for enhancing certain attributes in
                                                                      sort include SFAM [98], ASFF [48], and BiFPN [77]. The
a model, such as enlarging receptive field, introducing at-
                                                                      main idea of SFAM is to use SE module to execute channel-
tention mechanism, or strengthening feature integration ca-
                                                                      wise level re-weighting on multi-scale concatenated feature
pability, etc., and post-processing is a method for screening
                                                                      maps. As for ASFF, it uses softmax as point-wise level re-
model prediction results.
                                                                      weighting and then adds feature maps of different scales.
    Common modules that can be used to enhance recep-
                                                                      In BiFPN, the multi-input weighted residual connections is
tive field are SPP [25], ASPP [5], and RFB [47]. The
                                                                      proposed to execute scale-wise level re-weighting, and then
SPP module was originated from Spatial Pyramid Match-
                                                                      add feature maps of different scales.
ing (SPM) [39], and SPMs original method was to split fea-
ture map into several d × d equal blocks, where d can be                 In the research of deep learning, some people put their
{1, 2, 3, ...}, thus forming spatial pyramid, and then extract-       focus on searching for good activation function. A good
ing bag-of-word features. SPP integrates SPM into CNN                 activation function can make the gradient more efficiently
and use max-pooling operation instead of bag-of-word op-              propagated, and at the same time it will not cause too
eration. Since the SPP module proposed by He et al. [25]              much extra computational cost. In 2010, Nair and Hin-
will output one dimensional feature vector, it is infeasible to       ton [56] propose ReLU to substantially solve the gradient
be applied in Fully Convolutional Network (FCN). Thus in              vanish problem which is frequently encountered in tradi-
the design of YOLOv3 [63], Redmon and Farhadi improve                 tional tanh and sigmoid activation function. Subsequently,
SPP module to the concatenation of max-pooling outputs                LReLU [54], PReLU [24], ReLU6 [28], Scaled Exponential
with kernel size k × k, where k = {1, 5, 9, 13}, and stride           Linear Unit (SELU) [35], Swish [59], hard-Swish [27], and
equals to 1. Under this design, a relatively large k × k max-         Mish [55], etc., which are also used to solve the gradient
pooling effectively increase the receptive field of backbone          vanish problem, have been proposed. The main purpose of
feature. After adding the improved version of SPP module,             LReLU and PReLU is to solve the problem that the gradi-
YOLOv3-608 upgrades AP50 by 2.7% on the MS COCO                       ent of ReLU is zero when the output is less than zero. As
object detection task at the cost of 0.5% extra computation.          for ReLU6 and hard-Swish, they are specially designed for
The difference in operation between ASPP [5] module and               quantization networks. For self-normalizing a neural net-
improved SPP module is mainly from the original k ×k ker-             work, the SELU activation function is proposed to satisfy
nel size, max-pooling of stride equals to 1 to several 3 × 3          the goal. One thing to be noted is that both Swish and Mish
kernel size, dilated ratio equals to k, and stride equals to 1        are continuously differentiable activation function.
in dilated convolution operation. RFB module is to use sev-               The post-processing method commonly used in deep-
eral dilated convolutions of k ×k kernel, dilated ratio equals        learning-based object detection is NMS, which can be used
to k, and stride equals to 1 to obtain a more comprehensive           to filter those BBoxes that badly predict the same ob-
spatial coverage than ASPP. RFB [47] only costs 7% extra              ject, and only retain the candidate BBoxes with higher re-
inference time to increase the AP50 of SSD on MS COCO                 sponse. The way NMS tries to improve is consistent with
by 5.7%.                                                              the method of optimizing an objective function. The orig-
    The attention module that is often used in object detec-          inal method proposed by NMS does not consider the con-
tion is mainly divided into channel-wise attention and point-         text information, so Girshick et al. [19] added classification
wise attention, and the representatives of these two atten-           confidence score in R-CNN as a reference, and according to
tion models are Squeeze-and-Excitation (SE) [29] and Spa-             the order of confidence score, greedy NMS was performed
tial Attention Module (SAM) [85], respectively. Although              in the order of high score to low score. As for soft NMS [1],
SE module can improve the power of ResNet50 in the Im-                it considers the problem that the occlusion of an object may
ageNet image classification task 1% top-1 accuracy at the             cause the degradation of confidence score in greedy NMS
cost of only increasing the computational effort by 2%, but           with IoU score. The DIoU NMS [99] developers way of
on a GPU usually it will increase the inference time by               thinking is to add the information of the center point dis-
about 10%, so it is more appropriate to be used in mobile             tance to the BBox screening process on the basis of soft
devices. But for SAM, it only needs to pay 0.1% extra cal-            NMS. It is worth mentioning that, since none of above post-
culation and it can improve ResNet50-SE 0.5% top-1 accu-              processing methods directly refer to the captured image fea-
racy on the ImageNet image classification task. Best of all,          tures, post-processing is no longer required in the subse-
it does not affect the speed of inference on the GPU at all.          quent development of an anchor-free method.

                                                                  4
                                     Table 1: Parameters of neural networks for image classification.
                                                                            Average size
                             Input network   Receptive                                                BFLOPs                     FPS
       Backbone model                                     Parameters       of layer output
                               resolution    field size                                      (512x512 network resolution)   (GPU RTX 2070)
                                                                             (WxHxC)
        CSPResNext50           512x512        425x425      20.6 M             1058 K               31 (15.5 FMA)                  62
        CSPDarknet53           512x512        725x725      27.6 M              950 K               52 (26.0 FMA)                  66
    EfficientNet-B3 (ours)     512x512       1311x1311     12.0 M              668 K               11 (5.5 FMA)                   26

3. Methodology                                                                  Hypothetically speaking, we can assume that a model
                                                                            with a larger receptive field size (with a larger number of
    The basic aim is fast operating speed of neural network,                convolutional layers 3 × 3) and a larger number of parame-
in production systems and optimization for parallel compu-                  ters should be selected as the backbone. Table 1 shows the
tations, rather than the low computation volume theoreti-                   information of CSPResNeXt50, CSPDarknet53, and Effi-
cal indicator (BFLOP). We present two options of real-time                  cientNet B3. The CSPResNext50 contains only 16 convo-
neural networks:                                                            lutional layers 3 × 3, a 425 × 425 receptive field and 20.6
                                                                            M parameters, while CSPDarknet53 contains 29 convolu-
  • For GPU we use a small number of groups (1 - 8) in                      tional layers 3 × 3, a 725 × 725 receptive field and 27.6
    convolutional layers: CSPResNeXt50 / CSPDarknet53                       M parameters. This theoretical justification, together with
                                                                            our numerous experiments, show that CSPDarknet53 neu-
  • For VPU - we use grouped-convolution, but we re-                        ral network is the optimal model of the two as the backbone
    frain from using Squeeze-and-excitement (SE) blocks                     for a detector.
    - specifically this includes the following models:
                                                                                The influence of the receptive field with different sizes is
    EfficientNet-lite / MixNet [76] / GhostNet [21] / Mo-
                                                                            summarized as follows:
    bileNetV3
                                                                               • Up to the object size - allows viewing the entire object
3.1. Selection of architecture
    Our objective is to find the optimal balance among the in-                 • Up to network size - allows viewing the context around
put network resolution, the convolutional layer number, the                      the object
parameter number (filter size2 * filters * channel / groups),
and the number of layer outputs (filters). For instance, our                   • Exceeding the network size - increases the number of
numerous studies demonstrate that the CSPResNext50 is                            connections between the image point and the final ac-
considerably better compared to CSPDarknet53 in terms                            tivation
of object classification on the ILSVRC2012 (ImageNet)
dataset [10]. However, conversely, the CSPDarknet53 is                         We add the SPP block over the CSPDarknet53, since it
better compared to CSPResNext50 in terms of detecting ob-                   significantly increases the receptive field, separates out the
jects on the MS COCO dataset [46].                                          most significant context features and causes almost no re-
    The next objective is to select additional blocks for in-               duction of the network operation speed. We use PANet as
creasing the receptive field and the best method of parame-                 the method of parameter aggregation from different back-
ter aggregation from different backbone levels for different                bone levels for different detector levels, instead of the FPN
detector levels: e.g. FPN, PAN, ASFF, BiFPN.                                used in YOLOv3.
    A reference model which is optimal for classification is                   Finally, we choose CSPDarknet53 backbone, SPP addi-
not always optimal for a detector. In contrast to the classi-               tional module, PANet path-aggregation neck, and YOLOv3
fier, the detector requires the following:                                  (anchor based) head as the architecture of YOLOv4.
                                                                               In the future we plan to expand significantly the content
  • Higher input network size (resolution) – for detecting                  of Bag of Freebies (BoF) for the detector, which theoreti-
    multiple small-sized objects                                            cally can address some problems and increase the detector
                                                                            accuracy, and sequentially check the influence of each fea-
  • More layers – for a higher receptive field to cover the                 ture in an experimental fashion.
    increased size of input network                                            We do not use Cross-GPU Batch Normalization (CGBN
                                                                            or SyncBN) or expensive specialized devices. This al-
  • More parameters – for greater capacity of a model to                    lows anyone to reproduce our state-of-the-art outcomes on
    detect multiple objects of different sizes in a single im-              a conventional graphic processor e.g. GTX 1080Ti or RTX
    age                                                                     2080Ti.

                                                                       5
3.2. Selection of BoF and BoS
   For improving the object detection training, a CNN usu-
ally uses the following:

  • Activations: ReLU, leaky-ReLU, parametric-ReLU,
    ReLU6, SELU, Swish, or Mish

  • Bounding box regression loss: MSE, IoU, GIoU,
    CIoU, DIoU

  • Data augmentation: CutOut, MixUp, CutMix

  • Regularization method: DropOut, DropPath [36],
                                                                    Figure 3: Mosaic represents a new method of data augmen-
    Spatial DropOut [79], or DropBlock
                                                                    tation.
  • Normalization of the network activations by their               mixed, while CutMix mixes only 2 input images. This al-
    mean and variance: Batch Normalization (BN) [32],               lows detection of objects outside their normal context. In
    Cross-GPU Batch Normalization (CGBN or SyncBN)                  addition, batch normalization calculates activation statistics
    [93], Filter Response Normalization (FRN) [70], or              from 4 different images on each layer. This significantly
    Cross-Iteration Batch Normalization (CBN) [89]                  reduces the need for a large mini-batch size.
  • Skip-connections: Residual connections, Weighted                   Self-Adversarial Training (SAT) also represents a new
    residual connections, Multi-input weighted residual             data augmentation technique that operates in 2 forward
    connections, or Cross stage partial connections (CSP)           backward stages. In the 1st stage the neural network alters
                                                                    the original image instead of the network weights. In this
   As for training activation function, since PReLU and             way the neural network executes an adversarial attack on it-
SELU are more difficult to train, and ReLU6 is specifically         self, altering the original image to create the deception that
designed for quantization network, we therefore remove the          there is no desired object on the image. In the 2nd stage, the
above activation functions from the candidate list. In the          neural network is trained to detect an object on this modified
method of reqularization, the people who published Drop-            image in the normal way.
Block have compared their method with other methods in
detail, and their regularization method has won a lot. There-
fore, we did not hesitate to choose DropBlock as our reg-
ularization method. As for the selection of normalization
method, since we focus on a training strategy that uses only
one GPU, syncBN is not considered.

3.3. Additional improvements
    In order to make the designed detector more suitable for
training on single GPU, we made additional design and im-
provement as follows:

  • We introduce a new method of data augmentation Mo-
    saic, and Self-Adversarial Training (SAT)

  • We select optimal hyper-parameters while applying                       Figure 4: Cross mini-Batch Normalization.
    genetic algorithms                                                 CmBN represents a CBN modified version, as shown
                                                                    in Figure 4, defined as Cross mini-Batch Normalization
  • We modify some exsiting methods to make our design
                                                                    (CmBN). This collects statistics only between mini-batches
    suitble for efficient training and detection - modified
                                                                    within a single batch.
    SAM, modified PAN, and Cross mini-Batch Normal-
    ization (CmBN)                                                     We modify SAM from spatial-wise attention to point-
                                                                    wise attention, and replace shortcut connection of PAN to
  Mosaic represents a new data augmentation method that             concatenation, as shown in Figure 5 and Figure 6, respec-
mixes 4 training images. Thus 4 different contexts are              tively.

                                                                6
                                                                   4. Experiments

                                                                      We test the influence of different training improve-
                                                                   ment techniques on accuracy of the classifier on ImageNet
                                                                   (ILSVRC 2012 val) dataset, and then on the accuracy of the
                                                                   detector on MS COCO (test-dev 2017) dataset.

                                                                   4.1. Experimental setup

                                                                      In ImageNet image classification experiments, the de-
                Figure 5: Modified SAM.                            fault hyper-parameters are as follows: the training steps is
                                                                   8,000,000; the batch size and the mini-batch size are 128
                                                                   and 32, respectively; the polynomial decay learning rate
                                                                   scheduling strategy is adopted with initial learning rate 0.1;
                                                                   the warm-up steps is 1000; the momentum and weight de-
                                                                   cay are respectively set as 0.9 and 0.005. All of our BoS
                                                                   experiments use the same hyper-parameter as the default
                                                                   setting, and in the BoF experiments, we add an additional
                                                                   50% training steps. In the BoF experiments, we verify
                                                                   MixUp, CutMix, Mosaic, Bluring data augmentation, and
                Figure 6: Modified PAN.                            label smoothing regularization methods. In the BoS experi-
                                                                   ments, we compared the effects of LReLU, Swish, and Mish
3.4. YOLOv4                                                        activation function. All experiments are trained with a 1080
                                                                   Ti or 2080 Ti GPU.
  In this section, we shall elaborate the details of YOLOv4.
                                                                      In MS COCO object detection experiments, the de-
  YOLOv4 consists of:                                              fault hyper-parameters are as follows: the training steps is
 • Backbone: CSPDarknet53 [81]                                     500,500; the step decay learning rate scheduling strategy is
                                                                   adopted with initial learning rate 0.01 and multiply with a
 • Neck: SPP [25], PAN [49]                                        factor 0.1 at the 400,000 steps and the 450,000 steps, re-
                                                                   spectively; The momentum and weight decay are respec-
 • Head: YOLOv3 [63]                                               tively set as 0.9 and 0.0005. All architectures use a sin-
                                                                   gle GPU to execute multi-scale training in the batch size
                                                                   of 64 while mini-batch size is 8 or 4 depend on the ar-
  YOLO v4 uses:                                                    chitectures and GPU memory limitation. Except for us-
 • Bag of Freebies (BoF) for backbone: CutMix and                  ing genetic algorithm for hyper-parameter search experi-
   Mosaic data augmentation, DropBlock regularization,             ments, all other experiments use default setting. Genetic
   Class label smoothing                                           algorithm used YOLOv3-SPP to train with GIoU loss and
                                                                   search 300 epochs for min-val 5k sets. We adopt searched
 • Bag of Specials (BoS) for backbone: Mish activa-                learning rate 0.00261, momentum 0.949, IoU threshold for
   tion, Cross-stage partial connections (CSP), Multi-             assigning ground truth 0.213, and loss normalizer 0.07 for
   input weighted residual connections (MiWRC)                     genetic algorithm experiments. We have verified a large
                                                                   number of BoF, including grid sensitivity elimination, mo-
 • Bag of Freebies (BoF) for detector: CIoU-loss,
                                                                   saic data augmentation, IoU threshold, genetic algorithm,
   CmBN, DropBlock regularization, Mosaic data aug-
                                                                   class label smoothing, cross mini-batch normalization, self-
   mentation, Self-Adversarial Training, Eliminate grid
                                                                   adversarial training, cosine annealing scheduler, dynamic
   sensitivity, Using multiple anchors for a single ground
                                                                   mini-batch size, DropBlock, Optimized Anchors, different
   truth, Cosine annealing scheduler [52], Optimal hyper-
                                                                   kind of IoU losses. We also conduct experiments on various
   parameters, Random training shapes
                                                                   BoS, including Mish, SPP, SAM, RFB, BiFPN, and Gaus-
 • Bag of Specials (BoS) for detector: Mish activation,            sian YOLO [8]. For all experiments, we only use one GPU
   SPP-block, SAM-block, PAN path-aggregation block,               for training, so techniques such as syncBN that optimizes
   DIoU-NMS                                                        multiple GPUs are not used.

                                                               7
4.2. Influence of different features on Classifier                    4.3. Influence of different features on Detector
      training                                                             training
   First, we study the influence of different features on                Further study concerns the influence of different Bag-of-
classifier training; specifically, the influence of Class la-         Freebies (BoF-detector) on the detector training accuracy,
bel smoothing, the influence of different data augmentation           as shown in Table 4. We significantly expand the BoF list
techniques, bilateral blurring, MixUp, CutMix and Mosaic,             through studying different features that increase the detector
as shown in Fugure 7, and the influence of different activa-          accuracy without affecting FPS:
tions, such as Leaky-ReLU (by default), Swish, and Mish.
                                                                        • S: Eliminate grid sensitivity the equation bx = σ(tx )+
                                                                          cx , by = σ(ty ) + cy , where cx and cy are always whole
                                                                          numbers, is used in YOLOv3 for evaluating the ob-
                                                                          ject coordinates, therefore, extremely high tx absolute
                                                                          values are required for the bx value approaching the
                                                                          cx or cx + 1 values. We solve this problem through
                                                                          multiplying the sigmoid by a factor exceeding 1.0, so
                                                                          eliminating the effect of grid on which the object is
                                                                          undetectable.

                                                                        • M: Mosaic data augmentation - using the 4-image mo-
                                                                          saic during training instead of single image

                                                                        • IT: IoU threshold - using multiple anchors for a single
       Figure 7: Various method of data augmentation.
                                                                          ground truth IoU (truth, anchor) > IoU threshold
    In our experiments, as illustrated in Table 2, the clas-
sifier’s accuracy is improved by introducing the features               • GA: Genetic algorithms - using genetic algorithms for
such as: CutMix and Mosaic data augmentation, Class la-                   selecting the optimal hyperparameters during network
bel smoothing, and Mish activation. As a result, our BoF-                 training on the first 10% of time periods
backbone (Bag of Freebies) for classifier training includes
the following: CutMix and Mosaic data augmentation and                  • LS: Class label smoothing - using class label smooth-
Class label smoothing. In addition we use Mish activation                 ing for sigmoid activation
as a complementary option, as shown in Table 2 and Table
3.                                                                      • CBN: CmBN - using Cross mini-Batch Normalization
Table 2: Influence of BoF and Mish on the CSPResNeXt-50 clas-             for collecting statistics inside the entire batch, instead
sifier accuracy.                                                          of collecting statistics inside a single mini-batch
                                Label
MixUp CutMix Mosaic Bluring
                              Smoothing
                                        Swish Mish Top-1 Top-5          • CA: Cosine annealing scheduler - altering the learning
                                                                          rate during sinusoid training
                                                77.9% 94.0%
   X                                            77.2% 94.0%
          X                                     78.0% 94.3%             • DM: Dynamic mini-batch size - automatic increase of
                 X                              78.1% 94.5%               mini-batch size during small resolution training by us-
                        X                       77.5% 93.8%               ing Random training shapes
                                 X              78.1% 94.4%
                                         X      64.5% 86.0%
                                              X 78.9% 94.5%             • OA: Optimized Anchors - using the optimized anchors
          X      X               X              78.5% 94.8%               for training with the 512x512 network resolution
          X      X               X            X 79.8% 95.2%
                                                                        • GIoU, CIoU, DIoU, MSE - using different loss algo-
Table 3: Influence of BoF and Mish on the CSPDarknet-53 classi-           rithms for bounded box regression
fier accuracy.

MixUp CutMix Mosaic Bluring
                                Label
                                        Swish Mish Top-1 Top-5           Further study concerns the influence of different Bag-
                              Smoothing                               of-Specials (BoS-detector) on the detector training accu-
                                                77.2% 93.6%           racy, including PAN, RFB, SAM, Gaussian YOLO (G), and
          X      X               X              77.8% 94.4%           ASFF, as shown in Table 5. In our experiments, the detector
          X      X               X            X 78.7% 94.8%
                                                                      gets best performance when using SPP, PAN, and SAM.

                                                                  8
                          Table 4: Ablation Studies of Bag-of-Freebies. (CSPResNeXt50-PANet-SPP, 512x512).
                      S      M    IT   GA     LS       CBN     CA   DM     OA      loss     AP       AP50       AP75
                                                                                  MSE      38.0%     60.0%      40.8%
                      X                                                           MSE      37.7%     59.9%      40.5%
                             X                                                    MSE      39.1%     61.8%      42.0%
                                  X                                               MSE      36.9%     59.7%      39.4%
                                        X                                         MSE      38.9%     61.7%      41.9%
                                                X                                 MSE      33.0%     55.4%      35.4%
                                                        X                         MSE      38.4%     60.7%      41.3%
                                                                X                 MSE      38.7%     60.7%      41.9%
                                                                    X             MSE      35.3%     57.2%      38.0%
                      X                                                           GIoU     39.4%     59.4%      42.5%
                      X                                                           DIoU     39.1%     58.8%      42.1%
                      X                                                           CIoU     39.6%     59.2%      42.6%
                      X      X    X     X                                         CIoU     41.5%     64.0%      44.8%
                             X          X                                  X      CIoU     36.1%     56.5%      38.4%
                      X      X    X     X                                  X      MSE      40.3%     64.0%      43.1%
                      X      X    X     X                                  X      GIoU     42.4%     64.4%      45.9%
                      X      X    X     X                                  X      CIoU     42.4%     64.4%      45.9%

 Table 5: Ablation Studies of Bag-of-Specials. (Size 512x512).           Table 6: Using different classifier pre-trained weightings for de-
                                                                         tector training (all other training parameters are similar in all mod-
  Model                                  AP         AP50     AP75
                                                                         els) .
  CSPResNeXt50-PANet-SPP                42.4%       64.4%   45.9%
  CSPResNeXt50-PANet-SPP-RFB            41.8%       62.7%   45.1%         Model (with optimal setting)        Size       AP    AP50    AP75
  CSPResNeXt50-PANet-SPP-SAM            42.7%       64.6%   46.3%         CSPResNeXt50-PANet-SPP             512x512    42.4    64.4    45.9
  CSPResNeXt50-PANet-SPP-SAM-G          41.6%       62.7%   45.0%         CSPResNeXt50-PANet-SPP
  CSPResNeXt50-PANet-SPP-ASFF-RFB       41.1%       62.6%   44.4%                                            512x512    42.3    64.3    45.7
                                                                          (BoF-backbone)
                                                                          CSPResNeXt50-PANet-SPP
4.4. Influence of different backbones and pre-                                                               512x512    42.3    64.2    45.8
                                                                          (BoF-backbone + Mish)
     trained weightings on Detector training                              CSPDarknet53-PANet-SPP
                                                                                                             512x512    42.4    64.5    46.0
                                                                          (BoF-backbone)
                                                                          CSPDarknet53-PANet-SPP
                                                                                                             512x512    43.0    64.9    46.5
   Further on we study the influence of different backbone                (BoF-backbone + Mish)
models on the detector accuracy, as shown in Table 6. We
notice that the model characterized with the best classifica-            4.5. Influence of different mini-batch size on Detec-
tion accuracy is not always the best in terms of the detector                  tor training
accuracy.                                                                    Finally, we analyze the results obtained with models
                                                                         trained with different mini-batch sizes, and the results are
   First, although classification accuracy of CSPResNeXt-                shown in Table 7. From the results shown in Table 7, we
50 models trained with different features is higher compared             found that after adding BoF and BoS training strategies, the
to CSPDarknet53 models, the CSPDarknet53 model shows                     mini-batch size has almost no effect on the detector’s per-
higher accuracy in terms of object detection.                            formance. This result shows that after the introduction of
                                                                         BoF and BoS, it is no longer necessary to use expensive
   Second, using BoF and Mish for the CSPResNeXt50                       GPUs for training. In other words, anyone can use only a
classifier training increases its classification accuracy, but           conventional GPU to train an excellent detector.
further application of these pre-trained weightings for de-                Table 7: Using different mini-batch size for detector training.
tector training reduces the detector accuracy. However, us-                Model (without OA)                  Size     AP     AP50    AP75
ing BoF and Mish for the CSPDarknet53 classifier training                  CSPResNeXt50-PANet-SPP
increases the accuracy of both the classifier and the detector                                                  608     37.1   59.2    39.9
                                                                           (without BoF/BoS, mini-batch 4)
which uses this classifier pre-trained weightings. The net                 CSPResNeXt50-PANet-SPP
                                                                                                                608     38.4   60.6    41.6
result is that backbone CSPDarknet53 is more suitable for                  (without BoF/BoS, mini-batch 8)
the detector than for CSPResNeXt50.                                        CSPDarknet53-PANet-SPP
                                                                                                                512     41.6   64.1    45.0
                                                                           (with BoF/BoS, mini-batch 4)
                                                                           CSPDarknet53-PANet-SPP
   We observe that the CSPDarknet53 model demonstrates                                                          512     41.7   64.2    45.2
                                                                           (with BoF/BoS, mini-batch 8)
a greater ability to increase the detector accuracy owing to
various improvements.

                                                                    9
Figure 8: Comparison of the speed and accuracy of different object detectors. (Some articles stated the FPS of their detectors
for only one of the GPUs: Maxwell/Pascal/Volta)

5. Results                                                           6. Conclusions
                                                                         We offer a state-of-the-art detector which is faster (FPS)
   Comparison of the results obtained with other state-              and more accurate (MS COCO AP50...95 and AP50 ) than
of-the-art object detectors are shown in Figure 8. Our               all available alternative detectors. The detector described
YOLOv4 are located on the Pareto optimality curve and are            can be trained and used on a conventional GPU with 8-16
superior to the fastest and most accurate detectors in terms         GB-VRAM this makes its broad use possible. The original
of both speed and accuracy.                                          concept of one-stage anchor-based detectors has proven its
   Since different methods use GPUs of different architec-           viability. We have verified a large number of features, and
tures for inference time verification, we operate YOLOv4             selected for use such of them for improving the accuracy of
on commonly adopted GPUs of Maxwell, Pascal, and Volta               both the classifier and the detector. These features can be
architectures, and compare them with other state-of-the-art          used as best-practice for future studies and developments.
methods. Table 8 lists the frame rate comparison results of
using Maxwell GPU, and it can be GTX Titan X (Maxwell)               7. Acknowledgements
or Tesla M40 GPU. Table 9 lists the frame rate comparison               The authors wish to thank Glenn Jocher for the
results of using Pascal GPU, and it can be Titan X (Pascal),         ideas of Mosaic data augmentation, the selection of
Titan Xp, GTX 1080 Ti, or Tesla P100 GPU. As for Table               hyper-parameters by using genetic algorithms and solving
10, it lists the frame rate comparison results of using Volta        the grid sensitivity problem https://github.com/
GPU, and it can be Titan Volta or Tesla V100 GPU.                    ultralytics/yolov3.

                                                                10
Table 8: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (test-
dev 2017). (Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with
batch=1 without using tensorRT.)
 Method          Backbone           Size      FPS        AP       AP50     AP75       APS     APM     APL
                        YOLOv4: Optimal Speed and Accuracy of Object Detection
 YOLOv4          CSPDarknet-53 416    38 (M)     41.2%   62.8%     44.3%     20.4%            44.4%   56.0%
 YOLOv4          CSPDarknet-53 512    31 (M)    43.0%    64.9%     46.5%     24.3%            46.1%   55.2%
 YOLOv4          CSPDarknet-53 608    23 (M)     43.5%   65.7%     47.3%     26.7%            46.7%   53.3%
                 Learning Rich Features at High-Speed for Single-Shot Object Detection [84]
 LRF             VGG-16           300    76.9 (M)   32.0%      51.5%    33.8%     12.6%     34.9%     47.0%
 LRF             ResNet-101       300    52.6 (M)   34.3%      54.1%    36.6%     13.2%     38.2%     50.7%
 LRF             VGG-16           512    38.5 (M)   36.2%      56.6%    38.7%     19.0%     39.9%     48.8%
 LRF             ResNet-101       512    31.3 (M)   37.3%      58.5%    39.7%     19.7%     42.8%     50.1%
                   Receptive Field Block Net for Accurate and Fast Object Detection [47]
 RFBNet          VGG-16           300    66.7 (M)    30.3%    49.3%     31.8%     11.8%       31.9%   45.9%
 RFBNet          VGG-16           512    33.3 (M)    33.8%    54.2%     35.9%     16.2%       37.1%   47.4%
 RFBNet-E        VGG-16           512    30.3 (M)    34.4%    55.7%     36.4%     17.6%       37.0%   47.6%
                                  YOLOv3: An incremental improvement [63]
 YOLOv3          Darknet-53        320    45 (M)   28.2%     51.5%    29.7%           11.9%   30.6%   43.4%
 YOLOv3          Darknet-53        416    35 (M)   31.0%     55.3%    32.3%           15.2%   33.2%   42.8%
 YOLOv3          Darknet-53        608    20 (M)   33.0%     57.9%    34.4%           18.3%   35.4%   41.9%
 YOLOv3-SPP      Darknet-53        608    20 (M)   36.2%     60.6%    38.2%           20.6%   37.4%   46.1%
                                    SSD: Single shot multibox detector [50]
 SSD             VGG-16             300    43 (M)     25.1%     43.1%      25.8%       6.6%   25.9%   41.4%
 SSD             VGG-16             512    22 (M)     28.8%     48.5%      30.3%      10.9%   31.8%   43.5%
                      Single-shot refinement neural network for object detection [95]
 RefineDet       VGG-16           320    38.7 (M)    29.4%    49.2%     31.3%      10.0%      32.0%   44.4%
 RefineDet       VGG-16           512    22.3 (M)    33.0%    54.5%     35.5%      16.3%      36.3%   44.3%
             M2det: A single-shot object detector based on multi-level feature pyramid network [98]
 M2det          VGG-16              320     33.4 (M)    33.5%     52.4%     35.6%    14.4%    37.6%   47.6%
 M2det          ResNet-101          320     21.7 (M)    34.3%     53.5%     36.5%    14.8%    38.8%   47.9%
 M2det          VGG-16              512      18 (M)     37.6%     56.6%     40.5%    18.4%    43.4%   51.2%
 M2det          ResNet-101          512     15.8 (M)    38.8%     59.4%     41.7%    20.5%    43.9%   53.4%
 M2det          VGG-16              800     11.8 (M)    41.0%     59.7%     45.0%    22.1%    46.5%   53.8%
                          Parallel Feature Pyramid Network for Object Detection [34]
 PFPNet-R        VGG-16             320     33 (M)    31.8%    52.9%     33.6%       12%      35.5%   46.1%
 PFPNet-R        VGG-16             512     24 (M)    35.2%    57.6%     37.9%     18.7%      38.6%   45.9%

                                   Focal Loss for Dense Object Detection [45]
 RetinaNet       ResNet-50          500    13.9 (M)    32.5%    50.9%      34.8%      13.9%   35.8%   46.7%
 RetinaNet       ResNet-101         500    11.1 (M)    34.4%    53.1%      36.8%      14.7%   38.5%   49.1%
 RetinaNet       ResNet-50          800     6.5 (M)    35.7%    55.0%      38.5%      18.9%   38.9%   46.3%
 RetinaNet       ResNet-101         800     5.1 (M)    37.8%    57.5%      40.8%      20.2%   41.1%   49.2%
                 Feature Selective Anchor-Free Module for Single-Shot Object Detection [102]
 AB+FSAF         ResNet-101         800    5.6 (M)   40.9%     61.5%    44.0%     24.0%      44.2%    51.3%
 AB+FSAF         ResNeXt-101        800    2.8 (M)   42.9%     63.8%    46.3%     26.6%      46.2%    52.7%
                              CornerNet: Detecting objects as paired keypoints [37]
 CornerNet       Hourglass          512    4.4 (M)     40.5%      57.8%    45.3%      20.8%   44.8%   56.7%

                                                       11
Table 9: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (test-dev 2017).
(Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with batch=1 without using
tensorRT.)
 Method            Backbone                    Size      FPS       AP       AP50      AP75     APS     APM     APL
                            YOLOv4: Optimal Speed and Accuracy of Object Detection
 YOLOv4            CSPDarknet-53        416     54 (P)   41.2%     62.8%     44.3%             20.4%   44.4%   56.0%
 YOLOv4            CSPDarknet-53        512     43 (P)   43.0%     64.9%     46.5%             24.3%   46.1%   55.2%
 YOLOv4            CSPDarknet-53        608     33 (P)   43.5%     65.7%    47.3%              26.7%   46.7%   53.3%
                          CenterMask: Real-Time Anchor-Free Instance Segmentation [40]
 CenterMask-Lite   MobileNetV2-FPN      600×     50.0 (P)  30.2%       -        -      14.2%           31.9%   40.9%
 CenterMask-Lite   VoVNet-19-FPN        600×     43.5 (P)  35.9%       -        -      19.6%           38.0%   45.9%
 CenterMask-Lite   VoVNet-39-FPN        600×     35.7 (P)  40.7%       -        -      22.4%           43.2%   53.5%
                       Enriched Feature Guided Refinement Network for Object Detection [57]
 EFGRNet           VGG-16                 320     47.6 (P)  33.2%     53.4%    35.4%     13.4%         37.1%   47.9%
 EFGRNet           VG-G16                 512     25.7 (P)  37.5%     58.8%    40.4%     19.7%         41.6%   49.4%
 EFGRNet           ResNet-101             512     21.7 (P)  39.0%     58.8%    42.3%     17.8%         43.6%   54.5%
                                              Hierarchical Shot Detector [3]
 HSD               VGG-16                     320      40 (P)    33.5%     53.2%      36.1%    15.0%   35.0%   47.8%
 HSD               VGG-16                     512     23.3 (P)   38.8%     58.2%      42.5%    21.8%   41.9%   50.2%
 HSD               ResNet-101                 512     20.8 (P)   40.2%     59.4%      44.0%    20.0%   44.4%   54.9%
 HSD               ResNeXt-101                512     15.2 (P)   41.9%     61.1%      46.2%    21.8%   46.6%   57.0%
 HSD               ResNet-101                 768     10.9 (P)   42.3%     61.2%      46.9%    22.8%   47.3%   55.9%
                       Dynamic anchor feature selection for single-shot object detection [41]
 DAFS              VGG16                 512      35 (P)      33.8%     52.9%     36.9%      14.6%     37.0%   47.7%

                                         Soft Anchor-Point Object Detection [101]
 SAPD              ResNet-50                    -     14.9 (P)   41.7%     61.9%      44.6%    24.1%   44.6%   51.6%
 SAPD              ResNet-50-DCN                -     12.4 (P)   44.3%     64.4%      47.7%    25.5%   47.3%   57.0%
 SAPD              ResNet-101-DCN               -      9.1 (P)   46.0%     65.9%      49.6%    26.3%   49.2%   59.6%
                                         Region proposal by guided anchoring [82]
 RetinaNet         ResNet-50                    -     10.8 (P)   37.1%    56.9%       40.0%    20.1%   40.1%   48.0%
 Faster R-CNN      ResNet-50                    -     9.4 (P)    39.8%    59.2%       43.5%    21.8%   42.6%   50.7%
                              RepPoints: Point set representation for object detection [87]
 RPDet             ResNet-101                 -       10 (P)    41.0%      62.9%     44.3%     23.6%   44.1%   51.7%
 RPDet             ResNet-101-DCN             -        8 (P)    45.0%      66.1%     49.0%     26.6%   48.6%   57.5%
                          Libra R-CNN: Towards balanced learning for object detection [58]
 Libra R-CNN       ResNet-101              -      9.5 (P)   41.1%     62.1%      44.7%     23.4%       43.7%   52.5%
                       FreeAnchor: Learning to match anchors for visual object detection [96]
 FreeAnchor        ResNet-101              -      9.1 (P)   43.1%      62.2%     46.4%      24.5%      46.1%   54.8%
         RetinaMask: Learning to Predict Masks Improves State-of-The-Art Single-Shot Detection for Free [14]
 RetinaMask      ResNet-50-FPN            800×    8.1 (P)    39.4%    58.6%      42.3%    21.9%      42.0%     51.0%
 RetinaMask      ResNet-101-FPN           800×    6.9 (P)    41.4%    60.8%      44.6%    23.0%      44.5%     53.5%
 RetinaMask      ResNet-101-FPN-GN        800×    6.5 (P)    41.7%    61.7%      45.0%    23.5%      44.7%     52.8%
 RetinaMask      ResNeXt-101-FPN-GN       800×    4.3 (P)    42.6%    62.5%      46.0%    24.8%      45.6%     53.8%
                            Cascade R-CNN: Delving into high quality object detection [2]
 Cascade R-CNN     ResNet-101              -       8 (P)     42.8%     62.1%      46.3%        23.7%   45.5%   55.2%
                                   Centernet: Object detection with keypoint triplets [13]
 Centernet         Hourglass-52                 -      4.4 (P)    41.6%     59.4%      44.2%   22.5%   43.1%   54.1%
 Centernet         Hourglass-104                -      3.3 (P)    44.9%     62.4%      48.1%   25.6%   47.4%   57.4%
                               Scale-Aware Trident Networks for Object Detection [42]
 TridentNet        ResNet-101               -       2.7 (P)   42.7%    63.6%      46.5%        23.9%   46.6%   56.6%
 TridentNet        ResNet-101-DCN           -       1.3 (P)   46.8%    67.6%      51.5%        28.0%   51.2%   60.5%

                                                            12
Table 10: Comparison of the speed and accuracy of different object detectors on the MS COCO dataset (test-dev 2017).
(Real-time detectors with FPS 30 or higher are highlighted here. We compare the results with batch=1 without using
tensorRT.)
 Method                Backbone                  Size         FPS        AP       AP50      AP75     APS     APM     APL
                               YOLOv4: Optimal Speed and Accuracy of Object Detection
 YOLOv4                CSPDarknet-53     416       96 (V)    41.2%    62.8%     44.3%                20.4%   44.4%   56.0%
 YOLOv4                CSPDarknet-53     512       83 (V)    43.0%    64.9%     46.5%                24.3%   46.1%   55.2%
 YOLOv4                CSPDarknet-53     608       62 (V)    43.5%    65.7%     47.3%                26.7%   46.7%   53.3%
                                      EfficientDet: Scalable and Efficient Object Detection [77]
 EfficientDet-D0       Efficient-B0               512        62.5 (V)    33.8%     52.2%     35.8%   12.0%   38.3%   51.2%
 EfficientDet-D1       Efficient-B1               640        50.0 (V)    39.6%     58.6%     42.3%   17.9%   44.3%   56.0%
 EfficientDet-D2       Efficient-B2               768        41.7 (V)    43.0%     62.3%     46.2%   22.5%   47.0%   58.4%
 EfficientDet-D3       Efficient-B3               896        23.8 (V)    45.8%     65.0%     49.3%   26.6%   49.4%   59.8%
                                Learning Spatial Fusion for Single-Shot Object Detection [48]
 YOLOv3 + ASFF*        Darknet-53            320         60 (V)     38.1%    57.4%     42.1%         16.1%   41.6%   53.6%
 YOLOv3 + ASFF*        Darknet-53            416         54 (V)     40.6%    60.6%     45.1%         20.3%   44.2%   54.1%
 YOLOv3 + ASFF*        Darknet-53           608×        45.5 (V)    42.4%    63.0%     47.4%         25.5%   45.7%   52.3%
 YOLOv3 + ASFF*        Darknet-53           800×        29.4 (V)    43.9%    64.1%     49.2%         27.0%   46.6%   53.4%
                                           HarDNet: A Low Memory Traffic Network [4]
 RFBNet                HarDNet68                512      41.5 (V) 33.9%     54.3%    36.2%           14.7%   36.6%   50.5%
 RFBNet                HarDNet85                512      37.1 (V) 36.8%     57.1%    39.5%           16.9%   40.5%   52.9%
                                             Focal Loss for Dense Object Detection [45]
 RetinaNet             ResNet-50                  640        37 (V)    37.0%        -         -        -       -       -
 RetinaNet             ResNet-101                 640       29.4 (V)   37.9%        -         -        -       -       -
 RetinaNet             ResNet-50                 1024       19.6 (V)   40.1%        -         -        -       -       -
 RetinaNet             ResNet-101                1024       15.4 (V)   41.1%        -         -        -       -       -

                    SM-NAS: Structural-to-Modular Neural Architecture Search for Object Detection [88]
 SM-NAS: E2           -                   800×600    25.3 (V)   40.0%     58.2%     43.4%     21.1%    42.4%         51.7%
 SM-NAS: E3           -                   800×600    19.7 (V)   42.8%     61.2%     46.5%     23.5%    45.5%         55.6%
 SM-NAS: E5           -                  1333×800     9.3 (V)   45.9%     64.6%     49.6%     27.1%    49.0%         58.0%
                     NAS-FPN: Learning scalable feature pyramid architecture for object detection [17]
 NAS-FPN              ResNet-50             640       24.4 (V)   39.9%        -         -          -           -       -
 NAS-FPN              ResNet-50            1024       12.7 (V)   44.2%        -         -          -           -       -
     Bridging the Gap Between Anchor-based and Anchor-free Detection via Adaptive Training Sample Selection [94]
 ATSS               ResNet-101          800×      17.5 (V)    43.6%     62.1%     47.4%    26.1%    47.0%      53.6%
 ATSS               ResNet-101-DCN      800×      13.7 (V)    46.3%     64.7%     50.4%    27.7%    49.8%      58.4%
              RDSNet: A New Deep Architecture for Reciprocal Object Detection and Instance Segmentation [83]
 RDSNet               ResNet-101           600        16.8 (V)   36.0%     55.2%     38.7%    17.4%    39.6%         49.7%
 RDSNet               ResNet-101           800        10.9 (V)   38.1%     58.5%     40.8%    21.2%    41.5%         48.2%
                              CenterMask: Real-Time Anchor-Free Instance Segmentation [40]
 CenterMask            ResNet-101-FPN      800×      15.2 (V)   44.0%       -        -               25.8%   46.8%   54.9%
 CenterMask            VoVNet-99-FPN       800×      12.9 (V)   46.5%       -        -               28.7%   48.9%   57.2%

                                                                 13
References                                                             [14] Cheng-Yang Fu, Mykhailo Shvets, and Alexander C Berg.
                                                                            RetinaMask: Learning to predict masks improves state-
 [1] Navaneeth Bodla, Bharat Singh, Rama Chellappa, and                     of-the-art single-shot detection for free. arXiv preprint
     Larry S Davis. Soft-NMS–improving object detection with                arXiv:1901.03353, 2019. 12
     one line of code. In Proceedings of the IEEE International        [15] Robert Geirhos, Patricia Rubisch, Claudio Michaelis,
     Conference on Computer Vision (ICCV), pages 5561–5569,                 Matthias Bethge, Felix A Wichmann, and Wieland Brendel.
     2017. 4                                                                ImageNet-trained cnns are biased towards texture; increas-
 [2] Zhaowei Cai and Nuno Vasconcelos. Cascade R-CNN:                       ing shape bias improves accuracy and robustness. In Inter-
     Delving into high quality object detection. In Proceedings             national Conference on Learning Representations (ICLR),
     of the IEEE Conference on Computer Vision and Pattern                  2019. 3
     Recognition (CVPR), pages 6154–6162, 2018. 12                     [16] Golnaz Ghiasi, Tsung-Yi Lin, and Quoc V Le. DropBlock:
 [3] Jiale Cao, Yanwei Pang, Jungong Han, and Xuelong Li. Hi-               A regularization method for convolutional networks. In Ad-
     erarchical shot detector. In Proceedings of the IEEE In-               vances in Neural Information Processing Systems (NIPS),
     ternational Conference on Computer Vision (ICCV), pages                pages 10727–10737, 2018. 3
     9705–9714, 2019. 12                                               [17] Golnaz Ghiasi, Tsung-Yi Lin, and Quoc V Le. NAS-FPN:
 [4] Ping Chao, Chao-Yang Kao, Yu-Shan Ruan, Chien-Hsiang                   Learning scalable feature pyramid architecture for object
     Huang, and Youn-Long Lin. HarDNet: A low memory traf-                  detection. In Proceedings of the IEEE Conference on Com-
     fic network. Proceedings of the IEEE International Confer-             puter Vision and Pattern Recognition (CVPR), pages 7036–
     ence on Computer Vision (ICCV), 2019. 13                               7045, 2019. 2, 13
 [5] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,            [18] Ross Girshick. Fast R-CNN. In Proceedings of the IEEE In-
     Kevin Murphy, and Alan L Yuille. DeepLab: Semantic im-                 ternational Conference on Computer Vision (ICCV), pages
     age segmentation with deep convolutional nets, atrous con-             1440–1448, 2015. 2
     volution, and fully connected CRFs. IEEE Transactions             [19] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra
     on Pattern Analysis and Machine Intelligence (TPAMI),                  Malik. Rich feature hierarchies for accurate object de-
     40(4):834–848, 2017. 2, 4                                              tection and semantic segmentation. In Proceedings of the
 [6] Pengguang Chen. GridMask data augmentation. arXiv                      IEEE Conference on Computer Vision and Pattern Recog-
     preprint arXiv:2001.04086, 2020. 3                                     nition (CVPR), pages 580–587, 2014. 2, 4
 [7] Yukang Chen, Tong Yang, Xiangyu Zhang, Gaofeng Meng,              [20] Jianyuan Guo, Kai Han, Yunhe Wang, Chao Zhang, Zhao-
     Xinyu Xiao, and Jian Sun. DetNAS: Backbone search for                  hui Yang, Han Wu, Xinghao Chen, and Chang Xu. Hit-
     object detection. In Advances in Neural Information Pro-               Detector: Hierarchical trinity architecture search for object
     cessing Systems (NeurIPS), pages 6638–6648, 2019. 2                    detection. In Proceedings of the IEEE Conference on Com-
 [8] Jiwoong Choi, Dayoung Chun, Hyun Kim, and Hyuk-Jae                     puter Vision and Pattern Recognition (CVPR), 2020. 2
     Lee. Gaussian YOLOv3: An accurate and fast object de-             [21] Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing
     tector using localization uncertainty for autonomous driv-             Xu, and Chang Xu. GhostNet: More features from cheap
     ing. In Proceedings of the IEEE International Conference               operations. In Proceedings of the IEEE Conference on
     on Computer Vision (ICCV), pages 502–511, 2019. 7                      Computer Vision and Pattern Recognition (CVPR), 2020.
 [9] Jifeng Dai, Yi Li, Kaiming He, and Jian Sun. R-FCN:                    5
     Object detection via region-based fully convolutional net-        [22] Bharath Hariharan, Pablo Arbeláez, Ross Girshick, and
     works. In Advances in Neural Information Processing Sys-               Jitendra Malik. Hypercolumns for object segmentation
     tems (NIPS), pages 379–387, 2016. 2                                    and fine-grained localization. In Proceedings of the IEEE
[10] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,                 Conference on Computer Vision and Pattern Recognition
     and Li Fei-Fei. ImageNet: A large-scale hierarchical im-               (CVPR), pages 447–456, 2015. 4
     age database. In Proceedings of the IEEE Conference on            [23] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-
     Computer Vision and Pattern Recognition (CVPR), pages                  shick. Mask R-CNN. In Proceedings of the IEEE In-
     248–255, 2009. 5                                                       ternational Conference on Computer Vision (ICCV), pages
[11] Terrance DeVries and Graham W Taylor. Improved reg-                    2961–2969, 2017. 2
     ularization of convolutional neural networks with CutOut.         [24] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     arXiv preprint arXiv:1708.04552, 2017. 3                               Delving deep into rectifiers: Surpassing human-level per-
[12] Xianzhi Du, Tsung-Yi Lin, Pengchong Jin, Golnaz Ghiasi,                formance on ImageNet classification. In Proceedings of
     Mingxing Tan, Yin Cui, Quoc V Le, and Xiaodan Song.                    the IEEE International Conference on Computer Vision
     SpineNet: Learning scale-permuted backbone for recog-                  (ICCV), pages 1026–1034, 2015. 4
     nition and localization. arXiv preprint arXiv:1912.05027,         [25] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     2019. 2                                                                Spatial pyramid pooling in deep convolutional networks for
[13] Kaiwen Duan, Song Bai, Lingxi Xie, Honggang Qi, Qing-                  visual recognition. IEEE Transactions on Pattern Analy-
     ming Huang, and Qi Tian. CenterNet: Keypoint triplets for              sis and Machine Intelligence (TPAMI), 37(9):1904–1916,
     object detection. In Proceedings of the IEEE International             2015. 2, 4, 7
     Conference on Computer Vision (ICCV), pages 6569–6578,            [26] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     2019. 2, 12                                                            Deep residual learning for image recognition. In Proceed-

                                                                  14
     ings of the IEEE Conference on Computer Vision and Pat-            [40] Youngwan Lee and Jongyoul Park. CenterMask: Real-time
     tern Recognition (CVPR), pages 770–778, 2016. 2                         anchor-free instance segmentation. In Proceedings of the
[27] Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh                     IEEE Conference on Computer Vision and Pattern Recog-
     Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu,                    nition (CVPR), 2020. 12, 13
     Ruoming Pang, Vijay Vasudevan, et al. Searching for Mo-            [41] Shuai Li, Lingxiao Yang, Jianqiang Huang, Xian-Sheng
     bileNetV3. In Proceedings of the IEEE International Con-                Hua, and Lei Zhang. Dynamic anchor feature selection for
     ference on Computer Vision (ICCV), 2019. 2, 4                           single-shot object detection. In Proceedings of the IEEE In-
[28] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry                          ternational Conference on Computer Vision (ICCV), pages
     Kalenichenko, Weijun Wang, Tobias Weyand, Marco An-                     6609–6618, 2019. 12
     dreetto, and Hartwig Adam. MobileNets: Efficient con-              [42] Yanghao Li, Yuntao Chen, Naiyan Wang, and Zhaoxiang
     volutional neural networks for mobile vision applications.              Zhang. Scale-aware trident networks for object detection.
     arXiv preprint arXiv:1704.04861, 2017. 2, 4                             In Proceedings of the IEEE International Conference on
[29] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation                   Computer Vision (ICCV), pages 6054–6063, 2019. 12
     networks. In Proceedings of the IEEE Conference on Com-            [43] Zeming Li, Chao Peng, Gang Yu, Xiangyu Zhang, Yang-
     puter Vision and Pattern Recognition (CVPR), pages 7132–                dong Deng, and Jian Sun. DetNet: Design backbone for
     7141, 2018. 4                                                           object detection. In Proceedings of the European Confer-
[30] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kil-                 ence on Computer Vision (ECCV), pages 334–350, 2018.
     ian Q Weinberger. Densely connected convolutional net-                  2
     works. In Proceedings of the IEEE Conference on Com-               [44] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
     puter Vision and Pattern Recognition (CVPR), pages 4700–                Bharath Hariharan, and Serge Belongie. Feature pyramid
     4708, 2017. 2                                                           networks for object detection. In Proceedings of the IEEE
[31] Forrest N Iandola, Song Han, Matthew W Moskewicz,                       Conference on Computer Vision and Pattern Recognition
     Khalid Ashraf, William J Dally, and Kurt Keutzer.                       (CVPR), pages 2117–2125, 2017. 2
     SqueezeNet: AlexNet-level accuracy with 50x fewer pa-              [45] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He,
     rameters and¡ 0.5 MB model size.            arXiv preprint              and Piotr Dollár. Focal loss for dense object detection. In
     arXiv:1602.07360, 2016. 2                                               Proceedings of the IEEE International Conference on Com-
[32] Sergey Ioffe and Christian Szegedy. Batch normalization:                puter Vision (ICCV), pages 2980–2988, 2017. 2, 3, 11, 13
     Accelerating deep network training by reducing internal co-        [46] Tsung-Yi Lin, Michael Maire, Serge Belongie, James
     variate shift. arXiv preprint arXiv:1502.03167, 2015. 6                 Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and
[33] Md Amirul Islam, Shujon Naha, Mrigank Rochan, Neil                      C Lawrence Zitnick. Microsoft COCO: Common objects
     Bruce, and Yang Wang. Label refinement network for                      in context. In Proceedings of the European Conference on
     coarse-to-fine semantic segmentation.       arXiv preprint              Computer Vision (ECCV), pages 740–755, 2014. 5
     arXiv:1703.00551, 2017. 3                                          [47] Songtao Liu, Di Huang, et al. Receptive field block net for
[34] Seung-Wook Kim, Hyong-Keun Kook, Jee-Young Sun,                         accurate and fast object detection. In Proceedings of the
     Mun-Cheon Kang, and Sung-Jea Ko. Parallel feature pyra-                 European Conference on Computer Vision (ECCV), pages
     mid network for object detection. In Proceedings of the                 385–400, 2018. 2, 4, 11
     European Conference on Computer Vision (ECCV), pages               [48] Songtao Liu, Di Huang, and Yunhong Wang. Learning spa-
     234–250, 2018. 11                                                       tial fusion for single-shot object detection. arXiv preprint
[35] Günter Klambauer, Thomas Unterthiner, Andreas Mayr,                    arXiv:1911.09516, 2019. 2, 4, 13
     and Sepp Hochreiter. Self-normalizing neural networks.             [49] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.
     In Advances in Neural Information Processing Systems                    Path aggregation network for instance segmentation. In
     (NIPS), pages 971–980, 2017. 4                                          Proceedings of the IEEE Conference on Computer Vision
[36] Gustav Larsson, Michael Maire, and Gregory                              and Pattern Recognition (CVPR), pages 8759–8768, 2018.
     Shakhnarovich.        FractalNet: Ultra-deep neural net-                1, 2, 7
     works without residuals. arXiv preprint arXiv:1605.07648,          [50] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
     2016. 6                                                                 Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C
[37] Hei Law and Jia Deng. CornerNet: Detecting objects as                   Berg. SSD: Single shot multibox detector. In Proceedings
     paired keypoints. In Proceedings of the European Confer-                of the European Conference on Computer Vision (ECCV),
     ence on Computer Vision (ECCV), pages 734–750, 2018. 2,                 pages 21–37, 2016. 2, 11
     11                                                                 [51] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully
[38] Hei Law, Yun Teng, Olga Russakovsky, and Jia Deng.                      convolutional networks for semantic segmentation. In Pro-
     CornerNet-Lite: Efficient keypoint based object detection.              ceedings of the IEEE Conference on Computer Vision and
     arXiv preprint arXiv:1904.08900, 2019. 2                                Pattern Recognition (CVPR), pages 3431–3440, 2015. 4
[39] Svetlana Lazebnik, Cordelia Schmid, and Jean Ponce. Be-            [52] Ilya Loshchilov and Frank Hutter.          SGDR: Stochas-
     yond bags of features: Spatial pyramid matching for recog-              tic gradient descent with warm restarts. arXiv preprint
     nizing natural scene categories. In Proceedings of the IEEE             arXiv:1608.03983, 2016. 7
     Conference on Computer Vision and Pattern Recognition              [53] Ningning Ma, Xiangyu Zhang, Hai-Tao Zheng, and Jian
     (CVPR), volume 2, pages 2169–2178. IEEE, 2006. 4                        Sun. ShuffleNetV2: Practical guidelines for efficient cnn

                                                                   15
     architecture design. In Proceedings of the European Con-               of the IEEE Conference on Computer Vision and Pattern
     ference on Computer Vision (ECCV), pages 116–131, 2018.                Recognition (CVPR), pages 4510–4520, 2018. 2
     2                                                                 [67] Abhinav Shrivastava, Abhinav Gupta, and Ross Girshick.
[54] Andrew L Maas, Awni Y Hannun, and Andrew Y Ng. Rec-                    Training region-based object detectors with online hard ex-
     tifier nonlinearities improve neural network acoustic mod-             ample mining. In Proceedings of the IEEE Conference on
     els. In Proceedings of International Conference on Ma-                 Computer Vision and Pattern Recognition (CVPR), pages
     chine Learning (ICML), volume 30, page 3, 2013. 4                      761–769, 2016. 3
[55] Diganta Misra.          Mish: A self regularized non-             [68] Karen Simonyan and Andrew Zisserman. Very deep convo-
     monotonic neural activation function. arXiv preprint                   lutional networks for large-scale image recognition. arXiv
     arXiv:1908.08681, 2019. 4                                              preprint arXiv:1409.1556, 2014. 2
[56] Vinod Nair and Geoffrey E Hinton. Rectified linear units          [69] Krishna Kumar Singh, Hao Yu, Aron Sarmasi, Gautam
     improve restricted boltzmann machines. In Proceedings                  Pradeep, and Yong Jae Lee. Hide-and-Seek: A data aug-
     of International Conference on Machine Learning (ICML),                mentation technique for weakly-supervised localization and
     pages 807–814, 2010. 4                                                 beyond. arXiv preprint arXiv:1811.02545, 2018. 3
[57] Jing Nie, Rao Muhammad Anwer, Hisham Cholakkal, Fa-               [70] Saurabh Singh and Shankar Krishnan. Filter response
     had Shahbaz Khan, Yanwei Pang, and Ling Shao. Enriched                 normalization layer: Eliminating batch dependence in
     feature guided refinement network for object detection. In             the training of deep neural networks. arXiv preprint
     Proceedings of the IEEE International Conference on Com-               arXiv:1911.09737, 2019. 6
     puter Vision (ICCV), pages 9537–9546, 2019. 12                    [71] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya
[58] Jiangmiao Pang, Kai Chen, Jianping Shi, Huajun Feng,                   Sutskever, and Ruslan Salakhutdinov. DropOut: A simple
     Wanli Ouyang, and Dahua Lin. Libra R-CNN: Towards bal-                 way to prevent neural networks from overfitting. The jour-
     anced learning for object detection. In Proceedings of the             nal of machine learning research, 15(1):1929–1958, 2014.
     IEEE Conference on Computer Vision and Pattern Recog-                  3
     nition (CVPR), pages 821–830, 2019. 2, 12                         [72] K-K Sung and Tomaso Poggio. Example-based learning
                                                                            for view-based human face detection. IEEE Transactions
[59] Prajit Ramachandran, Barret Zoph, and Quoc V Le.
                                                                            on Pattern Analysis and Machine Intelligence (TPAMI),
     Searching for activation functions.         arXiv preprint
                                                                            20(1):39–51, 1998. 3
     arXiv:1710.05941, 2017. 4
                                                                       [73] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon
[60] Abdullah Rashwan, Agastya Kalra, and Pascal Poupart.
                                                                            Shlens, and Zbigniew Wojna. Rethinking the inception ar-
     Matrix Nets: A new deep architecture for object detection.
                                                                            chitecture for computer vision. In Proceedings of the IEEE
     In Proceedings of the IEEE International Conference on
                                                                            Conference on Computer Vision and Pattern Recognition
     Computer Vision Workshop (ICCV Workshop), pages 0–0,
                                                                            (CVPR), pages 2818–2826, 2016. 3
     2019. 2
                                                                       [74] Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan,
[61] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali                 Mark Sandler, Andrew Howard, and Quoc V Le. MNAS-
     Farhadi. You only look once: Unified, real-time object de-             net: Platform-aware neural architecture search for mobile.
     tection. In Proceedings of the IEEE Conference on Com-                 In Proceedings of the IEEE Conference on Computer Vision
     puter Vision and Pattern Recognition (CVPR), pages 779–                and Pattern Recognition (CVPR), pages 2820–2828, 2019.
     788, 2016. 2                                                           2
[62] Joseph Redmon and Ali Farhadi. YOLO9000: better, faster,          [75] Mingxing Tan and Quoc V Le. EfficientNet: Rethinking
     stronger. In Proceedings of the IEEE Conference on Com-                model scaling for convolutional neural networks. In Pro-
     puter Vision and Pattern Recognition (CVPR), pages 7263–               ceedings of International Conference on Machine Learning
     7271, 2017. 2                                                          (ICML), 2019. 2
[63] Joseph Redmon and Ali Farhadi. YOLOv3: An incremental             [76] Mingxing Tan and Quoc V Le. MixNet: Mixed depthwise
     improvement. arXiv preprint arXiv:1804.02767, 2018. 2,                 convolutional kernels. In Proceedings of the British Ma-
     4, 7, 11                                                               chine Vision Conference (BMVC), 2019. 5
[64] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.            [77] Mingxing Tan, Ruoming Pang, and Quoc V Le. Efficient-
     Faster R-CNN: Towards real-time object detection with re-              Det: Scalable and efficient object detection. In Proceedings
     gion proposal networks. In Advances in Neural Information              of the IEEE Conference on Computer Vision and Pattern
     Processing Systems (NIPS), pages 91–99, 2015. 2                        Recognition (CVPR), 2020. 2, 4, 13
[65] Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak, Amir               [78] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:
     Sadeghian, Ian Reid, and Silvio Savarese. Generalized in-              Fully convolutional one-stage object detection. In Proceed-
     tersection over union: A metric and a loss for bounding                ings of the IEEE International Conference on Computer Vi-
     box regression. In Proceedings of the IEEE Conference on               sion (ICCV), pages 9627–9636, 2019. 2
     Computer Vision and Pattern Recognition (CVPR), pages             [79] Jonathan Tompson, Ross Goroshin, Arjun Jain, Yann Le-
     658–666, 2019. 3                                                       Cun, and Christoph Bregler. Efficient object localization
[66] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey                      using convolutional networks. In Proceedings of the IEEE
     Zhmoginov, and Liang-Chieh Chen. MobileNetV2: In-                      Conference on Computer Vision and Pattern Recognition
     verted residuals and linear bottlenecks. In Proceedings                (CVPR), pages 648–656, 2015. 6

                                                                  16
[80] Li Wan, Matthew Zeiler, Sixin Zhang, Yann Le Cun, and                    [93] Hang Zhang, Kristin Dana, Jianping Shi, Zhongyue Zhang,
     Rob Fergus. Regularization of neural networks using Drop-                     Xiaogang Wang, Ambrish Tyagi, and Amit Agrawal. Con-
     Connect. In Proceedings of International Conference on                        text encoding for semantic segmentation. In Proceedings
     Machine Learning (ICML), pages 1058–1066, 2013. 3                             of the IEEE Conference on Computer Vision and Pattern
[81] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,                             Recognition (CVPR), pages 7151–7160, 2018. 6
     Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. CSPNet:                    [94] Shifeng Zhang, Cheng Chi, Yongqiang Yao, Zhen Lei, and
     A new backbone that can enhance learning capability of                        Stan Z Li. Bridging the gap between anchor-based and
     cnn. Proceedings of the IEEE Conference on Computer Vi-                       anchor-free detection via adaptive training sample selec-
     sion and Pattern Recognition Workshop (CVPR Workshop),                        tion. In Proceedings of the IEEE Conference on Computer
     2020. 2, 7                                                                    Vision and Pattern Recognition (CVPR), 2020. 13
[82] Jiaqi Wang, Kai Chen, Shuo Yang, Chen Change Loy, and                    [95] Shifeng Zhang, Longyin Wen, Xiao Bian, Zhen Lei, and
     Dahua Lin. Region proposal by guided anchoring. In Pro-                       Stan Z Li. Single-shot refinement neural network for ob-
     ceedings of the IEEE Conference on Computer Vision and                        ject detection. In Proceedings of the IEEE Conference on
     Pattern Recognition (CVPR), pages 2965–2974, 2019. 12                         Computer Vision and Pattern Recognition (CVPR), pages
[83] Shaoru Wang, Yongchao Gong, Junliang Xing, Lichao                             4203–4212, 2018. 11
     Huang, Chang Huang, and Weiming Hu. RDSNet: A                            [96] Xiaosong Zhang, Fang Wan, Chang Liu, Rongrong Ji, and
     new deep architecture for reciprocal object detection and                     Qixiang Ye. FreeAnchor: Learning to match anchors for
     instance segmentation. arXiv preprint arXiv:1912.05070,                       visual object detection. In Advances in Neural Information
     2019. 13                                                                      Processing Systems (NeurIPS), 2019. 12
[84] Tiancai Wang, Rao Muhammad Anwer, Hisham Cholakkal,                      [97] Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, and Jian Sun.
     Fahad Shahbaz Khan, Yanwei Pang, and Ling Shao. Learn-                        ShuffleNet: An extremely efficient convolutional neural
     ing rich features at high-speed for single-shot object detec-                 network for mobile devices. In Proceedings of the IEEE
     tion. In Proceedings of the IEEE International Conference                     Conference on Computer Vision and Pattern Recognition
     on Computer Vision (ICCV), pages 1971–1980, 2019. 11                          (CVPR), pages 6848–6856, 2018. 2
[85] Sanghyun Woo, Jongchan Park, Joon-Young Lee, and In                      [98] Qijie Zhao, Tao Sheng, Yongtao Wang, Zhi Tang, Ying
     So Kweon. CBAM: Convolutional block attention module.                         Chen, Ling Cai, and Haibin Ling. M2det: A single-shot
     In Proceedings of the European Conference on Computer                         object detector based on multi-level feature pyramid net-
     Vision (ECCV), pages 3–19, 2018. 1, 2, 4                                      work. In Proceedings of the AAAI Conference on Artificial
[86] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and                    Intelligence (AAAI), volume 33, pages 9259–9266, 2019. 2,
     Kaiming He. Aggregated residual transformations for deep                      4, 11
     neural networks. In Proceedings of the IEEE Conference on                [99] Zhaohui Zheng, Ping Wang, Wei Liu, Jinze Li, Rongguang
     Computer Vision and Pattern Recognition (CVPR), pages                         Ye, and Dongwei Ren. Distance-IoU Loss: Faster and bet-
     1492–1500, 2017. 2                                                            ter learning for bounding box regression. In Proceedings
[87] Ze Yang, Shaohui Liu, Han Hu, Liwei Wang, and Stephen                         of the AAAI Conference on Artificial Intelligence (AAAI),
     Lin. RepPoints: Point set representation for object detec-                    2020. 3, 4
     tion. In Proceedings of the IEEE International Conference               [100] Zhun Zhong, Liang Zheng, Guoliang Kang, Shaozi Li,
     on Computer Vision (ICCV), pages 9657–9666, 2019. 2, 12                       and Yi Yang. Random erasing data augmentation. arXiv
[88] Lewei Yao, Hang Xu, Wei Zhang, Xiaodan Liang, and                             preprint arXiv:1708.04896, 2017. 3
     Zhenguo Li. SM-NAS: Structural-to-modular neural archi-
                                                                             [101] Chenchen Zhu, Fangyi Chen, Zhiqiang Shen, and Mar-
     tecture search for object detection. In Proceedings of the
                                                                                   ios Savvides. Soft anchor-point object detection. arXiv
     AAAI Conference on Artificial Intelligence (AAAI), 2020.
                                                                                   preprint arXiv:1911.12448, 2019. 12
     13
                                                                             [102] Chenchen Zhu, Yihui He, and Marios Savvides. Feature se-
[89] Zhuliang Yao, Yue Cao, Shuxin Zheng, Gao Huang, and
                                                                                   lective anchor-free module for single-shot object detection.
     Stephen Lin. Cross-iteration batch normalization. arXiv
                                                                                   In Proceedings of the IEEE Conference on Computer Vision
     preprint arXiv:2002.05712, 2020. 1, 6
                                                                                   and Pattern Recognition (CVPR), pages 840–849, 2019. 11
[90] Jiahui Yu, Yuning Jiang, Zhangyang Wang, Zhimin Cao,
     and Thomas Huang. UnitBox: An advanced object detec-
     tion network. In Proceedings of the 24th ACM international
     conference on Multimedia, pages 516–520, 2016. 3
[91] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk
     Chun, Junsuk Choe, and Youngjoon Yoo. CutMix: Regu-
     larization strategy to train strong classifiers with localizable
     features. In Proceedings of the IEEE International Confer-
     ence on Computer Vision (ICCV), pages 6023–6032, 2019.
     3
[92] Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and
     David Lopez-Paz. MixUp: Beyond empirical risk mini-
     mization. arXiv preprint arXiv:1710.09412, 2017. 3

                                                                        17
