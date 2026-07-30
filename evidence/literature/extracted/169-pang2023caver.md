---
source_id: 169
bibtex_key: pang2023caver
title: CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection
year: 2023
domain_theme: RGB-D SOD
verified_pdf: 169_CAVER.pdf
char_count: 121622
---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                               1

                                         CAVER: Cross-Modal View-Mixed Transformer for
                                               Bi-Modal Salient Object Detection
                                                                              Youwei Pang, Xiaoqi Zhao, Lihe Zhang and Huchuan Lu
                                                                                        https://github.com/lartpang/CAVER

                                            Abstract—Most of the existing bi-modal (RGB-D and RGB-T)
                                         salient object detection methods utilize the convolution operation
                                         and construct complex interweave fusion structures to achieve
arXiv:2112.02363v3 [cs.CV] 16 Feb 2023

                                         cross-modal information integration. The inherent local connec-
                                         tivity of the convolution operation constrains the performance
                                         of the convolution-based methods to a ceiling. In this work, we
                                         rethink these tasks from the perspective of global information
                                         alignment and transformation. Specifically, the proposed cross-
                                         modal view-mixed transformer (CAVER) cascades several cross-
                                         modal integration units to construct a top-down transformer-
                                         based information propagation path. CAVER treats the multi-
                                         scale and multi-modal feature integration as a sequence-to-
                                         sequence context propagation and update process built on a
                                         novel view-mixed attention mechanism. Besides, considering the
                                         quadratic complexity w.r.t. the number of input tokens, we design
                                         a parameter-free patch-wise token re-embedding strategy to sim-
                                         plify operations. Extensive experimental results on RGB-D and
                                         RGB-T SOD datasets demonstrate that such a simple two-stream
                                                                                                                              Pixel-wise Token Embedding      Patch-wise Token Re-Embedding
                                         encoder-decoder framework can surpass recent state-of-the-art
                                         methods when it is equipped with the proposed components. Code
                                                                                                                       Fig. 1. Patch-wise token re-embedding (PTRE). Before matrix multiplication,
                                         and pretrained models will be available at the link.                          the parameter-free PTRE is used to reshape features. Thus, pixel-wise tokens
                                            Index Terms—Bi-modal salient object detection, RGB-D salient               are aggregated and converted into patch-wise tokens.
                                         object detection, RGB-T salient object detection, multi-modal
                                         transformer, attention mechanism, convolutional neural networks.
                                                                                                                 position relationship between objects, and the infrared map
                                                                                                                 based on the thermal radiation can better present the overall
                                                                                                                 shape of the object in various complex scenarios. They help
                                                                 I. I NTRODUCTION                                to distinguish different objects and alleviate the above issues.
                                              ALIENT object detection (SOD) aims to identify the Therefore, recent research is gradually shifting towards the
                                         S    most significant objects or regions in images or videos integration of modality-specific and modality-complementary
                                         from various visual scenes. It plays a fundamental and cues from RGB and depth/thermal images to excavate and
                                         important role in many computer vision tasks, such as se- capture objects of interest. At the same time, long-range context
                                         mantic segmentation [1], medical image segmentation [2], [3] and contrast information play a key role in identifying and
                                         video object segmentation [4]–[6], person re-identification [7], locating salient objects. However, the purely convolution-based
                                         camouflaged object detection [8]–[10], image editing [11] and architectures 1 possibly encounter the performance bottleneck,
                                         compression [12].                                                       which is caused by the localized convolution operation and the
                                            Although many purely CNN-based methods [13]–[17] fixedness of the learned parameters. Hence, the introduction
                                         achieve quite promising results on the RGB SOD task, they still of a new architecture becomes more and more important.
                                         struggle with challenges of complex or low-contrast scenes, and            The transformer [21] has superior performance against
                                         obscured or indistinguishable objects. To this end, some recent existing state-of-the-art CNNs in several computer vision
                                         studies have attempted to introduce additional information, tasks [22], [23], which can be attributed to its powerful ability
                                         such as depth [18], light field [19] and thermal infrared [20] to extract features and model long-range dependencies. In this
                                         images, to make the model comfortable with complicated and paper, we introduce the transformer to design a simple yet
                                         diverse natural scenes. The depth map can explicitly provide effective RGB-D SOD model, CAVER. A novel transformer-
                                         complementary spatial structure information and the relative based top-down multi-level structure is engineered for the cross-
                                                                                                                 modal fusion, which can be easily assembled to a CNN feature
                                           Y. Pang, X. Zhao, L. Zhang and H. Lu are with the School of Infor- extractor, like ResNets [24]–[26]. We leverage the self- and
                                         mation and Communication Engineering, Dalian University of Technology,
                                         Dalian, China (e-mail: lartpang@mail.dlut.edu.cn; zxq@mail.dlut.edu.cn; cross-attention to learn feature alignment where each element
                                         zhanglihe@dlut.edu.cn; lhchuan@dlut.edu.cn). This work was supported by
                                         the National Natural Science Foundation of China #62276046 and the Liaoning      1 Their core components are the convolution, which is different from our
                                         Natural Science Foundation #2021-KF-12-10.                                    transformer-based structure.
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                      2

gathers information from other elements in the global sequence directions: one is to explore where the observer is looking,
based on semantic similarity. This can naturally achieve the   i.e. eye fixation prediction [27], and the other is to locate
transformation and enhancement of intra-modal features and     and segment completely visually attractive regions, i.e. salient
the matching and fusion of inter-modal features. However,      object detection (SOD) [28], [29]. In this paper, we focus on
a prominent problem of the transformer is the unbearable       the latter. With the UNet-like [30] architecture becoming the
quadratic computational complexity caused by the attention     dominant paradigm for SOD, the proliferation of CNN-based
operation based on all elements of the feature map. To cope    methods has driven the rapid development of SOD in recent
with this, we introduce the patch embedding into the attention years [31], [32].
block. Instead of using the patch embedding to extract and           b) Bi-modal Salient Object Detection.: In the bi-modal
compress image features in the input stage [22] or at the      SOD field, RGB-D and RGB-T are two thriving and important
beginning of each stage corresponding to different feature     branches. They additionally introduce depth or thermal infrared
scales [23], we apply it to improve each matrix multiplication information, respectively, which can provide a more compre-
of self- and cross-attention with the pixel-wise tokens as the hensive understanding of the scene. Roughly speaking, the
input. We call this parameter-free operation “patch-wise token existing methods can be broadly classified into three categories
re-embedding” (PTRE) as shown in Fig. 1. When learning         depending on the cross-modal fusion strategy: early fusion,
multi-scale and high-resolution features, such a design can    intermediate fusion, and late fusion. Early fusion methods
reduce computation and memory costs by a factor of p2 and      directly combine the low-level information of two modalities,
p4 (p is the side length of the patch), respectively. At the same
                                                               e.g., concatenating the inputs [33]–[35] or integrating their
time, considering that the existing transformer-based methods  low-level features [36]. Although such a scheme may reduce
pay too much attention to the spatial context information      the number of model parameters, this also makes it difficult
in the process of the feature alignment while ignoring the     to control the interference of noise within different modalities
positive role of the channel context. Therefore we introduce a to the whole model. Unlike early fusion, late fusion methods
parallel channel attention branch into the attention operation generally adopt a dual-stream structure and focus more on the
and propose the view-mixed attention (VMA) block. Global       cross-modal fusion of high-level features [37]–[39] or final
context and object detail information have positive value for  predictions [40]. The semantic information enriched by high-
the SOD task, so the convolutional design is introduced into   level features has a positive guide for good prediction results.
the feed forward network that follows the attention operation  In fact, both low-level and high-level features have the same
to enhance the perception of local details. As a result, the   importance in the SOD task, and they complement each other.
proposed components can work together to effectively explore   The low-level features can provide rich texture and structural
and excavate global and local cues in the feature decoding     scene perception, which is missing in the high-level features.
process.                                                       Hence, an intermediate fusion strategy that utilizes both simul-
   Our contributions can be summarized as:                     taneously is gradually becoming the mainstream of bi-modal
   • We introduce the transformer to rethink the bi-modal SOD  SOD methods [41]–[57]. Our proposed method can also be
     modeling from a sequence-to-sequence perspective, which   classified into this category. These algorithms usually construct
     gains better interpretability.                            various cross-modal interaction strategies based on the CNN
   • We build a top-down transformer-based information prop-   structure, which typically draw on the plug-and-play modules
     agation path enhanced by the view-mixed attention block,  or their variants to enhance and rectify the representation of
     which can align the features of RGB and depth/thermal     features such as ASPP [58] or DenseASPP [59], PPM [60],
     modalities and fully exploit the inter- and intra-modal   convolutional channel/spatial attention blocks [61]–[63] in [34],
     information from spatial and channel views.               [44], [46], [50], [54]–[57], [64]–[67] and ConvLSTM [68]
   • We boost the matrix operation in the attention by using   in [44]. Specifically, a novel joint learning and densely coopera-
     the patch-wise token re-embedding, which improves the     tive fusion architecture through a siamese network are designed
     efficiency of the transformer for multi-scale and high-   in [50]. In [67], the bifurcated backbone strategy and depth-
     resolution features. And aided by the convolutional feed  enhanced module are proposed to excavate informative cues
     forward network, the locality of features can be further  and fuse the two modalities in a complementary way. And [69]
     enhanced, and key cues in both global and local contexts  explores both the shared information and modality-specific
     can be fully perceived and explored.                      properties. Uncertainty-aware stochastic framework [65], [70]
   • Extensive experiments demonstrate that the proposed       and mutual information minimization regularization [66] are
     model outperforms recent methods on seven RGB-D SOD       also introduced to optimize the interaction process of two
     datasets and three RGB-T SOD datasets.                    modalities. Unlike them, we introduce a global sequence
                                                               perspective for feature enhancement and interaction. This can
                                                               effectively fill the lack of contextual information caused by the
                    II. R ELATED W ORK                         local reception field of the convolution operation.
     a) Visual Attention.: Humans can quickly capture sig-           c) Attention-Based Model.: On the one hand, as men-
nificant objects or regions in a scene. The modeling and tioned earlier, the attention mechanism is closely related to
investigation of such an ability is a fundamental and critical the SOD task. Some methods [44], [46], [65], [70] apply
problem in computer vision, i.e. visual attention mechanism. convolutional channel and spatial attention blocks [61]–[63].
Research in this area can be divided into two different And recent methods design some task-friendly variants. Inspired
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                                                          3

                                                      Depth/Thermal Image 𝑰𝒅/𝒕                                                                        𝒇𝒊𝒓𝒈𝒃−𝒅/𝒕

                                                      Feature Encoder Network
                                                                                                                                          Cross-Scale Self-Attention

                                                                                                                                            𝒇෠ 𝒊𝒓𝒈𝒃−𝒅/𝒕
                                              𝒇𝟏𝒅/𝒕      𝒇𝟐𝒅/𝒕        𝒇𝟑𝒅/𝒕      𝒇𝟒𝒅/𝒕
                         Saliency Predictor

                                                                                         Linear Projection
                                                                                                                                                          Add                           Upsample

                                                                                                             Integration Unit
        Saliency Map 𝑷

                                                                                                               Cross-Modal
                                                                                                                                            𝒇෨ 𝒊𝒓𝒈𝒃−𝒅/𝒕
                                              CMIU1     CMIU2        CMIU3       CMIU4
                                                                                                                                          Inter-Modal Cross-Attention

                                                                                                                                𝒇෨ 𝒊𝒓𝒈𝒃                                       𝒇෨ 𝒊𝒅/𝒕
                                              𝒇𝟏𝒓𝒈𝒃      𝒇𝟐𝒓𝒈𝒃        𝒇𝟑𝒓𝒈𝒃      𝒇𝟒𝒓𝒈𝒃
                                                                                                                                    Intra-Modal                    Intra-Modal
                                                                                                                                   Self-Attention                 Self-Attention
                                                      Feature Encoder Network

                                                           RGB Image 𝑰𝒓𝒈𝒃                                                                 𝒇𝒊𝒓𝒈𝒃                       𝒇𝒊𝒅/𝒕             𝒇𝒊+𝟏
                                                                                                                                                                                         𝒓𝒈𝒃−𝒅/𝒕

Fig. 2. The overview of the proposed model. This is a dual-stream encoder-decoder architecture with a very simple and straightforward form. Note that the
dashed line denotes an optional path for the decoder. In our model, the CMIU4 only contains two inputs frgb4        4
                                                                                                              and fd/t   and fˆrgb−d/t
                                                                                                                               4       = f˜rgb−d/t
                                                                                                                                           4       . The
         i+1
feature frgb−d/t exists in CMIU1-3, which is upsampled using bilinear interpolation in the 2D form.

by the dynamic convolution [71], [38] design the dynamic methods which propose the transformer-based encoder, our
dilated pyramid module with position-specific and image- work is more inclined to explore the design of the transformer-
specific multi-scale filters to provide cross-modal contextual based decoder, especially for cross-modal tasks such as RGB-
guidance for the RGB feature. A saliency-guided bilateral D SOD and RGB-T SOD. We use it to decode the extracted
attention module in [49] is proposed to capture meaning- features from RGB and depth/thermal images and build a simple
ful foreground and background complementary information. encoder-decoder architecture for these two bi-modal SOD tasks.
Although these data-adaptive feature enhancement methods Since these bi-modal tasks require considering two modalities,
in spatial or channel form can improve the flexibility and their integration and alignment are the key points of our model
expressiveness of the model, these convolution-based strategies design. This work and the existing methods can complement
do not model long-range dependencies well and still have a each other. In addition, we apply the transformer to multi-
large room for improvement. The most related works [64], [72] scale high-resolution features, which faces the computational
introduce the non-local block [73] or self-attention block [21], pressure from higher-resolution features.
but they are only used to enhance the high-level feature
interaction in the spatial view and the model body is still                         III. O UR M ETHOD : CAVER
limited by the CNN architecture. Besides, limited by the large      In this paper, we propose CAVER, a simple yet effective
computational cost of the original self-attention operation, cross-modal feature integration network based on the trans-
they give up the positive gain that contextual information former. In the following, we first show the overview of the
can bring in the processing and fusion of shallow bi-modal model and then describe the details of each component.
features. In contrast, our channel and spatial view-mixed
approach achieves further exploration by thoroughly building
                                                                 A. Network Overview
the multi-level cross-modal fusion scheme from a sequence-
to-sequence transformation perspective. On the other hand,          In our approach, the widely used CNN backbone acts as
the transformer [21] is built on the similarity-based attention  the  feature encoder network for two modalities: RGB and
mechanism, which has shown powerful performance in natural       depth/thermal.    As shown in Fig. 2, the features with different
                                                                                 i    4                                   i    4
language processing and is receiving more and more interest      scales (i.e. {f rgb }i=1 from the RGB image Irgb and {fd/t }i=1
from researchers in computer vision. The recent remarkable from the depth/thermal image Id/t ) from each intermediate
performance of vision transformers [22], [23] reflects that the layer of the backbone are fed directly to the corresponding stage
transformer is a general and effective architecture to transform in the proposed transformer-based information propagation
features. Most of them use the transformer to extract image path. These multi-scale features abound with the cues about
features for the classification task. SETR [74] is a pioneering appearances, boundaries, textures, and more complex semantic
work of applying the transformer to the segmentation field and concepts from the RGB modality, relative spatial location
it uses ViT [22] to extract features and builds a lightweight relationships between objects from the depth modality, and the
convolutional decoder to obtain predictions. Similarly to it, integrity and thermal radiation property of the object self from
the existing methods tend to explore the application of the the thermal infrared modality. By absorbing shallow features
transformer in the encoder, and there is little work focusing from top to down, this serialized cross-modal information
on the decoder. In the segmentation task, the decoder plays an aggregation process gradually recovers the high-resolution
important role and both transformer-based encoder and decoder representation. And the salient object regions are enriched
are worthy of being explored. So different from the existing and shaped. Eventually, the refined features are mapped as
                                                                 the final single-channel saliency map P via a simple saliency
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                               4

                     Add                                                 Add                                                           ×𝜷
                                                                                                                             Add

                 Conv-FFN                                              Conv-FFN                                           ×𝜶

                                                                     Normalization                                Patch-wise Spatial-View
               Normalization                                                                                             Multi-Head
                                                                                                                    Self/Cross-Attention
                                                                         Cat
                     Add                                     Add                     Add                               Channel-View
                                                                                                                         Multi-Head
                  PV-MHSA                                PV-MHCA                  PV-MHCA                           Self/Cross-Attention

               Normalization                           Normalization            Normalization

                      (a)                                                 (b)                                                 (c)
Fig. 3. Patch-wise view-mixed attention blocks of the proposed network. “Normalization” denotes the BN [75] layer in our method. (a) Self-attention block.
(b) Cross-attention block. (c) View-mixed attention operation.

                              2D Feature Map
                                                                                                                 i+1
                                                                                is the sum of the upsampled frgb−d/t     and the output f˜rgb−d/t
                                                                                                                                          i

                                                                                of the inter-modal cross-attention block, otherwise, the input
                                  1   2   3
                                                                                is equal to f˜rgb−d/t
                                                                                              i                            1
                                                                                                      . The resolution of frgb−d/t is a quarter of
                                  4   5   6
                                                                                that of the input Irgb and Id/t .
                                  7   8   9
        Unflatten                                          flatten
                                                                                C. Intra-Modal/Cross-Scale Self-Attention (IMSA/CSSA)
                      1     2 3 4 5 6 7 8            9
                                                                                   The IMSA and CSSA blocks play different roles, but their
                            1D Feature Sequence
                                                                                structures are the same. The specific details of the self-attention
                                                                                block can be found in Fig. 3a, which is characterized by a
Fig. 4. Conversion between the 2D feature map and the 1D feature sequence.
                                                                                patch-wise view-mixed multi-head self-attention (PV-MHSA), a
                                                                                convolutional feed forward network (Conv-FFN), normalization
predictor which contains a bilinear interpolation operation,                    layers and residual connectors. The PV-MHSA follows a
some convolution layers, and a sigmoid activation. It is                        pre-normalization [76], [77] layer and they are wrapped by
supervised by the binary ground truth G.                                        a residual connector. The output is then passed to a pre-
                                                                                normalized Conv-FFN whose input and output are similarly
                                                                                connected in a residual way. The overall process can be
B. Transformer-based Information Propagation Path (TIPP)                        expressed as:
   The TIPP is proposed mainly to process and integrate top-                    X = PV-MHSA(Norm(X)) + X,
down features from both RGB and depth/thermal modalities                                                                    (1)
                                                                                X = Conv-FFN(Norm(X)) + X,
with different scales, which consists of four cascaded cross-
modal integration units (CMIUs), as shown in Fig. 2. Among where X ∈ RN ×D refers to the flattened image features. N =
them, the 4th CMIU is only responsible for the integration of H × W and D denote the number of pixel tokens and the
                                                    4          4
cross-modal information. It takes feature maps frgb     and fd/t  embedding dimension.
with the same scale as input. While each of the remaining              a) Multi-Head Self-Attention (MHSA).: At first, we intro-
CMIUs needs to additionally integrate the output feature map duce its original form in the transformer [21]. This operation
from the adjacent higher level. In addition, each input map is actually a feature alignment process, which computes the
of the CMIU needs to be converted into a D-dimensional feature correlation to reconstruct the query itself. And a single
pixel-wise embedding map in a separate embedding layer. head of it can be defined as:
Empirically, D is set to 64, which helps generate more compact
                                                                                                              Qh Kh>
feature embeddings and reduces memory cost. Before the                Yh = Attn(Qh , Kh> , Vh , e) = Softmax(        )Vh ,
                                                                                                                e           (2)
integration of modalities through the inter-modal cross attention
                                                                                   [Qh , Kh , Vh ] = X[Wq , Wk , Wv ],
block, frgb and fd/t are first reconstructed and self-reinforced
by an intra-modal self-attention block, respectively. For the where Qh , Kh , Vh are a single head of query, key and value,
following cross-scale self-attention block, if there exists the respectively. Wq , Wk , Wv ∈ RD×D/Nh are the corresponding
          i+1
feature frgb−d/t  from the previous CMIU, the input fˆrgb−d/t
                                                          i
                                                                  projection matrices. Nh is the number of heads and e =
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                             5

p
   D/Nh is a scaling factor. The outputs from different heads        interaction, the local correlation still has a strong practical
are concatenated together and fused by a dense layer. The final      value as a kind of inductive bias for image data in the
output Z ∈ RN ×D can be expressed as Z = [Y1 , . . . , YNh ]Wo       vision task. The original position-wise feed forward network
and Wo ∈ RD×D is an output projection layer. It is noted             (FFN) in the transformer only performs the separate channel
that the dot product operation in the attention matrix Qh Kh>        transformation for each element of the sequence, which lacks
has a quadratic complexity w.r.t. the input sequence length,         attention to the local context. Hence, we adapt the FFN by using
i.e. N 2 , which limits it to handling multi-scale high-resolution   the convolution operation. The original two fully-connected
features. In addition, the current MHSA only considers feature       layers are replaced with the common combination of “3 × 3
alignment on the spatial view, while ignoring the potential          convolution → batch normalization → activation” and finally
value of the channel view. With these considerations in mind,        a 1 × 1 convolution layer is utilized to obtain the feature with
two improvements are made in our method: 1) The patch-wise           the same dimension as the output of the original FFN.
token re-embedding strategy (PTRE) is designed to reduce
the computational complexity, which ensures the ability of the       D. Inter-Modal Cross-Attention (IMCA)
model to integrate a wider range of contextual information.
                                                                        The IMCA block contains two streams (i.e., RGB and
2) The feature reconstruction in the channel view is also
                                                                     depth/thermal) and the multi-head cross-attention (MHCA)
introduced to build the view-mixed attention (VMA) based
                                                                     is the protagonist here. The MHCA is very similar to the
on MHSA. Based on the proposed PTRE and VMA, we can
                                                                     MHSA, the only difference is that the sources of information
construct a lighter PV-MHSA to replace the original MHSA,
                                                                     for Q and K/V are no longer the same. This change in form
which has a more efficient calculation process and a better
                                                                     allows it to be used to construct interactions between different
modeling capability.
                                                                     information sources. In our method, the cross-attention block
      b) Patch-wise Token Re-Embedding (PTRE).: The PTRE
                                                                     (Fig. 3b) is used to associate and interact information between
is applied to improve the matrix operation from the pixel-
                                                                     modalities. Its input is from the outputs of two separated IMSA
wise form to the patch-wise form compared with the MHSA,
                                                                     blocks. Similarly to the self-attention block, the input features
which reduces the complexity by a factor of p2 . Here, p2 is
                                                                     are also normalized. Then, they are passed into the patch-wise
the number of elements in a patch. Specifically, Qh , Kh and
                                                                     view-mixed multi-head cross-attention (PV-MHCA) equipped
Vh in Equ. 2 are unflattened to the 2D form (Fig. 4) and
                                                                     with the PTRE and the VMA for cross-modal alignment and
adjusted by the PTRE operation. In the PTRE, the map with
                                                                     enhancement. Next, the features Z rgb and Z d/t from two
D/Nh -dimensional embedding is unfolded to N/p2 ×Dp2 /Nh
                                                                     modality streams are concatenated, normalized and then locally
(Fig. 1). After the operation in Equ. 2, the patch-wise result is
                                                                     enhanced by a cascaded Conv-FFN. Finally, the output is the
reshaped back to N × D/Nh and subsequent operations are
                                                                     sum of the results from the PV-MHCA and the Conv-FFN.
consistent with those of the MHSA.
                                                                     Specifically, the RGB stream can be formulated as:
      c) View-Mixed Attention (VMA).: In our method, the
channel-view self-attention is introduced to enhance the form                Z rgb = αrgb Zsrgb + β rgb Zcrgb ,
of self-attention shown in Equ. 2 which only gathers the                                             d/t>      d/t
                                                                             Zsrgb = [Attn(Qrgb
                                                                                            h , Kh          , Vh , e)]N
                                                                                                                      h=1 Ws ,
                                                                                                                        h
                                                                                                                                   (4)
information from the spatial view. The main difference between                                      d/t  d/t>
the two is that the objects for pairwise similarity calculation             Zcrgb> = [Attn(Qrgb>
                                                                                            h    , Kh , Vh    , n)]N
                                                                                                                   h=1 Wc ,
                                                                                                                     h

are changed from spatial locations in the feature sequence           where [. . . ]N h
                                                                                   h=1 represents the concatenation operation for
to independent feature channels. Specifically, the form of the       all heads and Ws and Wc are output projection matrices
calculation in Equ. 2 is consequently transformed into the           corresponding to different views to fuse these heads, similar
following form:                                                      to the PV-MHSA. To get the output Z d/t of the depth/thermal
                                                                     stream, just replace inputs Qrgb , K d/t and V d/t , and learnable
                  Yh> = Attn(Q>         >
                              h , Kh , Vh , n),               (3)    weights αrgb and β rgb : Qrgb → Qd/t , K d/t → K rgb , V d/t →
            √                                                        V rgb , αrgb → αd/t , β rgb → β d/t .
where n = N is a scaling factor. In the proposed block, the
two operations are executed in parallel, and the output features
                                                                                           IV. E XPERIMENTS
Zs and Zc from the spatial and channel branches are combined
by learnable weights α ∈ [0, 1] and β ∈ [0, 1] to obtain the         A. Datasets
output of the VMA: Z = αZs + βZc . Compared with the                   To validate the proposed model and components, we
single spatial token attention in Equ. 2, the computational          conducted experiments on seven RGB-D and three RGB-T
cost is reduced from 2N 2 D to 2N 2 D/p2 + 2N D2 , and the           benchmarks that have been widely used to evaluate RGB-
memory cost is reduced from Nh N 2 + N D to Nh N 2 /p4 +             D/RGB-T SOD methods.
D2 /Nh + 2N D. In our default setting (D = 64 and Nh = 2),                a) RGB-D SOD.: NJUD [78] involves a lot of complex
when N > 65 (i.e., the length and width of the feature map           data, which consists of 1985 images collected from the Internet,
are both greater than 8 and it is a very common scenario),           3D movies, and stereo photos, with their corresponding depth
the proposed view-mixed attention is more efficient than the         images. NLPR [33] contains 1000 pairs of RGB and depth
standard attention form.                                             images covering rich indoor and outdoor scenes. SIP [35]
     d) Convolutional Feed Forward Network (Conv-FFN).:              containing 929 pairs of images is a recent high-resolution
Although the transformer can better model the long-range             dataset. It is collected in an outdoor scene and contains
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                                                                                                     6

                                                                 TABLE I
C OMPARISON WITH RECENT STATE - OF - THE - ART RGB-D SOD METHODS ON NJUD [78], NLPR [33], SIP [35] AND STEREO1000 [79]. ?: USING THE
MULTI - SCALE TRAINING TECHNIQUE . —: NOT AVAILABLE . T HE BEST THREE RESULTS ARE HIGHLIGHTED USING RED , GREEN AND BLUE IN THE ORDER .

                                                     NJUD                                               NLPR                                                       SIP                                      STEREO1000
               METHOD
                                      Sm ↑    Fβω ↑ M AE ↓ Fβ ↑ Em ↑                   Sm ↑      Fβω ↑ M AE ↓ Fβ ↑ Em ↑                         Sm ↑       Fβω ↑ M AE ↓ Fβ ↑ Em ↑                 Sm ↑ Fβω ↑ M AE ↓ Fβ ↑ Em ↑
               CPFP19 [43]            0.878   0.828       0.053      0.877     0.900   0.884     0.807      0.038         0.862      0.920      0.850      0.788     0.064     0.851     0.899     0.879    0.817    0.051   0.874   0.907
               DMRA19 [44]            0.886   0.846       0.051      0.886     0.920   0.899     0.838      0.031         0.879      0.941      0.806      0.739     0.086     0.821     0.863     0.752    0.647    0.087   0.743   0.816
               MMCI19 [42]            0.859   0.739       0.079      0.853     0.882   0.856     0.676      0.059         0.815      0.872      0.833      0.712     0.086     0.818     0.886     0.873    0.760    0.068   0.863   0.905
               TANet19 [41]           0.878   0.803       0.061      0.874     0.909   0.886     0.779      0.041         0.863      0.916      0.835      0.748     0.075     0.830     0.894     0.871    0.787    0.060   0.861   0.916
               JLDCF20 [50]           0.902   0.869       0.041      0.904     0.935   0.925     0.882      0.022         0.918      0.955      0.880      0.844     0.049     0.889     0.923     0.903    0.857    0.040   0.904   0.937
               S2MA20 [64]            0.894   0.842       0.053      0.889     0.916   0.915     0.852      0.030         0.902      0.942      0.872      0.819     0.057     0.877     0.913     0.890    0.825    0.051   0.882   0.926
               UCNet20 [70]           0.897   0.868       0.043      0.895     0.934   0.920     0.878      0.025         0.903      0.955      0.875      0.836     0.051     0.879     0.918     0.903    0.867    0.039   0.899   0.942
               BBSNet20 [67]          0.926   0.892       0.033      0.929     0.944   0.930     0.878      0.024         0.915      0.952      0.887      0.840     0.052     0.895     0.922     0.913    0.864    0.039   0.910   0.941
               CMWNet20 [45]          0.903   0.857       0.046      0.902     0.923   0.917     0.856      0.029         0.903      0.940      0.867      0.811     0.062     0.874     0.909     0.905    0.847    0.043   0.901   0.930
               CoNet20 [46]           0.896   0.848       0.046      0.893     0.924   0.908     0.841      0.031         0.887      0.933      0.858      0.802     0.063     0.867     0.909     0.905    0.865    0.038   0.901   0.941
               DANet20 [34]           0.899   0.857       0.045      0.898     0.922   0.915     0.862      0.028         0.903      0.949      0.875      0.822     0.054     0.876     0.915     0.901    0.846    0.043   0.892   0.931
               HDFNet20 [38]          0.908   0.877       0.038      0.911     0.932   0.923     0.882      0.023         0.917      0.957      0.886      0.848     0.047     0.894     0.924     0.900    0.853    0.041   0.900   0.931
               ICNet20 [80]           0.894   0.843       0.052      0.891     0.913   0.923     0.864      0.028         0.908      0.945      0.854      0.791     0.069     0.857     0.900     0.903    0.844    0.045   0.898   0.926
               ?D3Net20 [35]          0.900   0.854       0.046      0.900     0.916   0.912     0.849      0.030         0.897      0.945      0.860      0.799     0.063     0.861     0.902     0.899    0.838    0.046   0.891   0.924
               SPNet21 [69]           0.924   0.906       0.028      0.928     0.953   0.927     0.896      0.021         0.919      0.959      0.894      0.868     0.043     0.904     0.931     0.907    0.873    0.037   0.906   0.942
               RD3D21 [53]            0.916   0.886       0.036      0.914     0.942   0.930     0.889      0.022         0.919      0.959      0.885      0.845     0.048     0.889     0.924     0.911    0.871    0.037   0.906   0.944
               TriTransNet21 [72]     0.920   0.906       0.030      0.926     0.954   0.928     0.902      0.020         0.924      0.964      0.886      0.864     0.043     0.899     0.929     0.908    0.882    0.033   0.911   0.950
               DCF21 [81]             0.904   0.876       0.039      0.905     0.940   0.922     0.884      0.024         0.910      0.956      0.874      0.840     0.052     0.886     0.921     0.906    0.872    0.037   0.904   0.943
               HAINet21 [51]          0.912   0.883       0.038      0.915     0.934   0.924     0.887      0.024         0.915      0.959      0.880      0.842     0.053     0.892     0.919     0.907    0.866    0.040   0.906   0.935
               CCAFNet21 [52]         0.910   0.877       0.037      0.910     0.941   0.922     0.875      0.027         0.909      0.952      0.877      0.829     0.054     0.880     0.916     0.892    0.844    0.045   0.887   0.932
               DCMF21 [82]            0.913   0.867       0.043      0.915     0.925   0.922     0.856      0.029         0.906      0.940      0.870      0.808     0.062     0.872     0.906     0.910    0.849    0.043   0.906   0.930
               UCNet-CVAE21 [65]      0.904   0.886       0.038      0.907     0.943   0.922     0.889      0.023         0.909      0.956      0.882      0.850     0.045     0.889     0.927     0.906    0.878    0.036   0.904   0.945
               ?CMINet21 [66]         0.929   0.910       0.029      0.934     0.953   0.932     0.900      0.021         0.922      0.962      0.899      0.872     0.040     0.910     0.937     0.918    0.886    0.032   0.916   0.948
               OursR50(I)             0.921   0.901       0.031      0.925     0.953   0.929     0.895      0.020         0.921      0.962      0.893      0.864     0.042     0.902     0.933     0.913    0.882    0.033   0.912   0.949
               OursR50(II)            0.920   0.900       0.031      0.923     0.951   0.929     0.895      0.022         0.921      0.961      0.893      0.868     0.042     0.906     0.933     0.914    0.883    0.033   0.911   0.949
               OursR101(I)            0.927   0.909       0.028      0.932     0.956   0.930     0.898      0.023         0.923      0.961      0.895      0.871     0.043     0.909     0.935     0.917    0.888    0.032   0.918   0.951
               OursR101(II)           0.926   0.906       0.029      0.928     0.953   0.934     0.904      0.021         0.929      0.966      0.904      0.879     0.037     0.915     0.943     0.917    0.888    0.032   0.916   0.951

                                                                TABLE II
 C OMPARISON WITH RECENT STATE - OF - THE - ART RGB-D SOD METHODS ON SSD [83], LFSD [84] AND DUTRGBD [44]. ?: USING THE MULTI - SCALE
       TRAINING TECHNIQUE . —: NOT AVAILABLE . T HE BEST THREE RESULTS ARE HIGHLIGHTED USING RED , GREEN AND BLUE IN THE ORDER .

                                                                                 SSD                                          LFSD                                                   DUTRGBD
                                              METHOD
                                                                     Sm ↑ Fβω ↑ M AE ↓           Fβ ↑ Em ↑        Sm ↑ Fβω ↑ M AE ↓               Fβ ↑ Em ↑          Sm ↑ Fβω ↑       M AE ↓ Fβ ↑        Em ↑
                                              CPFP19 [43]             0.807    0.708   0.082     0.766    0.832     0.828    0.775      0.088      0.826     0.867   0.749   0.637     0.100     0.718   0.815
                                              DMRA19 [44]             0.857    0.784   0.059     0.844    0.898     0.847    0.811      0.076      0.856     0.899   0.888   0.851     0.048     0.897   0.930
                                              MMCI19 [42]             0.814    0.661   0.082     0.782    0.860     0.787    0.663      0.132      0.771     0.840   0.791   0.627     0.112     0.767   0.856
                                              TANet19 [41]            0.839    0.726   0.063     0.810    0.886     0.801    0.719      0.111      0.796     0.851   0.808   0.704     0.093     0.790   0.871
                                              JLDCF20 [50]            0.860    0.782   0.053     0.833    0.899     0.861    0.822      0.070      0.867     0.902   0.905   0.863     0.043     0.911   0.938
                                              S2MA20 [64]             0.868    0.787   0.052     0.848    0.898     0.837    0.772      0.094      0.835     0.876   0.903   0.862     0.044     0.900   0.935
                                              UCNet20 [70]            0.866    0.813   0.049     0.854    0.901     0.864    0.832      0.066      0.864     0.906   0.864   0.820     0.057     0.857   0.906
                                              BBSNet20 [67]           0.868    0.789   0.051     0.842    0.904     0.878    0.826      0.065      0.873     0.907   0.920   0.883     0.037     0.927   0.949
                                              CMWNet20 [45]           0.875    0.795   0.051     0.871    0.902     0.876    0.834      0.066      0.883     0.908   0.887   0.831     0.056     0.888   0.922
                                              CoNet20 [46]            0.853    0.779   0.060     0.840    0.898     0.862    0.814      0.071      0.859     0.901   0.919   0.890     0.034     0.927   0.952
                                              DANet20 [34]            0.864    0.795   0.050     0.843    0.911     0.849    0.795      0.079      0.844     0.881   0.899   0.860     0.043     0.906   0.937
                                              HDFNet20 [38]           0.879    0.821   0.045     0.870    0.911     0.854    0.806      0.076      0.862     0.891   0.907   0.864     0.041     0.918   0.938
                                              ICNet20 [80]            0.848    0.772   0.064     0.841    0.879     0.868    0.822      0.071      0.871     0.900   0.852   0.784     0.072     0.850   0.901
                                              ?D3Net20 [35]           0.857    0.777   0.058     0.834    0.904     0.825    0.760      0.095      0.810     0.863   0.775   0.668     0.097     0.742   0.849
                                              SPNet21 [69]            0.871    0.823   0.044     0.863    0.920     0.854    0.823      0.071      0.863     0.897   0.804   0.735     0.085     0.849   0.877
                                              RD3D21 [53]             0.803    0.707   0.082     0.772    0.869     0.858    0.816      0.073      0.854     0.898   0.931   0.907     0.031     0.939   0.957
                                              TriTransNet21 [72]      0.881    0.842   0.041     0.873    0.935     0.866    0.840      0.066      0.870     0.908   0.933   0.926     0.025     0.946   0.966
                                              DCF21 [81]              0.852    0.789   0.054     0.829    0.905     0.856    0.823      0.071      0.860     0.903   0.924   0.909     0.030     0.932   0.957
                                              HAINet21 [51]           0.857    0.798   0.052     0.838    0.908     0.854    0.811      0.079      0.853     0.892   0.910   0.883     0.038     0.920   0.939
                                              CCAFNet21 [52]          0.863    0.799   0.048     0.842    0.916     0.827    0.783      0.087      0.832     0.877   0.904   0.878     0.038     0.913   0.943
                                              DCMF21 [82]             0.882    0.803   0.053     0.867    0.895     0.877    0.825      0.068      0.875     0.905   0.928   0.888     0.035     0.932   0.951
                                              UCNet-CVAE21 [65]         —       —        —        —        —        0.864    0.836      0.064      0.863     0.908     —       —         —        —        —
                                              ?CMINet21 [66]          0.874    0.820   0.047     0.860    0.910     0.879    0.845      0.061      0.874     0.910   0.897   0.867     0.046     0.891   0.937
                                              OursR50(I)              0.878    0.824   0.041     0.859    0.920     0.873    0.842      0.063      0.877     0.914   0.903   0.874     0.042     0.904   0.937
                                              OursR50(II)             0.874    0.819   0.043     0.854    0.924     0.882    0.854      0.056      0.886     0.921   0.931   0.918     0.028     0.942   0.964
                                              OursR101(I)             0.887    0.838   0.037     0.876    0.932     0.863    0.825      0.074      0.865     0.907   0.913   0.886     0.039     0.920   0.947
                                              OursR101(II)            0.890    0.849   0.038     0.884    0.936     0.876    0.847      0.061      0.880     0.914   0.937   0.926     0.026     0.946   0.967

                           TABLE III                                                                                                                               TABLE IV
 C OMPARISON WITH RECENT STATE - OF - THE - ART RGB-T SOD METHODS                                                                     C OMPARISON OF FLOP S , THE NUMBER OF PARAMETERS , AND FPS OF
 ON VT821 [85], VT1000 [86] AND VT5000-TE [20]. T HE BEST THREE                                                                      SOME RECENT PUBLICLY AVAILABLE STATE - OF - THE - ART RGB-D/RGB-T
RESULTS ARE HIGHLIGHTED USING RED , GREEN AND BLUE IN THE ORDER .                                                                    SOD METHODS . T HE EVALUATION PROCESS IS PERFORMED ON A SINGLE
                                                                                                                                     2080T I GPU WHILE FOLLOWING THE DEFAULT INFERENCE SETTINGS OF
                        MTMR18 M3S-NIR19 ADF20 SDGL20 MIDD21 CSRNet21 CGFNet21 ECFFNet21 Ours50 Ours101                               EACH METHOD . ‡: O UR SELF - ATTENTION BLOCK IS REPLACED BY THE
   METHOD
                          [85]    [87]    [20]   [86]   [57]   [56]     [55]      [54]                                                          SHIFTED WINDOW BASED SELF - ATTENTION [23].
                Sm ↑     0.593    0.723   0.810   0.765      0.871     0.885       0.880       0.877     0.891    0.898
                Fβω ↑    0.264    0.407   0.626   0.583      0.760     0.821       0.829       0.799     0.834    0.845
VT821

           [85] M ↓      0.260    0.140   0.077   0.085      0.045     0.038       0.038       0.035     0.033    0.027                             METHOD                             BACKBONE          FLOPs (G)   Params. (M)      FPS
                Fβ ↑     0.646    0.738   0.752   0.735      0.851     0.858       0.866       0.835     0.876    0.877
                                                                                                                                                  SPNet21 [69]       Res2Net-50-v1b-26w-4s [25]            135.857      175.291      26.871
               Em ↑      0.762    0.861   0.845   0.847      0.898     0.912       0.918       0.907     0.919    0.928
                                                                                                                                                  RD3D21 [53]                 I3DResNet-50 [88]            101.460       46.900      25.934
                Sm ↑     0.706    0.726   0.910   0.787      0.915     0.918       0.923       0.924     0.936    0.938                      TriTransNet21 [72]       ResNet-50 [24]+ViT-B [22]            680.072      139.548      10.216
                Fβω ↑    0.485    0.463   0.804   0.652      0.856     0.878       0.900       0.883     0.908    0.911                             DCF21 [81]                   ResNet-50 [24]            107.815      108.491      23.869
VT1000

           [86] M ↓      0.119    0.145   0.034   0.090      0.027     0.024       0.023       0.022     0.018    0.017                          HAINet21 [51]                     VGG-16 [89]             350.831       59.823      12.187
                Fβ ↑     0.715    0.735   0.908   0.770      0.913     0.908       0.923       0.917     0.935    0.939                        CCAFNet21 [52]                      VGG-16 [89]             153.064       41.798      64.154
               Em ↑      0.836    0.828   0.922   0.857      0.942     0.940       0.955       0.947     0.945    0.949                           DCMF22 [82]                      VGG-16 [89]             271.058       58.937      23.093
                                                                                                                                                 CMINet21 [66]                   ResNet-50 [24]            376.444      185.468      10.339
                Sm ↑     0.680    0.652   0.863   0.750      0.867     0.868       0.883       0.875     0.892    0.899
VT5000TE

                Fβω ↑    0.397    0.327   0.722   0.558      0.763     0.796       0.831       0.800     0.835    0.849                          MIDD21 [57]                           VGG-16 [89]         434.437      52.428       21.526
           [20] M ↓      0.114    0.168   0.048   0.089      0.043     0.042       0.035       0.038     0.032    0.028                         CGFNet21 [55]                          VGG-16 [89]         760.556      66.382       12.538
                Fβ ↑     0.613    0.596   0.837   0.695      0.849     0.837       0.869       0.846     0.873    0.882
                                                                                                                                                        Ours50 ‡                  ResNet-50d [26]          44.392       55.515       26.623
               Em ↑      0.795    0.782   0.891   0.824      0.899     0.907       0.924       0.910     0.930    0.941
                                                                                                                                                         Ours50                   ResNet-50d [26]          44.442       55.793       35.193
                                                                                                                                                        Ours101                  ResNet-101d [26]          63.907       93.777       27.666

complex lighting conditions and diverse human poses. The
1000 stereoscopic images in STEREO1000 [79] were collected                                                                        from Flickr, NVIDIA 3D Vision Live, and Stereoscopic Image
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                          7

                                            (a)                                                                     (b)
Fig. 5.   Precision-Recall (PR) and Fβ -Threshold curves. ?: using the multi-scale training technique. (a) RGB-D SOD methods. (b) RGB-T SOD methods.

Gallery. SSD [83] is another RGB-D SOD dataset and only B. Evaluation Metrics
includes 80 samples covering indoor and outdoor scenes.
LFSD [84] contains 100 pairs of RGB-D images and is built         To fully demonstrate the performance differences between
for saliency detection on the light field. DUTRGBD [44] is different methods, we introduced several metrics to quantita-
a recently proposed large-scale RGB-D SOD dataset, which tively evaluate the models. Specifically, S-measure [90] (Sm )
contains 1200 pairs of RGB-D images, 800 from indoors and focuses on region-aware and object-aware structural similarities
400 from outdoors. It captures a large number of challenging between the saliency map and the ground truth. MAE [91],
objects and scenes. To make a fair comparison, we conduct (M ) indicates the average absolute pixel error. F-measure [92]
experiments with two training settings. (I): One is the setup (Fβ ) is a region-based similarity metric and based on precision
in works [35], [45], [50], [64], [65], [67], [69], the training and recall. E-measure [93] (Em ) is characterized as both
set only contains 1485 pairs from NJUD and 700 pairs from image-level statistics and local pixel matching. Weighted F-
NLPR and the remaining data of these datasets as the test set. measure [94] (F ω ) improves the metric Fβ by using a weighted
                                                                                β
(II): The other can be found in recent works [44], [46], [51], precision for measuring exactness and a weighted recall for
[72], [81]. 700 images from NLPR, 1485 images from NJUD measuring completeness. In addition to these metrics, we also
and 800 images from DUTRGBD are chosen as the training introduce “Precision-Recall” and “Fβ -Threshold” curves to
data.                                                           present a comprehensive comparison of the model performance.

     b) RGB-T SOD.: VT821 [85] includes 821 RGB-T image C. Implementation Detail
pairs and their ground truth annotations for the saliency        The backbone network is initialized by the weight pretrained
detection purpose. VT1000 [86] contains 1000 pairs of RGB-T on ImageNet, and the remaining structures are initialized
images including more than 400 kinds of common objects randomly using the default method of the PyTorch toolbox.
collected in 10 types of scenes under different illumination All our models are trained for 100 epochs with a batch size
conditions. VT5000 [20] is a large-scale dataset containing of 8 using the SGD optimizer with a momentum of 0.9 and a
5000 pairs of RGB-T images with ground truth annotations, weight decay of 0.0005 on an NVIDIA GTX 2080Ti GPU. The
which greatly improves the complexity and diversity of the learning rate is initialized as 0.005 and scheduled by the cosine
scenes. It is split into VT5000TR (2500) and VT5000TE (2500). strategy. The single-channel depth/thermal input is repeated
Following the setting of recent works [54]–[57], the training three times along the channel dimension to facilitate the use
set only contains the 2500 samples from VT5000TR and all of pretrained parameters, and RGB and depth/thermal images
remaining data are used as the test set.                      are resized to 256 × 256. Some data augmentation techniques
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                    8

       (1)
        (2)
        (3)
        (4)
        (5)
        (6)
        (7)
        (8)
        (9)
        (10)
        (11)

Fig. 6. Qualitative comparison of our model with seven recent state-of-the-art models. (1): Image; (2) Depth; (3) Mask; (4): Ours101 (II); (5): DCMF [82]; (6):
CCAFNet [52]; (7): HAINet [51]; (8): DCF [81]; (9): TriTransNet [72]; (10): RD3D [53]; (11): SPNet [69].

are also introduced into the training phase to avoid over-fitting,               (1)

such as some affine transforms, horizontal flipping and color
                                                                                 (2)

jittering. In the test stage, the RGB and depth/thermal images
are resized to 256 × 256, and the final prediction is resized
                                                                                 (3)

back to the original size for evaluation. For all experiments,
                                                                                 (4)

the model is supervised by the hybrid loss [95].
                                                                                 (5)

D. Comparison
                                                                                 (6)

   To demonstrate the effectiveness of our method, we
                                                                                 (7)

compare it with the recent 31 state-of-the-art RGB-D and
RGB-T SOD methods including CPFP [43], DMRA [44],
                                                                                 (8)

MMCI [42], TANet [41], JLDCF [50], S2MA [64], UC-
Net [70], BBSNet [67], CMWNet [45], CoNet [46], Fig. 7. Visual ablation experiments for different components. (1): Image;
DANet [34], HDFNet [38], ICNet [80], D3Net [35], SP- (2) Depth; (3) Mask; (4): +IMCA+IMSA+CSSA; (5): +IMCA+CSSA; (6):
Net [69], RD3D [53], TriTransNet [72], DCF [81], HAINet [51], +IMCA+IMSA; (7): +IMCA; (8): Baseline.
CCAFNet [52], UCNet-CVAE [65], CMINet [66], and
DCMF [82], MTMR [85], M3S-NIR [87], ADF [20],
SDGL [86], MIDD [57], CSRNet [56], CGFNet [55] and spatial attention [61]–[63], which deserves more attention in
ECFFNet [54]. All data used in experiments are from the future work. To compare the overall performance of different
resources released by the authors.                            methods, we also show PR and Fβ curves in Tab. 5. It can
     a) Quantitative Comparison.: In Tab. I, Tab. II and be seen that our methods correspond to the curves positioned
Tab. III, the detailed results from all competitors on ten more upward, which indicates that the proposed model performs
datasets in two tasks and five metrics are listed and our better.
methods perform best on all these datasets. For RGB-D SOD,         b) Qualitative Comparison.: Some visual comparisons
“Ours101 (II)” achieves the best average performance of 0.912 of different models are listed in Fig. 6, which covers the repre-
Sm , 0.886 Fβω , 0.035 M , 0.947 Em and 0.914 Fβ , which sentative methods published recently. As we can see that these
are significant relative gains of 0.98% Sm , 0.60%Fβω , 5.43% samples have various types of scenes and objects, including
M , 0.36% Em and 0.77% Fβ over the second-best method the large object with large internal variability (Column 1-5),
TriTransNet [72] which has more parameters, FLOPs and the out-of-bounds object (Column 1, 2, 8, 10, and 11), the
latency (see Tab. IV). In the comparison on RGB-T SOD, our medium-sized object with unclear and complex boundaries
method also has more consistent and obvious performance in the low-brightness scene (Column 6-9), the sample with
gains. It should be emphasized that this work focuses on a strong background interference (Column 1, 3, 6, and 11)
exploring and designing a new architecture suitable for bi- These results fully demonstrate the robustness of the proposed
modal SOD. Therefore, the whole network is very simple and algorithm against different data, which can be attributed to
we do not explore collaboration with other modules, such as the powerful information modeling capability of the proposed
ASPP [58], DenseASPP [59], and convolutional channel and view-mixed attention mechanism.
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                                                                                                                                      9

                                                                  TABLE V
 A BLATION ANALYSIS OF THE DIFFERENT COMPONENTS . ‡: T HE MODEL VARIANT WHERE OUR SELF - ATTENTION BLOCK IS REPLACED BY THE SHIFTED
WINDOW BASED SELF - ATTENTION [23]. “(L IN .)”: T HE MODEL VARIANT WHERE THE C ONV-FFN IS REPLACED BY THE LINEAR FFN. T HE BEST RESULTS
                                                         ARE HIGHLIGHTED USING RED .

                                                                NJUD                                                         SIP                                                   STEREO1000                                                      AVERAGE
 METHOD
                                          Sm ↑         Fβω ↑    M ↓         Em ↑          Fβ ↑         Sm ↑     Fβω ↑        M ↓           Em ↑       Fβ ↑        Sm ↑         Fβω ↑  M ↓   Em ↑                    Fβ ↑      Sm ↑         Fβω ↑     M ↓   Em ↑        Fβ ↑
 Baseline                                  0.917       0.891     0.034       0.939        0.922        0.883    0.847        0.048         0.924     0.891        0.903        0.862      0.039        0.935        0.899     0.901        0.867      0.040    0.933   0.904
 +IMCA                                     0.920       0.897     0.032       0.950        0.923        0.886    0.853        0.047         0.927     0.895        0.908        0.873      0.035        0.945        0.907     0.905        0.874      0.038    0.941   0.908
 +IMCA+IMSA                                0.917       0.895     0.032       0.949        0.923        0.889    0.858        0.045         0.930     0.898        0.911        0.879      0.034        0.949        0.909     0.906        0.877      0.037    0.943   0.910
 +IMCA+CSSA                                0.922       0.901     0.031       0.952        0.926        0.892    0.863        0.043         0.932     0.901        0.911        0.878      0.034        0.947        0.906     0.908        0.881      0.036    0.944   0.911
 +IMCA+IMSA+CSSA                           0.921       0.901     0.031       0.953        0.925        0.893    0.864        0.042         0.933     0.902        0.913        0.882      0.033        0.949        0.912     0.909        0.882      0.035    0.945   0.913
 +IMCA+IMSA‡ +CSSA‡                        0.921       0.902     0.030       0.954        0.926        0.884    0.852        0.047         0.925     0.891        0.909        0.876      0.036        0.946        0.906     0.905        0.877      0.038    0.942   0.908
 +IMCA+IMSA+CSSA (Lin.)                    0.918       0.897     0.033       0.949        0.923        0.885    0.851        0.046         0.928     0.893        0.910        0.876      0.035        0.948        0.908     0.904        0.875      0.038    0.942   0.908

                                                            TABLE VI
A BLATION ANALYSIS OF THE CHANNEL AND SPATIAL ATTENTION BRANCHES IN THE VIEW- MIXED ATTENTION BLOCK . ×0 IS EQUIVALENT TO THE BRANCH
                                                  BEING REMOVED FROM THE BLOCK .

                                                               NJUD                                                         SIP                                                   STEREO1000                                                       AVERAGE
 SPATIAL            CHANNEL
                                        Sm ↑       Fβω ↑       M ↓         Em ↑         Fβ ↑       Sm ↑        Fβω ↑        M ↓           Em ↑      Fβ ↑         Sm ↑         Fβω ↑  M ↓   Em ↑                 Fβ ↑          Sm ↑         Fβω ↑     M ↓   Em ↑        Fβ ↑
     ×α               ×β                0.921      0.901       0.031       0.953        0.925      0.893       0.864        0.042         0.933     0.902        0.913        0.882     0.033        0.949      0.912         0.909        0.882      0.035    0.945   0.913
     ×0.5             ×0.5              0.920      0.900       0.030       0.952        0.923      0.891       0.865        0.044         0.932     0.904        0.912        0.880     0.034        0.947      0.910         0.908        0.882      0.036    0.944   0.912
      ×0               ×1               0.918      0.898       0.033       0.949        0.921      0.886       0.856        0.046         0.928     0.897        0.910        0.877     0.034        0.948      0.907         0.905        0.877      0.038    0.942   0.908
      ×1               ×0               0.922      0.902       0.031       0.953        0.926      0.889       0.858        0.046         0.928     0.897        0.910        0.878     0.034        0.947      0.909         0.907        0.879      0.037    0.943   0.911

                             & 0 , 8                                                       & 0 , 8                                                       & 0 , 8                                                        & 0 , 8  
                                                                                                                                                                                                                                                        0
                                                                                                                                                                                                                                                                        0
                                                                                                                                                                                                                                                        1
                                                                                                                                                                                                                                                                        1
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        2
                                                                                                                                                                                                                                                        2
                                                                                                                                                                                                                                                                        3
                                                                                                                                                                                                                                                        3
                                                         6 $

                                                                                                                      6 $

                                                                                                                                                                                        6 $

                                                                                                                                                                                                                                                         6 $
                    /t

                                                                                   /t

                                                                                                                                                    /t

                                                                                                                                                                                                                    /t
                             rgb

                                          d/t

                                                                                            rgb

                                                                                                         d/t

                                                                                                                                                             rgb

                                                                                                                                                                          d/t

                                                                                                                                                                                                                              rgb

                                                                                                                                                                                                                                           d/t
        gb

                                                                      gb

                                                                                                                                     gb

                                                                                                                                                                                                      gb
                 d

                                                                                d

                                                                                                                                                 d

                                                                                                                                                                                                                  d
               6 $

                                                                              6 $

                                                                                                                                               6 $

                                                                                                                                                                                                                6 $
                                                    & 6

                                                                                                                 & 6

                                                                                                                                                                                   & 6

                                                                                                                                                                                                                                                    & 6
      r

                                                                    r

                                                                                                                                   r

                                                                                                                                                                                                     r
    6 $

                                                                  6 $

                                                                                                                                 6 $

                                                                                                                                                                                                   6 $
                                        rgb

                                                                                                       rgb

                                                                                                                                                                        rgb

                                                                                                                                                                                                                                         rgb
              , 0

                                                                            , 0

                                                                                                                                              , 0

                                                                                                                                                                                                              , 0
                           d/t

                                                                                          d/t

                                                                                                                                                           d/t

                                                                                                                                                                                                                            d/t
  , 0

                                                                , 0

                                                                                                                               , 0

                                                                                                                                                                                               , 0
                      & $

                                   & $

                                                                                      & $

                                                                                                   & $

                                                                                                                                                      & $

                                                                                                                                                                   & $

                                                                                                                                                                                                                       & $

                                                                                                                                                                                                                                    & $
                     , 0

                                  , 0

                                                                                    , 0

                                                                                                 , 0

                                                                                                                                                     , 0

                                                                                                                                                                  , 0

                                                                                                                                                                                                                      , 0

                                                                                                                                                                                                                                   , 0
Fig. 8. Visualization of the weights α and β from different attention blocks in CMIU 1-4 of our four models: “∗0 ”: “Ours50 (I)”, “∗1 ”: “Ours50 (II)”, “∗2 ”:
“Ours101 (I)” and “∗3 ”: “Ours101 (II)”. “IMSAx ”: The intra-modal self-attention block from the stream corresponding to the x modality. “IMCAa→b ”: The
inter-modal cross-attention block with the input b for generating Q and the input a for generating K and V . “CSSA”: The cross-scale self-attention block.

E. Ablation Analysis                                              the model and therefore act in different roles. We show a
   To evaluate the effectiveness of the proposed components careful ablation analysis in Tab. V and Fig. 7 for different
and investigate their importance and contributions, based on combinations of them. The results in the table and the visual
the model “Ours50 (I)”, we construct the ablation study on comparison reflect that they all have a positive effect on the
RGB-D SOD datasets. At first, we build a CNN-based FPN- model and the best performance is achieved when they coexist.
like two-stream model as the baseline network in which the It further leads us to wonder whether a better performance
features with the same resolution from both modalities are could be obtained by repeatedly stacking more such structures.
added directly. As can be seen from Tab. V, it is a sufficiently This may be beyond the original intention of our structural
strong baseline model, which also makes the gains from our design, but it is worth exploring further in the future. Besides,
approach more reliable. We also attach some other ablation we also try to replace these three self-attention blocks with
analyses about the visualization of attention maps and some the shifted window based self-attention block from the classic
typical failure cases.                                            work of the vision transformer, Swin Transformer [23]. In each
     a) Effectiveness of Inter-Modal Cross-Attention.: In our block, a window-based self-attention module and a shifted
method, the inter-modal cross-attention enables the interaction one are placed sequentially. The window size and the number
and fusion of information between modalities by aligning of heads are set to 7 and 2. Layer Normalization is used to
related representations and gathering global context cues. In normalize internal feature maps. As can be seen from the
the ablation analysis in Tab. V, we show its performance comparison in Tab. IV and Tab. V, with a similar amount of
improvement compared to the baseline model. The signifi- parameters and FLOPs, our method has higher FPS and better
cant improvement in average performance demonstrates the average performance, which indicates the competitiveness of
effectiveness of such a structural design.                        the proposed structure.
     b) Effectiveness of Inter-Modal and Cross-Scale Self-             c) Region-wise or Position-wise?: The utilization of the
Attention.: The intra-modal and cross-scale self-attention blocks local context is one of the key factors for the success of
are located at different locations in the information flow of convolution in 2D vision tasks. Although the transformer can
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                                                                          10

                                                                TABLE VII
       A BLATION ANALYSIS OF THE DIFFERENT COMPONENTS . T HE BEST RESULTS ARE HIGHLIGHTED USING RED . W HEN “NUM=0”, THE MODEL IS
                                                      EQUIVALENT TO THE BASELINE .

                            NJUD                                               SIP                                             STEREO1000                                           AVERAGE
 NUM
           Sm ↑     Fβω ↑   M ↓      Em ↑      Fβ ↑       Sm ↑     Fβω ↑       M ↓       Em ↑     Fβ ↑     Sm ↑            Fβω ↑  M ↓   Em ↑             Fβ ↑      Sm ↑     Fβω ↑     M ↓   Em ↑           Fβ ↑
   4       0.921    0.901   0.031    0.953     0.925      0.893    0.864       0.042     0.933    0.902    0.913           0.882    0.033     0.949      0.912     0.909    0.882       0.035     0.945    0.913
   3       0.918    0.897   0.033    0.950     0.922      0.892    0.863       0.043     0.933    0.901    0.909           0.874    0.035     0.946      0.907     0.906    0.878       0.037     0.943    0.910
   2       0.919    0.896   0.032    0.951     0.925      0.889    0.856       0.045     0.930    0.895    0.909           0.873    0.035     0.945      0.907     0.906    0.875       0.037     0.942    0.909
   1       0.919    0.893   0.033    0.945     0.921      0.882    0.842       0.051     0.918    0.885    0.909           0.873    0.036     0.943      0.906     0.903    0.869       0.040     0.935    0.904
   0       0.917    0.891   0.034    0.939     0.922      0.883    0.847       0.048     0.924    0.891    0.903           0.862    0.039     0.935      0.899     0.901    0.867       0.040     0.933    0.904

                                                             TABLE VIII
A BLATION ANALYSIS OF THE PATH SIZE FOR THE PTRE IN DIFFERENT DECODING LEVELS . I N THESE FORMS , THE FOUR NUMBERS CORRESPOND TO THE
                                 FOUR LEVELS FROM TOP TO BOTTOM , RESPECTIVELY. “—”: O UT OF MEMORY.

                   FLOPs                     NJUD                                          SIP                                         STEREO1000                                       AVERAGE
 PATCH SIZE
                    (G)     Sm ↑    Fβω ↑    M ↓      Em ↑     Fβ ↑    Sm ↑      Fβω ↑     M ↓    Em ↑     Fβ ↑            Sm ↑    Fβω ↑  M ↓   Em ↑            Fβ ↑    Sm ↑    Fβω ↑     M ↓   Em ↑       Fβ ↑
    1, 1, 1, 1     71.853    —        —       —         —       —       —         —        —        —       —                —      —         —        —       —          —      —         —         —       —
    2, 2, 2, 2     50.907   0.918   0.896    0.032     0.948   0.920   0.889     0.860    0.044    0.931   0.898           0.914   0.882    0.033     0.949   0.911     0.907   0.879     0.036    0.943   0.910
    4, 4, 4, 4     45.731   0.917   0.896    0.033     0.948   0.920   0.893     0.865    0.042    0.934   0.903           0.912   0.880    0.034     0.948   0.909     0.907   0.880     0.036    0.943   0.911
   8, 8, 8, 8      44.442   0.921   0.901    0.031     0.953   0.925   0.893     0.864    0.042    0.933   0.902           0.913   0.882    0.033     0.949   0.912     0.909   0.882     0.035    0.945   0.913
  8, 16, 16, 16    44.120   0.920   0.900    0.032     0.951   0.924   0.892     0.863    0.044    0.932   0.901           0.912   0.878    0.034     0.947   0.908     0.908   0.880     0.037    0.943   0.911
  8, 16, 32, 32    44.039   0.915   0.894    0.033     0.948   0.917   0.883     0.851    0.047    0.923   0.891           0.914   0.884    0.033     0.950   0.912     0.904   0.876     0.038    0.940   0.907
  8, 16, 32, 64    44.021   0.916   0.893    0.034     0.947   0.917   0.890     0.861    0.042    0.933   0.898           0.911   0.878    0.035     0.947   0.908     0.906   0.877     0.037    0.942   0.908

                                                                                                                                            Image               Depth           Mask
facilitate the propagation of global information, it does not
pay enough attention to the local region, which may lead
to important local details being overlooked. To alleviate this
problem, we introduce locality to assist the attention operations.
The Conv-FFN (Sec. III-C0d) is used to replace the original
                                                                                                            Channel-View

position-wise FFN. The comparison between Row 5 and Row
7 in Tab. V reflects that the region-wise operation in the FFN
affects the overall performance.
                                                                                                            Spatial-View

      d) Analysis of View-Mixed Attention.: The good perfor-
mance of the proposed view-mixed attention can be seen from
the aforementioned experiments and comparisons. To further
verify the effectiveness of this multi-view attention variant, in
                                                                                                            Spatial-Attn

Tab. VI, we compare the performance of the two branches using
different combination strategies based on the model “Ours50 (I)”
and our strategy shows the best performance. It is worth noting
that when both weights are fixed at 0.5, the model is also
                                                                                                            Spatial-Attn

competitive. Besides, from the summary of the weights in
different CMIUs in Fig. 8, the learned α and β are around
0.5. The differences between learned parameters in different               IMSA-RGB      IMSA-D     IMCA-RGB2D     IMCA-D2RGB       CSSA
positions further reflect the flexibility of our method, which
also enables our method to remain optimal in most metrics. Fig. 9. Visualization of different attention operations in the 1st CMIU. In
Besides, the figure also reflects some interesting phenomena. these maps, normalization and upsampling based on the bilinear interpolation
                                                                  are applied to show them more clearly. Besides, we also visually compare the
In the shallow layer, the overall weight values are relatively spatial attention maps of two different queries marked by the blue and red
larger, and the channel branch in the cross-modal interaction squares from the background and foreground of the image. “Channe-View”:
block IMCA plays a more important role. This also implies The pairwise channel similarity score map from the channel-view attention
                                                                  operation. “Spatial-View”: The pairwise spatial similarity score map from
the necessity of introducing shallow features as well as the the patch-wise spatial-view attention operation. “Spatial-Attn”: The global
channel view. Besides, despite the differences in model capacity spatial attention map corresponding to the position of the blue and red squares.
and training data, the trends in the four model weights are “IMSA-x”: The maps from the IMSA corresponding to the x modality. “IMCA-
                                                                  a2b”: The maps from the IMCA with the input b for generating Q and the
very similar. The underlying reason is still worth exploring, input a for generating K and V . “CSSA”: The maps from the CSSA.
and it also further highlights the potential of the channel-wise
interaction pattern in the feature decoding stage.
      e) Number of Stages with the CMIU.: To explore the the model has been consistently decreased on multiple datasets.
effect of the CMIU, we gradually replace the CMIU in the                f) Patch Size of the PTRE.: The size of the patch re-
original CAVER with the simple convolutional layer in the embedding in the PTRE is an important hyperparameter. We
order from shallow to deep. The experimental results are listed compare several settings in Tab. VIII. It should be noted
in Tab. VII. It can be seen from the table that with the gradual that “1, 1, 1, 1” is actually equivalent to the standard attention
removal of the CMIU from shallow to deep, the performance of operation [21], which cannot be trained on our device due to its
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                   11

           1             2            3           4           5           6            7           8             9           10           11           12

Fig. 10.       Visualization of some typical failure cases from RGB-D and RGB-T test datasets.

large memory requirements. As shown in the table, compared                          2) Ambiguity of the definition. In our collection, the
with other settings, “8, 8, 8, 8” has the best average performance                      definition of saliency objects in some samples (Case
and a moderate computational cost, so, it is used as the                                3-6, 8, and 11 in Fig. 10) do not meet the criteria for
default setting in our other experiments. This also reflects that                       visual saliency. The performance loss brought by these
simply increasing the computational cost does not necessarily                           samples is difficult to ignore for some bi-modal SOD
lead to a better performance, which sometimes depends on a                              datasets with small data volumes involved in this paper.
more reasonable structural design. An interesting phenomenon                            But our model does segment those visually more salient
occurs under the setting of the final line of Tab. VIII. In our                         objects well. This can actually provide some meaningful
experiments, the input image size is 256, and the sizes of the                          references for future work on the label calibration task.
four feature maps extracted from the encoder are 64, 32, 16, and                    3) Misleadingness of the annotation image. As shown in
8, respectively. So in this case, the size of the attention maps                        cases 7 and 9 in Fig. 10, our method yields visually
in all spatial branches is 1 × 1, and the process of gathering                          more accurate predictions for these RGB images, but
information from the value V is simplified to scale V using                             incomplete or unaligned masks from the test dataset
a specific scalar factor. Its performance is not as good as the                         cause unexpected errors in the evaluation process.
setting “8, 8, 8, 8”, but it is still competitive. The existence                  The aforementioned issues are still very challenging now, and
of the channel-view component does play an important role                         these will be the focus of our future work.
in such competitive performance. It builds dense interactions
between feature channels by performing dynamic feature fusion
                                                                                                             V. C ONCLUSION
of different global views of the entire image. So, it can provide
effective assistance for such a simple model. Considering its                        In this paper, we rethink the architecture design for the
more efficient computation, it can be the basis for exploring                     bi-modal SOD task. A novel view-mixed transformer-based
lighter model variants.                                                           top-down information propagation path is proposed to enhance
      g) Visualization of Attention Maps.: To visualize the                       the capability of perceiving and excavating the important
impact of attention operations at different positions, we show                    global cues in intra-modal features and simplify the cross-
in Fig. 9 the learned pair-wise similarity score map which is                     modal long-range interaction and alignment. And by using the
calculated by the dot product between the patch-wise query                        PTRE, the computational and storage intensity of the matrix
and key. To show the learning effect more intuitively, we also                    operation in the attention block is effectively reduced, which
supplement the normalized alignment score map of the query                        makes it possible to process multi-scale high-resolution features.
token corresponding to the red marker in RGB and depth images                     In addition, the convolutional FFN further enhances the
and the global key token sequence. It can be noticed that in the                  critical local details in the feature map. Extensive experimental
whole process, the feature discriminativeness and the intra-class                 comparisons show the effectiveness of the proposed method.
similarity are significantly enhanced. From another standpoint,
the global dependency pattern can be clearly observed in each                                                  R EFERENCES
map of different blocks, which is the source of the power of                       [1] Y. Wei, X. Liang, Y. Chen, X. Shen, M.-M. Cheng, J. Feng, Y. Zhao,
the attention operation.                                                               and S. Yan, “Stc: A simple to complex framework for weakly-supervised
                                                                                       semantic segmentation,” TPAMI, vol. 39, no. 11, pp. 2314–2320, 2017.
      h) Analysis of Typical Failure Cases.: We show some
                                                                                   [2] X. Zhao, L. Zhang, and H. Lu, “Automatic polyp segmentation via
typical failure cases in Fig. 10. The visualization results mainly                     multi-scale subtraction network,” in MICCAI, 2021, pp. 120–130.
involve the following three very thorny problems:                                  [3] D.-P. Fan, G.-P. Ji, T. Zhou, G. Chen, H. Fu, J. Shen, and L. Shao,
                                                                                       “Pranet: Parallel reverse attention network for polyp segmentation,” in
   1) Uncertainty of the object. In Case 1, 2, 10, and 12, the                         MICCAI, 2020, pp. 263–273.
      object of interest is difficult to be completely captured                    [4] X. Lu, W. Wang, J. Shen, D. Crandall, and J. Luo, “Zero-shot video
                                                                                       object segmentation with co-attention siamese networks,” TPAMI, pp.
      due to the extremely complex scene. The location and                             1–1, 2020.
      segmentation of such objects rely on the model’s ability to                  [5] D.-P. Fan, W. Wang, M.-M. Cheng, and J. Shen, “Shifting more attention
      adapt to such significant environmental interference. Our                        to video salient object detection,” in CVPR, 2019, pp. 8546–8556.
                                                                                   [6] X. Zhao, Y. Pang, J. Yang, L. Zhang, and H. Lu, “Multi-source fusion and
      architectural form based on global relationship modeling                         automatic predictor selection for zero-shot video object segmentation,”
      may lead to weaker performance for such objects.                                 in ACM MM, 2021, pp. 2645–2653.
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                           12

 [7] R. Zhao, W. Ouyang, and X. Wang, “Unsupervised salience learning for             [36] L. Qu, S. He, J. Zhang, J. Tian, Y. Tang, and Q. Yang, “Rgbd salient
     person re-identification,” in CVPR, 2013, pp. 3586–3593.                              object detection via deep fusion,” TIP, vol. 26, no. 5, pp. 2274–2285,
 [8] D.-P. Fan, G.-P. Ji, G. Sun, M.-M. Cheng, J. Shen, and L. Shao,                       2017.
     “Camouflaged object detection,” in CVPR, 2020, pp. 2777–2787.                    [37] J. Han, H. Chen, N. Liu, C. Yan, and X. Li, “Cnns-based rgb-d saliency
 [9] D.-P. Fan, G.-P. Ji, M.-M. Cheng, and L. Shao, “Concealed object                      detection via cross-view transfer and multiview fusion,” TC, vol. 48,
     detection,” TPAMI, 2021.                                                              no. 11, pp. 3171–3183, 2018.
[10] Y. Pang, X. Zhao, T.-Z. Xiang, L. Zhang, and H. Lu, “Zoom in and                 [38] Y. Pang, L. Zhang, X. Zhao, and H. Lu, “Hierarchical dynamic filtering
     out: A mixed-scale triplet network for camouflaged object detection,” in              network for rgb-d salient object detection,” in ECCV, 2020, pp. 235–252.
     CVPR, 2022.                                                                      [39] H. Chen, Y. Deng, Y. Li, T.-Y. Hung, and G. Lin, “Rgbd salient object
[11] W. Wang, J. Shen, and H. Ling, “A deep network solution for attention                 detection via disentangled cross-modal fusion,” TIP, vol. 29, pp. 8407–
     and aesthetics aware photo cropping,” TPAMI, vol. 41, no. 7, pp. 1531–                8416, 2020.
     1544, 2019.                                                                      [40] N. Wang and X. Gong, “Adaptive fusion for rgb-d salient object detection,”
[12] C. Guo and L. Zhang, “A novel multiresolution spatiotemporal saliency                 IEEE Access, vol. 7, pp. 55 277–55 284, 2019.
     detection model and its applications in image and video compression,”            [41] H. Chen and Y. Li, “Three-stream attention-aware network for rgb-d
     TIP, vol. 19, no. 1, pp. 185–198, 2010.                                               salient object detection,” TIP, vol. 28, no. 6, pp. 2825–2835, 2019.
[13] J. Wei, S. Wang, and Q. Huang, “F3 net: Fusion, feedback and focus for           [42] H. Chen, Y. Li, and D. Su, “Multi-modal fusion network with multi-scale
     salient object detection,” in AAAI, 2020, pp. 12 321–12 328.                          multi-path and cross-modal interactions for rgb-d salient object detection,”
[14] J. Wei, S. Wang, Z. Wu, C. Su, Q. Huang, and Q. Tian, “Label decoupling               PR, vol. 86, pp. 376–385, 2019.
     framework for salient object detection,” in CVPR, 2020, pp. 13 022–              [43] J.-X. Zhao, Y. Cao, D.-P. Fan, M.-M. Cheng, X.-Y. Li, and L. Zhang,
     13 031.                                                                               “Contrast prior and fluid pyramid integration for rgbd salient object
[15] X. Zhao, Y. Pang, L. Zhang, H. Lu, and L. Zhang, “Suppress and balance:               detection,” in CVPR, 2019, pp. 3927–3936.
     A simple gated network for salient object detection,” in ECCV, 2020,             [44] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-scale
     pp. 35–51.                                                                            recurrent attention network for saliency detection,” in ICCV, 2019, pp.
[16] J.-J. Liu, Q. Hou, and M.-M. Cheng, “Dynamic feature integration for                  7253–7262.
     simultaneous detection of salient object, edge and skeleton,” TIP, pp.           [45] G. Li, Z. Liu, L. Ye, Y. Wang, and H. Ling, “Cross-modal weighting
     1–15, 2020.                                                                           network for rgb-d salient object detection,” in ECCV, 2020, pp. 665–681.
[17] Y. Pang, X. Zhao, L. Zhang, and H. Lu, “Multi-scale interactive network          [46] W. Ji, J. Li, M. Zhang, Y. Piao, and H. Lu, “Accurate rgb-d salient object
     for salient object detection,” in CVPR, 2020, pp. 9410–9419.                          detection via collaborative learning,” in ECCV, 2020, pp. 52–69.
[18] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “Rgb-d salient            [47] X. Zhao, Y. Pang, L. Zhang, H. Lu, and X. Ruan, “Self-supervised
     object detection: A survey,” CVMJ, pp. 1–33, 2021.                                    representation learning for rgb-d salient object detection,” in AAAI, 2021.
[19] K. Fu, Y. Jiang, G.-P. Ji, T. Zhou, Q. Zhao, and D.-P. Fan, “Light field         [48] X. Zhao, Y. Pang, L. Zhang, and H. Lu, “Joint learning of salient object
     salient object detection: A review and benchmark,” CVMJ, vol. 8, no. 4,               detection, depth estimation and contour extraction,” TIP, vol. 31, pp.
     pp. 509–534, 2022.                                                                    7350–7362, 2022.
[20] Z. Tu, Y. Ma, Z. Li, C. Li, J. Xu, and Y. Liu, “Rgbt salient object detection:
                                                                                      [49] Z. Zhang, Z. Lin, J. Xu, W.-D. Jin, S.-P. Lu, and D.-P. Fan, “Bilateral
     A large-scale dataset and benchmark,” ArXiv, vol. abs/2007.03262, 2020.
                                                                                           attention network for rgb-d salient object detection,” TIP, vol. 30, pp.
[21] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,               1949–1961, 2021.
     L. u. Kaiser, and I. Polosukhin, “Attention is all you need,” in NIPS,
                                                                                      [50] K. Fu, D.-P. Fan, G.-P. Ji, Q. Zhao, J. Shen, and C. Zhu, “Siamese
     vol. 30, 2017.
                                                                                           network for rgb-d salient object detection and beyond,” TPAMI, vol. 44,
[22] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,
                                                                                           no. 9, pp. 5541–5559, 2022.
     T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly,
                                                                                      [51] G. Li, Z. Liu, M. Chen, Z. Bai, W. Lin, and H. Ling, “Hierarchical
     J. Uszkoreit, and N. Houlsby, “An image is worth 16x16 words:
                                                                                           alternate interaction network for rgb-d salient object detection,” TIP,
     Transformers for image recognition at scale,” in ICLR, 2021.
                                                                                           vol. 30, pp. 3528–3542, 2021.
[23] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and B. Guo,
     “Swin transformer: Hierarchical vision transformer using shifted windows,”       [52] W. Zhou, Y. Zhu, J. Lei, J. Wan, and L. Yu, “Ccafnet: Crossflow and
     in ICCV, 2021, pp. 9992–10 002.                                                       cross-scale adaptive fusion network for detecting salient objects in rgb-d
                                                                                           images,” TMM, pp. 1–1, 2021.
[24] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
     recognition,” in CVPR, 2016, pp. 770–778.                                        [53] Q. Chen, Z. Liu, Y. X. Zhang, K. Fu, Q. Zhao, and H. Du, “Rgb-d
[25] S.-H. Gao, M.-M. Cheng, K. Zhao, X.-Y. Zhang, M.-H. Yang, and P. Torr,                salient object detection via 3d convolutional neural networks,” in AAAI,
     “Res2net: A new multi-scale backbone architecture,” TPAMI, vol. 43,                   2021.
     no. 2, pp. 652–662, Feb 2021.                                                    [54] W. Zhou, Q. Guo, J. Lei, L. Yu, and J.-N. Hwang, “Ecffnet: Effective
[26] T. He, Z. Zhang, H. Zhang, Z. Zhang, J. Xie, and M. Li, “Bag of tricks                and consistent feature fusion network for rgb-t salient object detection,”
     for image classification with convolutional neural networks,” in CVPR,                TCSVT, vol. 32, no. 3, pp. 1224–1235, 2022.
     June 2019, pp. 558–567.                                                          [55] J. Wang, K. Song, Y. Bao, L. Huang, and Y. Yan, “Cgfnet: Cross-guided
[27] L. Itti, C. Koch, and E. Niebur, “A model of saliency-based visual                    fusion network for rgb-t salient object detection,” TCSVT, pp. 1–1, 2021.
     attention for rapid scene analysis,” TPAMI, vol. 20, no. 11, pp. 1254–           [56] F. Huo, X. Zhu, L. Zhang, Q. Liu, and Y. Shu, “Efficient context-guided
     1259, 1998.                                                                           stacked refinement network for rgb-t salient object detection,” TCSVT,
[28] T. Liu, Z. Yuan, J. Sun, J. Wang, N. Zheng, X. Tang, and H.-Y. Shum,                  pp. 1–1, 2021.
     “Learning to detect a salient object,” TPAMI, vol. 33, no. 2, pp. 353–367,       [57] Z. Tu, Z. Li, C. Li, Y. Lang, and J. Tang, “Multi-interactive dual-decoder
     2011.                                                                                 for rgb-thermal salient object detection,” TIP, vol. 30, pp. 5678–5691,
[29] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned                 2021.
     salient region detection,” in CVPR, 2009, pp. 1597–1604.                         [58] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille,
[30] O. Ronneberger, P. Fischer, and T. Brox, “U-net: Convolutional networks               “Deeplab: Semantic image segmentation with deep convolutional nets,
     for biomedical image segmentation,” in MICCAI, 2015, pp. 234–241.                     atrous convolution, and fully connected crfs,” TPAMI, vol. 40, no. 4, pp.
[31] A. Borji, M.-M. Cheng, Q. Hou, H. Jiang, and J. Li, “Salient object                   834–848, 2017.
     detection: A survey,” CVMJ, vol. 5, pp. 117–150, 2014.                           [59] M. Yang, K. Yu, C. Zhang, Z. Li, and K. Yang, “Denseaspp for semantic
[32] W. Wang, Q. Lai, H. Fu, J. Shen, H. Ling, and R. Yang, “Salient object                segmentation in street scenes,” in CVPR, June 2018, pp. 3684–3692.
     detection in the deep learning era: An in-depth survey,” TPAMI, pp. 1–1,         [60] H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia, “Pyramid scene parsing
     2021.                                                                                 network,” in CVPR, 2017, pp. 2881–2890.
[33] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “Rgbd salient object                 [61] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” CVPR,
     detection: A benchmark and algorithms,” in ECCV, 2014, pp. 92–109.                    pp. 7132–7141, 2018.
[34] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A single stream                [62] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon, “Cbam: Convolutional block
     network for robust and real-time rgb-d salient object detection,” in ECCV,            attention module,” in ECCV, 2018, pp. 3–19.
     2020, pp. 646–662.                                                               [63] X. Li, W. Wang, X. Hu, and J. Yang, “Selective kernel networks,” in
[35] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking rgb-                CVPR, June 2019, pp. 510–519.
     d salient object detection: Models, data sets, and large-scale benchmarks,”      [64] N. Liu, N. Zhang, and J. Han, “Learning selective self-mutual attention
     TNNLS, vol. 32, no. 5, pp. 2075–2089, 2021.                                           for rgb-d saliency detection,” in CVPR, 2020, pp. 13 753–13 762.
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                   13

[65] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Saleh, S. Aliakbarian, and            [93] D.-P. Fan, C. Gong, Y. Cao, B. Ren, M.-M. Cheng, and A. Borji,
     N. Barnes, “Uncertainty inspired rgb-d saliency detection,” TPAMI,                   “Enhanced-alignment measure for binary foreground map evaluation,”
     vol. 44, no. 9, pp. 5761–5779, 2022.                                                 in IJCAI, 2018, pp. 698–704.
[66] J. Zhang, D.-P. Fan, Y. Dai, X. Yu, Y. Zhong, N. Barnes, and L. Shao,           [94] R. Margolin, L. Zelnik-Manor, and A. Tal, “How to evaluate foreground
     “Rgb-d saliency detection via cascaded mutual information minimization,”             maps?” in CVPR, 2014, pp. 248–255.
     in ICCV, 2021, pp. 4318–4327.                                                   [95] X. Qin, Z. Zhang, C. Huang, C. Gao, M. Dehghan, and M. Jagersand,
[67] Y. Zhai, D.-P. Fan, J. Yang, A. Borji, L. Shao, J. Han, and L. Wang,                 “Basnet: Boundary-aware salient object detection,” in CVPR, 2019, pp.
     “Bifurcated backbone strategy for rgb-d salient object detection,” TIP,              7479–7489.
     vol. 30, pp. 8727–8742, 2021.
[68] X. Shi, Z. Chen, H. Wang, D.-Y. Yeung, W.-k. Wong, and W.-c.
     Woo, “Convolutional lstm network: A machine learning approach for
     precipitation nowcasting,” in NIPS, 2015, pp. 802–810.
[69] T. Zhou, D.-P. Fan, G. Chen, Y. Zhou, and H. Fu, “Specificity-preserving
     rgb-d saliency detection,” CVMJ, 2022.
[70] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Sadat Saleh, T. Zhang, and
     N. Barnes, “Uc-net: Uncertainty inspired rgb-d saliency detection via
     conditional variational autoencoders,” in CVPR, 2020, pp. 8579–8588.
[71] X. Zhu, D. Cheng, Z. Zhang, S. Lin, and J. Dai, “An empirical study
     of spatial attention mechanisms in deep networks,” in ICCV, 2019, pp.
     6687–6696.
[72] Z. Liu, Y. Wang, Z. Tu, Y. Xiao, and B. Tang, “Tritransnet: Rgb-d salient
     object detection with a triplet transformer embedding network,” in ACM
     MM, 2021, pp. 4481–4490.
[73] X. Wang, R. Girshick, A. Gupta, and K. He, “Non-local neural networks,”
     in CVPR, 2018, pp. 7794–7803.
[74] S. Zheng, J. Lu, H. Zhao, X. Zhu, Z. Luo, Y. Wang, Y. Fu, J. Feng,
     T. Xiang, P. H. Torr, and L. Zhang, “Rethinking semantic segmentation
     from a sequence-to-sequence perspective with transformers,” in CVPR,
     2021.
[75] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network
     training by reducing internal covariate shift,” in ICML, 2015, pp. 448–456.
[76] K. He, X. Zhang, S. Ren, and J. Sun, “Identity mappings in deep residual
     networks,” in ECCV, 2016, pp. 630–645.
[77] R. Xiong, Y. Yang, D. He, K. Zheng, S. Zheng, C. Xing, H. Zhang,
     Y. Lan, L. Wang, and T. Liu, “On layer normalization in the transformer
     architecture,” in ICML, vol. 119, 13–18 Jul 2020, pp. 10 524–10 533.
[78] R. Ju, Y. Liu, T. Ren, L. Ge, and G. Wu, “Depth-aware salient object
     detection using anisotropic center-surround difference,” SPIC, vol. 38,
     pp. 115–126, 2015, recent Advances in Saliency Models, Applications
     and Evaluations.
[79] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency
     analysis,” in CVPR, 2012, pp. 454–461.
[80] W. Wang, J. Shen, M.-M. Cheng, and L. Shao, “An iterative and
     cooperative top-down and bottom-up inference network for salient object
     detection,” in CVPR, 2019, pp. 5968–5977.
[81] W. Ji, J. Li, S. Yu, M. Zhang, Y. Piao, S. Yao, Q. Bi, K. Ma, Y. Zheng,
     H. Lu, and L. Cheng, “Calibrated rgb-d salient object detection,” in
     CVPR, 2021, pp. 9466–9476.
[82] F. Wang, J. Pan, S. Xu, and J. Tang, “Learning discriminative cross-
     modality features for rgb-d saliency detection,” TIP, vol. 31, pp. 1285–
     1297, 2022.
[83] C. Zhu and G. Li, “A three-pathway psychobiological framework of
     salient object detection using stereoscopic technology,” in ICCVW, 2017,
     pp. 3008–3014.
[84] N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light field,”
     in CVPR, 2014, pp. 2806–2813.
[85] G. Wang, C. Li, Y. Ma, A. Zheng, J. Tang, and B. Luo, “Rgb-t saliency
     detection benchmark: Dataset, baselines, analysis and a novel approach,”
     in IGTA, 2018, pp. 359–369.
[86] Z. Tu, T. Xia, C. Li, X. Wang, Y. Ma, and J. Tang, “Rgb-t image saliency
     detection via collaborative graph learning,” TMM, vol. 22, no. 1, pp.
     160–173, 2020.
[87] Z. Tu, T. Xia, C. Li, Y. Lu, and J. Tang, “M3s-nir: Multi-modal multi-
     scale noise-insensitive ranking for rgb-t saliency detection,” in MIPR,
     2019, pp. 141–146.
[88] J. a. Carreira and A. Zisserman, “Quo vadis, action recognition? a new
     model and the kinetics dataset,” in CVPR, July 2017, pp. 4724–4733.
[89] K. Simonyan and A. Zisserman, “Very deep convolutional networks for
     large-scale image recognition,” arXiv preprint arXiv:1409.1556, 2014.
[90] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-measure:
     A new way to evaluate foreground maps,” in ICCV, 2017, pp. 4548–4557.
[91] F. Perazzi, P. Krähenbühl, Y. Pritch, and A. Hornung, “Saliency filters:
     Contrast based filtering for salient region detection,” in CVPR, 2012, pp.
     733–740.
[92] R. Achanta, S. Hemami, F. Estrada, and S. Süsstrunk, “Frequency-tuned
     salient region detection,” in CVPR, no. Conf, 2009, pp. 1597–1604.
