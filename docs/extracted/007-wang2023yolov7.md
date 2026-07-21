---
source_id: 007
bibtex_key: wang2023yolov7
title: YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors
year: 2023 (pracetak arXiv Juli 2022)
domain_theme: Fondasi RGB
verified_pdf: 7_YOLOv7.pdf
char_count: 95789
---

YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object
                                                                         detectors

                                                             Chien-Yao Wang1 , Alexey Bochkovskiy, and Hong-Yuan Mark Liao1
                                                                 1
                                                                   Institute of Information Science, Academia Sinica, Taiwan
                                                    kinyiu@iis.sinica.edu.tw, alexeyab84@gmail.com, and liao@iis.sinica.edu.tw

                                                                 Abstract
arXiv:2207.02696v1 [cs.CV] 6 Jul 2022

                                           YOLOv7 surpasses all known object detectors in both
                                        speed and accuracy in the range from 5 FPS to 160 FPS
                                        and has the highest accuracy 56.8% AP among all known
                                        real-time object detectors with 30 FPS or higher on GPU
                                        V100. YOLOv7-E6 object detector (56 FPS V100, 55.9%
                                        AP) outperforms both transformer-based detector SWIN-
                                        L Cascade-Mask R-CNN (9.2 FPS A100, 53.9% AP) by
                                        509% in speed and 2% in accuracy, and convolutional-
                                        based detector ConvNeXt-XL Cascade-Mask R-CNN (8.6
                                        FPS A100, 55.2% AP) by 551% in speed and 0.7% AP
                                        in accuracy, as well as YOLOv7 outperforms: YOLOR,
                                        YOLOX, Scaled-YOLOv4, YOLOv5, DETR, Deformable
                                        DETR, DINO-5scale-R50, ViT-Adapter-B and many other
                                        object detectors in speed and accuracy. Moreover, we train            Figure 1: Comparison with other real-time object detectors, our
                                        YOLOv7 only on MS COCO dataset from scratch without                   proposed methods achieve state-of-the-arts performance.
                                        using any other datasets or pre-trained weights. Source
                                        code is released in https:// github.com/ WongKinYiu/ yolov7.
                                                                                                              opment of MCUNet [49, 48] and NanoDet [54] focused on
                                                                                                              producing low-power single-chip and improving the infer-
                                        1. Introduction                                                       ence speed on edge CPU. As for methods such as YOLOX
                                            Real-time object detection is a very important topic in           [21] and YOLOR [81], they focus on improving the infer-
                                        computer vision, as it is often a necessary component in              ence speed of various GPUs. More recently, the develop-
                                        computer vision systems. For example, multi-object track-             ment of real-time object detector has focused on the de-
                                        ing [94, 93], autonomous driving [40, 18], robotics [35, 58],         sign of efficient architecture. As for real-time object de-
                                        medical image analysis [34, 46], etc. The computing de-               tectors that can be used on CPU [54, 88, 84, 83], their de-
                                        vices that execute real-time object detection is usually some         sign is mostly based on MobileNet [28, 66, 27], ShuffleNet
                                        mobile CPU or GPU, as well as various neural processing               [92, 55], or GhostNet [25]. Another mainstream real-time
                                        units (NPU) developed by major manufacturers. For exam-               object detectors are developed for GPU [81, 21, 97], they
                                        ple, the Apple neural engine (Apple), the neural compute              mostly use ResNet [26], DarkNet [63], or DLA [87], and
                                        stick (Intel), Jetson AI edge devices (Nvidia), the edge TPU          then use the CSPNet [80] strategy to optimize the architec-
                                        (Google), the neural processing engine (Qualcomm), the AI             ture. The development direction of the proposed methods in
                                        processing unit (MediaTek), and the AI SoCs (Kneron), are             this paper are different from that of the current mainstream
                                        all NPUs. Some of the above mentioned edge devices focus              real-time object detectors. In addition to architecture op-
                                        on speeding up different operations such as vanilla convolu-          timization, our proposed methods will focus on the opti-
                                        tion, depth-wise convolution, or MLP operations. In this pa-          mization of the training process. Our focus will be on some
                                        per, the real-time object detector we proposed mainly hopes           optimized modules and optimization methods which may
                                        that it can support both mobile GPU and GPU devices from              strengthen the training cost for improving the accuracy of
                                        the edge to the cloud.                                                object detection, but without increasing the inference cost.
                                            In recent years, the real-time object detector is still de-       We call the proposed modules and optimization methods
                                        veloped for different edge device. For example, the devel-            trainable bag-of-freebies.

                                                                                                          1
   Recently, model re-parameterization [13, 12, 29] and dy-            2.2. Model re-parameterization
namic label assignment [20, 17, 42] have become important
                                                                           Model re-parametrization techniques [71, 31, 75, 19, 33,
topics in network training and object detection. Mainly af-
                                                                       11, 4, 24, 13, 12, 10, 29, 14, 78] merge multiple compu-
ter the above new concepts are proposed, the training of
                                                                       tational modules into one at inference stage. The model
object detector evolves many new issues. In this paper, we
                                                                       re-parameterization technique can be regarded as an en-
will present some of the new issues we have discovered and
                                                                       semble technique, and we can divide it into two cate-
devise effective methods to address them. For model re-
                                                                       gories, i.e., module-level ensemble and model-level ensem-
parameterization, we analyze the model re-parameterization
                                                                       ble. There are two common practices for model-level re-
strategies applicable to layers in different networks with the
                                                                       parameterization to obtain the final inference model. One
concept of gradient propagation path, and propose planned
                                                                       is to train multiple identical models with different train-
re-parameterized model. In addition, when we discover that
                                                                       ing data, and then average the weights of multiple trained
with dynamic label assignment technology, the training of
                                                                       models. The other is to perform a weighted average of the
model with multiple output layers will generate new issues.
                                                                       weights of models at different iteration number. Module-
That is: “How to assign dynamic targets for the outputs of
                                                                       level re-parameterization is a more popular research issue
different branches?” For this problem, we propose a new
                                                                       recently. This type of method splits a module into multi-
label assignment method called coarse-to-fine lead guided
                                                                       ple identical or different module branches during training
label assignment.
                                                                       and integrates multiple branched modules into a completely
   The contributions of this paper are summarized as fol-              equivalent module during inference. However, not all pro-
lows: (1) we design several trainable bag-of-freebies meth-            posed re-parameterized module can be perfectly applied to
ods, so that real-time object detection can greatly improve            different architectures. With this in mind, we have devel-
the detection accuracy without increasing the inference                oped new re-parameterization module and designed related
cost; (2) for the evolution of object detection methods, we            application strategies for various architectures.
found two new issues, namely how re-parameterized mod-
ule replaces original module, and how dynamic label as-                2.3. Model scaling
signment strategy deals with assignment to different output
                                                                           Model scaling [72, 60, 74, 73, 15, 16, 2, 51] is a way
layers. In addition, we also propose methods to address the
                                                                       to scale up or down an already designed model and make
difficulties arising from these issues; (3) we propose “ex-
                                                                       it fit in different computing devices. The model scaling
tend” and “compound scaling” methods for the real-time
                                                                       method usually uses different scaling factors, such as reso-
object detector that can effectively utilize parameters and
                                                                       lution (size of input image), depth (number of layer), width
computation; and (4) the method we proposed can effec-
                                                                       (number of channel), and stage (number of feature pyra-
tively reduce about 40% parameters and 50% computation
                                                                       mid), so as to achieve a good trade-off for the amount of
of state-of-the-art real-time object detector, and has faster
                                                                       network parameters, computation, inference speed, and ac-
inference speed and higher detection accuracy.
                                                                       curacy. Network architecture search (NAS) is one of the
                                                                       commonly used model scaling methods. NAS can automat-
2. Related work                                                        ically search for suitable scaling factors from search space
2.1. Real-time object detectors                                        without defining too complicated rules. The disadvantage
                                                                       of NAS is that it requires very expensive computation to
    Currently state-of-the-art real-time object detectors are          complete the search for model scaling factors. In [15], the
mainly based on YOLO [61, 62, 63] and FCOS [76, 77],                   researcher analyzes the relationship between scaling factors
which are [3, 79, 81, 21, 54, 85, 23]. Being able to become            and the amount of parameters and operations, trying to di-
a state-of-the-art real-time object detector usually requires          rectly estimate some rules, and thereby obtain the scaling
the following characteristics: (1) a faster and stronger net-          factors required by model scaling. Checking the literature,
work architecture; (2) a more effective feature integration            we found that almost all model scaling methods analyze in-
method [22, 97, 37, 74, 59, 30, 9, 45]; (3) a more accurate            dividual scaling factor independently, and even the methods
detection method [76, 77, 69]; (4) a more robust loss func-            in the compound scaling category also optimized scaling
tion [96, 64, 6, 56, 95, 57]; (5) a more efficient label assign-       factor independently. The reason for this is because most
ment method [99, 20, 17, 82, 42]; and (6) a more efficient             popular NAS architectures deal with scaling factors that are
training method. In this paper, we do not intend to explore            not very correlated. We observed that all concatenation-
self-supervised learning or knowledge distillation methods             based models, such as DenseNet [32] or VoVNet [39], will
that require additional data or large model. Instead, we will          change the input width of some layers when the depth of
design new trainable bag-of-freebies method for the issues             such models is scaled. Since the proposed architecture is
derived from the state-of-the-art methods associated with              concatenation-based, we have to design a new compound
(4), (5), and (6) mentioned above.                                     scaling method for this model.

                                                                   2
Figure 2: Extended efficient layer aggregation networks. The proposed extended ELAN (E-ELAN) does not change the gradient transmis-
sion path of the original architecture at all, but use group convolution to increase the cardinality of the added features, and combine the
features of different groups in a shuffle and merge cardinality manner. This way of operation can enhance the features learned by different
feature maps and improve the use of parameters and calculations.

3. Architecture                                                         E-ELAN uses expand, shuffle, merge cardinality to achieve
                                                                        the ability to continuously enhance the learning ability of
3.1. Extended efficient layer aggregation networks                      the network without destroying the original gradient path.
                                                                        In terms of architecture, E-ELAN only changes the archi-
    In most of the literature on designing the efficient ar-            tecture in computational block, while the architecture of
chitectures, the main considerations are no more than the               transition layer is completely unchanged. Our strategy is
number of parameters, the amount of computation, and the                to use group convolution to expand the channel and car-
computational density. Starting from the characteristics of             dinality of computational blocks. We will apply the same
memory access cost, Ma et al. [55] also analyzed the in-                group parameter and channel multiplier to all the compu-
fluence of the input/output channel ratio, the number of                tational blocks of a computational layer. Then, the feature
branches of the architecture, and the element-wise opera-               map calculated by each computational block will be shuf-
tion on the network inference speed. Dollár et al. [15] addi-          fled into g groups according to the set group parameter g,
tionally considered activation when performing model scal-              and then concatenate them together. At this time, the num-
ing, that is, to put more consideration on the number of el-            ber of channels in each group of feature map will be the
ements in the output tensors of convolutional layers. The               same as the number of channels in the original architec-
design of CSPVoVNet [79] in Figure 2 (b) is a variation of              ture. Finally, we add g groups of feature maps to perform
VoVNet [39]. In addition to considering the aforementioned              merge cardinality. In addition to maintaining the original
basic designing concerns, the architecture of CSPVoVNet                 ELAN design architecture, E-ELAN can also guide differ-
[79] also analyzes the gradient path, in order to enable the            ent groups of computational blocks to learn more diverse
weights of different layers to learn more diverse features.             features.
The gradient analysis approach described above makes in-
ferences faster and more accurate. ELAN [1] in Figure 2 (c)
considers the following design strategy – “How to design an             3.2. Model scaling for concatenation-based models
efficient network?.” They came out with a conclusion: By                    The main purpose of model scaling is to adjust some at-
controlling the shortest longest gradient path, a deeper net-           tributes of the model and generate models of different scales
work can learn and converge effectively. In this paper, we              to meet the needs of different inference speeds. For ex-
propose Extended-ELAN (E-ELAN) based on ELAN and                        ample the scaling model of EfficientNet [72] considers the
its main architecture is shown in Figure 2 (d).                         width, depth, and resolution. As for the scaled-YOLOv4
   Regardless of the gradient path length and the stacking              [79], its scaling model is to adjust the number of stages. In
number of computational blocks in large-scale ELAN, it has              [15], Dollár et al. analyzed the influence of vanilla convolu-
reached a stable state. If more computational blocks are                tion and group convolution on the amount of parameter and
stacked unlimitedly, this stable state may be destroyed, and            computation when performing width and depth scaling, and
the parameter utilization rate will decrease. The proposed              used this to design the corresponding model scaling method.

                                                                    3
Figure 3: Model scaling for concatenation-based models. From (a) to (b), we observe that when depth scaling is performed on
concatenation-based models, the output width of a computational block also increases. This phenomenon will cause the input width
of the subsequent transmission layer to increase. Therefore, we propose (c), that is, when performing model scaling on concatenation-
based models, only the depth in a computational block needs to be scaled, and the remaining of transmission layer is performed with
corresponding width scaling.

The above methods are mainly used in architectures such as
PlainNet or ResNet. When these architectures are in execut-
ing scaling up or scaling down, the in-degree and out-degree
of each layer will not change, so we can independently an-
alyze the impact of each scaling factor on the amount of
parameters and computation. However, if these methods
are applied to the concatenation-based architecture, we will
find that when scaling up or scaling down is performed on
depth, the in-degree of a translation layer which is immedi-
ately after a concatenation-based computational block will
decrease or increase, as shown in Figure 3 (a) and (b).
   It can be inferred from the above phenomenon that
we cannot analyze different scaling factors separately for
a concatenation-based model but must be considered to-
gether. Take scaling-up depth as an example, such an ac-
tion will cause a ratio change between the input channel and         Figure 4: Planned re-parameterized model. In the proposed
output channel of a transition layer, which may lead to a de-        planned re-parameterized model, we found that a layer with resid-
crease in the hardware usage of the model. Therefore, we             ual or concatenation connections, its RepConv should not have
must propose the corresponding compound model scaling                identity connection. Under these circumstances, it can be replaced
method for a concatenation-based model. When we scale                by RepConvN that contains no identity connections.
the depth factor of a computational block, we must also cal-
culate the change of the output channel of that block. Then,             RepConv actually combines 3 × 3 convolution, 1 × 1
we will perform width factor scaling with the same amount            convolution, and identity connection in one convolutional
of change on the transition layers, and the result is shown          layer. After analyzing the combination and correspond-
in Figure 3 (c). Our proposed compound scaling method                ing performance of RepConv and different architectures,
can maintain the properties that the model had at the initial        we find that the identity connection in RepConv destroys
design and maintains the optimal structure.                          the residual in ResNet and the concatenation in DenseNet,
                                                                     which provides more diversity of gradients for different fea-
4. Trainable bag-of-freebies                                         ture maps. For the above reasons, we use RepConv with-
                                                                     out identity connection (RepConvN) to design the architec-
4.1. Planned re-parameterized convolution
                                                                     ture of planned re-parameterized convolution. In our think-
    Although RepConv [13] has achieved excellent perfor-             ing, when a convolutional layer with residual or concate-
mance on the VGG [68], when we directly apply it to                  nation is replaced by re-parameterized convolution, there
ResNet [26] and DenseNet [32] and other architectures,               should be no identity connection. Figure 4 shows an exam-
its accuracy will be significantly reduced. We use gradi-            ple of our designed “planned re-parameterized convolution”
ent flow propagation paths to analyze how re-parameterized           used in PlainNet and ResNet. As for the complete planned
convolution should be combined with different network.               re-parameterized convolution experiment in residual-based
We also designed planned re-parameterized convolution ac-            model and concatenation-based model, it will be presented
cordingly.                                                           in the ablation study session.

                                                                 4
Figure 5: Coarse for auxiliary and fine for lead head label assigner. Compare with normal model (a), the schema in (b) has auxiliary head.
Different from the usual independent label assigner (c), we propose (d) lead head guided label assigner and (e) coarse-to-fine lead head
guided label assigner. The proposed label assigner is optimized by lead head prediction and the ground truth to get the labels of training
lead head and auxiliary head at the same time. The detailed coarse-to-fine implementation method and constraint design details will be
elaborated in Apendix.

4.2. Coarse for auxiliary and fine for lead loss                         to execute label assignment. The method proposed in this
                                                                         paper is a new label assignment method that guides both
    Deep supervision [38] is a technique that is often used              auxiliary head and lead head by the lead head prediction.
in training deep networks. Its main concept is to add                    In other words, we use lead head prediction as guidance to
extra auxiliary head in the middle layers of the network,                generate coarse-to-fine hierarchical labels, which are used
and the shallow network weights with assistant loss as the               for auxiliary head and lead head learning, respectively. The
guide. Even for architectures such as ResNet [26] and                    two proposed deep supervision label assignment strategies
DenseNet [32] which usually converge well, deep supervi-                 are shown in Figure 5 (d) and (e), respectively.
sion [70, 98, 67, 47, 82, 65, 86, 50] can still significantly
improve the performance of the model on many tasks. Fig-                     Lead head guided label assigner is mainly calculated
ure 5 (a) and (b) show, respectively, the object detector ar-            based on the prediction result of the lead head and the
chitecture “without” and “with” deep supervision. In this                ground truth, and generate soft label through the optimiza-
paper, we call the head responsible for the final output as              tion process. This set of soft labels will be used as the tar-
the lead head, and the head used to assist training is called            get training model for both auxiliary head and lead head.
auxiliary head.                                                          The reason to do this is because lead head has a relatively
    Next we want to discuss the issue of label assignment. In            strong learning capability, so the soft label generated from it
the past, in the training of deep network, label assignment              should be more representative of the distribution and corre-
usually refers directly to the ground truth and generate hard            lation between the source data and the target. Furthermore,
label according to the given rules. However, in recent years,            we can view such learning as a kind of generalized residual
if we take object detection as an example, researchers often             learning. By letting the shallower auxiliary head directly
use the quality and distribution of prediction output by the             learn the information that lead head has learned, lead head
network, and then consider together with the ground truth to             will be more able to focus on learning residual information
use some calculation and optimization methods to generate                that has not yet been learned.
a reliable soft label [61, 8, 36, 99, 91, 44, 43, 90, 20, 17, 42].           Coarse-to-fine lead head guided label assigner also
For example, YOLO [61] use IoU of prediction of bounding                 used the predicted result of the lead head and the ground
box regression and ground truth as the soft label of object-             truth to generate soft label. However, in the process we gen-
ness. In this paper, we call the mechanism that considers                erate two different sets of soft label, i.e., coarse label and
the network prediction results together with the ground truth            fine label, where fine label is the same as the soft label gen-
and then assigns soft labels as “label assigner.”                        erated by lead head guided label assigner, and coarse label
    Deep supervision needs to be trained on the target ob-               is generated by allowing more grids to be treated as posi-
jectives regardless of the circumstances of auxiliary head or            tive target by relaxing the constraints of the positive sample
lead head. During the development of soft label assigner re-             assignment process. The reason for this is that the learning
lated techniques, we accidentally discovered a new deriva-               ability of an auxiliary head is not as strong as that of a lead
tive issue, i.e., “How to assign soft label to auxiliary head            head, and in order to avoid losing the information that needs
and lead head ?” To the best of our knowledge, the relevant              to be learned, we will focus on optimizing the recall of aux-
literature has not explored this issue so far. The results of            iliary head in the object detection task. As for the output
the most popular method at present is as shown in Figure 5               of lead head, we can filter the high precision results from
(c), which is to separate auxiliary head and lead head, and              the high recall results as the final output. However, we must
then use their own prediction results and the ground truth               note that if the additional weight of coarse label is close to

                                                                     5
                                        Table 1: Comparison of baseline object detectors.
             Model                  #Param.    FLOPs     Size   APval     APval
                                                                            50     APval
                                                                                     75     APval
                                                                                              S     APval
                                                                                                      M     APval
                                                                                                              L
             YOLOv4 [3]              64.4M     142.8G    640    49.7%     68.2%    54.3%    32.9%   54.8%   63.7%
             YOLOR-u5 (r6.1) [81]    46.5M     109.1G    640    50.2%     68.7%    54.6%    33.2%   55.5%   63.7%
             YOLOv4-CSP [79]         52.9M     120.4G    640    50.3%     68.6%    54.9%    34.2%   55.6%   65.1%
             YOLOR-CSP [81]          52.9M     120.4G    640    50.8%     69.5%    55.3%    33.7%   56.0%   65.4%
             YOLOv7                  36.9M     104.7G    640    51.2%     69.7%    55.5%    35.2%   56.0%   66.7%
             improvement             -43%       -15%      -      +0.4      +0.2     +0.2     +1.5     =      +1.3
             YOLOR-CSP-X [81]        96.9M     226.8G    640    52.7%     71.3%    57.4%    36.3%   57.5%   68.3%
             YOLOv7-X                71.3M     189.9G    640    52.9%     71.1%    57.5%    36.9%   57.7%   68.6%
             improvement             -36%       -19%      -      +0.2      -0.2     +0.1     +0.6    +0.2    +0.3
             YOLOv4-tiny [79]          6.1       6.9     416    24.9%     42.1%    25.7%     8.7%   28.4%   39.2%
             YOLOv7-tiny               6.2       5.8     416    35.2%     52.8%    37.3%    15.7%   38.0%   53.4%
             improvement              +2%       -19%      -     +10.3     +10.7    +11.6     +7.0    +9.6   +14.2
             YOLOv4-tiny-3l [79]       8.7       5.2     320    30.8%     47.3%    32.2%    10.9%   31.9%   51.5%
             YOLOv7-tiny               6.2       3.5     320    30.8%     47.3%    32.2%    10.0%   31.9%   52.2%
             improvement              -39%      -49%      -       =         =        =       -0.9     =      +0.7
             YOLOR-E6 [81]           115.8M    683.2G    1280   55.7%     73.2%    60.7%    40.1%   60.4%   69.2%
             YOLOv7-E6               97.2M     515.2G    1280   55.9%     73.5%    61.1%    40.6%   60.3%   70.0%
             improvement              -19%      -33%       -     +0.2      +0.3     +0.4     +0.5    -0.1    +0.8
             YOLOR-D6 [81]           151.7M    935.6G    1280   56.1%     73.9%    61.2%    42.4%   60.5%   69.9%
             YOLOv7-D6               154.7M    806.8G    1280   56.3%     73.8%    61.4%    41.3%   60.6%   70.1%
             YOLOv7-E6E              151.7M    843.2G    1280   56.8%     74.4%    62.1%    40.8%   62.1%   70.6%
             improvement                =       -11%       -     +0.7      +0.5     +0.9     -1.6    +1.6    +0.7

that of fine label, it may produce bad prior at final predic-       5. Experiments
tion. Therefore, in order to make those extra coarse positive
grids have less impact, we put restrictions in the decoder,         5.1. Experimental setup
so that the extra coarse positive grids cannot produce soft            We use Microsoft COCO dataset to conduct experiments
label perfectly. The mechanism mentioned above allows               and validate our object detection method. All our experi-
the importance of fine label and coarse label to be dynam-          ments did not use pre-trained models. That is, all models
ically adjusted during the learning process, and makes the          were trained from scratch. During the development pro-
optimizable upper bound of fine label always higher than            cess, we used train 2017 set for training, and then used val
coarse label.                                                       2017 set for verification and choosing hyperparameters. Fi-
                                                                    nally, we show the performance of object detection on the
4.3. Other trainable bag-of-freebies                                test 2017 set and compare it with the state-of-the-art object
                                                                    detection algorithms. Detailed training parameter settings
   In this section we will list some trainable bag-of-              are described in Appendix.
freebies. These freebies are some of the tricks we used                We designed basic model for edge GPU, normal GPU,
in training, but the original concepts were not proposed            and cloud GPU, and they are respectively called YOLOv7-
by us. The training details of these freebies will be elab-         tiny, YOLOv7, and YOLOv7-W6. At the same time, we
orated in the Appendix, including (1) Batch normalization           also use basic model for model scaling for different ser-
in conv-bn-activation topology: This part mainly connects           vice requirements and get different types of models. For
batch normalization layer directly to convolutional layer.          YOLOv7, we do stack scaling on neck, and use the pro-
The purpose of this is to integrate the mean and variance           posed compound scaling method to perform scaling-up of
of batch normalization into the bias and weight of convolu-         the depth and width of the entire model, and use this to ob-
tional layer at the inference stage. (2) Implicit knowledge         tain YOLOv7-X. As for YOLOv7-W6, we use the newly
in YOLOR [81] combined with convolution feature map in              proposed compound scaling method to obtain YOLOv7-E6
addition and multiplication manner: Implicit knowledge in           and YOLOv7-D6. In addition, we use the proposed E-
YOLOR can be simplified to a vector by pre-computing at             ELAN for YOLOv7-E6, and thereby complete YOLOv7-
the inference stage. This vector can be combined with the           E6E. Since YOLOv7-tiny is an edge GPU-oriented archi-
bias and weight of the previous or subsequent convolutional         tecture, it will use leaky ReLU as activation function. As
layer. (3) EMA model: EMA is a technique used in mean               for other models we use SiLU as activation function. We
teacher [75], and in our system we use EMA model purely             will describe the scaling factor of each model in detail in
as the final inference model.                                       Appendix.

                                                                6
                                       Table 2: Comparison of state-of-the-art real-time object detectors.
    Model                         #Param.      FLOPs       Size     FPS     APtest / APval      APtest
                                                                                                  50        APtest
                                                                                                              75          APtest
                                                                                                                            S      APtest
                                                                                                                                     M      APtest
                                                                                                                                              L
    YOLOX-S [21]                   9.0M         26.8G      640      102      40.5% / 40.5%          -          -            -        -        -
    YOLOX-M [21]                   25.3M        73.8G      640       81      47.2% / 46.9%          -          -            -        -        -
    YOLOX-L [21]                   54.2M       155.6G      640       69      50.1% / 49.7%          -          -            -        -        -
    YOLOX-X [21]                   99.1M       281.9G      640       58      51.5% / 51.1%          -          -            -        -        -
    PPYOLOE-S [85]                 7.9M         17.4G      640      208      43.1% / 42.7%       60.5%      46.6%         23.2%    46.4%    56.9%
    PPYOLOE-M [85]                 23.4M        49.9G      640      123      48.9% / 48.6%       66.5%      53.0%         28.6%    52.9%    63.8%
    PPYOLOE-L [85]                 52.2M       110.1G      640       78      51.4% / 50.9%       68.9%      55.6%         31.4%    55.3%    66.1%
    PPYOLOE-X [85]                 98.4M       206.6G      640       45      52.2% / 51.9%       69.9%      56.5%         33.3%    56.3%    66.4%
    YOLOv5-N (r6.1) [23]           1.9M         4.5G       640      159         - / 28.0%           -          -            -        -        -
    YOLOv5-S (r6.1) [23]           7.2M         16.5G      640      156         - / 37.4%           -          -            -        -        -
    YOLOv5-M (r6.1) [23]           21.2M        49.0G      640      122         - / 45.4%           -          -            -        -        -
    YOLOv5-L (r6.1) [23]           46.5M       109.1G      640       99         - / 49.0%           -          -            -        -        -
    YOLOv5-X (r6.1) [23]           86.7M       205.7G      640       83         - / 50.7%           -          -            -        -        -
    YOLOR-CSP [81]                 52.9M       120.4G      640      106      51.1% / 50.8%       69.6%      55.7%         31.7%    55.3%    64.7%
    YOLOR-CSP-X [81]               96.9M       226.8G      640       87      53.0% / 52.7%       71.4%      57.9%         33.7%    57.1%    66.8%
    YOLOv7-tiny-SiLU               6.2M         13.8G      640      286      38.7% / 38.7%       56.7%      41.7%         18.8%    42.4%    51.9%
    YOLOv7                         36.9M       104.7G      640      161      51.4% / 51.2%       69.7%      55.9%         31.8%    55.5%    65.0%
    YOLOv7-X                       71.3M       189.9G      640      114      53.1% / 52.9%       71.2%      57.8%         33.8%    57.1%    67.4%

    YOLOv5-N6 (r6.1) [23]           3.2M        18.4G      1280     123         - / 36.0%           -          -            -        -        -
    YOLOv5-S6 (r6.1) [23]           12.6M       67.2G      1280     122         - / 44.8%           -          -            -        -        -
    YOLOv5-M6 (r6.1) [23]           35.7M      200.0G      1280      90         - / 51.3%           -          -            -        -        -
    YOLOv5-L6 (r6.1) [23]           76.8M      445.6G      1280      63         - / 53.7%           -          -            -        -        -
    YOLOv5-X6 (r6.1) [23]          140.7M      839.2G      1280      38         - / 55.0%           -          -            -        -        -
    YOLOR-P6 [81]                   37.2M      325.6G      1280      76      53.9% / 53.5%       71.4%      58.9%         36.1%    57.7%    65.6%
    YOLOR-W6 [81]                   79.8G      453.2G      1280      66      55.2% / 54.8%       72.7%      60.5%         37.7%    59.1%    67.1%
    YOLOR-E6 [81]                  115.8M      683.2G      1280      45      55.8% / 55.7%       73.4%      61.1%         38.4%    59.7%    67.7%
    YOLOR-D6 [81]                  151.7M      935.6G      1280      34      56.5% / 56.1%       74.1%      61.9%         38.9%    60.4%    68.7%
    YOLOv7-W6                       70.4M      360.0G      1280      84      54.9% / 54.6%       72.6%      60.1%         37.3%    58.7%    67.1%
    YOLOv7-E6                       97.2M      515.2G      1280      56      56.0% / 55.9%       73.5%      61.2%         38.0%    59.9%    68.4%
    YOLOv7-D6                      154.7M      806.8G      1280      44      56.6% / 56.3%       74.0%      61.8%         38.8%    60.1%    69.5%
    YOLOv7-E6E                     151.7M      843.2G      1280      36      56.8% / 56.8%       74.4%      62.1%         39.3%    60.5%    69.0%
   1 Our FLOPs is calaculated by rectangle input resolution like 640 × 640 or 1280 × 1280.
   2 Our inference time is estimated by using letterbox resize input image to make its long side equals to 640 or 1280.

5.2. Baselines                                                                   5.3. Comparison with state-of-the-arts
    We choose previous version of YOLO [3, 79] and state-                            We compare the proposed method with state-of-the-art
of-the-art object detector YOLOR [81] as our baselines. Ta-                      object detectors for general GPUs and Mobile GPUs, and
ble 1 shows the comparison of our proposed YOLOv7 mod-                           the results are shown in Table 2. From the results in
els and those baseline that are trained with the same settings.                  Table 2 we know that the proposed method has the best
    From the results we see that if compared with YOLOv4,                        speed-accuracy trade-off comprehensively. If we compare
YOLOv7 has 75% less parameters, 36% less computation,                            YOLOv7-tiny-SiLU with YOLOv5-N (r6.1), our method
and brings 1.5% higher AP. If compared with state-of-the-                        is 127 fps faster and 10.7% more accurate on AP. In ad-
art YOLOR-CSP, YOLOv7 has 43% fewer parameters, 15%                              dition, YOLOv7 has 51.4% AP at frame rate of 161 fps,
less computation, and 0.4% higher AP. In the performance                         while PPYOLOE-L with the same AP has only 78 fps frame
of tiny model, compared with YOLOv4-tiny-31, YOLOv7-                             rate. In terms of parameter usage, YOLOv7 is 41% less than
tiny reduces the number of parameters by 39% and the                             PPYOLOE-L. If we compare YOLOv7-X with 114 fps in-
amount of computation by 49%, but maintains the same AP.                         ference speed to YOLOv5-L (r6.1) with 99 fps inference
On the cloud GPU model, our model can still have a higher                        speed, YOLOv7-X can improve AP by 3.9%. If YOLOv7-
AP while reducing the number of parameters by 19% and                            X is compared with YOLOv5-X (r6.1) of similar scale, the
the amount of computation by 33%.                                                inference speed of YOLOv7-X is 31 fps faster. In addi-
                                                                                 tion, in terms of the amount of parameters and computation,
                                                                                 YOLOv7-X reduces 22% of parameters and 8% of compu-
                                                                                 tation compared to YOLOv5-X (r6.1), but improves AP by
                                                                                 2.2%.

                                                                            7
   If we compare YOLOv7 with YOLOR using the input
resolution 1280, the inference speed of YOLOv7-W6 is 8
fps faster than that of YOLOR-P6, and the detection rate is
also increased by 1% AP. As for the comparison between
YOLOv7-E6 and YOLOv5-X6 (r6.1), the former has 0.9%
AP gain than the latter, 45% less parameters and 63% less
computation, and the inference speed is increased by 47%.
YOLOv7-D6 has close inference speed to YOLOR-E6, but
improves AP by 0.8%. YOLOv7-E6E has close inference
speed to YOLOR-D6, but improves AP by 0.3%.                          Figure 6: Planned RepConv 3-stacked ELAN. Blue circles are the
                                                                     position we replace Conv by RepConv.
5.4. Ablation study
5.4.1    Proposed compound scaling method                             Table 4: Ablation study on planned RepConcatenation model.

Table 3 shows the results obtained when using different               Model            APval APval
                                                                                               50  APval
                                                                                                     75  APval
                                                                                                           S   APval
                                                                                                                 M   APval
                                                                                                                       L

model scaling strategies for scaling up. Among them, our              base (3-S ELAN) 52.26% 70.41% 56.77% 35.81% 57.00% 67.59%
proposed compound scaling method is to scale up the depth             Figure 6 (a)    52.18% 70.34% 56.90% 35.71% 56.83% 67.51%
                                                                      Figure 6 (b)    52.30% 70.30% 56.92% 35.76% 56.95% 67.74%
of computational block by 1.5 times and the width of tran-            Figure 6 (c)    52.33% 70.56% 56.91% 35.90% 57.06% 67.50%
sition block by 1.25 times. If our method is compared with            Figure 6 (d)    52.17% 70.32% 56.82% 35.33% 57.06% 68.09%
the method that only scaled up the width, our method can              Figure 6 (e)    52.23% 70.20% 56.81% 35.34% 56.97% 66.88%
improve the AP by 0.5% with less parameters and amount
of computation. If our method is compared with the method
that only scales up the depth, our method only needs to in-          volution block that conforms to our design strategy, we ad-
crease the number of parameters by 2.9% and the amount of            ditionally design a reversed dark block for the experiment,
computation by 1.2%, which can improve the AP by 0.2%.               whose architecture is shown in Figure 7. Since the CSP-
It can be seen from the results of Table 3 that our proposed         Darknet with dark block and reversed dark block has exactly
compound scaling strategy can utilize parameters and com-            the same amount of parameters and operations, it is fair to
putation more efficiently.                                           compare. The experiment results illustrated in Table 5 fully
                                                                     confirm that the proposed planned re-parameterized model
        Table 3: Ablation study on proposed model scaling.           is equally effective on residual-based model. We find that
 Model                 #Param. FLOPs Size APval APval  val           the design of RepCSPResNet [85] also fit our design pat-
                                                  50 AP75
                                                                     tern.
 base (v7-X light)     47.0M   125.5G 640 51.7% 70.1% 56.0%
 width only (1.25 w)   73.4M   195.5G 640 52.4% 70.9% 57.1%
 depth only (2.0 d)    69.3M   187.6G 640 52.7% 70.8% 57.3%
 compound (v7-X)       71.3M   189.9G 640 52.9% 71.1% 57.5%
 improvement              -       -    -   +1.2 +1.0 +1.5

5.4.2    Proposed planned re-parameterized model
In order to verify the generality of our proposed planed             Figure 7: Reversed CSPDarknet. We reverse the position of 1 × 1
re-parameterized model, we use it on concatenation-based             and 3 × 3 convolutional layer in dark block to fit our planned re-
                                                                     parameterized model design strategy.
model and residual-based model respectively for verifica-
tion. The concatenation-based model and residual-based
model we chose for verification are 3-stacked ELAN and
CSPDarknet, respectively.                                                Table 5: Ablation study on planned RepResidual model.
   In the experiment of concatenation-based model, we re-            Model               APval APval
                                                                                                 50  APval
                                                                                                       75  APval
                                                                                                             S   APval
                                                                                                                   M   APval
                                                                                                                         L
place the 3 × 3 convolutional layers in different positions in       base (YOLOR-W6) 54.82% 72.39% 59.95% 39.68% 59.38% 68.30%
3-stacked ELAN with RepConv, and the detailed configura-             RepCSP          54.67% 72.50% 59.58% 40.22% 59.61% 67.87%
tion is shown in Figure 6. From the results shown in Table 4         RCSP            54.36% 71.95% 59.54% 40.15% 59.02% 67.44%
                                                                     RepRCSP         54.85% 72.51% 60.08% 40.53% 59.52% 68.06%
we see that all higher AP values are present on our proposed
planned re-parameterized model.                                      base (YOLOR-CSP) 50.81% 69.47% 55.28% 33.74% 56.01% 65.38%
                                                                     RepRCSP          50.91% 69.54% 55.55% 34.44% 55.74% 65.46%
   In the experiment dealing with residual-based model,
since the original dark block does not have a 3 × 3 con-

                                                                 8
                          Figure 8: Objectness map predicted by different methods at auxiliary head and lead head.

5.4.3     Proposed assistant loss for auxiliary head                         Since the proposed YOLOv7 uses multiple pyramids to
                                                                         jointly predict object detection results, we can directly con-
In the assistant loss for auxiliary head experiments, we com-            nect auxiliary head to the pyramid in the middle layer for
pare the general independent label assignment for lead head              training. This type of training can make up for informa-
and auxiliary head methods, and we also compare the two                  tion that may be lost in the next level pyramid prediction.
proposed lead guided label assignment methods. We show                   For the above reasons, we designed partial auxiliary head
all comparison results in Table 6. From the results listed in            in the proposed E-ELAN architecture. Our approach is to
Table 6, it is clear that any model that increases assistant             connect auxiliary head after one of the sets of feature map
loss can significantly improve the overall performance. In               before merging cardinality, and this connection can make
addition, our proposed lead guided label assignment strat-               the weight of the newly generated set of feature map not
egy receives better performance than the general indepen-                directly updated by assistant loss. Our design allows each
dent label assignment strategy in AP, AP50 , and AP75 . As               pyramid of lead head to still get information from objects
for our proposed coarse for assistant and fine for lead label            with different sizes. Table 8 shows the results obtained us-
assignment strategy, it results in best results in all cases. In         ing two different methods, i.e., coarse-to-fine lead guided
Figure 8 we show the objectness map predicted by different               and partial coarse-to-fine lead guided methods. Obviously,
methods at auxiliary head and lead head. From Figure 8 we                the partial coarse-to-fine lead guided method has a better
find that if auxiliary head learns lead guided soft label, it            auxiliary effect.
will indeed help lead head to extract the residual informa-
                                                                                Table 8: Ablation study on partial auxiliary head.
tion from the consistant targets.
                                                                                 Model            Size   APval   APval
                                                                                                                   50     APval
                                                                                                                            75

         Table 6: Ablation study on proposed auxiliary head.                     base (v7-E6E)   1280    56.3%   74.0%    61.5%
                                                                                 aux             1280    56.5%   74.0%    61.6%
   Model                         Size    APval    APval
                                                    50     APval
                                                             75                  partial aux     1280    56.8%   74.4%    62.1%
   base (v7-E6)                  1280    55.6%    73.2%    60.7%                 improvement       -      +0.5    +0.4     +0.6
   independent                   1280    55.8%    73.4%    60.9%
   lead guided                   1280    55.9%    73.5%    61.0%
   coarse-to-fine lead guided    1280    55.9%    73.5%    61.1%
                                                                         6. Conclusions
   improvement                     -      +0.3     +0.3     +0.4
                                                                            In this paper we propose a new architecture of real-
                                                                         time object detector and the corresponding model scaling
   In Table 7 we further analyze the effect of the proposed              method. Furthermore, we find that the evolving process
coarse-to-fine lead guided label assignment method on the                of object detection methods generates new research top-
decoder of auxiliary head. That is, we compared the results              ics. During the research process, we found the replace-
of with/without the introduction of upper bound constraint.              ment problem of re-parameterized module and the alloca-
Judging from the numbers in the Table, the method of con-                tion problem of dynamic label assignment. To solve the
straining the upper bound of objectness by the distance from             problem, we propose the trainable bag-of-freebies method
the center of the object can achieve better performance.                 to enhance the accuracy of object detection. Based on the
                                                                         above, we have developed the YOLOv7 series of object de-
        Table 7: Ablation study on constrained auxiliary head.           tection systems, which receives the state-of-the-art results.
     Model                      Size    APval    APval    APval
                                                   50       75           7. Acknowledgements
     base (v7-E6)               1280    55.6%    73.2%    60.7%
     aux without constraint     1280    55.9%    73.5%    61.0%             The authors wish to thank National Center for High-
     aux with constraint        1280    55.9%    73.5%    61.1%          performance Computing (NCHC) for providing computa-
     improvement                  -      +0.3     +0.3     +0.4
                                                                         tional and storage resources.

                                                                     9
                    Table 9: More comparison (batch=1, no-TRT, without extra object detection training data)
          Model                            #Param.    FLOPs          Size   FPSV 100   APtest / APval   APtest
                                                                                                          50     APtest
                                                                                                                   75

          YOLOv7-tiny-SiLU                  6.2M       13.8G         640      286      38.7% / 38.7%    56.7%    41.7%
          PPYOLOE-S [85]                    7.9M       17.4G         640      208      43.1% / 42.7%    60.5%    46.6%
          YOLOv7                            36.9M      104.7G     640         161      51.4% / 51.2%    69.7%    55.9%
          YOLOv5-N (r6.1) [23]               1.9M       4.5G      640         159         - / 28.0%        -        -
          YOLOv5-S (r6.1) [23]               7.2M      16.5G      640         156         - / 37.4%        -        -
          PPYOLOE-M [85]                    23.4M      49.9G      640         123      48.9% / 48.6%    66.5%    53.0%
          YOLOv5-N6 (r6.1) [23]              3.2M      18.4G     1280         123         - / 36.0%        -        -
          YOLOv5-S6 (r6.1) [23]             12.6M      67.2G     1280         122         - / 44.8%        -        -
          YOLOv5-M (r6.1) [23]              21.2M      49.0G      640         122         - / 45.4%        -        -
          YOLOv7-X                          71.3M      189.9G     640         114      53.1% / 52.9%    71.2%    57.8%
          YOLOR-CSP [81]                    52.9M      120.4G     640         106      51.1% / 50.8%    69.6%    55.7%
          YOLOX-S [21]                       9.0M      26.8G      640         102      40.5% / 40.5%       -        -
          YOLOv5-L (r6.1) [23]              46.5M      109.1G     640          99         - / 49.0%        -        -
          YOLOv5-M6 (r6.1) [23]             35.7M      200.0G    1280          90         - / 51.3%        -        -
          YOLOR-CSP-X [81]                  96.9M      226.8G     640          87      53.0% / 52.7%    71.4%    57.9%
          YOLOv7-W6                         70.4M      360.0G    1280          84      54.9% / 54.6%    72.6%    60.1%
          YOLOv5-X (r6.1) [23]              86.7M      205.7G     640          83         - / 50.7%        -        -
          YOLOX-M [21]                      25.3M      73.8G      640          81      47.2% / 46.9%       -        -
          PPYOLOE-L [85]                    52.2M      110.1G     640          78      51.4% / 50.9%    68.9%    55.6%
          YOLOR-P6 [81]                     37.2M      325.6G    1280          76      53.9% / 53.5%    71.4%    58.9%
          YOLOX-L [21]                      54.2M      155.6G     640          69      50.1% / 49.7%       -        -
          YOLOR-W6 [81]                     79.8G      453.2G    1280          66      55.2% / 54.8%    72.7%    60.5%
          YOLOv5-L6 (r6.1) [23]             76.8M      445.6G    1280          63         - / 53.7%        -        -
          YOLOX-X [21]                     99.1M       281.9G     640          58      51.5% / 51.1%       -        -
          YOLOv7-E6                        97.2M       515.2G    1280          56      56.0% / 55.9%    73.5%    61.2%
          YOLOR-E6 [81]                    115.8M      683.2G    1280          45      55.8% / 55.7%    73.4%    61.1%
          PPYOLOE-X [85]                   98.4M       206.6G     640          45      52.2% / 51.9%    69.9%    56.5%
          YOLOv7-D6                        154.7M      806.8G    1280          44      56.6% / 56.3%    74.0%    61.8%
          YOLOv5-X6 (r6.1) [23]            140.7M      839.2G    1280          38         - / 55.0%        -        -
          YOLOv7-E6E                       151.7M      843.2G    1280          36      56.8% / 56.8%    74.4%    62.1%
          YOLOR-D6 [81]                    151.7M      935.6G    1280          34      56.5% / 56.1%    74.1%    61.9%
          F-RCNN-R101-FPN+ [5]             60.0M       246.0G    1333          20         - / 44.0%        -       -
          Deformable DETR [100]            40.0M       173.0G      -           19         - / 46.2%        -       -
          Swin-B (C-M-RCNN) [52]           145.0M      982.0G    1333         11.6        - / 51.9%        -       -
          DETR DC5-R101 [5]                60.0M       253.0G    1333          10         - / 44.9%        -       -
          EfficientDet-D7x [74]            77.0M       410.0G    1536          6.5     55.1% / 54.4%    72.4%    58.4%
          Dual-Swin-T (C-M-RCNN) [47]      113.8M      836.0G    1333          6.5        - / 53.6%        -       -
          ViT-Adapter-B [7]                122.0M      997.0G      -           4.4        - / 50.8%        -       -
          Dual-Swin-B (HTC) [47]           235.0M         -      1600          2.5     58.7% / 58.4%       -       -
          Dual-Swin-L (HTC) [47]           453.0M         -      1600          1.5     59.4% / 59.1%       -       -

          Model                            #Param.    FLOPs          Size   FPSA100    APtest / APval   APtest
                                                                                                          50     APtest
                                                                                                                   75

          DN-Deformable-DETR [41]           48.0M      265.0G    1333         23.0        - / 48.6%        -       -
          ConvNeXt-B (C-M-RCNN) [53]           -       964.0G    1280         11.5        - / 54.0%     73.1%    58.8%
          Swin-B (C-M-RCNN) [52]               -       982.0G    1280         10.7        - / 53.0%     71.8%    57.5%
          DINO-5scale (R50) [89]            47.0M      860.0G    1333         10.0        - / 51.0%        -       -
          ConvNeXt-L (C-M-RCNN) [53]           -      1354.0G    1280         10.0        - / 54.8%     73.8%    59.8%
          Swin-L (C-M-RCNN) [52]               -      1382.0G    1280          9.2        - / 53.9%     72.4%    58.8%
          ConvNeXt-XL (C-M-RCNN) [53]          -      1898.0G    1280          8.6        - / 55.2%     74.2%    59.9%

8. More comparison                                                    and convolutional-based detector ConvNeXt-XL Cascade-
   YOLOv7 surpasses all known object detectors in both                Mask R-CNN (8.6 FPS A100, 55.2% AP) by 551% in speed
speed and accuracy in the range from 5 FPS to 160 FPS and             and 0.7% AP in accuracy, as well as YOLOv7 outperforms:
has the highest accuracy 56.8% AP test-dev / 56.8% AP                 YOLOR, YOLOX, Scaled-YOLOv4, YOLOv5, DETR, De-
min-val among all known real-time object detectors with 30            formable DETR, DINO-5scale-R50, ViT-Adapter-B and
FPS or higher on GPU V100. YOLOv7-E6 object detector                  many other object detectors in speed and accuracy. More
(56 FPS V100, 55.9% AP) outperforms both transformer-                 over, we train YOLOv7 only on MS COCO dataset from
based detector SWIN-L Cascade-Mask R-CNN (9.2 FPS                     scratch without using any other datasets or pre-trained
A100, 53.9% AP) by 509% in speed and 2% in accuracy,                  weights.

                                                                10
                                              Figure 9: Comparison with other object detectors.

                                        Figure 10: Comparison with other real-time object detectors.

           Table 10: Comparison of different setting.
    Model              Presicion      IoU threshold     APval
    YOLOv7-X         FP16 (default)    0.65 (default)   52.9%
    YOLOv7-X            FP32               0.65         53.0%
    YOLOv7-X            FP16               0.70         53.0%
    YOLOv7-X            FP32               0.70         53.1%
    improvement            -                 -          +0.2%
   * Similar to meituan/YOLOv6 and PPYOLOE, our model could

   get higher AP when set higher IoU threshold.

   The maximum accuracy of the YOLOv7-E6E (56.8%
AP) real-time model is +13.7% AP higher than the cur-
rent most accurate meituan/YOLOv6-s model (43.1% AP)
on COCO dataset. Our YOLOv7-tiny (35.2% AP, 0.4
ms) model is +25% faster and +0.2% AP higher than
meituan/YOLOv6-n (35.0% AP, 0.5 ms) under identical                         Figure 11: Comparison with other real-time object detectors.
conditions on COCO dataset and V100 GPU with batch=32.

                                                                     11
References                                                                   IEEE/CVF Conference on Computer Vision and Pattern
                                                                             Recognition (CVPR), pages 13733–13742, 2021. 2, 4
 [1] anonymous. Designing network design strategies. anony-
                                                                        [14] Xiaohan Ding, Xiangyu Zhang, Yizhuang Zhou, Jungong
     mous submission, 2022. 3
                                                                             Han, Guiguang Ding, and Jian Sun. Scaling up your ker-
 [2] Irwan Bello, William Fedus, Xianzhi Du, Ekin Dogus                      nels to 31x31: Revisiting large kernel design in CNNs. In
     Cubuk, Aravind Srinivas, Tsung-Yi Lin, Jonathon Shlens,                 Proceedings of the IEEE/CVF Conference on Computer Vi-
     and Barret Zoph. Revisiting ResNets: Improved training                  sion and Pattern Recognition (CVPR), 2022. 2
     and scaling strategies. Advances in Neural Information Pro-        [15] Piotr Dollár, Mannat Singh, and Ross Girshick. Fast and
     cessing Systems (NeurIPS), 34, 2021. 2                                  accurate model scaling. In Proceedings of the IEEE/CVF
 [3] Alexey Bochkovskiy, Chien-Yao Wang, and Hong-                           Conference on Computer Vision and Pattern Recognition
     Yuan Mark Liao. YOLOv4: Optimal speed and accuracy of                   (CVPR), pages 924–932, 2021. 2, 3
     object detection. arXiv preprint arXiv:2004.10934, 2020.           [16] Xianzhi Du, Barret Zoph, Wei-Chih Hung, and Tsung-Yi
     2, 6, 7                                                                 Lin. Simple training strategies and model scaling for object
 [4] Yue Cao, Thomas Andrew Geddes, Jean Yee Hwa Yang,                       detection. arXiv preprint arXiv:2107.00057, 2021. 2
     and Pengyi Yang. Ensemble deep learning in bioinformat-            [17] Chengjian Feng, Yujie Zhong, Yu Gao, Matthew R Scott,
     ics. Nature Machine Intelligence, 2(9):500–508, 2020. 2                 and Weilin Huang. TOOD: Task-aligned one-stage object
 [5] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nico-                detection. In Proceedings of the IEEE/CVF International
     las Usunier, Alexander Kirillov, and Sergey Zagoruyko.                  Conference on Computer Vision (ICCV), pages 3490–3499,
     End-to-end object detection with transformers. In Pro-                  2021. 2, 5
     ceedings of the European Conference on Computer Vision             [18] Di Feng, Christian Haase-Schütz, Lars Rosenbaum, Heinz
     (ECCV), pages 213–229, 2020. 10                                         Hertlein, Claudius Glaeser, Fabian Timm, Werner Wies-
 [6] Kean Chen, Weiyao Lin, Jianguo Li, John See, Ji Wang, and               beck, and Klaus Dietmayer. Deep multi-modal object de-
     Junni Zou. AP-loss for accurate one-stage object detection.             tection and semantic segmentation for autonomous driv-
     IEEE Transactions on Pattern Analysis and Machine Intel-                ing: Datasets, methods, and challenges. IEEE Transac-
     ligence (TPAMI), 43(11):3782–3798, 2020. 2                              tions on Intelligent Transportation Systems, 22(3):1341–
 [7] Zhe Chen, Yuchen Duan, Wenhai Wang, Junjun He, Tong                     1360, 2020. 1
     Lu, Jifeng Dai, and Yu Qiao. Vision transformer adapter for        [19] Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin,
     dense predictions. arXiv preprint arXiv:2205.08534, 2022.               Dmitry P Vetrov, and Andrew G Wilson. Loss sur-
     10                                                                      faces, mode connectivity, and fast ensembling of DNNs.
 [8] Jiwoong Choi, Dayoung Chun, Hyun Kim, and Hyuk-Jae                      Advances in Neural Information Processing Systems
     Lee. Gaussian YOLOv3: An accurate and fast object detec-                (NeurIPS), 31, 2018. 2
     tor using localization uncertainty for autonomous driving.         [20] Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, and
     In Proceedings of the IEEE/CVF International Conference                 Jian Sun. OTA: Optimal transport assignment for object
     on Computer Vision (ICCV), pages 502–511, 2019. 5                       detection. In Proceedings of the IEEE/CVF Conference on
 [9] Xiyang Dai, Yinpeng Chen, Bin Xiao, Dongdong Chen,                      Computer Vision and Pattern Recognition (CVPR), pages
     Mengchen Liu, Lu Yuan, and Lei Zhang. Dynamic head:                     303–312, 2021. 2, 5
     Unifying object detection heads with attentions. In Pro-           [21] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian
     ceedings of the IEEE/CVF Conference on Computer Vision                  Sun. YOLOX: Exceeding YOLO series in 2021. arXiv
     and Pattern Recognition (CVPR), pages 7373–7382, 2021.                  preprint arXiv:2107.08430, 2021. 1, 2, 7, 10
     2                                                                  [22] Golnaz Ghiasi, Tsung-Yi Lin, and Quoc V Le. NAS-FPN:
[10] Xiaohan Ding, Honghao Chen, Xiangyu Zhang, Kaiqi                        Learning scalable feature pyramid architecture for object
     Huang, Jungong Han, and Guiguang Ding.                  Re-             detection. In Proceedings of the IEEE/CVF Conference on
     parameterizing your optimizers rather than architectures.               Computer Vision and Pattern Recognition (CVPR), pages
     arXiv preprint arXiv:2205.15242, 2022. 2                                7036–7045, 2019. 2
[11] Xiaohan Ding, Yuchen Guo, Guiguang Ding, and Jungong               [23] Jocher Glenn. YOLOv5 release v6.1. https://github.com/
     Han. ACNet: Strengthening the kernel skeletons for pow-                 ultralytics/yolov5/releases/tag/v6.1, 2022. 2, 7, 10
     erful CNN via asymmetric convolution blocks. In Proceed-           [24] Shuxuan Guo, Jose M Alvarez, and Mathieu Salzmann. Ex-
     ings of the IEEE/CVF International Conference on Com-                   pandNets: Linear over-parameterization to train compact
     puter Vision (ICCV), pages 1911–1920, 2019. 2                           convolutional networks. Advances in Neural Information
[12] Xiaohan Ding, Xiangyu Zhang, Jungong Han, and                           Processing Systems (NeurIPS), 33:1298–1310, 2020. 2
     Guiguang Ding. Diverse branch block: Building a con-               [25] Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing
     volution as an inception-like unit. In Proceedings of the               Xu, and Chang Xu. GhostNet: More features from cheap
     IEEE/CVF Conference on Computer Vision and Pattern                      operations. In Proceedings of the IEEE/CVF Conference on
     Recognition (CVPR), pages 10886–10895, 2021. 2                          Computer Vision and Pattern Recognition (CVPR), pages
[13] Xiaohan Ding, Xiangyu Zhang, Ningning Ma, Jungong                       1580–1589, 2020. 1
     Han, Guiguang Ding, and Jian Sun. RepVGG: Making                   [26] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     VGG-style convnets great again. In Proceedings of the                   Deep residual learning for image recognition. In Proceed-

                                                                   12
     ings of the IEEE/CVF Conference on Computer Vision and             [39] Youngwan Lee, Joong-won Hwang, Sangrok Lee, Yuseok
     Pattern Recognition (CVPR), pages 770–778, 2016. 1, 4, 5                Bae, and Jongyoul Park. An energy and GPU-computation
[27] Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh                     efficient backbone network for real-time object detection.
     Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu,                    In Proceedings of the IEEE/CVF Conference on Com-
     Ruoming Pang, Vijay Vasudevan, et al. Searching for Mo-                 puter Vision and Pattern Recognition Workshops (CVPRW),
     bileNetV3. In Proceedings of the IEEE/CVF Conference on                 pages 0–0, 2019. 2, 3
     Computer Vision and Pattern Recognition (CVPR), pages              [40] Buyu Li, Wanli Ouyang, Lu Sheng, Xingyu Zeng, and
     1314–1324, 2019. 1                                                      Xiaogang Wang. GS3D: An efficient 3d object detection
[28] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry                          framework for autonomous driving. In Proceedings of the
     Kalenichenko, Weijun Wang, Tobias Weyand, Marco An-                     IEEE/CVF Conference on Computer Vision and Pattern
     dreetto, and Hartwig Adam. MobileNets: Efficient con-                   Recognition (CVPR), pages 1019–1028, 2019. 1
     volutional neural networks for mobile vision applications.         [41] Feng Li, Hao Zhang, Shilong Liu, Jian Guo, Lionel M
     arXiv preprint arXiv:1704.04861, 2017. 1                                Ni, and Lei Zhang. DN-DETR: Accelerate detr training
[29] Mu Hu, Junyi Feng, Jiashen Hua, Baisheng Lai, Jian-                     by introducing query denoising. In Proceedings of the
     qiang Huang, Xiaojin Gong, and Xiansheng Hua. On-                       IEEE/CVF Conference on Computer Vision and Pattern
     line convolutional re-parameterization. In Proceedings of               Recognition (CVPR), pages 13619–13627, 2022. 10
     the IEEE/CVF Conference on Computer Vision and Pattern             [42] Shuai Li, Chenhang He, Ruihuang Li, and Lei Zhang. A
     Recognition (CVPR), 2022. 2                                             dual weighting label assignment scheme for object detec-
[30] Miao Hu, Yali Li, Lu Fang, and Shengjin Wang. A2 -FPN:                  tion. In Proceedings of the IEEE/CVF Conference on Com-
     Attention aggregation based feature pyramid network for                 puter Vision and Pattern Recognition (CVPR), pages 9387–
     instance segmentation. In Proceedings of the IEEE/CVF                   9396, 2022. 2, 5
     Conference on Computer Vision and Pattern Recognition              [43] Xiang Li, Wenhai Wang, Xiaolin Hu, Jun Li, Jinhui Tang,
     (CVPR), pages 15343–15352, 2021. 2                                      and Jian Yang. Generalized focal loss v2: Learning reliable
[31] Gao Huang, Yixuan Li, Geoff Pleiss, Zhuang Liu, John E                  localization quality estimation for dense object detection. In
     Hopcroft, and Kilian Q Weinberger. Snapshot ensembles:                  Proceedings of the IEEE/CVF Conference on Computer Vi-
     Train 1, get m for free. International Conference on Learn-             sion and Pattern Recognition (CVPR), pages 11632–11641,
     ing Representations (ICLR), 2017. 2                                     2021. 5
[32] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kil-            [44] Xiang Li, Wenhai Wang, Lijun Wu, Shuo Chen, Xiaolin
     ian Q Weinberger. Densely connected convolutional net-                  Hu, Jun Li, Jinhui Tang, and Jian Yang. Generalized focal
     works. In Proceedings of the IEEE/CVF Conference on                     loss: Learning qualified and distributed bounding boxes for
     Computer Vision and Pattern Recognition (CVPR), pages                   dense object detection. Advances in Neural Information
     4700–4708, 2017. 2, 4, 5                                                Processing Systems (NeurIPS), 33:21002–21012, 2020. 5
[33] Pavel Izmailov, Dmitrii Podoprikhin, Timur Garipov,
                                                                        [45] Yanghao Li, Hanzi Mao, Ross Girshick, and Kaiming He.
     Dmitry Vetrov, and Andrew Gordon Wilson. Averaging
                                                                             Exploring plain vision transformer backbones for object de-
     weights leads to wider optima and better generalization. In
                                                                             tection. arXiv preprint arXiv:2203.16527, 2022. 2
     Conference on Uncertainty in Artificial Intelligence (UAI),
                                                                        [46] Zhuoling Li, Minghui Dong, Shiping Wen, Xiang Hu, Pan
     2018. 2
                                                                             Zhou, and Zhigang Zeng. CLU-CNNs: Object detection for
[34] Paul F Jaeger, Simon AA Kohl, Sebastian Bickel-
                                                                             medical images. Neurocomputing, 350:53–59, 2019. 1
     haupt, Fabian Isensee, Tristan Anselm Kuder, Heinz-Peter
     Schlemmer, and Klaus H Maier-Hein. Retina U-Net: Em-               [47] Tingting Liang, Xiaojie Chu, Yudong Liu, Yongtao Wang,
     barrassingly simple exploitation of segmentation supervi-               Zhi Tang, Wei Chu, Jingdong Chen, and Haibin Ling. CB-
     sion for medical object detection. In Machine Learning for              NetV2: A composite backbone network architecture for ob-
     Health Workshop, pages 171–183, 2020. 1                                 ject detection. arXiv preprint arXiv:2107.00420, 2021. 5,
[35] Hakan Karaoguz and Patric Jensfelt. Object detection ap-                10
     proach for robot grasp detection. In IEEE International            [48] Ji Lin, Wei-Ming Chen, Han Cai, Chuang Gan, and Song
     Conference on Robotics and Automation (ICRA), pages                     Han. Memory-efficient patch-based inference for tiny deep
     4953–4959, 2019. 1                                                      learning. Advances in Neural Information Processing Sys-
[36] Kang Kim and Hee Seok Lee. Probabilistic anchor as-                     tems (NeurIPS), 34:2346–2358, 2021. 1
     signment with iou prediction for object detection. In Pro-         [49] Ji Lin, Wei-Ming Chen, Yujun Lin, Chuang Gan, Song
     ceedings of the European conference on computer vision                  Han, et al. MCUNet: Tiny deep learning on IoT de-
     (ECCV), pages 355–371, 2020. 5                                          vices. Advances in Neural Information Processing Systems
[37] Alexander Kirillov, Ross Girshick, Kaiming He, and Piotr                (NeurIPS), 33:11711–11722, 2020. 1
     Dollár. Panoptic feature pyramid networks. In Proceed-            [50] Yuxuan Liu, Lujia Wang, and Ming Liu. YOLOStereo3D:
     ings of the IEEE/CVF Conference on Computer Vision and                  A step back to 2D for efficient stereo 3D detection. In
     Pattern Recognition (CVPR), pages 6399–6408, 2019. 2                    IEEE International Conference on Robotics and Automa-
[38] Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou                   tion (ICRA), pages 13018–13024, 2021. 5
     Zhang, and Zhuowen Tu. Deeply-supervised nets. In Arti-            [51] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
     ficial Intelligence and Statistics, pages 562–570, 2015. 5              Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong,

                                                                   13
     et al. Swin transformer v2: Scaling up capacity and res-             [64] Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak, Amir
     olution. In Proceedings of the IEEE/CVF Conference on                     Sadeghian, Ian Reid, and Silvio Savarese. Generalized in-
     Computer Vision and Pattern Recognition (CVPR), 2022. 2                   tersection over union: A metric and a loss for bounding
[52] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng                    box regression. In Proceedings of the IEEE/CVF Confer-
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:                    ence on Computer Vision and Pattern Recognition (CVPR),
     Hierarchical vision transformer using shifted windows. In                 pages 658–666, 2019. 2
     Proceedings of the IEEE/CVF International Conference on              [65] Byungseok Roh, JaeWoong Shin, Wuhyun Shin, and
     Computer Vision (ICCV), pages 10012–10022, 2021. 10                       Saehoon Kim. Sparse DETR: Efficient end-to-end ob-
[53] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feicht-                    ject detection with learnable sparsity. arXiv preprint
     enhofer, Trevor Darrell, and Saining Xie. A ConvNet for                   arXiv:2111.14330, 2021. 5
     the 2020s. In Proceedings of the IEEE/CVF Conference on              [66] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey
     Computer Vision and Pattern Recognition (CVPR), pages                     Zhmoginov, and Liang-Chieh Chen. MobileNetV2: In-
     11976–11986, 2022. 10                                                     verted residuals and linear bottlenecks. In Proceedings of
[54] Rangi Lyu. NanoDet-Plus. https://github.com/RangiLyu/                     the IEEE/CVF Conference on Computer Vision and Pattern
     nanodet/releases/tag/v1.0.0-alpha-1, 2021. 1, 2                           Recognition (CVPR), pages 4510–4520, 2018. 1
[55] Ningning Ma, Xiangyu Zhang, Hai-Tao Zheng, and Jian                  [67] Zhiqiang Shen, Zhuang Liu, Jianguo Li, Yu-Gang Jiang,
     Sun. ShuffleNet V2: Practical guidelines for efficient CNN                Yurong Chen, and Xiangyang Xue. Object detection
     architecture design. In Proceedings of the European Con-                  from scratch with deep supervision. IEEE Transactions
     ference on Computer Vision (ECCV), pages 116–131, 2018.                   on Pattern Analysis and Machine Intelligence (TPAMI),
     1, 3                                                                      42(2):398–412, 2019. 5
[56] Kemal Oksuz, Baris Can Cam, Emre Akbas, and Sinan                    [68] Karen Simonyan and Andrew Zisserman. Very deep convo-
     Kalkan. A ranking-based, balanced loss function unifying                  lutional networks for large-scale image recognition. arXiv
     classification and localisation in object detection. Advances             preprint arXiv:1409.1556, 2014. 4
     in Neural Information Processing Systems (NeurIPS),                  [69] Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng
     33:15534–15545, 2020. 2                                                   Xu, Wei Zhan, Masayoshi Tomizuka, Lei Li, Zehuan Yuan,
[57] Kemal Oksuz, Baris Can Cam, Emre Akbas, and Sinan                         Changhu Wang, et al. Sparse R-CNN: End-to-end ob-
     Kalkan. Rank & sort loss for object detection and in-                     ject detection with learnable proposals. In Proceedings of
     stance segmentation. In Proceedings of the IEEE/CVF In-                   the IEEE/CVF Conference on Computer Vision and Pattern
     ternational Conference on Computer Vision (ICCV), pages                   Recognition (CVPR), pages 14454–14463, 2021. 2
     3009–3018, 2021. 2                                                   [70] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet,
[58] Shuvo Kumar Paul, Muhammed Tawfiq Chowdhury,                              Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent
     Mircea Nicolescu, Monica Nicolescu, and David Feil-                       Vanhoucke, and Andrew Rabinovich. Going deeper with
     Seifer. Object detection and pose estimation from rgb and                 convolutions. In Proceedings of the IEEE/CVF Confer-
     depth data for real-time, adaptive robotic grasping. In Ad-               ence on Computer Vision and Pattern Recognition (CVPR),
     vances in Computer Vision and Computational Biology,                      pages 1–9, 2015. 5
     pages 121–142. 2021. 1                                               [71] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon
[59] Siyuan Qiao, Liang-Chieh Chen, and Alan Yuille. De-                       Shlens, and Zbigniew Wojna. Rethinking the inception
     tectoRS: Detecting objects with recursive feature pyramid                 architecture for computer vision. In Proceedings of the
     and switchable atrous convolution. In Proceedings of the                  IEEE/CVF Conference on Computer Vision and Pattern
     IEEE/CVF Conference on Computer Vision and Pattern                        Recognition (CVPR), pages 2818–2826, 2016. 2
     Recognition (CVPR), pages 10213–10224, 2021. 2                       [72] Mingxing Tan and Quoc Le. EfficientNet: Rethinking
[60] Ilija Radosavovic, Raj Prateek Kosaraju, Ross Girshick,                   model scaling for convolutional neural networks. In Inter-
     Kaiming He, and Piotr Dollár. Designing network design                   national Conference on Machine Learning (ICML), pages
     spaces. In Proceedings of the IEEE/CVF Conference on                      6105–6114, 2019. 2, 3
     Computer Vision and Pattern Recognition (CVPR), pages                [73] Mingxing Tan and Quoc Le. EfficientNetv2: Smaller mod-
     10428–10436, 2020. 2                                                      els and faster training. In International Conference on Ma-
[61] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali                    chine Learning (ICML), pages 10096–10106, 2021. 2
     Farhadi. You only look once: Unified, real-time object de-           [74] Mingxing Tan, Ruoming Pang, and Quoc V Le. Efficient-
     tection. In Proceedings of the IEEE/CVF Conference on                     Det: Scalable and efficient object detection. In Proceedings
     Computer Vision and Pattern Recognition (CVPR), pages                     of the IEEE/CVF Conference on Computer Vision and Pat-
     779–788, 2016. 2, 5                                                       tern Recognition (CVPR), pages 10781–10790, 2020. 2, 10
[62] Joseph Redmon and Ali Farhadi. YOLO9000: better, faster,             [75] Antti Tarvainen and Harri Valpola. Mean teachers are better
     stronger. In Proceedings of the IEEE/CVF Conference on                    role models: Weight-averaged consistency targets improve
     Computer Vision and Pattern Recognition (CVPR), pages                     semi-supervised deep learning results. Advances in Neural
     7263–7271, 2017. 2                                                        Information Processing Systems (NeurIPS), 30, 2017. 2, 6
[63] Joseph Redmon and Ali Farhadi. YOLOv3: An incremental                [76] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:
     improvement. arXiv preprint arXiv:1804.02767, 2018. 1, 2                  Fully convolutional one-stage object detection. In Proceed-

                                                                     14
     ings of the IEEE/CVF International Conference on Com-                    Wang, Yuning Du, et al. PP-PicoDet: A better real-
     puter Vision (ICCV), pages 9627–9636, 2019. 2                            time object detector on mobile devices. arXiv preprint
[77] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:                     arXiv:2111.00902, 2021. 1
     A simple and strong anchor-free object detector. IEEE               [89] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun
     Transactions on Pattern Analysis and Machine Intelligence                Zhu, Lionel M Ni, and Heung-Yeung Shum. DINO: DETR
     (TPAMI), 44(4):1922–1933, 2022. 2                                        with improved denoising anchor boxes for end-to-end ob-
[78] Pavan Kumar Anasosalu Vasu, James Gabriel, Jeff                          ject detection. arXiv preprint arXiv:2203.03605, 2022. 10
     Zhu, Oncel Tuzel, and Anurag Ranjan.               An im-           [90] Haoyang Zhang, Ying Wang, Feras Dayoub, and Niko Sun-
     proved one millisecond mobile backbone. arXiv preprint                   derhauf. VarifocalNet: An IoU-aware dense object detector.
     arXiv:2206.04040, 2022. 2                                                In Proceedings of the IEEE/CVF Conference on Computer
[79] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-                            Vision and Pattern Recognition (CVPR), pages 8514–8523,
     Yuan Mark Liao. Scaled-YOLOv4: Scaling cross stage                       2021. 5
     partial network. In Proceedings of the IEEE/CVF Confer-             [91] Shifeng Zhang, Cheng Chi, Yongqiang Yao, Zhen Lei, and
     ence on Computer Vision and Pattern Recognition (CVPR),                  Stan Z Li. Bridging the gap between anchor-based and
     pages 13029–13038, 2021. 2, 3, 6, 7                                      anchor-free detection via adaptive training sample selec-
[80] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,                        tion. In Proceedings of the IEEE/CVF Conference on Com-
     Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. CSP-                       puter Vision and Pattern Recognition (CVPR), pages 9759–
     Net: A new backbone that can enhance learning capabil-                   9768, 2020. 5
     ity of CNN. In Proceedings of the IEEE/CVF Conference               [92] Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, and Jian
     on Computer Vision and Pattern Recognition Workshops                     Sun. ShuffleNet: An extremely efficient convolutional neu-
     (CVPRW), pages 390–391, 2020. 1                                          ral network for mobile devices. In Proceedings of the
[81] Chien-Yao Wang, I-Hau Yeh, and Hong-Yuan Mark Liao.                      IEEE/CVF Conference on Computer Vision and Pattern
     You only learn one representation: Unified network for                   Recognition (CVPR), pages 6848–6856, 2018. 1
     multiple tasks. arXiv preprint arXiv:2105.04206, 2021. 1,           [93] Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Zehuan
     2, 6, 7, 10                                                              Yuan, Ping Luo, Wenyu Liu, and Xinggang Wang. BYTE-
[82] Jianfeng Wang, Lin Song, Zeming Li, Hongbin Sun, Jian                    Track: Multi-object tracking by associating every detection
     Sun, and Nanning Zheng. End-to-end object detection                      box. arXiv preprint arXiv:2110.06864, 2021. 1
     with fully convolutional network. In Proceedings of the             [94] Yifu Zhang, Chunyu Wang, Xinggang Wang, Wenjun Zeng,
     IEEE/CVF Conference on Computer Vision and Pattern                       and Wenyu Liu. FAIRMOT: On the fairness of detec-
     Recognition (CVPR), pages 15849–15858, 2021. 2, 5                        tion and re-identification in multiple object tracking. Inter-
[83] Bichen Wu, Chaojian Li, Hang Zhang, Xiaoliang Dai,                       national Journal of Computer Vision, 129(11):3069–3087,
     Peizhao Zhang, Matthew Yu, Jialiang Wang, Yingyan Lin,                   2021. 1
     and Peter Vajda. FBNetv5: Neural architecture search for            [95] Zhaohui Zheng, Ping Wang, Wei Liu, Jinze Li, Rongguang
     multiple tasks in one run. arXiv preprint arXiv:2111.10007,              Ye, and Dongwei Ren. Distance-IoU loss: Faster and bet-
     2021. 1                                                                  ter learning for bounding box regression. In Proceedings
[84] Yunyang Xiong, Hanxiao Liu, Suyog Gupta, Berkin Akin,                    of the AAAI Conference on Artificial Intelligence (AAAI),
     Gabriel Bender, Yongzhe Wang, Pieter-Jan Kindermans,                     volume 34, pages 12993–13000, 2020. 2
     Mingxing Tan, Vikas Singh, and Bo Chen. MobileDets:                 [96] Dingfu Zhou, Jin Fang, Xibin Song, Chenye Guan, Junbo
     Searching for object detection architectures for mobile ac-              Yin, Yuchao Dai, and Ruigang Yang. IoU loss for 2D/3D
     celerators. In Proceedings of the IEEE/CVF Conference on                 object detection. In International Conference on 3D Vision
     Computer Vision and Pattern Recognition (CVPR), pages                    (3DV), pages 85–94, 2019. 2
     3825–3834, 2021. 1                                                  [97] Xingyi Zhou, Dequan Wang, and Philipp Krähenbühl. Ob-
[85] Shangliang Xu, Xinxin Wang, Wenyu Lv, Qinyao                             jects as points. arXiv preprint arXiv:1904.07850, 2019. 1,
     Chang, Cheng Cui, Kaipeng Deng, Guanzhong Wang,                          2
     Qingqing Dang, Shengyu Wei, Yuning Du, et al. PP-                   [98] Zongwei Zhou, Md Mahfuzur Rahman Siddiquee, Nima
     YOLOE: An evolved version of YOLO. arXiv preprint                        Tajbakhsh, and Jianming Liang. UNet++: A nested U-
     arXiv:2203.16250, 2022. 2, 7, 8, 10                                      Net architecture for medical image segmentation. In
[86] Zetong Yang, Yin Zhou, Zhifeng Chen, and Jiquan Ngiam.                   Deep Learning in Medical Image Analysis and Multimodal
     3D-MAN: 3D multi-frame attention network for object de-                  Learning for Clinical Decision Support, 2018. 5
     tection. In Proceedings of the IEEE/CVF Conference on               [99] Benjin Zhu, Jianfeng Wang, Zhengkai Jiang, Fuhang Zong,
     Computer Vision and Pattern Recognition (CVPR), pages                    Songtao Liu, Zeming Li, and Jian Sun. AutoAssign: Differ-
     1863–1872, 2021. 5                                                       entiable label assignment for dense object detection. arXiv
[87] Fisher Yu, Dequan Wang, Evan Shelhamer, and Trevor                       preprint arXiv:2007.03496, 2020. 2, 5
     Darrell. Deep layer aggregation. In Proceedings of the             [100] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang,
     IEEE/CVF Conference on Computer Vision and Pattern                       and Jifeng Dai. Deformable DETR: Deformable trans-
     Recognition (CVPR), pages 2403–2412, 2018. 1                             formers for end-to-end object detection. In Proceedings of
[88] Guanghua Yu, Qinyao Chang, Wenyu Lv, Chang Xu, Cheng                     the International Conference on Learning Representations
     Cui, Wei Ji, Qingqing Dang, Kaipeng Deng, Guanzhong                      (ICLR), 2021. 10

                                                                   15
