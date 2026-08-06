---
source_id: 134
bibtex_key: tang2024pcbyolo
title: PCB-YOLO: Enhancing PCB Surface Defect Detection with Coordinate Attention and Multi-Scale Feature Fusion
year: 2024
domain_theme: Industri
verified_pdf: 134_PCB_YOLO.pdf
char_count: 92582
---

RESEARCH ARTICLE

                                                 PCB-YOLO: Enhancing PCB surface defect
                                                 detection with coordinate attention and multi-
                                                 scale feature fusion
                                                 Ze Wei1, Fan Yang      1
                                                                         *, Kezhen Zhong2, Linkun Yao1

                                                 1 School of Electronic and Information Engineering, Hebei University of Technology, Tianjin, China,
                                                 2 Faculty of Computing, Harbin Institute of Technology, Harbin, China

                                                 * 15602088831@163.com

                                                 Abstract
                                                 Nowadays, industrial electronic products are integrated into all aspects of life, with
                                                 PCB quality playing a decisive role in their performance. Ensuring PCB factory
                                                 quality is thus crucial. Common PCB defects serve as key references for evaluating
                                                 quality. To address low detection accuracy and the bulky size of existing models,
                                                 we propose an improved PCB-YOLO model based on YOLOv8n.To reduce model
                                                 size, we introduce a novel CRSCC module combining SCConv convolution and
   OPEN ACCESS
                                                 C2f, enhancing PCB defect detection accuracy and significantly reducing model
Citation: Wei Z, Yang F, Zhong K, Yao L
(2025) PCB-YOLO: Enhancing PCB surface
                                                 parameters. For feature fusion, we propose the FFCA attention module, designed
defect detection with coordinate attention and   to handle PCB surface defect characteristics by fusing multi-scale local features.
multi-scale feature fusion. PLoS One 20(6):      This improves spatial dependency capture, detail attention, feature resolution, and
e0323684. https://doi.org/10.1371/journal.
pone.0323684                                     detection accuracy. Additionally, the WIPIoU loss function is developed to calculate
                                                 IoU using auxiliary boundaries and address low-quality data, improving small-target
Editor: Alemayehu Getahun Kumela, Universite
Cote d'Azur, FRANCE                              recognition and accelerating convergence. Experimental results demonstrate signif-
Received: January 21, 2025                       icant improvements in PCB defect detection, with mAP50 increasing by 5.7%, and
                                                 reductions of 13.3% and 14.8% in model parameters and computational complexity,
Accepted: April 12, 2025
                                                 respectively. Compared to mainstream models, PCB-YOLO achieves the best overall
Published: June 2, 2025
                                                 performance. The model’s effectiveness and generalization are further validated on
Copyright: © 2025 Wei et al. This is an open
                                                 the NEU-DET steel surface defect dataset, achieving excellent results. The PCB-
access article distributed under the terms of
the Creative Commons Attribution License,        YOLO model offers a practical, efficient solution for PCB and steel defect detection,
which permits unrestricted use, distribution,    with broad application prospects.
and reproduction in any medium, provided the
original author and source are credited.

Data availability statement: The data under-
lying the results presented in the study are
                                                 Introduction
available from https://osf.io/w6jsc/.            As the basic component of the electronic industry, printed circuit board (PCB) is
Funding: The author(s) received no specific      widely used in all kinds of electronic equipment in life and production [1–4]. The qual-
funding for this work.                           ity of PCB directly affects the performance and life of electronic equipment. There-
                                                 fore, defect detection of PCB is a key and necessary task in electronic manufacturing

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                                                   1 / 29
Competing interests: The authors have         industry. Flying pin testing is an electrical testing method that is mainly used to detect
declared that no competing interests exist.
                                              short and open circuit faults on circuit boards. This method utilizes multiple fast-­
                                              moving electrical probes driven by motors to contact the pins of the circuit board,
                                              thereby making electrical measurements, instead of a conventional needle bed
                                              [5]. As a traditional PCB inspection method, manual inspection relies on the visual
                                              inspection of production line operators, and usually requires the help of magnifying
                                              glass to identify defects on complex circuit boards. As the scale of integrated circuits
                                              increases, so does the complexity of printed circuit boards, which leads to increased
                                              difficulty in contact measurement and manual inspection. Traditional manual detec-
                                              tion methods are costly and inefficient, and are gradually being eliminated. Using
                                              efficient automated defect detection algorithms can not only significantly improve
                                              production efficiency, but also greatly reduce labor costs. In short, the application of
                                              automated defect detection technology not only optimizes the production process, but
                                              also promotes the rational allocation of human resources.
                                                  Before deep learning technology was widely used, PCB defect detection mainly
                                              relied on traditional image processing and machine learning methods. These tra-
                                              ditional methods face some challenges, such as sensitivity to data distribution,
                                              insufficient generalization ability, and inefficient detection. Wang et al. [6] proposed
                                              an on-line PCB defect detection technology based on machine vision, which firstly
                                              preprocesses the image, including operations such as smoothing, contrast enhance-
                                              ment and sharpening, to improve the image quality; Then, the image is processed
                                              and binarized, and the hybrid method of mathematical morphology and pattern
                                              recognition is used for defect recognition and detection; Finally, the reference image
                                              obtained by mathematical morphology method is used as the system self-inspection
                                              template, and the image difference detection algorithm is introduced to segment the
                                              defect image, remove redundant points and mark the recognition results. Yuk et al.
                                              [7] implemented PCB defect detection using accelerated robust features and random
                                              forest algorithms. By considering the density of features, a weighted kernel density
                                              estimation mAP is generated with weighted probability, and the detection of defect
                                              concentration area is realized. Some scholars have also proposed PCB surface
                                              defect detection methods based on machine learning, but this method is not a real-
                                              time method [8,9]. Although machine learning methods can identify defects on PCB
                                              surfaces, many algorithms still rely on manual setting of image features, which usu-
                                              ally needs to be based on prior knowledge. This dependency limits the generalization
                                              ability of the algorithm.
                                                  With the development of deep learning technology [10–16], using deep learning
                                              technology to solve PCB defect detection has gradually become the mainstream
                                              research method [17–19]. Huang et al. [20] improved the YOLOv5s architecture by
                                              introducing deeply separable convolution and spatial attention mechanisms, using
                                              an adaptive spatial feature fusion module, and proposed an SSA-YOLO model,
                                              which effectively solved the conflict information between features in different layers,
                                              enabling the model to better adapt to the detection requirements of complex scenes
                                              and multi-scale targets. Zhang et al. [21] developed a lightweight algorithm YOLO-
                                              RRL based on YOLOv8 architecture for the problems of various types of PCB surface

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                               2 / 29
defect detection and large amount of model calculation, and used RFD method to optimize the downsampling process of
shallow and deep feature mAPs; RepGFPN is used to optimize the feature fusion network to improve the fusion efficiency
of feature mAPs with different scales; Finally, a lightweight asymmetric detection head is used to reduce the amount of
model parameters and calculation while maintaining the detection accuracy. References [22] and [23] apply YOLOv7
model and YOLOv5s model to PCB defect detection respectively, and achieve fast and accurate detection effects by add-
ing convolution layer and upsampling layer, introducing attention mechanism and replacing activation function. In order to
better detect small defects in PCB, Xu et al. [24] added a detection layer and anchor frame dedicated to detecting small
targets to the YOLOv5s model. Inspired by the YOLOX model, a novel decoupling head mechanism was designed to
decouple the three tasks of classification prediction, position prediction and confidence prediction, which accelerated the
convergence speed of the model. The improved model has good adaptability and robustness. Xiao et al. [25] improved the
lightweight YOLOv7-tiny model by introducing coordinate attention mechanism, deep separable convolution and Inner-
CIoU loss function, and constructed an efficient PCB defect detection model CDI-YOLO, which balanced the contradiction
between accuracy, speed and parameter quantity and achieved accurate defect detection. Jiang et al. [26] designed the
DCR-YOLO model by drawing lessons from the overall structure of YOLO series models and the idea of target detection.
The model uses a backbone network composed of double cross residual blocks and ordinary residual blocks, and pro-
poses a PCR module to enhance the feature fusion mechanism between feature layers of different scales. The SSDT-FPN
module and C5ECA module are designed to improve the feature fusion layer and self-made feature weights respectively,
and the average detection accuracy is 98.58%. To sum up, the application of deep learning technology has significantly
improved the efficiency and accuracy of PCB defect detection. Different research teams have proposed a variety of effec-
tive solutions for the particularity of PCB defects by improving and optimizing the existing network architecture.
    In recent years, although deep learning-based PCB defect detection methods have made significant progress, they
still face some challenges in practical applications. Existing methods often perform poorly when dealing with tiny defects
in complex backgrounds, resulting in high missed detection rates. At the same time, many models have deficiencies in
feature extraction and context understanding, limiting their generalization capabilities in diverse PCB scenarios. In addi-
tion, the accuracy of bounding box regression is also a common problem in existing methods, which directly affects the
precise localization of defects. In response to these key issues, we propose an improved PCB-YOLO model, which aims
to fill the shortcomings of existing research. Our model is based on YOLOv8, an efficient and smaller parameter object
detection algorithm suitable for the deployment of industrial inspection equipment. We improve YOLOv8 in the following
three aspects:

(1) To solve the problem of possible loss of feature information in lightweight design, we introduce the CRSCC module,
    which enhances the model’s capabilities in feature extraction and context awareness, enabling the model to better
    understand complex scenes, thus improving the generalization ability of detection.

(2) In view of the characteristics that PCB defects are usually small in size and have complex backgrounds, we design the
    FFCA module, which is a coordinate attention mechanism module that fuses multi-scale local features. By combining
    local and global features and introducing coordinate information, it effectively improves the model’s ability to capture
    the details of PCB surface defects, thereby improving the accuracy of detection.

(3) To improve the regression accuracy of the bounding box, we propose the WIPIoU loss function, which is the advan-
    tage of combining the three loss functions of Wise-IoU, MPDIoU, and Inner-IoU. The WIPIoU loss function not only
    enables the model to locate the target more accurately, but also accelerates the convergence rate of the model.

  Through these improvements, our PCB-YOLO model can handle tiny defects in complex backgrounds more effectively,
improving the accuracy and efficiency of inspection, thus bringing a more efficient and accurate solution to the field of
PCB defect inspection.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                   3 / 29
Materials and methods
Dataset
In this paper, the open source PCB defect dataset PKU-Market-PCB [27] of Peking University Intelligent Robot Open
Laboratory is used, with a total of 673 PCB defect images, some of which are shown in Fig 1. This data set involves
a total of 6 types of defects, including missing hole, mouse bite, open circuit, short circuit, spur, and spurious copper,
including 115 missing holes, 115 mouse bites, 116 open circuits, 116 short circuits, 115 burrs, 116 fake copper. Due to the
limited number of various PCB defect samples in this public data set, and the samples collected in an ideal environment,
it cannot meet the requirements of model training. Therefore, first, the data of the existing samples is enhanced, and the
data set is expanded to 4038 through operations such as rotation, mirroring, noise and brightness adjustment. Some of
the expanded sample images are shown in Fig 2. During the experiment, the data set is randomly divided into training set,
verification set and test set according to the ratio of 7:2:1, that is, 2825 images are used as the training set of the training
model, 808 images are used as the verification set, and 405 images are used as the test set. The final number of each
defect type is shown in the Table 1.

PCB-YOLO model
   In this study, we chose the YOLOv8 model as our benchmark model, and this choice is based on multiple consid-
erations. First, the YOLOv8 model has made significant improvements in architecture and training methods based on
previous YOLO versions. Improved model structure design, enhanced feature extraction techniques, and optimized

Fig 1. Images of different PCB surface defect types.

https://doi.org/10.1371/journal.pone.0323684.g001

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                       4 / 29
Fig 2. Data augmentation example diagram.

https://doi.org/10.1371/journal.pone.0323684.g002

Table 1. PKU-market-PCB dataset defect description and quantity.
Defect Type                 Defect description                               Number of Original   Number of Images After Expansion
                                                                             Images
missing hole                Failure to drill some holes correctly            115                  690
mouse bite                  Circuit board breakage                           115                  690
open circuit                Solder joint interruption                        116                  696
spur                        Excess metal fragments appear                    115                  690
short circuit               Undesirable current path between solder joints   116                  696
spurious copper             Copper foil layer fails to cover correctly       116                  696
Total number                /                                                673                  4038
https://doi.org/10.1371/journal.pone.0323684.t001

training methods are integrated. What really makes the YOLOv8 model stand out is its impressive combination of speed,
accuracy, and efficiency, making it one of the most powerful models ever made by Ultralytics. With an improved design,
YOLOv8 provides better feature extraction, the process of identifying important patterns and details from images, captur-
ing complex aspects more accurately even in challenging scenes. However, the YOLOv8 model has some shortcomings
in practical application. For example, the model has a large amount of parameters, which makes it difficult to deploy on
resource-constrained platforms such as mobile devices.
   This challenge is particularly important for our research, because in practical application scenarios, PCB defect detec-
tion involves real-time processing of multiple frames of images, so in large-scale defect detection tasks, detection speed
is crucial. At the same time, YOLOv8 model. There is still room for improvement in the detection accuracy. Although
the YOLOv8 model performs well in some aspects, it needs further optimization and adjustment, because our goal is to
develop an efficient and practical target detection system.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                         5 / 29
   The backbone part of YOLOv8 is basically the same as that of YOLOv5. Based on the CSP idea, the C3 module is
replaced with the C2f module. The C2f module draws lessons from the ELAN idea in YOLOv7 [28], and combines C3 and
ELAN to form the C2f module, so that YOLOv8 can obtain richer gradient flow information while ensuring lightweight. At
the end of the backbone network, the most popular SPPF module is still used, which ensures the detection accuracy of
objects at different scales. In the neck part, the feature fusion method used by YOLOv8 is PAN-FPN, which strengthens
the fusion and utilization of feature layer information at different scales. The head network generates a detection box by
applying the anchor box to the multi-scale feature mAP of the neck network, which shows the category, location and confi-
dence of the target. The structure of the YOLOv8 model is shown in Fig 3.
   According to different network depth and width, YOLOv8 can be divided into 5 versions: YOLOv8n, YOLOv8s,
YOLOv8m, YOLOv8l, YOLOv8x. Five versions of the YOLOv8 model were used to train the PCB surface defect data set.
The training results are shown in Table 2. The YOLOv8n model has the smallest amount of parameters and calculation,
and the average accuracy is also high. It is suitable for running on devices with limited computing resources and is very
suitable for embedded systems or mobile devices. Based on the consideration of lightweight and the need for accuracy,
this paper selects YOLOv8n as the benchmark model.
   Model lightweight improvement. In the field of PCB defect detection, the identification and location of small targets
has always been a challenging task. Since defects are usually small in size and difficult to distinguish in complex PCB
backgrounds, traditional feature extraction backbone networks based on convolutional neural networks (CNNs) often face
challenges. Since small targets occupy a small proportion of pixels in the original image, they are easily submerged in a
large amount of redundant information during the downsampling process, resulting in degraded detection performance.
Although the structure of C2f module in the backbone network of YOLOv8n model is relatively simple and has good
feature fusion ability, with the complexity of application scenarios, we realize that C2f module has certain limitations in
processing context information. Although the traditional Conv1 and Conv2 layers in C2f can extract features, they often
ignore the spatial context relationship between features, which is especially obvious when dealing with images with
complex backgrounds. SSconv convolution allows the network to not only consider local information when processing
images, but also combine global contextual information, which helps improve the model’s ability to understand complex
scenes and improve the final prediction results.
   Therefore, we propose a brand-new CRSCC module based on SCConv convolution [29] and C2f module to reduce the
redundant information of the feature mAP in both space and channel aspects, enhance the model’s understanding of the
spatial context, and thus improve the quality of feature extraction.
   In the CRSCC module shown in Fig 4, we have taken several improvements to enhance network performance. First,
we optimize the original C2f module and replace two standard convolution operations with the SCConv module. The
purpose of this replacement is to strengthen the ability of the backbone network in spatial context modeling, so that the
network can understand the spatial relationship between features more deeply. In addition, in order to further improve the
performance of the model in feature extraction and context awareness, we added residual connections between SCConv
modules. These residual connections effectively realize the feature fusion between different SCConv modules, and ensure
that the retention and utilization of feature information in the transmission process are more efficient. In this way, the net-
work can better integrate and utilize multi-level feature information, thus improving the overall performance (Fig 5).
   The essence of the CRSCC module lies in its SCConv structure, as shown in Fig 6. This structure consists of two key
components: the Spatial Reconstruction Unit (SRU) and the Channel Reconstruction Unit (CRU), whose detailed struc-
tures are shown in Fig 6, respectively. During the processing, the input feature X is first optimized through SRU, which
improves the efficiency of spatial information processing through the following two main steps.
   The first step is the spatial separation operation, which uses the scaling factor γ in group normalization to evaluate the
information content of different feature mAPs, and then separates the feature mAPs with large information and the feature
mAPs with small information into Xw1 and Xw2 parts. The second step is the spatial reconstruction operation. Through

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                      6 / 29
Fig 3. YOLOv8 model structure.

https://doi.org/10.1371/journal.pone.0323684.g003

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025   7 / 29
Table 2. Training results of different sizes of YOLOv8 on PKU-market-PCB dataset.
Model                        Parameters(MB)              FLOPs (G)              Precision/%   Recall/%   mAP50/%
YOLOv8n                      3.0                         8.1                    85.1          84.6       90.4
YOLOv8s                      11.1                        28.4                   95.4          76.3       91.2
YOLOv8m                      25.8                        78.7                   94.4          89.9       95.5
YOLOv8l                      43.6                        164.8                  90.5          90.1       95.0
YOLOv8x                      68.1                        257.4                  90.1          90.3       95.3
https://doi.org/10.1371/journal.pone.0323684.t002

Fig 4. CRSCC structure diagram.

https://doi.org/10.1371/journal.pone.0323684.g004

Fig 5. SCConv structure diagram.

https://doi.org/10.1371/journal.pone.0323684.g005

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                            8 / 29
Fig 6. (a) SRU structure diagram; (b) CRU structure diagram.

https://doi.org/10.1371/journal.pone.0323684.g006

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025   9 / 29
cross reconstruction, the weighted two different information features are combined to generate features with richer infor-
mation and optimize the space occupation. The reconstruction operation is shown in Equation (1):
                                                             ⊗             ⊗
                                                  ⊕Xw1 = W1
                                                                     w
                                                                 X, X⊕
                                                                     2 = W2    X
                                                       w                 w
                                              Xw11   X22 = Xw1 , Xw
                                                                  21   X12 = Xw2
                                           
                                                                  Xw1 ∪ Xw2 = Xw                                         (1)

Next, the spatially reconstructed feature Xw enters the CRU to optimize the channel information. CRU contains three
steps: segmentation, transformation, and fusion. In the segmentation stage, the feature Xw is divided into two parts Xup
and Xlow with different channel numbers, where αC and (1 – α)C represent their channel numbers respectively, and α
is an adjustable hyperparameter. Subsequently, these two-part features are channel-compressed by a 1 × 1 convolution
kernel.
   In the conversion stage, Xup is the main input of “rich feature extraction”, and the output Y1 is obtained through the com-
bination operation of packet convolution (GWC) and point convolution (PWC), as shown in equation (2). At the same time,
Xlow as supplementary information is only processed by PWC, and its output is combined with the original Xlow to obtain
Y2, as shown in Equation (3).

                                                           Y1 = MG Xup + Mp1 Xup                                           (2)

                                                            Y2 = Mp2 Xlow ∪ Xlow                                           (3)

Finally, in the fusion stage, the global average pooling technique is used to obtain S1 and S2, and the feature weight vec-
tors β1 and β2 are obtained by the Softmax function. These two weight vectors are used to combine Y1 and Y2 to gener-
ate the final channel purification feature Y. In this way, the CRSCC module can not only reduce redundant information, but
also improve the quality of features, which is of great significance for small target detection.
    Fusion multi-scale local feature coordinate attention. PCB defect detection is an important link in electronic
manufacturing industry, which is related to the quality and reliability of electronic products. With the development
of miniaturization and high density of electronic products, the defect detection of PCB has become more and more
challenging. The diversity of defect types, such as short circuit, open circuit, hole, foreign matter, offset, uneven copper
foil thickness, each defect has different characteristics and detection difficulty. The interference of complex background,
complex circuits on PCB and many background noises bring difficulties to defect identification. With the improvement
of technology, the size of some defects is very small, which puts forward higher requirements for the resolution and
sensitivity of the detection system. The balance between detection speed and accuracy requires fast detection speed on
the production line, but at the same time, high accuracy must be ensured, which is a big challenge for detection algorithms
and hardware equipment. Illumination and imaging problems, different lighting conditions may affect the quality of images,
thus affecting the accuracy of defect detection.
    In order to solve the above problems, in recent years, deep learning technology, especially attention mechanism, has
been introduced into PCB defect detection. Attention mechanism can make the model pay more attention to the key areas
related to defects in the image, while ignoring the unimportant background information, thus improving the detection
accuracy. It can adaptively learn the feature representation of defects, especially in complex circuit background. In addi-
tion, the attention mechanism helps the model to focus on small changes in the image, which is particularly effective for
the detection of small defects. By strengthening the model’s attention to defect areas, false detection caused by back-
ground interference can be reduced, and at the same time, the detection ability of small defects can be improved, and
missed detection can be reduced. The attention mechanism also helps the network make more efficient use of computing
resources, and reduces unnecessary calculations by focusing on key areas, thereby improving detection speed.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                    10 / 29
    The coordinate attention (CA) [30] module pools in two different directions, aggregates the input feature mAP infor-
mation horizontally and vertically, and embeds the position information into the channel attention, realizing the interac-
tion of two dimensions. However, the CA module only pays attention to the global position information and long-range
dependency of the corresponding direction, but does not pay attention to the local position information. In order to solve
the above problems, this paper designs the FFCA attention mechanism, and its structure is shown in Fig 7. FFCA mainly
includes three parts: feature grouping, multi-branch features and spatial information aggregation (Fig 8).
    The dimension of the input feature map of the FFCA module is C × H × W , which represents the number of channels,
height and width of the feature map respectively. The feature map is divided into G sub-features according to the number
of channels, and each group is isolated from each other, and subsequent operations are performed separately to learn
different features. G is generally much smaller than C to ensure the generalization ability of each group.
    Multi-branch features use different methods to process the input feature map, from left to right, they are vertical local
features, vertical global features, horizontal global features and horizontal local features respectively. The input feature xn
is denoted as x for convenience of representation. In the horizontal global feature branch, the grouped input feature maps
aggregate features along the horizontal direction to obtain long-range information and retain accurate information in the
vertical direction. Specifically, the input information is pooled using a pooling kernel of size (W, 1)to generate a feature

Fig 7. FFCA attention module structure.

https://doi.org/10.1371/journal.pone.0323684.g007

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                      11 / 29
Fig 8. PCB-YOLO model structure.

https://doi.org/10.1371/journal.pone.0323684.g008

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025   12 / 29
map zHg of size C/G × H × 1, and H, W, g, l in the upper corner indicates horizontal, vertical, global, and local respectively.
The pooled output is expressed as Equation (4), where W represents the width of the feature map and h represents the h
throw of the feature map.
                                                            1 ∑
                                                  zHg (h) =         x(h, i)
                                                            W
                                                              0≤i<W                                                         (4)

Next, keep the number of channels unchanged, use convolution to enhance the feature information, and obtain the final
weight yHg through the Sigmoid activation function, as shown in Equation (5), where σ represents the Sigmoid activation
function, F1×1 represents convolution 1 * 1, and zHg represents the pooled sequence feature. After that, the input features
are adjusted according to the weights to obtain the horizontal global feature YHg , which is expressed as Equation (6), and
Gn represents group normalization:
                                                            (     ( ))
                                                    yHg = σ F1×1 zHg                                                      (5)
                                                                       ((             ))
                                                            YHg = Gn        x × yHg                                            (6)

Similarly, the pooled features in the vertical global feature branch and the vertical global features are expressed as equa-
tions (7), (8), where H represents the height of the feature mAP and w represents the w-th row of the feature mAP.

                                                                       1 ∑
                                                          zWg (h) =        x(i, w)
                                                                       H
                                                                         0≤i<H                                                 (7)
                                                              (     (    (    )))
                                                      YWg = Gn x × σ F1×1 zWg                                                  (8)

In the horizontal local feature branch, multiple 1 × 3 convolutions are used to simulate the effects of 1 × 3, 1 × 5, 1 × 7 convo-
lutions, and fewer parameters are used to simulate multi-scale feature information to obtain the horizontal local feature
YHI . Equation is shown in (9), where Fn1×3 represents n times of 1 × 3 convolutions. Similarly, the vertical local feature is
expressed as equation (10), where Fn3×1 represents n times of 3 × 1 convolution, l represents local, and YHI is a horizontal
local feature. The characteristics of the four branches are denoted by YHg , YWg, YHI , YWI respectively.

                                                 YHl = F31×3 (x) + F21×3 (x) + F11×3 (x) + x                                   (9)

                                                 YWl = F31×3 (x) + F21×3 (x) + F11×3 (x) + x                                 (10)

Spatial information aggregation: After multi-branch processing, global and local information in two directions are obtained,
which are relatively independent. In order to achieve more comprehensive information description, the spatial information
aggregation module is used to promote the interaction between them. In the horizontal branch, the outputs YHg , YHl of the
                                        ′     ′
two branches are globally coded as YHg , YHl by global average pooling.
                                                                             
                                                      ′      1  ∑ ∑
                                                  YHg = S          YHg (j, i)
                                                            W×H
                                                                        0≤j<H 0≤I<W
                                                                                                                              (11)
                                                                                          
                                                      ′          1  ∑ ∑
                                                  YHl = S              YHl (j, i)
                                                                W×H
                                                                       0≤j<H 0≤I<W
                                                                                                                             (12)

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                        13 / 29
The global spatial features of the two branches are multiplied by the matrix dot product operation to generate the first spa-
tial attention mAP. Then, a second spatial attention mAP is generated in the same way, which retains the complete precise
spatial location information. The weights in the horizontal direction are added by the two generated spatial attention
mAPs, and then the input is compressed using the Sigmoid function to obtain the horizontal spatial weight YH , as shown in
Equation (13). In the same way, the vertical space weight YW is obtained.
                                                         (     ′         ′
                                                                            )
                                                 YH = σ YHg YHl + YHl YHg
                                                                                                                          (13)

Finally, the initial feature x is multiplied by the two dimensional weights to obtain the FFCA attention feature X, as shown in
Equation (14).

                                                                 X = YH YW x                                              (14)

    Loss function improvement. The calculation of loss function is an important part of object detection algorithm, and
the prediction box regression loss function of YOLOv8s algorithm defaults to CIoU [31]. CIoU is the calculation of the loss
of the bounding box, mainly considering three important geometric factors: the overlapping area of the predicted box and
the real box, the distance from the center point, and the predicted box and aspect ratio. The specific formula of CIoU is as
follows:
                                                                    (     (            )      )
                                                                        ρ2 Bpred , Bgt
                                                  CIoU = IoU –                           + αv
                                                                             c2
                                                                                                                          (15)
                                                            (                        )
                                                       4           wgt         wpred
                                                    v=       arctan gt – arctan pred
                                                       π           h           h                                          (16)

                                                                           v
                                                              α=
                                                                    (1 – IoU) + v                                         (17)
                                                                                                       (         )
Among them, α is used as a balance parameter, v is used to measure the length and width, and ρ2 Bpred , Bgt represents
the Euclidean distance between the prediction box and the center point of the real box. However, CIoU does not consider
the quality of the labeled examples of the data set itself and ignores the impact of low-quality data on detection perfor-
mance. harm. Therefore, this paper first introduces Wise-IoU [32] as a new bounding box loss function.
   β is used to denote the anomaly degree of the prediction box, which is defined as follows:
                                                                   L∗IoU
                                                             β=          ∈ [0, +∞)
                                                                   LIoU                                                   (18)

Where L∗IoU is the constant converted from the variable LIoU , LIoU is the running average of the momentum m, and the
calculation formula of m is:
                                                               √
                                                               tn
                                                        m = 0.05                                                      (19)

Where t is the Epoch value; n is the value of Batch Size.
 Wise-IoU is defined as:

                                                                         β
                                                          LWIoU =               RWIoU LIoU
                                                                       δα1β–δ                                             (20)

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                     14 / 29
                                                                  (                                  )
                                                                                2                2
                                                                       (x – xgt ) + (y – ygt )
                                                  RWIoU = exp               (           )∗
                                                                              W2g + H2g                                       (21)

                                                                LIoU = 1 – IoU                                                (22)

Among them, (x, y) and (xgt , ygt ) are coordinates of the center points of the prediction frame and the target frame respec-
tively; Wg and Hg are the dimensions of the smallest bounding box; IoU is the cross-to-merge ratio, which is a commonly
used quantity to measure the degree of overlap between the predicted frame and the real frame. α1 and δ are learning
parameters. Wise-IoU reduces the detrimental gradients of low-quality data, thereby improving the overall performance of
the model.
   But Wise-IoU is not aware of the limitations of IoU itself. Inner-IoU [33] proposes to calculate IoU with an auxiliary
border to improve the generalization ability. The specific calculation process is shown in equations (23) and (24), and the
scale factor ratio is used to control the size of the auxiliary bounding box.

                                                              w × ratio             w × ratio
                                                  bl = xc –             , br = xc –
                                                                 2                     2                                      (23)

                                                              h × ratio             h × ratio
                                                  bt = yc –             , bb = yc –
                                                                 2                     2                                      (24)

Through the above two equations, the center point of the detection frame can be transformed to obtain the corner vertices
of the auxiliary detection frame. Both the prediction box and the real box output by the model are transformed accordingly,
and the calculation results of the real box and the prediction box are represented by bgt and bpred respectively.
                                    (    (        )     (        )) (     (       )      (       ))
                            Sinter = min bgt               gt
                                            r , br – max bl , bl   × min bgt                gt
                                                                            b , bb – max bt , bt
                                                                                                                       (25)
                                                (         )
                                        Sunion = wgt × hgt × (ratio)2 + (w × h)(ratio)2 – Sinter                              (26)

                                                                              Sinter
                                                               IoUinner =
                                                                              Sunion                                          (27)

According to the above three formulas, it can be seen that Inner-IoU actually calculates the IoU between the auxiliary
borders. When ratio = 1, the Inner-IoU loss function is actually the IoU loss function. Since the PCB defect detection task
images are all small targets, the IoU will decrease if the labeling box is slightly offset. When ratio > 1, the auxiliary border is
larger than the actual border, which is helpful for sample regression with low IoU. Therefore, for small target detection, the
value of ratio should be greater than 1.
   MPDIoU is an improved regression loss function that can minimize the distance between the upper left corner and the
lower right corner of the prediction box and the real box [34]. It can well deal with the overlap of bounding boxes, has a
good effect on complex multi-objective scenes, and can improve the convergence speed.
                                                                   (            )            (            )
                                                                 ρ2 Ppred
                                                                     1    , Pgt
                                                                             1             ρ2 Ppred
                                                                                               2    , Pgt
                                                                                                       2
                                           MPDIoU = IoU –                              –
                                                                       w2 + h2                w2 + h 2                        (28)

Among them, Ppred
               1   , Ppred
                      2    , Pgt     gt
                              1 and P2 refer
                                           ( to the points
                                                        ) in the upper left corner and the lower right corner of the prediction
                                                     gt
box and the real box respectively, and ρ2 Ppred
                                              1   , P1 calculates the distance between the corresponding points.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                         15 / 29
   Combining inner-IoU and MPDIoU, Inner-MPDIoU is obtained, as shown in equation (29), which can not only calculate
IoU through the auxiliary border, improve the generalization ability, but also solve the overlapping problem of bounding
boxes in complex multi-objective scenes.
                                                              (             )       (              )
                                                                         gt                     gt
                                                            ρ2 Ppred
                                                                 1    , P1      ρ 2
                                                                                      P pred
                                                                                        2    , P2
                                   MPDIoUinner = IoUinner –                   –
                                                               w2 + h2              w2 + h 2                             (29)
On the basis of obtaining inner-MPDIoU, combining Wise-IoU can reduce the harm of low-quality data to detection perfor-
mance. At the same time, replacing the IoU calculation part of Wise-IoU with the obtained inner-MPDIoU, IoU can be calculated
through the auxiliary border, solving the limitation of IoU itself, improving the generalization ability of the model, and finally
obtaining the improved loss function WIPIoU, that is, equation (30), which can effectively improve the model detection effect.
                                      (                           )                       (              )       (              )
                                                                                               pred    gt             pred    gt
                          β
                                                  2
                                        (x – xgt ) + (y – ygt )
                                                                2                      ρ 2
                                                                                             P 1    , P1      ρ 2
                                                                                                                    P 2    , P2
             LWIPIoU =         × exp         (            )∗         × 1 – IoUinner +                      +                     
                          β–δ
                        δα1                    Wg + H g
                                                  2     2                                  w  2 + h2              w  2 + h2
                                                                                                                                    (30)

   Overall network architecture. As shown in Fig 9, the PCB-YOLO model consists of three parts: the backbone
network, the neck network and the head. The trunk part is responsible for extracting feature information and generating
multi-scale features. A novel CRSCC module based on SCConv convolution and C2f is proposed, which significantly
reduces the number of parameters of the model through spatial and channel feature purification, while improving
the accuracy of PCB defect detection, effectively solving the problem of bulky model volume; According to the
characteristics of PCB surface defects, the FFCA attention module is designed. By fusing multi-scale local features, it
can capture remote spatial dependence and multi-scale accurate local position information, enhance detail attention,
and improve the resolution ability and detection effect of features; The WIPIoU loss function is designed, and the IoU
is calculated by auxiliary boundary, and the influence of low-quality data is considered, which improves the recognition
accuracy of the model for small targets and accelerates the convergence speed of the model.

Results and analysis
Experiment environment
The operating system version used in this experiment is Ubuntu 18.04.5 LTS, the CPU is AMD Ryzen 5900HX processor,
the GPU is NVIDIA GeForce RTX 3090 (24GB), the CUDA version is 11.7, the deep learning framework is Pytorch 1.13.1,
and the compilation environment is Python 3.9. Model The detailed parameters for training are shown in Table 3.

Evaluation metrics
  A total of five evaluation metrics are employed in order to provide a comprehensive assessment of the detection model.
These include precision, recall, parameter count, computational complexity, and mean average precision (mAP). The
equations for these metrics are as follows:
                                                                          TP
                                                                P=
                                                                        TP + FP                                                    (31)
                                                                          TP
                                                                R=
                                                                        TP + FN                                                    (32)
                                                                       ∫ 1
                                                              P=             P(R)dR
                                                                        0                                                          (33)
                                                                             ∑1
                                                                              0 AP1
                                                              mAP =
                                                                               n                                                   (34)

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                             16 / 29
Fig 9. Confusion matrix.

https://doi.org/10.1371/journal.pone.0323684.g009

Table 3. Model training parameters.
Hyperparameters                                                        Value
Initial learning rate                                                  0.01
Optimizer                                                              SGD
Optimizer momentum                                                     0.937
Optimizer weight decay rate                                            0.0005
Batchsize                                                              16
Epoch                                                                  300
https://doi.org/10.1371/journal.pone.0323684.t003

TP represents the number of positive samples correctly predicted as positive by the model, FP represents the number
of negative samples incorrectly predicted as positive by the model, and FN represents the number of positive samples
incorrectly predicted as negative by the model. AP represents the area under the Precision-Recall (P-R) curve, while mAP
denotes the average of AP for each category.

Analysis of the impact of CRSCC modules in different positions on model performance
   In order to determine where the CRSCC module is added in the backbone network of YOLOv8n model to have the best
comprehensive improvement effect on each index, experiments are carried out for the following four situations. Although
the improved CRSCC module has stronger feature extraction ability and lower parameter quantity in theory, because the
improvement is carried out for C2f in the deep backbone network, there is uncertainty whether any improvement of C2f
can achieve performance improvement. Therefore, a set of comparative experiments are carried out to improve CRSCC
modules in different locations. Backbone 3_5_7_9 means to improve the C2f modules of layers 3, 5, 7 and 9 in the
backbone network, Backbone 5_7_9 means to improve the C2f modules of layers 5, 7 and 9 in the backbone network,
Backbone 7_9 means to improve the C2f modules of layers 7 and 9 in the backbone network, and Backbone9 means
to improve only the deepest C2f modules in the backbone network. The experimental results are shown in Table 4. The

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                               17 / 29
Table 4. Comparison of CRSCC module improvement in different locations.
Model                                     Parameters(MB)                 Precision/%               Recall/%    mAP50/%
YOLOv8n                                   3.0                            94.5                      88.9        95.7
Backbone3_5_7_9                           2.2                            93.6                      89.3        94.9
Backbone5_7_9                             2.3                            93.7                      89.9        96.1
Backbone7_9                               2.6                            93.3                      91.4        96.3
Backbone9                                 2.9                            94.0                      88.7        95.6
https://doi.org/10.1371/journal.pone.0323684.t004

experimental results show that although CRSCC module has lower parameters and stronger ability to extract features
than C2f in theory, the more improved modules, the better. The model has the best performance when the improvement
module acts on the deeper network.
   Attention mechanism contrast test. In order to verify the superiority of the FFCA attention mechanism proposed in
this paper, we use very popular attention modules for comparative experiments, such as SE [35], GAM [36], SimAM [37],
CBAM [38], ECA [39], EMA [40] and CA.
   The experimental results are shown in Table 5. It can be seen from Table 5 that most attention modules have a posi-
tive effect on the model after being added, and only SE attention module and GAM attention module will have a negative
impact on the model. Adding FFCA module to the model improves the detection effect greatly, which proves the effective-
ness and practicability of FFCA attention module.
   Analysis of the influence of WIPIoU loss function on model performance. In this chapter, we conduct quantitative
comparison experiments on several loss functions: CIoU, GIoU [41], SIoU [42], ShapeIoU [43], Inner-IoU, DIoU and
WIPIoU. The experimental results are shown in Table 6. By comparing the experimental results, we find that the model

Table 5. Analysis of influence of different attention modules on model performance.
Model                                               Precision/%                        Recall/%                mAP50/%
YOLOv8n                                             94.5                               88.9                    95.7
YOLOv8n+SE                                          92.7                               89.2                    94.3
YOLOv8n+GAM                                         94.1                               86.9                    95.3
YOLOv8n+SimAM                                       94.7                               87.8                    96.7
YOLOv8n+CBAM                                        95.0                               87.1                    97.1
YOLOv8n+ECA                                         94.5                               88.4                    96.3
YOLOv8n+EMA                                         93.0                               87.6                    97.4
YOLOv8n+CA                                          94.8                               88.5                    97.7
YOLOv8n+FFCA                                        95.3                               89.1                    98.4
https://doi.org/10.1371/journal.pone.0323684.t005

Table 6. Analysis of the impact of loss function on model performance.
Model                                                 Precision/%                       Recall/%               mAP50/%
YOLOv8n                                               94.5                              88.9                   95.7
YOLOv8n+Inner-IoU                                     94.3                              88.2                   95.8
YOLOv8n+GIoU                                          94.8                              89.0                   95.5
YOLOv8n+SIoU                                          94.7                              88.2                   95.5
YOLOv8n+Shape-IoU                                     94.9                              88.8                   96.0
YOLOv8n+DIoU                                          93.3                              89.1                   94.9
YOLOv8n+WIPIoU                                        95.1                              89.3                   96.2
https://doi.org/10.1371/journal.pone.0323684.t006

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                              18 / 29
accuracy, recall rate and mAP50 using the WIPIoU loss function are better than other loss functions. The accuracy of
the model using WIPIoU loss function is significantly improved, which shows that the model reduces misjudgment when
identifying defects and improves the detection accuracy. The performance of the WIPIoU loss function in recall rate is
also excellent, indicating that the model can effectively identify more real defects and reduce missed detection, which is
particularly important for PCB surface defect detection in practical applications.
   PCB-YOLO model performance analysis. We further evaluate the detection ability of the trained model through the
confusion matrix. The confusion matrix is shown in Fig 9. From the confusion matrix, it can be seen that the improved
model can reflect higher classification accuracy in the identification of various defects on the PCB surface, and the
classification performance is more balanced. The background false judgment rate of PCB surface defects is high, which
shows that the complex environment will interfere with the recognition of detection targets by the model, and there is still
the problem of missed detection of PCB surface defects, which may be due to the complexity of the environment that
makes the characteristics of tiny defects difficult to identify and capture.
   The relationship between training loss and verification loss is an important indicator to measure model performance. In
order to clearly describe the changing trend of loss function during model iteration, we draw a comparison of training loss
and verification loss curves of YOLOv8n and PCB-YOLO models, as shown in Fig 10.
   From the analysis of Fig 10, it can be seen that the training loss and verification loss of our proposed PCB-YOLO
model both decrease slowly at the same time and tend to a specific threshold, with little difference, and both of them are
lower than the YOLOv8n model, which shows that the WIPIoU algorithm can more accurately transmit the error back
along the gradient minimum path direction, and update the weight value to speed up the convergence speed and improve
the detection accuracy.
   Ablation experiment. In order to intuitively demonstrate the performance of the improved method in PCB defect
detection, a series of ablation experiments are designed with YOLOv8n model as the benchmark model, which is verified

Fig 10. Training loss and validation loss.

https://doi.org/10.1371/journal.pone.0323684.g010

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                   19 / 29
Table 7. Ablation experiment.
CRSCC              FFCA              WIPIoU         Parameters(MB)     FLOPs (G)   Precision/%     Recall/%       mAP50/%
                                                    3.0                8.1         94.5            88.9           95.7
√                                                   2.6                6.9         94.9            88.4           96.3(+0.6)
√                  √                                2.6                6.9         95.3            89.1           98.4(+2.7)
√                  √                 √              2.6                6.9         95.2            89.7           98.8(+3.1)
https://doi.org/10.1371/journal.pone.0323684.t007

by one-by-one ablation, in which “√” indicates joining the module, the experimental results are shown in Table 7, and the
bold part indicates the optimal value.
    It can be seen from Table 7 that after first replacing the C2f module in the backbone network with CRSCC module, the
mAP50 value increases by 2.5%, indicating that CRSCC module can effectively improve the model feature fusion ability
and the global feature information extraction ability of defect feature image; Then, after adding the FFCA attention mod-
ule to the feature fusion network part, mAP50 increased by 2.2%, indicating that our proposed FFCA module enables
the network to better utilize low-level and high-level features, improve the accuracy and robustness of detection, and
improve the detection effect of small targets; Finally, the CIoU loss function is replaced by the WIPIoU loss function, and
the mAP value is increased by 0.4%, which shows that the improved loss function can effectively improve the robustness
of the model. The results of ablation experiments show that the improvements made to YOLOv8n model in this paper can
improve its detection accuracy, which shows the rationality and effectiveness of PCB-YOLO algorithm. To sum up, the
various improved methods proposed in this paper have positive effects on PCB surface defect detection.
    Comparative analysis with other models. In order to verify the performance of the improved model in PCB surface
defect detection tasks more deeply, the improved model is compared with the mainstream target detection models,
including Faster-RCNN [44], SSD [45], Rtdetr-l [46], YOLOv7-tiny, YOLOv8n, YOLOv10n [47], and YOLO11n models, and
other state-of-the-art methods such as YOLOv5-SSCD [48], Improved-YOLOv5s [49], CDS-YOLO [50], CGS-YOLOv5
[51], YOLO-HMC [52], YOLO-World [53], Mask DINO [54], EffNet-YOLO [55], YOLOv8-PCB [56], MS-DETR [57]. Table
8 gives a comparative analysis of our proposed method and the above method on a series of indicators, including
parameter quantity, calculation quantity, accuracy, recall rate and average accuracy mean, where bold indicates the
optimal value.
    It can be seen from Table 8 that the Faster-RCNN model is the largest and has the largest number of parameters, but
the average accuracy is the lowest, and the detection effect is poor; The Rtdeter-l model is to improve the model with the
best detection effect, but it has the highest amount of calculation and cannot exert full performance on devices with low
computing power; The parameters of YOLOv5n model and YOLO11n model are the smallest, both are 2.5, but the detec-
tion results are average; Comparing PCB-YOLO with the current SOTA method, YOLOv5-SSCD, Improved-YOLOv5s,
CDS-YOLO, and CGS-YOLOv5 models have larger sizes but lower accuracy; YOLO-World and Mask DINO have the low-
est detection accuracy when there are many parameters, while CGS-YOLOv5 has lower detection accuracy; YOLO-HMC
has high detection accuracy with good model size control; The EffNet-PCB model has a larger size and slightly lower
accuracy; The YOLOv8-PCB model has the fewest parameters, but slightly lower detection accuracy; Although PCB-
YOLO has a lower detection speed than MS-DETR, MS-DETR has a larger number of parameters and calculations, and
its detection accuracy is not high; The PCB-YOLO model proposed in this paper shows the strongest performance, with
an average accuracy of 98.8, which is 3.1 percentage points higher than the benchmark model. In terms of parameters, it
meets the requirements of lightweight, and at the same time, it can be easily run on equipment with low computing power.
The experimental results clearly show that our method is superior to other methods in overall performance.
    Visualization experiments. In order to visually demonstrate the advantages of this algorithm in detection
performance, we use the PCB-YOLO model and several other different detection algorithms to conduct comparative

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                 20 / 29
Table 8. PCB-YOLO compared with other different models.
                                      Model              FLOPs(G)      Parameters(MB)   Precision/%   Recall/%   mAP50/%    FPS
Advanced two-stage methods            Faster R-CNN       136.8         /                93.3          81.1       88.3       17.4
Advanced one-stage methods            SSD                12.3          38.8             92.0          89.7       93.4       22.1
                                      Rtdetr-l           32.0          103.5            95.2          97.1       97.3       19.7
                                      YOLOv7-tiny        13.9          6.2              92.9          94.1       94.6       62.5
                                      YOLOv8n            3.0           8.1              94.5          88.9       95.7       94.3
                                      YOLOv10n           2.6           8.2              93.0          94.9       95.1       73.6
                                      YOLO11n            2.5           6.3              91.6          95.2       94.4       75.5
Current SOTA methods                  YOLOv5-SSCD        25.4          /                96.3          89.1       94.5       /
                                      Improved-YOLOv5s   16.4          46.6             /             97.2       96.1       /
                                      CDS-YOLO           13.5          /                97.4          92.9       95.3       /
                                      YOLO-World         13.38         38.4             84.7          80.4       83.6       44.1
                                      Mask DINO          223           1326             82.1          77.3       81.0       9.2
                                      CGS-YOLOv5         /             8.2              /             /          95.4       /
                                      YOLO-HMC           /             5.94             /             /          98.6       /
                                      EffNet-PCB         22.2          12.6             96.2          96.1       95.6       /
                                      YOLOv8-PCB         7.1           5.2              94.7          94.0       96.1       /
                                      MS-DETR            45.6          14.0             /             /          96.9       115
Proposed                              PCD-YOLO           2.6           6.9              96.3          97.9       98.8       102.8
https://doi.org/10.1371/journal.pone.0323684.t008

Fig 11. Missing hole S defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g011

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                       21 / 29
Fig 12. Short defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g012

experiments on PCB surface defect datasets, and different types of defect types are labeled by different color borders.
The experimental results are shown in Figs 11–16. It can be seen from the figure that in some defect detection with
obvious features, all algorithms can detect defects, but when the defect features are not obvious, most models have
serious false detection and missed detection. In contrast, our algorithm performs better at identifying PCB surface defects.
We can see that this algorithm has made significant progress in the detection of spur and spurious copper defects. This
is also clearly reflected in the visualization results. Especially in the aspect of difficult detection defects, other algorithms
generally have a high missed detection rate, but our algorithm can accurately mark multiple defects, which shows that

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                       22 / 29
Fig 13. Open circuit defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g013

the optimized algorithm has stronger ability in shallow feature extraction and fusion, and effectively reduces the missed
detection phenomenon, especially in the detection of small target defects.
   Model generalization verification. In order to further verify the effectiveness and generality of the algorithm, in
addition to validating it on the PCB surface defect dataset, the NEU-DET steel surface defect dataset provided by
Northeastern University was also used for validation. This dataset contains a total of 1800 images with a size of 200 × 200
pixels, covering six types of defects: silver lines, inclusions, patches, rough surfaces, scratches, and dents. Each type of
defect has 300 images. The dataset is divided into a training set, a validation set, and a testing set in a ratio of 6:2:2, with
1080 images in the training set, 360 images in the validation set, and 360 images in the testing set. Compared PCB-
YOLO, YOLOv8n, MD-YOLO [58], Mask-DINO, YOLO -World, DF-YOLOv7 [59], BiCCFM [60],GLF-NET [61].
   The experimental results are shown in Table 9. Compared with YOLOv8n, the average accuracy of PCB-YOLO is
improved by 5.7%, the amount of parameters is reduced by 13.3%, and the amount of calculation is reduced by 14.8%;
Compared with the improved version of YOLOv5, the average accuracy of MD-YOLO is increased by 1 percentage point;
Compared to Mask DINO, PCB-YOLO significantly improved the mean average precision by 17.4%, while reducing the
number of parameters by 98.8% and computational load by 99.5%. Compared to YOLO-World, PCB-YOLO improved
the mean average precision by 12.9%, reduced the number of parameters by 80.6%, and decreased the computational
load by 82.0%. Compared with the DF-YOLOv7 model, the average accuracy of PCB-YOLO has been improved by 2.1
percentage points, and the computational load has been slightly reduced by 4.5 G FLOP; Compared with BiCCFM, PCB-
YOLO improved the average accuracy by 5 percentage points using approximately the same number of parameters and
less than half of the FLOP calculation; GLF-NET achieves the same average accuracy as our proposed PCB-YOLO, but

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                       23 / 29
Fig 14. Mouse bite defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g014

the computational complexity and model complexity are relatively high. The experimental results demonstrate that the
improved model has enhanced accuracy, proving the greater potential of the proposed model in industrial applications.
Furthermore, the algorithm exhibits significant advantages in terms of parameter count and computational efficiency, fur-
ther validating its strong generalization performance across different datasets.

Conclusions
In this paper, a PCB-YOLO model based on YOLOv8 framework is proposed to solve the problems of low detection
accuracy and low detection efficiency in PCB surface defect detection. First of all, aiming at the problem that the existing

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                    24 / 29
Fig 15. Spur defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g015

PCB surface defect detection model has a large number of parameters and is not easy to deploy on edge devices, we
propose a CRSCC module to replace the C2f module of the feature extraction part. Through feature purification in space
and channels, the redundant information of the feature mAP50 improves the quality of the feature. The purified feature
mAP50 contains richer information, which helps the model better identify the target, improve the detection ability of the
model pair, and reduce the amount of model parameters and calculations; Then, aiming at the problem that there are
many small target defects on the PCB surface, we propose a brand-new coordinate attention mechanism MLFCA that
fuses multi-scale local features. This module can simultaneously capture remote spatial dependencies and multi-scale
accurate local position information, enhance the attention to details, effectively solve the problem of position information

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                    25 / 29
Fig 16. Spurious copper defect detection diagram.

https://doi.org/10.1371/journal.pone.0323684.g016

Table 9. Comparative experiment of model generalization.
Model                         Parameters(MB)              FLOPs (G)      Precision/%             Recall/%             mAP50/%
YOLOv8n                       3.0                         8.1            73.3                    67.9                 73.7
MD-YOLO                       9.0                         14.1           72.5                    72.9                 78.2
Mask DINO                     223                         1326           64.3                    59.8                 61.8
YOLO-World                    13.38                       38.4           70.1                    64.4                 66.3
DF-YOLOv7                     /                           12.4           /                       /                    77.1
BiCCFM                        12.2                        33.2           /                       /                    74.2
GLF-NET                       12.0                        34.6           /                       /                    79.2
PCB-YOLO                      2.6                         6.9            78.3                    70.7                 79.2
https://doi.org/10.1371/journal.pone.0323684.t009

loss in traditional global pooling, and improve the feature resolution ability and detection effect; Finally, we use the WIPIoU
loss function instead of the CIoU function. WIPIoU calculates IoU through the auxiliary border and considers the influence
of low-­quality data, which effectively improves the model’s recognition accuracy of small targets. In addition, WIPIoU com-
bines the advantages of Inner-IoU and MPDIoU. It improves the generalization ability of the model and accelerates the
convergence speed of the model.
   Experiments were conducted on the public data set PKU-Market-PCB. The experimental results show that the PCB-
YOLO model has greatly improved the PCB surface defect task compared with the benchmark model. It is worth noting
that mAP50 has improved by 5.7%, and The amount of model parameters and calculations were reduced by 13.3%

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                     26 / 29
and 14.8% respectively. The mAP50 value is 8.5%, 5.1%, 7.5% and 5.8% higher than that of YOLOv7-tiny, YOLOv8n,
YOLOv10n and YOLO11n, respectively. Taken together, our model has the best overall performance. Despite this, the
PCB-YOLO model still has room for improvement in detection accuracy. In the future, we will further study and explore
other improvement methods, such as introducing more advanced attention mechanisms, data enhancement technologies,
etc., to further improve the detection accuracy and robustness of the model.

Author contributions
Conceptualization: Ze Wei.
Data curation: Fan Yang.
Formal analysis: Kezhen Zhong.
Funding acquisition: Kezhen Zhong.
Investigation: Linkun Yao.
Methodology: Ze Wei.
Project administration: Kezhen Zhong.
Resources: Kezhen Zhong.
Software: Ze Wei.
Supervision: Kezhen Zhong.
Validation: Ze Wei.
Visualization: Fan Yang.
Writing – original draft: Ze Wei.
Writing – review & editing: Fan Yang.

References
 1.   Zhou Y, Yuan M, Zhang J, Ding G, Qin S. Review of vision-based defect detection research and its perspectives for printed circuit board. J Manuf
      Syst. 2023;70:557–78. https://doi.org/10.1016/j.jmsy.2023.08.019
 2.   Zhao W, Xu J, Fei W, Liu Z, He W, Li G. The reuse of electronic components from waste printed circuit boards: a critical review. Environ Sci: Adv.
      2023;2(2):196–214. https://doi.org/10.1039/d2va00266c
 3.   Priyan MV, Annadurai R, Onyelowe KC, Alaneme GU, Giri NC. Recycling and sustainable applications of waste printed circuit board in concrete
      application and validation using response surface methodology. Sci Rep. 2023;13(1):16509. https://doi.org/10.1038/s41598-023-43919-9 PMID:
      37783749
 4.   Niu B, Shanshan E, Xu Z, Guo J. How to efficient and high-value recycling of electronic components mounted on waste printed circuit boards:
      Recent progress, challenge, and future perspectives. J Clean Product. 2023;415:137815. https://doi.org/10.1016/j.jclepro.2023.137815
 5.   Gaidhane VH, Hote YV, Singh V. An efficient similarity measure approach for PCB surface defect detection. Pattern Anal Applic. 2017;21(1):277–
      89. https://doi.org/10.1007/s10044-017-0640-9
 6.   Wang W-C, Chen S-L, Chen L-B, Chang W-J. A machine vision based automatic optical inspection system for measuring drilling quality of printed
      circuit boards. IEEE Access. 2017;5:10817–33. https://doi.org/10.1109/access.2016.2631658
 7.   Yuk EH, Park SH, Park C-S, Baek J-G. Feature-learning-based printed circuit board inspection via speeded-up robust features and random forest.
      Appl Sci. 2018;8(6):932. https://doi.org/10.3390/app8060932
 8.   Tsai D, Hsieh Y. Machine vision-based positioning and inspection using expectation–maximization technique. IEEE Trans Instrum Meas.
      2017;66(11):2858–68. https://doi.org/10.1109/tim.2017.2717284
 9.   Liu Z, Qu B. Machine vision based online detection of PCB defect. Microprocess Microsyst. 2021;82:103807. https://doi.org/10.1016/j.
      micpro.2020.103807
10.   Zhang Z, Lu Y, Zhao Y, Pan Q, Jin K, Xu G, et al. TS-YOLO: an all-day and lightweight tea canopy shoots detection model. Agronomy.
      2023;13(5):1411. https://doi.org/10.3390/agronomy13051411
11.   Zhang T, Zhou J, Liu W, Yue R, Yao M, Shi J, et al. Seedling-YOLO: high-efficiency target detection algorithm for field broccoli seedling transplant-
      ing quality based on YOLOv7-tiny. Agronomy. 2024;14(5):931. https://doi.org/10.3390/agronomy14050931

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                                                 27 / 29
12.   Ma J, Zhao Y, Fan W, Liu J. An improved YOLOv8 Model for lotus seedpod instance segmentation in the lotus pond environment. Agronomy.
      2024;14(6):1325. https://doi.org/10.3390/agronomy14061325
13.   Zhang Q, Chen Q, Xu W, Xu L, Lu E. Prediction of feed quantity for wheat combine harvester based on improved YOLOv5s and weight of single
      wheat plant without stubble. Agriculture. 2024;14(8):1251. https://doi.org/10.3390/agriculture14081251
14.   Ma Z, Yang S, Li J, Qi J. Research on SLAM localization algorithm for orchard dynamic vision based on YOLOD-SLAM2. Agriculture.
      2024;14(9):1622. https://doi.org/10.3390/agriculture14091622
15.   Jiang L, Wang Y, Wu C, Wu H. Fruit distribution density estimation in YOLO-detected strawberry images: a kernel density and nearest neighbor
      analysis approach. Agriculture. 2024;14(10):1848. https://doi.org/10.3390/agriculture14101848
16.   Hao S, Li X, Peng W. Yolo-CXR: a novel detection network for locating multiple small lesions in chest X-ray images. IEEE Access. 2024.
17.   Chen B, Wei M, Liu J, Li H, Dai C, Liu J, et al. EFS-YOLO: a lightweight network based on steel strip surface defect detection. Meas Sci Technol.
      2024;35(11):116003. https://doi.org/10.1088/1361-6501/ad66fe
18.   Liu Z, Lyu W, Wang C, Guo Q, Zhou D, Xu W. D-CenterNet: an anchor-free detector with knowledge distillation for industrial defect detection. IEEE
      Trans Instrum Meas. 2022;71:1–12. https://doi.org/10.1109/tim.2022.3204332
19.   Huang X, Li Y, Bao Y. Adaptive cross transformer with contrastive learning for surface defect detection. IEEE Trans Instrum Meas. 2024.
20.   Huang X, Zhu J, Huo Y. SSA-YOLO: an improved yolo for hot-rolled strip steel surface defect detection. IEEE Trans Instrum Meas. 2024.
21.   Zhang T, Zhang J, Pan P, Zhang X. YOLO-RRL: a lightweight algorithm for PCB surface defect detection. Appl Sci. 2024;14(17):7460. https://doi.
      org/10.3390/app14177460
22.   Yang Y, Kang H. An enhanced detection method of PCB defect based on improved YOLOv7. Electronics. 2023;12(9):2120. https://doi.org/10.3390/
      electronics12092120
23.   Du B, Wan F, Lei G, Xu L, Xu C, Xiong Y. YOLO-MBBi: PCB surface defect detection method based on enhanced YOLOv5. Electronics.
      2023;12(13):2821. https://doi.org/10.3390/electronics12132821
24.   Xu H. FCD-YOLO: improved YOLOv5 based on decoupled head and attention mechanism for defect detection on printed circuit board. In: 2022
      2nd International Conference on Networking Systems of AI (INSAI). IEEE. 2022. 7–11.
25.   Xiao G, Hou S, Zhou H. PCB defect detection algorithm based on CDI-YOLO. Sci Rep. 2024;14(1):7351. https://doi.org/10.1038/s41598-024-
      57491-3 PMID: 38548814
26.   Jiang Y, Cai M, Zhang D. Lightweight network DCR-YOLO for surface defect detection on printed circuit boards. Sensors (Basel).
      2023;23(17):7310. https://doi.org/10.3390/s23177310 PMID: 37687766
27.   Huang W, Wei P. A PCB dataset for defects detection and classification. arXiv. 2019;1901.08204.
28.   Wang C, Bochkovskiy A, Liao H. YOLOv7: trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. In: Proceedings of the
      IEEE/CVF Conf Comput Vis Pattern Recognit. 7464–75.
29.   Li J, Wen Y, He L. SCConv: spatial and channel reconstruction convolution for feature redundancy. In: 2023 IEEE/CVF Conference on Computer
      Vision and Pattern Recognition (CVPR). IEEE. 2023. 6153–62. https://doi.org/10.1109/cvpr52729.2023.00596
30.   Hou Q, Zhou D, Feng J. Coordinate attention for efficient mobile network design. In: Proceedings of the IEEE/CVF Conf Comput Vis Pattern Rec-
      ognit. 2021. 13713–22.
31.   Zheng Z, Wang P, Liu W, Li J, Ye R, Ren D. Distance-IoU Loss: faster and better learning for bounding box regression. AAAI. 2020;34(07):12993–
      3000. https://doi.org/10.1609/aaai.v34i07.6999
32.   Tong Z, Chen Y, Xu Z. Wise-IoU: bounding box regression loss with dynamic focusing mechanism. arXiv. 2023;2301.10051.
33.   Zhang H, Xu C, Zhang S. Inner-IoU: more effective intersection over union loss with auxiliary bounding box. arXiv. 2023;2311.02877.
34.   Ma S, Xu Y. Mpdiou: a loss for efficient and accurate bounding box regression. arXiv. 2023;2307.07662.
35.   Hu J, Shen L, Sun G. Squeeze-and-excitation networks. In: Proc IEEE Conf Comput Vis Pattern Recognit. 2018. 7132–41.
36.   Liu Y, Shao Z, Hoffmann N. Global attention mechanism: retain information to enhance channel-spatial interactions. arXiv. 2021;2112.05561.
37.   Yang L, Zhang R, Li L. Simam: a simple, parameter-free attention module for convolutional neural networks. In: Int Conf Mach Learn. PMLR.
      11863–74.
38.   Woo S, Park J, Lee JY. Cbam: convolutional block attention module. In: Proceedings of the European Conf Comput Vis (ECCV). 2018. 3–19.
39.   Wang Q, Wu B, Zhu P. ECA-Net: efficient channel attention for deep convolutional neural networks. In: Proceedings of the IEEE/CVF Conference
      on Computer Vision and Pattern Recognition. 2020. 11534–42.
40.   Li X, Zhong Z, Wu J. Expectation-maximization attention networks for semantic segmentation. In: Proceedings of the IEEE/CVF International Con-
      ference on Computer Vision. 2019. 9167–76.
41.   Rezatofighi H, Tsoi N, Gwak J. Generalized intersection over union: a metric and a loss for bounding box regression. In: Proceedings of the IEEE/
      CVF Conference on Computer Vision and Pattern Recognition. 2019. 658–66.
42.   Gevorgyan Z. Siou loss: more powerful learning for bounding box regression. arXiv. 2022;2205.12740.
43.   Zhang H, Zhang S. Shape-IoU: more accurate metric considering bounding box shape and scale. arXiv. 2023;2312.17663.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                                               28 / 29
44.   Ren S, He K, Girshick R, Sun J. Faster R-CNN: towards real-time object detection with region proposal networks. IEEE Trans Pattern Anal Mach
      Intell. 2017;39(6):1137–49. https://doi.org/10.1109/TPAMI.2016.2577031 PMID: 27295650
45.   Liu W, Anguelov D, Erhan D. Ssd: single shot multibox detector. In: Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, the
      Netherlands, October 11–14, 2016, Proceedings, Part I. Springer International Publishing. 2016. 21–37.
46.   Zhao Y, Lv W, Xu S, Wei J, Wang G, Dang Q, et al. DETRs beat YOLOs on real-time object detection. In: 2024 IEEE/CVF Conference on Com-
      puter Vision and Pattern Recognition (CVPR). IEEE. 2024. 16965–74. https://doi.org/10.1109/cvpr52733.2024.0160
47.   Wang A, Chen H, Liu L. Yolov10: real-time end-to-end object detection. arXiv. 2024;2405.14458.
48.   Chen X, Zhou Y. PCB defect target detection based on improved YOLOv5s. In: Proceedings of the 2023 7th International Conference on Innova-
      tion in Artificial Intelligence. ACM. 2023. 26–31. https://doi.org/10.1145/3594409.3594414
49.   Zhang Y, Xu M, Zhu Q. Improved YOLOv5s combining enhanced backbone network and optimized self-attention for PCB defect detection. J
      Supercomput. 2024;1–29.
50.   Shao M, Min L, Liu M, Li X, liu J, Li X. An enhanced network model for PCB defect detection: CDS-YOLO. J Real-Time Image Proc. 2024;21(6).
      https://doi.org/10.1007/s11554-024-01580-z
51.   Zhu H, Jiang J, Wang Y. Cgs-yolov5: a defect detection algorithm for PCB board based on yolov5 algorithm. In: Proceedings of the Second Interna-
      tional Conference on Physics, Photonics, and Optical Engineering (ICPPOE 2023). SPIE. 320–9.
52.   Yuan M, Zhou Y, Ren X. Yolo-hmc: an improved method for PCB surface defect detection. IEEE Trans Instrum Meas. 2024.
53.   Cheng T, Song L, Ge Y. Yolo-world: real-time open-vocabulary object detection. In: Proceedings of the IEEE/CVF Conference on Computer Vision
      and Pattern Recognition. 2024. 16901–11.
54.   Li F, Zhang H, Xu H. Mask dino: towards a unified transformer-based framework for object detection and segmentation. In: Proceedings of the
      IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023. 3041–50.
55.   Hou Y, Zhang X. A lightweight and high-accuracy framework for Printed Circuit Board defect detection. Eng Appl Artif Intell. 2025;148:110375.
      https://doi.org/10.1016/j.engappai.2025.110375
56.   Wang J, Xie X, Liu G. A lightweight pcb defect detection algorithm based on improved yolo v8-pcb. Symmetry. 2025;17(2):309.
57.   Ji L, Huang C, Li H, Han W, Yi L. MS-DETR: a real-time multi-scale detection transformer for PCB defect detection. SIViP. 2025;19(3). https://doi.
      org/10.1007/s11760-024-03757-2
58.   Zheng H, Chen X, Cheng H, Du Y, Jiang Z. MD-YOLO: surface defect detector for industrial complex environments. Optics Lasers Eng.
      2024;178:108170. https://doi.org/10.1016/j.optlaseng.2024.108170
59.   Zhang W, Huang T, Xu J. Df-yolov7: steel surface defect detection based on focal module and deformable convolution. Signal Image Video Pro-
      cess. 2025;19(1):1–10.
60.   Xie Z, Jin L. Steel surface defect detection based on bidirectional cross-scale fusion deep network. Opt Rev. 2025;1–13.
61.   Ma Y, Zhang Z, Ma S. Glf-net: global and local dynamic feature fusion network for real-time steel strip surface defect detection. IEEE Access. 2025.

PLOS One | https://doi.org/10.1371/journal.pone.0323684 June 2, 2025                                                                               29 / 29
