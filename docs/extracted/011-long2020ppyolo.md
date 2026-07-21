---
source_id: 011
bibtex_key: long2020ppyolo
title: PP-YOLO: An Effective and Efficient Implementation of Object Detector
year: 2020
domain_theme: Fondasi RGB
verified_pdf: 11_PP-YOLO.pdf
char_count: 53521
---

PP-YOLO: An Effective and Efficient Implementation of Object Detector

                                                       Xiang Long, Kaipeng Deng, Guanzhong Wang, Yang Zhang, Qingqing Dang,
                                                         Yuan Gao, Hui Shen, Jianguo Ren, Shumin Han, Errui Ding, Shilei Wen
                                                          {longxiang, dengkaipeng, wangguanzhong, zhangyang57, dangqingqing,
                                                 gaoyuan18, shenhui08, v renjianguo, hanshumin, dingerrui, wenshilei}@baidu.com
                                                                                                 Baidu Inc.
arXiv:2007.12099v3 [cs.CV] 3 Aug 2020

                                                                Abstract                                                               50
                                                                                                                                                                                                                    PP-YOLO (ours)
                                                                                                                                                                                                                    YOLOv4
                                                                                                                                       48
                                                                                                                                                                                                                    EfficientDet
                                                                                                                                                         EfficientDet
                                            Object detection is one of the most important areas in                                     46                                               PP-YOLO (ours)              YOLOv3+ASFF*

                                                                                                            MS-COCO(test-dev) mAP(%)
                                                                                                                                                                                                                    RFB
                                        computer vision, which plays a key role in various prac-                                       44
                                                                                                                                                                                                                    RetinaNet

                                        tical scenarios. Due to limitation of hardware, it is often
                                                                                                                                       42        RetinaNet
                                        necessary to sacrifice accuracy to ensure the infer speed of
                                        the detector in practice. Therefore, the balance between ef-                                   40
                                                                                                                                                                                                     YOLOv4
                                        fectiveness and efficiency of object detector must be con-                                     38

                                        sidered. The goal of this paper is to implement an ob-                                         36
                                                                                                                                                                        YOLOv3+ASFF*

                                        ject detector with relatively balanced effectiveness and ef-                                                                   RFB
                                                                                                                                       34
                                        ficiency that can be directly applied in actual application
                                        scenarios, rather than propose a novel detection model.                                        32
                                                                                                                                            10      20       30   40     50   60   70     80    90     100    110   120      130     140
                                        Considering that YOLOv3 has been widely used in prac-                                                                                      FPS(V100)
                                        tice, we develop a new object detector based on YOLOv3.
                                        We mainly try to combine various existing tricks that al-           Figure 1. Comparison of the proposed PP-YOLO and other state-
                                        most not increase the number of model parameters and                of-the-art object detectors. PP-YOLO runs faster than YOLOv4
                                        FLOPs, to achieve the goal of improving the accuracy of             and improves mAP from 43.5% to 45.2%.
                                        detector as much as possible while ensuring that the speed
                                        is almost unchanged. Since all experiments in this pa-
                                        per are conducted based on PaddlePaddle, we call it PP-             them, the network structures of YOLO to YOLOv3 have
                                        YOLO. By combining multiple tricks, PP-YOLO can achieve             relatively large changes. YOLOv4 considers various strate-
                                        a better balance between effectiveness (45.2% mAP) and              gies such as bag of freebies and bag of specials on the ba-
                                        efficiency (72.9 FPS), surpassing the existing state-of-the-        sis of YOLOv3, which greatly improves the performance of
                                        art detectors such as EfficientDet and YOLOv4. Source               the detector. This paper introduces an improved YOLOv3
                                        code is at https://github.com/PaddlePaddle/                         model based on PaddlePaddle (PP-YOLO). A bunch of
                                        PaddleDetection.                                                    tricks that almost not increase the infer time are added to
                                                                                                            improve the overall performance of the model.
                                                                                                               Unlike YOLOv4, we did not explore different backbone
                                        1. Introduction
                                                                                                            networks and data augmentation methods, nor did we use
                                           Object detection is an important yet challenging task.           NAS to search for hyperparameters. For the backbone, we
                                        In the past few years, thanks to the advance of deep con-           directly use the most common ResNet[13] as the backbone
                                        volutional neural network[18, 13], object detectors have            of PP-YOLO. For data augmentation, we directly used the
                                        achieved remarkable performance[33, 21, 31, 32, 1, 22, 28,          most basic MixUp [43]. One reason is that ResNet is used
                                        9, 45, 2, 5, 37, 20, 4, 15, 35].                                    more wildly, such that various deep learning frameworks
                                           In particular, one stage object detectors have a good bal-       have deeply optimized for ResNet series, which will be
                                        ance between speed and accuracy, and have been widely               more convenient in actual deployment and will have better
                                        used in practice[27, 22, 30, 31, 32, 1]. YOLO series,               infer speed in practical. Another reason is that the replace-
                                        including YOLOv1[30], YOLOv2[31], YOLOv3[32] and                    ment of backbone and data augmentation are relatively in-
                                        YOLOv4[1], is one of the most famous series. Among                  dependent factors, almost irrelevant to the tricks discussed

                                                                                                        1
in this paper. Since there are already a lot of works to study       ization problem, including CornerNet[19], CenterNet[8],
backbone network and to explore data augmentation, we do             ExtremeNet[47] and RepPoint[40]. Breaking the limitation
not repeat them in this paper. Searching for hyperparame-            imposed by hand-craft anchors, anchor-free methods show
ters using NAS often consumes more computing power, so               great potential for extreme object scales and aspect ratios
there is usually no condition to use NAS to perform a hyper-         [16]. The performance of some recently proposed anchor-
parameter search in each new scenario. Therefore, we still           free detectors can also compete with state-of-the-art anchor-
use the manually set parameters following YOLOv3[32].                based detectors.
We believe that using a better backbone network, using                   YOLO series detectors [30, 31, 32, 1] have been widely
more effective data augmentation method and using NAS                used in practice, due to their excellent effectiveness and
to search for hyperparameters can further improve the per-           efficiency. Until the writing of this paper, it has devel-
formance of PP-YOLO.                                                 oped to YOLOv4[1]. YOLOv4 discusses a large number
    The focus of this paper is how to stack some effective           of tricks including many “bag of freebies” which not in-
tricks that hardly affect efficiency to get better performance.      crease the infer time, and several “bag of specials” that in-
Many of these tricks cannot be directly applied to the net-          crease the inference cost by a small amount but can signif-
work structure of YOLOv3, so small modification is re-               icantly improve the accuracy of object detection. YOLOv4
quired. Moreover, where to add tricks also needs care-               greatly improves the effectiveness and efficiency of the
ful consideration and experiment. This paper is not in-              YOLOv3[32]. This paper is also developed based on
tended to introduce a novel object detecotor. It is more             YOLOv3 model and also explored a lot of tricks. Unlike
like a recipe, which tell you how to build a better detec-           YOLOV4, we have not explored some widely studied parts
tor step by step. We have found some tricks that are ef-             such as data augmentation and backbone. Many tricks we
fective for the YOLOv3 detector, which can save devel-               discussed in this paper are different from YOLOV4 and the
opers’ time of trial and error. The final PP-YOLO model              detailed implementation of tricks is also different.
improves the mAP on COCO from 43.5% to 45.2% at a
speed faster than YOLOv4. The code and model is released             3. Method
in the PaddleDetection code-base (https://github.
com/PaddlePaddle/PaddleDetection).                                       An one-stage anchor-based detector is normally made
                                                                     up of a backbone network, a detection neck, which is typ-
2. Related Work                                                      ically a feature pyramid network (FPN), and a detection
                                                                     head for object classification and localization. They are
   Anchor-based methods are still the mainstream of object           also common components in most of the one-stage anchor-
detection [33, 21, 31, 32, 1, 22, 28, 9, 45, 2, 5, 37, 20, 4, 15],   free detectors based on anchor-point. We first revise the de-
which evolved from early proposal based detectors, such              tail structure of YOLOv3 and introduce a modified version
as Fast R-CNN [11]. Their core idea is to introduce an-              which replace the backbone to ResNet50-vd-dcn, which is
chor boxes, which can be viewed as pre-defined propos-               used as the basic baseline in this paper. Then we introduce
als, as a priori for bounding box regression. It mainly              a bunch of tricks which can improve the performance of
includes two branches: one-stage detectors and two-stage             YOLOv3 almost without losing efficiency.
detectors[24]. A large amount of one-stage detectors in-
cluding YOLOv2[31], YOLOv3[32], YOLOv4[1], Reti-                     3.1. Architecture
naNet [22], RefineDet [44], EfficentDet [35], FreeAnchor
[45], and two-stage detectors including faster R-CNN [33]            Backbone The overall architecture of YOLOv3 is shown
FPN[21], Cascade R-CNN[2], Trident-Net[20] are pro-                  in Fig. 2. In original YOLOv3[32], DarkNet-53 is first
posed to promote the growth of state-of-the-art perfor-              applied to extract feature maps at different scales. Since
mance in object detection continuously. Besides, anchor-             ResNet[13] has been widely used and and has been stud-
free detectors have recently received more and more at-              ied more extensively, there are more different variants for
tention. In the past two years, a large number of new                selection, and it has also been better optimized by deep
anchor-free methods have been proposed. The anchor-                  learning frameworks. So, we replace the original backbone
free method actually has a long history. Earlier works               DarkNet-53 with ResNet50-vd in PP-YOLO. Considering
such as YOLOv1[30], DenseBox[14] and UnitBox[41] can                 directly replace DarkNet-53 with ResNet50-vd will hurt the
be considered as early anchor-free detectors. They can               performance of YOLOv3 detector. We replace some con-
be divided into two types. Anchor-point based detec-                 volutional layers in ResNet50-vd with deformable convo-
tors perform object bounding box regression based on an-             lutional layers. The effectiveness of Deformable Convolu-
chor points instead of anchor boxes, including FSAF [49],            tional Networks (DCN) has been verified in many detection
FCOS[36], FoveaBox[17], SAPD[48]. Keypoint based de-                 models. DCN itself will not significantly increase the num-
tectors reformulate the object detection as keypoints local-         ber of parameters and FLOPs in the model, but in practical
                Backbone                               FPN                Feature Pyramid                                                  C
                                                                                                                     YOLO loss       Concatenate
                                                                                                       Head
                 C5                                                         P5                                                        Conv 3×3
                                                                                                                                        C, 2C
                 C4                                                                                    Head          YOLO loss
                                                                                                                                        filter size
                 C3                                                         P4                                                       in dim, out dim

                 C2                                                                                    Head          YOLO loss        Inject Points
                 C1                                                         P3

                                   C5       Conv 1×1
                                                                                                  P5                                    Cross
                                                             Conv Block          Conv Block                           class
                                            512, 512                                                                             K     Entropy
     Conv 3×3           Conv 1×1                                                                                                        Loss
                                                                    Upsample Block                      Conv 3×3
       C, 2C             C, C/2
                                                                                                          C, 2C
                                   C4       Conv 1×1
                                                                                                  P4
                                        C                    Conv Block          Conv Block                            box             L1 Loss
                                            512, 256                                                                             4

     Conv 1×1           Upsample                                                                        Conv 1×1
                                                                    Upsample Block
       2C, C               ×2                                                                           2C, 3(K+5)
                                   C3                                                                                                 Objectness
                                            Conv 1×1                                              P3                             1
                                        C                    Conv Block          Conv Block                                              Loss
                                            256, 128

    Conv Block        Upsample Block                          FPN                                         Head                YOLO loss

Figure 2. The network architecture of YOLOv3 and inject points for PP-YOLO. Activation layers are omitted for brevity. Details are
described in Section 3.1 and Section 3.2.

application, too many DCN layers will greatly increase in-                 3.2. Selection of Tricks
fer time. Therefore, in order to balance the efficiency and
                                                                              The various tricks we used in this paper are described
effectiveness, we only replace 3 × 3 convolution layers in
                                                                           in this section. These tricks are all already existing, which
the last stage with DCNs. We denote this modified back-
                                                                           coming from different works [10, 1, 42, 39, 38, 25, 12]. This
bone as ResNet50-vd-dcn, and the output of stage 3, 4 and
                                                                           paper does not propose an novel detection method, but just
5 as C3 , C4 , C5 .
                                                                           focuses on combining the existing tricks to implement an
Detection Neck Then the FPN [21] is used to build an                       effective and efficient detector. Because many tricks can-
feature pyramid with lateral connections between feature                   not be applied to YOLOv3 directly, we need to adjust them
maps. Feature maps C3 , C4 , C5 are input to the FPN mod-                  according to the its structure.
ule. We denote the output feature maps of pyramid level l                  Larger Batch Size Using a larger batch size can improve
as Pl , where l = 3, 4, 5 in our experiments. The resolution               the stability of training and get better results. Here we
of Pl is W2l
             ×H 2l
                   for an input image of size W × H. The                   change the training batch size from 64 to 192, and adjust
detail structure of FPN is shown in Fig. 2.                                the training schedule and learning rate accordingly.
Detection Head The detection head of YOLOv3 is very                        EMA When training a model, it is often beneficial to main-
simple. It consists of two convolutional layers. A 3 × 3 con-              tain moving averages of the trained parameters. Evaluations
volutional followed by an 1 × 1 convolutional layer is adopt               that use averaged parameters sometimes produce signifi-
to get the final predictions. The output channel of each fi-               cantly better results than the final trained values [35]. The
nal prediction is 3(K + 5), where K is number of classes.                  Exponential Moving Average (EMA) compute the moving
Each position on each final prediction map has been asso-                  averages of trained parameters using exponential decay. For
ciate with three different anchors. For each anchor, the first             each parameter W , we maintain an shadow parameter
K channels are the prediction of probability for K classes.
The following 4 channels are the prediction for bounding                                      WEM A = λWEM A + (1 − λ)W,                          (1)
box localization. The last channel is the prediction of ob-
jectness score. For classification and localization, cross en-             where λ is the decay. We apply EMA with decay λ of
tropy loss and L1 loss is adopt correspondingly. An ob-                    0.9998 and use the shadow parameter WEM A for evalua-
jectness loss [32] is applied to supervise objectness score,               tion.
which is used to identify whether is there an object or not.               DropBlock [10] DropBlock is a form of structured dropout,
where units in a contiguous region of a feature map are          creasing function of their overlaps. However, such process
dropped together. Different from the original paper, we          is sequential like traditional Greedy NMS and could not
only apply DropBlock to the FPN, since we find that adding       be implemented in parallel. Matrix NMS views this pro-
DropBlock to the backbone will lead to a decrease of the         cess from another perspective and implement it in a parallel
performance. The detailed inject points of the DropBlock         manner. Therefore, the Matrix NMS is faster than tradi-
are marked by ”triangles” in Figure 2.                           tional NMS, which will not bring any loss of efficiency.
IoU Loss [42] Bounding box regression is the crucial step in     CoordConv [25] CoordConv, which works by giving con-
object detection. In YOLOv3, L1 loss is adopted for bound-       volution access to its own input coordinates through the use
ing box regression. It is not tailored to the mAP evaluation     of extra coordinate channels. CoordConv allows networks
metric, which is strongly rely on Intersection over Union        to learn either complete translation invariance or varying
(IoU). IoU loss and other variations such as CIoU loss and       degrees of translation dependence. Considering that Coord-
GIoU loss[46, 34] have been proposed to address this prob-       Conv will add two inputs channels to the convolution layer,
lem. Different from YOLOv4, we do not replace the L1-loss        some parameters and FLOPs will be added. In order to re-
with IoU loss directly, we add another branch to calculate       duce the loss of efficiency as much as possible, we do not
IoU loss. We find that the improvements of various IoU loss      change convolutional layers in backbone, and only replace
are similar, so we choose the most basic IoU loss [42].          the 1x1 convolution layer in FPN and the first convolution
IoU Aware [39] In YOLOv3, the classification probabil-           layer in detection head with CoordConv. The detailed in-
ity and objectness score is multiplied as the final detection    ject points of the CoordConv are marked by ”diamonds” in
confidence, which do not consider the localization accu-         Figure 2.
racy. To solve this problem, an IoU prediction branch is         SPP [12] The Spatial Pyramid Pooling (SPP) is first pro-
added to measure the accuracy of localization. During train-     posed by He et al[12]. SPP integrates SPM into CNN
ing, IoU aware loss is adopt to training the IoU prediction      and use max-pooling operation instead of bag-of-word op-
branch. During inference, the predicted IoU is multiplied        eration. YOLOv4 apply SPP module by concatenating
by the classification probability and objectiveness score to     max-pooling outputs with kernel size k × k, where k =
compute the final detection confidence, which is more cor-       {1, 5, 9, 13}, and stride equals to 1. Under this design, a
related with the localization accuracy. The final detection      relatively large k × k max-pooling effectively increase the
confidence is then used as the input of the subsequent NMS.      receptive field of backbone feature. In detail, the SPP only
IoU aware branch will add additional computational cost.         applied on the top feature map as shown in Figure 2 with
However, only 0.01% number of parameters and 0.0001%             ”star” mark. No parameter are introduced by SPP itself, but
FLOPs are added, which can be almost ignored.                    the number of input channel of the following convolutional
Grid Sensitive[1] Grid Sensitive is an effective trick intro-    layer will increase. So around 2% additional papameters
duced by YOLOv4. When we decode the coordinate of the            and 1% extra FLOPs are introduced.
bounding box center x and y, in original YOLOv3, we can          Better Pretrain Model Using a pretrain model with higher
get them by                                                      classification accuracy on ImageNet may result in better de-
                                                                 tection performance. Here we use the distilled ResNet50-vd
                   x = s · (gx + σ(px )),                 (2)
                                                                 model as the pretrain model [29] . This obviously does not
                   y = s · (gy + σ(py )),                 (3)    affect the efficiency of the detector.
where σ is the sigmoid function, gx and gy are integers and
s is a scale factor. Obviously, x and y cannot be exactly        4. Experiment
equal to s · gx or s · (gx + 1). This makes it difficult to         In this section, we present the effectiveness of differ-
predict the centres of bounding boxes that just located on       ent tricks. Experiments were carried out on the bounding
the grid boundary. We can address this problem, by change        box detection track of the COCO dataset [23]. Following
the equation to                                                  the common practice [32, 35, 1], we use trainval35k
          x = s · (gx + α · σ(px ) − (α − 1)/2),          (4)    split for training, which contains ∼118k images, minival
                                                                 split (5k) for validation and ablation study, and test-dev
           y = s · (gy + α · σ(py ) − (α − 1)/2),         (5)
                                                                 split(∼20k) for testing.
where α is set to 1.05 in this paper. This makes it easier for
the model to predict bounding box center exactly located on      4.1. Implementation Details
the grid boundary. The FLOPs added by Grid Sensitive is             We use ResNet50-vd-dcn[13] as the backbone networks
really small, and can be totally ignored.                        unless specified. The architecture of FPN and head in our
Matrix NMS [38] Matrix NMS is motivated by Soft-NMS,             basic models is completely the same as YOLOv3[32]. The
which decays the other detection scores as amonotonic de-        details have been presented in section 3.1. We initialize
                   Methods                           mAP(%)        Parameters       GFLOPs        infer time   FPS
              A    Darknet53 YOLOv3                  38.9          59.13 M          65.52         17.2 ms      58.2
              B    ResNet50-vd-dcn YOLOv3            39.1          43.89 M          44.71         12.6 ms      79.2
              C    B + LB + EMA + DropBlock          41.4          43.89 M          44.71         12.6 ms      79.2
              D    C + IoU Loss                      41.9          43.89 M          44.71         12.6 ms      79.2
              E    D + Iou Aware                     42.5          43.90 M          44.71         13.3 ms      74.9
              F    E + Grid Sensitive                42.8          43.90 M          44.71         13.4 ms      74.8
              G    F + Matrix NMS                    43.5          43.90 M          44.71         13.4 ms      74.8
              H    G + CoordConv                     44.0          43.93 M          44.76         13.5ms       74.1
              I    H + SPP                           44.3          44.93 M          45.12         13.7 ms      72.9
              J    I + Better ImageNet Pretrain      44.6          44.93 M          45.12         13.7 ms      72.9
                                Table 1. The ablation study of tricks on the MS-COCO minival split.

our detectors following common practice. Specifically, our          a larger batch size and EMA to improve the stability of the
backbone networks are initialized with the weights pre-             model, and also apply DropBlock to prevent the model from
trained on ImageNet[7]. For the FPN and detection heads,            overfitting. After using these strategies, the mAP of model
we initialize them randomly as same as in YOLOv3[32].               (C) increases to 41.4% without any loss of efficiency.
For the baseline model (A, B), The training schedule is as
                                                                    C → F Next, we consider modifying the YOLO loss to im-
same as YOLOv3. Under larger batch size setting, the entire
                                                                    prove the effectiveness of the model, because modifying the
network is trained with stochastic gradient descent (SGD)
                                                                    loss generally only has an impact on the training process,
for 250K iterations with the initial learning rate being 0.01
                                                                    and will not or rarely affect the infer time. We add IoU
and a minibatch of 192 images distributed on 8 GPUs. The
                                                                    Loss (D), IoU Aware (E) and Grid Sensitive (F) modules,
learning rate is divided by 10 at iteration 150K and 200K,
                                                                    and increase the mAP by 0.5%, 0.6% and 0.3% respec-
respectively. Weight decay is set as 0.0005, and momentum
                                                                    tively. Among them, IoU loss will not affect the number
is set as 0.9. Multi-scale training from 320 to 608 pixels is
                                                                    of parameters and the infer time at all. IoU Aware and Grid
applied. MixUp[43] is adopted for data augmentation.
                                                                    Sensitive will increase the post-processing time by 0.7ms
4.2. Ablation Study                                                 and 0.1ms, since the current implementation is not efficient
                                                                    enough, which can be greatly reduced by merging them as
    In this section, we present the effectiveness of each mod-      a single OP in PaddlePaddle in the future. On the whole,
ule in an incremental manner. The reason is that each trick is      we have increased the mAP of PP-YOLO from 41.4% to
not completely independent. Some tricks are effective when          42.8%.
applied alone, but they are not effective when combined to-
gether. Since there are too many combinations of various            F → G Post-processing is also a place where we can im-
tricks, it is difficult to conduct a comprehensive analysis.        prove the performance. We use Matrix NMS (G) to replace
Therefore, we show how to improve the performance of                traditional greedy NMS. We can see that the mAP has im-
the object detector step by step in the order of our explo-         proved by 0.6%. Since the infer time in Table 1 does not
ration and discovering the effectiveness of tricks. Results         consider NMS, so the influence is not shown here. In fact,
are shown in Table 1, where infer time and FPS do not con-          the overall infer time is decreased since the efficiency of
sider the influence of NMS following YOLOv4[1].                     MatrixNMS is higher than traditional NMS.
A → B First of all, we try to build a basic version of PP-          G → I It has become difficult to continue to improve mAP
YOLO. Because the ResNet[13] series is more widely used,            without increasing the number of parameters and FLOPs.
we first replace the original YOLOv3 backbone Darknet53             So we considered two methods that only increase a few
with ResNet50-vd. However, we found that it will cause              parameters and FLOPs but can bring effective improve-
a significant decrease in mAP. Considering that the number          ments, CoordConv (H) and SPP (I). CoordConv will cause
of parameters and FLOPs of ResNet50-vd are much smaller             the input channel of convolutional layers increase by 2,
than those of Darknet53, we replace the 3 × 3 convolutional         the number of parameters increases by 0.03M, and FLOPs
layer in the last stage of ResNet with deformable convolu-          increases by 0.05G, which is very small compared to the
tion layer[6]. In this way, we get a basic PP-YOLO model            whole model. It can bring an improvement of 0.5% mAP.
(B) with a mAP of 39.1%, which is slightly higher than the          SPP itself does not increase the parameters, but it will in-
original YOLOv3 (A), but its parameters, FLOPs and infer            crease the input channel of the convolutional layer just fol-
time are much smaller than the original YOLOv3 model.               lowing it, resulting in an increase of the parameters by 1M
B → C We first try to optimize the training strategy. We use        and FLOPs by 0.36G. It can improve the mAP of PP-YOLO
                                                                  FPS (V100)
  Method                     Backbone              Size                                AP      AP50       AP75      APS     APM       APL
                                                            w/o TRT with TRT
  RetinaNet [22]              ResNet-50             640         37           -        37.0%       -         -         -       -         -
  RetinaNet [22]              ResNet-101            640        29.4          -        37.9%       -         -         -       -         -
  RetinaNet [22]              ResNet-50            1024        19.6          -        40.1%       -         -         -       -         -
  RetinaNet [22]              ResNet-101           1024        15.4          -        41.1%       -         -         -       -         -
  EfficientDet-D0 [35]        Efficient-B0          512       98.0+          -        33.8% 52.2% 35.8% 12.0% 38.3% 51.2%
  EfficientDet-D1 [35]        Efficient-B1          640       74.1+          -        39.6% 58.6% 42.3% 17.9% 44.3% 56.0%
  EfficientDet-D2 [35]        Efficient-B2          768       56.5+          -        43.0% 62.3% 46.2% 22.5% 47.0% 58.4%
  EfficientDet-D2 [35]        Efficient-B3          896       34.5+          -        45.8% 65.0% 49.3% 26.6% 49.4% 59.8%
  RFBNet[3]                   HarDNet68             512        41.5          -        33.9% 54.3% 36.2% 14.7% 36.6% 50.5%
  RFBNet[3]                   HarDNet85             512        37.1          -        36.8% 57.1% 39.5% 16.9% 40.5% 52.9%
  YOLOv3 + ASFF* [26] Darknet-53                    320         60           -        38.1% 57.4% 42.1% 16.1% 41.6% 53.6%
  YOLOv3 + ASFF* [26] Darknet-53                    416         54           -        40.6% 60.6% 45.1% 20.3% 44.2% 54.1%
  YOLOv3 + ASFF* [26] Darknet-53                    608        45.5          -        42.4% 63.0% 47.4% 25.5% 45.7% 52.3%
  YOLOv3 + ASFF* [26] Darknet-53                    800        29.4          -        43.9% 64.1% 49.2% 27.0% 46.6% 53.4%
  YOLOv4 [1]                  CSPDarknet-53         416         96        164.0∗      41.2% 62.8% 44.3% 20.4% 44.4% 56.0%
  YOLOv4 [1]                  CSPDarknet-53         512         83        138.4∗      43.0% 64.9% 46.5% 24.3% 46.1% 55.2%
  YOLOv4 [1]                  CSPDarknet-53         608         62        105.5∗      43.5% 65.7% 47.3% 26.7% 46.7% 53.3%
  PP-YOLO                     ResNet50-vd-dcn 320             132.2        242.2      39.3% 59.3% 42.7% 16.7% 41.4% 57.8%
  PP-YOLO                     ResNet50-vd-dcn 416             109.6        215.4      42.5% 62.8% 46.5% 21.2% 45.2% 58.2%
  PP-YOLO                     ResNet50-vd-dcn 512              89.9        188.4      44.4% 64.6% 48.8% 24.4% 47.1% 58.2%
  PP-YOLO                     ResNet50-vd-dcn 608              72.9        155.6      45.2% 65.2% 49.9% 26.3% 47.8% 57.2%
Table 2. Comparison of the speed and accuracy of different object detectors on the MS-COCO (test-dev 2017). We compare the results with
batch size = 1, without tensorRT (w/o TRT) or with tensorRT(with TRT). Results marked by ”+” are updated results from the corresponding
official code base, which are higher than the results in original paper. Results marked by ”*” are test in our environment using official code
and model, which are slightly higher than results reported in official code-base.

by 0.3% further. After adding these two modules, the infer                ported in official code-base.
time has increased by 0.3ms.                                                 Compared with other state-of-the-art methods, our PP-
I → J Replacing the pre-trained model is a very common                    YOLO has certain advantages in speed and accuracy. For
approach. However, the accuracy of pretrained classifica-                 example, compared with YOLOv4, our PPYOLO can in-
tion model is higher does not mean that the final detection               creased the mAP on COCO from 43.5% to 45.2% with FPS
model is more effective, and the degree of improvement will               improved from 62 to 72.9. It is worth noticing that tensorRT
be affected by the tricks we used. So we consider it at the               accelerates the PP-YOLO model more obviously. The rel-
end. For fair comparisons, we still use ImageNet for pre-                 ative improvement of PP-YOLO (around 100%) is larger
training. We use a distilled ResNet50-vd model for back-                  than YOLOv4(around 70%). We speculate that it is mainly
bone initialization. The mAP of PP-YOLO can be further                    because tensorRT optimizes for ResNet model better than
improved by 0.3%. In fact, using other detection datasets                 Darknet.
for pre-training can greatly improve the performance of the                  In addition, we can get a series of PP-YOLO results by
model, but this is beyond the scope of this paper.                        changing the input size of the image. Here we also show
                                                                          the results for 320, 416, 512 and 608 input sizes. Figure 1
4.3. Comparison with Other State-of-the-Art De-                           shows that PP-YOLO results have advantages in the balance
     tectors                                                              of speed and accuracy compared with other detectors.
   Comparison of the results on MS-COCO test split with
                                                                          5. Conclusions
other state-of-the-art object detectors are shown in Figure
1 and Table 2. The FPS results of PP-YOLO and other                          This paper introduce a new implementation of object
methods are all tested on V100 with batch size = 1. We                    detector based on PaddlePaddle, called PP-YOLO. PP-
considered two different test conditions, without tensorRT                YOLO is faster (FPS) and more accurate(COCO mAP) than
(w/o TRT) and with tensorRT (with TRT). The test methods                  other state-of-the-art detectors, such as EfficientDet and
are consistent with YOLOv4[1]. Results marked by ”+” are                  YOLOv4. In this paper, we explore a lot of tricks and
updated results from the corresponding official code-base,                show how to combine these tricks on the YOLOv3 detec-
which are higher than the results in original paper, Results              tor and demonstrate their effectiveness. We hope this paper
marked by ”*” are test in our environment using official                  can help developers and researchers save exploration time
code and model, which are slightly higher than results re-                and get better performance in practical applications.
References                                                         the IEEE conference on computer vision and pattern
                                                                   recognition, pages 770–778, 2016. 1, 2, 4, 5
 [1] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao.
                                                              [14] L. Huang, Y. Yang, Y. Deng, and Y. Yu. Densebox:
     Yolov4: Optimal speed and accuracy of object detec-
                                                                   Unifying landmark localization with end to end object
     tion. arXiv preprint arXiv:2004.10934, 2020. 1, 2, 3,
                                                                   detection. arXiv preprint arXiv:1509.04874, 2015. 2
     4, 5, 6
                                                              [15] B. Jiang, R. Luo, J. Mao, T. Xiao, and Y. Jiang. Ac-
 [2] Z. Cai and N. Vasconcelos. Cascade r-cnn: Delving
                                                                   quisition of localization confidence for accurate object
     into high quality object detection. In Proceedings of
                                                                   detection. In ECCV, pages 784–799, 2018. 1, 2
     the IEEE conference on computer vision and pattern
     recognition, pages 6154–6162, 2018. 1, 2                 [16] W. Ke, T. Zhang, Z. Huang, Q. Ye, J. Liu, and
                                                                   D. Huang. Multiple anchor learning for visual object
 [3] P. Chao, C.-Y. Kao, Y.-S. Ruan, C.-H. Huang, and Y.-          detection. arXiv preprint arXiv:1912.02252, 2019. 2
     L. Lin. Hardnet: A low memory traffic network. In
                                                              [17] T. Kong, F. Sun, H. Liu, Y. Jiang, and J. Shi. Fove-
     Proceedings of the IEEE international conference on
                                                                   abox: Beyond anchor-based object detector. arXiv
     computer vision, 2019. 6
                                                                   preprint arXiv:1904.03797, 2019. 2
 [4] J. Choi, D. Chun, H. Kim, and H.-J. Lee. Gaussian        [18] A. Krizhevsky, I. Sutskever, and G. E. Hinton. Im-
     yolov3: An accurate and fast object detector using            agenet classification with deep convolutional neural
     localization uncertainty for autonomous driving. In           networks. In Advances in neural information process-
     IEEE ICCV, pages 502–511, 2019. 1, 2                          ing systems, pages 1097–1105, 2012. 1
 [5] J. Dai, Y. Li, K. He, and J. Sun. R-fcn: Object de-      [19] H. Law and J. Deng. Cornernet: Detecting objects
     tection via region-based fully convolutional networks.        as paired keypoints. In Proceedings of the European
     In Advances in neural information processing systems,         Conference on Computer Vision (ECCV), pages 734–
     pages 379–387, 2016. 1, 2                                     750, 2018. 2
 [6] J. Dai, H. Qi, Y. Xiong, Y. Li, G. Zhang, H. Hu,         [20] Y. Li, Y. Chen, N. Wang, and Z. Zhang. Scale-aware
     and Y. Wei. Deformable convolutional networks. In             trident networks for object detection. In Proceedings
     Proceedings of the IEEE international conference on           of the IEEE International Conference on Computer Vi-
     computer vision, pages 764–773, 2017. 5                       sion, 2019. 1, 2
 [7] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and        [21] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan,
     L. Fei-Fei. Imagenet: A large-scale hierarchical im-          and S. Belongie. Feature pyramid networks for object
     age database. In 2009 IEEE conference on computer             detection. In Proceedings of the IEEE conference on
     vision and pattern recognition, pages 248–255. Ieee,          computer vision and pattern recognition, pages 2117–
     2009. 5                                                       2125, 2017. 1, 2, 3
 [8] K. Duan, S. Bai, L. Xie, H. Qi, Q. Huang, and Q. Tian.   [22] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár.
     Centernet: Object detection with keypoint triplets. In        Focal loss for dense object detection. In Proceedings
     Proceedings of the IEEE International Conference on           of the IEEE international conference on computer vi-
     Computer Vision, 2019. 2                                      sion, pages 2980–2988, 2017. 1, 2, 6
 [9] C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg.    [23] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona,
     DSSD: Deconvolutional single shot detector. In arXiv          D. Ramanan, P. Dollár, and C. L. Zitnick. Microsoft
     preprint arXiv:1701.06659, 2016. 1, 2                         coco: Common objects in context. In European con-
                                                                   ference on computer vision, pages 740–755. Springer,
[10] G. Ghiasi, T.-Y. Lin, and Q. V. Le. Dropblock: A              2014. 4
     regularization method for convolutional networks. In
     NeurIPS, 2018. 3                                         [24] L. Liu, W. Ouyang, XiaogangWang, P. Fieguth,
                                                                   J. Chen, X. Liu, and M. Pietikainen. Deep learning
[11] R. B. Girshick. Fast R-CNN. In IEEE ICCV, pages               for generic object detection: A survey. Int. J. Comp.
     1440–1448, 2015. 2                                            Vis., 2019. 2
[12] K. He, X. Zhang, S. Ren, and J. Sun. Spatial pyra-       [25] R. Liu, J. Lehman, P. Molino, F. P. Such, E. Frank,
     mid pooling in deep convolutional networks for visual         A. Sergeev, and J. Yosinski. An intriguing failing of
     recognition. IEEE transactions on pattern analysis            convolutional neural networks and the coordconv so-
     and machine intelligence, 37(9):1904–1916, 2015. 3,           lution. In NeurIPS, pages 9605–9616, 2018. 3, 4
     4                                                        [26] S. Liu, D. Huang, and Y. Wang. Learning spatial fu-
[13] K. He, X. Zhang, S. Ren, and J. Sun. Deep resid-              sion for single-shot object detection. arXiv preprint
     ual learning for image recognition. In Proceedings of         arXiv:1911.09516, 2019. 6
[27] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed,       [41] J. Yu, Y. Jiang, Z. Wang, Z. Cao, and T. Huang. Unit-
     C.-Y. Fu, and A. C. Berg. Ssd: Single shot multibox            box: An advanced object detection network. In Pro-
     detector. In European conference on computer vision,           ceedings of the 24th ACM international conference on
     pages 21–37. Springer, 2016. 1                                 Multimedia, pages 516–520. ACM, 2016. 2
[28] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. E.          [42] J. Yu, Y. Jiang, Z. Wang, Z. Cao, and T. Huang. Unit-
     Reed, C. Fu, and A. C. Berg. SSD: single shot multi-           box: An advanced object detection network. In MM,
     box detector. In ECCV, pages 21–37, 2016. 1, 2                 2016. 3, 4
[29] PaddleClas.        Introduction of model compres-         [43] H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-
     sion methods. [EB/OL]. https://github.                         Paz. mixup: Beyond empirical risk minimization. In
     com/PaddlePaddle/PaddleClas/blob/                              ICLR, 2018. 1, 5
     master/docs/en/advanced_tutorials/                        [44] S. Zhang, L. Wen, X. Bian, Z. Lei, and S. Z. Li.
     distillation/distillation_en.md. 4                             Single-shot refinement neural network for object de-
[30] J. Redmon, S. K. Divvala, R. B. Girshick, and                  tection. In Proceedings of the IEEE Conference
     A. Farhadi. You only look once: Unified, real-time ob-         on Computer Vision and Pattern Recognition, pages
     ject detection. In IEEE CVPR, pages 779–788, 2016.             4203–4212, 2018. 2
     1, 2                                                      [45] X. Zhang, F. Wan, C. Liu, R. Ji, and Q. Ye. Freean-
[31] J. Redmon and A. Farhadi. Yolo9000: better, faster,            chor: Learning to match anchors for visual object de-
     stronger. In Proceedings of the IEEE conference on             tection. In Advances in neural information processing
     computer vision and pattern recognition, pages 7263–           systems, 2019. 1, 2
     7271, 2017. 1, 2
                                                               [46] Z. Zheng, P. Wang, W. Liu, J. Li, R. Ye, and
[32] J. Redmon and A. Farhadi. Yolov3: An incremen-                 D. Ren. Distance-iou loss: Faster and better learning
     tal improvement. arXiv preprint arXiv:1804.02767,              for bounding box regression. In AAAI, 2020. 4
     2018. 1, 2, 3, 4, 5
                                                               [47] X. Zhou, J. Zhuo, and P. Krahenbuhl. Bottom-up ob-
[33] S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn:          ject detection by grouping extreme and center points.
     Towards real-time object detection with region pro-            In Proceedings of the IEEE Conference on Computer
     posal networks. In Advances in neural information              Vision and Pattern Recognition, pages 850–859, 2019.
     processing systems, pages 91–99, 2015. 1, 2                    2
[34] H. Rezatofighi, N. Tsoi, J. Gwak, A. Sadeghian,           [48] C. Zhu, F. Chen, Z. Shen, and M. Savvides.
     I. Reid, and S. Savarese. Generalized intersection over        Soft anchor-point object detection. arXiv preprint
     union: A metric and a loss for bounding box regres-            arXiv:1911.12448, 2019. 2
     sion. In CVPR, 2019. 4
                                                               [49] C. Zhu, Y. He, and M. Savvides. Feature selective
[35] M. Tan, R. Pang, and Q. V. Le. Efficientdet: Scalable          anchor-free module for single-shot object detection. In
     and efficient object detection. In CVPR, 2020. 1, 2, 3,        The IEEE Conference on Computer Vision and Pattern
     4, 6                                                           Recognition (CVPR), June 2019. 2
[36] Z. Tian, C. Shen, H. Chen, and T. He. Fcos: Fully con-
     volutional one-stage object detection. In Proceedings
     of the IEEE International Conference on Computer Vi-
     sion, 2019. 2
[37] J. Wang, K. Chen, S. Yang, C. C. Loy, and D. Lin.
     Region proposal by guided anchoring. In IEEE CVPR,
     pages 2965–2974, 2019. 1, 2
[38] X. Wang, R. Zhang, T. Kong, L. Li, and C. Shen.
     Solov2: Dynamic, faster and stronger. arXiv preprint
     arXiv:2003.10152, 2020. 3, 4
[39] S. Wu, X. Li, and X. Wang. Iou-aware single-stage
     object detector for accurate localization. Image and
     Vision Computing, page 103911, 2020. 3, 4
[40] Z. Yang, S. Liu, H. Hu, L. Wang, and S. Lin. Rep-
     points: Point set representation for object detection.
     In Proceedings of the IEEE International Conference
     on Computer Vision, 2019. 2
