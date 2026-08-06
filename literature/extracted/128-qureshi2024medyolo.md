---
source_id: 128
bibtex_key: qureshi2024medyolo
title: A Comprehensive Systematic Review of YOLO for Medical Object Detection (2018 to 2023)
year: 2024
domain_theme: Medis
verified_pdf: 128_Systematic_Review_YOLO_Medis_Qureshi.pdf
char_count: 135613
---

Received 4 February 2024, accepted 7 April 2024, date of publication 10 April 2024, date of current version 29 April 2024.
Digital Object Identifier 10.1109/ACCESS.2024.3386826

A Comprehensive Systematic Review of YOLO
for Medical Object Detection (2018 to 2023)
MOHAMMED GAMAL RAGAB 1,2 , SAID JADID ABDULKADIR 1,2 , (Senior Member, IEEE),
AMGAD MUNEER 1 , ALAWI ALQUSHAIBI 1,2 , EBRAHIM HAMID SUMIEA 1,2 ,
RIZWAN QURESHI 3 , (Senior Member, IEEE), SAFWAN MAHMOOD AL-SELWI 1,2 ,
AND HITHAM ALHUSSIAN 1,2
1 Department of Computer and Information Sciences, Universiti Teknologi PETRONAS, Seri Iskandar 32610, Malaysia
2 Centre for Research in Data Science, Universiti Teknologi PETRONAS, Seri Iskandar 32610, Malaysia
3 Fast School of Computing, National University of Computer and Emerging Sciences, Karachi 75030, Pakistan

Corresponding author: Rizwan Qureshi (engr.rizwanqureshi786@gmail.com)
This work was supported by the Ministry of Higher Education (MOHE), Malaysia for providing financial assistance under Fundamental
Research Grant Scheme (FRGS/1/2022/ICT02/UTP/02/4) and Universiti Teknologi PETRONAS under the Yayasan Universiti Teknologi
PETRONAS (YUTP-FRG/015LC0-308) for providing the required facilities to conduct this research work.

  ABSTRACT YOLO (You Only Look Once) is an extensively utilized object detection algorithm that
  has found applications in various medical object detection tasks. This has been accompanied by the
  emergence of numerous novel variants in recent years, such as YOLOv7 and YOLOv8. This study
  encompasses a systematic exploration of the PubMed database to identify peer-reviewed articles published
  between 2018 and 2023. The search procedure found 124 relevant studies that employed YOLO for
  diverse tasks including lesion detection, skin lesion classification, retinal abnormality identification, cardiac
  abnormality detection, brain tumor segmentation, and personal protective equipment detection. The findings
  demonstrated the effectiveness of YOLO in outperforming alternative existing methods for these tasks.
  However, the review also unveiled certain limitations, such as well-balanced and annotated datasets, and the
  high computational demands. To conclude, the review highlights the identified research gaps and proposes
  future directions for leveraging the potential of YOLO for medical object detection.

  INDEX TERMS YOLO, healthcare applications, artificial intelligence, medical object detection, medical
  imaging, systematic review.

I. INTRODUCTION                                                                               process [7]. In recent years, artificial intelligence methods
Object detection is an essential task in computer vision, with                                have shown great promise for healthcare applications [8],
numerous applications in various domains, including medical                                   [9], [10], [11], [12]. Deep learning-based object detection
imaging [1], [2], surgical procedures [3], and personal protec-                               algorithms have shown exceptional performance in real time
tive equipment detection [4]. It plays a crucial role in medical                              object detection and localization [13], [14], [15]. Accurate
imaging by enabling the identification and localization of                                    and efficient object detection algorithms are essential for
abnormalities or objects of interest within medical images [5],                               assisting healthcare professionals in diagnosing and treating
[6]. Medical diagnosis relies heavily on the accurate detection                               various medical conditions [16], [17], [18]. One such object
and localization of abnormalities in medical images. The                                      detection algorithm is You Only Look Once (YOLO) [19],
traditional approach to object detection in medical imaging                                   [20], [21], [22], which has gained significant attention.
involves manual annotation and segmentation of the regions                                       YOLO is a state-of-the-art, real time, end-to-end object
of interest, which is a time-consuming and error-prone                                        detection algorithm that has gained significant attention in
                                                                                              the computer vision community [23]. YOLO is a single-stage
   The associate editor coordinating the review of this manuscript and                        detector, which means that it can detect all the objects in an
approving it for publication was Claudio Loconsole             .                              image in a single forward pass through a convolutional neural
                                  2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
VOLUME 12, 2024                                      For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/                         57815
                                                          M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

network (CNN). It uses a single neural network to predict the              • Evaluate the performance of YOLO in medical applica-
bounding boxes and class probabilities of the objects present                tions by synthesizing its accuracy, precision, recall, and
in an image [24]. This makes YOLO very fast, and it can                      other relevant metrics as reported in the selected studies.
achieve real time speeds on even a modest GPU [25].                        • Identify common challenges, limitations, and gaps in
   The application of YOLO in the medical domain has gar-                    the existing literature on the use of YOLO in medical
nered interest due to its ability to detect and localize anatom-             imaging.
ical structures [26], [27], lesions [28], [29], tumors [30],               • Provide insights and recommendations for future
[31], [32], and other clinically relevant medical objects [33],              research directions, improvements, and potential appli-
[34]. It can detect and localize abnormalities in medical                    cations of YOLO in the medical domain.
images, which can aid in the early detection and diagnosis                 The rest of this section contains the following sub-sections:
of various diseases, including breast cancer, lung cancer,              You Only Look Once (I-A), YOLO algorithm and architec-
narrowing of blood vessels [35], brain atrophy [36], and                ture (I-B), YOLO in action (I-C), image annotation (I-D),
abnormal protein deposits [37], cardiovascular diseases [38],           how YOLO operates (I-E), and advantages and drawbacks of
and neurological disorders [39]. The adoption of YOLO                   YOLO (I-F).
in medical applications has the potential to improve the
accuracy and efficiency of medical diagnosis, which can have            A. YOU ONLY LOOK ONCE (YOLO)
a significant impact on patient outcomes.                               This sub-section provides a brief description of YOLO,
   The real time performance of YOLO makes it particu-                  its versions, structure, and how it works. YOLO, proposed
larly appealing for time-sensitive medical procedures and               by Redmon et al. [45], is an object detection algorithm
clinical decision-making [40]. By accurately and efficiently            that uses convolutional neural networks (CNN) [46], [47]
identifying objects of interest, YOLO can potentially aid in            to detect objects in real time [25]. It is a single-stage
early disease detection, treatment planning, and monitoring             method that can achieve real time performance on a standard
of disease progression. However, as the adoption of YOLO                GPU [48]. It divides the image into a grid of cells, and
in medical imaging increases, it is essential to evaluate its           each cell is responsible for detecting objects within a certain
performance, strengths, limitations, and the specific medical           area [49], which allows for faster object detection compared
domains in which it has been applied [41]. Therefore, a sys-            to traditional two-stage methods and is particularly useful for
tematic literature review (SLR) may provide a comprehensive             real time applications. It has evolved over multiple versions,
and rigorous approach to analyze the existing literature on             each offering improvements in speed, detection accuracy, and
YOLO in medical applications. By systematically collecting,             capability to detect objects of varying sizes [50].
evaluating, and synthesizing the available evidence, this                  YOLO exhibits a high level of generalizability, making
review aims to identify the strengths, limitations, and                 it less prone to failure when applied to novel domains
potential of YOLO in medical applications. The findings of              or unexpected situations [23]. Unlike previous approaches
this review will assist researchers, healthcare professionals,          that repurpose classifiers for detection, YOLO is a versatile
and developers in understanding the performance of YOLO                 detector that learns to detect various objects. It acquires
and its suitability for different medical object detection tasks.       generalized representations of objects, enabling it to surpass
   Survey Motivation: There are already existing review                 leading detection methods like Deformable Parts Model
articles on YOLO, such as algorithmic developments in                   (DPM) [51] and Region-based Convolutional Neural Net-
YOLO [25], challenges and architectural developments for                work (R-CNN) [52], [53] by a good margin. However, YOLO
object detection using YOLO in [23], and a review on object             has some problems with detecting small objects and will
detection techniques in [42]. A survey on object detection for          do worse with scenes with many overlapping objects. The
medical images using deep learning techniques was published             main advantage of YOLO lies in its real time object detection
in [43] and a comprehensive analysis of applying object                 capability, which is crucial in time-sensitive applications.
detection methods for medical image analysis in [44]. In this              The YOLO architecture has evolved significantly from
paper, we focused on the YOLO architecture, its evolution,              its inception in v1 to the cutting-edge advancements in
and applications for three key medical applications; medical            v8 as shown in Figure 1. With v1, the initial foundation
images, personal protective equipment detection, and surgical           was laid, introducing a groundbreaking concept of real time
procedures. To the best of our knowledge, it is the first article       object detection through a single network pass in 2015.
to discuss three key medical applications using the YOLO                YOLOv2 (2016): Improves YOLOv5 by using a larger
series architecture.                                                    input size, more anchor boxes, and a new loss function.
   The main contributions of this paper are:                            YOLOv3 (2018): Introduces a new network architecture
   • Identify and select relevant peer-reviewed articles                called Darknet-53, which is deeper and more accurate than
      published between 2018 and 2023 that focus on the                 the previous architectures used in YOLO.
      application of YOLO in medical imaging.                              YOLOv4 (2019): Improves upon YOLOv3 by using a
   • Analyze and summarize the characteristics of the                   new training method called Mosaic data augmentation, which
      selected studies, including the medical domains,                  helps to improve the model’s robustness to different object
      datasets, evaluation metrics, and findings.                       scales and orientations. YOLOv5 (2020): Introduces a new

57816                                                                                                                              VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                                                                                      pooling (SPP) module and the path aggregation network
                                                                                      (PAN). The neck’s function is to combine the feature
                                                                                      maps from various layers of the backbone network and
                                                                                      forward them to the head. In YOLO, popular neck
                                                                                      options include Spatial Pyramid Pooling (SPP), Feature
                                                                                      Pyramid Network (FPN), NAS-FPN, and Rep-PAN.
                                                                                   ❐ Head: The head component is responsible for handling
                                                                                      the combined features and making predictions regarding
                                                                                      bounding boxes, objectness scores, and classification
                                                                                      scores. In YOLO, a one-stage object detection approach,
                                                                                      like YOLOv3, is employed as the detection head. The
                                                                                      head’s primary role is to generate the ultimate output of
                                                                                      the network, which includes predicted bounding boxes
                                                                                      and class labels. YOLO utilizes various popular heads,
                                                                                      such as Efficient decoupled, Multi-scale, and Anchor-
                                                                                      based detection heads.
                                                                                   The YOLOv1 architecture, Figure 3, is inspired by
FIGURE 1. Timeline of YOLO versions.                                            GoogLeNet and it replaces inception modules with 1 × 1 and
                                                                                3×3 convolutional layers. This architecture utilizes two fully
network architecture called CSPDarknet, which is more                           connected layers on the convoluted feature map, outputting a
efficient than Darknet-53. YOLOv6 (2021): Improves upon                         final prediction grid of size S x S x (5B + K) [48].
YOLOv5 by using a new loss function called GIoU, which                             This initial YOLO model prioritized speed by utilizing
helps to improve the model’s accuracy. YOLOv7 (2022):                           a single CNN [58] to directly predict object locations and
Introduces a new network architecture called Panoptic                           classes in real time. However, this approach led to decreased
YOLO, which can detect both objects and semantic segments                       accuracy, particularly for small objects or those with overlap-
in an image.                                                                    ping bounding boxes [59]. The detection architecture of the
   YOLOv8 (2023): The latest version of YOLO, which                             original YOLO model performed a single pass on the image
introduces a number of new features, including a new network                    to predict object locations and class labels [60]. Subsequent
architecture called BiFPN, a new loss function called CIoU,                     versions of YOLO introduced improvements to address these
and a new training method called Cross-GPU training.                            limitations.
                                                                                   YOLOv2, for instance, introduced batch normalization,
B. YOLO ALGORITHM AND ARCHITECTURE                                              anchor boxes, and passthrough layers to enhance object
The YOLO architecture consists of three main components:                        localization. Additionally, it incorporated multiscale training
(i) the backbone; (ii) the neck; (iii) the head [23], [48], [50],               and achieved a processing speed of 40-90 frames per
[54]. The architecture of the backbone, neck, and head can                      Second (FPS) [50]. These refinements aimed to enhance
vary between different versions of YOLO, and improvements                       both accuracy and speed in object detection tasks. The
in these components have led to significant improvements in                     performance of YOLOv3 was improved by incorporating a
the overall accuracy and speed of the YOLO network [25],                        multi-scale feature extraction architecture. New backbone
[55]. The choice of backbone, neck, and head can affect the                     network, feature pyramid network, and more anchor boxes.
speed and accuracy of the YOLO model and depends on                             It allowed a tradeoff between speed and accuracy [25].
the specific application and the desired trade-off [49]. More                      YOLOv4 and YOLOv5 introduced new network back-
recent versions of YOLO have introduced improvements in                         bones, improved data augmentation, and optimized training
all three components to achieve better performance. Figure 2                    strategies. This enhanced accuracy without severely impact-
represents YOLO Architecture.                                                   ing real time performance [61], [62]. YOLO framework
  ❐ Backbone: The primary role of the backbone is to                            for object detection consistently evolved to balance speed
      extract valuable characteristics from the initial image.                  and accuracy in detection tasks. PP-YOLO [63], developed
      Usually, a convolutional neural network is employed                       by Alibaba Group, provided further improvements with a
      as the backbone, which has been trained on extensive                      new backbone network, spatial attention module, and path
      datasets like ImageNet. The backbone functions as the                     aggregation network, making it faster and more accurate than
      network responsible for extracting features and gener-                    YOLOv5 [64].
      ating feature maps from the input images. In YOLO,                           YOLOv6 implemented a variant of the EfficientNet archi-
      some commonly utilized backbones include VGG16,                           tecture named EfficientNet-L2, surpassing the EfficientDet
      ResNet50, CSPDarknet53, and EfficientRep.                                 architecture used in YOLOv5 in terms of efficiency. It also
  ❐ Neck: The neck serves as the intermediary between the                       introduced a design called EfficientRep Backbone and Rep-
      backbone and the head in the architecture. It consists                    PAN Neck, leading to faster and more accurate results. The
      of two main components, namely the spatial pyramid                        head of the network was decoupled, adding layers, and

VOLUME 12, 2024                                                                                                                          57817
                                                            M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                  FIGURE 2. The architecture of YOLO consists of a backbone, neck, and head. The backbone, neck, and head
                  vary in different versions of YOLO. For backbone, normally Darknet, VGG16, or Resnet are used; for neck
                  feature pyramid network (FPN) [56], and for neck Densenet [57] or sparsenet are used.

                      FIGURE 3. YOLOv1 network architecture [48].

separating these features from the final head, which improved             C. YOLO IN ACTION
performance [65].                                                         YOLO revolutionized the process of object detection by
   YOLOv7 improved accuracy without raising inference                     simultaneously detecting all bounding boxes within an S × S
costs, reducing parameters and computation by 40% and                     region using grids. It predicts B bounding boxes for each
50% respectively, compared to other leading real time object              class, accompanied by confidence scores for C different
detectors [66]. It had a faster, stronger network architecture,           classes per grid element [48]. Each bounding box prediction
more accurate detection performance, a more robust loss                   comprises of five values: Pc , bx , by , bh , bw . Here, Pc repre-
function, and enhanced label assignment and model training                sents the confidence score, reflecting the model’s confidence
efficiency. It also required cheaper computing hardware and               in the presence and accuracy of the object within the box. The
could be trained faster on small datasets without pre-trained             coordinates bx and by denote the box center relative to the
weights [50], [67].                                                       grid cell, while bh and bw indicate the box height and width
   YOLOv8 [68], the most advanced model at the time                       relative to the entire image. The output of YOLO is a tensor of
of writing, had better feature aggregation and a mish                     size S × S × (B × 5 + C), which may undergo non-maximum
activation function that improved detection accuracy and                  suppression (NMS) to eliminate duplicate detections. These
processing speed. It is an anchor-free model, predicting                  grid cells facilitate operations related to bounding box
object centers directly without known anchor boxes. YOLO-                 estimation and class probabilities [50]. Consequently, YOLO
NAS [69], created by Deci AI, outperformed its predecessors               estimates the likelihood of the detection element’s bounding
(especially YOLOv6 and YOLOv8) by achieving higher                        box center being located within the grid cell, as formulated
mAP values on the COCO dataset while maintaining                          by Equation 2.
lower latency. It also performed best on the Roboflow                               C(P) = Prob(p) × IoU (prediction, target)            (1)
100 dataset benchmark, indicating its ease of fine-tuning
on custom datasets. Thus, the YOLO family of object                       where: C(P) is the confidence of prediction P, Prob(p) is
detection models has consistently evolved to optimize both                the probability of presence of object p, and IoU (prediction,
speed and accuracy, providing a variety of models to                      target) is the Intersection over Union between the predicted
cater to diverse applications and hardware requirements.                  and target bounding boxes.
Table 1 summarizes the key features of each version                                                            B ∩ Bgt
of YOLO.                                                                                            IoU =                                        (2)
                                                                                                               B ∪ Bgt

57818                                                                                                                                VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 1. Key features of each version of YOLO.

TABLE 2. YOLO included studies categorized in the Oncology domain.

   In the context of the YOLO algorithm, the target box is
denoted as Bgt , while the predicted box is represented as
B. The probability (p) signifies whether the object exists
within the detected bounding box. The IoU metric, defined
by Equation 2, calculates the intersection area between the
ground truth and predicted bounding boxes. It determines
an acceptable area for each detected object in the input
image and makes decisions based on it. To obtain the most
suitable bounding box, the confidence value is applied after
the estimation. The process of computation of the IoU can be
illustrated as shown in Figure 4.

D. IMAGE ANNOTATION
Image annotation [70] is a vital process in computer vision                     FIGURE 4. Computing the Intersection over Union: (a) poor detection
                                                                                performance, (b) good detection performance, (c) excellent detection
and machine learning. It is the process of labeling or marking                  performance.
specific objects or regions of interest within an image [71].
It involves adding metadata or annotations to images to
provide additional information about the objects or features                    or semantic segmentations around those objects. Accurate
present in the image. The purpose of image annotation                           annotations are crucial for training models to accurately
is to create a labeled dataset that serves as training data                     detect, recognize, and segment objects. They provide ground
for learning algorithms, particularly for tasks like object                     truth data, enable object localization, ensure model accuracy
detection, object recognition, and image segmentation [72].                     and performance, and facilitate diverse and domain-specific
By annotating images, human annotators or data scientists                       datasets. Annotations also aid in model evaluation and serve
manually outline or mark the objects of interest within                         as a valuable resource for transfer learning. In summary,
the image, often by drawing bounding boxes, polygons,                           image annotation is a fundamental step that underpins

VOLUME 12, 2024                                                                                                                                   57819
                                                              M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 3. YOLO included studies categorized in the Pathology domain.

the development of reliable and effective computer vision                      In the above matrix, each line represents a single object
systems in various industries and applications [41].                        annotation where c represents the class or label of the
   There are several popular tools available for annotating                 object being annotated. It is usually represented by an
images. The choice of tool often depends on personal                        integer index corresponding to the class label defined in the
preference, project requirements, and the specific desired fea-             YOLO configurations. x and y represents the normalized x, y
tures. Commonly used tools include Visual Object Tagging                    coordinate of the bounding box’s center point. The value
Tool (VoTT) [73], VGG Image Annotator (VIA) [74], and                       is relative to the width of the image, ranging from 0 to 1.
Roboflow [75] which is a popular platform for managing,                     w and h represent the normalized width and height of the
preprocessing, and annotating datasets for computer vision                  bounding box. The value is relative to the width of the image,
tasks. It provides a comprehensive end-to-end solution for                  ranging from 0 to 1. Each annotation line corresponds to one
dataset management, annotation, and preprocessing, offering                 annotated object in the image. Multiple lines can be present
a range of features that can help streamline your object                    in the annotation file, each representing a different object.
detection workflow. When it comes to annotating datasets for
YOLO, there are a few commonly used annotation formats
                                                                            E. HOW YOLO OPERATES
that work well with YOLO-based object detection models.
                                                                            During the process of predicting bounding boxes, YOLO
The most popular annotation format for YOLO datasets is
                                                                            employs ‘‘dynamic anchor boxes’’ utilizing a clustering
the Darknet format, which is the native format used by the
                                                                            algorithm. This algorithm groups the ground truth bounding
Darknet framework, the original implementation of YOLO.
                                                                          boxes into clusters and utilizes the centroids of these clusters
                       ci x y w h                                           as anchor boxes [76]. By doing so, the anchor boxes become
                     ci x y w h                                           better aligned with the size and shape of the detected objects.
                                                 
                    · · · · · · · · · · · · · · ·         (3)             However, the primary source of error in YOLO arises from
                                                 
                     ci x y w h                                           localization. This is due to the fact that the bounding box
                       ci x y w h                                           ratios are entirely learned from the data, causing YOLO to

57820                                                                                                                                  VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 4. YOLO included studies categorized in the Radiology domain.

VOLUME 12, 2024                                                                            57821
                                                               M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 4. (Continued.) YOLO included studies categorized in the Radiology domain.

TABLE 5. YOLO included studies categorized in the Surgical Procedures domain.

struggle with atypical ratio bounding boxes [77].                            YOLO defines a threshold value for the confidence score,
                                                                             where predictions below this threshold are discarded. Non-
                         bx = σ (tx ) + cx
                                                                             maximum suppression is then applied to generate the final
                         by = σ ty + cy
                                    
                                                                             positions for the detected bounding boxes. Finally, a loss
                         bw = (pw ) ∗ etw                          (4)       function is computed for the detected bounding boxes in the
                         bh = Ph ∗ e   th                                    last stage. Figure 5 provides a clear understanding of the work
                                                                             of YOLO.
   In the YOLO framework, the bounding box coordinates are
denoted as bx , by , bw , and bh , while the center coordinates
are represented by x, y, and the width and height are                        F. ADVANTAGES AND DRAWBACKS OF YOLO FOR
given by bw and ph respectively. Each bounding box has                       MEDICAL OBJECT DETECTION
estimated coordinates tx , ty , tw , and th . The values cx and              YOLO is also highly generalized and can recognize a wide
cy correspond to the upper-left coordinates of the grid cell.                range of objects. However, it is important to be aware of the

57822                                                                                                                                   VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 6. YOLO included studies categorized in the Personal Protective Equipment Detection domain.

                                                                                      within complex medical images, supporting precise
                                                                                      diagnoses.
                                                                                    • Multi-medical Object Detection: YOLO excels in
                                                                                      detecting multiple objects simultaneously, making it
                                                                                      valuable for identifying various medical anomalies,
                                                                                      tumors, lesions, pathologies factors, or abnormalities
                                                                                      within a single image.
                                                                                    • Adaptability: The YOLO architecture is versatile and
                                                                                      can be fine-tuned for specific medical domains, such
                                                                                      as surgical procedures, personal protective detection
                                                                                      equipment, and medical images.
                                                                                    • Minimal False Positives: YOLO’s ability to incorporate
                                                                                      global context reduces the likelihood of false positive
                                                                                      detections, enhancing the reliability of medical diag-
                                                                                      noses.

                                                                                2) DRAWBACKS OF YOLO FOR MEDICAL OBJECT
                                                                                DETECTION
                                                                                There are some drawbacks of YOLO such as:
                                                                                   • Large Dataset Requirement: One of the primary
                                                                                     drawbacks of YOLO is its need for a substantial dataset
                                                                                     of images for training. The collection of these images
FIGURE 5. YOLO works by dividing the input image into a grid of cells.
Each cell predicts a bounding box, a confidence score, and the class                 can be both time-consuming and expensive.
probabilities for the objects in that cell. The bounding box is a rectangle        • Sensitivity to Object Scale: YOLO’s performance can
that is used to surround the object. A confidence score, between 0 and 1,
indicates how confident the model is that the object is present in the cell.         be significantly affected by the scale of objects in
The class probabilities are the probabilities that the object in the cell            the input image, leading to potential false positives or
belongs to each of the possible classes.
                                                                                     negatives.
                                                                                   • Difficulty with Small Objects: YOLO often struggles
                                                                                     to detect smaller objects as efficiently as it does larger
advantages and disadvantages of YOLO before using it for a                           ones. The system divides the image into a grid of cells,
specific application.                                                                and small objects might not be large enough to occupy
                                                                                     an entire cell, affecting detection accuracy.
1) ADVANTAGES OF YOLO FOR MEDICAL OBJECT                                           • Issues with Occluded Objects: YOLO tends to falter
DETECTION                                                                            when tasked with detecting objects obscured by others.
   • Real-Time    Detection: YOLO’s inherent ability to                              As it predicts the bounding box of each object,
     detect objects in a single pass enables real time                               an obscured or partially visible object might not
     processing of medical images, which is crucial in                               have a well-defined bounding box, limiting detection
     time-sensitive medical scenarios such as surgeries or                           performance.
     emergency diagnostics.                                                        • Limited Object Diversity: The system often struggles
   • Efficiency: YOLO’s single-pass architecture is com-                             with a diverse set of object classes. As YOLO is trained
     putationally efficient, allowing for faster processing                          on a finite dataset of images, it may find it challenging
     speeds and reduced computational requirements, which                            to generalize its detection capabilities to unfamiliar
     is especially important for medical applications that                           objects.
     demand rapid results.                                                         The rest of this research work is structured as follows.
   • Accuracy: YOLO’s holistic approach to object detec-                        Section II provides the methodology for conducting this
     tion considers contextual information, leading to accu-                    study. Section III highlights the results of the literature’s
     rate localization and classification of medical objects                    applicable studies and responds to the previously stated

VOLUME 12, 2024                                                                                                                          57823
                                                       M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

research questions using synthesized data from the included                RQ5: How does YOLO compare to other existing
research. Finally, section IV concludes this paper.                        object detection algorithms in terms of performance,
                                                                           efficiency, and applicability to medical imaging?
II. METHODS
                                                                     2) SEARCH STRATEGY
This paper seeks to assemble a comprehensive compilation of
                                                                     A systematic search of the literature was conducted using
relevant studies focusing on YOLO in the medical domain,
                                                                     the National Library of Medicine’s PubMed database
covering the period from 2018 to 2023. The aims are to
                                                                     (https://pubmed.ncbi.nlm.nih.gov, accessed and last searched
explore YOLO’s potential capabilities in medical applica-
                                                                     on 26 January 2024 ) to identify relevant papers published
tions, diagnosis, and treatment planning. This paper was
                                                                     between 01/01/2018 and 31/12/2023). The search strategy
conducted using the Preferred Reporting Items for Systematic
                                                                     employed a combination of keywords, specifically (YOLO
Reviews and Meta-Analyses (PRISMA) statement [78].
                                                                     AND ((medical application) OR (medical image))), and
The rest of this section has been thoroughly organized
                                                                     adhered to the PRISMA guidelines [78]. The inclusion
into two subsections. The first subsection (II-A) highlights
                                                                     criteria focused on original research articles, while review
the evidence acquisition, which explains the aim (II-A1),
                                                                     papers, abstracts, and reports from meetings were excluded.
search strategy (II-A2), and study selection criteria (II-A3).
                                                                     Each identified article underwent a thorough evaluation to
Meanwhile, evidence synthesis of this SLR is presented in
                                                                     determine its eligibility for inclusion in this SLR. Figure 6
the second subsection (II-B).
                                                                     illustrates the PRISMA flowchart conducted in this study.

A. EVIDENCE ACQUISITION                                              3) STUDY SELECTION CRITERIA
Evidence acquisition in PRISMA involves systematically               The selection criteria were carefully designed to ensure the
searching and selecting relevant studies from databases.             identification of research articles that best align with the
Medical applications with YOLO capabilities can aid in               objectives of the systematic review while excluding those that
automating the identification and extraction of relevant             are not relevant. The following inclusion criteria were applied
evidence from medical images. This integration streamlines           to identify the studies to be included in this review:
the evidence acquisition process, improving efficiency and             1) Inclusion Criteria:
accuracy in SLRs.                                                         ❐ Peer-reviewed articles published between 2018 and
                                                                             2023 that focus on the application of YOLO in the
                                                                             medical domain.
1) AIM
                                                                          ❐ Studies that report original research findings.
The primary goal of this systematic review is to compre-
                                                                          ❐ Studies that primarily focus on medical applications
hensively analyze and evaluate the application of YOLO
                                                                             of YOLO.
in medical imaging with a focus on assessing its accu-
                                                                          ❐ Studies published in English language.
racy, efficiency, and effectiveness in medical applications.           2) Exclusion Criteria:
Additionally, the review aims to identify medical areas
                                                                          ❐ Studies published before 1 January 2018.
where YOLO has been successfully utilized, examining
                                                                          ❐ Review papers, abstracts, and reports from meetings
the literature to determine its strengths and potential for
                                                                             or conferences.
significant advancements. Moreover, it provides practical
                                                                          ❐ Studies that do not involve the YOLO algorithm or its
implications for integrating YOLO into medical applications,
                                                                             application in the medical domain.
considering how its utilization can enhance efficiency,
                                                                          ❐ Studies with insufficient information or incomplete
accuracy, and automation in medical image and diagnosis.
                                                                             methodology.
To this end, the following questions were established as our
                                                                          ❐ Studies that primarily focus on non-medical applica-
SLR research focus:
                                                                             tions of YOLO.
     RQ1: What are the key medical domains in which                       ❐ Studies published in languages other than English.
     YOLO has been applied for medical object detection?
     RQ2: What are the performance metrics used to evaluate          B. EVIDENCE SYNTHESIS
     the effectiveness of YOLO in medical applications,              Initially, 124 articles were obtained from the database search,
     and how does YOLO perform in terms of accuracy,                 and 48 were included in this study. The quality assessment
     precision, recall, and other relevant metrics?                  guidelines employed in this systematic review are designed to
     RQ3: What are the specific tasks and objects of                 reduce bias, enhance transparency, and ensure repeatability.
     interest within the medical domain where YOLO has               These guidelines focus on the YOLO medical applications
     demonstrated strong performance?                                utilizing medical datasets. The following criteria were
     RQ4: What are the limitations and challenges encoun-            considered during the assessment process: alignment of the
     tered when using YOLO in medical applications,                  selected studies with the primary objective of the systematic
     such as imbalanced datasets, small sample sizes, and            review, evaluation of the utilization of performance metrics,
     computational requirements?                                     scrutiny of the soundness of the conclusions drawn in the

57824                                                                                                                           VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                   FIGURE 6. PRISMA flowchart.

                                                                                observable in the graph of the identified publications, starting
                                                                                with a modest count of 3 identified publications in 2018. This
                                                                                number remains relatively stable in 2019, suggesting a period
                                                                                of early academic interest. The subsequent years illustrate
                                                                                a notable increase in research activity. The year 2020 sees
                                                                                the number double to 6 identified publications, indicating
                                                                                a growing recognition of YOLO’s relevance in medical
                                                                                research. This momentum is maintained and amplified in the
                                                                                following years, with a steady rise to 18 papers in 2021 and a
                                                                                sharper ascent to 33 in 2022. The most striking leap occurs
                                                                                in 2023, where the count of identified publications surges
                                                                                to 58. This substantial growth over five years signifies a
                                                                                robust and accelerating interest in the application of YOLO
FIGURE 7. Trend of publications on the YOLO applications in medical             within medical imaging. It is worth mentioning that, the
imaging.                                                                        observed decrease in the number of included studies in
                                                                                2023 is attributable to the implementation of more strict
                                                                                inclusion and exclusion criteria, ensuring that only the most
selected studies, and verification of the use of valid and                      pertinent and high-quality research is selected for review.
reliable datasets.                                                                 Figure 8 illustrates the distribution of the main versions of
   Figure 7 displays the years and the corresponding counts of                  YOLO detected from the 48 included studies. The pie chart
identified and included publications. A clear upward trend is                   indicates that YOLOv3 is the most frequently encountered

VOLUME 12, 2024                                                                                                                           57825
                                                              M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                                                                            FIGURE 9. Three major domains of YOLO in healthcare; Medical Imaging,
                                                                            Surgical Procedures, and Personal Protective Equipment Detection.

FIGURE 8. Distribution of YOLO versions in medical imaging.

                                                                            in chest X-rays, breast masses in mammograms, and brain
version in the literature, with 21 instances, followed by                   tumors in MRI scans [17], [30], [86], [87]. Its ability to
YOLOv5 in 9 instances, and YOLOv4 in 8 instances. This                      identify these objects of interest accurately and efficiently
could suggest that these versions have reached a level of                   enables earlier detection, leading to timely intervention and
maturity and performance that makes them popular among                      improved patient outcomes. In Figure 10, different medical
researchers and practitioners. YOLOv7 and YOLOv8 are                        image applications clearly explain the advancement of YOLO
represented as well with 2 instances each, indicating their                 in the field.
emerging presence in the field and suggesting that more                        Moreover, YOLO has shown promise in detecting anoma-
research papers on these versions could be yet to be                        lies in medical images. Anomalies can encompass a wide
published.                                                                  range of abnormalities, such as fractures, hemorrhages,
                                                                            or foreign objects. YOLO’s real time performance makes
III. RESULTS                                                                it well-suited for tasks such as identifying fractures in X-
This section highlights the results of the literature’s appli-              rays, detecting bleeds in brain CT scans, or identifying
cable studies and responds to the previously stated research                foreign bodies in radiographic images [87], [88]. By rapidly
questions (Sub-section II-A1) using synthesized data from                   flagging anomalies, YOLO assists radiologists and clinicians
the included research.                                                      in prioritizing critical cases and expediting appropriate
   The key medical domains and applications where YOLO                      treatment.
has been applied for medical object detection, along with                      In addition, YOLO has been applied successfully in
their performance metrics used to evaluate the YOLO’s                       segmenting organs such as the heart, liver, kidney, and brain
effectiveness in these applications, with a focus on accuracy,              in different imaging modalities, including MRI and CT
precision, recall, and other relevant metrics, are categorized              scans [32], [81]. Accurate identification and delineation of
from the 48 included studies into three main domains as                     organs are crucial for surgical planning, radiation therapy,
shown in Figure 9: I) Medical Imaging (III-A), II) Surgi-                   and monitoring disease progression [31]. Its high accuracy
cal Procedures (III-B), and Personal Protective Equipment                   and efficiency streamline the segmentation process and
Detection (III-C).                                                          contribute to more precise diagnoses and treatment plans.
                                                                            In surgical settings, YOLO has shown promise in detecting
A. MEDICAL IMAGING                                                          and tracking surgical instruments during procedures [83],
YOLO has exhibited strong performance in various tasks                      [84]. By analyzing live video feeds, YOLO can identify
and objects of interest within medical imaging [5], including               instruments, surgical tools, and other objects of interest in
lesion detection [28], [79], anomaly detection [80], organ                  real time, providing valuable assistance to surgeons and
segmentation [31], [81], and instrument tracking [82], [83],                improving surgical safety. Its ability to handle fast-paced
[84]. These applications highlight YOLO’s potential to                      environments and track objects accurately makes it a valuable
enhance diagnostic accuracy, improve workflow efficiency,                   tool in computer-assisted interventions and robotic surgeries.
and ultimately advance patient care in the field of med-                       Also, YOLO has shown tremendous success in the detec-
ical imaging. One of the primary applications of YOLO                       tion and classification of breast masses in mammograms [19],
in medical imaging is the detection and localization of                     [79], [89], [90], [91]. Its use in such applications has proven
lesions [85]. Lesions can include tumors, nodules, masses,                  to significantly reduce the time, cost, and potential for
or any abnormality that may indicate disease [29]. YOLO has                 human error inherent in traditional methods of mammogram
demonstrated strong performance in detecting lung nodules                   evaluation. The YOLO system preprocesses the mammo-

57826                                                                                                                                  VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                  FIGURE 10. YOLO in different medical images applications: (a) periodontitis bone loss diagnosis, (b) glomerular
                  detection, (c) breast cancer detection (d) lung normal and abnormal detection, (e) brain tumor detection, (f) white and
                  red blood cells detections.

grams and then detects masses in them, distinguishing                           evaluation process of screening mammograms is a laborious
between malignant and benign lesions without any human                          task, requiring significant time, cost, and human resources,
intervention [80], [92].                                                        and is prone to errors due to fatigue and the inherent subjec-
   The included studies in the medical imagining domain have                    tivity of human evaluation. However, with the introduction
been further classified into three sub-domains: Oncology                        of YOLO into this process, an end-to-end computer-aided
(Table 2), Pathology (Table 3), and Radiology (Table 4).                        diagnosis system has been proposed and implemented [122].
   However, while the applications of YOLO in healthcare                        The described system performs preprocessing on DICOM-
have been fruitful, there are challenges, including the need for                format mammograms to convert them into images while
large, diverse, and high-quality datasets for model training.                   preserving all the data. It is capable of detecting masses
The algorithm’s sensitivity to the scale of objects in images                   in full-field digital mammograms and can differentiate
is another aspect that needs further improvement. Despite                       between malignant and benign lesions automatically, without
these challenges, with continuous research and refinement,                      requiring any human intervention, significantly reducing the
YOLO’s application in medical imaging holds significant                         potential for human error and streamlining the entire process.
promise for advancing healthcare diagnostics. One of the
most promising areas of application for YOLO is medical                          B. SURGICAL PROCEDURES
imaging. YOLO has shown promising results in various fields                     YOLO could also be applied in surgical procedures. It offers
such as radiology, oncology, and pathology [19]. For instance,                  great potential for surgical procedures, particularly in the
in tumor detection, YOLO can identify and locate abnormal                       context of computer-assisted and robotic surgery. The
growths in medical images, assisting healthcare professionals                   algorithm’s ability to detect, classify, and locate objects in
in early disease diagnosis and treatment planning [30], [31],                   real time can be of significant value in the surgical environ-
[32]. In the context of COVID-19, YOLO has demonstrated                         ment [82], [83], [84]. For instance, YOLO can be utilized
its value in detecting and quantifying infection patterns in                    to identify and locate specific surgical instruments within
lung CT scans, contributing to rapid and effective patient                      the operating field, helping to streamline instrument tracking
management [21].                                                                and potentially reducing surgical errors. Additionally, it could
   As healthcare moves towards a more digitized environ-                        play a role in enhancing the safety and precision of robotic
ment, the volume of medical imaging data is growing. This                       surgical systems by improving their ability to recognize
data can be effectively analyzed using AI and machine                           and interact with various surgical elements in real time.
learning tools like YOLO to extract valuable insights that                      Figure 11 demonstrates the usage of YOLO in surgical
can aid in diagnosis and treatment planning. For instance,                      procedures.
YOLO has been used to detect and classify breast masses                            The study by Wang et al. [83] developed an AI model
in mammograms [19], [79], [89], [90], [91]. The traditional                     based on YOLOv3 to identify parathyroid glands during

VOLUME 12, 2024                                                                                                                             57827
                                                                 M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

        FIGURE 11. YOLO surgical procedures applications of (a)surgical tool detection in open surgery videos, (b) surgical instruments, (c) real
        time instance segmentation of surgical instruments.

endoscopic thyroid surgery. Using 1,700 images from thy-                       by healthcare professionals and the use of various medical
roidectomy videos, the model outperformed junior surgeons                      devices. However, these traditional methods can be time-
and was comparable to senior surgeons in identification                        consuming, costly, and subject to human error.
rates. Amiri Tehrani Zade et al. [84] developed a CNN-                            For instance, YOLO could be deployed to monitor
based method to enhance needle tracking in ultrasound for                      patient activity and movements in an in-patient setting,
medical procedures. Using advanced motion estimation and                       identifying potential falls or other hazardous events before
the YOLOv3 framework, it accurately locates needles in                         they occur [21]. This real time alert system could greatly
real time ultrasound, outperforming current methods, and                       enhance patient safety and improve healthcare outcomes.
promising better ultrasound-guided interventions. Table 5                      Similarly, for patients with chronic conditions, YOLO could
shows YOLO included studies categorized in the surgical                        potentially be utilized to monitor medication intake or
procedures domain.                                                             adherence to certain therapeutic exercises, promoting better
   Surgeons often rely on various imaging technologies, such                   disease management. YOLO could provide valuable support,
as MRI or CT scans, to guide their procedures. However,                        identifying significant health events from recorded or live
interpreting these images and applying their insights to the                   video feeds. Despite the promising prospects, integrating
surgical process can be challenging. With the use of YOLO,                     YOLO into patient monitoring systems presents challenges,
these images could be analyzed in real time, providing                         including ensuring patient privacy and dealing with diverse
surgeons with immediate feedback and guidance during                           and complex real-world scenarios. However, with ongoing
the procedure [82]. This could potentially lead to more                        research and development, YOLO’s application in patient
precise surgeries, fewer complications, and better patient                     monitoring can revolutionize care delivery, enhancing patient
outcomes. Furthermore, YOLO could be integrated with                           safety and health outcomes.
surgical navigation systems to improve real time imaging,                         Moreover, YOLO has been applied in face mask detec-
enabling surgeons to better visualize the surgical field and                   tion. Han et al [21] developed an enhanced, lightweight
carry out complex procedures with higher precision. This is                    YOLOv4-tiny-based detector for real time mask status
particularly relevant for minimally invasive surgeries where                   detection, offering improved precision and speed with
real time imaging plays a crucial role. Despite these potential                fewer parameters, suitable for public health applications.
applications, integrating YOLO into surgical procedures also                   Loey et al. [4] proposed a deep learning model combining
brings challenges. These include ensuring the algorithm’s                      ResNet-50 and YOLOv2 to detect medical face masks in
robustness and reliability in a highly variable and complex                    images, achieving 81% precision and outperforming related
surgical environment, and addressing concerns related to                       models in accuracy. Table 6 shows YOLO-included studies
patient safety and data privacy. Nevertheless, with continued                  categorized in the personal protective equipment detection
research and technological refinement, YOLO’s application                      domain.
in surgical procedures promises to enhance surgical precision                     With the applications of YOLO, it is possible to build
and patient outcomes [84].                                                     automated patient monitoring systems that can continuously
                                                                               monitor patients’ vital signs and behavior and alert healthcare
C. PERSONAL PROTECTIVE EQUIPMENT DETECTION                                     professionals to any abnormal patterns or signs of distress.
YOLO has demonstrated significant potential in the field                       Such systems could potentially lead to faster response times
of patient monitoring as shown in Figure 12. Real-time                         in emergency situations, more effective use of healthcare
patient monitoring is a critical component of healthcare,                      resources, and better overall patient outcomes.
providing valuable insights into a patient’s condition and                        Finally, Table 7 shows the data sources of all the 48
enabling timely interventions. Continuous patient monitoring                   included studies. From those studies reviewed, no common
is crucial in many healthcare scenarios, from intensive care                   datasets were identified across the medical applications,
units to home-based care. The ability of YOLO to detect                        except for a few instances:
and recognize objects in real time can be adapted to monitor                      • In lung nodule detection: the Lung Nodule Analysis
various aspects of patient care. Traditionally, this monitoring                     2016 (LUNA16) dataset was used in 2 papers [86]
has been done through a combination of manual observations                          and [87].

57828                                                                                                                                      VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                   FIGURE 12. Medical personal protective equipment categories: (a) suit, (b) face shield;(c) goggles, (d) mask, and
                   (e) glove.

   • In  breast cancer detection: three public benchmark                        features, it simultaneously escalates the model’s complexity
     datasets were utilized.                                                    and the computational resources needed.
     – INbreast was used in 4 papers [17], [79], [89],                             Though promising, the adoption of YOLO in healthcare
        and [90].                                                               brings with it an array of challenges and limitations that
     – Digital Database for Screening Mammography                               must be acknowledged. However, a prominent drawback
        (DDSM) was used in 2 papers [17] and [91].                              is its comparative need for more accuracy in detecting
     – An enhanced version of DDSM, the Curated Breast                          small targets, a shortfall with potential ramifications in areas
        Imaging Subset of Digital Database for Screen-                          such as pill recognition or the identification of tiny lesions
        ing Mammography (CBIS-DDSM) was used once                               in medical imaging where the identification of minuscule
        by [90].                                                                objects is crucial [125]. It utilizes a deep network structure
   • In brain tumor detection: the Tumor Cancer Imaging                         for feature extraction, enhancing accuracy at the cost of
     Archive (TCIA) dataset was utilized by [32] and [81].                      considerable computational power. This requirement can be
  On the other hand, the majority of the included studies have                  a limiting factor in healthcare settings where resources are
used different datasets, with many not publicly accessible                      constrained [126], [127].
due to patient privacy concerns. Legal and ethical guidelines                      Despite these limitations, YOLO is a robust object
require tight data-sharing controls to protect patient confi-                   detection algorithm used in various applications. As the
dentiality, highlighting the challenge in medical research to                   algorithm develops, its accuracy and performance will likely
balance scientific progress with data privacy and protection                    improve Chaudhary et al. 2023, [128]. The best alternative
norms.                                                                          to YOLO will depend on the specific application. If speed
                                                                                is essential, then YOLO may be the best choice [23]. Faster
IV. SUMMARY                                                                     R-CNN or RetinaNet may be the best choice if accuracy is
This section summarizes this SLR into four sub-sections:                        critical. It is also essential to consider the size of the objects
the limitations of YOLO in healthcare (IV-A), future                            that need to be detected. YOLO is not as good at detecting
directions (IV-B), ethical considerations (IV-C), and the final                 small objects as more significant objects [50]. If small objects
conclusion (IV-D).                                                              must be detected, Faster R-CNN or RetinaNet may be better
                                                                                choices. Finally, it is essential to consider the diversity of the
A. LIMITATIONS OF YOLO IN HEALTHCARE                                            objects that need to be detected [129].
While YOLO has made notable strides in object detection,
it has inherent limitations [123]. The system leverages a one-
stage algorithm that directly predicts object bounding boxes                     B. FUTURE DIRECTIONS
and class probabilities from images, significantly improv-                      Developing YOLO variants specifically designed for health-
ing detection speed. YOLO backbones network structure                           care applications is another promising research direction.
excludes pooling and fully connected layers, instead accom-                     Such customized systems could cater to the unique demands
plishing image convolutional transformations by modifying                       of healthcare, resulting in more effective and efficient tools.
the step size of the convolutional core [124]. While this                       Integrating YOLO with other AI techniques, such as rein-
technique augments the network’s depth and ability to extract                   forcement learning and transfer learning, could significantly

VOLUME 12, 2024                                                                                                                             57829
                                                 M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 7. Data Sources of the selected studies.

57830                                                                                                                     VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

TABLE 7. (Continued.) Data Sources of the selected studies.

enhance its performance. Reinforcement learning could                               • Clinical Relevance: The dataset needs to be clinically
enable the system to learn from its errors, thereby continually                      relevant and accurately represent the challenges that
improving, while transfer learning would allow the applica-                          medical professionals face in real-world scenarios.
tion of knowledge acquired from one task to related tasks,                         Addressing these challenges requires collaboration
potentially boosting accuracy and efficiency [130]. Moreover,                   between medical professionals, data annotators, and machine
it will be interesting to see the potential applications of large               learning experts. Rigorous quality control, careful dataset
language models [131] in YOLO or object detection tasks.                        curation, and domain-specific adaptations of YOLO models
   Given YOLO’s success in medical imaging, future studies                      are essential for successful medical object detection.
are likely to concentrate on enhancing its accuracy for
small target detection and extending its application to other                   2) TRANSFER LEARNING FOR MEDICAL OBJECT DETECTION
healthcare areas, such as patient activity monitoring, real time                Transfer learning is a valuable technique that can signif-
anomaly detection during surgical procedures, or disease pro-                   icantly benefit the application of YOLO in the medical
gression prediction based on image data. Moreover, there is                     imaging domain. Here is how transfer learning can be
a growing interest in integrating YOLO more effectively into                    leveraged to improve YOLO’s performance:
clinical workflows. This could involve developing interfaces                       • Pre-Trained Models: Begin by training YOLO on a
for seamless interaction between healthcare professionals                            large dataset from a related domain, such as natural
and the system or devising protocols to ensure appropriate                           images. This pre-training imparts general object recog-
communication and utilization of the system’s outputs in                             nition capabilities to YOLO, capturing low-level fea-
clinical decision-making. This rapidly evolving field will                           tures that can be valuable for medical object detection.
continue to reveal novel applications, benefits, and limitations                   • Fine-Tuning: After pre-training, fine-tune the YOLO
of this technology.                                                                  model using a smaller but domain-specific medical
                                                                                     image dataset. This step adapts the model’s learned
                                                                                     features to the specific characteristics of medical
1) DEVELOPING NEW DATASETS FOR MEDICAL OBJECT                                        images, enhancing its ability to detect medical objects.
DETECTION                                                                          • Transfer of Knowledge: Transfer learning facilitates
Developing new datasets for medical object detection using                           the transfer of knowledge from the pre-trained model
YOLO models can be challenging due to several reasons:                               to the medical domain. This approach jumpstarts the
                                                                                     training process and reduces the amount of labeled
   • Data Privacy and Ethics: Medical data is sensitive and                          medical data required, a critical advantage in medical
      protected by strict privacy regulations.                                       imaging where labeled data is often limited.
   • Annotating Medical Images: Medical images often                               • Improved Convergence: Transfer learning allows the
     require precise and detailed annotations. Expert knowl-                         YOLO model to converge faster during fine-tuning,
     edge is needed to accurately label abnormalities, making                        leading to quicker deployment and reducing the risk
     annotation time-consuming and labor-intensive. The                              of overfitting, especially when working with smaller
     cost of annotating a large dataset can be significant.                          medical datasets.
   • Limited Data Availability: Unlike general object                              • Enhanced Feature Extraction: The pre-trained fea-
     detection, medical datasets are smaller due to the                              tures capture valuable information about edges, textures,
     limited availability of medical images, especially for                          and basic shapes. These features can be particularly
     rare conditions. This scarcity can affect the model’s                           beneficial in medical image analysis, aiding in the
     performance and generalization.                                                 detection of various anomalies.
   • Class Imbalance: Medical conditions are often rare,
     leading to a class imbalance where certain classes have                     C. ETHICAL CONSIDERATIONS
     very few instances. This can lead to biased models that                    As YOLO and similar technologies become more prevalent in
     perform poorly on underrepresented classes.                                healthcare, it is important to consider the ethical implications.
   • Complexity and Variability: Medical images can                             Implementing YOLO in healthcare elicits various ethical
     exhibit variations due to factors like lighting, equip-                    and legal quandaries. Issues such as data privacy, informed
     ment, patient demographics, and disease progression.                       consent, and the potential for bias in AI algorithms will need
     Capturing this variability in the dataset is crucial for                   to be addressed. Future research will need to not only focus
     robust model performance.                                                  on improving the technical aspects of these systems but also

VOLUME 12, 2024                                                                                                                            57831
                                                                   M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

ensure that they are used in a way that respects patient rights                    [2] Z. Li, M. Dong, S. Wen, X. Hu, P. Zhou, and Z. Zeng, ‘‘CLU-
and upholds the principles of medical ethics.                                          CNNs: Object detection for medical images,’’ Neurocomputing, vol. 350,
                                                                                       pp. 53–59, Jul. 2019.
                                                                                   [3] J. Peng, Q. Chen, L. Kang, H. Jie, and Y. Han, ‘‘Autonomous recognition
D. CONCLUSION                                                                          of multiple surgical instruments tips based on arrow OBB-YOLO
                                                                                       network,’’ IEEE Trans. Instrum. Meas., vol. 71, pp. 1–13, 2022.
To conclude, this SLR offers a comprehensive analysis of
                                                                                   [4] M. Loey, G. Manogaran, M. H. N. Taha, and N. E. M. Khalifa, ‘‘Fighting
the utilization of YOLO in various medical applications,                               against COVID-19: A novel deep learning model based on YOLO-v2 with
encompassing tumor detection, blood transfusion medicine,                              ResNet-50 for medical face mask detection,’’ Sustain. Cities Soc., vol. 65,
COVID-19, colorectal cancer, radiology, laryngeal cancer,                              Feb. 2021, Art. no. 102600.
                                                                                   [5] R. Yang and Y. Yu, ‘‘Artificial convolutional neural network in object
parathyroid surgery, and dorsal hand veins recognition,                                detection and semantic segmentation for medical imaging analysis,’’
among others. The review incorporated a significant body                               Frontiers Oncol., vol. 11, Mar. 2021, Art. no. 638182.
of literature, aggregating insights from 124 papers published                      [6] M. Tsuneki, ‘‘Deep learning models in medical image analysis,’’ J. Oral
                                                                                       Biosci., vol. 64, no. 3, pp. 312–320, Sep. 2022.
between 2018 and 2023. The findings reveal the pivotal role
                                                                                   [7] Y. Zhao, K. Zeng, Y. Zhao, P. Bhatia, M. Ranganath, M. L. Kozhikkavil,
YOLO plays in enhancing the efficiency and accuracy of                                 C. Li, and G. Hermosillo, ‘‘Deep learning solution for medical image
medical diagnoses and procedures.                                                      localization and orientation detection,’’ Med. Image Anal., vol. 81,
   The study also has a few limitations. In this study,                                Oct. 2022, Art. no. 102529.
                                                                                   [8] R. Qureshi, M. Irfan, H. Ali, A. Khan, A. S. Nittala, S. Ali, A. Shah,
we only focused on the Pubmed database, other databases                                T. M. Gondal, F. Sadak, Z. Shah, M. U. Hadi, S. Khan, Q. Al-Tashi,
may have relevant articles as well. However, in the medical                            J. Wu, A. Bermak, and T. Alam, ‘‘Artificial intelligence and biosensors
domain, Pubmed is considered as a gold standard. Another                               in healthcare and its clinical relevance: A review,’’ IEEE Access, vol. 11,
                                                                                       pp. 61600–61620, 2023.
limitation is that we considered object detection tasks only in
                                                                                   [9] Q. Al-Tashi, M. B. Saad, A. Muneer, R. Qureshi, S. Mirjalili,
medical images, personal protective equipment, and surgical                            A. Sheshadri, X. Le, N. I. Vokes, J. Zhang, and J. Wu, ‘‘Machine
procedures. Further medical instruments are not considered                             learning models for the identification of prognostic and predictive cancer
as medical objects.                                                                    biomarkers: A systematic review,’’ Int. J. Mol. Sci., vol. 24, no. 9, p. 7781,
                                                                                       Apr. 2023.
   By rapidly identifying and localizing ailments ranging                         [10] R. Qureshi, M. Irfan, T. M. Gondal, S. Khan, J. Wu, M. U. Hadi,
from tumors to various cancers, YOLO has significantly                                 J. Heymach, X. Le, H. Yan, and T. Alam, ‘‘AI in drug discovery and its
improved patient outcomes while reducing diagnosis and                                 clinical relevance,’’ Heliyon, vol. 9, no. 7, Jul. 2023, Art. no. e17575.
                                                                                  [11] T. Panch, H. Mattie, and L. A. Celi, ‘‘The ‘inconvenient truth’ about AI
treatment times. However, despite the remarkable successes                             in healthcare,’’ NPJ Digit. Med., vol. 2, no. 1, p. 77, 2019.
of YOLO, its deployment is not without challenges. These                          [12] R. Qureshi, B. Zou, T. Alam, J. Wu, V. H. F. Lee, and H. Yan,
include its sensitivity to object scale, difficulty in detecting                       ‘‘Computational methods for the analysis and prediction of EGFR-
small or occluded objects, and considerable computational                              mutated lung cancer drug resistance: Recent advances in drug design,
                                                                                       challenges and future prospects,’’ IEEE/ACM Trans. Comput. Biol.
resource requirements. To harness the full potential of YOLO,                          Bioinf., vol. 20, no. 1, pp. 238–255, Jan. 2023.
these issues need to be addressed by ongoing and future                           [13] Z. Zou, K. Chen, Z. Shi, Y. Guo, and J. Ye, ‘‘Object detection in 20 years:
research.                                                                              A survey,’’ Proc. IEEE, vol. 111, no. 3, pp. 257–276, Mar. 2023.
   Also, ethical considerations like data privacy and algorith-                   [14] M. Nawaz, R. Qureshi, M. A. Teevno, and A. R. Shahid, ‘‘Object
                                                                                       detection and segmentation by composition of fast fuzzy C-mean
mic bias need to be considered in the development of YOLO-                             clustering based maps,’’ J. Ambient Intell. Humanized Comput., vol. 14,
based systems, particularly in healthcare. In summary, the                             no. 6, pp. 7173–7188, Jun. 2023.
integration of YOLO into healthcare applications represents                       [15] Z.-Q. Zhao, P. Zheng, S.-T. Xu, and X. Wu, ‘‘Object detection with deep
                                                                                       learning: A review,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 30,
a significant stride towards a future where AI not only                                no. 11, pp. 3212–3232, Nov. 2019.
enhances the accuracy and speed of medical processes but                          [16] I. Krasin, T. Duerig, N. Alldrin, V. Ferrari, S. Abu-El-Haija,
also democratizes access to quality healthcare. Nevertheless,                          A. Kuznetsova, H. Rom, J. Uijlings, S. Popov, and A. Veit, ‘‘OpenImages:
                                                                                       A public dataset for large-scale multi-label and multi-class image
continued research and development are essential for further                           classification,’’ Dataset, vol. 2, no. 3, p. 18, 2017. [Online]. Available:
improvements and for the optimal integration of YOLO into                              https://github.com/openimages
healthcare settings.                                                              [17] M. A. Al-antari, S.-M. Han, and T.-S. Kim, ‘‘Evaluation of deep
                                                                                       learning detection and classification towards computer-aided diag-
                                                                                       nosis of breast lesions in digital X-ray mammograms,’’ Comput.
ACKNOWLEDGMENT                                                                         Methods Programs Biomed., vol. 196, 2020, Art. no. 105584, doi:
The authors would like to thank Ministry of Higher                                     10.1016/j.cmpb.2020.105584.
Education (MOHE), Malaysia for providing financial                                [18] Y. E. Almalki, A. I. Din, M. Ramzan, M. Irfan, K. M. Aamir,
                                                                                       A. Almalki, S. Alotaibi, G. Alaglan, H. A. Alshamrani, and S. Rahman,
assistance under Fundamental Research Grant Scheme                                     ‘‘Deep learning models for classification of dental diseases using
(FRGS/1/2022/ICT02/UTP/02/4) and Universiti Teknologi                                  orthopantomography X-ray OPG images,’’ Sensors, vol. 22, no. 19,
PETRONAS under the Yayasan Universiti Teknologi                                        p. 7370, Sep. 2022, doi: 10.3390/s22197370.
                                                                                  [19] A. Baccouche, B. Garcia-Zapirain, Y. Zheng, and A. S. Elmaghraby,
PETRONAS (YUTP-FRG/015LC0-308) for providing the                                       ‘‘Early detection and classification of abnormality in prior mammograms
required facilities to conduct this research work.                                     using image-to-image translation and YOLO techniques,’’ Comput.
                                                                                       Methods Programs Biomed., vol. 221, Jun. 2022, Art. no. 106884, doi:
                                                                                       10.1016/j.cmpb.2022.106884.
REFERENCES                                                                        [20] M. Dobrovolny, J. Benes, J. Langer, O. Krejcar, and A. Selamat,
  [1] A. Esteva, K. Chou, S. Yeung, N. Naik, A. Madani, A. Mottaghi, Y. Liu,           ‘‘Study on sperm-cell detection using YOLOv5 architecture with
      E. Topol, J. Dean, and R. Socher, ‘‘Deep learning-enabled medical                labaled dataset,’’ Genes, vol. 14, no. 2, p. 451, Feb. 2023, doi:
      computer vision,’’ NPJ Digit. Med., vol. 4, no. 1, p. 5, Jan. 2021.              10.3390/genes14020451.

57832                                                                                                                                              VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

 [21] Z. Han, H. Huang, Q. Fan, Y. Li, Y. Li, and X. Chen, ‘‘SMD-YOLO:               [40] I. Pacal, A. Karaman, D. Karaboga, B. Akay, A. Basturk, U. Nalbantoglu,
      An efficient and lightweight detection method for mask wearing status               and S. Coskun, ‘‘An efficient real-time colonic polyp detection
      during the COVID-19 pandemic,’’ Comput. Methods Programs Biomed.,                   with YOLO algorithms trained by using negative samples and large
      vol. 221, Jun. 2022, Art. no. 106888, doi: 10.1016/j.cmpb.2022.106888.              datasets,’’ Comput. Biol. Med., vol. 141, Feb. 2022, Art. no. 105031, doi:
 [22] Z. Huang, Y. Li, T. Zhao, P. Ying, Y. Fan, and J. Li, ‘‘Infusion port               10.1016/j.compbiomed.2021.105031.
      level detection for intravenous infusion based on YOLO v3 neural               [41] L. Tan, T. Huangfu, L. Wu, and W. Chen, ‘‘Comparison of RetinaNet,
      network,’’ Math. Biosciences Eng., vol. 18, no. 4, pp. 3491–3501, 2021,             SSD, and YOLO v3 for real-time pill identification,’’ BMC Med.
      doi: 10.3934/mbe.2021175.                                                           Informat. Decis. Making, vol. 21, no. 1, pp. 1–11, Dec. 2021.
 [23] T. Diwan, G. Anirudh, and J. V. Tembhurne, ‘‘Object detection using            [42] K. Li and L. Cao, ‘‘A review of object detection techniques,’’ in Proc.
      YOLO: Challenges, architectural successors, datasets and applications,’’            5th Int. Conf. Electromechanical Control Technol. Transp. (ICECTT),
      Multimedia Tools Appl., vol. 82, no. 6, pp. 9243–9275, Mar. 2023.                   May 2020, pp. 385–390.
 [24] W. Fang, L. Wang, and P. Ren, ‘‘Tinier-YOLO: A real-time object                [43] A. Kaur, Y. Singh, N. Neeru, L. Kaur, and A. Singh, ‘‘A survey on deep
      detection method for constrained environments,’’ IEEE Access, vol. 8,               learning approaches to medical images and a systematic look up into
      pp. 1935–1944, 2020.                                                                real-time object detection,’’ Arch. Comput. Methods Eng., vol. 29, no. 4,
 [25] P. Jiang, D. Ergu, F. Liu, Y. Cai, and B. Ma, ‘‘A review of YOLO algorithm          pp. 2071–2111, Jun. 2022.
      developments,’’ Proc. Comput. Sci., vol. 199, pp. 1066–1073, Jan. 2022.        [44] N. Ganatra, ‘‘A comprehensive study of applying object detection
 [26] M. J. Mortada, S. Tomassini, H. Anbar, M. Morettini, L. Burattini, and              methods for medical image analysis,’’ in Proc. 8th Int. Conf. Comput.
      A. Sbrollini, ‘‘Segmentation of anatomical structures of the left heart from        Sustain. Global Develop. (INDIACom), Mar. 2021, pp. 821–826.
      echocardiographic images using deep learning,’’ Diagnostics, vol. 13,          [45] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, ‘‘You only look once:
      no. 10, p. 1683, May 2023.                                                          Unified, real-time object detection,’’ in Proc. IEEE Conf. Comput. Vis.
                                                                                          Pattern Recognit. (CVPR), Jun. 2016, pp. 779–788.
 [27] P. Zeng, S. Liu, S. He, Q. Zheng, J. Wu, Y. Liu, G. Lyu, and P. Liu,
      ‘‘TUSPM-NET: A multi-task model for thyroid ultrasound standard plane          [46] S. Albawi, T. A. Mohammed, and S. Al-Zawi, ‘‘Understanding of a
      recognition and detection of key anatomical structures of the thyroid,’’            convolutional neural network,’’ in Proc. Int. Conf. Eng. Technol. (ICET),
      Comput. Biol. Med., vol. 163, Sep. 2023, Art. no. 107069.                           Aug. 2017, pp. 1–6.
                                                                                     [47] M. G. Ragab, S. J. Abdulkadir, and N. Aziz, ‘‘Random search one
 [28] A. Baccouche, B. Garcia-Zapirain, C. C. Olea, and A. S. Elmaghraby,
                                                                                          dimensional CNN for human activity recognition,’’ Int. Conf. Comput.
      ‘‘Breast lesions detection and classification via YOLO-based fusion
                                                                                          Intell. (ICCI), pp. 86–91, Oct. 2020.
      models,’’ Comput., Mater. Continua, vol. 69, no. 1, pp. 1407–1425, 2021.
                                                                                     [48] M. Hussain, ‘‘YOLO-v1 to YOLO-v8, the rise of YOLO and its
 [29] C. Santos, M. Aguiar, D. Welfer, and B. Belloni, ‘‘A new approach for
                                                                                          complementary nature toward digital manufacturing and industrial defect
      detecting fundus lesions using image processing and deep neural network
                                                                                          detection,’’ Machines, vol. 11, no. 7, p. 677, Jun. 2023.
      architecture based on YOLO model,’’ Sensors, vol. 22, no. 17, p. 6441,
                                                                                     [49] C. Chen, Z. Zheng, T. Xu, S. Guo, S. Feng, W. Yao, and Y. Lan, ‘‘YOLO-
      Aug. 2022.
                                                                                          based UAV technology: A review of the research and its applications,’’
 [30] F. J. P. Montalbo, ‘‘A computer-aided diagnosis of brain tumors using
                                                                                          Drones, vol. 7, no. 3, p. 190, Mar. 2023.
      a fine-tuned YOLO-based model with transfer learning,’’ KSII Trans.
                                                                                     [50] J. Terven and D. Cordova-Esparza, ‘‘A comprehensive review of YOLO
      Internet Inf. Syst., vol. 14, no. 12, pp. 4816–4834, 2020.
                                                                                          architectures in computer vision: From YOLOv1 to YOLOv8 and YOLO-
 [31] R. Rong, H. Sheng, K. W. Jin, F. Wu, D. Luo, Z. Wen, C. Tang,                       NAS,’’ 2023, arXiv:2304.00501.
      D. M. Yang, L. Jia, M. Amgad, L. A. D. Cooper, Y. Xie, X. Zhan,                [51] L. Aziz, M. S. B. Haji Salam, U. U. Sheikh, and S. Ayub, ‘‘Exploring deep
      S. Wang, and G. Xiao, ‘‘A deep learning approach for histology-based                learning-based architecture, strategies, applications and current trends in
      nucleus segmentation and tumor microenvironment characterization,’’                 generic object detection: A comprehensive review,’’ IEEE Access, vol. 8,
      Modern Pathol., vol. 36, no. 8, Aug. 2023, Art. no. 100196, doi:                    pp. 170461–170495, 2020.
      10.1016/j.modpat.2023.100196.
                                                                                     [52] P. Bharati and A. Pramanik, ‘‘Deep learning techniques—R-CNN to
 [32] M. Safdar, S. Kobaisi, and F. Zahra, ‘‘A comparative analysis of data               mask R-CNN: A survey,’’ in Computational Intelligence in Pattern
      augmentation approaches for magnetic resonance imaging (MRI) scan                   Recognition. Singapore: Springer, 2020, pp. 657–668.
      images of brain tumor,’’ Acta Inf. Medica, vol. 28, no. 1, p. 29, 2020, doi:   [53] C. Yu, Z. Hu, R. Li, X. Xia, Y. Zhao, X. Fan, and Y. Bai, ‘‘Segmentation
      10.5455/aim.2020.28.29-36.                                                          and density statistics of mariculture cages from remote sensing images
 [33] J. Zhou, B. Zhang, X. Yuan, C. Lian, L. Ji, Q. Zhang, and J. Yue, ‘‘YOLO-           using mask R-CNN,’’ Inf. Process. Agricult., vol. 9, no. 3, pp. 417–430,
      CIR: The network based on YOLO and ConvNeXt for infrared object                     Sep. 2022.
      detection,’’ Infr. Phys. Technol., vol. 131, Jun. 2023, Art. no. 104703.       [54] Y. Cao, D. Pang, Y. Yan, Y. Jiang, and C. Tian, ‘‘A photovoltaic surface
 [34] S. Bashir, R. Qureshi, A. Shah, X. Fan, and T. Alam, ‘‘YOLOv5-M:                    defect detection method for building based on deep learning,’’ J. Building
      A deep neural network for medical object detection in real-time,’’ in               Eng., vol. 70, Jul. 2023, Art. no. 106375.
      Proc. IEEE Symp. Ind. Electron. Appl. (ISIEA), Jul. 2023, pp. 1–6, doi:        [55] R. Kaur and S. Singh, ‘‘A comprehensive review of object detection
      10.1109/ISIEA58478.2023.10212322.                                                   with deep learning,’’ Digit. Signal Process., vol. 132, Jan. 2023,
 [35] H. M. Ali and N. K. El Abbadi, ‘‘Optic disc localization in retinal fundus          Art. no. 103812.
      images based on you only look once network (YOLO),’’ Int. J. Intell. Eng.      [56] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and S.
      Syst., vol. 16, no. 2, pp. 1–11, 2023.                                              Belongie, ‘‘Feature pyramid networks for object detection,’’ in Proc.
 [36] J. Liang, Z. Wang, and X. Ye, ‘‘Application of deep learning in imaging             IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017,
      diagnosis of brain diseases,’’ in Proc. 3rd Int. Conf. Mach. Learn., Big            pp. 936–944.
      Data Bus. Intell. (MLBDBI), Dec. 2021, pp. 166–175.                            [57] F. Iandola, M. Moskewicz, S. Karayev, R. Girshick, T. Darrell, and
 [37] H. Honda, S. Mori, A. Watanabe, N. Sasagasako, S. Sadashima, T.                     K. Keutzer, ‘‘DenseNet: Implementing efficient ConvNet descriptor
      Dong, K. Satoh, N. Nishida, and T. Iwaki, ‘‘Abnormal prion protein                  pyramids,’’ 2014, arXiv:1404.1869.
      deposits with high seeding activities in the skeletal muscle, femoral nerve,   [58] M. G. Ragab, S. J. Abdulkadir, N. Aziz, Q. Al-Tashi, Y. Alyousifi,
      and scalp of an autopsied case of sporadic Creutzfeldt–Jakob disease,’’             H. Alhussian, and A. Alqushaibi, ‘‘A novel one-dimensional CNN
      Neuropathology, vol. 41, no. 2, pp. 152–158, Apr. 2021.                             with exponential adaptive gradients for air pollution index prediction,’’
 [38] Z. Zhuang, G. Liu, W. Ding, A. N. J. Raj, S. Qiu, J. Guo,                           Sustainability, vol. 12, no. 23, p. 10090, Dec. 2020.
      and Y. Yuan, ‘‘Cardiac VFM visualization and analysis based on                 [59] A. B. Amjoud and M. Amrouch, ‘‘Object detection using deep learning,
      YOLO deep learning model and modified 2D continuity equation,’’                     CNNs and vision transformers: A review,’’ IEEE Access, vol. 11,
      Comput. Med. Imag. Graph., vol. 82, 2020, Art. no. 101732, doi:                     pp. 35479–35516, 2023.
      10.1016/j.compmedimag.2020.101732.                                             [60] W. Chen, Y. Li, Z. Tian, and F. Zhang, ‘‘2D and 3D object detection
 [39] K. K. Wong, M. Ayoub, Z. Cao, C. Chen, W. Chen, D. N. Ghista,                       algorithms from images: A survey,’’ Array, vol. 19, Sep. 2023,
      and C. W. J. Zhang, ‘‘The synergy of cybernetical intelligence with                 Art. no. 100305.
      medical image analysis for deep medicine: A methodological per-                [61] S. S. A. Zaidi, M. S. Ansari, A. Aslam, N. Kanwal, M. Asghar, and B. Lee,
      spective,’’ Comput. Methods Programs Biomed., vol. 240, Oct. 2023,                  ‘‘A survey of modern deep learning based object detection models,’’ Digit.
      Art. no. 107677.                                                                    Signal Process., vol. 126, Jun. 2022, Art. no. 103514.

VOLUME 12, 2024                                                                                                                                               57833
                                                                         M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

[62] X. Cong, S. Li, F. Chen, C. Liu, and Y. Meng, ‘‘A review of YOLO object            [84] A. A. T. Zade, M. J. Aziz, H. Majedi, A. Mirbagheri, and A. Ahmadian,
     detection algorithms based on deep learning,’’ Frontiers Comput. Intell.                ‘‘Spatiotemporal analysis of speckle dynamics to track invisible needle
     Syst., vol. 4, no. 2, pp. 17–20, Jun. 2023.                                             in ultrasound sequences using convolutional neural networks: A phantom
[63] A.-A. Tulbure, A.-A. Tulbure, and E.-H. Dulf, ‘‘A review on modern                      study,’’ Int. J. Comput. Assist. Radiol. Surgery, vol. 18, no. 8,
     defect detection models using DCNNs—Deep convolutional neural                           pp. 1373–1382, Feb. 2023, doi: 10.1007/s11548-022-02812-y.
     networks,’’ J. Adv. Res., vol. 35, pp. 33–48, Jan. 2022.                           [85] M. Mushtaq, M. U. Akram, N. S. Alghamdi, J. Fatima, and R. F. Masood,
[64] N.-N. Dao, T.-H. Do, S. Cho, and S. Dustdar, ‘‘Information revealed by                  ‘‘Localization and edge-based segmentation of lumbar spine vertebrae to
     vision: A review on the next-generation OCC standard for AIoV,’’ IT                     identify the deformities using deep learning models,’’ Sensors, vol. 22,
     Prof., vol. 24, no. 4, pp. 58–65, Jul. 2022.                                            no. 4, p. 1547, Feb. 2022, doi:10.3390/s22041547.
[65] S. Gupta and S. Nair, ‘‘A review of the emerging role of UAVs in                   [86] Y. Ahmadyar, A. Kamali-Asl, H. Arabi, R. Samimi, and H. Zaidi,
     construction site safety monitoring,’’ Mater. Today, Proc., 2023, doi:                  ‘‘Hierarchical approach for pulmonary-nodule identification from CT
     10.1016/j.matpr.2023.03.135.                                                            images using YOLO model and a 3D neural network classifier,’’
[66] Y. Wang, H. Wang, and Z. Xin, ‘‘Efficient detection model of steel                      Radiological Phys. Technol., vol. 17, no. 1, pp. 124–134, Mar. 2024, doi:
     strip surface defects based on YOLO-V7,’’ IEEE Access, vol. 10,                         10.1007/s12194-023-00756-9.
     pp. 133936–133944, 2022.                                                           [87] Y.-S. Huang, P.-R. Chou, H.-M. Chen, Y.-C. Chang, and R.-F.
[67] L. Cao, X. Zheng, and L. Fang, ‘‘The semantic segmentation of standing                  Chang, ‘‘One-stage pulmonary nodule detection using 3-D DCNN
     tree images based on the YOLO v7 deep learning algorithm,’’ Electronics,                with feature fusion and attention mechanism in CT image,’’ Comput.
     vol. 12, no. 4, p. 929, Feb. 2023.                                                      Methods Programs Biomed., vol. 220, Jun. 2022, Art. no. 106786, doi:
[68] G. Jocher, A. Chaurasia, and J. Qiu. (2023). Ultralytics YOLOv8.                        10.1016/j.cmpb.2022.106786.
     [Online]. Available: https://github.com/ultralytics/ultralytics                    [88] C. Liu, S.-C. Hu, C. Wang, K. Lafata, and F.-F. Yin, ‘‘Automatic detection
                                                                                             of pulmonary nodules on CT images with YOLOv3: Development and
[69] S. Aharon, Louis-Dupont, O. Masad, K. Yurkova, L. Fridman,
                                                                                             evaluation using simulated and patient data,’’ Quant. Imag. Med. Surg.,
     E. Khvedchenya, R. Rubin, N. Bagrov, B. Tymchenko, T. Keren, and
                                                                                             vol. 10, no. 10, pp. 1917–1929, Oct. 2020, doi: 10.21037/qims-19-883.
     A. Zhilko, ‘‘Super-gradients,’’ Tech. Rep., 2021, doi: 10.5281/ZEN-
                                                                                        [89] G. H. Aly, M. Marey, S. A. El-Sayed, and M. F. Tolba, ‘‘YOLO based
     ODO.7789328.
                                                                                             breast masses detection and classification in full-field digital mammo-
[70] D. Zhang, M. M. Islam, and G. Lu, ‘‘A review on automatic image
                                                                                             grams,’’ Comput. Methods Programs Biomed., vol. 200, Mar. 2021,
     annotation techniques,’’ Pattern Recognit., vol. 45, no. 1, pp. 346–362,
                                                                                             Art. no. 105823, doi: 10.1016/j.cmpb.2020.105823.
     Jan. 2012.
                                                                                        [90] Y. Su, Q. Liu, W. Xie, and P. Hu, ‘‘YOLO-LOGO: A transformer-based
[71] C. Sager, C. Janiesch, and P. Zschech, ‘‘A survey of image labelling for
                                                                                             YOLO segmentation model for breast mass detection and segmentation
     computer vision applications,’’ J. Bus. Analytics, vol. 4, no. 2, pp. 91–110,
                                                                                             in digital mammograms,’’ Comput. Methods Programs Biomed., vol. 221,
     Jul. 2021.
                                                                                             Jun. 2022, Art. no. 106903, doi: 10.1016/j.cmpb.2022.106903.
[72] A. Kumar, A. Kalia, K. Verma, A. Sharma, and M. Kaushal, ‘‘Scaling up
                                                                                        [91] Q. Fu and H. Dong, ‘‘Spiking neural network based on multi-scale
     face masks detection with YOLO on a novel dataset,’’ Optik, vol. 239,
                                                                                             saliency fusion for breast cancer detection,’’ Entropy, vol. 24, no. 11,
     Aug. 2021, Art. no. 166744.
                                                                                             p. 1543, Oct. 2022, doi: 10.3390/e24111543.
[73] S. Annadatha, M. Fridberg, S. Kold, O. Rahbek, and M. Shen, ‘‘A tool for           [92] Y. Ku, H. Ding, and G. Wang, ‘‘Efficient synchronous real-time
     thermal image annotation and automatic temperature extraction around                    CADe for multicategory lesions in gastroscopy by using multiclass
     orthopedic pin sites,’’ in Proc. IEEE 5th Int. Conf. Image Process. Appl.               detection model,’’ BioMed Res. Int., vol. 2022, pp. 1–9, Aug. 2022, doi:
     Syst. (IPAS), vol. Five, Dec. 2022, pp. 1–5.                                            10.1155/2022/8504149.
[74] A. Dutta, A. Gupta, and A. Zissermann. (2316). Vgg Image Annotator                 [93] D.-C. Cheng, T.-C. Hsieh, K.-Y. Yen, and C.-H. Kao, ‘‘Lesion-based bone
     (Via). [Online]. Available: http://www.robots.ox.ac.uk/~vgg/software/via                metastasis detection in chest bone scintigraphy images of prostate cancer
[75] F. Ciaglia, F. Saverio Zuppichini, P. Guerrie, M. McQuade, and                          patients using pre-train, negative mining, and deep learning,’’ Diagnos-
     J. Solawetz, ‘‘Roboflow 100: A rich, multi-domain object detection                      tics, vol. 11, no. 3, p. 518, Mar. 2021, doi: 10.3390/diagnostics11030518.
     benchmark,’’ 2022, arXiv:2211.13523.                                               [94] S. Li, Y. Li, J. Yao, B. Chen, J. Song, Q. Xue, and X. Yang, ‘‘Label-free
[76] Y. Hu, X. Wu, G. Zheng, and X. Liu, ‘‘Object detection of UAV for anti-                 classification of dead and live colonic adenocarcinoma cells based on 2D
     UAV based on improved YOLO v3,’’ in Proc. Chin. Control Conf. (CCC),                    light scattering and deep learning analysis,’’ Cytometry A, vol. 99, no. 11,
     Jul. 2019, pp. 8386–8390.                                                               pp. 1134–1142, Nov. 2021, doi: 10.1002/cyto.a.24475.
[77] Y. Jamtsho, P. Riyamongkol, and R. Waranusast, ‘‘Real-time bhutanese               [95] N. Larpant, W. Niamsi, J. Noiphung, W. Chanakiat, T. Sakuldamrong-
     license plate localization using YOLO,’’ ICT Exp., vol. 6, no. 2,                       panich, V. Kittichai, T. Tongloy, S. Chuwongin, S. Boonsang, and
     pp. 121–124, Jun. 2020.                                                                 W. Laiwattanapaisal, ‘‘Simultaneous phenotyping of five RH red blood
[78] M. J. Page, ‘‘The PRISMA 2020 statement: An updated guideline for                       cell antigens on a paper-based analytical device combined with deep
     reporting systematic reviews,’’ Systematic Rev., vol. 10, no. 1, p. 89,                 learning for rapid and accurate interpretation,’’ Analytica Chim. Acta,
     Dec. 2021, doi: 10.1186/s13643-021-01626-4.                                             vol. 1207, May 2022, Art. no. 339807, doi: 10.1016/j.aca.2022.339807.
[79] M. A. Al-Antari, M. A. Al-Masni, and T. S. Kim, ‘‘Deep learning                    [96] Z. Han, H. Huang, D. Lu, Q. Fan, C. Ma, X. Chen, Q. Gu, and
     computer-aided diagnosis for breast lesion in digital mammogram,’’ in                   Q. Chen, ‘‘One-stage and lightweight CNN detection approach with
     Deep Learning in Medical Image Analysis, vol. 1213, 2020, pp. 59–72.                    attention: Application to WBC detection of microscopic images,’’
     10.1007/978-3-030-33128-3_4.                                                            Comput. Biol. Med., vol. 154, Mar. 2023, Art. no. 106606, doi:
[80] L. Guo, Y. Yang, H. Ding, H. Zheng, H. Yang, J. Xie, Y. Li, T. Lin, and                 10.1016/j.compbiomed.2023.106606.
     Y. Ge, ‘‘A deep learning-based hybrid artificial intelligence model for the        [97] M.-Y. Quan, Y.-X. Huang, C.-Y. Wang, Q. Zhang, C. Chang, and
     detection and severity assessment of vitiligo lesions,’’ Ann. Transl. Med.,             S.-C. Zhou, ‘‘Deep learning radiomics model based on breast ultrasound
     vol. 10, no. 10, p. 590, 2022, doi: 10.21037/atm-22-1738.                               video to predict HER2 expression status,’’ Frontiers Endocrinology,
[81] S. Afshari, A. BenTaieb, and G. Hamarneh, ‘‘Automatic local-                            vol. 14, Apr. 2023, Art. no. 1144812, doi: 10.3389/fendo.2023.1144812.
     ization of normal active organs in 3D PET scans,’’ Computer-                       [98] R. Zhu, Y. Cui, J. Huang, E. Hou, J. Zhao, Z. Zhou, and H. Li,
     ized Med. Imag. Graph., vol. 70, pp. 111–118, Dec. 2018, doi:                           ‘‘YOLOv5s-SA: Light-weighted and improved YOLOv5s for sperm
     10.1016/j.compmedimag.2018.09.008.                                                      detection,’’ Diagnostics, vol. 13, no. 6, p. 1100, Mar. 2023, doi:
[82] Y. Huang, J. Li, X. Zhang, K. Xie, J. Li, Y. Liu, C. S. H. Ng,                          10.3390/diagnostics13061100.
     P. W. Y. Chiu, and Z. Li, ‘‘A surgeon preference-guided autonomous                 [99] G. Sun, C. Lyu, R. Cai, C. Yu, H. Sun, K. E. Schriver, L. Gao, and X. Li,
     instrument tracking method with a robotic flexible endoscope based on                   ‘‘DeepBhvTracking: A novel behavior tracking method for laboratory
     dVRK platform,’’ IEEE Robot. Autom. Lett., vol. 7, no. 2, pp. 2250–2257,                animals based on deep learning,’’ Frontiers Behav. Neurosci., vol. 15,
     Apr. 2022.                                                                              Oct. 2021, Art. no. 750894, doi: 10.3389/fnbeh.2021.750894.
[83] B. Wang, J. Zheng, J. Yu, S. Lin, S. Yan, L. Zhang, S. Wang, S. Cai,              [100] Z.-J. Huang, B. Patel, W.-H. Lu, T.-Y. Yang, W.-C. Tung, V. Bučinskas,
     A. H. A. Ahmed, L. Lin, F. Chen, G. W. Randolph, and W. Zhao,                           M. Greitans, Y.-W. Wu, and P. T. Lin, ‘‘Yeast cell detection using
     ‘‘Development of artificial intelligence for parathyroid recognition                    fuzzy automatic contrast enhancement (FACE) and you only look
     during endoscopic thyroid surgery,’’ Laryngoscope, vol. 132, no. 12,                    once (YOLO),’’ Sci. Rep., vol. 13, no. 1, p. 16222, Sep. 2023, doi:
     pp. 2516–2523, Dec. 2022, doi: 10.1002/lary.30173.                                      10.1038/s41598-023-43452-9.

57834                                                                                                                                                   VOLUME 12, 2024
M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

[101] Y.-F. Chen, Z.-J. Chen, Y.-Y. Lin, Z.-Q. Lin, C.-N. Chen, M.-L. Yang,         [117] T. Ma, Z. Ma, X. Zhang, and F. Zhou, ‘‘Evaluation of effect of
      J.-Y. Zhang, Y.-Z. Li, Y. Wang, and Y.-H. Huang, ‘‘Stroke risk study                curcumin on psychological state of patients with pulmonary hyper-
      based on deep learning-based magnetic resonance imaging carotid plaque              tension by magnetic resonance image under deep learning,’’ Contrast
      automatic segmentation algorithm,’’ Frontiers Cardiovascular Med.,                  Media Mol. Imag., vol. 2021, pp. 1–10, Jul. 2021, doi: 10.1155/2021/
      vol. 10, Feb. 2023, Art. no. 1101765, doi: 10.3389/fcvm.2023.1101765.               9935754.
[102] M. A. Al-masni, W.-R. Kim, E. Y. Kim, Y. Noh, and D.-H. Kim,                  [118] K.-C. Lee, Y. Cho, K.-S. Ahn, H.-J. Park, Y.-S. Kang, S. Lee, D. Kim, and
      ‘‘Automated detection of cerebral microbleeds in MR images: A two-                  C. H. Kang, ‘‘Deep-learning-based automated rotator cuff tear screening
      stage deep learning approach,’’ NeuroImage, Clin., vol. 28, Apr. 2020,              in three planes of shoulder MRI,’’ Diagnostics, vol. 13, no. 20, p. 3254,
      Art. no. 10246410.1016/j.nicl.2020.102464.                                          Oct. 2023, doi: 10.3390/diagnostics13203254.
[103] Y. Nambu, T. Mariya, S. Shinkai, M. Umemoto, H. Asanuma, I. Sato,             [119] J. Fu, J.-W. Chai, P.-L. Chen, Y.-W. Ding, and H.-C. Chen, ‘‘Quan-
      Y. Hirohashi, T. Torigoe, Y. Fujino, and T. Saito, ‘‘A screening assistance         titative measurement of spinal cerebrospinal fluid by cascade arti-
      system for cervical cytology of squamous cell atypia based on a two-step            ficial intelligence models in patients with spontaneous intracranial
      combined CNN algorithm with label smoothing,’’ Cancer Med., vol. 11,                hypotension,’’ Biomedicines, vol. 10, no. 8, p. 2049, Aug. 2022, doi:
      no. 2, pp. 520–529, Jan. 2022, doi: 10.1002/cam4.4460.                              10.3390/biomedicines10082049.
[104] A. Boonrod, A. Boonrod, A. Meethawolgul, and P. Twinprai, ‘‘Diagnostic        [120] B. Lv, L. Wu, T. Huangfu, J. He, W. Chen, and L. Tan, ‘‘Traditional
      accuracy of deep learning for evaluation of C-spine injury from lateral             Chinese medicine recognition based on target detection,’’ Evidence-
      neck radiographs,’’ Heliyon, vol. 8, no. 8, Aug. 2022, Art. no. e10372,             Based Complementary Alternative Med., vol. 2022, pp. 1–9, Jul. 2022,
      doi: 10.1016/j.heliyon.2022.e10372.                                                 doi: 10.1155/2022/9220443.
[105] C.-P. Tang, C.-H. Hsieh, and T.-L. Lin, ‘‘Computer-aided image                [121] T. Till, S. Tschauner, G. Singer, K. Lichtenegger, and H. Till, ‘‘Devel-
      enhanced endoscopy automated system to boost polyp and adenoma                      opment and optimization of AI algorithms for wrist fracture detection in
      detection accuracy,’’ Diagnostics, vol. 12, no. 4, p. 968, Apr. 2022, doi:          children using a freely available dataset,’’ Frontiers Pediatrics, vol. 11,
      10.3390/diagnostics12040968.                                                        Dec. 2023, Art. no. 1291804, doi: 10.3389/fped.2023.1291804.
[106] H. Matsui, S. Kamba, H. Horiuchi, S. Takahashi, M. Nishikawa,                 [122] F. Varçın, H. Erbay, E. Çetin, I. Çetin, and T. Kültü, ‘‘End-to-end
      A. Fukuda, A. Tonouchi, N. Kutsuna, Y. Shimahara, N. Tamai, and                     computerized diagnosis of spondylolisthesis using only lumbar X-rays,’’
      K. Sumiyama, ‘‘Detection accuracy and latency of colorectal lesions                 J. Digit. Imag., vol. 34, no. 1, pp. 85–95, Feb. 2021, doi: 10.1007/s10278-
      with computer-aided detection system based on low-bias evaluation,’’                020-00402-5.
      Diagnostics, vol. 11, no. 10, p. 1922, Oct. 2021, doi: 10.3390/diagnos-       [123] G. Oreski, ‘‘YOLO*C—Adding context improves YOLO performance,’’
      tics11101922.                                                                       Neurocomputing, vol. 555, Oct. 2023, Art. no. 126655.
[107] C.-P. Tang, H.-Y. Chang, W.-C. Wang, and W.-X. Hu, ‘‘A novel computer-        [124] M. Baghbanbashi, M. Raji, and B. Ghavami, ‘‘Quantizing YOLOv7: A
      aided detection/diagnosis system for detection and classification of                comprehensive study,’’ in Proc. 28th Int. Comput. Conf., Comput. Soc.
      polyps in colonoscopy,’’ Diagnostics, vol. 13, no. 2, p. 170, Jan. 2023,            Iran (CSICC), Iran, Jan. 2023, pp. 1–5.
      doi: 10.3390/diagnostics13020170.                                             [125] M. Hu, Z. Li, J. Yu, X. Wan, H. Tan, and Z. Lin, ‘‘Efficient-lightweight
[108] T. Ozturk, M. Talo, E. A. Yildirim, U. B. Baloglu, O. Yildirim,                     YOLO: Improving small object detection in YOLO for aerial images,’’
      and U. R. Acharya, ‘‘Automated detection of COVID-19 cases using                    Sensors, vol. 23, no. 14, p. 6423, Jul. 2023.
      deep neural networks with X-ray images,’’ Comput. Biol. Med.,                 [126] B. Aldughayfiq, F. Ashfaq, N. Z. Jhanjhi, and M. Humayun, ‘‘YOLO-
      vol. 121, Jun. 2020, Art. no. 103792, doi: 10.1016/j.compbiomed.2020.               based deep learning model for pressure ulcer detection and classifica-
      103792.                                                                             tion,’’ Healthcare, vol. 11, no. 9, p. 1222, Apr. 2023.
[109] Z. Kong, H. Ouyang, Y. Cao, T. Huang, E. Ahn, M. Zhang, and                   [127] H. Ghabri, W. Fathallah, M. Hamroun, S. B. Othman, H. Bellali, H. Sakli,
      H. Liu, ‘‘Automated periodontitis bone loss diagnosis in panoramic                  and M. N. Abdelkrim, ‘‘AI-enhanced thyroid detection using YOLO to
      radiographs using a bespoke two-stage detector,’’ Comput. Biol. Med.,               empower healthcare professionals,’’ in Proc. IEEE Int. Workshop Mech.
      vol. 152, Jan. 2023, Art. no. 106374, doi: 10.1016/j.compbiomed.2022.               Syst. Supervision (IW_MSS), Nov. 2023, pp. 1–6.
      106374.                                                                       [128] D. Chaudhary, A. Mathur, A. Chauhan, and A. Gupta, ‘‘Assistive object
[110] W. Panyarak, K. Wantanajittikul, A. Charuakkra, S. Prapayasatok, and                recognition and obstacle detection system for the visually impaired
      W. Suttapak, ‘‘Enhancing caries detection in bitewing radiographs using             using YOLO,’’ in Proc. 13th Int. Conf. Cloud Comput., Data Sci. Eng.
      YOLOv7,’’ J. Digit. Imag., vol. 36, no. 6, pp. 2635–2647, Dec. 2023, doi:           (Confluence), Jan. 2023, pp. 353–358.
      10.1007/s10278-023-00871-4.                                                   [129] B. Wu, C. Pang, X. Zeng, and X. Hu, ‘‘ME-YOLO: Improved YOLOv5
[111] Y. Tian, D. Zhao, and T. Wang, ‘‘An improved YOLO nano model for                    for detecting medical personal protective equipment,’’ Appl. Sci., vol. 12,
      dorsal hand vein detection system,’’ Med. Biol. Eng. Comput., vol. 60,              no. 23, p. 11978, Nov. 2022.
      no. 5, pp. 1225–1237, May 2022, doi: 10.1007/s11517-022-02551-x.              [130] N. Andrade, T. Ribeiro, J. Coelho, G. Lopes, and A. Ribeiro, ‘‘Combining
[112] S. Pang, T. Ding, S. Qiao, F. Meng, S. Wang, P. Li, and X. Wang, ‘‘A novel          YOLO and deep reinforcement learning for autonomous driving in public
      YOLOv3-arch model for identifying cholelithiasis and classifying                    roadworks scenarios,’’ in Proc. 14th Int. Conf. Agents Artif. Intell., 2022,
      gallstones on CT images,’’ PLoS ONE, vol. 14, no. 6, Jun. 2019,                     pp. 793–800.
      Art. no. e0217647, doi: 10.1371/journal.pone.0217647.                         [131] M. U. Hadi, R. Qureshi, A. Shah, M. Irfan, A. Zafar, M. B. Shaikh,
[113] M. A. Azam, C. Sampieri, A. Ioppi, S. Africano, A. Vallin, D.                       N. Akhtar, J. Wu, and S. Mirjalili, ‘‘Large language models: A com-
      Mocellin, M. Fragale, L. Guastini, S. Moccia, C. Piazza, L. S. Mattos,              prehensive survey of its applications, challenges, limitations, and future
      and G. Peretti, ‘‘Deep learning applied to white light and narrow                   prospects,’’ Tech. Rep., 2023, doi: 10.36227/techrxiv.23589741.v4.
      band imaging videolaryngoscopy: Toward real-time laryngeal cancer
      detection,’’ Laryngoscope, vol. 132, no. 9, pp. 1798–1806, Sep. 2022, doi:
      10.1002/lary.29960.
[114] J.-Y. Tsai, I. Y.-J. Hung, Y. L. Guo, Y.-K. Jan, C.-Y. Lin, T. T.-F. Shih,
      B.-B. Chen, and C.-W. Lung, ‘‘Lumbar disc herniation automatic                                          MOHAMMED GAMAL RAGAB received the
      detection in magnetic resonance imaging based on deep learning,’’                                       Bachelor of Science degree in software engineer-
      Frontiers Bioeng. Biotechnol., vol. 9, Aug. 2021, Art. no. 708137, doi:                                 ing from Universiti Teknologi PETRONAS in
      10.3389/fbioe.2021.708137.                                                                              2019, following the completion of his undergradu-
[115] B. Zhang, J. Li, Y. Bai, Q. Jiang, B. Yan, and Z. Wang, ‘‘An improved
                                                                                                              ate degree, he continued his studies at Universiti
      microaneurysm detection model based on SwinIR and YOLOv8,’’
      Bioengineering, vol. 10, no. 12, p. 1405, Dec. 2023, doi: 10.3390/bio-
                                                                                                              Teknologi PETRONAS, pursuing the master’s
      engineering10121405.                                                                                    degree by research in machine learning. Currently,
[116] P. Rouzrokh, T. Ramazanian, C. C. Wyles, K. A. Philbrick, J. C. Cai,                                    he is continuing his academic pursuits by pursuing
      M. J. Taunton, H. M. Kremers, D. G. Lewallen, and B. J. Erickson, ‘‘Deep                                the Ph.D. degree in information technology with
      learning artificial intelligence model for assessment of hip dislocation                                Universiti Teknologi PETRONAS. His ongoing
      risk following primary total hip arthroplasty from postoperative radio-       research builds on his previous work, focusing on the development of new
      graphs,’’ J. Arthroplasty, vol. 36, no. 6, pp. 2197–2203, Jun. 2021, doi:     and innovative techniques for optimizing the performance of deep learning
      10.1016/j.arth.2021.02.028.                                                   models.

VOLUME 12, 2024                                                                                                                                                57835
                                                                      M. G. Ragab et al.: Comprehensive Systematic Review of YOLO for Medical Object Detection

                           SAID JADID ABDULKADIR (Senior Member,                                               RIZWAN QURESHI (Senior Member, IEEE)
                           IEEE) received the B.Sc. degree in computer                                         received the Ph.D. degree from the City University
                           science from Moi University, the M.Sc. degree                                       of Hong Kong, Hong Kong, in 2021. His Ph.D.
                           in computer science from Universiti Teknologi                                       thesis focused on lung cancer drug resistance
                           Malaysia (UTM), and the Ph.D. degree in infor-                                      analysis using molecular dynamics simulation and
                           mation technology from Universiti Teknologi                                         machine learning. He joined the Fast School
                           PETRONAS (UTP). He is currently an Associate                                        of Computing, National University of Computer
                           Professor and a member of the Centre for Research                                   and Emerging Sciences, Karachi, Pakistan, as an
                           in Data Science (CeRDaS), UTP. He is involved                                       Assistant Professor. He is currently with the
                           in flagship consultancy projects for PETRONAS                                       College of Science and Engineering, Hamad Bin
under pipeline integrity, materials corrosion, and inspection. His research         Khalifa University, Doha, Qatar. He has published his findings and methods
interests include machine learning, deep learning architectures, optimiza-          in IEEE TRANSACTIONS ON COMPUTATIONAL BIOLOGY AND BIOINFORMATICS, IEEE
tions, and applications in predictive analytics. He is serving as the Treasurer     JOURNAL OF BIOMEDICAL AND HEALTH INFORMATICS, Pattern Recognition, and
for the IEEE Computational Intelligence Society Malaysia Chapter and the            IEEE BIBM Conference. His research interests include AI applications in
Editor-in-Chief for Platform journal.                                               life sciences, cancer data sciences, computer vision, and machine learning.

                         AMGAD MUNEER received the B.Eng. degree
                         (Hons.) in mechatronic engineering from Asia
                         Pacific University of Technology and Innovation
                         (APU), in 2018, and the master’s degree in
                         information technology from Universiti Teknologi
                         PETRONAS, Malaysia, in 2022. He is currently
                         with the Department of Imaging Physics, The
                         University of Texas MD Anderson Cancer Center,
                         Houston, TX, USA, as a Research Assistant.                                            SAFWAN MAHMOOD AL-SELWI received the
                         He has authored several high-impact articles in                                       bachelor’s degree in software engineering from
well-reputed journals and conferences. His research interests include                                          Taiz University, Yemen, in 2012, and the master’s
computer vision, AI applications for cancer data sciences, manufacturing                                       degree in computer applications from Banga-
data analytics, medical imaging, and bioinformatics. He is a reviewer of                                       lore University, India, in 2018. He is currently
many international impact-factor journals.                                                                     a Research Assistant with the Department of
                                                                                                               Computer and Information Sciences, Universiti
                                                                                                               Teknologi PETRONAS (UTP), Malaysia. He has
                         ALAWI ALQUSHAIBI received the B.Sc. degree
                                                                                                               a total experience of eight years both in academic
                         in computer networks and security from Universiti
                                                                                                               institutions and in the industry. His industry
                         Teknologi Malaysia, in 2012, and the master’s
                                                                                    working experience is related to Android applications and website
                         (by Research) degree from Universiti Teknologi
                                                                                    development. His research interests include artificial intelligence, machine
                         PETRONAS (UTP), in 2021. He is currently
                                                                                    learning, predictive and time-series analysis, metaheuristic algorithms, and
                         an Academic Researcher. During his academic
                                                                                    optimization.
                         journey, he has acquired knowledge and skills
                         in conducting independent research, producing
                         academic writing, and teaching computer science
                         courses. His research interests include machine
learning, data science, optimization, feature selection, classification, data
analytics, and image processing, specifically in generative adversarial
networks (GANs).

                           EBRAHIM HAMID SUMIEA received the B.S.
                           degree in software engineering from Asia Pacific                                    HITHAM ALHUSSIAN received the B.Sc. and
                           University of Technology and Innovation (APU),                                      M.Sc. degrees in computer science from the
                           in 2014, and the master’s degree in management.                                     School of Mathematical Sciences, University of
                           He is currently pursuing the Ph.D. degree with                                      Khartoum, Sudan, and the Ph.D. degree from Uni-
                           Universiti Teknologi PETRONAS, delving deeper                                       versiti Teknologi PETRONAS (UTP), Malaysia.
                           into the realm of artificial intelligence. He honed                                 He was a Postdoctoral Researcher with the High-
                           his skills in various programming languages and                                     Performance Cloud Computing Center, UTP. He is
                           software development methodologies at APU.                                          currently a Senior Lecturer with the Department
                           He is eager to explore the fusion of technology and                                 of Computer and Information Sciences, UTP. His
business. His work aims to leverage DDPG’s potential to address complex                                        current research interests include real-time parallel
problems, demonstrating the powerful capacity of AI to transform various            and distributed systems, big data and cloud computing, data mining, and real-
sectors. His research interests include reinforcement learning, specifically in     time analytics.
the area of deep deterministic policy gradient (DDPG).

57836                                                                                                                                              VOLUME 12, 2024
