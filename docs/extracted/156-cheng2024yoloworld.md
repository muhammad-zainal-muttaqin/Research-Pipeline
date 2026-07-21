---
source_id: 156
bibtex_key: cheng2024yoloworld
title: YOLO-World: Real-Time Open-Vocabulary Object Detection
year: 2024
domain_theme: Uncoded
verified_pdf: 156_YOLO-World.pdf
char_count: 88113
---

YOLO-World: Real-Time Open-Vocabulary Object Detection

                                          Tianheng Cheng3,2,∗ , Lin Song1,∗,✉ , Yixiao Ge1,2,† , Wenyu Liu3 , Xinggang Wang3,✉ , Ying Shan1,2
                                                                          ∗                        †                  ✉
                                                                              equal contribution       project lead       corresponding author

                                                                                1
                                                                               Tencent AI Lab 2 ARC Lab, Tencent PCG
                                                                 3
                                                                     School of EIC, Huazhong University of Science & Technology
arXiv:2401.17270v3 [cs.CV] 22 Feb 2024

                                                                                        Code & Models: YOLO-World

                                                                  Abstract

                                            The You Only Look Once (YOLO) series of detectors
                                         have established themselves as efficient and practical tools.
                                         However, their reliance on predefined and trained ob-
                                         ject categories limits their applicability in open scenar-
                                         ios. Addressing this limitation, we introduce YOLO-World,                                   20× Speedup
                                         an innovative approach that enhances YOLO with open-
                                         vocabulary detection capabilities through vision-language
                                         modeling and pre-training on large-scale datasets. Specif-
                                         ically, we propose a new Re-parameterizable Vision-
                                         Language Path Aggregation Network (RepVL-PAN) and
                                         region-text contrastive loss to facilitate the interaction be-
                                         tween visual and linguistic information. Our method excels
                                         in detecting a wide range of objects in a zero-shot man-
                                         ner with high efficiency. On the challenging LVIS dataset,
                                         YOLO-World achieves 35.4 AP with 52.0 FPS on V100,                      Figure 1. Speed-and-Accuracy Curve. We compare YOLO-
                                         which outperforms many state-of-the-art methods in terms                World with recent open-vocabulary methods in terms of speed and
                                         of both accuracy and speed. Furthermore, the fine-tuned                 accuracy. All models are evaluated on the LVIS minival and in-
                                                                                                                 ference speeds are measured on one NVIDIA V100 w/o TensorRT.
                                         YOLO-World achieves remarkable performance on several
                                                                                                                 The size of the circle represents the model’s size.
                                         downstream tasks, including object detection and open-
                                         vocabulary instance segmentation.
                                                                                                                 scenarios.
                                                                                                                     Recent works [8, 13, 48, 53, 58] have explored the
                                         1. Introduction                                                         prevalent vision-language models [19, 39] to address open-
                                                                                                                 vocabulary detection [58] through distilling vocabulary
                                         Object detection has been a long-standing and fundamental               knowledge from language encoders, e.g., BERT [5]. How-
                                         challenge in computer vision with numerous applications in              ever, these distillation-based methods are much limited due
                                         image understanding, robotics, and autonomous vehicles.                 to the scarcity of training data with a limited diversity of
                                         Tremendous works [16, 27, 43, 45] have achieved signif-                 vocabulary, e.g., OV-COCO [58] containing 48 base cate-
                                         icant breakthroughs in object detection with the develop-               gories. Several methods [24, 30, 56, 57, 59] reformulate ob-
                                         ment of deep neural networks. Despite the success of these              ject detection training as region-level vision-language pre-
                                         methods, they remain limited as they only handle object de-             training and train open-vocabulary object detectors at scale.
                                         tection with a fixed vocabulary, e.g., 80 categories in the             However, those methods still struggle for detection in real-
                                         COCO [26] dataset. Once object categories are defined and               world scenarios, which suffer from two aspects: (1) heavy
                                         labeled, trained detectors can only detect those specific cat-          computation burden and (2) complicated deployment for
                                         egories, thus limiting the ability and applicability of open            edge devices. Previous works [24, 30, 56, 57, 59] have

                                                                                                             1
demonstrated the promising performance of pre-training                to connect vision and language features and an open-
large detectors while pre-training small detectors to en-             vocabulary region-text contrastive pre-training scheme
dow them with open recognition capabilities remains un-               for YOLO-World.
explored.                                                           • The proposed YOLO-World pre-trained on large-scale
    In this paper, we present YOLO-World, aiming for                  datasets demonstrates strong zero-shot performance and
high-efficiency open-vocabulary object detection, and ex-             achieves 35.4 AP on LVIS with 52.0 FPS. The pre-trained
plore large-scale pre-training schemes to boost the tradi-            YOLO-World can be easily adapted to downstream tasks,
tional YOLO detectors to a new open-vocabulary world.                 e.g., open-vocabulary instance segmentation and referring
Compared to previous methods, the proposed YOLO-                      object detection. Moreover, the pre-trained weights and
World is remarkably efficient with high inference speed               codes of YOLO-World will be open-sourced to facilitate
and easy to deploy for downstream applications. Specif-               more practical applications.
ically, YOLO-World follows the standard YOLO archi-
tecture [20] and leverages the pre-trained CLIP [39] text           2. Related Works
encoder to encode the input texts. We further propose
the Re-parameterizable Vision-Language Path Aggregation             2.1. Traditional Object Detection
Network (RepVL-PAN) to connect text features and im-                Prevalent object detection research concentrates on fixed-
age features for better visual-semantic representation. Dur-        vocabulary (close-set) detection, in which object detectors
ing inference, the text encoder can be removed and the              are trained on datasets with pre-defined categories, e.g.,
text embeddings can be re-parameterized into weights of             COCO dataset [26] and Objects365 dataset [46], and then
RepVL-PAN for efficient deployment. We further inves-               detect objects within the fixed set of categories. During
tigate the open-vocabulary pre-training scheme for YOLO             the past decades, the methods for traditional object de-
detectors through region-text contrastive learning on large-        tection can be simply categorized into three groups, i.e.,
scale datasets, which unifies detection data, grounding data,       region-based methods, pixel-based methods, and query-
and image-text data into region-text pairs. The pre-trained         based methods. The region-based methods [11, 12, 16, 27,
YOLO-World with abundant region-text pairs demonstrates             44], such as Faster R-CNN [44], adopt a two-stage frame-
a strong capability for large vocabulary detection and train-       work for proposal generation [44] and RoI-wise (Region-
ing more data leads to greater improvements in open-                of-Interest) classification and regression. The pixel-based
vocabulary capability.                                              methods [28, 31, 42, 49, 61] tend to be one-stage detec-
    In addition, we explore a prompt-then-detect paradigm           tors, which perform classification and regression over pre-
to further improve the efficiency of open-vocabulary object         defined anchors or pixels. DETR [1] first explores object
detection in real-world scenarios. As illustrated in Fig. 2,        detection through transformers [50] and inspires extensive
traditional object detectors [16, 20, 23, 41–43, 52] con-           query-based methods [64]. In terms of inference speed,
centrate on the fixed-vocabulary (close-set) detection with         Redmon et al. presents YOLOs [40–42] which exploit sim-
predefined and trained categories. While previous open-             ple convolutional architectures for real-time object detec-
vocabulary detectors [24, 30, 56, 59] encode the prompts of         tion. Several works [10, 23, 33, 52, 55] propose various
a user for online vocabulary with text encoders and detect          architectures or designs for YOLO, including path aggrega-
objects. Notably, those methods tend to employ large de-            tion networks [29], cross-stage partial networks [51], and
tectors with heavy backbones, e.g., Swin-L [32], to increase        re-parameterization [6], which further improve both speed
the open-vocabulary capacity. In contrast, the prompt-then-         and accuracy. In comparison to previous YOLOs, YOLO-
detect paradigm (Fig. 2 (c)) first encodes the prompts of a         World in this paper aims to detect objects beyond the fixed
user to build an offline vocabulary and the vocabulary varies       vocabulary with strong generalization ability.
with different needs. Then, the efficient detector can infer
the offline vocabulary on the fly without re-encoding the           2.2. Open-Vocabulary Object Detection
prompts. For practical applications, once we have trained           Open-vocabulary object detection (OVD) [58] has emerged
the detector, i.e., YOLO-World, we can pre-encode the               as a new trend for modern object detection, which aims
prompts or categories to build an offline vocabulary and            to detect objects beyond the predefined categories. Early
then seamlessly integrate it into the detector.                     works [13] follow the standard OVD setting [58] by train-
    Our main contributions can be summarized into three             ing detectors on the base classes and evaluating the novel
folds:                                                              (unknown) classes. Nevertheless, this open-vocabulary set-
• We introduce the YOLO-World, a cutting-edge open-                 ting can evaluate the capability of detectors to detect and
   vocabulary object detector with high efficiency for real-        recognize novel objects, it is still limited for open scenar-
   world applications.                                              ios and lacks generalization ability to other domains due
• We propose a Re-parameterizable Vision-Language PAN               to training on the limited dataset and vocabulary. Inspired

                                                                2
 User                                             User                                                           User
                        Fixed                               Text                                                              Text             Offline
                      Vocabulary                           Encoder           Online                                          Encoder          Vocabulary
                                                                           Vocabulary
                                                                                                                                   Re-parameterize

                 Object Detector                                Large Detector                                                Lightweight Detector

  (a) Traditional Object Detector               (b) Preivous Open-Vocabulary Detector                                        (c) YOLO-World

Figure 2. Comparison with Detection Paradigms. (a) Traditional Object Detector: These object detectors can only detect objects
                                                        caption, e.g.,
within the fixed vocabulary pre-defined by the training datasets, noun80phrases,  category…
                                                                         categories of COCO dataset [26]. The fixed vocabulary limits the
extension for open scenes. (b) Previous Open-Vocabulary Detectors: Previous methods tend to develop large and heavy detectors for
open-vocabulary detection which intuitively have strong capacity. In addition, these detectors simultaneously encode images and texts as Text Embeddin
input for prediction, which is time-consuming for practical applications. (c) YOLO-World: We demonstrate the strong open-vocabulary
performance of lightweight detectors, e.g., YOLO detectors [20, 42], which is of great significance for real-world applications. Rather than         D
using online vocabulary, we present a prompt-then-detect paradigm for efficient inference, in which the user generates a series of prompts
according to the need and the prompts will be encoded into an offline vocabulary. Then it can be re-parameterized as the model weights              D
for deployment and further acceleration.
                                                    Vocabulary Embeddings                            Image-aware Embeddings       Region-Text Matching
 Training: Online Vocabulary
                                                              man                                             man
       A man and a                    Text
     woman are skiing                                         woman                                           woman
        with a dog                  Encoder                   dog                                             dog
        Extract Nouns                                                          Vision-Language PAN
  Deployment: Offline Vocabulary
                                     User’s
                                   Vocabulary                                                                                      Object Embeddings
                                                          Multi-scale
          User
                                                         Image Features
                                                                                                               Text
                                                                                                          Contrastive Head
                                    YOLO
                                   Backbone
                                                                                                             Box Head
        Input Image

Figure 3. Overall Architecture of YOLO-World. Compared to traditional YOLO detectors, YOLO-World as an open-vocabulary detector
adopts text as input. The Text Encoder first encodes the input text input text embeddings. Then the Image Encoder encodes the input image
                                                                                                                                       Multi-scale Image F
into multi-scale image features and the proposed RepVL-PAN exploits the multi-level cross-modality fusion for both image and text features.
Finally, YOLO-World predicts the regressed bounding boxes and the object embeddings for matching the categories or nouns that appeared
in the input text.

by vision-language pre-training [19, 39], recent works [8,              datasets through region-text matching and pre-train detec-
22, 53, 62, 63] formulate open-vocabulary object detection              tors with large-scale image-text pairs, achieving promising
as image-text matching and exploit large-scale image-text               performance and generalization. However, these methods
data to increase the training vocabulary at scale. OWL-                 often use heavy detectors like ATSS [61] or DINO [60]
ViTs [35, 36] fine-tune the simple vision transformers [7]              with Swin-L [32] as a backbone, leading to high com-
with detection and grounding datasets and build the sim-                putational demands and deployment challenges. In con-
ple open-vocabulary detectors with promising performance.               trast, we present YOLO-World, aiming for efficient open-
GLIP [24] presents a pre-training framework for open-                   vocabulary object detection with real-time inference and
vocabulary detection based on phrase grounding and eval-                easier downstream application deployment. Differing from
uates in a zero-shot setting. Grounding DINO [30] incor-                ZSD-YOLO [54], which also explores open-vocabulary de-
porates the grounded pre-training [24] into detection trans-            tection [58] with YOLO through language model align-
formers [60] with cross-modality fusions. Several meth-                 ment, YOLO-World introduces a novel YOLO framework
ods [25, 56, 57, 59] unify detection datasets and image-text            with an effective pre-training strategy, enhancing open-

                                                                    3
vocabulary performance and generalization.                            where L2-Norm(·) is the L2 normalization and wj ∈ W
                                                                      is the j-th text embeddings. In addition, we add the affine
3. Method                                                             transformation with the learnable scaling factor α and shift-
                                                                      ing factor β. Both the L2 norms and the affine transforma-
3.1. Pre-training Formulation: Region-Text Pairs                      tions are important for stabilizing the region-text training.
The traditional object detection methods, including the
YOLO-series [20], are trained with instance annotations
                                                                      Training with Online Vocabulary. During training, we
Ω = {Bi , ci }N i=1 , which consist of bounding boxes {Bi }
                                                                      construct an online vocabulary T for each mosaic sample
and category labels {ci }. In this paper, we reformulate the
                                                                      containing 4 images. Specifically, we sample all positive
instance annotations as region-text pairs Ω = {Bi , ti }N i=1 ,
                                                                      nouns involved in the mosaic images and randomly sam-
where ti is the corresponding text for the region Bi . Specif-
                                                                      ple some negative nouns from the corresponding dataset.
ically, the text ti can be the category name, noun phrases,
                                                                      The vocabulary for each mosaic sample contains at most M
or object descriptions. Moreover, YOLO-World adopts both
                                                                      nouns, and M is set to 80 as default.
the image I and texts T (a set of nouns) as input and outputs
predicted boxes {B̂k } and the corresponding object embed-
dings {ek } (ek ∈ RD ).                                               Inference with Offline Vocabulary. At the inference
                                                                      stage, we present a prompt-then-detect strategy with an of-
3.2. Model Architecture                                               fline vocabulary for further efficiency. As shown in Fig. 3,
The overall architecture of the proposed YOLO-World is il-            the user can define a series of custom prompts, which might
lustrated in Fig. 3, which consists of a YOLO detector, a             include captions or categories. We then utilize the text en-
Text Encoder, and a Re-parameterizable Vision-Language                coder to encode these prompts and obtain offline vocabu-
Path Aggregation Network (RepVL-PAN). Given the input                 lary embeddings. The offline vocabulary allows for avoid-
text, the text encoder in YOLO-World encodes the text into            ing computation for each input and provides the flexibility
text embeddings. The image encoder in the YOLO detector               to adjust the vocabulary as needed.
extracts the multi-scale features from the input image. Then
we leverage the RepVL-PAN to enhance both text and im-                3.3. Re-parameterizable Vision-Language PAN
age representation by exploiting the cross-modality fusion            Fig. 4 shows the structure of the proposed RepVL-PAN
between image features and text embeddings.                           which follows the top-down and bottom-up paths in [20, 29]
                                                                      to establish the feature pyramids {P3 , P4 , P5 } with the
YOLO Detector. YOLO-World is mainly developed                         multi-scale image features {C3 , C4 , C5 }. Furthermore,
based on YOLOv8 [20], which contains a Darknet back-                  we propose the Text-guided CSPLayer (T-CSPLayer) and
bone [20, 43] as the image encoder, a path aggregation net-           Image-Pooling Attention (I-Pooling Attention) to further
work (PAN) for multi-scale feature pyramids, and a head               enhance the interaction between image features and text
for bounding box regression and object embeddings.                    features, which can improve the visual-semantic represen-
                                                                      tation for open-vocabulary capability. During inference, the
Text Encoder. Given the text T , we adopt the Trans-                  offline vocabulary embeddings can be re-parameterized into
former text encoder pre-trained by CLIP [39] to extract the           weights of convolutional or linear layers for deployment.
corresponding text embeddings W = TextEncoder(T ) ∈
RC×D , where C is the number of nouns and D is the em-
                                                                      Text-guided CSPLayer. As Fig. 4 illustrates, the cross-
bedding dimension. The CLIP text encoder offers better
                                                                      stage partial layers (CSPLayer) are utilized after the top-
visual-semantic capabilities for connecting visual objects
                                                                      down or bottom-up fusion. We extend the CSPLayer
with texts compared to text-only language encoders [5].
                                                                      (also called C2f) of [20] by incorporating text guidance
When the input text is a caption or referring expression,
                                                                      into multi-scale image features to form the Text-guided
we adopt the simple n-gram algorithm to extract the noun
                                                                      CSPLayer. Specifically, given the text embeddings W and
phrases and then feed them into the text encoder.
                                                                      image features Xl ∈ RH×W ×D (l ∈ {3, 4, 5}), we adopt
                                                                      the max-sigmoid attention after the last dark bottleneck
Text Contrastive Head. Following previous works [20],                 block to aggregate text features into image features by:
we adopt the decoupled head with two 3×3 convs to regress
bounding boxes {bk }K k=1 and object embeddings {ek }k=1 ,
                                                          K
                                                                                   Xl′ = Xl · δ( max (Xl Wj⊤ ))⊤ ,              (2)
where K denotes the number of objects. We present a text                                        j∈{1..C}
contrastive head to obtain the object-text similarity sk,j by:
                                                                      where the updated Xl′ is concatenated with the cross-stage
                                                ⊤
   sk,j = α · L2-Norm(ek ) · L2-Norm(wj ) + β,             (1)        features as output. The δ indicates the sigmoid function.

                                                                  4
                                 woman
                                 dog=

          Text Embeddings                                Image-aware Embeddings                                  the image-text data. Considering image-text datasets have
                                                                                                                 noisy boxes, we only calculate the regression loss for sam-
                                                                                                                 ples with accurate bounding boxes.
 C5                                                    T-CSPLayer                                       P5

                                 I-Pooling Attention

                                                                               I-Pooling Attention
                                                               1
                       ×2                                    ×
                                                               2
                                                                                                                 Pseudo Labeling with Image-Text Data. Rather than di-
 C4             T-CSPLayer                             T-CSPLayer                                       P4       rectly using image-text pairs for pre-training, we propose an
                       ×2                                    ×
                                                                 1                                               automatic labeling approach to generate region-text pairs.
                                                                 2
                                                                                                                 Specifically, the labeling approach contains three steps: (1)
 C3             T-CSPLayer                                                                              P3       extract noun phrases: we first utilize the n-gram algo-
                         Text to Image                               Image to Text
                                                                                                                 rithm to extract noun phrases from the text; (2) pseudo la-
                                                                                                                 beling: we adopt a pre-trained open-vocabulary detector,
  S Split     C Concat             Text                              3×3                             Text        e.g., GLIP [24], to generate pseudo boxes for the given
      S     Dark Bottleneck   Max-Sigmoid                C                                C          MHCA
                                                                                                                 noun phrases for each image, thus providing the coarse
                                                                                                                 region-text pairs. (3) filtering: We employ the pre-trained
                                                                                                                 CLIP [39] to evaluate the relevance of image-text pairs and
             T-CSPLayer (C2f Block)                                        I-Pooling Attention
                                                                                                                 region-text pairs, and filter the low-relevance pseudo an-
Figure 4. Illustration of the RepVL-PAN. The proposed RepVL-                                                     notations and images. We further filter redundant bound-
PAN adopts the Text-guided CSPLayer (T-CSPLayer) for injecting                                                   ing boxes by incorporating methods such as Non-Maximum
language information into image features and the Image Pooling                                                   Suppression (NMS). We suggest the readers refer to the ap-
Attention (I-Pooling Attention) for enhancing image-aware text                                                   pendix for the detailed approach. With the above approach,
embeddings.                                                                                                      we sample and label 246k images from CC3M [47] with
                                                                                                                 821k pseudo annotations.
Image-Pooling Attention. To enhance the text embed-
dings with image-aware information, we aggregate image
features to update the text embeddings by proposing the
                                                                                                                 4. Experiments
Image-Pooling Attention. Rather than directly using cross-                                                       In this section, we demonstrate the effectiveness of the
attention on image features, we leverage max pooling on                                                          proposed YOLO-World by pre-training it on large-scale
multi-scale features to obtain 3 × 3 regions, resulting in a                                                     datasets and evaluating YOLO-World in a zero-shot manner
total of 27 patch tokens X̃ ∈ R27×D . The text embeddings                                                        on both LVIS benchmark and COCO benchmark (Sec. 4.2).
are then updated by:                                                                                             We also evaluate the fine-tuning performance of YOLO-
                                                                                                                 World on COCO, LVIS for object detection.
  W ′ = W + MultiHead-Attention(W, X̃, X̃) (3)

3.4. Pre-training Schemes                                                                                        4.1. Implementation Details

In this section, we present the training schemes for pre-                                                        The YOLO-World is developed based on the MMYOLO
training YOLO-World on large-scale detection, grounding,                                                         toolbox [3] and the MMDetection toolbox [2]. Following
and image-text datasets.                                                                                         [20], we provide three variants of YOLO-World for differ-
                                                                                                                 ent latency requirements, e.g., small (S), medium (M), and
                                                                                                                 large (L). We adopt the open-source CLIP [39] text encoder
Learning from Region-Text Contrastive Loss. Given
                                                                                                                 with pre-trained weights to encode the input text. Unless
the mosaic sample I and texts T , YOLO-World outputs
                                                                                                                 specified, we measure the inference speeds of all models on
K object predictions {Bk , sk }K  k=1 along with annotations                                                     one NVIDIA V100 GPU without extra acceleration mecha-
Ω = {Bi , ti }N
              i=1 . We follow  [20] and leverage task-aligned
                                                                                                                 nisms, e.g., FP16 or TensorRT.
label assignment [9] to match the predictions with ground-
truth annotations and assign each positive prediction with a                                                     4.2. Pre-training
text index as the classification label. Based on this vocabu-
lary, we construct the region-text contrastive loss Lcon with                                                    Experimental Setup. At the pre-training stage, we adopt
region-text pairs through cross entropy between object-text                                                      the AdamW optimizer [34] with an initial learning rate
(region-text) similarity and object-text assignments. In ad-                                                     of 0.002 and weight decay of 0.05. YOLO-World is pre-
dition, we adopt IoU loss and distributed focal loss for                                                         trained for 100 epochs on on 32 NVIDIA V100 GPUs with
bounding box regression and the total training loss is de-                                                       a total batch size of 512. During pre-training, we follow
fined as: L(I) = Lcon + λI · (Liou + Ldfl ), where λI is                                                         previous works [20] and adopt color augmentation, random
an indicator factor and set to 1 when input image I is from                                                      affine, random flip, and mosaic with 4 images for data aug-
detection or grounding data and set to 0 when it is from                                                         mentation. The text encoder is frozen during pre-training.

                                                                                                             5
 Dataset              Type         Vocab.   Images   Anno.           4.3. Ablation Experiments
 Objects365V1 [46]    Detection     365      609k    9,621k          We provide extensive ablation studies to analyze YOLO-
 GQA [17]             Grounding      -       621k    3,681k          World from two primary aspects, i.e., pre-training and ar-
 Flickr [38]          Grounding      -       149k     641k           chitecture. Unless specified, we mainly conduct ablation
 CC3M† [47]           Image-Text     -       246k     821k           experiments based on YOLO-World-L and pre-train Ob-
                                                                     jects365 with zero-shot evaluation on LVIS minival.
Table 1. Pre-training Data. The specifications of the datasets
used for pre-training YOLO-World.
                                                                     Pre-training Data. In Tab. 3, we evaluate the perfor-
                                                                     mance of pre-training YOLO-World using different data.
Pre-training Data. For pre-training YOLO-World, we                   Compared to the baseline trained on Objects365, adding
mainly adopt detection or grounding datasets including Ob-           GQA can significantly improve performance with an 8.4
jects365 (V1) [46], GQA [17], Flickr30k [38], as specified           AP gain on LVIS. This improvement can be attributed to
in Tab. 1. Following [24], we exclude the images from                the richer textual information provided by the GQA dataset,
the COCO dataset in GoldG [21] (GQA and Flickr30k).                  which can enhance the model’s ability to recognize large
The annotations of the detection datasets used for pre-              vocabulary objects. Adding part of CC3M samples (8%
training contain both bounding boxes and categories or               of the full datasets) can further bring 0.5 AP gain with 1.3
noun phrases. In addition, we also extend the pre-training           AP on rare objects. Tab. 3 demonstrates that adding more
data with image-text pairs, i.e., CC3M† [47], which we have          data can effectively improve the detection capabilities on
labeled 246k images through the pseudo-labeling method               large-vocabulary scenarios. Furthermore, as the amount of
discussed in Sec. 3.4.                                               data increases, the performance continues to improve, high-
                                                                     lighting the benefits of leveraging larger and more diverse
                                                                     datasets for training.
Zero-shot Evaluation. After pre-training, we di-
rectly evaluate the proposed YOLO-World on the LVIS                  Ablations on RepVL-PAN. Tab. 4 demonstrates the ef-
dataset [14] in a zero-shot manner. The LVIS dataset                 fectiveness of the proposed RepVL-PAN of YOLO-World,
contains 1203 object categories, which is much more                  including Text-guided CSPLayers and Image Pooling At-
than the categories of the pre-training detection datasets           tention, for the zero-shot LVIS detection. Specifically, we
and can measure the performance on large vocabulary                  adopt two settings, i.e., (1) pre-training on O365 and (2)
detection. Following previous works [21, 24, 56, 57], we             pre-training on O365 & GQA. Compared to O365 which
mainly evaluate on LVIS minival [21] and report the                  only contains category annotations, GQA includes rich
Fixed AP [4] for comparison. The maximum number of                   texts, particularly in the form of noun phrases. As shown
predictions is set to 1000.                                          in Tab. 4, the proposed RepVL-PAN improves the base-
                                                                     line (YOLOv8-PAN [20]) by 1.1 AP on LVIS, and the im-
                                                                     provements are remarkable in terms of the rare categories
Main Results on LVIS Object Detection. In Tab. 2, we                 (APr ) of LVIS, which are hard to detect and recognize. In
compare the proposed YOLO-World with recent state-of-                addition, the improvements become more significant when
the-art methods [21, 30, 56, 57, 59] on LVIS benchmark in a          YOLO-World is pre-trained with the GQA dataset and ex-
zero-shot manner. Considering the computation burden and             periments indicate that the proposed RepVL-PAN works
model parameters, we mainly compare with those methods               better with rich textual information.
based on lighter backbones, e.g., Swin-T [32]. Remarkably,
YOLO-World outperforms previous state-of-the-art meth-               Text Encoders. In Tab. 5, we compare the performance
ods in terms of zero-shot performance and inference speed.           of using different text encoders, i.e., BERT-base [5] and
Compared to GLIP, GLIPv2, and Grounding DINO, which                  CLIP-base (ViT-base) [39]. We exploit two settings dur-
incorporate more data, e.g., Cap4M (CC3M+SBU [37]),                  ing pre-training, i.e., frozen and fine-tuned, and the learn-
YOLO-World pre-trained on O365 & GolG obtains bet-                   ing rate for fine-tuning text encoders is a 0.01× factor of
ter performance even with fewer model parameters. Com-               the basic learning rate. As Tab. 5 shows, the CLIP text
pared to DetCLIP, YOLO-World achieves comparable per-                encoder obtains superior results than BERT (+10.1 AP for
formance (35.4 v.s. 34.4) while obtaining 20× increase in            rare categories in LVIS), which is pre-trained with image-
inference speed. The experimental results also demonstrate           text pairs and has better capability for vision-centric embed-
that small models, e.g., YOLO-World-S with 13M parame-               dings. Fine-tuning BERT during pre-training brings signifi-
ters, can be used for vision-language pre-training and ob-           cant improvements (+3.7 AP) while fine-tuning CLIP leads
tain strong open-vocabulary capabilities.                            to a severe performance drop. We attribute the drop to that

                                                                 6
  Method                      Backbone          Params       Pre-trained Data             FPS        AP     APr    APc       APf
  MDETR [21]                  R-101 [15]        169M         GoldG                          -        24.2   20.9   24.3      24.2
  GLIP-T [24]                 Swin-T [32]       232M         O365,GoldG                   0.12       24.9   17.7   19.5      31.0
  GLIP-T [24]                 Swin-T [32]       232M         O365,GoldG,Cap4M             0.12       26.0   20.8   21.4      31.0
  GLIPv2-T [59]               Swin-T [32]       232M         O365,GoldG                   0.12       26.9    -      -         -
  GLIPv2-T [59]               Swin-T [32]       232M         O365,GoldG,Cap4M             0.12       29.0    -      -         -
  Grounding DINO-T [30]       Swin-T [32]       172M         O365,GoldG                    1.5       25.6   14.4   19.6      32.2
  Grounding DINO-T [30]       Swin-T [32]       172M         O365,GoldG,Cap4M              1.5       27.4   18.1   23.3      32.7
  DetCLIP-T [56]              Swin-T [32]       155M         O365,GoldG                    2.3       34.4   26.9   33.9      36.3
  YOLO-World-S                YOLOv8-S        13M (77M)      O365,GoldG                74.1 (19.9)   26.2   19.1   23.6      29.8
  YOLO-World-M                YOLOv8-M       29M (92M)       O365,GoldG                58.1 (18.5)   31.0   23.8   29.2      33.9
  YOLO-World-L                YOLOv8-L       48M (110M)      O365,GoldG                52.0 (17.6)   35.0   27.1   32.8      38.3
  YOLO-World-L                YOLOv8-L       48M (110M)      O365,GoldG,CC3M†          52.0 (17.6)   35.4   27.6   34.1      38.0

Table 2. Zero-shot Evaluation on LVIS. We evaluate YOLO-World on LVIS minival [21] in a zero-shot manner. We report the Fixed
AP [4] for a fair comparison with recent methods. † denotes the pseudo-labeled CC3M in our setting, which contains 246k samples.
The FPS is evaluated on one NVIDIA V100 GPU w/o TensorRT. The parameters and FPS of YOLO-World are evaluated for both the
re-parameterized version (w/o bracket) and the original version (w/ bracket).

    Pre-trained Data         AP      APr     APc     APf              Text Encoder      Frozen?      AP     APr     APc       APf
    O365                     23.5    16.2    21.1    27.0             BERT-base         Frozen       14.6    3.4    10.7      20.0
    O365,GQA                 31.9    22.5    29.9    35.4             BERT-base         Fine-tune    18.3    6.6    14.6      23.6
    O365,GoldG               32.5    22.3    30.6    36.0             CLIP-base         Frozen       22.4   14.5    20.1      26.0
    O365,GoldG,CC3M†         33.0    23.6    32.0    35.5             CLIP-base         Fine-tune    19.3    8.6    15.7      24.8

Table 3. Ablations on Pre-training Data. We evaluate the zero-       Table 5. Text Encoder in YOLO-World. We ablate different text
shot performance on LVIS of pre-training YOLO-World with dif-        encoders in YOLO-World through the zero-shot LVIS evaluation.
ferent amounts of data.

    GQA      T→I     I→T     AP      APr     APc    APf              to demonstrate the effectiveness of the pre-training.
     ✗        ✗       ✗      22.4    14.5    20.1   26.0
     ✗        ✓       ✗      23.2    15.2    20.6   27.0             Experimental Setup. We use the pre-trained weights to
     ✗        ✓       ✓      23.5    16.2    21.1   27.0             initialize YOLO-World for fine-tuning. All models are fine-
     ✓        ✗       ✗      29.7    21.0    27.1   33.6             tuned for 80 epochs with the AdamW optimizer and the ini-
                                                                     tial learning rate is set to 0.0002. In addition, we fine-tune
     ✓        ✓       ✓      31.9    22.5    29.9   35.4
                                                                     the CLIP text encoder with a learning factor of 0.01. For the
                                                                     LVIS dataset, we follow previous works [8, 13, 63] and fine-
Table 4. Ablations on Re-parameterizable Vision-Language
                                                                     tune YOLO-World on the LVIS-base (common & frequent)
Path Aggregation Network. We evaluate the zero-shot perfor-
mance on LVIS of the proposed Vision-Language Path Aggrega-
                                                                     and evaluate it on the LVIS-novel (rare).
tion Network. T→I and I→T denote the Text-guided CSPLayers
and Image-Pooling Attention, respectively.                           COCO Object Detection. We compare the pre-trained
                                                                     YOLO-World with previous YOLO detectors [20, 23, 52]
                                                                     in Tab. 6. For fine-tuning YOLO-World on the COCO
fine-tuning on O365 may degrade the generalization ability           dataset, we remove the proposed RepVL-PAN for fur-
of the pre-trained CLIP, which contains only 365 categories          ther acceleration considering that the vocabulary size of
and lacks abundant textual information.                              the COCO dataset is small. In Tab. 6, it’s evident that
                                                                     our approach can achieve decent zero-shot performance on
4.4. Fine-tuning YOLO-World
                                                                     the COCO dataset, which indicates that YOLO-World has
In this section, we further fine-tune YOLO-World for close-          strong generalization ability. Moreover, YOLO-World af-
set object detection on the COCO dataset and LVIS dataset            ter fine-tuning on the COCO train2017 demonstrates

                                                                 7
  Method              Pre-train   AP     AP50   AP75   FPS                  Method                AP       APr     APc     APf
  Training from scratch.                                                    ViLD [13]             27.8     16.7    26.5    34.2
  YOLOv6-S [23]          ✗        43.7   60.8   47.0   442                  RegionCLIP [62]       28.2     17.1     -       -
  YOLOv6-M [23]          ✗        48.4   65.7   52.7   277                  Detic [63]            26.8     17.8     -       -
  YOLOv6-L [23]          ✗        50.7   68.1   54.8   166                  FVLM [22]             24.2     18.6     -       -
  YOLOv7-T [52]          ✗        37.5   55.8   40.2   404                  DetPro [8]            28.4     20.8    27.8    32.4
  YOLOv7-L [52]          ✗        50.9   69.3   55.3   182                  BARON [53]            29.5     23.2    29.3    32.5
  YOLOv7-X [52]          ✗        52.6   70.6   57.3   131                  YOLOv8-S              19.4      7.4    17.4    27.0
  YOLOv8-S [20]          ✗        44.4   61.2   48.1   386                  YOLOv8-M              23.1      8.4    21.3    31.5
  YOLOv8-M [20]          ✗        50.5   67.3   55.0   238                  YOLOv8-L              26.9     10.2    25.4    35.8
  YOLOv8-L [20]          ✗        52.9   69.9   57.7   159                  YOLO-World-S          23.9     12.8    20.4    32.7
  Zero-shot transfer.                                                       YOLO-World-M          28.8     15.9    24.6    39.0
  YOLO-World-S          O+G       37.6   52.3   40.7     -                  YOLO-World-L          34.1     20.4    31.1    43.5
  YOLO-World-M          O+G       42.8   58.3   46.4     -
  YOLO-World-L          O+G       44.4   59.8   48.3     -           Table 7. Comparison with Open-Vocabulary Detectors on
                                                                     LVIS. We train YOLO-World on the LVIS-base (including com-
  YOLO-World-L        O+G+C       45.1   60.7   48.9     -
                                                                     mon and frequent) report the bbox AP. The YOLO-v8 are trained
  Fine-tuned w/ RepVL-PAN.                                           on the full LVIS datasets (including base and novel) along with the
  YOLO-World-S          O+G       45.9   62.3   50.1     -           class balanced sampling.
  YOLO-World-M          O+G       51.2   68.1   55.9     -
  YOLO-World-L        O+G+C       53.3   70.1   58.2     -
                                                                     4.5. Open-Vocabulary Instance Segmentation
  Fine-tuned w/o RepVL-PAN.
  YOLO-World-S          O+G       45.7   62.3   49.9   373           In this section, we further fine-tune YOLO-World for
  YOLO-World-M          O+G       50.7   67.2   55.1   231           segmenting objects under the open-vocabulary setting,
                                                                     which can be termed open-vocabulary instance segmenta-
  YOLO-World-L        O+G+C       53.3   70.3   58.1   156
                                                                     tion (OVIS). Previous methods [18] have explored OVIS
                                                                     with pseudo-labelling on novel objects. Differently, con-
Table 6. Comparison with YOLOs on COCO Object Detec-
                                                                     sidering that YOLO-World has strong transfer and gener-
tion. We fine-tune the YOLO-World on COCO train2017 and
evaluate on COCO val2017. The results of YOLOv7 [52] and             alization capabilities, we directly fine-tune YOLO-World
YOLOv8 [20] are obtained from MMYOLO [3]. ‘O’, ‘G’, and ‘C’          on a subset of data with mask annotations and evaluate the
denote pertaining using Objects365, GoldG, and CC3M† , respec-       segmentation performance under large-vocabulary settings.
tively. The FPS is measured on one NVIDIA V100 w/ TensorRT.          Specifically, we benchmark open-vocabulary instance seg-
                                                                     mentation under two settings:
                                                                     • (1) COCO to LVIS setting, we fine-tune YOLO-World on
higher performance compared to previous methods trained                 the COCO dataset (including 80 categories) with mask
from scratch.                                                           annotations, under which the models need to transfer
                                                                        from 80 categories to 1203 categories (80 → 1203);
                                                                     • (2) LVIS-base to LVIS setting, we fine-tune YOLO-World
                                                                        on the LVIS-base (including 866 categories, common &
LVIS Object Detection. In Tab. 7, we evaluate the fine-
                                                                        frequent) with mask annotations, under which the models
tuning performance of YOLO-World on the standard LVIS
                                                                        need to transfer from 866 categories to 1203 categories
dataset. Firstly, compared to the oracle YOLOv8s [20]
                                                                        (866 → 1203).
trained on the full LVIS datasets, YOLO-World achieves
                                                                     We evaluate the fine-tuned models on the standard LVIS
significant improvements, especially for larger models, e.g.,
                                                                     val2017 with 1203 categories, in which 337 rare cate-
YOLO-World-L outperforms YOLOv8-L by 7.2 AP and
                                                                     gories are unseen and can be used to measure the open-
10.2 APr . The improvements can demonstrate the effec-
                                                                     vocabulary performance.
tiveness of the proposed pre-training strategy for large-
vocabulary detection. Moreover, YOLO-World, as an effi-
cient one-stage detector, outperforms previous state-of-the-         Results. Tab. 8 shows the experimental results of extend-
art two-stage methods [8, 13, 22, 53, 63] on the overall per-        ing YOLO-World for open-vocabulary instance segmenta-
formance without extra designs, e.g., learnable prompts [8]          tion. Specifically, we adopt two fine-tuning strategies: (1)
or region-based alginments [13].                                     only fine-tuning the segmentation head and (2) fine-tuning

                                                                 8
all modules. Under strategy (1), the fine-tuned YOLO-                   corresponding bounding boxes, demonstrating that the pre-
World still retains the zero-shot capabilities acquired from            trained YOLO-World has the referring or grounding capa-
the pre-training stage, allowing it to generalize to unseen             bility. This ability can be attributed to the proposed pre-
categories without additional fine-tuning. Strategy (2) en-             training strategy with large-scale training data.
ables YOLO-World fit the LVIS dataset better, but it may
result in the degradation of the zero-shot capabilities.                5. Conclusion
    Tab. 8 shows the comparisons of fine-tuning YOLO-
World with different settings (COCO or LVIS-base) and                   We present YOLO-World, a cutting-edge real-time open-
different strategies (fine-tuning seg. head or fine-tuning              vocabulary detector aiming to improve efficiency and open-
all). Firstly, fine-tuning on LVIS-base obtains better perfor-          vocabulary capability in real-world applications. In this pa-
mance compared to that based on COCO. However, the ra-                  per, we have reshaped the prevalent YOLOs as a vision-
tios between AP and APr (APr /AP) are nearly unchanged,                 language YOLO architecture for open-vocabulary pre-
e.g., the ratios of YOLO-World on COCO and LVIS-base                    training and detection and proposed RepVL-PAN, which
are 76.5% and 74.3%, respectively. Considering that the                 connects vision and language information with the network
detector is frozen, we attribute the performance gap to the             and can be re-parameterized for efficient deployment. We
fact that the LVIS dataset provides more detailed and denser            further present the effective pre-training schemes with de-
segmentation annotations, which are beneficial for learn-               tection, grounding and image-text data to endow YOLO-
ing the segmentation head. When fine-tuning all mod-                    World with a strong capability for open-vocabulary de-
ules, YOLO-World obtains remarkable improvements on                     tection. Experiments can demonstrate the superiority of
LVIS, e.g., YOLO-World-L achieves 9.6 AP gain. However,                 YOLO-World in terms of speed and open-vocabulary per-
the fine-tuning might degrade the open-vocabulary perfor-               formance and indicate the effectiveness of vision-language
mance and lead to a 0.6 box APr drop for YOLO-World-L.                  pre-training on small models, which is insightful for future
                                                                        research. We hope YOLO-World can serve as a new bench-
4.6. Visualizations                                                     mark for addressing real-world open-vocabulary detection.
We provide the visualization results of pre-trained YOLO-
                                                                        References
World-L under three settings: (a) we perform zero-shot
inference with LVIS categories; (b) we input the custom                  [1] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas
prompts with fine-grained categories with attributes; (c) re-                Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-
ferring detection. The visualizations also demonstrate that                  to-end object detection with transformers. In ECCV, pages
YOLO-World has a strong generalization ability for open-                     213–229, 2020. 2
vocabulary scenarios along with referring ability.                       [2] Kai Chen, Jiaqi Wang, Jiangmiao Pang, Yuhang Cao, Yu
                                                                             Xiong, Xiaoxiao Li, Shuyang Sun, Wansen Feng, Ziwei Liu,
                                                                             Jiarui Xu, Zheng Zhang, Dazhi Cheng, Chenchen Zhu, Tian-
Zero-shot Inference on LVIS. Fig. 5 shows the visual-                        heng Cheng, Qijie Zhao, Buyu Li, Xin Lu, Rui Zhu, Yue Wu,
ization results based on the LVIS categories which are gen-                  Jifeng Dai, Jingdong Wang, Jianping Shi, Wanli Ouyang,
erated by the pre-trained YOLO-World-L in a zero-shot                        Chen Change Loy, and Dahua Lin. MMDetection: Open
manner. The pre-trained YOLO-World exhibits strong zero-                     mmlab detection toolbox and benchmark. arXiv preprint
shot transfer capabilities and is able to detect as many ob-                 arXiv:1906.07155, 2019. 5
jects as possible within the image.                                      [3] MMYOLO Contributors. MMYOLO: OpenMMLab YOLO
                                                                             series toolbox and benchmark. https://github.com/
                                                                             open-mmlab/mmyolo, 2022. 5, 8
Inference with User’s Vocabulary. In Fig. 6, we explore                  [4] Achal Dave, Piotr Dollár, Deva Ramanan, Alexander Kir-
the detection capabilities of YOLO-World with our defined                    illov, and Ross B. Girshick. Evaluating large-vocabulary
categories. The visualization results demonstrate that the                   object detectors: The devil is in the details. CoRR,
pre-trained YOLO-World-L also exhibits the capability for                    abs/2102.01066, 2021. 6, 7
(1) fine-grained detection (i.e., detect the parts of one ob-            [5] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
ject) and (2) fine-grained classification (i.e., distinguish dif-            Toutanova. BERT: pre-training of deep bidirectional trans-
ferent sub-categories of objects.).                                          formers for language understanding. In NAACL-HLT, pages
                                                                             4171–4186, 2019. 1, 4, 6
                                                                         [6] Xiaohan Ding, Xiangyu Zhang, Ningning Ma, Jungong Han,
Referring Object Detection. In Fig. 7, we leverage some                      Guiguang Ding, and Jian Sun. Repvgg: Making vgg-style
descriptive (discriminative) noun phrases as input, e.g., the                convnets great again. In CVPR, pages 13733–13742, 2021.
standing person, to explore whether the model can locate                     2
regions or objects in the image that match our given in-                 [7] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
put. The visualization results display the phrases and their                 Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,

                                                                    9
            Model                  Fine-tune Data     Fine-tune Modules          AP      APr     APc     APf     APb     APbr
            YOLO-World-M           COCO                   Seg Head               12.3     9.1    10.9    14.6    22.3    16.2
            YOLO-World-L           COCO                   Seg Head               16.2    12.4    15.0    19.2    25.3    18.0
            YOLO-World-M           LVIS-base              Seg Head               16.7    12.6    14.6    20.8    22.3    16.2
            YOLO-World-L           LVIS-base              Seg Head               19.1    14.2    17.2    23.5    25.3    18.0
            YOLO-World-M           LVIS-base                  All                25.9    13.4    24.9    32.6    32.6    15.8
            YOLO-World-L           LVIS-base                  All                28.7    15.0    28.3    35.2    36.2    17.4

Table 8. Open-Vocabulary Instance Segmentation. We evaluate YOLO-World for open-vocabulary instance segmentation under the two
settings. We fine-tune the segmentation head or all modules of YOLO-World and report Mask AP for comparison. APb denotes the box
AP.

Figure 5. Visualization Results on Zero-shot Inference on LVIS. We adopt the pre-trained YOLO-World-L and infer with the LVIS
vocabulary (containing 1203 categories) on the COCO val2017.

     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-                  Open-vocabulary object detection via vision and language
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is                knowledge distillation. In ICLR, 2022. 1, 2, 7, 8
     worth 16x16 words: Transformers for image recognition at             [14] Agrim Gupta, Piotr Dollár, and Ross B. Girshick. LVIS: A
     scale. In ICLR, 2021. 3                                                   dataset for large vocabulary instance segmentation. In CVPR,
 [8] Yu Du, Fangyun Wei, Zihe Zhang, Miaojing Shi, Yue Gao,                    pages 5356–5364, 2019. 6
     and Guoqi Li. Learning to prompt for open-vocabulary ob-             [15] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     ject detection with vision-language model. In CVPR, pages                 Deep residual learning for image recognition. In CVPR,
     14064–14073, 2022. 1, 3, 7, 8                                             pages 770–778, 2016. 7
 [9] Chengjian Feng, Yujie Zhong, Yu Gao, Matthew R. Scott,               [16] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross B.
     and Weilin Huang. TOOD: task-aligned one-stage object de-                 Girshick. Mask R-CNN. In ICCV, pages 2980–2988, 2017.
     tection. In ICCV, pages 3490–3499. IEEE, 2021. 5                          1, 2
[10] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian                [17] Drew A. Hudson and Christopher D. Manning. GQA: A new
     Sun. YOLOX: exceeding YOLO series in 2021. CoRR,                          dataset for real-world visual reasoning and compositional
     abs/2107.08430, 2021. 2                                                   question answering. In CVPR, pages 6700–6709, 2019. 6
[11] Ross B. Girshick. Fast R-CNN. In ICCV, pages 1440–1448,              [18] Dat Huynh, Jason Kuen, Zhe Lin, Jiuxiang Gu, and Ehsan
     2015. 2                                                                   Elhamifar. Open-vocabulary instance segmentation via ro-
[12] Ross B. Girshick, Jeff Donahue, Trevor Darrell, and Jitendra              bust cross-modal pseudo-labeling. In CVPR, pages 7010–
     Malik. Rich feature hierarchies for accurate object detection             7021, 2022. 8
     and semantic segmentation. In CVPR, pages 580–587, 2014.             [19] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh,
     2                                                                         Hieu Pham, Quoc V. Le, Yun-Hsuan Sung, Zhen Li, and Tom
[13] Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, and Yin Cui.                        Duerig. Scaling up visual and vision-language representation

                                                                     10
   {men, women, boy, girl} {elephant, ear, leg, trunk, ivory} {golden dog, black dog, spotted dog} {grass, sky, zebra, trunk, tree}

Figure 6. Visualization Results on User’s Vocabulary. We define the custom vocabulary for each input image and YOLO-World can
detect the accurate regions according to the vocabulary. Images are obtained from COCO val2017.

       the person in red               the brown animal                   the tallest person            person with a white shirt

  the jumping     person holding a         person holding a toy                 the standing person                   moon
     person         baseball bat

Figure 7. Visualization Results on Referring Object Detection. We explore the capability of the pre-trained YOLO-World to detect
objects with descriptive noun phrases. Images are obtained from COCO val2017.

     learning with noisy text supervision. In ICML, pages 4904–              work for industrial applications.   CoRR, abs/2209.02976,
     4916, 2021. 1, 3                                                        2022. 2, 7, 8
[20] Glenn Jocher, Ayush Chaurasia, and Jing Qiu. Ultralyt-             [24] Liunian Harold Li, Pengchuan Zhang, Haotian Zhang, Jian-
     ics yolov8. https://github.com/ultralytics/                             wei Yang, Chunyuan Li, Yiwu Zhong, Lijuan Wang, Lu
     ultralytics, 2023. 2, 3, 4, 5, 6, 7, 8                                  Yuan, Lei Zhang, Jenq-Neng Hwang, Kai-Wei Chang, and
[21] Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel                     Jianfeng Gao. Grounded language-image pre-training. In
     Synnaeve, Ishan Misra, and Nicolas Carion. MDETR - mod-                 CVPR, pages 10955–10965, 2022. 1, 2, 3, 5, 6, 7, 13
     ulated detection for end-to-end multi-modal understanding.         [25] Chuang Lin, Peize Sun, Yi Jiang, Ping Luo, Lizhen Qu, Gho-
     In ICCV, pages 1760–1770, 2021. 6, 7                                    lamreza Haffari, Zehuan Yuan, and Jianfei Cai. Learning
[22] Weicheng Kuo, Yin Cui, Xiuye Gu, A. J. Piergiovanni,                    object-language alignments for open-vocabulary object de-
     and Anelia Angelova. F-VLM: open-vocabulary object de-                  tection. In ICLR, 2023. 3
     tection upon frozen vision and language models. CoRR,              [26] Tsung-Yi Lin, Michael Maire, Serge J. Belongie, James
     abs/2209.15639, 2022. 3, 8                                              Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and
[23] Chuyi Li, Lulu Li, Hongliang Jiang, Kaiheng Weng, Yifei                 C. Lawrence Zitnick. Microsoft COCO: common objects
     Geng, Liang Li, Zaidan Ke, Qingyuan Li, Meng Cheng,                     in context. In Proceedings of the European Conference on
     Weiqiang Nie, Yiduo Li, Bo Zhang, Yufei Liang, Linyuan                  Computer Vision (ECCV), pages 740–755, 2014. 1, 2, 3, 13
     Zhou, Xiaoming Xu, Xiangxiang Chu, Xiaoming Wei, and               [27] Tsung-Yi Lin, Piotr Dollár, Ross B. Girshick, Kaiming He,
     Xiaolin Wei. Yolov6: A single-stage object detection frame-             Bharath Hariharan, and Serge J. Belongie. Feature pyramid

                                                                   11
     networks for object detection. In CVPR, pages 936–944,              [43] Joseph Redmon, Santosh Kumar Divvala, Ross B. Girshick,
     2017. 1, 2                                                               and Ali Farhadi. You only look once: Unified, real-time ob-
[28] Tsung-Yi Lin, Priya Goyal, Ross B. Girshick, Kaiming He,                 ject detection. In CVPR, pages 779–788, 2016. 1, 2, 4
     and Piotr Dollár. Focal loss for dense object detection. In        [44] Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun.
     ICCV, pages 2999–3007, 2017. 2                                           Faster R-CNN: towards real-time object detection with re-
[29] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.                gion proposal networks. IEEE Transactions on Pattern Anal-
     Path aggregation network for instance segmentation. In                   ysis and Machine Intelligence, pages 1137–1149, 2017. 2
     CVPR, pages 8759–8768, 2018. 2, 4                                   [45] Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun.
[30] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao                     Faster R-CNN: towards real-time object detection with re-
     Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun                 gion proposal networks. IEEE Transactions on Pattern Anal-
     Zhu, and Lei Zhang. Grounding DINO: marrying DINO with                   ysis and Machine Intelligence, pages 1137–1149, 2017. 1
     grounded pre-training for open-set object detection. CoRR,          [46] Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang
     abs/2303.05499, 2023. 1, 2, 3, 6, 7                                      Yu, Xiangyu Zhang, Jing Li, and Jian Sun. Objects365:
[31] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian                     A large-scale, high-quality dataset for object detection. In
     Szegedy, Scott E. Reed, Cheng-Yang Fu, and Alexander C.                  ICCV, pages 8429–8438, 2019. 2, 6
     Berg. SSD: single shot multibox detector. In ECCV, pages            [47] Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu
     21–37, 2016. 2                                                           Soricut. Conceptual captions: A cleaned, hypernymed, im-
[32] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng                   age alt-text dataset for automatic image captioning. In ACL,
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:                   pages 2556–2565, 2018. 5, 6, 13
     Hierarchical vision transformer using shifted windows. In           [48] Cheng Shi and Sibei Yang. Edadet: Open-vocabulary ob-
     ICCV, pages 9992–10002, 2021. 2, 3, 6, 7                                 ject detection using early dense alignment. In ICCV, pages
[33] Xiang Long, Kaipeng Deng, Guanzhong Wang, Yang Zhang,                    15678–15688, 2023. 1
     Qingqing Dang, Yuan Gao, Hui Shen, Jianguo Ren, Shumin
                                                                         [49] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:
     Han, Errui Ding, and Shilei Wen. PP-YOLO: an effec-
                                                                              fully convolutional one-stage object detection. In ICCV,
     tive and efficient implementation of object detector. CoRR,
                                                                              pages 9626–9635, 2019. 2
     abs/2007.12099, 2020. 2
                                                                         [50] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
[34] Ilya Loshchilov and Frank Hutter. Decoupled weight decay
                                                                              reit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia
     regularization. In ICLR, 2019. 5
                                                                              Polosukhin. Attention is all you need. In NeurIPS, pages
[35] Matthias Minderer, Alexey A. Gritsenko, Austin Stone,
                                                                              5998–6008, 2017. 2
     Maxim Neumann, Dirk Weissenborn, Alexey Dosovitskiy,
                                                                         [51] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,
     Aravindh Mahendran, Anurag Arnab, Mostafa Dehghani,
                                                                              Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. Cspnet: A
     Zhuoran Shen, Xiao Wang, Xiaohua Zhai, Thomas Kipf, and
                                                                              new backbone that can enhance learning capability of CNN.
     Neil Houlsby. Simple open-vocabulary object detection with
                                                                              In CVPRW, pages 1571–1580, 2020. 2
     vision transformers. In ECCV, 2022. 3
[36] Matthias Minderer, Alexey A. Gritsenko, and Neil Houlsby.           [52] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-
     Scaling open-vocabulary object detection. In NeurIPS, 2023.              Yuan Mark Liao. Yolov7: Trainable bag-of-freebies sets
     3                                                                        new state-of-the-art for real-time object detectors. In CVPR,
[37] Vicente Ordonez, Girish Kulkarni, and Tamara L. Berg.                    pages 7464–7475, 2023. 2, 7, 8
     Im2text: Describing images using 1 million captioned pho-           [53] Size Wu, Wenwei Zhang, Sheng Jin, Wentao Liu, and
     tographs. In NeurIPS, pages 1143–1151, 2011. 6                           Chen Change Loy. Aligning bag of regions for open-
[38] Bryan A. Plummer, Liwei Wang, Chris M. Cervantes,                        vocabulary object detection. In CVPR, pages 15254–15264,
     Juan C. Caicedo, Julia Hockenmaier, and Svetlana Lazebnik.               2023. 1, 3, 8
     Flickr30k entities: Collecting region-to-phrase correspon-          [54] Johnathan Xie and Shuai Zheng. ZSD-YOLO: zero-shot
     dences for richer image-to-sentence models. Int. J. Comput.              YOLO detection using vision-language knowledgedistilla-
     Vis., pages 74–93, 2017. 6                                               tion. CoRR, 2021. 3
[39] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya                  [55] Shangliang Xu, Xinxin Wang, Wenyu Lv, Qinyao Chang,
     Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,                    Cheng Cui, Kaipeng Deng, Guanzhong Wang, Qingqing
     Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen                      Dang, Shengyu Wei, Yuning Du, and Baohua Lai.
     Krueger, and Ilya Sutskever. Learning transferable visual                PP-YOLOE: an evolved version of YOLO.                   CoRR,
     models from natural language supervision. In ICML, pages                 abs/2203.16250, 2022. 2
     8748–8763, 2021. 1, 2, 3, 4, 5, 6, 13                               [56] Lewei Yao, Jianhua Han, Youpeng Wen, Xiaodan Liang, Dan
[40] Joseph Redmon and Ali Farhadi. YOLO9000: better, faster,                 Xu, Wei Zhang, Zhenguo Li, Chunjing Xu, and Hang Xu.
     stronger. In CVPR, pages 6517–6525, 2017. 2                              Detclip: Dictionary-enriched visual-concept paralleled pre-
[41] Joseph Redmon and Ali Farhadi. Yolov3: An incremental                    training for open-world detection. In NeurIPS, 2022. 1, 2, 3,
     improvement. CoRR, abs/1804.02767, 2018. 2                               6, 7
[42] Joseph Redmon, Santosh Kumar Divvala, Ross B. Girshick,             [57] Lewei Yao, Jianhua Han, Xiaodan Liang, Dan Xu, Wei
     and Ali Farhadi. You only look once: Unified, real-time ob-              Zhang, Zhenguo Li, and Hang Xu. Detclipv2: Scal-
     ject detection. In CVPR, pages 779–788, 2016. 2, 3                       able open-vocabulary object detection pre-training via word-

                                                                    12
     region alignment. In CVPR, pages 23497–23506, 2023. 1, 3,            where cat is the concentration and MP(·, 3) denotes the
     6                                                                    max pooling for 3 × 3 output features. {X3 , X4 , X5 } are
[58] Alireza Zareian, Kevin Dela Rosa, Derek Hao Hu, and Shih-            the multi-scale features in RepVL-PAN. X̃ is flattened and
     Fu Chang. Open-vocabulary object detection using captions.           has the shape of B × D × 27. Then we can update the text
     In CVPR, pages 14393–14402, 2021. 1, 2, 3                            embeddings by:
[59] Haotian Zhang, Pengchuan Zhang, Xiaowei Hu, Yen-Chun
     Chen, Liunian Harold Li, Xiyang Dai, Lijuan Wang, Lu                    W ′ = W + Softmax(W ⊙ X̃), dim=-1) ⊙ W,                    (6)
     Yuan, Jenq-Neng Hwang, and Jianfeng Gao. Glipv2: Uni-
     fying localization and vision-language understanding. In             A.2. Fine-tuning Details.
     NeurIPS, 2022. 1, 2, 3, 6, 7
[60] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun
                                                                          We remove all T-CSPLayers and Image-Pooling Atten-
     Zhu, Lionel M. Ni, and Heung-Yeung Shum. DINO: DETR                  tion in RepVL-PAN when transferring YOLO-World to
     with improved denoising anchor boxes for end-to-end object           COCO [26] object detection, which only contains 80 cat-
     detection. In ICLR, 2023. 3                                          egories and has a relatively low dependency on visual-
[61] Shifeng Zhang, Cheng Chi, Yongqiang Yao, Zhen Lei, and               language interaction. During fine-tuning, we initialize
     Stan Z. Li. Bridging the gap between anchor-based and                YOLO-World using pre-trained weights. The learning rate
     anchor-free detection via adaptive training sample selection.        of fine-tuning is set to 0.0002 with the weight decay set to
     In CVPR, pages 9756–9765, 2020. 2, 3                                 0.05. After fine-tuning, we pre-compute the class text em-
[62] Yiwu Zhong, Jianwei Yang, Pengchuan Zhang, Chunyuan                  beddings with given COCO categories and store the embed-
     Li, Noel Codella, Liunian Harold Li, Luowei Zhou, Xiyang             dings into the weights of the classification layers.
     Dai, Lu Yuan, Yin Li, and Jianfeng Gao. Regionclip:
     Region-based language-image pretraining. In CVPR, pages              B. Automatic Labeling on Large-scale Image-
     16772–16782, 2022. 3, 8
[63] Xingyi Zhou, Rohit Girdhar, Armand Joulin, Philipp
                                                                              Text Data
     Krähenbühl, and Ishan Misra. Detecting twenty-thousand             In this section, we add details procedures for labeling
     classes using image-level supervision. In ECCV, pages 350–           region-text pairs with large-scale image-text data, e.g.,
     368, 2022. 3, 7, 8
                                                                          CC3M [47]. The overall labeling pipeline is illustrated in
[64] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang,
                                                                          Fig. 8, which mainly consists of three procedures, i.e., (1)
     and Jifeng Dai. Deformable DETR: deformable transformers
                                                                          extract object nouns, (2) pseudo labeling, and (3) filtering.
     for end-to-end object detection. In ICLR, 2021. 2
                                                                          As discussed in Sec. 3.4, we adopt the simple n-gram algo-
                                                                          rithm to extract nouns from captions.
A. Additional Details
A.1. Re-parameterization for RepVL-PAN                                    Region-Text Proposals. After obtaining the set of object
                                                                          nouns T = {tk }K from the first step, we leverage a pre-
During inference on an offline vocabulary, we adopt re-                   trained open-vocabulary detector, i.e., GLIP-L [24], to gen-
parameterization for RepVL-PAN for faster inference speed                 erate pseudo boxes {Bi } along with confidence scores {ci }:
and deployment. Firstly, we pre-compute the text embed-
dings W ∈ RC×D through the text encoder.                                           {Bi , ti , ci }N
                                                                                                  i=1 = GLIP-Labeler(I, T ),            (7)

                                                                          where {Bi , ti , ci }N
                                                                                               i=1 are the coarse region-text proposals.
Re-parameterize T-CSPLayer. For each T-CSPLayer in
RepVL-PAN, we can re-parameterize and simplify the pro-
cess of adding text guidance by reshaping the text embed-                 CLIP-based Re-scoring & Filtering. Considering the
dings W ∈ RC×D×1×1 into the weights of a 1 × 1 convo-                     region-text proposals containing much noise, we present
lution layer (or a linear layer), as follows:                             a restoring and filtering pipeline with the pre-trained
                                                                          CLIP [39]. Given the input image I, caption T , and
 X ′ = X ⊙ Sigmoid(max(Conv(X, W ), dim=1)), (4)                          the coarse region-text proposals {Bi , ti , ci }N
                                                                                                                          i=1 , the specific
                                                                          pipeline is listed as follows:
where X× ∈ RB×D×H×W and X ′ ∈ RB×D×H×W are                                • (1) Compute Image-Text Score: we forward the image I
the input and output image features. ⊙ is the matrix multi-                 with its caption T into CLIP and obtain the image-text
plication with reshape or transpose.                                        similarity score simg .
                                                                          • (2) Compute Region-Text Score: we crop the region im-
Re-parameterize I-Pooling Attention. The I-Pooling                          ages from the input image according to the region boxes
Attention can be re-parameterize or simplified by:                          {Bi }. Then we forward the cropped images along with
                                                                            their texts {ti } into CLIP and obtain the region-text simi-
       X̃ = cat(MP(X3 , 3), MP(X4 , 3), MP(X5 , 3)),          (5)           larity S r = {sri }Ni=1 .

                                                                     13
       Automatic Labeling Pipeline

                          “A photography of a man
                               and a woman”

                                                    nouns   Open-Vocabulary     boxes
                                  n-gram                                                   CLIP Labeler
                                                                Labeler

                                  caption                       image                   image, object nouns
                          Extracting Object Nouns           Pseudo Labeling             CLIP-based Filtering

Figure 8. Labeling Pipeline for Image-Text Data We first leverage the simple n-gram to extract object nouns from the captions. We adopt
a pre-trained open-vocabulary detector to generate pseudo boxes given the object nouns, which forms the coarse region-text proposals.
Then we use a pre-trained CLIP to rescore or relabel the boxes along with filtering.

                                   objects
• (3) [Optional] Re-Labeling: we can forward each                       on rare categories (APr ). However, using fine-grained an-
  cropped image with all nouns and assign the noun with                 notations (GoldG) for small models can provide significant
  maximum similarity, which can help correct the texts                  improvements, which indicates that large-scale high-quality
  wrongly labeled by GLIP.                                              annotated data can significantly enhance the capabilities of
• (4) Rescoring: we adopt the region-text
                                        p similarity   S r to           small models. And Tab. 3 in the main text has shown that
  rescore the confidence scores c˜i = ci ∗ si .r                        pre-training with the combination of fine-annotated data
• (5) Region-level Filtering: we first divide the region-text           and pseudo-annotated data can perform better. We will ex-
  proposals into different groups according to the texts and            plore more about the data for pre-training small models or
  then perform non-maximum suppression (NMS) to fil-                    YOLO detectors in future work.
  ter the duplicate predictions (the NMS threshold is set to
  0.5). Then we filter out the proposals with low confidence
  scores (the threshold is set to 0.3).
• (6) Image-level Filtering: we compute the image-level
  region-text scores sregion by averaging the kept region-
  text scores. Then
                  √ we obtain the image-level confidence
  score by s = simg ∗ sregion and we keep the images
  with scores larger than 0.3.
The thresholds mentioned above are empirically set accord-
ing to the part of labeled results and the whole pipeline is
automatic without human verification. Finally, the labeled
samples are used for pre-training YOLO-World. We will
provide the pseudo annotations of CC3M for further re-
search.

C. Pre-training YOLO-World at Scale
When pre-training small models, e.g., YOLO-World-S, a
natural question we have is: how much capacity does a
small model have, and how much training data or what kind
of data does a small model need? To answer this question,
we leverage different amounts of pseudo-labeled region-text
pairs to pre-train YOLO-World. As shown in Tab. 9, adding
more image-text samples can increase the zero-shot per-
formance of YOLO-World-S. Tab. 9 indicates: (1) adding
image-text data can improve the overall zero-shot perfor-
mance of YOLO-World-S; (2) using an excessive amount
of pseudo-labeled data may have some negative effects for
small models (YOLO-World-S), though it can improve the

                                                                  14
                       Method              Pre-trained Data          Samples   AP     APr     APc     APf
                       YOLO-World-S        O365                       0.61M    16.3    9.2    14.1    20.1
                       YOLO-World-S        O365+GoldG                 1.38M    24.2   16.4    21.7    27.8
                       YOLO-World-S        O365+CC3M-245k             0.85M    16.5   10.8    14.8    19.1
                       YOLO-World-S        O365+CC3M-520k             1.13M    19.2   10.7    17.4    22.4
                       YOLO-World-S        O365+CC3M-750k             1.36M    18.2   11.2    16.0    21.1

Table 9. Zero-shot Evaluation on LVIS. We evaluate the performance of pre-training YOLO-World-S with different amounts of data, the
image-text data.

                                                                15
