---
source_id: 194
bibtex_key: huang2026ledetr
title: Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design
year: 2026
domain_theme: Fondasi RGB
verified_pdf: 194_Le-DETR Encoder Efisien untuk DETR Real-Time.pdf
char_count: 75624
---

Revisiting Real-Time Detection Transformer with Efficient Encoder Design

                                                   Jiannan Huang1        Aditya Kane1 Fengzhe Zhou1 Yunchao Wei2 Humphrey Shi1
                                                                     1
                                                                       SHI Labs @ Georgia Tech 2 Beijing Jiaotong University

                                                                  Abstract                                                           MS COCO Object Detection
                                                                                                                            55
arXiv:2602.21010v1 [cs.CV] 24 Feb 2026

                                         Real-time object detection is crucial for real-world applica-
                                         tions as it requires high accuracy with low latency. While De-
                                         tection Transformers (DETR) have demonstrated significant                          54

                                                                                                              COCO AP (%)
                                         performance improvements, current real-time DETR models
                                         are challenging to reproduce from scratch due to excessive                         53
                                         pre-training overheads on the backbone, constraining re-                                                                      YOLOv8
                                         search advancements by hindering the exploration of novel                                                                     YOLOv9
                                                                                                                            52                                         YOLOv10
                                         backbone architectures. In this paper, we want to show that                                                                   YOLOv11
                                                                                                                                                                       YOLOv12
                                         by using general good design, it is possible to have high per-                                                                RT-DETRv2
                                         formance with low pre-training cost. After a thorough study                        51                                         D-FINE
                                                                                                                                                                       DEIM-D-FINE
                                         of the backbone architecture, we propose EfficientNAT at var-                                                                 Le-DETR
                                         ious scales, which incorporates modern efficient convolution                            4       5          6         7          8
                                         and local attention mechanisms. Moreover, we re-design the                                          Latency (ms)
                                         hybrid encoder with local attention, significantly enhancing
                                         both performance and inference speed. Based on these ad-               Figure 1. The performance of each model. The results show that
                                         vancements, we present Le-DETR (Low-cost and Efficient                 our model outperforms the existing models and achieves a new
                                         DEtection TRansformer), which achieves a new SOTA in                   SOTA for real-time detection models. These results are tested using
                                                                                                                vanilla PyTorch profiler on 1×RTX4090.
                                         real-time detection using only ImageNet1K and COCO2017
                                         training datasets, saving about 80% images in pre-training
                                         stage compared with previous methods. We demonstrate                  In parallel, transformer-based detection models, such as the
                                         that with well-designed, real-time DETR models can achieve            DETR [23, 25, 44, 46, 48], have shown powerful perfor-
                                         strong performance without the need for complex and com-              mance by eliminating complex post-processing steps, partic-
                                         putationally expensive pretraining. Extensive experiments             ularly Non-Maximum Suppression (NMS) [10], which has
                                         show that Le-DETR-M/L/X achieves 52.9/54.3/55.1 mAP on                become a key bottleneck in accelerating inference. Several
                                         COCO Val2017 with 4.45/5.01/6.68 ms on an RTX4090. It                 end-to-end models [23, 35, 39, 44] have made significant
                                         surpasses YOLOv12-L/X by +0.6/-0.1 mAP while achieving                progress in the field of real-time object detection.
                                         similar speed and +20% speedup. Compared with DEIM-D-                    Although transformer-based real-time detectors demon-
                                         FINE, Le-DETR-M achieves +0.2 mAP with slightly faster                strate such impressive performance, they are challenging
                                         inference, and surpasses DEIM-D-FINE-L by +0.4 mAP                    to reproduce from scratch and improve due to the exces-
                                         with only 0.4 ms additional latency. Code and weights will            sive pertaining overheads in the backbone. As illustrated in
                                         be open-sourced.                                                      Fig. 2, real-time DETR models require an additional four
                                                                                                               million images [4], approximately four times the size of the
                                                                                                               ImageNet 1K pretraining dataset. Furthermore, these mod-
                                         1. Introduction                                                       els depend on long knowledge distillation schedules, which
                                                                                                               require higher computational overheads [4] to complete the
                                         The rapid advancements in deep learning have facilitated the          pretraining process. We ablate the key changes comparing
                                         development of highly effective real-time object detectors,           with ResNet50 and ResNet50 vd ssld [4, 16], which is used
                                         most notably exemplified by the YOLO series [19, 29, 32, 35–          by RT-DETRv2-L as backbone:(1) Variants from ResNet50
                                         37, 39, 40, 42, 43, 45]. These models have significantly              to ResNet50-D; (2) Computationally expensive pre-training
                                         advanced the field by demonstrating the efficacy of Convo-            technologies. Results of Tab. 1 illustrates that a significant
                                         lutional Neural Networks (CNNs) in real-time applications.            portion of their strong performance is derived from the sub-

                                                                                                          1
                                                                                                                      Decoder
                                                                                                                      Architecture
                                                             RT-DETRs                                                 Training Objectives
                                                             Le-DETR
      Real-time DETR Models
                                                                              Enc     Dec
            Long Knowledge
          Distillation Schedules

         Additional 4M Images

                                                                                                                   Encoder design can also
                     Le-DETR                                                                                       save pre-training cost.

           1M ImageNet1K
                                                                              Enc     Dec

                                         Training Latency mAP
                                        Overheads

Figure 2. Left: Comparison of Le-DETR and Real-Time DETR series in training overheads, While saving lots of training overheads offered
by efficient encoder design, our model outperforms the previous SOTA model, D-FINE and DEIM-D-FINE.Right: Unlike previous works
such as DEIM and D-FINE mainly focus on decoder architecture and training objects, we focus on efficient encoder design.

stantial pre-training overhead (KD &ATI). This creates a              Conv feed-forward network (FFN) to enhance feature pro-
significant barrier, effectively locking the community into           cessing. Also, guided by previous work [2, 12, 26], we
specific, costly pre-training pipelines. It leads to a criti-         conducted a detailed backbone study to explore optimal
cal research question: Is this massive pre-training overhead          backbone design choices. In addition, the hybrid encoder in-
a fundamental requirement for advanced performance, or                corporates the Neighborhood Attention-based Improved Fea-
is it merely a compensation for sub-optimal architectural             ture Inference (NAIFI) module, which is designed to strike
designs in current models? As shown in Fig. 2, though                 an optimal balance between performance and latency by cap-
previous works like DEIM, and D-FINE focus majorly on                 italizing on the advantages of Neighborhood Attention, also
decoder architecture and training objectives, we hypothesize          our models benefit from well-established implementations
that superior architectural design can break this dependency,         from the community.
achieving advanced performance using only ImageNet-1K                     Extensive experiments demonstrate that our model ex-
pre-training.                                                         hibits remarkable performance, establishing a new SOTA
   We found that the architectural modifications introduced           in real-time object detection, with saving 3M, about 80%
by real-time DETR models primarily focus on CNN-style                 images for pre-traing the backbone, showing that the exces-
detection techniques, such as the FPN-PAN [20, 21] and                sive pre-training overheads are not necessary for advanced
the RepVGG-C3 block [7]. However, there is a lack of em-              performance. Specifically, Le-DETR-M/L/X achieves
phasis on modern attention techniques, specifically local             52.9/54.3/55.1 mAP and 4.73/5.01/6.68 ms on an RTX4090.
attention [11–13], which limits models’ ability to achieve            As shown in Fig. 1, compared with previous SOTA in yolo
good performance. This limitation arises from slow infer-             series, it outpeforms YOLOv12-L/X by 0.6, -0.1 mAP by
ence of attention mechanisms and insufficient exploitation            having -0.02%, 20% speedup, respectively. Compared to
of localized features.                                                previous SOTA in DETR series, it outpeforms DEIM-D-
                                                                      FINE-M by 0.2 mAP with slightly speedup, LE-DETR-X
   In this paper, we demonstrate that the key to low-cost,
                                                                      out perform DEIM-D-FINE-L by 0.4 mAP with only 0.4 ms
high-performance real-time detection lies in the architectural
                                                                      slower. Extensive ablation experiments validate the effec-
design itself. By using general good design, it is possible to
                                                                      tiveness and non-redundancy of our proposed improvements,
have advanced performance while having low pre-training
                                                                      and experiments on the backbone scale design investigated
overheads. To this end, we propose Le-DETR (Low-Cost
                                                                      how to scale up and scale down the EfficientNAT efficiently.
and Efficient DEtection TRansformer). Our method is de-
signed to significantly reduce the cost of training a real-time       To be summarized, our contributions are as follows:
DETR model from scratch while having SOTA performance.                • We identify a commonly overlooked limitation of real-time
Le-DETR leverages local attention techniques to improve                  DETR models: their substantial pre-training overheads on
the model performance and speed up the inference process.                backbone, which have hindered further innovation within
Within this backbone, we introduce a novel EfficientNAT                  the research community. We show that even not specially
module that integrates Neighborhood Attention with an MB-                design for low pre-training data, it is possible to have

                                                                  2
               Model              KD & ATI      Variant    Pretraining Image Nums        Latency(ms)        APval
                                      ✓            ✓                    5M                    5.46           53.4
               RT-DETRv2-L            ✗            ✓                    1M                    5.46        51.6 (↓1.8)
                                      ✗            ✗                    1M                    4.91        51.6 (↓1.8)
               Le-DETR-L               ✗           ✗                    1M                    5.01           54.3

Table 1. This table presents the performance of the RT-DETRv2 models without the use of knowledge distillation (KD) techniques
and additional training images (ATI) for backbone pretraining. Variant means whether to use ResNet50-D [16]. When compared to
RT-DETRv2-L, our model achieves a +0.9 mAP improvement. Under identical pre-training settings, the performance gap further widens,
with our model surpassing RT-DETRv2-L by +2.7 mAP.

  SOTA performance with only pre-training on ImageNet1K,              the community from further improving models. Our work
  reducing ∼80% training images. It can boost reproducibil-           focuses on using modern attention technologies to design a
  ity and architectural innovation in this field.                     new model to further improve the reproducibility and perfor-
• We propose a novel backbone for real-time detection that            mance of transformer-based real-time detection models.
  substantially reduces the computational costs associated
  with enhancing DETR models after a detailed backbone                2.2. Efficient Attention
  study.
• We show that local attention is effective in real-time detec-       Attention [38] has proven to be a highly effective mech-
  tion. Using local attention, we redesign the encoder of the         anism for capturing long-range dependencies and enhanc-
  model to enhance the performance of Le-DETR.                        ing feature representation in models. In addition, it helps
                                                                      transformer-based models show a powerful scaling capa-
2. Related Works                                                      bility. Previous work has also demonstrated the power of
                                                                      attentional mechanisms in computer vision. The Vision
2.1. Real-Time Detection
                                                                      Transformer (ViT) [8] introduced a fully attention-based
Real-time detection aims at localizing and classifying objects        architecture, showing that transformers could outperform
in given images with low latency. Due to the high speed and           traditional convolutional networks in image classification by
powerful performance of model inference, real-time detec-             capturing global dependencies. Building on this, the Swin
tion models are crucial in real-world applications. Extensive         Transformer [22] utilized a hierarchical structure with shifted
works [1, 17, 19, 23, 27–29, 36, 37, 39, 40, 42–45, 48] have          windows, enabling attention to be computed efficiently in a
explored the field of real-time detection. Specifically, the          local context while still capturing global information. Fur-
YOLO series models show powerful performance. The mod-                thermore, the Detection Transformer (DETR) [46, 48, 49]
els of YOLOv1 [27], YOLOv2 [29], and YOLOv3 [28] form                 revolutionized object detection by formulating it as a set pre-
the paradigm of modern real-time detectors: backbone, neck,           diction problem, eliminating the need for traditional anchors
and head. YOLOv5 [36] mainly increases model perfor-                  and post-processing steps through the use of transformer-
mance by introducing CSPNet [41]. YOLOv8 [37] incorpo-                based attention, thereby simplifying the detection pipeline.
rated transformer-based layers and introduced C2F blocks,             However, self-attention is slow because its computational
enhancing the extraction of features for improved precision           complexity scales quadratically with the input size, requir-
in complex environments. YOLOv10 [39] introduced a two-               ing O(n2 ) operations to compute attention weights for all
stage supervision to build a NMS-free [9] detection model.            pairs of input tokens. Specifically, a BMM-style implemen-
Beyond conv-based YOLO series models, transformer-based               tation of self-attention – one having back-to-back matrix
real-time detection models show powerful performance. RT-             multiplications with softmax in between – is slowed down
DETR [48] outperforms YOLOv8 [37] mainly by replacing                 due to an excessive number of slow read/writes to global
the original Deformable DETR [49] decoder in DINO [3, 46]             memory. Much work [5, 6, 11–13, 18, 30] has explored
with the widely used FPN-PAN [20, 21] network and a novel             how to accelerate self-attention-based raining and inference.
RepVGG [7] block. RTDETR-v2 [23] further improved per-                Fused attention [5, 6, 30] accelerates self-attention by fusing
formance by setting up a set of bag-of-freebies. Although             the matrix multiplications and softmax into a single kernel,
real-time DETR models have made great progress, they al-              thereby reducing global memory read/writes while being
ways focus on integrating advanced technologies in object             functionally equivalent and reducing the quadratic complex-
detection, while lacking consideration of advanced efficient          ity without sacrificing accuracy. Specifically, Neighborhood
transformer technologies. In addition, they highly rely on a          Attention [11–14] reduces computational overhead by fo-
backbone that is trained with large amounts of data, the com-         cusing attention on a fixed local window, limiting the scope
plex training strategies, and expensive training costs hinder         to nearby elements while maintaining spatial context.

                                                                  3
                                                                                                                   EfficientNAT Backbone
                                                                             x L1                     x L2                x L3                         x L4

                                                               FusedMBConv

                                                                                        FusedMBConv

                                                                                                                                             EfficientNAT
                                                                                                                 MBConv

                                                                                                                                   MBConv
                                             DSConv

                                                                                                                                                                                  NAIFI
                                                                                                                                                 Block
                                     Conv

                                            DETR Decoder                                                     FeatureFusion

Figure 3. The proposed Le-DETR is structured in three distinct stages: backbone, encoder, and decoder. Each first block of stages in this
backbone serves as the downsampling block. In this figure, we also illustrate the encoder, which incorporates both the NAIFI and Feature
Fusion components.

         EfficientNATBlock                            NAIFI                                       are:
                                                                                                                                   Qi KρT1 (i) + B(i, ρ1 (i))
                                                                                                                                                             
                                                                                                                                        T
                                                                                                                                  Qi Kρ (i) + B(i, ρ2 (i)) 
                Neighborhood                      Neighborhood                                                                           2
                                                                                                                           Aki =                                                             (1)
                                                                                                                                                             
   Identity       Attention                         Attention                                                                                   ..            
                                                                                                                                                .            
                                                                                                                                     Qi KρTk (i) + B(i, ρk (i))
                  MBConv                              Linear
    Identity       FFN                                 FFN                                          And ρj (i) denotes i’s j-th nearest neighbor, The attention
                                                                                                 weight is computed as the dot product between the query
                                                                                                 of the i-th input and its k nearest neighboring keys. The
                                                                                                 neighboring values, Vik , are then defined as a matrix whose
Figure 4. Overview of EfficientNATBlock and Neighborhood                                         rows are the value projections of the k nearest neighbors of
Attention-based Improved Feature Inference(NAIFI).
                                                                                                 the i-th input:

3. Method                                                                                                             h                                                            iT
                                                                                                                 Vik = VρT1 (i)             VρT2 (i)          ···     VρTk (i)            .   (2)
3.1. Preliminary
Neighborhood Attention Neighborhood Attention (NA)                                                  Neighborhood Attention for the i-th token with neighbor-
[12] is an approach within the attention framework, em-                                           hood size k is then defined as:
phasizing localized feature aggregation by concentrating
                                                                                                                                                                Aki
                                                                                                                                                                     
attention on a small, spatial neighborhood around each query                                                                 NAk (i) = softmax                  √         Vik .               (3)
position. Unlike standard attention mechanisms, which con-                                                                                                        d
sider all possible context positions, NA reduces theoretical                                      3.2. Analysis of Pretraining on Backbone
computational complexity by limiting the scope of attention
to relevant, proximal areas. This method leverages spatial                                        Compared to real-time DETR models and the DETR [3],
correlations more efficiently and improves both computa-                                          a significant distinction is the reliance on extensively pre-
tional efficiency and the preservation of local structural in-                                    trained backbones in addition to modifications made to the
formation. Given an input X ∈ Rn×d , where X is a matrix                                          DETR encoder [4, 23]. Specifically, these detection mod-
whose rows are d-dimensional token vectors. Linear projec-                                        els only employ PResNet50/101 vd ssld [4, 16]1 , or PP-
tions are applied to obtain Q, K, and V from X. With these                                        HGNet v2 ssld [4]2 instead of ResNet50 as their backbone.
projections and relative positional biases B(i, j), the atten-                                           1 https://paddleclas.readthedocs.io/en/latest/models/ResNet and vd en.html
tion weights for the i-th input with a neighborhood size k,                                         2 https://github.com/PaddlePaddle/PaddleClas/blob/release/2.6/docs/en/models/PP-

denoted as Aki , are defined, and its k nearest neighborhood                                      HGNet en.md

                                                                                    4
Such backbone [4] is initially pre-trained on a dataset com-         tency and performance on ImageNet1K. To further enhance
prising four million filtered unlabeled images, followed by          inference speed and model performance, we investigate the
fine-tuning on ImageNet1K, which includes about one mil-             use of neighborhood attention, a variant of local attention,
lion images. This approach substantially increases the com-          in our proposed backbone to extract more robust features
putational and data pre-training overheads for training a            in the final stage. This leads to the development of our pro-
real-time detection model from scratch, as shown in Fig. 2.          posed EfficientNAT. The EfficientNAT architecture achieves
Although the pre-trained weights derived from these complex          these objectives by incorporating several efficient convolu-
pipelines enable high performance, they also pose challenges         tional operations in the first three stages, culminating in an
for researchers aiming to improve model efficiency and per-          attention module in the fourth and final stage. Specifically,
formance, as the reliance on such large-scale pre-training           we employ depthwise separable convolutions (DSConv) in
pipelines complicates replication, experimentation, and in-          the network’s stem to project input images into a feature
novation. Also, the 4M unlabeled filtered images are not             space. Consistent with common practices [2, 33, 47], we
open-sourced, which hinders the fair comparison and further          utilize Fused Mobile Convolution in the first two stages and
improvement by the community. Consequently, the current              standard Mobile Convolution in deeper stages, resulting in
real-time DETR models are largely confined to using either           progressively smaller feature maps with an increasing num-
PP-HGNetv2 or PResNet as the backbone [23, 25, 44, 48],              ber of channels. The first block in each stage functions as a
thereby limiting the exploration of novel backbone designs           downsampling layer, halving the spatial dimensions while
and hindering potential advancements in the field.                   doubling the number of channels. In the final stage of our
   In contrast, the widely adopted and cost-effective training       architecture, a Mobile Convolution (MBConv) downsam-
approach within the community involves pre-training solely           pling module, initiates the process, followed by a series of
on ImageNet1K, which contains approximately one million              EfficientNAT blocks. The EfficientNATBlock module com-
labeled images—only one-fifth of the data used by previous           bines Neighborhood Attention with an MBConv, serving
real-time DETR models, as shown in Fig. 2. In this paper,            as a Feed-Forward Network (FFN) to function as a highly
we want to answer one question: Is it possible to have SOTA          efficient yet powerful feature extractor.
performance while having low pre-training cost? In the
following section, we show that through careful backbone
design and study, and comprehensive re-design of the overall
model architecture, it is possible.
                                                                     Backbone Architecture Design To ensure the designed
3.3. Overview of Le-DETR                                             backbone achieves both high throughput and strong per-
                                                                     formance, model architecture—particularly the number of
Le-DETR follows the standard design paradigm of real-time            blocks per stage—is crucial. To efficiently scale the back-
DETR models, comprising an efficient backbone, an encoder,           bone up or down for variants of SOTA detection models,
and a decoder. As shown in Fig. 3, it provides a compre-             we conduct a detailed design study to determine the optimal
hensive overview of the proposed Le-DETR. In Section 3.4,            architecture. Specifically, in line with common practices in
we detail the architecture of our efficient backbone, termed         the community, there are three prominent patterns for scaling
EfficientNAT, which is carefully designed. Out of its per-           the model up or down: A balanced distribution [2]: the third
formance, we can get comparable performance with lower               and fourth stages have the same number of blocks, notated as
pre-training cost. Furthermore, in Section 3.5, we describe          PA , a late-stage heavy distribution [26]: the fourth stage has
how local attention mechanisms are employed in both the              more blocks than the third, notated as PB , and an early-stage
encoder and decoder. This dual emphasis on efficiency and            heavy distribution [11, 12, 15, 26]: the third stage has more
performance positions Le-DETR as a leading approach in               blocks than the fourth, notated as PC . To the best of our
real-time detection models.                                          knowledge, there is no established principle to accurately
                                                                     deduce which pattern is best for each model scale without
3.4. EfficientNAT Backbone
                                                                     any empirical experiments. Therefore, we conduct multi-
Architecture Design As shown in Tab. 1, the existing back-           ple experiments to identify the best pattern for each scale.
bone is not sufficient to have good performance with low             Detailed experimental design principle and quantitative ex-
pre-training overheads. As a consequence, reducing pre-              periment results are shown in Section 4.3.2. Based on the
training overhead while achieving improved performance               experimental results, we find that when scaling EfficientNAT
requires the introduction of a well-designed backbone capa-          to a large scale (X), using more blocks in the third stage (PC )
ble of both low-latency inference and the extraction of robust       yields better performance, while using the same number of
multi-scale image features for the encoder. We begin design-         blocks in the third and fourth stages (PA ) performs better
ing our backbone based on EfficientViT [2, 47], a series of          for the smaller scale (L) model. Additionally, we apply this
SOTA backbones that strike an effective balance between la-          conclusion when designing the even smaller (M) model.

                                                                 5
    Models                     Params (M)      GFLOPs      Latency(ms)       APval    APval
                                                                                        50     APval
                                                                                                 75     APval
                                                                                                          S      APval
                                                                                                                   M      APval
                                                                                                                            L

                                                        YOLO Series Models
    YOLOv5-M [36]                  25.1         64.2           3.57          49.1      66.0     53.8     31.2     54.2     65.4
    YOLOv5-L [36]                  46.5         109.1           5.57         49.0      67.3      -        -        -        -
    YOLOv5-X [36]                  86.7         205.7           8.55         50.7      68.9      -        -        -        -
    YOLOv8-M [37]                  25.9         78.9            4.06         50.3      67.3     54.8     32.3     55.9     66.5
    YOLOv8-L [37]                  43.7         165.2           6.52         52.9      69.8     57.7     35.5     58.5     69.8
    YOLOv8-X [37]                  68.2         257.8           8.51         53.9      71.1     58.9     36.0     59.4     70.9
    YOLOv9-M [43]                  20.1         76.8            4.78         51.5      68.4     54.0     33.8     57.2     67.3
    YOLOv9-C [43]                  25.5         102.8           5.06         52.9      69.8     57.7     35.6     58.2     69.0
    YOLOv10-B [39]                 15.4         59.1            5.19         52.4      69.5     57.1     35.0     57.7     68.3
    YOLOv10-L [39]                 24.4         120.3           6.12         53.2      70.1     58.1     35.8     58.5     69.4
    YOLOv10-X [39]                 29.5         160.4           6.69         54.4      71.3     59.3     37.0     59.8     70.9
    YOLO11-M [35]                  20.1         68.0            3.67         51.5      68.5     55.7     33.4     57.1     67.9
    YOLO11-L [35]                  25.3         86.9            5.03         53.3      70.1     58.2     35.6     59.1     69.2
    YOLO11-X [35]                  56.9         194.9           7.75         54.6      71.6     59.5     37.7     59.7     70.2
    YOLOv12-M [34]                 20.2         67.5            3.38         52.5      69.6     57.1     35.7     58.2     68.8
    YOLOv12-L [34]                 26.4         88.9            4.89         53.7      70.7     58.5     36.9     59.5     69.9
    YOLOv12-X [34]                 59.1         199.0           8.22         55.2      72.0     60.2     39.6     60.7     70.9
    YOLOv13-L [34]                 27.6         88.4            7.33         53.4      70.9     58.1      -        -        -
    YOLOv13-X [34]                 64.0         199.2          11.89         54.8      72.0     59.8      -        -        -
                                                    Transformer-based Models
                    ∗
    RT-DETRv2-M [23]               36.6         100.3          4.49          51.9      69.9     56.5     33.5     56.8     69.2
    RT-DETRv2-L [23]               42.9         137.3          5.46          53.4      71.6     57.4     36.0     57.9     70.8
    RT-DETRv2-X [23]               76.5         260.0          8.54          54.3      72.8     58.8     35.8     58.8     72.1
    RT-DETRv3-M∗ [44]              36.6         100.3          4.49          51.7       -        -        -        -        -
    RT-DETRv3-L [44]               42.9         137.3          5.46          53.4       -        -        -        -        -
    RT-DETRv3-X [44]               76.5         260.0          8.54          54.6       -        -        -        -        -
    D-FINE-M [25]                  19.2          56.6          4.39          52.3      69.8     56.4     33.2     56.5     70.2
    D-FINE-L [25]                  30.7          91.0          6.21          54.0      71.6     58.4     36.5     58.0     71.9
    DEIM-D-FINE-M [31]             19.2          56.6          4.39          52.7      70.0     57.3     35.3     56.7     69.5
    DEIM-D-FINE-L [31]             30.7          91.0          6.21          54.7      72.4     59.4     36.9     59.6     71.8
    Le-DETR-M (Ours)               31.4         114.1          4.45          52.9      70.0     57.4     35.4     56.9     68.6
    Le-DETR-L (Ours)               41.5         124.3          5.01          54.3      71.7     58.9     37.1     58.7     71.4
    Le-DETR-X (Ours)               44.9         196.9          6.68          55.1      72.5     59.8     38.1     59.6     71.4

Table 2. Comparison of our proposed Le-DETR and previous SOTA object detection models on COCO Val 2017. Experiments show that our
model Le-DETR-X outperforms the previous SOTA YOLOs and DEIM.

3.5. NAIFI & DETR Decoder                                              a prediction head is assigned to each decoding layer during
                                                                       training, enabling the reduction of decoder layers used dur-
We want to explore how the hybrid encoder can benefit                  ing inference, which further optimizes the model’s efficiency.
from modern attention mechanisms, specifically, from lo-               And we use Flash Attention [5] in the decoder to speed up
cal attention. To this end, we introduce a redesigned at-              the self-attention inference process.
tention mechanism, termed Neighborhood Attention-based
Improved Feature Inference (NAIFI). NAIFI is a single-layer
neighborhood attention transformer designed to optimize fea-           4. Experiments
ture representation. This module not only improves feature
                                                                       4.1. Experimental Setup
extraction quality but also accelerates processing speed by
using a relatively small kernel size, thereby facilitating rapid       Implementation Details We follow the commonly DETR
inference. Additionally, within the DINO [46] framework,               training process, employing supervised pre-training on Ima-

                                                                   6
  Models                               Params (M)      GFLOPs          Latency(ms)     APval    APval
                                                                                                  50     APval
                                                                                                           75     APval
                                                                                                                    S      APval
                                                                                                                             M      APval
                                                                                                                                      L

  Le-DETR w/ ResNet50 vd ssld              43.8          128.3              5.80        53.6     71.4     58.0     35.5     58.3     70.9
  Le-DETR w/ EfficientViT                  64.7          135.7              6.60        53.8     71.5     58.6     36.8     58.1     71.3
  Le-DETR w/o NAIFI                        41.5          124.3              5.18        54.1     71.2     58.9     36.3     58.6     70.4
  Le-DETR (Ours Full Method)               41.5          124.3              5.01        54.3     71.7     58.9     37.1     58.7     71.4

Table 3. Ablation experiment of components in our proposed Le-DETR. These experiments show the effectiveness of each module by
offering both model performance improvement or speedup model inference while keeping the same performance.

 Model Name      Params(M)   GFLOPs    Latency(ms)   APval   APval
                                                               50            YOLO series models as well as end-to-end transformer-based
 Le-DETR-M   4
                   31.4       114.1        4.19      52.5    69.3            real-time detectors (RT-DETRs). Tab. 2 summarizes the ex-
 Le-DETR-M5        32.7       115.0        4.45      52.9    70.0            perimental results. Consistent with prior work, our analysis
 Le-DETR-M6        34.0       115.6        4.73      52.9    70.0
                                                                             focuses on models at the M, L and X scales. Notably, Le-
 Le-DETR-L4        38.8       122.6        4.53      53.7    70.9
 Le-DETR-L5        40.1       123.5        4.79      54.2    71.6            DETR-M achieves a mean Average Precision (mAP) of 52.4
 Le-DETR-L6        41.5       124.3        5.01      54.3    71.7            with a processing time of 4.45 ms when tested on an RTX
 Le-DETR-X4        42.3       195.2        6.10      54.6    71.8            4090, Le-DETR-L achieves 53.6 mAP and 5.01 ms, and
 Le-DETR-X5        43.6       196.0        6.42      54.9    72.3
                                                                             Le-DETR-X attains a mAP of 54.7 with a processing time of
 Le-DETR-X6        44.9       196.9        6.68      55.1    72.5
                                                                             6.68 ms on the same hardware. Compared with YOLO11-M,
Table 4. Results of the ablation experiments using different number          Le-DETR-M is 1.4 mAP better, and for YOLO11-L, Le-
of layers in the model decoder, we use six decoder layers for train-         DETR-L has 1.0 mAP better performance and comparable la-
ing, with corner labels corresponding to different inference layers.         tency, Le-DETR-X is 0.5mAP better than YOLO11-X, and it
                                                                             is 14% faster than it. Compared with YOLOv12, Le-DETR-
geNet1K and then training the model on COCO train2017                        M is 0.4 mAP better than YOLOv12-M, for YOLOv12-L,
dataset. For evaluation, we employ the COCO dataset.                         Le-DETR-L has 0.6mAP better performance with similar
Model performance is assessed using the traditional COCO                     latency, and Le-DETR-X is 20% fatser than YOLOv12-X
mean Average Precision (mAP) metric, which provides a                        with comparable performance. In comparison to SOTA real-
comprehensive measure of accuracy across various object                      time DETR models, Le-DETR-L has 0.7 mAP better perfor-
classes. To further elucidate the model’s capabilities, we                   mance than RT-DETRv2/v3-L while being 9% faster, with
report COCO mAP metrics at multiple scales, thereby evalu-                   Le-DETR-M is 1.0/1.2 mAP better. Similarly, Le-DETR-X
ating performance under different conditions. To accelerate                  outperforms RT-DETRv2-X by 0.8 mAP, RT-DETRv3 by
inference, we adopt a 5-layer decoder architecture in Le-                    0.5 mAP and is 22% faster speed than RT-DETR-v2/v3-X.
DETR-M. Within this decoder, we incorporate two training                     For D-FINE models, Le-DETR-M outperforms it by 0.6
enhancements from D-FINE [25]: Fine-grained Distribu-                        mAP and with only 0.3 ms slower. Le-DETR-L achieves
tion Refinement (FDR) and Global Optimal Localization                        a 0.3 mAP improvement over D-FINE-L and 20% faster.
Self-Distillation (GO-LSD). Also, wo use the Matchability-                   Compared with DEIM-D-FINE-M, Le-DETR-M is 0.2 mAP
Aware Loss (MAL), which is proposed by DEIM [31], as our                     better than it and faster, Le-DETR-X is 0.4 mAP better
training loss. Detailed hyper-parameters are in Appendix.                    thank DEIM-D-FINE-L with only 4% slower. Moreover,
Dataset & Metric To evaluate the performance of Le-DETR,                     Le-DETR offers a significant advantage in terms of repro-
we report detailed metrics including the total number of                     ducibility, as it can be trained from scratch with substantially
parameters and GFLOPs, which serve as indicators of the                      reduced pre-training overhead compared to existing real-time
model’s computational complexity. For latency testing, we                    DETR models due to the efficient encoder design.
measure inference delay using the PyTorch profiler in FP16                   4.3. Ablation Experiments
precision on an RTX 4090 GPU. In accordance with estab-
lished practices in real-time detection, we utilize an input                 4.3.1. Ablation experiments on individual components
shape of (640, 640) for both GFLOPs and latency bench-                       EfficientNAT Backbone We conducted two experiments
marks to ensure consistency with typical operational scenar-                 to assess the effectiveness of modifications to the back-
ios. Specifically, we employ the calc-flops repo [24] to                     bone. The first row of Tab. 3 presents the results for the
compute the GFLOPs and parameter counts of our model.                        proposed overall backbone. By replacing EfficientNAT with
                                                                             ResNet50 vd ssld, which is used in RT-DETR-v1/2/3, the
4.2. Quantitative Experiments                                                latency increases from 5.01 ms to 5.80 ms, while the mAP
In this section, we present a comparative analysis of our                    decreases from 54.3 to 53.6. This performance reduction
model against SOTA real-time detectors. Specifically, we                     is primarily due to the decline in mAPS and mAPM . Addi-
evaluate our approach in comparison to the well-established                  tionally, we compare our proposed EfficientNAT with the

                                                                        7
  Model Name      Block Number      Top1 Acc     Top5 Acc     Throughput                                                                    L-scale
                                                                                                   82.8                                     X-scale
       PA -1 ✓       (1, 1, 4, 4)    81.994       95.432          1798.75                                                                   PA
       PA -2         (1, 1, 6, 6)    82.135       95.302          1607.68                                                                   PB
  L                                                                                                82.6                                     PC
       PB            (1, 1, 4, 8)    82.046       94.972          1524.13                                                                   Final Choice

                                                                               Top1 Accuracy (%)
       PC           (1, 1, 10, 2)    81.946       95.494          1278.94
                                                                                                   82.4
       PA -1         (2, 2, 8, 8)    82.300       95.224          1247.82
       PA -2       (2, 2, 10, 10)    82.238       95.086          1166.25
                                                                                                   82.2
       PA -3       (2, 2, 12, 12)    82.083       94.906          1059.28
       PB -1        (2, 2, 8, 10)    82.178       95.008          1211.05
  X    PB -2        (2, 2, 4, 12)    82.152       94.840          1183.47                          82.0
       PB -3        (2, 2, 2, 15)    81.744       94.744          1162.34
       PC -1        (2, 2, 15, 2)    82.638       95.768          1058.14                          81.8
       PC -2 ✓      (2, 7, 15, 2)    82.902       95.960          1006.83
                                                                                                          1000   1200       1400     1600           1800
       PC -3        (2, 7, 18, 2)    82.750       95.890           950.25                                               Throughput

Table 5. We conducted experiments to explore different patterns on the backbone. As described in Section 3.4, we designed our backbone
scale study using three distinct patterns. These are referred to as PA , PB , and PC , corresponding to balanced distribution, late-stage heavy
distribution and an early-stage heavy distribution patterns, respectively. The results demonstrate that, for the L-scale, PA yields the best
performance, whereas PC for the X-scale. The images clearly show the preference of different patterns at different scales.

EfficientViT-L1. The second row of Tab. 3 shows the cor-                    ments using them on COCO. Experiment results show that
responding results. Using the EfficientViT-L1 as the back-                  they have the same mAP, while the model using PA -1 is
bone increases latency from 5.01 ms to 6.60 ms, while mAP                   faster (4.53 ms vs 4.96 ms). Thus, we chose PA -1 as our
decreases slightly from 54.3 to 53.8. These experiments                     final architecture. For the X scale, we observed PC -1 to
demonstrate the necessity for proposing a new backbone and                  outperform other configurations and thus scaled it to PC -2,
the performance of EfficientNAT.                                            which was chosen as our final configuration. However, we
NAIFI We replace the proposed NAIFI with the original                       found that scaling it to PC -3 resulted in a drop in accuracy.
AIFI, as introduced in RT-DETR, within the hybrid encoder.                  Finally, we choose PC -2 for X-scale. The figure in Tab. 5
The third row of Tab. 3 presents the results. When using                    clearly visualizes the pattern selection.
the original AIFI, mAP decreases from 54.3 to 54.1, while                   4.3.3. Ablation Experiments on Decoder Layers
latency increases from 5.01 ms to 5.18 ms. The experimen-                   To evaluate the model’s performance under different num-
tal results indicate that: (1) Using local attention instead of             bers of inference decoder layers, we conducted inference
self-attention reduces latency, thereby making the model in-                decoder layer ablation experiments. All models are first
ference process faster; and (2) Local attention in the encoder              trained using six decoder layers. Tab. 4 presents the results,
improves model performance. These findings demonstrate                      demonstrating that Le-DETR can flexibly adjust the trade-
the efficiency of our proposed NAIFI. We will discuss the                   off between accuracy and efficiency in practical applications.
selection of kernel type and size in the Appendix.                          Also, it shows that using 5 layers in decoder, Le-DETR-M
                                                                            has 0.26ms speedup without harming the performance.
4.3.2. Ablation Experiments on Backbone Design
In this section, we detail the backbone scale design process.               5. Conclusion
As described in Section 3.4, we categorize our experiments                  This paper introduces Le-DETR, an efficient real-time
into three patterns: PA , balanced distribution; PB , late-stage            object detection model that addresses key limitations
heavy distribution; and PC , early-stage heavy distribution                 of transformer-based detection architectures. Le-DETR
These architecture schemes are elucidated in Tab. 5. In each                reduces plenty of pre-training overheads while having
experiment, we aim to maintain a constant number of blocks                  great performance in real-time detection. Our experiments
in the first two stages, while exploring different combina-                 demonstrate that Le-DETR has a series of models with
tions to identify the optimal pattern for each scale. We started            SOTA performance, with Le-DETR-M achieving 52.9 mAP
from three patterns corresponding to each design principle –                and 4.45 ms, Le-DETR-L surpassing previous models
                                                                            by achieving 54.3 mAP with a 5.01 ms latency, and
PA -1, PB -1 and PC -1, and then modified the same to main-                 Le-DETR-X achieves 55.1 mAP with 6.68 ms latency. We
tain a decent throughput-accuracy balance. For the L scale,                 discuss the limitation in the appendix. Future research
we observed PA -1 to have high throughput, and acceptable                   could further optimize transformer-based models to
accuracy. Owing to this, we experimented with PA -2, which                  minimize or eliminate pre-training requirements, improving
performed the best but shows a relatively low throughput                    accessibility and reproducibility of real-time DETR models.
compared with PA -1. Furthermore, we conducted experi-

                                                                      8
References                                                                      Xu, Haicheng Wu, Wen mei Hwu, Ming-Yu Liu, and
                                                                                Humphrey Shi. Generalized neighborhood attention: Multi-
 [1] Alexey Bochkovskiy, Chien-Yao Wang, and Hong-Yuan Mark                     dimensional sparse attention at the speed of light, 2025. 3
     Liao. Yolov4: Optimal speed and accuracy of object detection.         [15] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     arXiv preprint arXiv:2004.10934, 2020. 3                                   Deep residual learning for image recognition, 2015. 5
 [2] Han Cai, Junyan Li, Muyan Hu, Chuang Gan, and Song                    [16] Tong He, Zhi Zhang, Hang Zhang, Zhongyue Zhang, Jun-
     Han. Efficientvit: Lightweight multi-scale attention for high-             yuan Xie, and Mu Li. Bag of tricks for image classification
     resolution dense prediction. In Proceedings of the IEEE/CVF                with convolutional neural networks. In Proceedings of the
     International Conference on Computer Vision, pages 17302–                  IEEE/CVF conference on computer vision and pattern recog-
     17313, 2023. 2, 5                                                          nition, pages 558–567, 2019. 1, 3, 4
 [3] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas            [17] Siyu Jiao, Hongguang Zhu, Jiannan Huang, Yao Zhao, Yun-
     Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-                 chao Wei, and Humphrey Shi. Collaborative vision-text repre-
     end object detection with transformers. In European confer-                sentation optimizing for open-vocabulary segmentation, 2024.
     ence on computer vision, pages 213–229. Springer, 2020. 3,                 3
     4                                                                     [18] Benjamin Lefaudeux, Francisco Massa, Diana Liskovich,
 [4] Cheng Cui, Ruoyu Guo, Yuning Du, Dongliang He, Fu Li,                      Wenhan Xiong, Vittorio Caggiano, Sean Naren, Min Xu, Jieru
     Zewu Wu, Qiwen Liu, Shilei Wen, Jizhou Huang, Xiaoguang                    Hu, Marta Tintore, Susan Zhang, Patrick Labatut, Daniel Haz-
     Hu, Dianhai Yu, Errui Ding, and Yanjun Ma. Beyond self-                    iza, Luca Wehrstedt, Jeremy Reizenstein, and Grigory Sizov.
     supervision: A simple yet effective network distillation alter-            xformers: A modular and hackable transformer modelling li-
     native to improve backbones, 2021. 1, 4, 5                                 brary. https://github.com/facebookresearch/
 [5] Tri Dao. Flashattention-2: Faster attention with bet-                      xformers, 2022. 3
     ter parallelism and work partitioning. arXiv preprint                 [19] Chuyi Li, Lulu Li, Hongliang Jiang, Kaiheng Weng, Yifei
     arXiv:2307.08691, 2023. 3, 6                                               Geng, Liang Li, Zaidan Ke, Qingyuan Li, Meng Cheng,
 [6] Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christo-                   Weiqiang Nie, et al. Yolov6: A single-stage object detec-
     pher Ré. Flashattention: Fast and memory-efficient exact                  tion framework for industrial applications. arXiv preprint
     attention with io-awareness. Advances in Neural Information                arXiv:2209.02976, 2022. 1, 3
     Processing Systems, 35:16344–16359, 2022. 3                           [20] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
 [7] Xiaohan Ding, Xiangyu Zhang, Ningning Ma, Jungong Han,                     Bharath Hariharan, and Serge Belongie. Feature pyramid
     Guiguang Ding, and Jian Sun. Repvgg: Making vgg-style                      networks for object detection. In Proceedings of the IEEE
     convnets great again. In Proceedings of the IEEE/CVF con-                  conference on computer vision and pattern recognition, pages
     ference on computer vision and pattern recognition, pages                  2117–2125, 2017. 2, 3
     13733–13742, 2021. 2, 3                                               [21] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia. Path
 [8] Alexey Dosovitskiy. An image is worth 16x16 words: Trans-                  aggregation network for instance segmentation. In Proceed-
     formers for image recognition at scale. arXiv preprint                     ings of the IEEE conference on computer vision and pattern
     arXiv:2010.11929, 2020. 3                                                  recognition, pages 8759–8768, 2018. 2, 3
 [9] Pedro F Felzenszwalb, Ross B Girshick, David McAllester,              [22] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng
     and Deva Ramanan. Object detection with discriminatively                   Zhang, Stephen Lin, and Baining Guo. Swin transformer:
     trained part-based models. IEEE transactions on pattern                    Hierarchical vision transformer using shifted windows. In
     analysis and machine intelligence, 32(9):1627–1645, 2009. 3                Proceedings of the IEEE/CVF international conference on
[10] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra                  computer vision, pages 10012–10022, 2021. 3
     Malik. Rich feature hierarchies for accurate object detection         [23] Wenyu Lv, Yian Zhao, Qinyao Chang, Kui Huang,
     and semantic segmentation. In 2014 IEEE Conference on                      Guanzhong Wang, and Yi Liu. Rt-detrv2: Improved base-
     Computer Vision and Pattern Recognition, pages 580–587,                    line with bag-of-freebies for real-time detection transformer.
     2014. 1                                                                    arXiv preprint arXiv:2407.17140, 2024. 1, 3, 4, 5, 6
[11] Ali Hassani and Humphrey Shi. Dilated neighborhood atten-             [24] MrYxJ. calculate-flops.pytorch, 2024. Accessed: 2024-11-05.
     tion transformer. arXiv preprint arXiv:2209.15001, 2022. 2,                7
     3, 5                                                                  [25] Yansong Peng, Hebei Li, Peixi Wu, Yueyi Zhang, Xiaoyan
[12] Ali Hassani, Steven Walton, Jiachen Li, Shen Li, and                       Sun, and Feng Wu. D-fine: Redefine regression task in detrs
     Humphrey Shi. Neighborhood attention transformer. In Pro-                  as fine-grained distribution refinement, 2024. 1, 5, 6, 7
     ceedings of the IEEE/CVF Conference on Computer Vision                [26] Ilija Radosavovic, Raj Prateek Kosaraju, Ross Girshick, Kaim-
     and Pattern Recognition, pages 6185–6194, 2023. 2, 4, 5                    ing He, and Piotr Dollár. Designing network design spaces. In
[13] Ali Hassani, Wen-Mei Hwu, and Humphrey Shi. Faster neigh-                  Proceedings of the IEEE/CVF conference on computer vision
     borhood attention: Reducing the o (nˆ 2) cost of self attention            and pattern recognition, pages 10428–10436, 2020. 2, 5
     at the threadblock level. arXiv preprint arXiv:2403.04690,            [27] J Redmon. You only look once: Unified, real-time object
     2024. 2, 3                                                                 detection. In Proceedings of the IEEE conference on computer
[14] Ali Hassani, Fengzhe Zhou, Aditya Kane, Jiannan Huang,                     vision and pattern recognition, 2016. 3
     Chieh-Yun Chen, Min Shi, Steven Walton, Markus Hoehner-               [28] Joseph Redmon. Yolov3: An incremental improvement. arXiv
     bach, Vijay Thakkar, Michael Isaev, Qinsheng Zhang, Bing                   preprint arXiv:1804.02767, 2018. 3

                                                                       9
[29] Joseph Redmon and Ali Farhadi. Yolo9000: better, faster,             [45] Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan
     stronger. In Proceedings of the IEEE conference on computer               Zhang, and Xiuyu Sun. Damo-yolo: A report on real-time
     vision and pattern recognition, pages 7263–7271, 2017. 1, 3               object detection design. arXiv preprint arXiv:2211.15444,
[30] Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar,                    2022. 1, 3
     Pradeep Ramani, and Tri Dao. Flashattention-3: Fast and              [46] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun
     accurate attention with asynchrony and low-precision. arXiv               Zhu, Lionel M Ni, and Heung-Yeung Shum. Dino: Detr
     preprint arXiv:2407.08608, 2024. 3                                        with improved denoising anchor boxes for end-to-end object
[31] Huang Shihua, Lu Zhichao, Cun Xiaodong, Yu Yongjun,                       detection. arXiv preprint arXiv:2203.03605, 2022. 1, 3, 6
     Zhou Xiao, and Shen Xi. Deim: Detr with improved matching            [47] Zhuoyang Zhang, Han Cai, and Song Han. Efficientvit-sam:
     for fast convergence, 2025. 6, 7                                          Accelerated segment anything model without performance
[32] Yunyun Song, Zhengyu Xie, Xinwei Wang, and Yingquan                       loss. arXiv preprint arXiv:2402.05008, 2024. 5
     Zou. Ms-yolo: Object detection based on yolov5 optimized             [48] Yian Zhao, Wenyu Lv, Shangliang Xu, Jinman Wei,
     fusion millimeter-wave radar and machine vision. IEEE Sen-                Guanzhong Wang, Qingqing Dang, Yi Liu, and Jie Chen.
     sors Journal, 22(15):15435–15447, 2022. 1                                 Detrs beat yolos on real-time object detection. In Proceed-
[33] Mingxing Tan and Quoc Le. Efficientnetv2: Smaller models                  ings of the IEEE/CVF Conference on Computer Vision and
     and faster training. In International conference on machine               Pattern Recognition, pages 16965–16974, 2024. 1, 3, 5
     learning, pages 10096–10106. PMLR, 2021. 5                           [49] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang
[34] Yunjie Tian, Qixiang Ye, and David Doermann. Yolov12:                     Wang, and Jifeng Dai. Deformable detr: Deformable trans-
     Attention-centric real-time object detectors. arXiv preprint              formers for end-to-end object detection. arXiv preprint
     arXiv:2502.12524, 2025. 6                                                 arXiv:2010.04159, 2020. 3
[35] Ultralytics.     Yolov11.     https : / / github . com /
     ultralytics/ultralytics, 2023. Accessed: 2024-
     10-25. 1, 6
[36] Ultralytics.      Yolov5.     https : / / github . com /
     ultralytics/yolov5, 2023. Accessed: 2024-10-25.
     3, 6
[37] Ultralytics.      Yolov5.     https : / / github . com /
     ultralytics/ultralytics, 2023. Accessed: 2024-
     10-25. 1, 3, 6
[38] A Vaswani. Attention is all you need. Advances in Neural
     Information Processing Systems, 2017. 3
[39] Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong
     Han, and Guiguang Ding. Yolov10: Real-time end-to-end
     object detection. arXiv preprint arXiv:2405.14458, 2024. 1,
     3, 6
[40] Chengcheng Wang, Wei He, Ying Nie, Jianyuan Guo, Chuan-
     jian Liu, Yunhe Wang, and Kai Han. Gold-yolo: Efficient
     object detector via gather-and-distribute mechanism. Ad-
     vances in Neural Information Processing Systems, 36, 2024.
     1, 3
[41] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,
     Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. Cspnet: A
     new backbone that can enhance learning capability of cnn. In
     Proceedings of the IEEE/CVF conference on computer vision
     and pattern recognition workshops, pages 390–391, 2020. 3
[42] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-Yuan Mark
     Liao. Yolov7: Trainable bag-of-freebies sets new state-of-
     the-art for real-time object detectors. In Proceedings of the
     IEEE/CVF conference on computer vision and pattern recog-
     nition, pages 7464–7475, 2023. 1, 3
[43] Chien-Yao Wang, I-Hau Yeh, and Hong-Yuan Mark Liao.
     Yolov9: Learning what you want to learn using programmable
     gradient information. arXiv preprint arXiv:2402.13616, 2024.
     1, 6
[44] Shuo Wang, Chunlong Xia, Feng Lv, and Yifeng Shi.
     Rt-detrv3: Real-time end-to-end object detection with
     hierarchical dense positive supervision. arXiv preprint
     arXiv:2409.08475, 2024. 1, 5, 6

                                                                     10
Appendix
A. Implementation Details
In this section, we present the implementation details and
training hyperparameters of Le-DETR. Detailed parameters
are presented in Tab. 6. Compared with previous real-time
DETR models, we have some slight modifications. First,
Le-DETR-X uses 256 as the embedding dimension in the
encoder, to align with the smaller dimension from our de-
signed backbone, which is 384 in previous X-scale real-time
DETR models. Also, the feedforward dimension is reduced
to 1024 in the X-scale model, keeping the same as it is in the
L-scale model. We use a larger total batch size to accelerate
training, and they can still be trained under 12GB GPU like
8 * 2080Ti. Along with the larger total training batch size,
we also use a larger base learning rate and a larger backbone
learning rate. We use AdmaW as the optimizer for both the
backbone pretraining and the coco training.

B. Limitation
Though we highly reduce the pre-training cost of real-time
transformer-based object detection models, making it return
to a low-cost process. It’s necessary to claim that the training
process of YOLO series models shows no need for any addi-
tional data except images of COCO train 2017. Though since
our Le-DETR needs fewer epochs to converge compared
with YOLO series models, so the overall training overhead
is similar, we expect new transformer-based models without
any pre-training. Also, the lack of neighborhood attention
on ONNX and TensorRT exports may naturally hinder the
practical application of our work on a small subset of cases,
and we look forward to this progress.

C. Visualization in hard scenarios
In this section, we present visualization results demonstrat-
ing the effectiveness of our proposed Le-DETR model in
handling challenging scenarios. To evaluate its robustness,
we sampled a set of difficult images from the COCO Val2017
dataset. These images are particularly challenging due to
the presence of one or more of the following conditions: a
high density of objects within a single image, poor lighting
conditions such as dim or blurred light, and motion blur,
among other complexities.
   Fig. 5 illustrates the detection results of the Le-DETR-
L model, while Fig. 6 showcases the performance of the
Le-DETR-X model. The visualizations clearly indicate that
our proposed model demonstrates strong capabilities in han-
dling these hard cases. Specifically, the Le-DETR models
effectively identify objects even under adverse conditions,
highlighting their robustness and reliability in complex ob-
ject detection tasks.

                                                                   11
COCO Training Settings                    Le-DETR-M                     Le-DETR-L                     Le-DETR-X
Backbone                                 EfficientNAT-M                EfficientNAT-L                EfficientNAT-X
Backbone Freezing Layer                        (0, 1)                        (0, 1)                        (0, 1)
Embedding Dimension                             256                           256                           256
Feedforward Dimension                          1024                          1024                          1024
Encoder Layer Number                              1                             1                             1
NAAIFI Kernel Size                               63                            63                            63
Decoder Hidden Dimension                        256                           256                           256
Training Decoder Layer Number                     6                             6                             6
Inference Decoder Layer Number                    4                             6                             6
Queries                                         300                           300                           300
Denoising Tokens                                100                           100                           100
Sampling Point Number                   (S: 3, M: 6, L: 3)            (S: 3, M: 6, L: 3)            (S: 3, M: 6, L: 3)
Loss Function                            DEIMCriterion                 DEIMCriterion                 DEIMCriterion
Weight of LVFL                                    1                             1                             1
Weight of LBBox                                   5                             5                             5
Weight of LGIOU                                   2                             2                             2
Weight of LFGL                                  0.15                          0.15                          0.15
Weight of LDDF                                   1.5                           1.5                           1.5
Base Learning Rate                            1.25e-4                      1.25e-4                       1.25e-4
Backbone Learning Rate                          5e-5                          5e-5                          5e-5
Total Batch Size                                 64                            64                            64
Epochs                                           80                            80                            80
EMA Decay                                     0.9999                        0.9999                        0.9999
ImageNet-1K Training Settings           EfficientNAT-M                 EfficientNAT-L               EfficientNAT-X
EfficientNAT Block Number                  (1, 1, 2, 2)                 (1, 1, 1, 4, 4)               (1, 2, 7, 15, 2)
EfficientNAT Block Dimensions        (32, 64, 128, 256, 512)       (32, 64, 128, 256, 512)       (32, 64, 128, 256, 512)
Base Learning Rate                             1e-3                          1e-3                          1e-3
Warmup Learning Rate                           1e-6                          1e-6                          1e-6
Min Learning Rate                              5e-6                          5e-6                          5e-6
Epochs                                         300                           300                            300
Cooldown Epochs                                 10                            10                             10
Warmup Epochs                                   20                            20                             20
Batch Size                                     128                           128                            128
Learning Rate Scheduled                      Cosine                         Cosine                        Cosine
Weight Decay                                   5e-2                          5e-2                          5e-2

                 Table 6. Implementation details and training hyperparameters of our proposed method.

                                                         12
Figure 5. Visualization of applying Le-DETR-L into hard cases of object detection.

                                       13
Figure 6. Visualization of applying Le-DETR-X into hard cases of object detection.

                                       14
