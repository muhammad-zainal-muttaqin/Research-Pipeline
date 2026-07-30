---
source_id: 137
bibtex_key: zhu2021tphyolov5
title: TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios
year: 2021
domain_theme: Remote Sensing
verified_pdf: 137_TPH_YOLOv5.pdf
char_count: 55553
---

TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for
                                                      Object Detection on Drone-captured Scenarios

                                                             Xingkui Zhu1 *              Shuchang Lyu1 *           Xu Wang 1                Qi Zhao1 †
                                                                                   1
                                                                                       Beihang University, Beijing, China
arXiv:2108.11539v1 [cs.CV] 26 Aug 2021

                                                                       {adlith, lyushuchang, sy2002406, zhaoqi}@buaa.edu.cn

                                                                     Abstract

                                             Object detection on drone-captured scenarios is a re-
                                         cent popular task. As drones always navigate in different
                                         altitudes, the object scale varies violently, which burdens
                                         the optimization of networks. Moreover, high-speed and
                                         low-altitude flight bring in the motion blur on the densely
                                         packed objects, which leads to great challenge of object
                                         distinction. To solve the two issues mentioned above, we
                                         propose TPH-YOLOv5. Based on YOLOv5, we add one
                                         more prediction head to detect different-scale objects. Then
                                         we replace the original prediction heads with Transformer
                                         Prediction Heads (TPH) to explore the prediction poten-
                                         tial with self-attention mechanism. We also integrate con-
                                         volutional block attention model (CBAM) to find attention
                                         region on scenarios with dense objects. To achieve more
                                         improvement of our proposed TPH-YOLOv5, we provide
                                         bags of useful strategies such as data augmentation, multi-
                                         scale testing, multi-model integration and utilizing extra
                                         classifier. Extensive experiments on dataset VisDrone2021
                                         show that TPH-YOLOv5 have good performance with im-
                                         pressive interpretability on drone-captured scenarios. On
                                         DET-test-challenge dataset, the AP result of TPH-YOLOv5
                                         are 39.18%, which is better than previous SOTA method
                                         (DPNetV3) by 1.81%. On VisDrone Challenge 2021, TPH-
                                         YOLOv5 wins 5th place and achieves well-matched results           Figure 1. Intuitive cases to explain the three main problems in ob-
                                         with 1st place model (AP 39.43%). Compared to baseline            ject detection on drone-captured images. The cases in first row,
                                         model (YOLOv5), TPH-YOLOv5 improves about 7%, which               second row and third row respectively shows the size variation,
                                         is encouraging and competitive.                                   high-density and large coverage of objects on drone-captured im-
                                                                                                           ages.

                                         1. Introduction
                                                                                                           ing the performance of object detection on drone-captured
                                            Object detection technology on drone-captured scenarios        images and providing insight for the above-mentioned nu-
                                         has been widely used in many practical applications, such as      merous applications.
                                         plant protection [18, 41], wildlife protection [23, 22] and ur-      Recent years have witnessed significant progresses in ob-
                                         ban surveillance [1, 15]. In this paper, we focus on improv-      ject detection tasks using deep convolutional neural net-
                                           * Contribute Equally.                                           works [40, 37, 34, 27, 58]. Some notable benchmark
                                           † Corresponding author.                                         datasets like MS COCO [30] and PASCALVOC [9] greatly
Figure 2. The overview of working pipeline using TPH-YOLOv5. Compared to original version, we mainly improve the head by applying
Transformer Prediction Head (TPH). We also add one more head to better detect different scale objects. In addition, we employ bag of
tricks like data augmentation, multi-scale testing, model ensemble and self-trained classifier to make TPH-YOLOv5 stronger.

promote the development of object detection application.             also add multi-scale testing (ms-testing) and multi-model
However, most previous deep convolutional neural net-                ensemble strategies during inference to obtain more con-
works are designed for natural scene images. Directly ap-            vincing detection results. Moreover, through visualizing
plying previous models to tackle object detection task on            the failure cases, we find that our proposed architecture has
drone-captured scenarios mainly has three problems, which            excellent localization ability but poor classification ability,
are intuitively illustrated by some cases in Fig.1. First,           especially on some similar categories like “tricycle” and
the object scale varies violently because the flight altitude        “awning-tricycle”. To solve this problem, we provide a self-
of drones change greatly. Second, drone-captured images              trained classifier (ResNet18 [17]) using the image patches
contain objects with high density, which brings in occlu-            cropping from training data as classification training set.
sion between objects. Third, drone-captured images always            With self-trained classifier, our method has 0.8%∼1.0% im-
contain confusing geographic elements because of covering            provement on AP value.
large area. The above-mentioned three problems make the                  Our contributions are listed as follows:
object detection of drone-captured images very challenging.
   In object detection task, YOLO series [37, 38, 39, 2]                • We add one more prediction head to deal with large
play an important role in one-stage detectors. In this pa-                scale variance of objects.
per, we propose an improved model, TPH-YOLOv5 based
on YOLOv5 [21] to solve the above-mentioned three prob-                 • We integrate the Transformer Prediction Heads (TPH)
lems. The overview of the detection pipeline using TPH-                   into YOLOv5, which can accurately localize objects in
YOLOv5 is shown in Fig.2. We respectively use CSPDark-                    high-density scenes.
net53 [52, 2] and path aggregation network (PANet [33])
as backbone and neck of TPH-YOLOv5, which follows the                   • We integrate CBAM into YOLOv5, which can help the
original version. In the head part, we first introduce one                network to find region of interest in images that have
more head for tiny object detection. Totally, TPH-YOLOv5                  large region coverage.
contains four detection heads separately used for the detec-
tion of tiny, small, medium, large objects. Then, we replace            • We provide useful bag of tricks and filtering some use-
the original prediction heads with Transformer Prediction                 less tricks for object detection task on drone-captured
Heads (TPH) [7, 49] to explore the prediction potential. To               scenarios.
find the attention region in images with large coverage, we
adopt Convolutional Block Attention Module (CBAM [54])                  • We use self-trained classifier to improve the classifica-
to sequentially generate the attention map along channel-                 tion ability on some confusing categories.
wise and spatial-wise dimensions. Compared to YOLOv5,
our improved TPH-YOLOv5 can better deal with drone-
                                                                        • On VisDrone2021 test-challenge dataset, our proposed
captured images.
                                                                          TPH-YOLOv5 achieve 39.18% (AP), outperforming
   To further improve the performance of TPH-YOLOv5,                      DPNetV3 (previous SOTA method) by 1.81%. In Vis-
we employ bag of tricks (Fig.2). Specifically, we adopt data              Drone2021 DET challenge, TPH-YOLOv5 wins 5th
augmentation during training, which promote the adapta-                   place and has minor gap comparing with 1st place
tion for dramatic size changes of objects in images. We                   models.
2. Related Work                                                   a slightly change to NMS, which made Soft-NMS shows
                                                                  a significant improvement over traditional NMS on stan-
2.1. Data Augmentation                                            dard benchmark datasets (such as PASCAL VOC [10] and
    The effectiveness of data augmentation is to expand the       MS COCO [30]). It sets an attenuation function for the
dataset, so that the model has higher robustness to the im-       confidence of adjacent bounding boxes based on the IoU
ages obtained from different environments. Photometric            value instead of completely setting their confidence scores
distortions and geometric distortions are wildly used by re-      to zero and delete them. WBF works differently from NMS.
searchers. As for photometric distortion, we adjusted the         Both NMS and Soft-NMS exclude some boxes, while WBF
hue, saturation and value of the images. In dealing with ge-      merges all boxes to form the final result. Therefore, it can
ometric distortion, we add random scaling, cropping, trans-       solve all the inaccurate predictions of the model. We use
lation, shearing, and rotating. In addition to the above-         WBF to ensemble final models, which performs much bet-
mentioned global pixel augmentation methods, there are            ter than NMS.
some more unique data augmentation methods. Some re-
searchers have proposed methods using multiple images to-         2.3. Object Detection
gether for data augmentation i.e. MixUp [57], CutMix [56]             CNN-based object detectors can be divided into
and Mosaic [2]. MixUp randomly select two samples from            many types: 1) one-stage detectors: YOLOX [11],
the training images to perform random weighted summa-             FCOS [48], DETR [65], Scaled-YOLOv4 [51], Effi-
tion, and the labels of the samples also correspond to the        cientDet [45]. 2) two-stage detectors: VFNet [59],
weighted summation. Unlike occlusion works that gener-            CenterNet2 [62]. 3) anchor-based detectors: Scaled-
ally use zero-pixel ”black cloth” to occlude a image, Cut-        YOLOv4 [51], YOLOv5 [21]. 4) anchor-free detectors:
Mix uses an area of another image to cover the occluded           CenterNet [63], YOLOX [11], RepPoints [55]. Some detec-
area. Mosaic is an improved version of the CutMix. Mosaic         tors are specially designed for Drone-captured images like
stitches four images, which greatly enriches the background       RRNet [4], PENet [46], CenterNet [63] etc. But from the
of the detected object. In addition, batch normalization cal-     perspective of components, they generally consist of two
culates the activation statistics of 4 different images on each   parts, an CNN-based backbone, used for image feature ex-
layer.                                                            traction, and the other part is detection head used to predict
    In TPH-YOLOv5, we use a combination of MixUp, Mo-             the class and bounding box for object. In addition, the ob-
saic and traditional methods in data augmentation.                ject detectors developed in recent years often insert some
                                                                  layers between the backbone and the head, people usually
2.2. Multi-Model Ensemble Method in Object De-                    call this part the neck of the detector. Next, we will sepa-
     tection                                                      rately introduce these three structures in detail.
    Deep learning neural networks are non-linear methods.         Backbone.        The backbone that are often used in-
They provide greater flexibility and can scale in proportion      clude VGG [42], ResNet [17], DenseNet [20], Mo-
to the amount of training data. One disadvantage of this          bileNet [19], EfficientNet [44], CSPDarknet53 [52], Swin
flexibility is that they learn through random training algo-      Transformer [35] etc., rather than networks designed by
rithms, which means that they are sensitive to the details        ourselves. Because these networks have proven that they
of the training data, and may find a different set of weights     have strong feature extraction capabilities on classification
each time they train, resulting in different predictions. This    and other issues. But researchers will also fine-tune the
gives the neural network a high variance. A successful way        backbone to make it more suitable for specific tasks.
to reduce the variance of neural network models is to train       Neck. The neck is designed to make better use of the fea-
multiple models instead of a single model, and combine the        tures extracted by the backbone. It reprocesses and ratio-
predictions of these models.                                      nally uses the feature maps extracted by Backbone at dif-
    There are three different methods to ensemble boxes           ferent stages. Usually, a neck consists of several bottom-up
from different object detection models: Non-maximum sup-          paths and several top-down paths. Neck is a key link in the
pression (NMS) [36], Soft-NMS [53], weighted boxes fu-            target detection framework. The earliest neck is the use of
sion (WBF) [43]. In the NMS method, if the overlap, in-           up and down sampling block. The feature of this method is
tersection over union (IoU) of the boxes is higher than a         that there is no feature layer aggregation operation, such as
certain threshold, they are considered to belong to the same      SSD [34], directly follow the head after the multi-level fea-
object. For each object, NMS only leaves one bounding             ture map. Commonly used path-aggregation blocks in neck
box with the highest confidence, and other bounding boxes         are: FPN [28], PANet [33], NAS-FPN [12], BiFPN [45],
are deleted. Therefore, the box filtering process depends         ASFF [32], SFAM [61].The commonality of these methods
on the choice of this single IoU threshold, which have a          is to repeatedly use various up-and-down sampling, splic-
big impact on model performance. Soft-NMS has made                ing, dot sum or dot product to design aggregation strate-
Figure 3. The architecture of the TPH-YOLOv5. a) CSPDarknet53 backbone with three transformer encoder blocks at the end. b) The
Neck use the structure like PANet. c) Four TPHs (transformer prediction heads) use the feature maps from transformer encoder blocks in
Neck. In addition, the number of each block is marked with orange numbers on the left side of the block.

gies. There are also some additional blocks used in neck,             as our baseline.
like SPP [16], ASPP [5], RFB [31], CBAM [54].                             When we train the model using VisDrone2021
Head. As a classification network, the backbone cannot                dataset [64] with data augmentation strategy (Mosaic and
complete the positioning task, and the head is designed to            MixUp), we find that the results of YOLOv5x are much bet-
be responsible for detecting the location and category of the         ter than YOLOv5s, YOLOv5m and YOLOv5l, and the gap
object by the features maps extracted from the backbone.              of AP value is more than 1.5%. Even though the training
Heads are generally divided into two kinds: one-stage ob-             computation cost of the YOLOv5x model is more than that
ject detector and two-stage object detector. Two-stage de-            of other three models, we still choose to use YOLOv5x to
tectors have long been the dominant method in the field of            pursue the best detection performance. In addition, accord-
object detection, and the most representative one is the R-           ing to the features of drone-captured images, we adjust the
CNN series [14, 13, 40]. Compared with the two-stage de-              parameters of commonly used photometric distortions and
tector, the one-stage detector predicts the bounding box and          geometric distortions.
the class of objects at the same time. The speed advan-
tage of the one-stage detector is obvious, but the accuracy           3.2. TPH-YOLOv5
is lower. For one-stage detectors, the most representative               The framework of TPH-YOLOv5 is illustrated in Fig. 3.
models are YOLO series [37, 38, 39, 2], SSD [34] and Reti-            We modify the original YOLOv5 to make it specialize in
naNet [29].                                                           the VisDrone2021 dataset.
                                                                      Prediction head for tiny objects. We investigate the Vis-
3. TPH-YOLOv5                                                         Drone2021 dataset and find that it contains many extremely
                                                                      small instances, so we add one more prediction head for tiny
3.1. Overview of YOLOv5
                                                                      objects detection. Combined with the other three prediction
   YOLOv5 has four different models including YOLOv5s,                heads, our four-head structure can ease the negative influ-
YOLOv5m, YOLOv5l and YOLOv5x. Generally, YOLOv5                       ence caused by violent object scale variance. As shown in
respectively uses the architecture of CSPDarknet53 with an            Fig. 3, the prediction head (head No.1) we add is generated
SPP layer as backbone, PANet as Neck and YOLO detec-                  from low-level, high-resolution feature map, which is more
tion head [37]. To further optimize the whole architecture,           sensitive to tiny objects. After adding an additional detec-
bag of freebies and specials [2] are provided. Since it is the        tion head, although the computation and memory cost in-
most notable and convenient one-stage detector, we select it          crease, the performance of tiny objects detection gets large
improvement.

                                                                      Figure 5. The overview of CBAM module. Two sequential sub-
                                                                      modules are used to refine feature map that go through CBAM,
                                                                      residual paths are also used.

                                                                      process available.
                                                                      Convolutional block attention module (CBAM).
                                                                      CBAM [54] is a simple but effective attention module.
                                                                      It is a lightweight module that can be integrated into
                                                                      most notable CNN architectures, and it can be trained
                                                                      in an end-to-end manner. Given a feature map, CBAM
                                                                      sequentially infers the attention map along two separate
                                                                      dimensions of channel and spatial, and then multiplies
                                                                      the attention map with the input feature map to perform
                                                                      adaptive feature refinement. The structure of the CBAM
                                                                      module is shown in the Fig. 5. According to the experiment
Figure 4. The architecture of transformer encoder, which contains     in the paper [54], after integrating CBAM into different
two main blocks, a multi-head attention block and a feed-forward      models on different classification and detection datasets,
neural network (MLP). LayerNorm and Dropout layers help the           the performance of the model get large improved, which
network converge better and prevent the network from over fitting.
                                                                      proves the effectiveness of this module.
Multi-head attention can help the current node not only pay at-
tention to the current pixels, but also obtain the semantics of the      On drone-captured images, large covering region always
context.                                                              contains confusing geographical elements. Using CBAM
                                                                      can extract the attention area to help TPH-YOLOv5 resist
Transformer encoder block. Inspired by the vision trans-              the confusing information and focus on useful target ob-
former [6], we replace some convolutional blocks and CSP              jects.
bottleneck blocks in original version of YOLOv5 with                  Ms-testing and model ensemble. We train five different
transformer encoder blocks. The structure is shown in                 models in terms of different perspectives for model ensem-
Fig. 4. Compared to original bottleneck block in CSPDark-             ble. During inference phase, we first perform ms-testing
net53, we believe that transformer encoder block can cap-             strategy on single model. The implementation details of
ture global information and abundant contextual informa-              ms-testing are the following three steps. 1) Scaling the test-
tion. Each transformer encoder contains two sub-layers.               ing image to 1.3 times. 2) Respectively reducing the image
The first sub-layer is a multi-head attention layer and the           to 1 time, 0.83 times, and 0.67 times. 3) Flipping the im-
second one (MLP) is a fully-connected layer. Residual con-            ages horizontally. Finally, we feed the six different-scaling
nections are used between each sub-layer. Transformer en-             images to TPH-YOLOv5 and use NMS to fuse the testing
coder blocks increase the ability to capture different local          predictions.
information. It can also explore the feature representation              On different models, we perform the same ms-testing op-
potential with self-attention mechanism [50]. On the Vis-             eration and fuse the final five predictions by WBF to get the
Drone2021 dataset, transformer encoder blocks have better             final result.
performance on occluded objects with high-density.                    Self-trained classifier. After training the VisDrone2021
   Based on YOLOv5, we only apply transformer encoder                 dataset with TPH-YOLOv5, we test the test-dev dataset and
blocks in the head part to form Transformer Prediction Head           then analyze the results by visualizing the failure cases and
(TPH) and the end of backbone. Because the feature maps               draw a conclusion that TPH-YOLOv5 has excellent local-
at the end of the network have low resolution. Applying               ization ability but poor classification ability. We further ex-
TPH on low-resolution feature maps can decrease the ex-               plore the confusion matrix which is shown in Fig.6, and
pensive computation and memory cost. Moreover, when                   observe that the precision of the some hard categories such
we enlarge the resolution of input images, we optional re-            as tricycle and awning-tricycle are very low. Therefore, we
move some TPH blocks at early layers to make the training             propose an extra self-trained classifier. First, we construct
a training set by cropping the ground-truth bounding boxes
and resizing each image patches to 64×64. Then we select
ResNet18 [17] as classifier network. As shown in experi-
mental results, our method get around 0.8%˜1.0% improve-
ment on AP value with the help of this self-trained classifier.

                                                                  Figure 7. Some images were taken too high, resulting in many
                                                                  small objects, which cannot be recognized.

                                                                  training the model, which can often be of great help to the
                                                                  improvement of mAP. We have analyzed bounding boxes
                                                                  in the VisDrone2021 dataset. When the input image size is
                                                                  set to 1536, there are 622 of 342391 labels are less than 3
                                                                  pixels in size. As shown in Fig. 7, these small objects are
Figure 6. Confusion matrix was made at IoU threshold of 0.45,     hard to recognize. When we use gray squares to cover these
confidence threshold of 0.25.                                     small objects and train our model on the processed dataset,
                                                                  the mAP improves by 0.2, better than not.
                                                                  Ms-testing. When training neural network models for com-
4. Experiments
                                                                  puter vision problems, data augmentation is a technique of-
   We use the testset-challenge and testset-dev of the Vis-       ten used to improve performance and reduce generalization
Drone2021 dataset to evaluate our model, and we report            errors. When using a model to make predictions, image data
mAP (average of all 10 IoU thresholds, ranging from               augmentation of test dataset can also be applied to allow the
[0.5: 0.95]) and AP50. VisDrone2021-DET dataset is the            model to make predictions on multiple different versions of
same as VisDrone2019-DET dataset and VisDrone2018-                images. The prediction of the augmented images can be
DET dataset.                                                      averaged to get better prediction performance.
4.1. Implementation Details                                          We scale the test images to three different sizes in ms-
                                                                  testing, and then flip them horizontally, so that a total of
   We implement TPH-YOLOv5 on Pytorch 1.8.1. All of               6 different images are obtained. After testing six different
our models use an NVIDIA RTX3090 GPU for training and             images and fusing the results, we get the final test result.
testing. In the training phase, we use part of pre-trained
model from yolov5x, because TPH-YOLOv5 and YOLOv5
share most part of backbone (block 0˜8) and some part of          4.2. Comparisons with the State-of-the-art
head (block 10˜13 and block 15˜18), there are many weights
can be transferred from YOLOv5x to TPH-YOLOv5, by us-             On VisDrone2021-DET testset-challenge.
ing these weights we can save a lot of training time.                Due to the limited number of submissions in the Vis-
   Because the VisDrone2021 training set is a bit small,          Drone2021 competition server, we only obtained the re-
we only train the model on VisDrone2021 trainset for 65           sults of 4 models on testset-challenge and the final results
epochs, and the first 2 epochs are used for warm-up. We           of the ensemble of 5 models. We finally got a good score
use adam optimizer for training, and use 3e-4 as the initial      of 39.18 on testset-challenge, which is much higher than
learning rate with the cosine lr schedule. The learning rate      VisDrone2020’s best score of 37.37. Ranked fifth in the
of the last epoch decays to 0.12 of the initial learning rate.    VisDrone 2021 leader board, our score is 0.25 lower than
The size of the input image of our model is very large, the       the 39.43 of the first place. If the number of submissions
long side of the image is 1536 pixels, which leads to the         is not used up, we will definitely get better results. Table
batch size is only 2.                                             1 lists the score of our model, compared with the scores in
Data analysis. According to our previous engineering ex-          the previous year’s VisDrone competition and the scores of
perience, it is very important to walk through dataset before     algorithms submitted by the committee.
   Methods                                mAP (%)       AP50 (%)        result. 1) TPH-YOLOv5-1 use the input image size of 1920
   RetinaNet[29]                           11.81         21.37          and all categories have equal weights. 2) TPH-YOLOv5-
   RefineDet[60]                           14.90         28.76          2 use the input image size of 1536 and all categories have
   DetNet59[26]                            15.26         29.23
                                                                        equal weights. 3) TPH-YOLOv5-3 use the input image size
   Cascade-RCNN[3]                         16.09         31.91
   FPN[28]                                 16.51         32.20          of 1920 and the weight of each category is related to the
   Light-RCNN[25]                          16.53         32.78          number of labels, which is shown in Fig. 8. The more la-
   CornetNet[24]                           17.41         34.12          bels of a certain category, the lower the weight it is given. 4)
   RRNet (2019 2nd )[4]                    29.13         55.82          TPH-YOLOv5-4 use the input image size of 1536 and the
   DPNet-ensemble (2019 SOTA) [8]          29.62         54.00          weight of each category is related to the number of labels.
   SMPNet (2020 2nd )[47]                  35.98         59.53          5) TPH-YOLOv5-5 use the backbone of YOLOv5l and use
   DPNetV3 (2020 SOTA)[47]                 37.37         62.05
   TPH-YOLOv5 ensemble                     39.18           \
                                                                        the input image size of 1536.

Table 1. The comparison of the performance in VisDrone2021
testset-challenge

4.3. Ablation Studies
On VisDrone2021-DET testset-dev. we analyze impor-
tance of each proposed component on local testset-dev as
we cannot test these on VisDrone2021 competition server,
the number of submissions to the competition server is very
valuable. The impact of each component is listed in the ta-
ble 2.
   Methods                              mAP (%)          AP50 (%)
   YOLOv5                                 28.88            49.33
   YOLOv5+P2                          31.03 (↑2.15)    51.61 (↑ 2.28)
   YOLOv5+P2+transformer              32.84 (↑ 1.81)   53.87 (↑ 2.26)
   TPH-YOLOv5 (previous+CBAM)         33.63 (↑ 0.79)   54.77 (↑ 0.90)
   TPH-YOLOv5+ms-testing              34.90 (↑ 1.27)   56.40 (↑ 1.63)
   TPH-YOLOv5+ms-testing+Classifier   35.74 (↑ 0.84)   57.31 (↑ 0.91)

     Table 2. Ablation Study on VisDrone2021 testset-dev.

                                                                                Figure 8. The number of labels of each category.
Effect of extra prediction head. Adding a detection head
for tiny objects makes the number of layers of the origi-               Some detection result on VisDrone2021 testset-
nal YOLOv5x change from 607 to 719, and GFLOPs from                     challenge. We have selected some representative images
219.0 to 259.0. This of course increases the amount of cal-             as the display of the test results. Fig. 9 shows the result
culation, but the mAP improvement is also very high. From               of large objects, tiny objects, dense objects and the image
Fig. 9 we can see that TPH-YOLOv5 performs well when                    covering a large area.
detecting small objects, so the increasing in calculation is
worthwhile.
                                                                        5. Conclusion
Effect of transformer encoder blocks. After using the
transformer encoder block, the total layers of the model de-                In this paper, we add some cutting-edge techniques
crease from 719 to 705, and GFLOPs from 259.0 to 237.3.                 i.e. transformer encoder block, CBAM and some experi-
Use transformer encoder blocks can not only increase mAP,               enced tricks to YOLOv5 and form a state-of-the-art detec-
but also reduce the size of the network. At the same time, it           tor called TPH-YOLOv5, which is especially good at ob-
also plays a role in the detection of dense objects and large           ject detection in drone-captured scenarios. We refresh the
objects.                                                                record of VisDrone2021 dataset, our experiments showed
Effect of model ensemble. We list the mAP of the final re-              that TPH-YOLOv5 achieved state-of-the-art performance in
sults of our five different models in each category and com-            VisDrone2021 dataset. We have tried a large number of fea-
pared them with the fusion model in table 3. In training                tures, and used some of them to improve the accuracy of
phrase, we use different input image sizes and change the               object detector. We hope this report can help developers
weight of each category to make each model unique. So                   and researchers get a better experience in the analysis and
that the final ensemble model can get a relatively balanced             processing of drone-captured scenarios.
        Methods                  all    pedestrian   people   bicycle    car     van    trunk   tricycle   awning-tricycle    bus    motor
        TPH-YOLOv5-1            34.90     27.52      15.32     15.21    65.99   44.23   47.56    23.96         22.11         58.85   28.44
        TPH-YOLOv5-2            34.29     27.97      14.88     14.17    67.63   45.01   44.76    25.12         20.48         55.72   27.74
        TPH-YOLOv5-3            34.68     22.88      16.01     19.26    48.88   42.98   47.82    32.86         35.65         54.16   28.25
        TPH-YOLOv5-4            34.17     23.48      15.79     17.62    49.99   42.76   47.13    31.66         32.21         54.19   27.37
        TPH-YOLOv5-5            33.04     25.98      14.90     13.10    63.05   43.45   42.56    25.20         21.06         53.65   27.10
        TPH-YOLOv5 ensemble     37.32     29.00      16.75     15.69    68.94   49.79   45.16    27.33         24.72         61.80   30.90

             Table 3. Comparison of TPH-YOLOv5 models‘ performances on VisDrone2021 testset-dev for each category.

Figure 9. Some visualization results from our TPH-YOLOv5 on testset-challenge, different category use bounding boxes with different
color. The performance is good at localization tiny objects, dense objects and objects blurred by motion.

6. Acknowledgments                                                          [5] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,
                                                                                Kevin Murphy, and Alan L Yuille. Deeplab: Semantic image
  This work was supported by National Natural Science                           segmentation with deep convolutional nets, atrous convolu-
Foundation of China (62072021).                                                 tion, and fully connected crfs. IEEE transactions on pattern
                                                                                analysis and machine intelligence, 40(4):834–848, 2017.
                                                                            [6] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
References                                                                      Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
 [1] Nicolas Audebert, Bertrand Le Saux, and Sébastien Lefèvre.               Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
     Beyond rgb: Very high resolution urban remote sensing with                 vain Gelly, et al. An image is worth 16x16 words: Trans-
     multimodal deep networks. ISPRS Journal of Photogramme-                    formers for image recognition at scale. arXiv preprint
     try and Remote Sensing, 140:20–32, 2018.                                   arXiv:2010.11929, 2020.
                                                                            [7] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
 [2] Alexey Bochkovskiy, Chien-Yao Wang, and Hong-
                                                                                Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
     Yuan Mark Liao. Yolov4: Optimal speed and accuracy of
                                                                                Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
     object detection. arXiv preprint arXiv:2004.10934, 2020.
                                                                                vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image
 [3] Zhaowei Cai and Nuno Vasconcelos. Cascade r-cnn: Delv-                     is worth 16x16 words: Transformers for image recognition
     ing into high quality object detection. In Proceedings of the              at scale. In 9th International Conference on Learning Rep-
     IEEE conference on computer vision and pattern recogni-                    resentations, ICLR 2021, Virtual Event, Austria, May 3-7,
     tion, pages 6154–6162, 2018.                                               2021, 2021.
 [4] Changrui Chen, Yu Zhang, Qingxuan Lv, Shuo Wei, Xi-                    [8] Dawei Du, Pengfei Zhu, Longyin Wen, Xiao Bian, Haibin
     aorui Wang, Xin Sun, and Junyu Dong. Rrnet: A hybrid                       Lin, Qinghua Hu, Tao Peng, Jiayu Zheng, Xinyao Wang, Yue
     detector for object detection in drone-captured images. In                 Zhang, et al. Visdrone-det2019: The vision meets drone ob-
     Proceedings of the IEEE/CVF International Conference on                    ject detection in image challenge results. In Proceedings of
     Computer Vision Workshops, pages 0–0, 2019.                                the IEEE/CVF International Conference on Computer Vision
     Workshops, pages 0–0, 2019.                                          Daniel Khromov, Ding Yiwei, Doug, Durgesh, and Francisco
 [9] Mark Everingham, Luc Van Gool, Christopher K. I.                     Ingham. ultralytics/yolov5: v5.0 - YOLOv5-P6 1280 mod-
     Williams, John M. Winn, and Andrew Zisserman. The pas-               els, AWS, Supervise.ly and YouTube integrations, Apr. 2021.
     cal visual object classes (VOC) challenge. Int. J. Comput.      [22] Benjamin Kellenberger, Diego Marcos, and Devis Tuia. De-
     Vis., 88(2):303–338, 2010.                                           tecting mammals in uav images: Best practices to address a
[10] Mark Everingham, Luc Van Gool, Christopher KI Williams,              substantially imbalanced dataset with deep learning. Remote
     John Winn, and Andrew Zisserman. The pascal visual object            Sensing of Environment, 216:139–153, 2018.
     classes (voc) challenge. International journal of computer      [23] Benjamin Kellenberger, Michele Volpi, and Devis Tuia. Fast
     vision, 88(2):303–338, 2010.                                         animal detection in UAV images using convolutional neu-
[11] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian                ral networks. In 2017 IEEE International Geoscience and
     Sun. Yolox: Exceeding yolo series in 2021. arXiv preprint            Remote Sensing Symposium, IGARSS 2017, Fort Worth, TX,
     arXiv:2107.08430, 2021.                                              USA, July 23-28, 2017, pages 866–869. IEEE, 2017.
[12] Golnaz Ghiasi, Tsung-Yi Lin, and Quoc V Le. Nas-fpn:            [24] Hei Law and Jia Deng. Cornernet: Detecting objects as
     Learning scalable feature pyramid architecture for object            paired keypoints. In Proceedings of the European confer-
     detection. In Proceedings of the IEEE/CVF Conference                 ence on computer vision (ECCV), pages 734–750, 2018.
     on Computer Vision and Pattern Recognition, pages 7036–         [25] Zeming Li, Chao Peng, Gang Yu, Xiangyu Zhang, Yang-
     7045, 2019.                                                          dong Deng, and Jian Sun. Light-head r-cnn: In defense of
[13] Ross Girshick. Fast r-cnn. In Proceedings of the IEEE inter-         two-stage object detector. arXiv preprint arXiv:1711.07264,
     national conference on computer vision, pages 1440–1448,             2017.
     2015.                                                           [26] Zeming Li, Chao Peng, Gang Yu, Xiangyu Zhang, Yangdong
[14] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra            Deng, and Jian Sun. Detnet: A backbone network for object
     Malik. Rich feature hierarchies for accurate object detection        detection. arXiv preprint arXiv:1804.06215, 2018.
     and semantic segmentation. In Proceedings of the IEEE con-
                                                                     [27] Tsung-Yi Lin, Priya Goyal, Ross B. Girshick, Kaiming He,
     ference on computer vision and pattern recognition, pages
                                                                          and Piotr Dollár. Focal loss for dense object detection. In
     580–587, 2014.
                                                                          IEEE International Conference on Computer Vision, ICCV
[15] Jingjing Gu, Tao Su, Qiuhong Wang, Xiaojiang Du, and                 2017, Venice, Italy, October 22-29, 2017, pages 2999–3007.
     Mohsen Guizani. Multiple moving targets surveillance based           IEEE Computer Society, 2017.
     on a cooperative network for multi-uav. IEEE Commun.
                                                                     [28] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
     Mag., 56(4):82–89, 2018.
                                                                          Bharath Hariharan, and Serge Belongie. Feature pyra-
[16] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
                                                                          mid networks for object detection. In Proceedings of the
     Spatial pyramid pooling in deep convolutional networks for
                                                                          IEEE conference on computer vision and pattern recogni-
     visual recognition. IEEE transactions on pattern analysis
                                                                          tion, pages 2117–2125, 2017.
     and machine intelligence, 37(9):1904–1916, 2015.
                                                                     [29] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and
[17] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
                                                                          Piotr Dollár. Focal loss for dense object detection. In Pro-
     Deep residual learning for image recognition. In Proceed-
                                                                          ceedings of the IEEE international conference on computer
     ings of the IEEE conference on computer vision and pattern
                                                                          vision, pages 2980–2988, 2017.
     recognition, pages 770–778, 2016.
                                                                     [30] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
[18] Jennifer N. Hird, Alessandro Montaghi, Gregory J. McDer-
                                                                          Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
     mid, Jahan Kariyeva, Brian J. Moorman, Scott E. Nielsen,
                                                                          Zitnick. Microsoft coco: Common objects in context. In
     and Anne C. S. McIntosh. Use of unmanned aerial vehicles
                                                                          European conference on computer vision, pages 740–755.
     for monitoring recovery of forest vegetation on petroleum
                                                                          Springer, 2014.
     well sites. Remote. Sens., 9(5):413, 2017.
[19] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry                  [31] Songtao Liu, Di Huang, et al. Receptive field block net for
     Kalenichenko, Weijun Wang, Tobias Weyand, Marco An-                  accurate and fast object detection. In Proceedings of the Eu-
     dreetto, and Hartwig Adam. Mobilenets: Efficient convolu-            ropean Conference on Computer Vision (ECCV), pages 385–
     tional neural networks for mobile vision applications. arXiv         400, 2018.
     preprint arXiv:1704.04861, 2017.                                [32] Songtao Liu, Di Huang, and Yunhong Wang. Learning spa-
[20] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kil-              tial fusion for single-shot object detection. arXiv preprint
     ian Q Weinberger. Densely connected convolutional net-               arXiv:1911.09516, 2019.
     works. In Proceedings of the IEEE conference on computer        [33] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.
     vision and pattern recognition, pages 4700–4708, 2017.               Path aggregation network for instance segmentation. In Pro-
[21] Glenn Jocher, Alex Stoken, Jirka Borovec, NanoCode012,               ceedings of the IEEE conference on computer vision and pat-
     Ayush Chaurasia, TaoXie, Liu Changyu, Abhiram V, Laugh-              tern recognition, pages 8759–8768, 2018.
     ing, tkianai, yxNONG, Adam Hogan, lorenzomammana,               [34] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
     AlexWang1900, Jan Hajek, Laurentiu Diaconu, Marc,                    Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C
     Yonghye Kwon, oleg, wanghaoyang0106, Yann Defretin,                  Berg. Ssd: Single shot multibox detector. In European con-
     Aditya Lohia, ml5ah, Ben Milanko, Benjamin Fineran,                  ference on computer vision, pages 21–37. Springer, 2016.
[35] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei,                [50] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     Zheng Zhang, Stephen Lin, and Baining Guo. Swin trans-               reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
     former: Hierarchical vision transformer using shifted win-           Polosukhin. Attention is all you need. In Advances in neural
     dows. arXiv preprint arXiv:2103.14030, 2021.                         information processing systems, pages 5998–6008, 2017.
[36] Alexander Neubeck and Luc Van Gool. Efficient non-              [51] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-
     maximum suppression. In 18th International Conference on             Yuan Mark Liao. Scaled-yolov4: Scaling cross stage
     Pattern Recognition (ICPR’06), volume 3, pages 850–855.              partial network. In Proceedings of the IEEE/CVF Confer-
     IEEE, 2006.                                                          ence on Computer Vision and Pattern Recognition, pages
[37] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali               13029–13038, 2021.
     Farhadi. You only look once: Unified, real-time object de-      [52] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,
     tection. In Proceedings of the IEEE conference on computer           Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. Cspnet: A
     vision and pattern recognition, pages 779–788, 2016.                 new backbone that can enhance learning capability of cnn.
[38] Joseph Redmon and Ali Farhadi. Yolo9000: better, faster,             In Proceedings of the IEEE/CVF conference on computer
     stronger. In Proceedings of the IEEE conference on computer          vision and pattern recognition workshops, pages 390–391,
     vision and pattern recognition, pages 7263–7271, 2017.               2020.
[39] Joseph Redmon and Ali Farhadi. Yolov3: An incremental           [53] Derui Wang, Chaoran Li, Sheng Wen, Qing-Long Han,
     improvement. arXiv preprint arXiv:1804.02767, 2018.                  Surya Nepal, Xiangyu Zhang, and Yang Xiang. Daedalus:
[40] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.               Breaking nonmaximum suppression in object detection via
     Faster r-cnn: Towards real-time object detection with region         adversarial examples. IEEE Transactions on Cybernetics,
     proposal networks. Advances in neural information process-           2021.
     ing systems, 28:91–99, 2015.                                    [54] Sanghyun Woo, Jongchan Park, Joon-Young Lee, and In So
[41] Zhenfeng Shao, Congmin Li, Deren Li, Orhan Altan, Lei                Kweon. Cbam: Convolutional block attention module. In
     Zhang, and Lin Ding. An accurate matching method for pro-            Proceedings of the European conference on computer vision
     jecting vector data into surveillance video to monitor and           (ECCV), pages 3–19, 2018.
     protect cultivated land. ISPRS Int. J. Geo Inf., 9(7):448,      [55] Ze Yang, Shaohui Liu, Han Hu, Liwei Wang, and Stephen
     2020.                                                                Lin. Reppoints: Point set representation for object detection.
[42] Karen Simonyan and Andrew Zisserman. Very deep convo-                In Proceedings of the IEEE/CVF International Conference
     lutional networks for large-scale image recognition. arXiv           on Computer Vision, pages 9657–9666, 2019.
     preprint arXiv:1409.1556, 2014.                                 [56] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk
[43] Roman Solovyev, Weimin Wang, and Tatiana Gabruseva.                  Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regular-
     Weighted boxes fusion: Ensembling boxes from different               ization strategy to train strong classifiers with localizable fea-
     object detection models. Image and Vision Computing,                 tures. In Proceedings of the IEEE/CVF International Con-
     107:104117, 2021.                                                    ference on Computer Vision, pages 6023–6032, 2019.
[44] Mingxing Tan and Quoc Le. Efficientnet: Rethinking model        [57] Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and
     scaling for convolutional neural networks. In International          David Lopez-Paz. mixup: Beyond empirical risk minimiza-
     Conference on Machine Learning, pages 6105–6114. PMLR,               tion. arXiv preprint arXiv:1710.09412, 2017.
     2019.                                                           [58] Haoyang Zhang, Ying Wang, Feras Dayoub, and Niko Sun-
[45] Mingxing Tan, Ruoming Pang, and Quoc V Le. Efficientdet:             derhauf. Varifocalnet: An iou-aware dense object detector.
     Scalable and efficient object detection. In Proceedings of           In Proceedings of the IEEE/CVF Conference on Computer
     the IEEE/CVF conference on computer vision and pattern               Vision and Pattern Recognition, pages 8514–8523, 2021.
     recognition, pages 10781–10790, 2020.                           [59] Haoyang Zhang, Ying Wang, Feras Dayoub, and Niko Sun-
[46] Ziyang Tang, Xiang Liu, Guangyu Shen, and Baijian Yang.              derhauf. Varifocalnet: An iou-aware dense object detector.
     Penet: object detection using points estimation in aerial im-        In Proceedings of the IEEE/CVF Conference on Computer
     ages. arXiv preprint arXiv:2001.08247, 2020.                         Vision and Pattern Recognition, pages 8514–8523, 2021.
[47] Visdrone Team.               Visdrone 2020 leaderboard.         [60] Shifeng Zhang, Longyin Wen, Xiao Bian, Zhen Lei, and
     Website,      2020.            http://aiskyeye.com/                  Stan Z Li. Single-shot refinement neural network for ob-
     visdrone-2020-leaderboard/.                                          ject detection. In Proceedings of the IEEE conference on
[48] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. Fcos:                 computer vision and pattern recognition, pages 4203–4212,
     Fully convolutional one-stage object detection. In Proceed-          2018.
     ings of the IEEE/CVF international conference on computer       [61] Qijie Zhao, Tao Sheng, Yongtao Wang, Zhi Tang, Ying Chen,
     vision, pages 9627–9636, 2019.                                       Ling Cai, and Haibin Ling. M2det: A single-shot object de-
[49] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-              tector based on multi-level feature pyramid network. In Pro-
     reit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia          ceedings of the AAAI conference on artificial intelligence,
     Polosukhin. Attention is all you need. In Advances in Neu-           volume 33, pages 9259–9266, 2019.
     ral Information Processing Systems 30: Annual Conference        [62] Xingyi Zhou, Vladlen Koltun, and Philipp Krähenbühl.
     on Neural Information Processing Systems 2017, December              Probabilistic two-stage detection.               arXiv preprint
     4-9, 2017, Long Beach, CA, USA, pages 5998–6008, 2017.               arXiv:2103.07461, 2021.
[63] Xingyi Zhou, Dequan Wang, and Philipp Krähenbühl. Ob-
     jects as points. arXiv preprint arXiv:1904.07850, 2019.
[64] Pengfei Zhu, Longyin Wen, Xiao Bian, Haibin Ling, and
     Qinghua Hu. Vision meets drones: A challenge. arXiv
     preprint arXiv:1804.07437, 2018.
[65] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang
     Wang, and Jifeng Dai. Deformable detr: Deformable trans-
     formers for end-to-end object detection. arXiv preprint
     arXiv:2010.04159, 2020.
