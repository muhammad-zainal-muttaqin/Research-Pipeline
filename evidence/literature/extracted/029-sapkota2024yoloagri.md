---
source_id: 029
bibtex_key: sapkota2024yoloagri
title: YOLOv1 to YOLOv10: A Comprehensive Review of YOLO Variants and Their Application in the Agricultural Domain
year: 2024
domain_theme: Survei YOLO
verified_pdf: 29_Review YOLO Pertanian (Sapkota dkk.).pdf
char_count: 144820
---

YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO
                                             VARIANTS AND THEIR APPLICATION IN THE AGRICULTURAL
                                                                  DOMAIN

                                                                               Mujadded Al Rabbani Alif* and Muhammad Hussain
arXiv:2406.10139v1 [cs.CV] 14 Jun 2024

                                               Department of Computer Science, Huddersfield University, Queensgate, Huddersfield HD1 3DH, UK;
                                              *
                                               Correspondence: M.Alif@hud.ac.uk;

                                                                                                           June 17, 2024

                                                                                                          A BSTRACT
                                                  This survey investigates the transformative potential of various YOLO variants, from YOLOv1 to
                                                  the state-of-the-art YOLOv10, in the context of agricultural advancements. The primary objective
                                                  is to elucidate how these cutting-edge object detection models can re-energise and optimize diverse
                                                  aspects of agriculture, ranging from crop monitoring to livestock management. It aims to achieve
                                                  key objectives, including the identification of contemporary challenges in agriculture, a detailed
                                                  assessment of YOLO’s incremental advancements, and an exploration of its specific applications
                                                  in agriculture. This is one of the first surveys to include the latest YOLOv10, offering a fresh
                                                  perspective on its implications for precision farming and sustainable agricultural practices in the
                                                  era of Artificial Intelligence and automation. Further, the survey undertakes a critical analysis of
                                                  YOLO’s performance, synthesizes existing research, and projects future trends. By scrutinizing
                                                  the unique capabilities packed in YOLO variants and their real-world applications, this survey
                                                  provides valuable insights into the evolving relationship between YOLO variants and agriculture.
                                                  The findings contribute towards a nuanced understanding of the potential for precision farming and
                                                  sustainable agricultural practices, marking a significant step forward in the integration of advanced
                                                  object detection technologies within the agricultural sector.

                                         Keywords Precision Farming; Automation; Computer Vision; YOLO; Object Detection; Agricultural Applications ;
                                         Real-Time Image processing; Deep Learning in Agriculture; Convolutional Neural Networks(CNN); YOLO version
                                         comparison; Automated Crop monitoring

                                         1   Introduction
                                         In recent years, the intersection of computer vision and agriculture has experienced remarkable strides, unlocking a
                                         transformative era in precision farming and agricultural management [1]. Among the key technologies driving this
                                         paradigm shift is the evolution of the You Only Look Once (YOLO) algorithm, a family of object detectors that have
                                         manifested exceptional efficiency and accuracy. This review aims to delve into the mainstream YOLO variants, starting
                                         with YOLOv1 and continuing with the latest advancements in the form of YOLOv10. In particular, this exploration seeks
                                         to unravel the emerging potential of YOLO variants in revolutionising agricultural practices and fostering sustainable
                                         advancements. The YOLO family of object detectors, introduced by Joseph Redmon in 2015 with YOLOv1, marked
                                         a watershed moment in the object detection catalogue of architectures. YOLO’s distinctive characteristic lies in its
                                         ability to perform real-time object detection by dividing the input image into a grid matrix and predicting bounding
                                         boxes and class probabilities simultaneously [2]. This shift from conventional two-stage methodologies significantly
                                         enhanced speed and maintained competitive accuracy, setting the stage for subsequent YOLO iterations. As YOLO
                                         progressed through its reforms, each variant addressed limitations in addition to introducing novel techniques for
                                         refining edge-based performance. The transition from YOLOv1 to YOLOv10 witnessed advancements in several fields,
                                         including architectural design, training strategies, and optimisation techniques. The later variants of YOLO are designed
                                         to tackle challenges such as small object targets, occlusions, and improving performance across diverse datasets. It is
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

important to understand these complexities to fully appreciate the potential applicability of YOLO variants in complex
sub-domains such as agriculture.
Agriculture, being a multifaceted domain, demands robust and highly efficient tools for monitoring and management
of crops, livestock, and environmental conditions [3]. The integration of YOLO variants in agricultural applications
is promising for revolutionising tasks such as crop monitoring [4], disease detection [5], yield estimation [6], and
livestock management. The real-time capacity offered by YOLO, coupled with its accuracy and adaptability, make
YOLO variants an attractive solution for addressing the evolving challenges in modern agriculture. Given the rising
demands within the agricultural sector, computer vision stands out as a transformative force for several reasons:

       • Scale and Precision: Automation, enabled by computer vision, accelerates large-scale and precise operations.
         Computer vision algorithms can facilitate the rapid and accurate analysis of visual data, allowing for the
         monitoring of vast agricultural landscapes with unprecedented levels of speed and precision.
       • Efficiency and Resource Optimisation: The integration of computer vision can improve the efficiency
         of automated processes. Advanced image recognition and on-device analysis can enable the allocation of
         resources such as water, fertilizers, and land. This not only maximises yield but also promotes sustainable
         farming practices.
       • Real-time Response: Computer vision contributes to real-time monitoring and analysis. Automated systems,
         fuelled by computer vision, can swiftly detect and respond to emerging challenges, such as disease outbreaks
         or pest invasions, ensuring a rapid and targeted intervention to alleviate potential losses and maintain crop
         health.
       • Data-Driven Decision-Making: Computer vision augments automation by providing a wealth of real-time
         visual data. This data-driven approach can enable farmers and stakeholders to make informed decisions,
         improving overall farm management and strategic planning.

In the subsequent sections of this review, we will navigate through key advancements of each YOLO variant, elucidating
enhancements introduced in each variant. Subsequently, we will examine specific applications and the potential impact
of YOLO variants in agriculture, investigating how these variants can contribute to sustainable farming practices
and agricultural advancements. As we navigate through this review, it becomes clear that the fusion of cutting-edge
computer vision technologies, represented by YOLO variants, with the agricultural landscape holds the promise of
driving a new era of precision farming and resource optimization.

1.1   Survey Objective

This review endeavours to examine the transformative potential of YOLO variants, spanning from YOLOv1 to the
state-of-the-art YOLOv10, in the realm of agricultural advancements. The overarching aim is to elucidate how these
state-of-the-art architectures belonging to the YOLO family can reshape and optimise various facets of agriculture,
ranging from crop monitoring to livestock management. The primary focus will be on harnessing the unique capabilities
of YOLO variants to accommodate the dynamic challenges faced by the agricultural sector. Specifically, this review
aims to achieve the following objectives:
Assessment of YOLO Evolution: We trace the fundamental advancements of each YOLO variant, examining
the architectural enhancements, algorithmic refinements, and methodological innovations. By comprehensively
understanding the incremental evolution of YOLO variants, we can affirm the technological strides that contribute to
YOLO’s applicability in diverse agricultural scenarios.
Exploration of YOLO Applications in Agriculture: We then explore the specific applications of YOLO variants
in agricultural sub-domains. This involves the investigation of real-world use cases where YOLO has demonstrated
high efficacy, such as crop monitoring, livestock tracking, and detection of anomalies in the agricultural landscape. By
identifying these applications, we can gauge the versatility of YOLO in tackling the multifaceted challenges of modern
agriculture.
Critical Analysis of YOLO’s Performance: A critical review of the performance of YOLO variants in agricultural
contexts is presented. This includes assessing metrics such as detection accuracy, processing speed, and adaptability to
diverse agricultural environments. Through a nuanced analysis, we are able to ascertain the strengths and limitations of
YOLO in meeting the specific demands of agriculture.
Synthesis of Existing Research: The survey aims to synthesize and analyse existing research studies that have explored
the intersection of YOLO variants concerning the agricultural domain. By consolidating the findings of these works,
we unlock key insights and discern common trends, paving the way for a comprehensive understanding of the current
landscape.

                                                           2
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Projection of Future Trends: We anticipate future trends crucial for benchmarking the impact of YOLO variants in
agriculture. This objective involves extrapolating from current research and technological trajectories to envisaging
potential advancements, challenges, and emerging applications of YOLO in the agricultural domain.
In brief, this review aspires to present a holistic manifestation of the evolving relationship between YOLO variants and
agriculture, unravelling the layers of innovation that hold the promise of ushering in a new era of precision farming and
sustainable agricultural practices.

1.2    Organization of Paper

This review initiates by delineating agricultural challenges, followed by an introduction to Convolutional Neural
Networks (CNNs) to furnish readers with foundational insights into the principles underpinning the YOLO framework.
Subsequently, a general introduction to object detection techniques is presented to establish the necessary contextual
background for the subsequent discourse.
Furthermore, the review undertakes a comprehensive examination of the evolutionary trajectories of YOLO architectures,
systematically investigating the modifications and enhancements introduced by each variant.
Subsequent to this examination, the review scrutinizes the application of YOLO variants in sub-domains of agriculture,
encompassing crop diseases, pest infestations, resource optimisation, and precision farming. In the conclusive segments,
the findings are summarised in detail, culminating in a comprehensive assessment of YOLO variants as a transformative
solution for agricultural domains.

2     Convolutional Neural Networks (CNN)
Deep Learning (DL) has emerged as a multi-domain innovation amid the popularity of various Machine Learning
(ML) techniques like Decision Trees (DT), Support Vector Machines (SVM), KMeans, Multilayer Perceptron (MLP),
and Artificial Neural Networks (ANN). DL, a subset of ML and an Artificial Intelligence (AI) component, has
demonstrated remarkable success across diverse domains. Its applications include biological data handling [7], speech
recognition [8], character recognition [9], micro-blogs [10], text classification [11], unstructured text data mining
with fault classification [12], gene expression [13], bolt detection [14, 15], pallet damage detection [16], automatic
landslide detection [17], video processing, including caption generation [18], intrusion detection [19] and stock market
prediction [20]. However, these examples only scratch the surface of Deep Learning’s vast potential.
In the context of this review, computer vision involves training machines to comprehend and interpret visual content
at a sophisticated level. This field includes various subfields such as object detection [21], image restoration, scene
or object recognition, pose and motion estimation, object segmentation, and video tracking, among others [22].
Unlike conventional image processing, which requires manual feature extraction through the definition of feature
descriptors, deep learning architectures serve as automatic feature extractors. This makes deep learning a lucrative
alternative, enabling researchers to overcome conventional image processing constraints and focus more on improving
application-specific performance.
Deep learning models encompass various techniques, including Recurrent Neural Networks (RNNs) for sequential data
processing and their architectural variants, such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU)
for memory and context preservation [23]. Convolutional Neural Networks (CNNs) specialize in visual perception
tasks involving image data, as other DL algorithms like ANNs struggle with scaling inefficiencies when confronted
with high-dimensional input data, such as images.
The architectural footprint of Convolutional Neural Networks (CNNs) at an abstract level consists of a set of convolution,
pooling, and activation functions that transform inputs through a staged process to reach the appropriate output.
A fundamental component within convolutional blocks of a CNN is defining the number of kernels/filters and their
respective dimensions. These are crucial for feature extraction, providing low-level spatial information to subsequent
layers for developing semantic relationships [24].
                                                                            
                                                             d−1
                                                             X
                                             qil = f bi +         wi+j xi+j                                         (1)
                                                             j=0

                                                     d1−1
                                                                                           !
                                                     X d2−1
                                                          X
                                   l
                                  qij =f     bij +               w(i+k)(j+l) x(i+k)(j+l)                              (2)
                                                     k=0 l=0

                                                             3
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Similar to ANNs, the weights (w) and spatial input (x) are multiplied via the dot product. After introducing the bias
term (b), a non-linear activation function (f ) is applied.
Equations (1) and (2) express the convolution operation for the input, respectively. In these equations, qil represents
the output of the i-th neuron in layer l. For text input, the filter size is denoted as d, while for visual input, d1 and d2
represent the filter width and filter height.
The output post-convolving is subjected to pooling to extract prominent features through aggregation, i.e., downsampling
along the spatial dimensions.
Multifaceted aggregation, i.e., pooling frameworks, are available [25], such as average pooling, sum pooling, and
max pooling. For example, the mathematical composition of the latter, i.e., the max pooling function, is expressed by
equation 3.

                                                             (l−1)    (l−1)
                                                qil = max(q(i−j) , q(i+j) )                                              (3)

Rectified Linear Unit (ReLU) is the profoundly utilised activation function within the convolutional blocks, as it is, in
essence, a ’max-operation’, making it computationally lightweight for its mathematical chemistry, as expressed via (4)
in comparison to the sigmoid and TanH expressed via (5) and (6), respectively.

                                                    f (x) = max(0, x)                                                    (4)

                                                               1
                                                      x→                                                                 (5)
                                                            1 + e−x

                                                 tanh(x) = 2σ(2x) − 1                                                    (6)

The visual manifestation of an abstract CNN is presented in Figure 1. The key components of CNNs can be labelled as
a set of convolutional blocks consisting of filters that can be optimised, followed by a defined number of fully connected
layers leading to the output [26].

    Figure 1: The General structure of a CNN, highlighting convolutional layers, pooling, and fully connected layers.

3     Object Detection
The development of effective object detectors presents several challenges for researchers and practitioners. A primary
concern is handling variations in image resolutions and aspect ratios, which becomes more challenging when target
objects exhibit significant differences in spatial dimensions. Class imbalance, especially in scenarios where obtaining
an adequate number of images for certain classes is difficult, can negatively impact the performance of object detectors,
resulting in biased predictions [27].
Another significant challenge lies in the computational complexity of object detection architectures, demanding
substantial computational resources in terms of power, memory, and time [28, 29]. Figure 2 illustrates object detection
for single and multiple objects in an image, depicting detectors with deep internal networks that require significant
computational resources for processing complex image datasets and extracting crucial features.

                                                             4
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

            Figure 2: Single and multiple objects in an image: Classification, Localization, Segmentation.

Object detection methods can be categorized into Two-stage object detectors and single-stage detectors. The former
proposes candidate regions in the image, followed by classification and localization within those proposed regions.
Examples of two-stage detectors include RCNN (Region-based Convolutional Neural Network) [30], Fast R-CNN [31],
Faster R-CNN [32], and FPN (Feature Pyramid Network) [33].
RCNN [30], introduced in 2014, utilized a selective search for candidate region proposals. It then employed a CNN
network for feature extraction, followed by an SVM classifier for classification and localization. Although accurate,
RCNN was computationally inefficient due to its two-stage process. Fast R-CNN [31] addressed efficiency concerns by
introducing ROI pooling. This approach used ROI pooling to extract fixed-size feature maps for each region from the
original feature maps, resulting in significant computational speed-up. Faster R-CNN [32] improved upon Fast R-CNN
by introducing the Region Proposal Network (RPN), which directly generated region proposals from convolutional
feature maps, eliminating the need for a separate proposal stage. Integration of RPN into Fast R-CNN enhanced both
speed and accuracy. FPN (Feature Pyramid Network) [33] enhanced two-stage detectors by addressing the challenge
of detecting targets at multiple scales. FPN generated a feature pyramid by incorporating feature maps of varying
resolutions from different stages of the network, enabling the model to detect targets of different scales effectively.
While two-stage detectors exhibit impressive accuracy, their high computational demand limits their applications.
Single-stage detectors aim to detect objects in a single pass, eliminating the need for a separate region proposal step,
as shown in Figure 3. Notable single-stage detectors include SSD (Single Shot Multibox Detector), YOLO variants
(You Only Look Once), RefineDet++, DSSD (Deconvolution Single Shot Detector), and RetinaNet. SSD [34] utilizes
multiple convolutional feature maps at different scales for predicting bounding boxes and class probability scores.
It effectively detects objects of various sizes and shapes in a single forward pass. RefineDet++[35] enhances the
original RefineDet architecture by refining target proposals iteratively through multiple stages. Improved feature fusion
mechanisms and refined target boundaries contribute to enhanced accuracy. DSSD (Deconvolution Single Shot Detector)
incorporates deconvolution layers to retain spatial information lost during feature pooling. This aids in maintaining

                            Figure 3: Abstract architecture of single-stage object detectors.

                                                           5
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

spatial resolution, allowing DSSD to capture fine-grained details. RetinaNet [36] addresses class imbalance with Focal
Loss, assigning higher weights to hard, misclassified samples, improving the architecture’s ability to handle class
imbalance and enhance detection performance.
Single-stage detectors offer advantages such as faster inference speed and a lightweight footprint compared to two-stage
detectors, making them suitable for resource-constrained environments. YOLO has emerged as a strong competitor
among single-stage detectors, demonstrating impressive accuracy and real-time inference capabilities due to its
straightforward architecture. It has proven to be effective in various real-world applications, showcasing its potential for
production purposes.

4     YOLO Architecture Background
This section delves into the foundational principles and architecture underlying YOLO, detailing the unique advance-
ments associated with each iteration. The YOLO algorithm, introduced in 2015 by Joesph Redmon et al. [37], stands
for "You Only Look Once." This name reflects its distinctive approach, examining the entire image just once to identify
objects and their positions. In contrast to conventional methods employing two-stage detection processes, YOLO
treats object detection as a regression problem [37]. In the YOLO paradigm, a single convolutional neural network is
employed to predict bounding boxes and class probabilities for an entire image. This streamlined approach differs from
traditional methods with more intricate pipelines.

4.1    YOLOv1

The core concept of YOLOv1 entails superimposing a grid cell-sized "s x s" onto an image. Whenever an object’s centre
lands within a grid cell, that specific cell is tasked with identifying the object, enabling other cells to ignore its existence
in situations where multiple instances occur. Regarding object detection, every grid cell anticipates "B" bounding boxes,
complete with dimensions and confidence scores. The confidence score indicates the probability of an object residing
within the designated bounding box. Mathematically, the confidence score is represented as Equation (7):

                                        confidence score = p(object) × IoUtruth pred                                        (7)
In this context, p(object) denotes the likelihood of the object’s presence (with a range between 0 and 1), and IoUtruth pred
represents the intersection-over-union between the predicted bounding box and the ground truth.
The primary goal is accurately identifying and localising objects using bounding boxes. YOLO tackles challenges
related to overlapping predicted bounding boxes through a non-maximum suppression (NMS) mechanism, eliminating
those with an Intersection over Union (IoU) below a specified threshold. The original YOLO architecture, built on
Darknet, introduced two sub-variants: one with 24 convolutional layers and another called ’Fast YOLO’ with nine
layers. Different penalties were assigned for bounding boxes containing objects and those indicating the absence of
an object. The overall loss function incorporated coordinates, width, height, confidence score, and class probability
considerations.
In terms of performance, the simpler YOLO version achieved a mean average precision (mAP) of 63.4% at 45 frames
per second (FPS), while the Fast YOLO variant reached 52.7% at 155 FPS. Despite surpassing some real-time detectors,
they fell short of state-of-the-art (SOTA) benchmarks at that particular time. Nevertheless, limitations such as lower
recall and localization errors spurred further advancements in subsequent YOLO variants.

4.2    YOLOv2

Expanding on the achievements of YOLOv1, YOLOv2 brings forth notable enhancements in its design. This version
incorporates ideas from Network-In-Network and VGG, opting for the Darknet-19 framework, consisting of 19
convolutional layers and 5 layers specifically designated for maximum pooling, as detailed in Table 1. YOLOv2
employs a blend of pooling layers and 1 x 1 convolutions, enabling down-sampling within the network architecture.
An essential challenge in object detection lies in the limited availability of labelled data, often confining methods
to predetermined categories. YOLOv2 tackles this challenge by amalgamating the ImageNet and COCO datasets,
broadening its detection capabilities to encompass over 9418 object instances [38]. For enhanced scalability, YOLOv2
adopts Word-Tree, a hierarchical classification and detection approach adept at efficiently handling the expanded array
of categories.
Despite initial difficulties with small object detection, YOLOv2 marks substantial improvements over its predecessor. It
introduces diverse data augmentation techniques and optimization strategies, yielding noteworthy advancements:

                                                               6
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

                                          Table 1: Darknet-19 framework
                                    Type          Filters Size/Stride   Output
                                 Convolutional      32       3x3       224 x 224
                                   Maxpool       2 x 2/2 112 x 112
                                 Convolutional      64       3x3       112 x 112
                                   Maxpool       2 x 2/2    56 x 56
                                 Convolutional     128       3x3        56 x 56
                                 Convolutional      64       1x1        56 x 56
                                 Convolutional     128       3x3        56 x 56
                                   Maxpool       2 x 2/2    28 x 28
                                 Convolutional     256       3x3        28 x 28
                                 Convolutional     128       1x1        28 x 28
                                 Convolutional     256       3x3        28 x 28
                                   Maxpool       2 x 2/2    14 x 14
                                 Convolutional     512       3x3        14 x 14
                                 Convolutional     256       1x1        14 x 14
                                 Convolutional     512       3x3        14 x 14
                                 Convolutional     256       1x1        14 x 14
                                 Convolutional     512       3x3        14 x 14
                                   Maxpool       2 x 2/2     7x7
                                 Convolutional     1024      3x3         7x7
                                 Convolutional     512       1x1         7x7
                                 Convolutional     1024      3x3         7x7
                                 Convolutional     512       1x1         7x7
                                 Convolutional     1024      3x3         7x7
                                 Convolutional     1000      1x1         7x7
                                   Avgpool       Global      1000
                                   Softmax

      • YOLOv2 predicts object dimensions across a range of sizes, from 320 x 320 to 608 x 608, by discarding fully
        connected layers present in YOLOv1.
      • A 4% increase in mean average precision (mAP) is attained through a higher resolution classifier. In contrast
        to V1, YOLOv2 undergoes training on 448 x 448 images for classification before detection, enhancing the
        accuracy of bounding box predictions.
      • The integration of Batch Normalization addresses inconsistencies in input distribution during training, resulting
        in an approximate 2% mAP improvement.
      • Enhanced bounding box coordinate prediction is achieved by predicting location coordinates in relation to grid
        cell locations, leading to a 5% increase in mAP with more uniform bounding box aspect ratios and sizes.
      • YOLOv2 employs convolutional layers for feature extraction and predicts bounding boxes using anchor boxes,
        contributing to a 7% improvement in recall.
      • The adoption of a clustering algorithm based on K-means eliminates the need for manual selection of anchor
        boxes, thereby enhancing accuracy.
      • To tackle the challenge of smaller object detection, skip connections inspired by ResNet are incorporated,
        resulting in a 1% increase in mAP. For instance, a 26 x 26 x 512 feature map transforms into a 13 x 13 x 2048
        feature map, concatenating with the model’s output, enabling more robust object recognition across various
        dimensions.

4.3   YOLOv3

The introduction of YOLOv3 [39] in 2018 by Joesph Redmon et al. represented a significant evolution, featuring
an expanded architecture outlined in Table 2. This iteration embraced contemporary technological advancements
while maintaining real-time processing capabilities. Similar to YOLOv2, YOLOv3 predicts four coordinates for each
bounding box but introduces an objectness score for each box, determined through logistic regression. This score
assumes values of 1 or 0, indicating whether the anchor box has the highest overlap with the ground truth (1) or other
anchor boxes (0). Unlike Faster R-CNN [40], YOLOv3 associates a single anchor box with each ground truth object,

                                                           7
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

incurring only the classification loss in cases where no anchor box is associated, excluding localization and confidence
losses.

                                      Figure 4: Multi-scale Detection Architecture

                                            Table 2: YOLOv3 Architecture
                            Layer       Filters     Size      Repeat           Output Size
                            Image         —          —          —               416 × 416
                             Conv         32      3×3/1         1               416 × 416
                             Conv         64      3×3/2         1               208 × 208
                             Conv         32      1×1/1      Conv × 1           208 × 208
                             Conv         64      3×3/1      Conv × 1           208 × 208
                           Residual       —          —     Residual × 1         208 × 208
                             Conv         128     3×3/2         1               104 × 104
                             Conv         64      1×1/1      Conv × 2           104 × 104
                             Conv         128     3×3/1      Conv × 2           104 × 104
                           Residual       —          —     Residual × 2         104 × 104
                             Conv         256     3×3/2         1                52 × 52
                             Conv         128     1×1/1      Conv × 8            52 × 52
                             Conv         256     3×3/1      Conv × 8            52 × 52
                           Residual       —          —     Residual × 8          52 × 52
                             Conv         512     3×3/2         1                26 × 26
                             Conv         256     1×1/1      Conv × 8            26 × 26
                             Conv         512     3×3/1      Conv × 8            26 × 26
                           Residual       —          —     Residual × 8          26 × 26
                             Conv        1024     3×3/2         1                13 × 13
                             Conv         512     1×1/1      Conv × 4            13 × 13
                             Conv        1024     3×3/1      Conv × 4            13 × 13
                           Residual       —          —     Residual × 4          13 × 13

In contrast to utilizing SoftMax for classification, YOLOv3 employs binary cross-entropy, enabling the assignment of
multiple labels to a single box. The architecture integrates an extensive feature extractor with 53 convolutional layers
and incorporates residual connections.
Significant improvements involve a modified spatial pyramid pooling (SPP) block within the backbone to accommodate
a broader receptive field. YOLOv3 organizes feature maps into three scales: (416×416), (13×13), (26×26), and
(52×52) for input, each featuring three prior boxes for every position (as depicted in Figure 4). Collectively, these
enhancements resulted in a 2.7% improvement in the AP50 metric.

                                                           8
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

The determination of eight prior boxes, distributed across the three-scale feature maps, employs the K-means algorithm.
Larger-scale feature maps incorporate smaller precedent boxes. The foundational architecture of YOLOv3 referred to as
Darknet-53, replaces all max-pooling layers with stride convolutions and integrates residual connections. Comprising
53 convolutional layers (as detailed in Table 2), this backbone architecture emerged as the primary benchmark for object
detection shifted from PASCAL VOC [41] to Microsoft COCO [42]. Consequently, all subsequent YOLO models were
evaluated using the MS COCO dataset. YOLOv3 achieved notable results: an average precision (AP) of 36.2% and an
AP-50 of 60.6% at a processing speed of 20 frames per second (FPS), surpassing the pace of previous state-of-the-art
models.

4.4   YOLOv4

In April 2020, a team led by Alexey Bochkovskiy introduced YOLOv4 [43], representing a profound departure from its
predecessors with revolutionary architectural changes aimed at improving performance while maintaining real-time
capabilities. The key advancements in YOLOv4 include the integration of CSP Darknet53, SPP structure [44], PANet
architecture [45] (depicted in Figure 5), CBN integration [46], and SAM incorporation [47], resulting in an efficient and
robust object detection model. Designed to simplify the training of object detectors, YOLOv4 aims to be accessible to
individuals with varying technical expertise. The study also validated the effectiveness of state-of-the-art methodologies,
such as bag-of-freebies and bag-of-specials, to enhance the efficiency of the training pipeline.
Unlike YOLOv3, where a single anchor point detected a ground truth, YOLOv4 uses multiple anchor points for a single
ground truth detection. This approach improves the selection ratio of positive samples, reduces the imbalance between
positive and negative samples, and enhances boundary detection accuracy.

                         Figure 5: Path Aggregation YOLOv4 (a) Addition (b) Concatenation

YOLOv4 employs the Complete Intersection over Union (CIoU) loss, depicted in Equation (8), to refine localization
accuracy by incorporating factors like IoU, maximum IoU, and regularization. The utilization of this loss function
enhances YOLOv4’s capability to accurately locate and outline objects in images, thereby improving overall object
detection performance.

                                                                  (ρ2 − IoU(b, b̂)2 )
                                     LCIoU = 1 − IoU(b, b̂) +
                                                                         ρ2                                            (8)
                                                         v
                                         +α·
                                               (1 − IoU(b, b̂) + v)

                                                             9
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Here, LCIoU denotes the CIoU loss, b stands for the predicted bounding box, b̂ represents the ground truth bounding
box, IoU(b, b̂) computes the Intersection over Union (IoU) between the predicted and ground truth boxes, ρ2 serves as a
parameter for the maximum possible IoU, α acts as a balancing factor, and v is employed to address small bounding
boxes.

4.5   YOLOv5

In 2020, Glenn Jocher introduced YOLOv5, following the release of YOLOv4 [46]. YOLOv5, managed by Ultralytics,
takes a different path from YOLOv4 in several key aspects. Notably, YOLOv5 opts for PyTorch instead of Darknet for
development, expanding its user base due to PyTorch’s user-friendly characteristics. YOLOv5 incorporates various
enhancements to improve its performance in object detection. At its core, YOLOv5 features a CSP (Cross Stage Partial)
Net, derived from the ResNet architecture, which includes a cross-stage partial connection for enhanced network
efficiency. The CSPNet is complemented by multiple SPP (Spatial Pyramid Pooling) blocks for feature extraction at
different scales.
The architecture’s neck includes a PAN (Path Aggregation Network) module and subsequent upsampling layers to
improve feature map resolution [48]. The head of YOLOv5 utilizes convolutional layers to predict bounding boxes
and class labels. YOLOv5 employs anchor-based predictions, associating each bounding box with predetermined
anchor boxes of specific shapes and sizes. The loss function in YOLOv5 combines Binary Cross-Entropy and Complete
Intersection over Union (CIoU) for class, objectness, and localization losses, expressed as (9):

                                        loss = λ1 · Lcls + λ2 · Lobj + λ3 · Lloc                                    (9)

Where Lcls , Lobj , and Lloc denote the Binary Cross-Entropy loss for class predictions, Binary Cross-Entropy loss for
objectness predictions, and CIoU loss for localization, respectively. The λ values serve as weighting factors for each
loss component.
The primary objective of YOLOv5 is to enhance efficiency and accuracy, surpassing its predecessors. It brings
advancements in feature extraction, feature aggregation, and anchor-based predictions. Furthermore, it ensures a
seamless transition from PyTorch to ONNX and CoreML frameworks, enhancing compatibility with iOS devices. In
evaluations on the MS COCO dataset’s test-dev 2017 split, YOLOv5x achieved an average precision (AP) score of
50.7% with a 640-pixel image size, processing at a high speed of 200 frames per second (FPS) on an NVIDIA V100.
With a larger input size of 1536 pixels, YOLOv5 achieved an even higher AP score of 55.8%, as evident from Table 3.

                                     Table 3: Variant Comparison of YOLOv5
 Model                         Average Precision (@50)    Parameters                      FLOPs
 YOLO-v5s                      55.8%                      7.5M                            13.2B
 YOLO-v5m                      62.4%                      21.8M                           39.4B
 YOLO-v5l                      65.4%                      47.8M                           88.1B
 YOLO-v5x                      66.9%                      86.7M                           205.7B

4.6   YOLOv6

Released in September 2022 by the Meituan Vision AI Department, YOLOv6 is a single-stage object detection frame-
work designed specifically for industrial applications. This version brings significant improvements and architectural
refinements, notably introducing CSPDarknet as the new backbone architecture, surpassing its predecessors’ efficiency
and speed benchmarks, YOLO-v4 and YOLO-v5. One key enhancement in YOLO-v6 is the integration of a feature
pyramid network (FPN), expanding the range of feature scales and resulting in a noticeable improvement in detection
accuracy. This underscores the commitment to enhancing overall performance [49].
YOLO-v6 is meticulously crafted for optimal real-time object detection performance, demonstrating impressive frame
rates on both central processing units (CPUs) and graphics processing units (GPUs).A pivotal evolution in the YOLOv6
architecture involves the separation of the classification and box regression heads, as illustrated in Figure 6. This
strategic architectural revision introduces additional layers within the network, effectively segregating these crucial
functions from the final head [50]. Empirical evidence supports the impact of this refinement in elevating the overall
model’s performance, reinforcing its capabilities [51].
In aggregate, YOLOv6 marks a substantial advancement in the progression of YOLO architectures, incorporating a wide
range of enhancements that span speed, accuracy, and operational efficiency. A thorough assessment of the MS COCO

                                                          10
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

                                           Figure 6: PANet Configuration [2]

dataset’s test-dev 2017 subset highlighted the capabilities of the YOLOv6L model, delivering an average precision (AP)
of 52.5% and an AP50 of 70%. Notably, this commendable performance was attained while sustaining a processing
speed of around 50 frames per second (FPS) on an NVIDIA Tesla T4 GPU. YOLOv6 is presented in three distinct
variants, as outlined in Table 4. Notably, YOLOv6nano stands out as the smallest and fastest alternative, characterized
by a minimal parameter count. This feature makes it particularly well-suited for real-time object detection tasks on
devices with limited computational capabilities. Advancing to YOLO-v6tiny, this variant offers a more expansive
architecture compared to YOLOv6nano, resulting in increased accuracy, as evidenced in Table 4. YOLOv6tiny proves
valuable when precision is crucial, especially in scenarios involving the detection of smaller objects.

                                        Table 4: YOLOv6 Variant Comparison
 v6 Variant               Size                   mAP                Parameters                     FLOPs
 Nano                     416-640                30.8-35.0%         4.3M                           4.7-11.1G
 Tiny                     640                    41.3%              15M                            36.7G
 Small                    640                    43.1%              17.2M                          44.2G

Conversely, YOLOv6small leads in architectural complexity, delivering a higher level of accuracy. This configuration is
particularly suitable for scenarios where detecting smaller objects within the visual field is paramount. The selection
among these variants depends on the specific use case and available computational resources. YOLOv6nano is an
optimal choice for scenarios requiring real-time detection on low-powered devices, while preferences for YOLOv6tiny
or YOLOv6small may arise in instances where greater accuracy and the identification of smaller objects are essential.
The decision should be tailored to the available resources and the desired accuracy threshold.

4.7   YOLOv7

Introduced in July 2022, YOLOv7 [52] marked a significant leap forward from its predecessors, showcasing improved
accuracy and speed enhancements ranging from 5 FPS to 160 FPS. These advancements primarily centred on boosting
efficiency and scalability by integrating the Extended Efficient Layer Aggregation Network (E-ELAN) [53] and
implementing a scalable concatenation-based architecture. E-ELAN plays a pivotal role in managing the gradient path,
thereby augmenting model learning and convergence. This technique is versatile and applicable to models with stacked
computational blocks, adeptly shuffling and merging features from different groups while preserving the integrity of
the gradient path. Model scaling is another critical aspect of YOLOv7, enabling the creation of models of varying
sizes. The devised scaling strategy adjusts the depth and width of the blocks uniformly, maintaining the optimal model
structure while mitigating hardware resource consumption. The amalgamation of various techniques, collectively
termed "bag-of-freebies," further amplifies YOLOv7’s performance. One such technique mirrors the re-parameterized
convolution concept employed in YOLOv6. However, the RepConvN approach was introduced in YOLOv7 due to
identified issues with the identity connection in RepConv [54] and concatenation in DenseNet [55].
Additionally, YOLOv7 utilizes coarse label assignment for the auxiliary head, reserving fine label assignment for the
lead head. While the auxiliary head contributes to the training process, the lead head produces the final output, as shown

                                                           11
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

in Figure 6. Moreover, batch normalization is employed, amalgamating the mean and variance of batch normalization
into the convolutional layer’s bias and weight during inference, ultimately enhancing model performance [56]. Under
rigorous evaluation on the MS COCO dataset’s test-dev 2017, YOLOv7E6 demonstrated outstanding performance,
achieving an average precision (AP) of 55.9% and an AP for the IoU threshold of 0.5 (AP50) of 73.5%, as showcased
in Table 5.

                                       Table 5: YOLOv7 Variant Comparison
 v7 Variant              Size                   mAP                Parameters                  FLOPs
 YOLO-v7 tiny            640                    52.8%              6.2M                        5.8G
 YOLO-v7                 640                    69.7%              36.9M                       104.7G
 YOLO-v7X                640                    71.1%              71.3M                       189.9G
 YOLO-v7E6               1280                   73.5%              97.2M                       515.2G
 YOLO-v7D6               1280                   73.8%              154.7M                      806.8G

4.8   YOLOv8

In January 2023, Ultralytics introduced YOLOv8, making a significant entrance into the field of computer vision [57].
The model’s precision was extensively assessed through evaluations on both COCO and Roboflow 100 datasets [57].
YOLOv8 distinguishes itself with user-oriented features, including a user-friendly command-line interface and a well-
organized Python package. The supportive YOLO community further enhances the model’s accessibility for users. The
innovation in YOLOv8, as detailed in its methodology [58], diverges from traditional anchor-based methods. Instead of
relying on predetermined anchor boxes, YOLOv8 adopts an anchor-free approach by predicting the object’s centre.
This adjustment addresses challenges associated with anchor boxes that may not accurately represent custom dataset
distributions. This approach’s advantages include reducing the number of box predictions and expedited post-processing
steps involving Non-Maximum Suppression. Notably, YOLO-v8’s training routine, which incorporates techniques
like online image augmentation, including mosaic augmentation, enhances the model’s ability to detect objects across
diverse conditions and novel spatial arrangements.
In its architectural evolution from its predecessor, YOLOv5 (also authored by the same individuals), YOLOv8 introduces
changes across its components. For instance, in the neck segment, YOLOv8 directly concatenates features without
enforcing uniform channel dimensions. This strategy contributes to a reduction in parameter count and overall tensor
size. When assessed on the MS COCO dataset’s test-dev 2017 subset, YOLOv8x demonstrated an average precision
(AP) of 53.9% at an image size of 640 pixels, surpassing YOLOv5’s AP of 50.7% with the same input size. Furthermore,
YOLOv8x exhibited remarkable processing speed, achieving 280 frames per second (FPS) using an NVIDIA A100 with
TensorRT. Notably, YOLOv8 is available in five distinct variants, each tailored to specific accuracy and computational
requirements, as detailed in Table 6.

                                      Table 6: YOLO-v8 Variant Comparison
 Model                   Size                  mAP                 Parameters                  FLOPs
 YOLO-v8n                640                   37.3%               3.2M                        8.7G
 YOLO-v8s                640                   44.9%               11.2M                       28.6G
 YOLO-v8m                640                   50.2%               25.9M                       78.9G
 YOLO-v8l                640                   52.9%               43.7M                       165.2G
 YOLO-v8x                640                   53.9%               68.2M                       257.8G

4.9   YOLOv9

YOLOv9, released in February 2024 [59] represents the latest addition to the mainstream YOLO variants. YOLOv9
boasts two key innovations: the Programmable Gradient Information (PGI) framework and the Generalized Efficient
Layer Aggregation Network (GELAN). The PGI framework aims to address the issue of information bottlenecks,
inherent in deep neural networks in addition to enabling deep supervision mechanisms to be compatible with lightweight
architectures. By implementing PGI, both lightweight and deep architectures can leverage substantial improvements in
accuracy, as PGI mandates reliable gradient information during training, thus enhancing the architecture’s capacity to
learn and make accurate predictions.
The GELAN architecture was purposefully designed to boost performance in object detection tasks via high efficiency
and lightweight footprint. GELAN manifests high performance across varying computational blocks and depth

                                                         12
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

configurations, making it suitable for deployment on different inference devices, including resource-constrained edge
devices. By combining the above two frameworks (PGI and GELAN), YOLOv9 presents a significant advancement in
lightweight object detection. Although in its early days, YOLOv9 has achieved remarkable competitiveness in object
detection tasks, outperforming YOLOv8 concerning parameter reduction and computational efficiency while improving
Average Precision (AP) by 0.6% on the MS COCO dataset.

4.10       YOLOv10

Building upon the momentum of innovation in the YOLO series, another groundbreaking development emerged in the
same year with the release of YOLOv10, also in 2024. This version pushes the boundaries further by addressing the
challenges associated with real-time object detection, which is critical for applications requiring rapid and accurate
responses, such as agricultural monitoring and autonomous vehicle navigation.
YOLOv10 distinguishes itself by completely eliminating the reliance on non-maximum suppression (NMS) during
post-processing, which is a significant step forward in enhancing inference speed. This model adopts a novel NMS-
free training approach using dual label assignments, allowing for a harmonious integration of accuracy and speed by
ensuring that the model remains computationally efficient while still capturing essential detection features. Moreover, the
architectural enhancements in YOLOv10 include the implementation of lightweight classification heads, spatial-channel
decoupled downsampling, and rank-guided block design, each contributing to substantial reductions in computational
demands and parameter count. These innovations not only improve the model’s efficiency but also its scalability across
various devices, from high-power servers to resource-limited edge devices.
Extensive testing demonstrates that YOLOv10 sets a new benchmark for the performance-efficiency trade-off. It
achieves remarkable improvements in latency and model size reduction compared to YOLOv9, while still delivering
competitive or superior detection accuracy. This is particularly evident in its application to the COCO dataset, where
YOLOv10 shows notable advancements in detection metrics, solidifying its position as a leader in the field of real-time
object detection technologies [60].
Table 7 provides a comparative overview of the major YOLO variants up to the current date. The table illustrates the
iterative evolution of the YOLO series of object detectors, with each iteration advancing the state-of-the-art in computer
vision.

                                          Table 7: YOLO Variant Comparison
    Version   Date   Contributions                                                                          Framework
      v1      2015   One-shot object detector                                                                 Darknet
      v2      2016   Multi-scale training, dimensional clustering                                             Darknet
      v3      2018   SPP block, Darknet-53                                                                    Darknet
      v4      2020   Mish-based activation, CSPDarknet-53 backbone                                            Darknet
      v5      2020   Anchor-free detection, SWISH-based activation, PANet                                     PyTorch
      v6      2022   Self-attention, anchor-free object detection                                             PyTorch
      v7      2022   Transformers, E-ELAN reparameterization                                                  PyTorch
      v8      2023   GANs, anchor-free detections                                                             PyTorch
      v9      2024   Programmable Gradient Information (PGI), Generalized Efficient Layer Aggre-              PyTorch
                     gation Network (GELAN)
     v10      2024   NMS-free training approach, dual label assignments, holistic model design for            PyTorch
                     enhanced accuracy and efficiency

5      Agricultural Applications of YOLO

In this section, we provide a comprehensive review of the current body of literature regarding the utilization of different
YOLO variants for various agricultural applications. The discussion is tailored to include applications such as weed
detection, crop classification, disease detection, animal tracking, and precision farming.

                                                            13
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

5.1   Weed Detection Using YOLO

Weed detection is a crucial aspect of modern agriculture as it directly impacts crop yield and resource optimization.
Traditional methods of weed management can be labour-intensive and time-consuming. The integration of YOLO
variants in weed detection brings forth a promising solution by offering real-time and efficient identification of weeds in
agricultural landscapes.
This subsection explores the application of YOLO in weed detection, focusing on its potential to revolutionize weed
management practices. We delve into the challenges associated with weed detection in traditional agriculture and
examine how YOLO variants address these challenges. Additionally, we explore real-world scenarios where YOLO
has demonstrated efficacy in accurately identifying and localizing weeds, contributing to advancements in precision
farming.
[61] developed and implemented a real-time weed detection system targeting green onion crops. Leveraging the
YOLOv3 deep learning algorithm, the system, coined YOLO-WEED, demonstrated notable efficiency and precision in
identifying weeds within video frames captured by Unmanned Aerial Vehicles (UAVs) [61]. This positions YOLO-
WEED as a valuable asset for precise agricultural activities such as targeted spraying and weed management. The
system’s performance evaluation, based on mean average precision and F1 score metrics, yielded impressive results with
a mean average precision of 93.81% and an F1 score of 0.94. The notable swiftness and accuracy of the YOLO-WEED
system make it a promising candidate for seamless integration into real-time automated aerial spray systems specifically
designed for green onion fields [61]. However, it is important to acknowledge certain limitations. The system’s
effectiveness is contingent upon the resolution of UAV video frames. Notably, the YOLOv3 algorithm employed in the
system encounters challenges in detecting smaller objects, presenting difficulties in identifying diminutive weeds within
the green onion fields [61]. Moreover, the YOLO-WEED system necessitates the presence of an onboard computer,
introducing an additional weight factor to the UAV sprayer system. Despite these considerations, the system’s overall
performance underscores its potential as an impactful solution for advancing precision farming practices, particularly in
the context of weed detection and control in green onion cultivation.
Boyu Ying et al. conducted a meticulous study on detecting weeds in images of carrot fields using an improved YOLOv4
model [62]. The researchers collected test images from the carrot fields in Central China’s Henan Province and aimed to
detect four common field weeds: crabgrass, plantain, pale persicaria, and cephalanoplos. They developed a lightweight
weed detection model called YOLOv4-weeds, which replaced the backbone network of YOLOv4 with MobileNetV3-
Small. This modification reduced the memory requirement of image processing and improved the efficiency and
accuracy of small weed detection in complex environments. The authors conducted comparative experiments with
other detection models and demonstrated that the YOLOv4-weeds model outperformed these models, especially in
detecting diverse weeds in complex field scenes. The research outcomes provide valuable insights and a reference
for weed detection, robot weeding, and selective spraying in agricultural settings. However, the study has potential
limitations, such as the diversity of weed species, generalization to other crops, robustness to environmental variability,
real-world deployment and validation, and consideration of computational resources. These findings significantly affect
the agricultural sector, as weed management is critical to crop yield and quality. The study provides a framework
for improving weed detection in complex agricultural environments, which can lead to efficient and cost-effective
weed management practices. However, further research is required to address the study’s limitations and enhance the
generalizability of the findings to other crops and environmental settings.
Dyrmann et al. conducted a study focusing on the identification and tracking of invasive alien plant species (IAPS)
along state roads, utilizing a camera-based monitoring system [63], as shown in Figure 7. The employed deep learning
algorithms successfully detected and classified IAPS in the collected images, demonstrating promising results for
real-time mapping of invasive alien plant species at driving speeds of 110 km/h. Despite notable achievements, the study
acknowledges certain limitations, such as challenges in detecting specific plant species like Lupinus polyphyllus and
Pastinaca sativa, and emphasizes the need for addressing these issues in future research. The study provides valuable
insights for cost-effective and efficient environmental conservation along roadsides.
Chen et al. concentrated on developing a YOLO-sesame model for weed detection in sesame fields [64]. The model,
incorporating an improved attention mechanism and feature fusion, exhibited high performance in terms of Frames Per
Second (FPS) and mean Average Precision (mAP). While showcasing promising results, the study highlights regional
specificity in the dataset and emphasizes the necessity for further work to enhance the model’s applicability to embedded
devices. This work contributes to the advancement of weed detection methodologies in sesame cultivation.
Wang et al. conducted field trials in Zhangjiakou City, Hebei Province, to test their method for real-world application
[65]. The study’s technique for image preprocessing and the deployment of an improved YOLOv5 CNN showed
satisfactory performance in practical scenarios. Despite notable achievements, the study recognizes limitations related
to environmental conditions and underscores the importance of addressing these challenges for broader applicability.

                                                           14
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

                               Figure 7: Plant Species Detection On Device Deployment

The study contributes to the progress of weed detection methodologies with potential implications for the early-stage
identification of invasive weeds.
Costello et al. investigated the use of RGB and HSI data for the field mapping of Parthenium weed in a controlled
environment [66]. Employing deep-learning algorithms, including decision-tree-based protocols, the study achieved
high accuracy in detecting and categorizing Parthenium weed growth stages. However, the study acknowledges
limitations such as the controlled environment and emphasizes the need for further exploration of AI algorithms and
technology improvements for enhanced detection success. This research offers valuable insights into the application
of AI and imaging techniques for Parthenium weed detection, with potential implications for weed management and
agriculture.
Dang et al. introduced the YOLOWeeds benchmark dataset for detecting various weed types in cotton production
systems [67]. Evaluating six different YOLO object detection models, the study provides a detailed experimental setup,
emphasizing challenges in weed management within cotton production. The results showcase the potential of YOLOv4
and YOLOv5 for real-time weed detection, prompting further exploration in machine vision-based weeding systems.
This work contributes to the advancement of automated weed identification with potential applications in sustainable
weed management in agriculture.
Pérez-Porras et al. conducted a study on detecting poppy (Papaver rhoeas) in wheat fields using YOLO architectures
[68]. Evaluating different YOLO models, the study optimized hyperparameters and assessed computational efficiency.
Despite achieving an accuracy of approximately 75%, the study acknowledges the need for field validation and
integration with agricultural practices. This research provides valuable insights into early weed detection in agricultural
fields, specifically in the case of poppy detection in wheat fields.
Sportelli et al. evaluated the performance of YOLO object detectors for weed detection in various turfgrass scenarios
[69]. Utilizing three datasets with specific characteristics, the study underscores the challenges associated with
accurate weed detection in turfgrass. While achieving high performance, the study acknowledges limitations in model
performance and emphasizes the need for further research to address these challenges. This work contributes to a
comprehensive understanding of the trade-offs between model performance and computational efficiency in weed
detection.

                                                           15
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Jin et al. proposed a novel method using YOLO-v3 to identify weeds in vegetable fields [70]. Adopting a two-stage
approach based on Convolutional Neural Networks (CNN), the method accurately detects weeds by focusing on the
detection of vegetable crops. Despite promising results, the study highlights the primary limitation in the lack of robust
sensing technology for the commercial development of intelligent robotic weeders. This research provides a feasible
approach for weed detection in various crops and emphasizes the need for advancements in sensing technology for
broader applications. Table 8 presents a compilation of studies employing diverse YOLO architectures for the detection
of weeds in the agricultural sector.

5.2   Crop Detection via YOLO

In the domain of precision agriculture, crop detection plays a pivotal role in optimizing farming practices and resource
utilization. Accurate identification and delineation of crops in large-scale fields contribute to improved monitoring,
yield estimation, and resource management. Various studies have explored the application of YOLO variants to address
the challenges associated with crop detection, showcasing the potential for real-time, efficient, and precise identification
of different crop types.

                                   Table 8: Studies on Weed Detection Using YOLO
 Authors           Model                                         Details
 [61]              YOLOv3                                        Real-time weed detection with UAVs in green
                                                                 onion fields. Mean average precision of
                                                                 93.81%, F1 score of 0.94.
 [62]              YOLOv4                                        Detection of weeds in carrot fields. Efficient de-
                                                                 tection of diverse weeds, outperforming other
                                                                 models in complex field scenes.
 [63]              YOLO                                          Identification and tracking of invasive alien
                                                                 plant species (IAPS) along Danish state roads.
                                                                 Successful results at driving speeds of 110
                                                                 km/h.
 [64]              YOLO-custom                                   Weed detection in sesame fields with improved
                                                                 attention mechanism and feature fusion. High
                                                                 FPS and mAP.
 [65]              YOLOv5                                        Field trials in Zhangjiakou City, Hebei
                                                                 Province, for weed detection. Satisfactory per-
                                                                 formance in practical scenarios.
 [66]              YOLOv4                                        Field mapping of Parthenium weed in a con-
                                                                 trolled environment. High accuracy in detect-
                                                                 ing and categorizing Parthenium weed growth
                                                                 stages.
 [67]              YOLOv4 & YOLOv5                               Introduction of YOLOWeeds benchmark
                                                                 dataset for detecting various weed types in cot-
                                                                 ton production systems. Evaluation of six dif-
                                                                 ferent YOLO object detection models.
 [68]              YOLO                                          Detection of poppy (Papaver rhoeas) in wheat
                                                                 fields. Approximate 75% accuracy.
 [69]              YOLO                                          Evaluation for weed detection in various turf-
                                                                 grass scenarios. Emphasis on challenges associ-
                                                                 ated with accurate weed detection in turfgrass.
 [70]              YOLO-v3                                       Novel method for weed detection in vegetable
                                                                 fields using a two-stage approach based on Con-
                                                                 volutional Neural Networks (CNN).

                                                            16
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

This subsection provides an overview of notable research endeavours that employ YOLO models for crop detection. The
studies discussed herein present advancements, methodologies, and outcomes related to the utilization of YOLO-based
approaches in identifying and delineating crops in diverse agricultural settings. The significance of robust crop detection
methodologies in the context of precision farming is emphasized, highlighting how YOLO variants contribute to
addressing the evolving needs of modern agriculture.
Tian et al. introduced an enhanced YOLO-V3 model designed for real-time apple detection in orchards [71]. Employing
a camera with a 3000 x 4000-pixel resolution under varying weather and illumination conditions, the researchers
gathered image data. Data augmentation techniques were applied to augment the dataset, enhancing its diversity.
To optimize feature layers with low resolution in the YOLO-V3 network, the authors incorporated the DenseNet
method, aiming to boost feature propagation, encourage reuse, and enhance overall network performance. The proposed
YOLOV3-dense model exhibited superior performance compared to the original YOLO-V3 and the Faster R-CNN
with VGG16 net model, particularly in terms of detection accuracy and real-time capabilities. Noteworthy, the study
concentrated exclusively on apple detection, neglecting exploration into other fruits or crops. Future investigations could
explore the adaptability of the proposed model to diverse agricultural contexts. Furthermore, the study overlooked the
potential impact of adverse weather conditions, such as rain or fog, on the model’s performance. Subsequent research
endeavours could delve into assessing the robustness of the model under various weather scenarios. Lastly, the study’s
evaluation on a large-scale dataset was lacking. Consequently, forthcoming studies may consider validating the model
on a more extensive dataset to further establish and validate its performance.
Sharpe and the research team developed a precision applicator for effective goosegrass control in Florida’s vegetable
plasticulture production [72]. The study assessed the utilization of the YOLOv3-tiny detector for on-site goosegrass
detection and spraying. Image processing involved various plants, including strawberry and tomato plants, as well as
other weed species, to train and test the neural network. While showcasing the potential of convolutional neural networks
in horticultural crop weed detection and management, the study identifies specific limitations and areas for improvement.
Primarily, the focus on goosegrass detection in strawberry and tomato production warrants further research to extend
the applicability of the network to diverse crops and weed species. The study highlights the superiority of the LB
annotation method for production and precision spraying but suggests that additional classes or grouping may enhance
overall network accuracy. Lastly, for tomatoes, the study acknowledges limitations in the piecewise image methodology,
urging further research to enhance detection accuracy for this particular crop.
Junos et al. introduced YOLO-P, an object detection model capable of identifying and locating objects (FFB, grabber,
and palm tree) in oil palm plantations [73]. Through multiple experiments, the proposed model demonstrated outstanding
mean average precision and F1 scores of 98.68% and 0.97, respectively. Characterized by a faster training process
and lightweight design (76 MB), the model exhibited accuracy in identifying fresh fruit bunches at various maturities,
offering potential applications in automated crop harvesting systems. The comprehensive experimental results suggest
that YOLO-P can accurately and robustly detect objects in palm oil plantations, thereby contributing to increased
productivity and optimized operational costs in the agricultural industry.
Chen et al. made significant strides in citrus fruit detection with the development of the CitrusYOLO algorithm [74].
Enhancements to the YOLOv4 model included the addition of a 152*152 feature detection layer, dense connections
for multiscale fusion, and integration of depthwise separable convolution and attention mechanism modules. These
improvements resulted in increased detection accuracy and real-time performance. CitrusYOLO exhibited superior
performance, outperforming standard deep learning algorithms in terms of accuracy and time efficiency. Despite
these advancements, the study recognizes certain limitations and areas for improvement. The dataset’s focus on two
varieties of Kumquats and Nanfeng tangerines and four varieties of Fertile orange, Tangerine, Mashui orange, and
Gonggan suggests the potential for improved performance with expanded citrus varieties and growth stages. The
algorithm’s performance under varied lighting conditions and its applicability to other fruits or objects in different
environments remain unknown. While experiments demonstrated effectiveness, real-world applications such as orchard
yield estimation and fruit harvesting robots require further validation.
Hong et al. developed a lightweight model for detecting wheat ear Fusarium head blight (FHB) using RGB images
[75]. Leveraging YOLOv4 and MobileNet architectures, the proposed model struck a balance between accuracy and
real-time FHB detection. With an accuracy of 93.69% in detecting wheat ear FHB, outperforming the MobileNetv2-
YOLOv4 model, the suggested model’s reduced size facilitates deployment on uncrewed aerial vehicles (UAVs). While
demonstrating great potential for real-time FHB detection, the study acknowledges certain limitations and areas for
improvement. The study’s exclusive focus on wheat ear Fusarium head blight detection, overlooking other diseases
affecting wheat crops, suggests future research considerations for expanding the model’s disease detection capabilities.
Challenges related to incorrect detections of small objects and detection performance in complex backgrounds highlight
the need for refining the model’s performance. Additionally, the study’s emphasis on reducing parameters necessitates
exploration of the model’s generalization across different edge platforms.

                                                            17
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Wang et al. proposed a real-time method for vehicle identification and tracking using Improved YOLOv4 and binocular
positioning (BPO) [76]. Addressing the tracking problem in agricultural master-slave follow-up operations, the study’s
experiments showcased the method’s accuracy in identifying and tracking the master vehicle in real time. Low RMS
errors in terms of longitudinal, lateral, and heading angle deviation signify the method’s effectiveness in meeting the
positioning requirements of the master vehicle. The study also created a dataset for training and testing the identification
model, hinting at future work on constructing and testing enslaved person automatic follow-up systems. While the study
does not explicitly mention limitations, potential areas for further exploration include the validation of the method in
diverse agricultural environments and consideration of its performance under varying weather and lighting conditions.
Table 9 compiles a summary of research endeavours utilizing diverse YOLO architectures for crop detection within the
agricultural domain.

                                   Table 9: Studies on Crop Detection Using YOLO
 Author               Model                                 Details
 [71]                 YOLOv3-dense                          Enhanced YOLO-V3 model for real-time apple
                                                            detection in orchards. Superior performance in
                                                            detection accuracy and real-time capabilities.
 [72]                 YOLOv3-tiny                           Utilization of YOLOv3-tiny detector for on-site
                                                            goosegrass detection and spraying in vegetable
                                                            plasticulture production. Potential for convolu-
                                                            tional neural networks in horticultural crop weed
                                                            detection and management.
 [73]                 YOLO-P                                Introduction of YOLO-P for identifying and locat-
                                                            ing objects (FFB, grabber, and palm tree) in oil
                                                            palm plantations. Outstanding mean average preci-
                                                            sion (98.68%) and F1 score (0.97).
 [74]                 Citrus-YOLO                           Development of CitrusYOLO algorithm for citrus
                                                            fruit detection. Improved YOLOv4 model with
                                                            increased detection accuracy and real-time perfor-
                                                            mance.
 [75]                 YOLOv4                                Lightweight model for detecting wheat ear Fusar-
                                                            ium head blight (FHB) using RGB images.
                                                            YOLOv4 and MobileNet architectures for a bal-
                                                            ance between accuracy and real-time FHB detec-
                                                            tion.
 [76]                 YOLOv                                 Real-time method for vehicle identification and
                                                            tracking using Improved YOLO (IYO) v4 and
                                                            binocular positioning (BPO). Accuracy in iden-
                                                            tifying and tracking master vehicles in agricultural
                                                            master-slave follow-up operations.

5.3   Animal Tracking with YOLO

In recent years, the application of You Only Look Once (YOLO) object detection models has revolutionized animal
tracking in ecological research. YOLO’s real-time and high-precision capabilities make it a compelling tool for
monitoring wildlife, enabling the automatic identification and tracking of animals in diverse environments. This
subsection delves into the innovative use of YOLO-based systems for animal tracking, exploring their contributions to
understanding animal behaviour, migration patterns, and ecological dynamics.
Wang et al. conducted a study to monitor and analyze the behaviours of egg breeders in self-breeding cages using visual
image processing and the YOLO v3 deep learning algorithm [77]. Their approach identified six behaviours, achieving
high precision rates and offering insights into the welfare state of egg breeders. Despite the success, the study’s
limitation involves the analysis of a limited sample size of Hy-Line Gray egg breeders in a single cage, warranting
further investigation across diverse breeds, larger populations, and comparisons with existing methods for behaviour
recognition [77].

                                                            18
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Schütz et al. applied YOLOv4 for red fox detection and motion monitoring, showcasing the potential of computer
vision systems in studying animal behaviour [78]. While the study emphasized the efficiency and accuracy of computer
evaluation, limitations included occasional camera manipulation by foxes and challenges in detecting rarely occurring
fox positions not present in the training set. Proposed solutions involve securing the camera appropriately and expanding
the training set to address bias and improve accuracy [78].
Yu et al. utilized the YOLO-improved model and edge computing to detect dairy cow feeding behaviour automatically
[79]. The proposed DRN-YOLO algorithm exhibited improved precision, recall, mean Average Precision (mAP), and
F1-score, with potential areas for improvement outlined, such as further subdividing cow foraging behaviour and testing
generalizability across diverse farm environments and cow populations [79].
Elmessery et al. conducted a comprehensive study to develop and validate a YOLOv8-based model for automatically
detecting broiler pathological phenomena in intensive poultry houses [80]. Despite successful training and detection,
limitations included a constrained dataset of diseased broilers due to disease-related constraints and potential impacts of
illumination intensity on image quality [80].
Barreiros et al. proposed the development of a tracking algorithm using YOLOv2 and Kalman filter to accurately track
the movements of groups of zebrafish in a controlled experimental setup [81]. They successfully implemented a system
that could detect and track individual fish within a group, delimiting the region of fish heads for detection and estimating
the best state of the fish’s head position in each frame using the Kalman filter
Rančić et al. developed and tested a pipeline for detecting animals, specifically deer, using YOLOv3, YOLOv4,
YOLOv4-tiny, and SSD applied to UAV images [82]. While the study achieved high-performance predictions, limitations
included the challenge of limited data addressed through pre-trained models, indicating the need for further research to
enhance the system’s robustness and generalizability [82].
Zheng et al. proposed the YOLO-BYTE algorithm for tracking multiple dairy cows using a single camera [83]. Despite
achieving high precision in dairy cow target detection, potential environmental impacts on accuracy were acknowledged,
emphasizing the algorithm’s need for further examination across diverse datasets and scenarios [83].
Wangli, et al. proposed a new pig detection and counting model called YOLOv5-SA-FC, which integrates shuffle
attention and Focal-CIoU loss into the YOLOv5 framework backbone [84]. By leveraging the shuffle attention module,
the model dynamically focuses on relevant features for pig detection and counting while reducing the weights of
non-essential features. Additionally, the Focal-CIoU loss mechanism prioritizes predicted boxes with higher overlap
with the target box, improving detection performance. Similarly, Jonggwan et al. developed an EmbeddedPigCount
technology that utilizes TinyYOLOv4 to accurately count pigs on large-scale pig farms [85]. They collected image
data from a commercial pig farm in Korea, where a surveillance camera captured images of pigs and humans moving
in a hallway. The researchers manually annotated bounding boxes in the images and used a total of 2675 images for
training the detection module. The research achieved a counting accuracy of 99.44% even when pigs passed through
the counting zone back and forth.

5.4   Disease Detection in Agriculture Using YOLO

The agricultural sector faces constant challenges in maintaining crop health and ensuring optimal yields. Identifying and
addressing plant diseases promptly are essential components of sustainable farming practices. With advancements in
computer vision and deep learning, particularly the You Only Look Once (YOLO) algorithm, there has been a growing
interest in leveraging these technologies for automated disease detection in crops.
This subsection explores several studies that employ YOLO-based models to detect and monitor diseases in agricultural
settings. These studies showcase the potential of YOLO in providing accurate and efficient solutions for disease
identification, contributing to the development of intelligent and technology-driven approaches in modern agriculture.
Liu and Wang conducted a study focusing on the detection of tomato diseases and insect pests in natural environments,
culminating in the creation of a dedicated dataset [86]. Utilizing the YOLO v3 model, they achieved a commendable
detection accuracy of 92.39% in a swift 20.39 ms. The improved YOLO v3 surpassed alternative methods in both
accuracy and speed, including SSD, Faster R-CNN, and the original YOLO v3. While the algorithm demonstrated
effectiveness in real-time detection, there remains an opportunity to enhance both accuracy and speed for practical
applications, particularly in comparison to the high precision attainable through deep learning-based classification
methods.
Morbekar and colleagues developed a real-time crop disease detection model utilizing the YOLO object detection
method [87] for detection and classification, as shown in Figure 8. The model exhibited promising results with a notable
accuracy of 98.5% when tested on the PlantVillage dataset. However, the study’s limitations include the dataset’s focus

                                                            19
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

                               Figure 8: Real-time YOLO-based Leaf Disease Detection

on major crops in India, potentially limiting its applicability to other crops and regions. Additionally, the system’s scope
is confined to detecting diseases solely on leaves, neglecting other crucial parts of the crop, such as stems or fruits.
Nihar and Raghavendra proposed an innovative approach for real-time rice crop disease detection, developing a state-of-
the-art deep learning model based on the tiny_yolov3 algorithm [88]. Achieving an impressive accuracy rate of 98.92%,
their model facilitates early identification of potential issues, allowing farmers to proactively safeguard their crops. The
authors suggested the model’s adaptability for pest detection, enhancing its versatility for diverse applications.
Agbulos et al. employed the YOLO Algorithm to identify rice leaf diseases, achieving an overall accuracy of 73.33%
[89]. While successful in identifying leaf blast and brown spot diseases, the study’s focus on static rice leaf images
and the hardware setup’s limitations, including the Raspberry Pi 3 and camera module, pose potential challenges in
real-world scenarios. Future improvements may involve upgrading hardware components for enhanced image quality
and exploring a broader spectrum of diseases in rice plants.
Lippi and colleagues developed an insect detection system using a YOLO-based Convolutional Neural Network (CNN)
for identifying true bugs in hazelnut orchards [90]. With an average precision of approximately 94.5%, the system
showcased real-time processing capabilities. However, scalability concerns arise when applying the system to large
orchards, and potential challenges associated with the system’s depth sensor resolution may impact its performance.
Reddy and Deeksha trained a YOLOv4 model for detecting and identifying leaf diseases in mulberry crops, achieving
high speed and accuracy [91]. The model’s capability to recommend corresponding pesticides post-detection holds
promise for effective disease management. The study, while successful in its focus on mulberry crops, encourages
further exploration for identifying various diseases and considering real-time video classification.
Mathew and Mahesh explored the significance of early disease detection in apple trees, employing YOLO V3 networks
for disease detection [92]. The study highlighted YOLO V3’s benefits, such as faster results and improved accuracy, but
acknowledged challenges, including environmental interference and the need for continuous plant health monitoring.
Verma et al. proposed a framework employing YOLO algorithms for insect detection in soybean crops [93]. While
achieving high mean average precision, the study acknowledged limitations, including dataset size constraints and
occasional misclassifications. The potential ethical and environmental implications of pesticide application based on
insect detection were also noted for further consideration.
Kundu et al. developed a YOLO v5-based system for automated seed segregation and classification, achieving high
precision and recall of 99% [94]. While impactful in classifying pearl millet and maize seeds, the study identified the
need for further research in seed classification for mixed cropping scenarios and the broader categorization of seeds
based on crop type and quality.

                                                            20
  M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                          APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

                          Table 10: Studies on Crop Disease and Pest Detection Using YOLO
 Authors           Model                                         Details
 [86]              YOLO v3                                       Detection of tomato diseases and insect pests.
                                                                 Accuracy of 92.39% in 20.39 ms.
 [87]              YOLO                                          Real-time crop disease detection. Accuracy of
                                                                 98.5% on PlantVillage dataset.
 [88]              YOLO-v3 Tiny                                  Real-time rice crop disease detection. Accu-
                                                                 racy rate of 98.92%.
 [89]              YOLO                                          Identification of rice leaf diseases. Overall ac-
                                                                 curacy of 73.33%.
 [90]              YOLO-based CNN                                Insect detection in hazelnut orchards. Average
                                                                 precision of approximately 94.5%.
 [91]              YOLOv4                                        Mulberry crop disease detection. High speed
                                                                 and accuracy.
 [92]              YOLO V3                                       Apple tree disease detection. Improved accu-
                                                                 racy and faster results.
 [93]              YOLO                                          Insect detection in soybean crops. High mean
                                                                 average precision.
 [94]              YOLO v5                                       Seed classification in agriculture. Precision and
                                                                 recall of 99%.
 [95]              YOLO v5                                       Bell pepper plant disease identification. Supe-
                                                                 rior accuracy and reduced model size.
 [96]              YOLOv7                                        Tea leaf disease detection. AI-based solution
                                                                 for Bangladesh’s tea cultivation.
 [97]              YOLO-Tea model                                Improved model for tea disease and insect pest
                                                                 detection.

Mathew and Mahesh employed YOLO v5 for identifying diseases in bell pepper plants, demonstrating superior accuracy
and reduced model size [95]. The study hinted at the potential extension of disease detection to various diseases
affecting bell pepper plants, promising improvements in farm yield through prompt disease identification.
Soeb et al. introduced an AI-based solution using the YOLOv7 approach for detecting tea leaf diseases, emphasizing the
need to explore AI’s benefits in Bangladesh’s tea cultivation [96]. Acknowledging limitations such as limited labelled
data and a lack of established evaluation metrics, the study advocated for further research to enhance the YOLOv7
model’s effectiveness in tea leaf disease detection.
Xue et al. proposed the YOLO-Tea model, addressing small target challenges for tea diseases and insect pests with
improved feature extraction and attention mechanisms [97]. While showcasing its potential through ablative experiments
and comparisons, the study emphasized the need for continued exploration and evaluation, particularly in real-world tea
disease monitoring applications. Table 10 provides an overview of studies employing various YOLO architectures for
the detection of crop diseases and pests in the agricultural domain.

5.5   Precision Framing Using YOLO

Precision farming, a crucial aspect in various agricultural applications, involves accurately delineating and identifying
specific targets within an image or video frame. The application of You Only Look Once (YOLO) algorithms in
precision framing has demonstrated remarkable capabilities in detecting and classifying objects with speed and
efficiency. This subsection explores several studies that leverage YOLO for precision framing in diverse agricultural
contexts, showcasing its effectiveness in tasks such as disease and pest detection, seed classification, and more. These
applications not only enhance the accuracy of target identification but also contribute to optimizing agricultural processes
and improving overall crop management.
Li et al. employed convolutional neural networks (CNNs) to identify agricultural greenhouses (AGs) in high-resolution
satellite images [98]. The study compared the performance of three prominent CNN-based object detection models:

                                                            21
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

Faster R-CNN, YOLO v3, and SSD. Utilizing the PyTorch deep learning framework on a workstation equipped with
two TITAN RTX GPUs, the authors trained and evaluated the models. By fusing GF-1 data into 2 m multispectral
data along with GF-2, the study enhanced sample diversity and assessed method transferability across distinct data
sources exhibiting similar AG styles. The findings indicated that the YOLO v3 model surpassed the other models
in terms of accuracy and efficiency for AG detection. While the research contributes valuable insights into AG
detection methodologies and CNN-based object detection in remote sensing, the authors recognized the need for future
investigations to leverage multispectral and hyperspectral data in satellite images for improved object detection. The
study’s exclusive focus on AG detection prompts further exploration of other geospatial objects in future research.
Khan et al. developed a deep learning system for distinguishing between crops and weeds in strawberry and pea
fields, aiming for integration into precision agriculture sprayers for real-time weed management [99]. Unmanned
aerial vehicles equipped with cameras captured field images, and the deep learning techniques were optimized for
high accuracy in identifying small weed patches, particularly in early growth stages. The system exhibited an overall
average accuracy of 94.73%, outperforming existing machine learning and deep learning-based approaches. Despite its
robustness, the study acknowledged limitations related to dataset size, generalizability, and real-time integration into
precision spraying systems, calling for additional research and development.
Mamdouh and Khattab introduced a YOLO-based deep learning framework for detecting and counting olive fruit
flies in orchards [100]. The framework demonstrated exceptional precision (0.84), recall (0.97), F1-score (0.9), and
mean Average Precision (mAP) of 96.68%, surpassing existing pest detection systems. The authors highlighted
the framework’s potential benefits over traditional manual methods, emphasizing its effectiveness through extensive
simulation experiments. Recognizing the framework’s limitations, including a lack of a large-scale dataset, the authors
proposed future improvements such as real-life image evaluation, dataset enrichment, and transformation into a
multi-class classifier.

5.6   Comparative Analysis

Our methodology systematically compares different YOLO applications within agricultural settings, integrating key
aspects such as task complexity, control over experimental conditions, hardware dependencies, and a critical analysis of
results and error measurement methods. This holistic approach not only assesses performance but also elucidates the
practical implications of deploying these models in real-world agricultural scenarios.
In the comparative analysis of different YOLO versions across various application domains, particularly in agriculture,
each version of the YOLO architecture demonstrates unique strengths and encounters specific limitations that influence
its suitability for certain tasks (see Table 11). For instance, YOLOv1 primarily addressed standard datasets like VOC
2007 or Sesame Fields Image Dataset with straightforward object recognition tasks like weed detection. In contrast,
later versions like YOLOv4 and YOLOv5 have been utilized in more complex agricultural datasets that feature varied
backgrounds, multiple object classes, and demand real-time detection capabilities. These tasks are evaluated not only
for accuracy but also for the model’s ability to manage the intricacies of natural scenes, including variable lighting
conditions, occlusions, and overlapping objects.
Our analysis underscores the importance of controlling experimental conditions to validate the robustness of object
detection models. YOLOv3’s deployment in UAV-based weed detection, for instance, involves not just the algorithm’s
performance but also factors like flight stability, camera quality, and environmental interference—all of which sig-
nificantly impact outcomes. Similarly, YOLOv6’s application in wildlife monitoring presents challenges such as
varying animal speeds and camouflaged backgrounds, pushing the limits of detection capabilities under less controlled
but highly variable conditions. The choice of hardware significantly influences the deployment of YOLO models.
Our review spans hardware from high-end GPUs for training to embedded systems like NVIDIA Jetson for infield
deployment, critically evaluating performance metrics like frame rate, processing speed, and power consumption to
determine feasibility in agricultural settings where limited power and mobility often dictate hardware choices.
Our methodology includes a critical review of error measurement techniques, now detailed in the ’Performance Metrics’
column of our comparative analysis table (see Table 11). We focus on metrics such as precision, recall, mAP, and F1
score, which are crucial for assessing model performance across different scenarios. Additionally, we categorize errors
into types such as localization, classification, and false positives/negatives. This categorization not only provides a
nuanced view of model performance but also enhances our understanding of the practical implications of deploying
these models in field conditions. For instance, in YOLOv4’s application in crop disease detection, understanding the
impact of false negatives is crucial, as missing a diseased plant could lead to wider spread within the crop.
Compiling data from this comprehensive methodology allows us to synthesize findings across different YOLO applica-
tions and versions, highlighting trends like improvements in speed and accuracy versus trade-offs in computational
demand and complexity. This synthesis not only addresses current research questions but also identifies gaps for future

                                                          22
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

research, suggesting potential model training or deployment enhancements to better meet the specific needs of precision
agriculture. The evolution of the YOLO architectures marks a significant trajectory of technological enhancements,
methodically refined to address the diverse and challenging demands of agricultural applications. Each version from
YOLOv1 through YOLOv10 has been adapted to overcome specific limitations, leading to more sophisticated systems
capable of complex environmental interactions. These iterative advancements highlight the importance of selecting
the appropriate YOLO variant tailored to specific agricultural tasks, balancing computational demands with precision
requirements for tasks such as pest identification and crop disease monitoring. By aligning the model capabilities with
task-specific needs, researchers and practitioners can harness YOLO technologies to propel the future of precision
agriculture and sustainable farming practices effectively.
This comparative analysis highlights the critical role of model selection based on specific application needs and the
technological trade-offs involved, providing a framework for future research and application in technology-driven
agriculture.

        Table 11: Comparative Analysis of Different YOLO Versions Across Various Application Domains
 YOLO             Application Domain             Strengths                     Limitations
 Version
    YOLOv1         Object Detection, Weed and         Fast real-time processing        Struggles with small objects
                   Crop Detection
                   [63, 68, 69, 76, 87, 89, 92, 93]
    YOLOv2         Animal Tracking [81]               Improved recall, handles small   Higher computational
                                                      objects better                   requirements
    YOLOv3         Agriculture                        Multi-scale detection, good in   Not optimized for very
                   [61, 70, 71, 72, 77, 86, 88, 92]   diverse conditions               low-power devices
    YOLOv4         Agriculture                        Robust in complex visual         Setup complexity for training
                   [62, 66, 75, 78, 91, 85]           environments                     on custom datasets
    YOLOv5         Weed Detection                     Very fast, suitable for          May require fine-tuning for
                   [65, 67, 94, 95, 84]               real-time applications           specific scenarios
    YOLOv6         Wildlife Monitoring [101]          High accuracy with enhanced      Needs high computation
                                                      depth                            power for best results
    YOLOv7         Crop Disease Detection [96]        High precision, effective in     Computational efficiency
                                                      crowded scenes                   decreases with scale
    YOLOv8         Agriculture [80, 102]              Very high speed, suitable for    Can struggle with very small
                                                      dynamic environments             or fast-moving objects
    YOLOv9         Plant Disease detection            High accuracy and recall,        Requires extensive dataset for
                   [103, 104]                         suitable for detailed medical    training
                                                      scans
    YOLOv10        —                                  Enhanced accuracy-efficiency     Complex configuration for
                                                      trade-off, NMS-free model        multi-source integration

6     Discussion
The integration of YOLO variants in agriculture has emerged as a transformative approach, revolutionizing various
aspects of farming and crop management. As evidenced in Table 8, 9 and 10, the diverse range of YOLO models
employed for agricultural applications showcases the adaptability and efficacy of this architecture in addressing the
unique challenges within the agricultural domain. Notably, the consistently high levels of accuracy achieved across
different applications, including weed detection, crop identification, and disease diagnosis, underscore the robust
performance of YOLO-based models in diverse agricultural scenarios.
Real-time Precision Agriculture: One of the standout features of YOLO variants in agriculture is their ability to
facilitate real-time precision farming. The models, such as YOLOv3, YOLOv4, and YOLOv5, have demonstrated
exceptional swiftness and accuracy in detecting and identifying objects in agricultural landscapes. This real-time
capability holds significant promise for optimizing farming practices, enabling timely decision-making, and enhancing
resource allocation efficiency.
Weed Detection and Management: The application of YOLO variants in weed detection, as illustrated by studies
such as [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], signifies a paradigm shift in traditional weed management practices.
The real-time identification and localization of weeds using YOLO models empower farmers to implement targeted

                                                           23
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

and efficient weed control measures. Despite certain challenges, such as resolution limitations in detecting smaller
objects, the overall performance of YOLO-based systems like YOLO-WEED [61] and YOLOv4-weeds [62] indicates
their potential for widespread adoption in weed management.
Crop Detection and Monitoring: The significance of robust crop detection methodologies in precision agriculture
cannot be overstated. YOLO variants, as exemplified by studies such as [71, 72, 73, 74, 75, 76], contribute to accurate
identification and delineation of crops in large-scale fields. These models offer a comprehensive solution for monitoring
crop health, estimating yields, and optimizing resource management. The development of specialized models like
CitrusYOLO [74] and YOLO-P [73] for specific crops further emphasizes the adaptability of YOLO architectures to
diverse agricultural settings.

7     Challenges in YOLO-based Agricultural Applications

While the achievements in agricultural applications of YOLO are remarkable, challenges persist. The regional specificity
in some datasets, hardware constraints, and the need for further research to enhance model applicability are areas
that warrant attention. Future work should focus on addressing these challenges, exploring the generalizability of
models to different crops and environmental conditions, and fostering advancements in sensing technologies for broader
applications.

7.1    Data Specificity and Generalization

One notable challenge in YOLO-based agricultural applications lies in the specificity of datasets used for model
training. Many studies focus on particular crops or regions, which may limit the model’s generalizability across diverse
agricultural landscapes [105]. Addressing this challenge involves creating more comprehensive and diverse datasets
that encompass various crops, growth stages, and environmental conditions [106]. Additionally, research efforts should
aim at developing transfer learning techniques to enhance model adaptability to new agricultural contexts [107].

7.2    Hardware Limitations

The deployment of YOLO-based systems in real-world agricultural settings may encounter hardware constraints,
especially in resource-limited environments [108]. Many studies leverage powerful computing resources for model
training and inference, but practical implementation on edge devices or embedded systems poses challenges [109].
Future research should explore model optimization techniques, quantization, and lightweight architectures to make
YOLO variants more accessible for deployment on edge devices commonly used in precision farming equipment.

7.3    Environmental Variability

Agricultural environments are inherently dynamic, with variations in lighting conditions, weather, and terrain. YOLO
models, while robust, may face challenges in adapting to these environmental changes. Ensuring the reliability of
detection under diverse conditions requires the development of models that are resilient to variations in illumination,
adverse weather, and different terrains. This necessitates the incorporation of environmental adaptability in model
training and further exploration of techniques like domain adaptation.

7.4    Small Object Detection

Identifying diminutive weeds or diseases in agricultural contexts presents a unique set of hurdles for YOLO variants.
The intrinsic structure of YOLO may encounter difficulties in discerning smaller objects within an image. Addressing
this obstacle necessitates advancements in feature extraction, attention mechanisms, or the exploration of multi-scale
detection strategies. Moreover, ensemble techniques can be used to overcome false positives and negatives as done
by researchers [110, 111, 112, 113]. It is crucial for future research to concentrate on refining YOLO architectures to
augment the precision of detecting small objects in precision farming applications. Furthermore, the integration of
attention mechanisms can serve as a valuable approach, steering YOLO architectures towards subtle defects, as has
been successfully implemented in industries like textiles [114, 115, 116, 117, 118, 119].

                                                           24
    M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                            APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

8     Future Directions and Opportunities
8.1    Multi-Modal Integration

The integration of multi-modal data sources, such as combining RGB images with thermal or hyperspectral data, holds
great potential for advancing YOLO-based agricultural applications [120]. Combining different modalities can provide
richer information for more accurate and robust detection of crops, weeds, and diseases. Future research should explore
the fusion of diverse data sources to enhance the overall performance and reliability of YOLO models in precision
agriculture.

8.2    Explainability and Interpretability

As YOLO models become integral to decision-making in agriculture, ensuring their explainability and interpretability is
crucial. Farmers and stakeholders need to understand the rationale behind model predictions to trust and effectively
implement precision farming practices. Future work should focus on developing methodologies for explaining YOLO
model decisions and providing insights into how and why certain detections are made, especially in complex and
dynamic agricultural environments.

8.3    Real-Time Adaptive Systems

The evolution of YOLO architectures toward real-time capabilities opens avenues for developing adaptive systems that
respond dynamically to changing agricultural conditions. Future YOLO-based models could incorporate real-time
learning mechanisms, enabling them to adapt and improve their performance over time based on continuous feedback
from the field. This would contribute to the development of intelligent and self-improving precision agriculture systems.

8.4    Human-AI Collaboration

Recognizing the expertise of farmers, future research should explore models that facilitate human-AI collaboration
in decision-making processes. Integrating farmer knowledge with AI-driven insights can lead to more effective and
context-aware agricultural practices. Human-AI collaboration is vital for addressing the complexities and uncertainties
inherent in agriculture, allowing for seamless integration of YOLO-based technologies into the existing farming
ecosystem.
In summary, overcoming the challenges and leveraging future opportunities requires a concerted effort from the research
community, industry stakeholders, and farmers. The continuous refinement of YOLO-based models, coupled with
advancements in data collection, hardware, and interpretability, will propel the application of AI in agriculture towards
sustainable and efficient farming practices.

9     Conclusion
In conclusion, the intersection of YOLO variants and agriculture presents a transformative potential for precision
farming, weed management, and crop monitoring. The consistent advancements and promising results showcased in
various studies underscore the pivotal role of YOLO architectures in shaping the future of smart and efficient agriculture.
The comprehensive review of YOLO variants in agricultural applications highlights the transformative potential of
these models in revolutionizing precision farming. From crop detection and disease identification to weed management,
YOLO variants have showcased remarkable capabilities, offering real-time and efficient solutions to long-standing
challenges in agriculture. The discussion and analysis of various studies underscore the versatility and adaptability of
YOLO architectures across diverse agricultural scenarios. Despite the evident successes, challenges persist, necessitating
ongoing research efforts. The specificity of training datasets, hardware limitations, and environmental variability pose
hurdles that demand innovative solutions. Future research should prioritize the development of more inclusive datasets,
optimization techniques for edge devices, and models resilient to dynamic agricultural environments.
Looking ahead, multi-modal integration, explainability, and real-time adaptive systems present exciting opportunities
for further enhancing the utility of YOLO models in agriculture. The fusion of different data modalities, coupled with
real-time learning mechanisms, can usher in a new era of intelligent and context-aware precision farming. Additionally,
a focus on human-AI collaboration acknowledges the indispensable role of farmers in the decision-making process,
promoting a harmonious integration of AI technologies into existing agricultural practices. In conclusion, the evolution
of YOLO variants in agriculture signifies a paradigm shift towards sustainable, efficient, and technologically-driven
farming practices. As researchers, practitioners, and stakeholders collaborate, the future holds great promise for the

                                                            25
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

continued advancement of YOLO-based applications, contributing to the global effort to address food security and
promote environmentally conscious agriculture.

References
  [1] Diwan P Ariana, Renfu Lu, and Daniel E Guyer. Near-infrared hyperspectral reflectance imaging for detection
      of bruises on pickling cucumbers. Computers and electronics in agriculture, 53(1):60–70, 2006.
  [2] Muhammad Hussain. Yolo-v1 to yolo-v8, the rise of yolo and its complementary nature toward digital manufac-
      turing and industrial defect detection. Machines, 11(7):677, 2023.
  [3] Xiaolin Zhu and Guanghui Li. Rapid detection and visualization of slight bruise on apples using hyperspectral
      imaging. International journal of food properties, 22(1):1709–1719, 2019.
  [4] Amirhossein Zaji, Zheng Liu, Gaozhi Xiao, Pankaj Bhowmik, Jatinder S Sangha, and Yuefeng Ruan. Wheat
      spikes height estimation using stereo cameras. IEEE Transactions on AgriFood Electronics, 2023.
  [5] Shuang-Lin Mao, Yu-Ming Wei, Wenguang Cao, Xiu-Jin Lan, Ma Yu, Zheng-Mao Chen, Guo-Yue Chen, and
      You-Liang Zheng. Confirmation of the relationship between plant height and fusarium head blight resistance in
      wheat (triticum aestivum l.) by qtl meta-analysis. Euphytica, 174:343–356, 2010.
  [6] Xu Wang, Daljit Singh, Sandeep Marla, Geoffrey Morris, and Jesse Poland. Field-based high-throughput
      phenotyping of plant height in sorghum using different sensing technologies. Plant Methods, 14(1):1–16, 2018.
  [7] S. Liao, J. Wang, R. Yu, K. Sato, and Z. Cheng. Cnn for situations understanding based on sentiment analysis of
      twitter data. Procedia Computer Science, 111:376–381, 2017.
  [8] H. Sak, A. Senior, K. Rao, and F. Beaufays. Fast and accurate recurrent neural network acoustic models for
      speech recognition. arXiv:1507.06947 [cs, stat], Jul. 2015.
  [9] Mujadded Al Rabbani Alif, Sabbir Ahmed, and Muhammad Abul Hasan. Isolated bangla handwritten character
      recognition with convolutional neural network. pages 1–6, 2017.
 [10] Y. Zhang, Y. Tong, and Y. Jiang. Study of sentiment classification for chinese microblog based on recurrent
      neural network. Chinese Journal of Electronics, 25(4):601–607, Jul. 2016.
 [11] S. Lai, L. Xu, K. Liu, and J. Zhao. Recurrent convolutional neural networks for text classification. Proceedings
      of the AAAI Conference on Artificial Intelligence, 29(1), Feb. 2015.
 [12] D. Wei and et al. Research on unstructured text data mining and fault classification based on rnn-lstm with
      malfunction inspection report. Energies, 10(3):406, Mar. 2017.
 [13] D. Quang and X. Xie. Danq: A hybrid convolutional and recurrent deep neural network for quantifying the
      function of dna sequences. Nucleic Acids Research, 44(11):e107–e107, Apr. 2016.
 [14] Mujadded Al Rabbani Alif, Muhammad Hussain, Gareth Tucker, and Simon Iwnicki. Boltvision: A comparative
      analysis of cnn, cct, and vit in achieving high accuracy for missing bolt classification in train components.
      Machines, 12(2):93, 2024.
 [15] Mujadded Al Rabbani Alif and Muhammad Hussain. Lightweight convolutional network with integrated attention
      mechanism for missing bolt detection in railways. Metrology, 4(2):254–278, 2024.
 [16] Mujadded Al Rabbani Alif. Attention-based automated pallet racking damage detection. 9(1), 2024.
 [17] M. R. Mezaal, B. Pradhan, M. I. Sameen, H. Z. Mohd Shafri, and Z. M. Yusoff. Optimized neural architecture
      for automatic landslide detection from high-resolution airborne laser scanning data. Applied Sciences, 7(7):730,
      Jul. 2017.
 [18] N. Xu and et al. Dual-stream recurrent neural network for video captioning. IEEE Transactions on Circuits and
      Systems for Video Technology, 29(8):2482–2493, Aug. 2019.
 [19] J. Kim, J. Kim, H. L. Thu, and H. Kim. Long short term memory recurrent neural network classifier for intrusion
      detection. In 2016 International Conference on Platform Technology and Service (PlatCon), 2016.
 [20] A. M. Rather, A. Agarwal, and V. N. Sastry. Recurrent neural network and a hybrid model for prediction of stock
      returns. Expert Systems with Applications, 42(6):3234–3241, Apr. 2015.
 [21] Ming Liang and Xiaolin Hu. Recurrent convolutional neural network for object recognition. IEEE Xplore, Jun.
      2015. (accessed Dec. 03, 2020).
 [22] W. Nash, T. Drummond, and N. Birbilis. A review of deep learning in the study of materials degradation. npj
      Materials Degradation, 2(1), Nov. 2018.

                                                         26
M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                        APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

[23] T. Diwan, G. Anirudh, and J. V. Tembhurne. Object detection using yolo: Challenges, architectural successors,
     datasets and applications. Multimedia Tools and Applications, Aug. 2022.
[24] Y. Bengio, A. Courville, and P. Vincent. Unsupervised feature learning and deep learning: A review and new
     perspectives, 2012. Accessed: May 17, 2023.
[25] Ujjwal. An intuitive explanation of convolutional neural networks. the data science blog, May 29 2017.
[26] K. Chen, K. Franko, and R. Sang. Structured model pruning of convolutional networks on tensor processing
     units. arXiv:2107.04191 [cs], Jul. 2021.
[27] S. Agarwal, J. O. D. Terrail, and F. Jurie. Recent advances in object detection in the age of deep convolutional
     neural networks. arXiv.org, Aug. 20 2019.
[28] L. Liu and et al. Deep learning for generic object detection: A survey. Sep. 2018.
[29] C.-Y. Wang, H.-Y. M. Liao, Y.-H. Wu, P.-Y. Chen, J.-W. Hsieh, and I.-H. Yeh. Cspnet: A new backbone that can
     enhance learning capability of cnn. openaccess.thecvf.com, 2020. (accessed Apr. 23, 2023).
[30] Xingxing Xie, Gong Cheng, Jiabao Wang, Xiwen Yao, and Junwei Han. Oriented r-cnn for object detection. In
     Proceedings of the IEEE/CVF international conference on computer vision, pages 3520–3529, 2021.
[31] R. Girshick. Fast r-cnn. In International Conference on Computer Vision, pages 1137–1149, 2015.
[32] S. Ren and et al. Faster r-cnn: towards real-time object detection with region proposal networks. In IEEE
     Transactions on Pattern Analysis and Machine Intelligence, pages 1137–1149, 2017.
[33] T.-Y. Lin and et al. Feature pyramid networks for object detection. In Proceedings of the 2017 IEEE Conference
     on Computer Vision and Pattern Recognition (CVPR), pages 936–944, 2017.
[34] W. Liu and et al. Ssd: single shot multibox detector. In European Conference on Computer Vision, 2016.
[35] Chang Sun, Yibo Ai, Sheng Wang, and Weidong Zhang. Dense-refinedet for traffic sign detection and classifica-
     tion. Sensors, 20(22):6570, 2020.
[36] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and Piotr Dollár. Focal loss for dense object detection. arXiv (Cornell
     University), Aug. 2017.
[37] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi. You only look once: Unified, real-time object detection. In
     CVPR, pages 779–788, 2016.
[38] J. Redmon and A. Farhadi. Yolo9000: Better, faster, stronger. Dec. 2016.
[39] F. Borisyuk, A. Gordo, and V. Sivakumar. Rosetta. In Proceedings of the 24th ACM SIGKDD International
     Conference on Knowledge Discovery & Data Mining, Jul. 2018.
[40] J.-H. Won, D.-H. Lee, K.-M. Lee, and C.-H. Lin. An improved yolov3-based neural network for de-identification
     technology. IEEE Xplore, Jun. 2019.
[41] M. Everingham, S. M. A. Eslami, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisserman. The PASCAL
     visual object classes (voc) challenge. International Journal of Computer Vision, 88(2):303–338, 2010.
[42] T.-Y. Lin et al. Microsoft coco: Common objects in context. 2014.
[43] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao. Yolov4: Optimal speed and accuracy of object detection. Apr.
     2020.
[44] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. openaccess.thecvf.com, 2016.
[45] Z. Ma, M. Li, and Y. Wang. Pan: Path integral based convolution for deep graph neural networks. Apr. 2019.
[46] Z. Yao, Y. Cao, S. Zheng, G. Huang, and S. Lin. Cross-iteration batch normalization. In openaccess.thecvf.com,
     2021.
[47] S. He, R. Bao, J. Li, P. E. Grant, and Y. Ou. Accuracy of segment-anything model (sam) in medical image
     segmentation tasks. Apr. 2023.
[48] J. Solawetz. YOLOv5 New Version - Improvements and Evaluation. Roboflow Blog, Jun. 2020.
[49] C.-Y. Wang, A. Bochkovskiy, and H.-Y. Liao. YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for
     real-time object detectors, Jul. 2022.
[50] Z. Wang et al. Mosaic representation learning for self-supervised visual pre-training. openreview.net, Feb. 2023.
[51] J. Solawetz and et al. What’s new in yolov6?, Jul. 2022.
[52] X. Xu, Y. Jiang, W. Chen, Y. Huang, Y. Zhang, and X. Sun. Damo-yolo: A report on real-time object detection
     design, Dec. 2022.

                                                        27
M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                        APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

[53] X. Ding, X. Zhang, N. Ma, J. Han, G. Ding, and J. Sun. Repvgg: Making vgg-style convnets great again. In
     openaccess.thecvf.com, 2021.
[54] G. Huang, Z. Liu, and Kilian Q Weinberger. Densely connected convolutional networks. 2016.
[55] G. Jocher, A. Chaurasia, and J. Qiu. Yolo by ultralytics, 2023. Accessed: February 30, 2023.
[56] J. Solawetz. Yolov7 - a breakdown of how it works, Jul. 2022.
[57] J. Solawetz and et al. What is yolov8? the ultimate guide, Jan. 2023.
[58] G. Jocher and et al. ultralytics/yolov5: v3.0, Aug. 2020.
[59] Chien-Yao Wang and Hong-Yuan Mark Liao. YOLOv9: Learning what you want to learn using programmable
     gradient information. 2024.
[60] Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong Han, and Guiguang Ding. Yolov10: Real-time
     end-to-end object detection. arXiv preprint arXiv:2405.14458, 2024.
[61] Addie Ira Borja PARICO and Tofael AHAMED. An aerial weed detection system for green onion crops using
     the you only look once (yolov3) deep learning algorithm. Engineering in Agriculture, Environment and Food,
     13(2):42–48, 2020.
[62] Boyu Ying, Yuancheng Xu, Shuai Zhang, Yinggang Shi, and Li Liu. Weed detection in images of carrot fields
     based on improved yolo v4. Traitement du Signal, 38(2), 2021.
[63] Mads Dyrmann, Anders Krogh Mortensen, Lars Linneberg, Toke Thomas Høye, and Kim Bjerge. Camera
     assisted roadside monitoring for invasive alien plant species using deep learning. Sensors, 21(18):6126, 2021.
[64] Jiqing Chen, Huabin Wang, Hongdu Zhang, Tian Luo, Depeng Wei, Teng Long, and Zhikui Wang. Weed detection
     in sesame fields using a yolo model with an enhanced attention mechanism and feature fusion. Computers and
     Electronics in Agriculture, 202:107412, 2022.
[65] Qifan Wang, Man Cheng, Shuo Huang, Zhenjiang Cai, Jinlin Zhang, and Hongbo Yuan. A deep learning
     approach incorporating yolo v5 and attention mechanisms for field real-time detection of the invasive weed
     solanum rostratum dunal seedlings. Computers and Electronics in Agriculture, 199:107194, 2022.
[66] Benjamin Costello, Olusegun O Osunkoya, Juan Sandino, William Marinic, Peter Trotter, Boyang Shi, Felipe
     Gonzalez, and Kunjithapatham Dhileepan. Detection of parthenium weed (parthenium hysterophorus l.) and its
     growth stages using artificial intelligence. Agriculture, 12(11):1838, 2022.
[67] Fengying Dang, Dong Chen, Yuzhen Lu, and Zhaojian Li. Yoloweeds: a novel benchmark of yolo object
     detectors for multi-class weed detection in cotton production systems. Computers and Electronics in Agriculture,
     205:107655, 2023.
[68] Fernando J Pérez-Porras, Jorge Torres-Sánchez, Francisca López-Granados, and Francisco J Mesas-Carrascosa.
     Early and on-ground image-based detection of poppy (papaver rhoeas) in wheat using yolo architectures. Weed
     Science, 71(1):50–58, 2023.
[69] Mino Sportelli, Orly Enrique Apolo-Apolo, Marco Fontanelli, Christian Frasconi, Michele Raffaelli, Andrea
     Peruzzi, and Manuel Perez-Ruiz. Evaluation of yolo object detectors for weed detection in different turfgrass
     scenarios. Applied Sciences, 13(14):8502, 2023.
[70] Xiaojun Jin, Yanxia Sun, Jun Che, Muthukumar Bagavathiannan, Jialin Yu, and Yong Chen. A novel deep
     learning-based method for detection of weeds in vegetables. Pest Management Science, 78(5):1861–1869, 2022.
[71] Yunong Tian, Guodong Yang, Zhe Wang, Hao Wang, En Li, and Zize Liang. Apple detection during different
     growth stages in orchards using the improved yolo-v3 model. Computers and electronics in agriculture,
     157:417–426, 2019.
[72] Shaun M Sharpe, Arnold W Schumann, and Nathan S Boyd. Goosegrass detection in strawberry and tomato
     using a convolutional neural network. Scientific Reports, 10(1):9548, 2020.
[73] Mohamad Haniff Junos, Anis Salwa Mohd Khairuddin, Subbiah Thannirmalai, and Mahidzal Dahari. An
     optimized yolo-based object detection model for crop harvesting system. IET Image Processing, 15(9):2112–
     2125, 2021.
[74] Wenkang Chen, Shenglian Lu, Binghao Liu, Ming Chen, Guo Li, and Tingting Qian. Citrusyolo: A algorithm for
     citrus detection under orchard environment based on yolov4. Multimedia Tools and Applications, 81(22):31363–
     31389, 2022.
[75] Qingqing Hong, Ling Jiang, Zhenghua Zhang, Shu Ji, Chen Gu, Wei Mao, Wenxi Li, Tao Liu, Bin Li, and
     Changwei Tan. A lightweight model for wheat ear fusarium head blight detection based on rgb images. Remote
     Sensing, 14(14):3481, 2022.

                                                        28
M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                        APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

[76] Liang Wang, Lingmin Li, Hao Wang, Shaohua Zhu, Zhiqiang Zhai, and Zhongxiang Zhu. Real-time vehicle
     identification and tracking during agricultural master-slave follow-up operation using improved yolo v4 and
     binocular positioning. Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical
     Engineering Science, 237(6):1393–1404, 2023.
[77] Juan Wang, Nan Wang, Lihua Li, and Zhenhui Ren. Real-time behavior detection and judgment of egg breeders
     based on yolo v3. Neural Computing and Applications, 32:5471–5481, 2020.
[78] Anne K Schütz, Verena Schöler, E Tobias Krause, Mareike Fischer, Thomas Müller, Conrad M Freuling, Franz J
     Conraths, Mario Stanke, Timo Homeier-Bachmann, and Hartmut HK Lentz. Application of yolov4 for detection
     and motion monitoring of red foxes. Animals, 11(6):1723, 2021.
[79] Zhenwei Yu, Yuehua Liu, Sufang Yu, Ruixue Wang, Zhanhua Song, Yinfa Yan, Fade Li, Zhonghua Wang, and
     Fuyang Tian. Automatic detection method of dairy cow feeding behaviour based on yolo improved model and
     edge computing. Sensors, 22(9):3271, 2022.
[80] Wael M Elmessery, Joaquín Gutiérrez, Gomaa G Abd El-Wahhab, Ibrahim A Elkhaiat, Ibrahim S El-Soaly,
     Sadeq K Alhag, Laila A Al-Shuraym, Mohamed A Akela, Farahat S Moghanm, and Mohamed F Abdelshafie.
     Yolo-based model for automatic detection of broiler pathological phenomena through visual and thermal images
     in intensive poultry houses. Agriculture, 13(8):1527, 2023.
[81] Marta de Oliveira Barreiros, Diego de Oliveira Dantas, Luís Claudio de Oliveira Silva, Sidarta Ribeiro, and
     Allan Kardec Barros. Zebrafish tracking using yolov2 and kalman filter. Scientific reports, 11(1):3219, 2021.
[82] Kristina Rančić, Boško Blagojević, Atila Bezdan, Bojana Ivošević, Bojan Tubić, Milica Vranešević, Branislav
     Pejak, Vladimir Crnojević, and Oskar Marko. Animal detection and counting from uav images using convolutional
     neural networks. Drones, 7(3):179, 2023.
[83] Zhiyang Zheng, Jingwen Li, and Lifeng Qin. Yolo-byte: An efficient multi-object tracking algorithm for
     automatic monitoring of dairy cows. Computers and Electronics in Agriculture, 209:107857, 2023.
[84] Wangli Hao, Li Zhang, Meng Han, Kai Zhang, Fuzhong Li, Guoqiang Yang, and Zhenyu Liu. Yolov5-sa-fc: A
     novel pig detection and counting method based on shuffle attention and focal complete intersection over union.
     Animals, 13(20):3201, 2023.
[85] Jonggwan Kim, Yooil Suh, Junhee Lee, Heechan Chae, Hanse Ahn, Yongwha Chung, and Daihee Park. Embed-
     dedpigcount: Pig counting with video object detection and tracking on an embedded board. Sensors, 22(7):2689,
     2022.
[86] Jun Liu and Xuewei Wang. Tomato diseases and pests detection based on improved yolo v3 convolutional neural
     network. Frontiers in plant science, 11:898, 2020.
[87] Achyut Morbekar, Ashi Parihar, and Rashmi Jadhav. Crop disease detection using yolo. In 2020 International
     Conference for Emerging Technology (INCET), pages 1–5, 2020.
[88] G Nihar, V Raghavendra, V Suresh, and M Sandhya. Rice crop disease detection using yolo algorithm. In
     National Conference On Advances in Electronics Signal Processing and Communications (AESPC-2020),
     volume 6, 2020.
[89] Ma Kristin Agbulos, Yovito Sarmiento, and Jocelyn Villaverde. Identification of leaf blast and brown spot
     diseases on rice leaf with yolo algorithm. In 2021 IEEE 7th International Conference on Control Science and
     Systems Engineering (ICCSSE), pages 307–312. IEEE, 2021.
[90] Martina Lippi, Niccolò Bonucci, Renzo Fabrizio Carpio, Mario Contarini, Stefano Speranza, and Andrea
     Gasparri. A yolo-based pest detection system for precision agriculture. In 2021 29th Mediterranean Conference
     on Control and Automation (MED), pages 342–347, 2021.
[91] Monalika Padma Reddy and A Deeksha. Mulberry leaf disease detection using yolo. International Journal of
     Advance Research, Ideas and Innovations in Technology, 7:1816–1821, 2021.
[92] Midhun P Mathew and Therese Yamuna Mahesh. Determining the region of apple leaf affected by disease using
     yolo v3. In 2021 International Conference on Communication, Control and Information Sciences (ICCISc),
     volume 1, pages 1–4, 2021.
[93] Shani Verma, Shrivishal Tripathi, Anurag Singh, Muneendra Ojha, and Ravi R Saxena. Insect detection and
     identification using yolo algorithms on soybean crop. In TENCON 2021 - 2021 IEEE Region 10 Conference
     (TENCON), pages 272–277, 2021.
[94] Nidhi Kundu, Geeta Rani, and Vijaypal Singh Dhaka. Seeds classification and quality testing using deep learning
     and yolo v5. In Proceedings of the International Conference on Data Science, Machine Learning and Artificial
     Intelligence, pages 153–160, 2021.

                                                        29
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

 [95] Midhun P Mathew and Therese Yamuna Mahesh. Leaf-based disease detection in bell pepper plant using yolo
      v5. Signal, Image and Video Processing, pages 1–7, 2022.
 [96] Md Janibul Alam Soeb, Md Fahad Jubayer, Tahmina Akanjee Tarin, Muhammad Rashed Al Mamun, Fahim Ma-
      hafuz Ruhad, Aney Parven, Nabisab Mujawar Mubarak, Soni Lanka Karri, and Islam Md Meftaul. Tea leaf
      disease detection and identification based on yolov7 (yolo-t). Scientific reports, 13(1):6078, 2023.
 [97] Zhenyang Xue, Renjie Xu, Di Bai, and Haifeng Lin. Yolo-tea: A tea disease detection model improved by
      yolov5. Forests, 14(2):415, 2023.
 [98] Min Li, Zhijie Zhang, Liping Lei, Xiaofan Wang, and Xudong Guo. Agricultural greenhouses detection in
      high-resolution satellite images based on convolutional neural networks: Comparison of faster r-cnn, yolo v3 and
      ssd. Sensors, 20(17):4938, 2020.
 [99] Shahbaz Khan, Muhammad Tufail, Muhammad Tahir Khan, Zubair Ahmad Khan, and Shahzad Anwar. Deep
      learning-based identification system of weeds and crops in strawberry and pea fields for a precision agriculture
      sprayer. Precision Agriculture, 22(6):1711–1727, 2021.
[100] Nariman Mamdouh and Ahmed Khattab. Yolo-based deep learning framework for olive fruit fly detection and
      counting. IEEE Access, 9:84252–84262, 2021.
[101] Wenjie Mao, Gang Li, and Xiaowei Li. Improved re-parameterized convolution for wildlife detection in
      neighboring regions of southwest china. Animals, 14(8):1152, 2024.
[102] Jiayou Shi, Yuhao Bai, Jun Zhou, and Baohua Zhang. Multi-crop navigation line extraction based on improved
      yolo-v8 and threshold-dbscan under complex agricultural environments. Agriculture, 14(1):45, 2023.
[103] Chun-Tse Chien, Rui-Yang Ju, Kuang-Yi Chou, and Jen-Shiun Chiang. Yolov9 for fracture detection in pediatric
      wrist trauma x-ray images. arXiv preprint arXiv:2403.11249, 2024.
[104] Boudjemaa Boudaa, Kamel Abada, Walid Aymen Aichouche, and Ahmed Nabil Belakermi. Advancing plant
      diseases detection with pre-trained yolo models. In 2024 6th International Conference on Pattern Analysis and
      Intelligent Systems (PAIS), pages 1–6. IEEE, 2024.
[105] Zolo Kiala, John Odindi, and Onisimo Mutanga. Determining the capability of the tree-based pipeline optimiza-
      tion tool (tpot) in mapping parthenium weed using multi-date sentinel-2 image data. Remote Sensing, 14(7):1687,
      2022.
[106] Wen-Hao Su. Advanced machine learning in point spectroscopy, rgb-and hyperspectral-imaging for automatic
      discriminations of crops and weeds: A review. Smart Cities, 3(3):767–792, 2020.
[107] Yuri Shendryk, Natalie A Rossiter-Rachor, Samantha A Setterfield, and Shaun R Levick. Leveraging high-
      resolution satellite imagery and gradient boosting for invasive weed mapping. IEEE Journal of Selected Topics
      in Applied Earth Observations and Remote Sensing, 13:4443–4450, 2020.
[108] Arsalan Zahid, Muhammad Hussain, Richard Hill, and Hussain Al-Aqrabi. Lightweight convolutional network
      for automated photovoltaic defect detection. In 2023 9th International Conference on Information Technology
      Trends (ITT), pages 133–138. IEEE, 2023.
[109] Muhammad Hussain. Exudate detection: Integrating retinal-based affine mapping and design flow mechanism to
      develop lightweight architectures. IEEE Access, 2023.
[110] Hanse Ahn, Seungwook Son, Heegon Kim, Sungju Lee, Yongwha Chung, and Daihee Park. Ensemblepigdet:
      Ensemble deep learning for accurate pig detection. Applied Sciences, 11(12):5577, 2021.
[111] Manzhou Li, Siyu Cheng, Jingyi Cui, Changxiang Li, Zeyu Li, Chang Zhou, and Chunli Lv. High-performance
      plant pest and disease detection based on model ensemble with inception module and cluster algorithm. Plants,
      12(1):200, 2023.
[112] Sangyeon Lee, Amarpreet Singh Arora, and Choa Mun Yun. Detecting strawberry diseases and pest infections in
      the very early stage with an ensemble deep-learning model. Frontiers in Plant Science, 13:991134, 2022.
[113] Priya Singh and Rajalakshmi Krishnamurthi. Object detection using deep ensemble model for enhancing security
      towards sustainable agriculture. International Journal of Information Technology, 15(6):3113–3126, 2023.
[114] Rui Jin and Qiang Niu. Automatic fabric defect detection based on an improved yolov5. Mathematical Problems
      in Engineering, 2021, 2021.
[115] Jiaqi Zhang, Junfeng Jing, Pengwen Lu, and Shaojun Song. Improved mobilenetv2-ssdlite for automatic fabric
      defect detection system based on cloud-edge computing. Measurement, 201:111665, 2022.
[116] Bing Wei, Bailing Xu, Kuangrong Hao, and Lei Gao. Textile defect detection using multilevel and attentional
      deep learning network (mlma-net). Textile Research Journal, 92:004051752110737, 02 2022.

                                                         30
 M.A.R A LIF ET AL .: YOLOV 1 TO YOLOV 10: A COMPREHENSIVE REVIEW OF YOLO VARIANTS AND THEIR
                                         APPLICATION IN THE AGRICULTURAL DOMAIN - J UNE 17, 2024

[117] Zhengrui Peng, Xinyi Gong, Zhenfeng Lu, Xiangyi Xu, Bengang Wei, and Mukesh Prasad. A novel fabric
      defect detection network based on attention mechanism and multi-task fusion. In 2021 7th IEEE International
      Conference on Network Intelligence and Digital Content (IC-NIDC), pages 484–488, 11 2021.
[118] Zhoufeng Liu, Zhaochen Huo, Chunlei Li, Yan Dong, and Bicao Li. Dlse-net: A robust weakly supervised
      network for fabric defect detection. Displays, 68:102008, 07 2021.
[119] Liu Rong-qiang, Li Ming-hui, Shi Jia-chen, and Liang Yi-bin. Fabric defect detection method based on improved
      u-net. In Journal of Physics: Conference Series, volume 1948, page 012160. IOP Publishing, 2021.
[120] José Manuel Amigo and Carolina Santos. Preprocessing of hyperspectral and multispectral images. In Data
      handling in science and technology, volume 32, pages 37–53. Elsevier, 2019.

                                                        31
