---
source_id: 050
bibtex_key: wu2023hidanet
title: HiDAnet: RGB-D Salient Object Detection via Hierarchical Depth Awareness
year: 2023
domain_theme: RGB-D SOD
verified_pdf: 50_HiDAnet.pdf
char_count: 103265
---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                    1

                                                HiDAnet: RGB-D Salient Object Detection via
                                                      Hierarchical Depth Awareness
                                                       Zongwei Wu, Guillaume Allibert, Fabrice Meriaudeau, Chao Ma, and Cédric Demonceaux

                                            Abstract—RGB-D saliency detection aims to fuse multi-modal
                                         cues to accurately localize salient regions. Existing works often
                                         adopt attention modules for feature modeling, with few methods
                                         explicitly leveraging fine-grained details to merge with semantic
arXiv:2301.07405v1 [cs.CV] 18 Jan 2023

                                         cues. Thus, despite the auxiliary depth information, it is still
                                         challenging for existing models to distinguish objects with similar
                                         appearances but at distinct camera distances. In this paper,                         (a) RGB           (b) Depth        (c) Threshold     (d) Local Region
                                         from a new perspective, we propose a novel Hierarchical Depth
                                         Awareness network (HiDAnet) for RGB-D saliency detection.
                                         Our motivation comes from the observation that the multi-
                                         granularity properties of geometric priors correlate well with
                                         the neural network hierarchies. To realize multi-modal and
                                         multi-level fusion, we first use a granularity-based attention
                                         scheme to strengthen the discriminatory power of RGB and
                                         depth features separately. Then we introduce a unified cross                       (e) DASNet          (f) SPNet           (g) Ours           (h) GT
                                         dual-attention module for multi-modal and multi-level fusion
                                         in a coarse-to-fine manner. The encoded multi-modal features                    Fig. 1. Motivation of our hierarchical depth awareness. (a) and (b) are the
                                         are gradually aggregated into a shared decoder. Further, we                     paired RGB-D inputs. (c) and (d) represent Multi-Otsu thresholding on depth
                                         exploit a multi-scale loss to take full advantage of the hierarchical           histogram and the generated Otsu regions, respectively. Our approach takes
                                         information. Extensive experiments on challenging benchmark                     full advantage of depth priors to improve the feature discriminatory power
                                                                                                                         and obtain the saliency mask (g). Compared to two state-of-the-art (SOTA)
                                         datasets demonstrate that our HiDAnet performs favorably over                   RGB-D models (e) and (f), our method favorably yields results (g) closer to
                                         the state-of-the-art methods by large margins.                                  the ground-truth mask (h).
                                           Index Terms—Depth-Aware               Channel      Attention,     RGB-D
                                         Saliency Detection
                                                                                                                         channels. A number of saliency detection works [9], [10], [12],
                                                                I. I NTRODUCTION                                         [21] adopt channel attention to enhance multi-modal features.
                                            Salient object detection (SOD) aims to find the most promi-                  However, the first step of learning channel attention is to
                                         nent region inside an image that visually attracts human atten-                 aggregate the spatial information of feature maps to construct
                                         tion. Conventional SOD approaches only take color images as                     a 1 × 1 × C vector by using global average pooling, where
                                         inputs. With deep learning models, RGB SOD has achieved                         C is the number of channels. As a result, the foreground
                                         significant success [1]–[5]. However, these models may result                   and background contribute equally to the output, which is
                                         in unsatisfactory performance when dealing with complex                         not optimal to distinguish salient objects. Considering these
                                         scenes, e.g., low-contrast light or object occlusion.                           issues, an intuitive motivation is to design local channel
                                            Recent advanced RGB-D sensors provide accessibility to                       attention referring to depth priors in order to improve feature
                                         depth maps at a low cost. The complementary geometric cues                      representation learning.
                                         can contribute to scene understanding. In the literature, two                      As shown in Fig. 1, while dealing with complex scenes,
                                         main designs have been widely exploited, i.e., single-streaming                 current state-of-the-art (SOTA) RGB-D models [13], [21] fail
                                         schemes that combine RGB-D images from the input side                           to extract the salient region due to similar visual appearance
                                         [6]–[8] and multi-streaming network that extracts multi-modal                   between the foreground and background (Fig. 1(f) and (g)).
                                         features separately and combines them at semantic levels [9]–                   However, we observe that salient regions often share similar
                                         [16]. Existing networks often directly extract semantic features                depth properties, i.e., a certain granularity of depth prior, that
                                         through the deep network, with few methods fully explore the                    help to distinguish the salient objects from the background
                                         rich geometric priors provided by the depth map.                                (Fig.1(b) and (d)). Inspired by this observation, we develop
                                            Previous works on channel attention [17]–[20] have shown                     a local feature enhancement scheme with granularity-based
                                         their effectiveness in emphasizing the attentive features among                 attention (GBA) to improve saliency detection. Specifically,
                                                                                                                         we propose to first generate various local regions according to
                                            Z. Wu, F. Meriaudeau, and C. Demonceaux are with ImViA, Université
                                         Bourgogne Franche-Comté, Dijon, France (e-mail: {zongwei wu@etu.; fab-         the granularity via Otsu thresholding [22], [23]. These regions
                                         rice.meriaudeau@; cedric.demonceaux@}u-bourgogne.fr )                           can be considered as distinct local spatial attention. Then for
                                            G. Allibert is with Université Côte d’Azur, CNRS, I3S, Nice, France (e-    each region, we apply local channel attention to improve the
                                         mail: allibert@i3s.unice.fr)
                                            Z. Wu and C. Ma are with MOE Key Lab of Artificial Intelligence, AI Insti-   feature discriminatory power. Fig. 1(c) and (d) illustrates such
                                         tute, Shanghai Jiao Tong University, Shanghai, China (chaoma@sjtu.edu.cn)       an example of the Otsu threshold values and granularity-aware
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                          2

masks, respectively. We show that our approach can better          [36], [40]–[42] propose a layer-wise attention to model the
reason about salient regions (Fig. 1(g)) that are closer to the    geometric contribution with respect to the network depth.
ground truth (Fig. 1(h)).                                          [41] explores an additional backbone to learn the weighting
   We further introduce a cross dual-attention module (CDA)        scalar purely from depth. [40] analyzes the similarity between
to learn channel and spatial attention from auxiliary modalities   RGB and depth features to regular the depth contribution.
to improve the current streaming. The enhanced features are        Sharing the same motivation, [36] computes the reliability of
hierarchically fused for final saliency map generation. Besides,   each modality at each stage and then merges them through
the same cross-interaction scheme is embedded to articulate        their reliability. Instead of learning the weighting scalar, [42]
features between encoders and decoders through a U-Net-            generates the weighting maps at each scale to calibrate the
like [24] architecture. We attentively mirror the multi-scale      feature response. Similarly, [43] leverages bilateral attention
encoder features to preserve valuable geometric priors within      to improve foreground-background features separately. Unlike
each decoder. The encoded features are gradually fused to          these works, we first divide the feature map into several local
a shared decoder. Finally, we use a multi-scale loss on top        regions with the help of depth granularity. The feature maps
of outputs from each decoder to optimize the saliency map.         are further calibrated with different local attention to improve
Concretely, our contributions are summarized as follows:           the feature discriminability. Compared to [42], [43], our fined-
   • We propose a novel granularity-based attention scheme         grained details are statically computed by maximizing the
     that attends to fine-grained details in order to strengthen   inter-class distance without learning parameters, leading to
     the feature discriminability of each modality.                more reasonable and stable locally-calibrated areas.
   • We design a new multi-modal and multi-level fusion               There exist other works which only extract features from
     scheme with a multi-scale loss to take full advantage of      RGB input while the depth map only serves as supervision
     the network hierarchy.                                        [21], [44], [45]. In this context, [46], [47] propose to leverage
   • We extensively validate our HiDAnet on large-scale chal-
                                                                   the pseudo-depth to guide the RGB learning. A2dele [44]
     lenging benchmarks. Our approach performs favorably           further formulates depth supervision as a knowledge transfer
     over SOTA models with large margins.                          problem. CoNet [45] and DASnet [21] propose a multi-task
                                                                   learning framework with an additional depth head together
                                                                   with the saliency branch. However, we argue that these meth-
                      II. R ELATED W ORK                           ods cannot fully leverage the multi-modal cues during feature
   There are extensive surveys [25]–[30] of salient object         extraction. Instead, we propose a cross-interaction scheme to
detection in the literature. In this section, we briefly review    take full advantage of cross-modal cues. We benefit from the
related RGB-D saliency detection as follows:                       auxiliary modality to alleviate errors in the feature modeling
Multi-Modal Fusion. The auxiliary depth map provides               (depth to RGB, and RGB to depth).
extra geometric clues in addition to visual appearance. To         Multi-Level Fusion. U-Net with skip connections [24] has
efficiently merge both modalities, several fusion methods have     shown its effectiveness in pixel-level segmentation tasks. Sev-
been proposed. A number of works [6]–[8], [31]–[33] directly       eral RGB-D SOD models [11], [13], [14], [48] equip this
concatenate the depth map with RGB images from the input           design for clearer boundary generation. [48] adopts the feature-
side through a single-stream network. On the one hand, JLDCF       wise addition. [13], [14] concatenate the encoder features with
and its successor [7], [31] explore the siamese design for         the decoder. [11] designs a dense connection between high-
saliency detection by concatenating RGB and depth images in        level features and the decoder. In this work, we exploit the
an additional dimension with a joint learning scheme. DANet        contribution of attention modules for skip connections applied
[6] forms a four-channel input and enhances the extracted          to SOD. It is worth mentioning the success of skip connections
features with a dual-attention mechanism learned from depth.       can be mainly attributed to aggregation between the semantic
[8], [32] propose the stochastic framework to analyze the          features provided by the contracting path and fine-grained
uncertainty during human labeling and model the distribution       features from the expansion path. From a new perspective, we
of the saliency output. Different from previous works, [33],       consider the encoder-decoder features as multi-modal features,
[34] attempt to address RGB-D SOD from the 3D point of             and a unified cross-fusion scheme is applied to boost the
view with a 3D convolutional neural network. The recent [35]       performance.
leverages the depth cues to mimicks multi-view images and          Attention for Feature Enhancement. Attention methods such
then fuse them to form the final output.                           as transformer [49], CBAM [17], SEnet [18], DA [50], and
   On the other side, multi-stream models [9]–[16], [36] have      ECA [20] have demonstrated their success in other vision
achieved leading performances in RGB-D SOD. These mod-             tasks. A number of RGB-D saliency models also equip at-
els adopt two parallel encoders on different modalities, and       tention modules to extract attentive features from different
the features are fused through different strategies. Several       modalities. VST [51] and TriTrans [14] adopt transformer [49]
works [9], [37], [38] firstly enhance the depth features before    for saliency detection. [21], [52], [53] apply the SE module
fusing with RGB features. It is worth noting that a portion        to compute modality-specific attention for feature calibration.
of the depth maps in existing saliency datasets are not of         Similarly, CDInet [11] designs a depth-induced channel atten-
satisfactory quality. As discussed in [7], [39]–[41], the depth    tion to enhance RGB features. From another perspective, [54]
may contain measurement or estimation bias. Thus, DCF [10]         deeply explores the spatial attention at different scales with
designs a calibration module to improve the depth quality.         the help of decoupled dynamic convolution. Sharing the same
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                     3

                                        Multi Granularities

                                                                                                                                         HiDANet
                                                                                                                                        GBA             CDA

 RGB                                                                                     𝒇𝟐             𝒇𝟏
                                                                            𝒇𝟑                                                          EMI             RFB
                                                                 𝒇𝟒
                                                                                                                                        Depth Awareness
               𝒇𝟏        𝒇𝟐        𝒇𝟑        𝒇𝟒

                                                                                                                         Loss           Encoder Fusion

                                                                                                                                        Decoder Fusion

                                                                                                                                        Skip Connection
 Depth
                                        Multi Granularities

Fig. 2. The overall architecture of our HiDAnet with U-Net-like design. It consists of granularity-based attention (GBA Section III-A), cross dual-attention
module (CDA Section III-B), and efficient multi-input fusion (EMI Section III-C). RFB is the receptive field block from [57] for accurate object detection.
White blocks denote the network backbone. Our granularity-based attention strengthens the discriminatory power of RGB and depth features separately. Our
cross dual-attention module takes advantage of cross-domain cues to attentively realize multi-modal and multi-level fusion in a coarse-to-fine manner. Our
efficient fusion scheme effectively models the shared information from each modality. The shared features are further improved with the skip connections for
final saliency map generation. Best viewed in color.

motivation, DFMnet [16] adopts a depth holistic attention                        and background. This module is naturally embedded into
on top of features with different resolutions. More recently,                    different levels of the encoder to correlate with the network
several works leverages both spatial and channel attention                       hierarchies. With the enhanced features, we propose a unified
to jointly improve the feature representation. For example,                      fusion mechanism (CDA) for multi-modal and multi-level
BBSnet [9] applies the CBAM [17] on the depth map to                             fusion. It enables a cross-domain interaction with both channel
improve the depth quality before fusion. [55] further improves                   and spatial attention to learn the informative shared features
the CBAM by highlighting spatial features. Sharing the same                      in a coarse-to-fine manner. These features are later gradually
motivation, CMINet [12] applies the DA [50] on to lately                         aggregated into the shared decoder through the efficient multi-
merge RGB-D features. Different from previous works with                         input fusion module (EMI). Lastly, we exploit a multi-level
bi-directional cross-modal attention, HAINet [56] explores the                   loss to take full advantage of the network hierarchies. Details
purified depth to improve the RGB features in turn.                              of each component are presented in the following sections.
   Despite the proven effectiveness, previous channel attention
schemes do not fully benefit from the geometric priors. For                      A. Feature Extraction with Granularity-Based Attention
example, the same attention can be applied to both fore-                            We observe that the multi-granularity properties of geo-
ground and background. The rich geometric priors in the                          metric priors correlate well with the network hierarchies of
input depth map have rarely been discovered, which limits                        saliency models. Inspired by this observation, we propose the
the performance of RGB-D saliency detection. DSA2F [15]                          granularity-based attention that aims to attentively combine the
introduces a depth-sensitive module with the help of the depth                   spatial attention mask with the conventional channel attention
histogram. However, it computes the depth region with a                          as shown in Fig. 3. For earlier layers, it strengthens the low-
fixed threshold for each input image and the attention scores                    level representations to precisely localize the salient object
are simply computed by a Conv1×1 . In contrast, we propose                       with a sharp boundary. For deeper layers, it improves the
to dynamically generate multi-granularity regions with the                       semantic abstraction and contributes to the identification of
multi-Otsu method [22], [23]. The fine-grained details are                       salient objects regardless of appearance variations.
further integrated with channel attention to enhance the feature                    Given the depth map D with its histogram H, we dy-
discriminability for sharper edge generation.                                    namically generate the fine-grained details. According to
                                                                                 the value/distance within the depth map, we use the Otsu
                              III. M ETHOD                                       algorithm [22] to discretize the histogram H into several
                                                                                 different regions. In this work, we use the extended multi-
  Fig. 2 presents the overall framework of our proposed
                                                                                 Otsu [23] to generate multiple thresholds. Assuming T random
HiDAnet. Note that the Otsu masks are generated from the
                                                                                 thresholds (d1 , d2 , ..., dT ) dividing the depth into T + 1 parts.
depth map during the pre-processing. Firstly, RGB and depth
                                                                                 Let (σi2 , wi ) be the variance and the pixels number of region i
maps are fed into two parallel encoders for feature extraction.
                                                                                 (1 ≤ i ≤ T + 1). The optimal values {d1∗ , d2∗ , ..., dT∗ } are chosen
For each individual encoder (RGB/Depth), we propose a
                                                                                 by maximizing the inter-class variance:
granularity-based module (GBA) with the help of input Otsu
masks to enhance the discriminatory power, e.g., foreground                               {d1∗ , d2∗ , ..., dT∗ } = argmax{σw2 (d1 , d2 , ..., dT )},     (1)
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                  4

            Otsu
 h                                             L-ECA
                𝑚&                                                  𝑓#$%                            L-ECA: Local Efficient Channel Attention
      w
                                              L-ECA
                𝑚'                                             h
                                                                    w      c
            …

                                                                                              L-AP                      ECA
                                              L-ECA
      𝑓!"       𝑚"

 h                                                             Multiplication      Addition   L-AP Local Average Pooling ECA Efficient Channel Attetnion

      w     c

Fig. 3. Diagram of the granularity-based attention. The depth awareness is encoded via Local Efficient Channel Attention (L-ECA). ECA is from [20].

                                      𝑇2     𝑇1                                          𝑇1
                                                                                               𝑇2    𝑇3
                                       𝑇3

     (1) RGB           (2) Depth       (3) DSA2F Thresholds, Regions, and Result               (4) Our Thresholds, Regions, and Result         (5) GT

Fig. 4. Visual comparison with concurrent DSA2F [15]. Our method maximizes the inter-class variance, leading to more accurate masks compared to DSA2F.
We further explore the granularity cues via channel attention, yielding results closer to the ground truth (5).

                 +1
where σw2 = ∑Ti=1   wi σi2 . To reduce the computational cost, we               the depth prior. Moreover, since the Otsu algorithm optimizes
only generate the Otsu regions once during pre-processing and                   the thresholds by maximizing inter-class variance, our gener-
further resize them to fit the resolution of feature maps from                  ated masks are more robust to the depth noise compared to
different scales.                                                               the concurrent work. Additionally, we leverage the granularity
   For the ith region mi , (1 ≤ i ≤ T + 1, i ∈ N∗ ), we mask                    with channel attention, while DSA2F simply uses a Conv1×1
out the feature map fin with element-wise multiplication to                     for local awareness. As shown in Fig. 4, by integrating the fine-
suppress the inactive area through fin ⊗ mi . Then, the channel                 grained details into the channel attention, we can reason about
attention is applied to improve the feature representation with                 more accurate saliency regions closer to the ground truth. The
local awareness. Compared to the vanilla channel attention                      quantitative comparison with [15], [45], [58] can be found in
[18], [20], we replace the global average pooling with the                      Section IV-C Tab. I. Our superior performance proves that we
local average pooling that attends to the local details referring               can better model the depth priors.
to geometric priors. Finally, the locally enhanced features
are aggregated by a residual connection for the final output                    B. Encoder Fusion with Cross Dual-Attention Module
generation fout . The overall process can be formulated as:                        Previous studies [21], [39], [44] have affirmed the effec-
            L − ECA(x) = σ (Conv1d (L − AP(x))) ⊗ x,                            tiveness of learning from two heterogeneous modalities for
                      T +1                                                      RGB-D SOD. Color images provide rich information in visual
                                                                        (2)
                fout = ∑ L − ECA( fin ⊗ mi ) + fin ,                            appearance while depth maps contain more spatial priors. Both
                      i=1                                                       modalities contribute to modulating homogeneous semantic
where σ (·) is the Sigmoid activation, ⊗ is the element-wise                    information. Therefore, the objective of multi-modal learning
multiplication, and L − AP denotes the local average pooling                    is to efficiently fuse features with diverse information from dif-
on each masked region. We provide more details on the                           ferent modalities. Similar to multi-modal features, multi-level
differences between the proposed granularity-based attention                    features also contain both heterogeneous and homogeneous
and traditional channel attention in the ablation study Section                 information: high-level features are richer in abstract semantic
V Tab. V.                                                                       cues while low-level features are richer in fine-grained details.
Remarks. Several previous works have proposed to explore                        Thus, from a new perspective, we design a unified fusion
depth prior in various manners such as the contrast in CPFP                     scheme to make full use of cross-domain cues for both multi-
[58], the edge in CoNet [45], or the histogram in DSA2F                         modal and multi-level reasoning.
[15]. Our approach resembles the DSA2F that both methods                           Assuming two paired multi-modal features fx and fy . We
belong to threshold-based segmentation frameworks. However,                     firstly build a transformation Ft to map the inputs fx , fy ∈
                                                                                                                       0
one main difference is that we dynamically generate optimized                   RC×h×w to feature maps fx0 , fy0 ∈ RC ×h×w with C0 = C2 . Specifi-
masks with the Ostu algorithm, while DSA2F applies fixed                        cally, Ft is the combination of a 1×1 convolution which halves
thresholds on the T + 1 largest depth distribution modes that                   the channel size and a 3 × 3 convolution which is expected to
cannot adapt to different scenarios without handcraft adjusting.                activate the edge response:
Fig. 4 illustrates the difference in the thresholds and regions.
We observe that our approach computes more discriminative                                       fx0 = Ft ( fx ) = Conv3×3 (Conv1×1 ( fx )),
                                                                                                                                                        (3)
regions, yielding a more effective and robust manner to explore                                 fy0 = Ft ( fy ) = Conv3×3 (Conv1×1 ( fy )).
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                           5

                                                                Multiplication                                          Addition         Multiplication
              SA                                           C Concatenation              𝑓!

              CA

                                                                                                               Conv
        𝑓′!                                                                                          C                       G-ECA
                                                                                        𝑓(

                                                         Conv
                                               C                                                                                                          𝑓#"$%&'
              CA                                                                        𝑓"
        𝑓′"                                                            𝑓′#$%

              SA
                                                                                                               Gloabl Average Pooling
                                                                                                      G-AP                   ECA

Fig. 5. The proposed multi-scale multi-level encoder fusion scheme with
cross-domain supervision. Best viewed in color.
                                                                                     Fig. 6. The proposed efficient decoder fusion scheme for multi-type
                                                                                     inputs. By fully exploiting the channel-wise dependencies, input features are
                                                                                     attentively aggregated to generate the shared output. Best viewed in color.
   Once obtaining the lightweight representation, the next step
is to aggregate features from different domains (RGB-D or
encoder-decoder). We observe from Fig. 1 that the fine-grained                       features, while [10], [21] only focus on channels; (B) Different
details, such as relative boundary, facilitate the identification                    from ASTA [59], our calibration is bi-directional (RGB to
of salient objects. Simultaneously, in case it is difficult to                       depth and depth to RGB), while ASTA is asymmetric which
distinguish objects at the same distance on the depth map,                           only leverages depth cues to improve RGB features. Hence, it
e.g., when distinguishing the motorbike from the street, the                         does not tackle depth noise; (C) SPNet [13] also adopts the
visual appearance becomes more reliable. Inspired by this                            symmetric fusion strategies. Our work differs from SPNet in
observation, we aim to use heterogeneous clues to compensate                         that we fully explore the attention modules for feature fusion,
for the single-domain streaming.                                                     while SPNet is built upon simple convolutions to combine
   To this end, we propose a cross dual-attention fusion scheme                      features; (D) The fusion scheme can also be implemented by
as shown in Fig. 5. Specifically, from each input feature map,                       the CBAM [17]. However, vanilla CBAM is modality-specific
                                              0
we learn the 1-D channel attention Mc ∈ RC ×1×1 to determine                         and cannot explore its relevance in cross-domain features. The
what information to be involved, and the 2-D spatial attention                       ablation study in Section V-C Tab. IX shows the gain with the
Ms ∈ R1×h×w to determine which part to focus. We formally                            cross interaction.
have the operations:
    Mc ( f 0 ) = σ (MLP(GAP( f 0 )) + MLP(GMP( f 0 ))),                              C. Decoder Aggregation with Efficient Multi-Input Fusion
         0                                          0              0           (4)   Module
    Ms ( f ) = σ (Conv7×7 (Concat(CAP( f ),CMP( f )))),
                                                                                        To aggregate the learned features from both RGB and
where σ (·) is the Sigmoid activation, MLP is the multi-layer                        depth decoders into the shared decoder, a simple concatenation
perceptron, GAP and GMP are the global average and max                               may not be adaptive enough due to the tripled number of
pooling, respectively, and CAP and CMP are the average                               descriptors. Thus, we propose an efficient multi-input fusion
and max pooling across the channel, respectively. With the                           strategy. Specifically, as shown in Fig. 6, after the simple
learned dual attention from separate feature maps, we enable                         concatenation between different inputs (RGB fR , depth fD ,
a cross-domain interaction. In such a way, we can alleviate the                      and previous-level shared features fh ), we adopt the vanilla
ambiguities in the domain-specific features. Finally, the cross-                     ECA [20] module (termed G-ECA with global pooling) to
enhanced features are fed into concatenation and convolution                         explore the inter-dependencies of different features. Thus, the
                                   0 . The overall process can
to form the shared representation fout                                               most responded features are adaptively selected to form the
be formulated as:                                                                    shared decoder. A residual addition is adapted to reinforce the
               fxenh = Ms ( fy0 ) ⊗ Mc ( fy0 ) ⊗ fx0 ,                               contribution of the previous level features. We have the overall
               fyenh = Ms ( fx0 ) ⊗ Mc ( fx0 ) ⊗ fy0 ,                         (5)   process:
                0
               fout = Conv3×3 (Concat( fxenh , fyenh )),                                fshared = G − ECA(Conv3×3 (Concat( fR , fD , fh ))) + fh .             (6)
where ⊗ denotes element-wise multiplication. For the shared                            The shared decoded features are then fed into our cross
encoder, starting from the second layer, once the multi-modal                        dual-attention scheme to realize the skip-connection between
features are fused through cross attention, the output is further                    the shared encoder-decoder.
combined with the previous level output through a Conv3×3 .                          Remarks. Our encoder fusion (CDA) and decoder fusion
Remarks. Our fusion design differs from concurrent works                             (EMI) are technically different. We observe that the spatial
[10], [13], [21], [59] in several aspects: (A) We leverage                           cues are gradually lost during encoding and become limited for
both spatial and channel attention to aggregate multi-modal                          decoders. This motivates us to apply both spatial and channel
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                   6

attention for the encoder fusion, while only using channel
attention for the decoder fusion.

                                                                       Max F-Measure ↑
D. Optimization
   To take full advantage of the hierarchical information,
we supervise multi-level outputs for both RGB, depth, and
shared/fused branches. For outputs from each level, the pre-
dicted map is upsampled to form the same resolution mask
as the ground truth. We adopt BCE loss LBCE for pixel
restriction and IoU loss LIoU for global restriction [21], [60],
[61]. Therefore, we have the loss Li for the ith level output:

                          Li = LBCE
                                i   + LIoU
                                       i .                   (7)                                       MAE ↓
   In total, we have five-level outputs (after each RFB in Fig.
2). Thus, by combining the loss from each branch (R for RGB,       Fig. 7. Average Max F-Measure, MAE, and Model Size of different
D for depth, and S for shared branches), the overall multi-level   methods on benchmark datasets. The circle size denotes the model size. Note
                                                                   that better models are shown in the upper left corner (i.e., with a larger
loss function Lml becomes:                                         F-measure and smaller MAE). Methods with smaller size perform inferior,
                                                                   making our method both efficient and accurate.
                      5
             Lml = ∑ λi (Li (R) + Li (D) + Li (S)),          (8)
                     i=1
                                                                   B. Experimental Settings
where λi is the weight of the different-level loss. To correlate      Our model is implemented based on Pytorch and trained
with the network hierarchies, we follow [21], [62] and set the     with a V100 GPU. Our backbone is initialized with the pre-
weight λ as {1, 0.8, 0.6, 0.4, 0.2}.                               trained weights obtained from ImageNet. For the depth stream,
   We expect the multi-level loss to measure the difference        we modify the first convolution to start from one channel. The
between the generated mask and ground truth at various layers,     input RGB-D resolution is fixed to 352×352. We choose the
and to force the network to learn hierarchical features that       Adam algorithm as our optimizer. We initialize the learning
capture long- and short-range spatial relationships between        rate to be 1e−4 which is further divided by 10 every 60
pixels. The gain by adopting the multi-level loss can be found     epochs. The total training time takes around 6 hours for 100
in the ablation study Section V Tab. VIII.                         epochs. During training, we adopt random flipping, rotating,
                                                                   and border clipping for data augmentation. During inference,
                                                                   the prediction maps from the shared branch are the final
                          IV. E XPERIMENTS
                                                                   outputs (middle branch of Fig. 2).
A. Benchmark Datasets                                                 We evaluate our performance with four generally-
                                                                   recognized metrics: F-measure is a region-based similarity
   To verify the effectiveness of our approach, we firstly
                                                                   metric that takes into account both Precision (P) and Recall
train with the conventional training dataset following the                                                         2 )·P·R

protocol presented in [9], [10], [13], [14], [21] with 2,195       (R). Mathematically, we have : Fβ = (1+β   β 2 ·P+R
                                                                                                                           . The value of
                                                                     2
                                                                   β is set to be 0.3 as suggested in [77] to emphasize the
samples: 1,485 samples from the NJU2K-train [63] and 700
samples from the NLPR-train [64]. For testing, experiments         precision. In this paper, we report the maximum F-measure
are conducted on five classical benchmark RGB-D datasets.          (Fβ ) score across the binary maps of different thresholds.
DES [65] : includes 135 images of indoor scenes captured           Mean Absolute Error (M) measures the approximation de-
by a Kinect camera. NLPR-test [64]: contains 300 natural           gree between the saliency map and ground-truth map at the
images captured by a Kinect under different illumination           pixel level. S-measure (Sm ) [78] evaluates the similarities be-
conditions. NJU2K-test [63]: contains 500 stereo image pairs       tween object-aware (So ) and region-aware (Sr ) structures of the
from different sources such as the Internet, 3D movies, and        saliency map compared to the ground truth. Mathematically,
photographs taken by a Fuji W3 stereo camera, where several        we have: Sm = α · So + (1 − α) · Sr , where α is set to be
depth maps are estimated through an optical flow method [66].      0.5. E-measure (Em ) evaluates both image-level statistics and
STERE [67]: includes 1,000 stereoscopic images downloaded          local pixel-matching information. Mathematically, we have:
                                                                            1
from the Internet where the depth map is estimated using the       Em = W ×H    ∑W     H
                                                                                 i=1 ∑ j=1 φFM (i, j), where φFM (i, j) stands for the
SIFT flow method [68]. SIP [39]: contains 929 images with          enhanced-alignment matrix as presented in [79]. To make a
humans in the scene, and images are acquired by a mobile           fair comparison, we use the same protocol as [13] to evaluate
device. We further evaluate our model on a newly published         the officially released saliency maps for each SOTA method.
dataset COME15K [12] where the depth is estimated through
a modified optical flow algorithm [69]. In this case, our model    C. Comparison with SOTA RGB-D models
is trained with provided 8,025 training samples and tested on      Quantitative Comparison: We provide in Figure 7 an
the “Difficult” set with 3,000 images.                             overview of the average performance on conventional bench-
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                           7

                                                                TABLE I
 Q UANTITATIVE COMPARISON WITH SOTA MODELS . ↑ (↓) DENOTES THAT THE HIGHER ( LOWER ) IS BETTER . W E USE THE M EAN A BSOLUTE E RROR
              (M), MAX F- MEASURE (Fm ), S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST.)

 Dataset           Size            DES                    NLPR                       NJU2K                           STERE                         SIP
 Metric            Mb   M ↓ Fβ ↑ Sm ↑ Em ↑ M ↓         Fβ ↑ Sm ↑     Em ↑   M↓     Fβ ↑ Sm ↑       Em ↑   M↓       Fβ ↑ Sm ↑     Em ↑   M↓     Fβ ↑ Sm ↑     Em ↑
 Performance of RGB-D Models with VGG Backbones
 DMRA19 [70]       278  .030 .907 .900 .934 .031       .888   .899   .940   .051   .896   .886     .920   .047     .895   .886   .930   .086   .852   .806   .847
 A2dele20 [44]     116  .029 .897 .886 .917 .029       .895   .899   .943   .051   .890   .871     .914   .044     .892   .879   .926   .070   .856   .829   .887
 AT SA20 [59]      131  .022 .931 .917 .954 .027       .907   .909   .947   .046   .905   .885     .928   .038     .912   .896   .940   .063   .884   .849   .895
 CMMS20 [71]       546  .018 .934 .934 .958 .028       .914   .919   .946   .044   .905   .900     .929   .045     .899   .894   .925   .058   .893   .872   .901
 DANet20 [6]       128  .029 .916 .904 .932 .047       .904   .897   .926   .045   .910   .899     .927   .048     .895   .892   .919   .054   .900   .888   .912
 CMW Net20 [72]    327  .022 .939 .934 .959 .029       .913   .917   .941   .046   .913   .903     .925   .043     .911   .905   .930   .062   .889   .867   .901
 HDFNet20 [48]     308  .021 .932 .926 .962 .023       .926   .923   .957   .039   .922   .908     .939   .042     .910   .900   .933   .048   .909   .886   .924
 PGAR20 [73]       62   .032 .894 .886 .906 .027       .912   .917   .941   .042   .918   .909     .932   .045     .902   .894   .919   .072   .852   .838   .875
 SSF20 [74]        126  .026 .912 .904 .930 .027       .912   .915   .947   .043   .911   .899     .929   .065     .859   .837   .882   .091   .810   .799   .855
 CASGNN20 [75]     160  .027 .917 .893 .926 .025       .914   .919   .953   .036   .927   .910     .944   .038     .913   .899   .940   -      -      -      -
 D3Net21 [39]      518  .031 .909 .897 .923 .030       .907   .912   .942   .049   .910   .900     .928   .039     .911   .902   .940   .063   .886   .866   .897
 CDINet21 [11]     217  .020 .943 .937 .962 .024       .923   .927   .953   .030   .928   .918     .945   .040     .912   .913   .937   .054   .904   .875   .908
 UCNet21 [32]      120  .018 .936 .934 .970 .025       .915   .920   .953   .043   .908   .897     .932   .039     .908   .902   .938   .051   .896   .875   .915
 DRLF21 [76]       351  .030 .909 .895 .918 .032       .904   .903   .929   .055   .896   .886     .914   .050     .897   .888   .916   .071   .869   .850   .882
 HAINet21 [56]     228  .018 .945 .935 .967 .024       .920   .924   .956   .037   .924   .911     .940   .040     .917   .907   .938   .052   .907   .879   .917
 BIANet21 [43]     189  .020 .939 .931 .955 .025       .921   .925   .954   .039   .928   .915     .939   .043     .910   .903   .932   .052   .904   .883   .916
 DCMF22 [53]       78   .022 .934 .932 .956 .029       .913   .922   .940   .041   .911   .902     .935   .043     .916   .910   .928   -      -      -      -
 Ours (VGG16)      269  .017 .944 .929 .968 .021       .927   .928   .962   .034   .930   .918     .947   .039     .915   .902   .939   .045   .909   .889   .927
 Performance of RGB-D Models with ResNet Backbones
 JLDCF21 [31]      548  .020 .934 .931 .961 .022       .925   .925   .955   .041   .912   .902     .936   .040     .913   .903   .934   .049   .903   .880   .918
 RD3D21 [34]       179  .019 .941 .935 .965 .022       .927   .930   .959   .036   .923   .916     .941   .037     .917   .911   .939   .048   .906   .885   .918
 BIANet21 [43]     244  .020 .939 .930 .958 .023       .924   .926   .956   .036   .929   .917     .942   .039     .912   .905   .935   .047   .904   .887   .920
 CoNet20 [45]      162  .024 .920 .914 .944 .027       .903   .911   .943   .046   .902   .896     .926   .037     .909   .905   .941   .058   .887   .860   .911
 DASNet20 [21]     141  .024 .926 .905 .932 .021       .929   .929   .960   .042   .911   .902     .935   .037     .915   .910   .939   .051   .900   .877   .918
 BBSNet21 [38]     200  .021 .942 .934 .955 .023       .927   .930   .953   .035   .931   .920     .941   .041     .919   .908   .931   .055   .902   .879   .910
 DCF21 [10]        435  .024 .910 .905 .941 .022       .918   .924   .958   .036   .922   .912     .946   .039     .911   .902   .940   .052   .899   .876   .916
 DSA2F21 [15]      -    .021 .896 .920 .962 .024       .897   .918   .950   .039   .901   .903     .923   .036     .898   .904   .933   -      -      -      -
 DSNet21 [55]      661  .021 .939 .928 .956 .024       .925   .926   .951   .034   .929   .921     .946   .036     .922   .914   .941   .052   .899   .876   .910
 UTANet21 [52]     186  .026 .921 .900 .932 .020       .928   .932   .964   .037   .915   .902     .945   .033     .921   .910   .948   .048   .897   .873   .925
 C2DFNet22 [54]    198  .020 .937 .922 .948 .021       .926   .928   .956   -      -      -        -      .038     .911   .902   .938   .053   .894   .782   .911
 MV SalNet22 [35]  -    .019 .942 .937 .973 .022       .931   .930   .960   .036   .923   .912     .944   .036     .921   .913   .944   -      -      -      -
 SPSN22 [36]       149  .017 .942 .937 .973 .023       .917   .923   .956   .032   .927   .918     .949   .035     .909   .906   .941   .043   .910   .891   .932
 Ours (ResNet50)   523  .015 .947 .939 .973 .022       .927   .925   .957   .030   .937   .924     .952   .033     .926   .914   .948   .043   .915   .893   .930
 Performance of RGB-D Models with Res2Net Backbones
 BIANet21 [43]     244  .017 .948 .942 .972 .022       .926   .928   .957   .034   .932   .923     .945   .038     .916   .908   .935   .046   .908   .889   .922
 SPNet21 [13]      702  .014 .950 .945 .980 .021       .925   .927   .959   .028   .935   .925     .954   .037     .915   .907   .944   .043   .916   .894   .930
 Ours (Res2Net50) 525   .013 .952 .946 .980 .021       .929   .930   .961   .029   .939   .926     .954   .035     .921   .911   .946   .043   .919   .892   .927

                                                                TABLE II
     Q UANTITATIVE COMPARISON ON THE CHALLENGING COME15K Difficult TEST SET [12]. W E USE THE M EAN A BSOLUTE E RROR (M), MAX
                   F- MEASURE (Fm ), S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST.)

                    JLDCF            A2dele           DMRA             CoNet              BBSnet                 SPnet           CMINet               Ours
       M↓            .075             .092             .137             .113               .071                   .065            .064                .062
       Em ↑          .870             .838             .775             .813               .876                   .888            .893                .893

mark datasets, i.e., DES [65], NLPR [64], NJU2K [63],                       size with 269 MB and around 6 FPS. Our HiDAnet with
STERE [67], and SIP [39]. The detailed quantitative perfor-                 ResNet50 backbones further sets new SOTA records on DES,
mances can be found in Tab. I. We also present in Tab. II                   NLPR, and NJU2K datasets with 523 MB and around 12 FPS.
the quantitative comparison on the newly published challeng-                We also follow the SOTA SPNet and replace our backbone
ing COME15K [12] dataset. All saliency maps are directly                    with Res2Net50. It can be seen that our method performs
provided by authors or computed by authorized codes.                        favorably compared to SPNet with only 525 MB compared to
                                                                            that of SPNet with 702 MB. Our FPS is around 11. We also
   Under the consideration of a fair comparison, we conduct                 exhibit in Fig. 9 the PR curves with several latest published
experiments with different backbones such as VGG16 [80],                    models to further demonstrate the superior performance of our
ResNet50 [19], and Res2Net50 [81]. It can be seen that                      model.
our HiDAnet with each backbone achieves comparable and
superior performance compared to the SOTA models with                          Finally, in addition to the difference in the backbone,
the same backbone. Specifically, our HiDANet with VGG16                     we observe that existing works adopt different architectures,
backbones achieves significantly better performance on NLPR                 i.e., design of decoder, supervision, training settings, etc.
and SIP datasets, while being very competitive on the model                 Under the consideration of fair comparison and to purely
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                     8

   RGB         Depth           JLDCF         BBSnet         DASnet         DCFnet   DFMnet      TriTrans     SPnet       Ours         GT

    RGB         Depth           JLDCF        BBSNet         DASNet         DCFNet   DFMNet       TriTrans    SPNet        Ours       GT
Fig. 8. Visual comparison between our HiDAnet and SOTA methods in various challenging cases. It can be seen that our method better explores the
granularity prior to reason about the saliency map closer to the ground truth.

                             TABLE III                                         truth masks. For the motorbike in the 1st row, our model
  Q UANTITATIVE COMPARISON WITH DIFFERENT FUSION DESIGNS . W E                 can selectively remove the background region (board). For the
REPLACE OUR FUSION MODULE WITH FOUR SOTA FUSION MODULES AND
RETRAIN THE NEW NETWORKS UNDER THE SAME TRAINING SETTING . W E                 sculpture in the 2nd row, our network pays local attention to
     USE THE M EAN A BSOLUTE E RROR (M), MAX F- MEASURE (Fm ),                 the foreground and thus the hollow part can be detailed. We
S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION METRICS .             can also accurately extract the human with large deformations
                          (B OLD : BEST.)
                                                                               (3rd − 5th rows).
                                                                               Robustness against Depth Noise: Tab. IV reports the robust-
 Dataset                Size     NLPR        NJU2K       STERE         SIP
                                                                               ness analysis on the depth quality. To make a fair comparison,
 Metric                 Mb     Fβ ↑ Em ↑   Fβ ↑ Em ↑   Fβ ↑ Em ↑   Fβ ↑ Em ↑
 Res2Net50 + Ours       525    .929 .961   .939 .954   .921 .946   .919 .927   we conduct experiments and compare with the SOTA SPnet
 Res2Net50 + BBS [9]    509    .922 .953   .918 .939   .890 .909   .916 .917   [13] and CMINet [12] under the same inferior condition with
 Res2Net50 + CDI [11]   531    .926 .958   .927 .946   .922 .945   .907 .920   a simulated Gaussian noise on depth. We further evaluate
 Res2Net50 + DCF [10]   347    .927 .958   .933 .948   .916 .939   .911 .923
 Res2Net50 + SP [13]    737    .925 .959   .935 .954   .915 .944   .916 .930   the performances on the simulated noisy testing dataset. The
                                                                               noise level is defined by the conventional metrics RMSE and
                                                                               δ 1. While RMSE and δ 1 are 0, we report the performance
                                                                               tested with the vanilla dataset (without noise). Drop ∆ denotes
analyze the effectiveness of encoder fusion design, we re-                     the performance degradation by % under the simulated depth
implement several fusion alternatives under the same architec-                 noise.
ture (Res2Net50 + fusion). Specifically, we choose the same                       Note that CMINet designs a multi-scale mutual information
backbone (Res2Net50), the same decoder (the SOTA [13]),                        minimization during the encoding stage and lately merge
loss (multi-scale supervision), and the same training settings                 multi-modal features at the semantic level, yielding an un-
as ours. The only difference between one model to another is in                satisfactory performance while dealing with noisy datasets
the fusion module. The quantitative comparison can be found                    (drop 2.0% Sm and 2.3% Em for noisy DES). Differently, both
in Table III. It can be seen that by replacing our fusion with                 SPnet and ours fuse features at each stage, leading to superior
other methods, the empirical results significantly drop. This                  robustness against the noise. Compared to SPnet, it can be seen
validates the superior effectiveness of our granularity and CDA                that our performance is more stable, which can be attributed
in leveraging RGB-D cues compared to other alternatives.                       to our granularity attention and fusion designs. The gain of
                                                                               each component can be found in Tab. VIII.
Qualitative Comparison: Fig. 8 illustrates generated saliency
maps of different methods on challenging cases: cluttered
                                                                                                   V. A BLATION S TUDY
background and foreground with a similar appearance (1st −
2nd rows), human in the scene (3rd − 5th rows), and low                        A. Comparison with Vanilla Channel Attention
contrast on the depth map (6th − 7th rows). Compared to the                      We propose granularity-based attention (GBA) referring to
SOTA models, our HiDAnet yields results closer to the ground-                  geometric priors, which differs from the traditional channel
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                                  9

Fig. 9. Comparison on PR curves. Our HiDANet achieves better performance compared to the 12 listed SOTA methods across different datasets.

                                                              TABLE IV
 E XPERIMENTS UNDER INFERIOR CONDITIONS WITH SIMULATED DEPTH NOISES (RMSE, δ 1). W HILE RMSE, δ 1 ARE 0, IT REPRESENTS THE RESULT
      WITHOUT SIMULATED NOISES . D ROP ∆ DENOTES THE ABSOLUTE PERFORMANCE DIFFERENCE . O UR H I DA NET LEADS TO A MORE STABLE
PERFORMANCE COMPARED TO THE SOTA METHODS WITH A LOWER ∆ UNDER DIFFERENT INFERIOR CONDITIONS , PROVING THAT OUR MODEL IS MORE
ROBUST AGAINST DEPTH NOISES . W E USE THE M EAN A BSOLUTE E RROR (M), MAX F- MEASURE (Fm ), S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS
                                                  EVALUATION METRICS . (B OLD : BEST.)

 Dataset                             DES                                                NLPR                                            NJU2K
  Metric     RMSE       δ1      M↓       Fβ ↑   Sm ↑    Em ↑    RMSE         δ1      M↓     Fβ ↑    Sm ↑   Em ↑   RMSE        δ1     M↓      Fβ ↑   Sm ↑     Em ↑
CMINet21        0        0      .016     .944   .940    .975       0          0      .020   .931    .932   .959      0         0     .028    .940   .929     .954
CMINet21      .261     .270     .022     .925   .920    .952     .259       .342     .021   .929    .932   .960    .236      .413    .032    .934   .922     .948
Drop ∆(%)       -        -        .6      1.9    2.0     2.3       -          -        .1    0.2      0      .1      -         -      0.4     0.6    .7        .6
 SPNet21        0        0      .014     .950   .945    .980       0          0      .021   .925    .927   .959      0         0     .028    .935   .925     .954
 SPNet21      .261     .270     .017     .944   .935    .972     .259       .342     .020   .922    .924   .956    .236      .413    .033    .931   .920     .946
Drop ∆(%)       -        -        .3       .6     1       .8       -          -        .1     .3     .3      .3      -         -       .5      .4    .5       .8
   Ours         0        0      .013     .952   .946    .980       0          0      .021   .929    .930   .961      0         0     .029    .939   .926     .954
   Ours       .261     .270     .015     .948   .943    .980     .259       .342     .021   .930    .930   .962    .236      .413    .029    .935   .925     .953
Drop ∆(%)       -        -        .2       .4    .3       0        -          -        0      .1      0      .1      -         -       0       .4     .1       .1

                                                                  TABLE V
      A BLATION STUDY ON ATTENTION DESIGNS WITH DIFFERENT AVERAGE POOLING METHODS . W E USE THE M EAN A BSOLUTE E RROR (M), MAX
                     F- MEASURE (Fm ), S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST.)

                                                                      DES                           NLPR                     NJU2K                         STERE
#                         Description
                                                               M↓             Fβ ↑           M↓            Fβ ↑       M↓              Fβ ↑          M↓              Fβ ↑
 I          Vanilla Global Attention + Global Pooling          .019           .940           .020          .929       .030            .936          .037            .918
 II             Local Attention + Global Pooling               .015           .947           .021          .927       .032            .928          .038            .915
III           Our Local Attention + Local Pooling              .013           .952           .021          .929       .029            .939          .035            .921

attention on the pooling strategies. Formally, let z ∈ RC be the                        where (I) denotes the vanilla global average pooling, (II) is the
squeezed spatial information from feature x ∈ RH×W ×C . Ac-                             global pooling with local region mi (.), and (III) is our proposed
cordingly, we can obtain three variations of average pooling:                           GBA module that applies local pooling with local region mi (.).
                                                                                        Note that when depth data is constant, i.e., all the pixels
                                                                                        belong to the same granularity, our local average becomes
                                ∑ ∑ x(.)                                                the global average pooling and our model is equivalent to
                        (I) z =          ;
                                 H ×W                                                   the conventional channel attention [18], [20]. To verify our
                                 ∑ ∑ x(.) · mi ()                                       effectiveness, we conduct experiments by replacing our local
                        (II) z =                  ;                            (9)
                                    H ×W                                                pooling with the aforementioned poolings. Empirical results in
                                  ∑ ∑ x(.) · mi (.)                                     Tab. V show that compared to (I), (II) can better leverage local
                        (III) z =
                                    ∑ ∑ mi (.)
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                         10

                                                           TABLE VI
  E XPERIMENTS BY GRADUALLY ADDING GRANULARITY ATTENTION MODULE ON RGB AND D EPTH STREAMS . RGB(G)/D(G) DENOTES THE CASE
     WHEN GRANULARITY ATTENTION IS APPLIED TO RGB/D EPTH BRANCH . W E USE THE M EAN A BSOLUTE E RROR (M), MAX F- MEASURE (Fm ),
                         S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST.)

 Dataset                           DES                         NLPR                          NJU2K                     STERE                         SIP
 Metric                 M↓     Fβ ↑ Sm ↑     Em ↑    M↓     Fβ ↑ Sm ↑    Em ↑      M↓     Fβ ↑ Sm ↑   Em ↑   M↓     Fβ ↑ Sm ↑   Em ↑   M↓     Fβ ↑      Sm ↑   Em ↑
 (A) RGB + D            .015   .949 .940     .972    .022   .925 .927    .960      .030   .932 .923   .952   .037   .913 .901   .936   .046   .914      .889   .923
 (B) RGB(G) + D         .014   .951 .943     .980    .021   .927 .926    .960      .030   .936 .923   .953   .036   .916 .907   .945   .043   .919      .894   .928
 (C) RGB(G) + D(G)      .013   .952 .946     .980    .021   .929 .930    .961      .029   .939 .926   .954   .035   .921 .911   .946   .043   .919      .892   .927

awareness which spatially constrains attention around the local                       the full benefit from the geometric priors. For example, the
region. However, with a large H ×W , the attention activation                         building in the 1st row cannot be perfectly distinguished from
is limited. Hence, we further propose to adopt local pooling to                       the background; the cups in the 2nd row are mixed with the
automatically adjust the weight (III). Our superior performance                       table and a part of the wall. The unsatisfactory thresholding
validates the effectiveness of our local design.                                      on the depth histogram leads to sub-optimal performance
                                                                                      of granularity-based attention that the discriminatory power
B. Why GBA in both streams                                                            cannot be fully exploited. While augmenting the number of
                                                                                      thresholds to T = 2, we observe from the 5th column that
   We analyze in Tab. VI the contribution of GBA for both                             the scene can be better discretized. The fine-grained details
RGB and Depth feature modelings: (A) We remove the GBA                                contribute to the clearer boundary generation as shown in the
from our network, denoted as RGB+D; (B) GBA is only                                   6th column. We further augment the number of thresholds
applied in the RGB stream, denoted as RGB(G) + D; (C)                                 to T = 3 and observe the over-discretization, leading to the
GBA is applied in both streams, denoted as RGB(G) +                                   misunderstanding on the depth map. Thus, it results in lower
D(G). We observe that the performance augments by gradually                           quality salient masks as shown in the 8th column.
inserting GBA into the encoders. This shows that GBA can be
                                                                                         Thus, we perform the experiments with different numbers of
considered as depth-aware attention for the RGB stream and
                                                                                      thresholds T . Tab. VII shows that the best overall performance
as a self-enhancement module for the Depth stream to produce
                                                                                      is achieved with T = 2 thresholds, thus with n = 3 regions. It
regions with favorable objectness.
                                                                                      can be considered as a scene discretization into three parts:
 𝑹𝑮𝑩     𝑫𝒆𝒑𝒕𝒉     𝑻=𝟏     𝑴𝒂𝒔𝒌𝟏    𝑻=𝟐      𝑴𝒂𝒔𝒌𝟐     𝑻=𝟑     𝑴𝒂𝒔𝒌𝟑     𝑮𝑻
                                                                                      close, middle, and far regions. Our plain HiDAnet is with
                                                                                      T = 2 thresholds and achieves the best performance. We also
                                                                                      discover that the sensitivity to thresholding varies from one
                                                                                      dataset to another, especially the NLPR dataset which is not
                                                                                      highly sensitive to the granularity. This is mainly due to
                                                                                      the fact that NLPR contains objects residing in the back-
                                                                                      ground. In such circumstances, the target object has the mixed
                                                                                      depth response as the background, leading to less-noticeable
  RGB Depth T = 1 Mask1 T = 2 Mask2 T = 3 Mask3 GT                                    granularity as shown in the last two rows of Figure 10. In
Fig. 10. Qualitative comparison with different numbers of Otsu thresholds             more common and popular cases (DES, NJU2K, STERE, and
(T = 1, 2, 3) for our granularity-based attention. With the threshold T , we          SIP), our fine-grained details achieve significant improvement
divide the depth map into T + 1 regions with different colors. Each region
shares the same granularity of geometric information. With one threshold              compared to our baseline with conventional attention as shown
T = 1, the local regions are coarse and cannot get the full benefit from the          in Tab. VII.
geometric priors. This results in unsatisfactory salient masks (4th column).
With two thresholds T = 2, the depth map is better discretized with more fine-
grained details, yielding salient masks closer to the ground truth (6th column).      D. Ablation study on Key Components
With three thresholds T = 3, the depth map is over-discretized, resulting in
sub-optimal salient masks (8th column). Our plain HiDAnet is built upon                  Tab. VIII presents a thorough ablation study for each key
T = 2.                                                                                component. We observe that by gradually adding proposed
                                                                                      modules, our network leads to better performance. We also
                                                                                      conduct experiments by replacing our proposed modules with
C. Number of Otsu Regions for GBA                                                     several SOTA counterparts. Specifically, we compare our
   Our fine-grained details are determined by the number of                           Granularity-Based Attention with the DEDA module proposed
Otsu regions as shown in Figure 10. The two first columns                             in [6]. Both our GBA and DEDA belong to the mask-guided
represent the paired RGB-D inputs. On the 3rd , 5th , and                             attention modules. Specifically, DEDA leverages the depth
7th columns we list the Otsu regions with different numbers                           map to dynamically learn the masked-guided attention map
of multi granularities, respectively. On the 4th , 6th , and 8th                      which is supervised by the ground truth. The learned attention
columns we list the generated masks with different numbers                            map refers to the contrast to guide RGB learning. Differently,
of thresholds T = 1, 2, 3, respectively.                                              our mask is statically computed by the Otsu threshold by
   By comparing the 3rd and 5th columns, it can be seen                               maximizing inter-class variance. The computed local regions
that a small number of Otsu threshold T = 1 cannot get                                refer to the fine-grained details which are further integrated
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                           11

                                                            TABLE VII
 Q UANTITATIVE COMPARISON WITH DIFFERENT OTSU THRESHOLDS . O UR PLAIN H I DA NET IS WITH T = 2 THRESHOLDS . T = 2 ACHIEVES THE BEST
     PERFORMANCE WITH A REASONABLE FPS. W E USE THE M EAN A BSOLUTE E RROR (M), MAX F- MEASURE (Fm ), S- MEASURE (Sm ), AND MAX
                                      E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST.)

 Dataset                          DES                      NLPR                       NJU2K                       STERE                            SIP
 Metric        FPS ↑   M↓     Fβ ↑ Sm ↑   Em ↑   M↓     Fβ ↑ Sm ↑   Em ↑   M↓      Fβ ↑ Sm ↑    Em ↑   M↓      Fβ ↑ Sm ↑     Em ↑    M↓     Fβ ↑      Sm ↑   Em ↑
 T =0          13.3    .019   .941 .927   .955   .020   .929 .931   .961   .031    .936 .924    .952   .037    .919 .908     .943    .046   .915      .888   .924
 T =1          12.6    .015   .951 .948   .979   .023   .927 .927   .960   .029    .933 .924    .953   .035    .918 .908     .944    .044   .918      .894   .927
 T =2          11.3    .013   .952 .946   .980   .021   .929 .930   .961   .029    .939 .926    .954   .035    .921 .911     .946    .043   .919      .892   .927
 T =3          10.5    .015   .949 .942   .979   .020   .929 .928   .961   .031    .929 .920    .949   .036    .914 .900     .940    .044   .916      .891   .925

                           TABLE VIII                                                                           TABLE IX
A BLATION STUDY ON KEY COMPONENTS OF OUR PROPOSED H I DA NET.                        A BLATION STUDY ON ENCODER FUSION AND DECODER FUSION
 W E PARTIALLY REMOVE KEY COMPONENTS OR REPLACE THE FUSION                        DESIGNS . W E USE THE M EAN A BSOLUTE E RROR (M), MAX F- MEASURE
    DESIGNS WITH A SIMPLE ADDITION . Skip STANDS FOR THE SKIP                      (Fm ), S- MEASURE (Sm ), AND MAX E- MEASURE (Em ) AS EVALUATION
   CONNECTION WITH THE PROPOSED CROSS DUAL ATTENTION . Lml                                              METRICS . (B OLD : BEST.)
    DENOTES THE MULTI - LEVEL SUPERVISION . W E USE THE M EAN
A BSOLUTE E RROR (M), MAX F- MEASURE (Fm ), S- MEASURE (Sm ), AND                                                            DES               STERE
    MAX E- MEASURE (Em ) AS EVALUATION METRICS . (B OLD : BEST;                                Configuration
                                                                                                                      M↓            Fβ ↑    M↓     Fβ ↑
                   U NDERLINE : SECOND BEST.)                                                  HiDAnet                .013          .952    .035   .921
                                                                                      C1       Add                    .017          .945    .039   .915
   # Baseline GBA CDA Skip EMI Lml
                                          DEDA DCF      DES      STERE                C2       Cat + Conv             .016          .946    .039   .916
                                           [6]  [10] M ↓ Fβ ↑ M ↓ Fβ ↑                C3       Self + Add             .015          .948    .036   .918
   1       X                                         .018 .941 .038 .917              C4       Self + Cat + Conv      .014          .949    .037   .917
   2       X       X                                 .016 .944 .037 .917              C5       Cross + Add            .015          .947    .036   .919
   3       X       X    X                            .016 .946 .036 .919              E1       Cat + Conv             .015          .947    .038   .914
   4       X       X    X     X                      .015 .947 .036 .923              E2       Cat + ECA + Conv       .016          .945    .038   .915
   5       X       X    X     X   X                  .014 .949 .034 .921              E3       Cat + Conv + ECA       .015          .949    .037   .916
   6       X                  X   X   X    X         .016 .946 .041 .914              E4       E2 + Residual          .014          .950    .036   .920
   7       X       X          X   X   X          X .017 .946 .037 .918
   8       X       X    X     X   X   X              .013 .952 .035 .921

                                                                                  fused with CC and then fed into the ECA. (E4) Based on
with semantics cues. Empirically, by comparing (#6 − #8),                         the configuration E2, we further add a residual addition. By
our GBA performs favorably against DEDA, showing that                             comparing (E2 − E3) and (E4 − Ours), we can observe that
our method can better leverage the depth cues to distinguish                      the ECA module performs better with a reduced channel size.
objects with different camera distances. We also replace our                      The comparison between (E2 − E4) validates the effectiveness
encoder fusion (CDA) with the concurrent DCF [10] built upon                      of residual addition which propagates the hierarchical features.
channel attention. The main difference is that DCF is based
on channel attention, while our CDA additionally leverages                                                    VI. C ONCLUSION
the spatial attention for better localization. By comparing
(#7 − #8), we can observe that while CDA is replaced by                              In this paper, we propose an end-to-end HiDAnet for
the DCF, the performance drops significantly. This validates                      RGB-D saliency detection. Different from previous networks,
the effectiveness of our CDA with both channel and spatial                        we fully leverage fine-grained details and merge them with
attention.                                                                        semantic cues through the local channel attention. Extensive
Design of Cross Dual Attention: We verify in Tab. IX the                          evaluations on challenging RGB-D benchmarks indicate that
design of our encoder fusion by removing or replacing each                        our HiDAnet improves saliency detection in several challeng-
component: (C1) Features are simply fused through addition;                       ing scenarios where the SOTA approaches fail, notably in cases
(C2) Features are fused through concatenation-convolution                         where multiple objects with similar appearances but at distinct
(CC); (C3) Features are firstly self-enhanced with vanilla                        camera distances (granularity). Our method has the potential
CBAM before the addition fusion. (C4) Features are firstly                        to be used in many other tasks, including semantic and instant
self-enhanced and later fused through CC. (C5) We explore                         segmentation.
the attention in a cross manner and fuse features with addition.
We can observe the gain of attention modules by comparing
                                                                                                        ACKNOWLEDGEMENTS
(C1 −C3 −C5), the improvement from cross-domain interac-
tion by comparing (C3 −C5), and the contribution of CC by                            We gratefully acknowledge Zhuyun Zhou and Renato Mar-
comparing (C5−Ours). These results validate the effectiveness                     tins for discussion and proofreading. This research is sup-
of our proposed encoder fusion scheme.                                            ported in part by the French National Research Agency
Design of Efficient Multi-Input Fusion: We also verify the                        through ANR CLARA (ANR-18-CE33-0004), the French AD-
design of our decoder fusion in Tab. IX: (E1) Features are                        VANCES project ISITE-BFC project (ANR-15-IDEX-0003),
fused with CC. (E2) Features are concatenated and fed into                        and is financed by the French Conseil Régional de Bourgogne-
the ECA model before the convolution. (E3) Features are                           Franche-Comté.
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                       12

                              R EFERENCES                                         [21] J. Zhao, Y. Zhao, J. Li, and X. Chen, “Is depth really necessary for
                                                                                       salient object detection?” in Proceedings of the 28th ACM International
 [1] P. Zhang, D. Wang, H. Lu, H. Wang, and B. Yin, “Learning uncertain                Conference on Multimedia (ACM MM), 2020.
     convolutional features for accurate saliency detection,” in Proceedings of   [22] N. Otsu, “A threshold selection method from gray-level histograms,”
     the IEEE International Conference on Computer Vision (ICCV), 2017.                IEEE transactions on systems, man, and cybernetics (TSMC), vol. 9,
 [2] Z. Deng, X. Hu, L. Zhu, X. Xu, J. Qin, G. Han, and P.-A. Heng,                    no. 1, pp. 62–66, 1979.
     “R3net: Recurrent residual refinement network for saliency detection,”       [23] P.-S. Liao, T.-S. Chen, P.-C. Chung et al., “A fast algorithm for multilevel
     in Proceedings of the 27th International Joint Conference on Artificial           thresholding,” Journal of Information Science and Engineering (JISE),
     Intelligence (IJCAI), 2018.                                                       vol. 17, pp. 713–727, 2001.
 [3] J.-J. Liu, Q. Hou, M.-M. Cheng, J. Feng, and J. Jiang, “A simple pooling-    [24] O. Ronneberger, P. Fischer, and T. Brox, “U-net: Convolutional networks
     based design for real-time salient object detection,” in Proceedings of           for biomedical image segmentation,” in International Conference on
     the IEEE/CVF conference on Computer Vision and Pattern Recognition                Medical image computing and computer-assisted intervention (MIC-
     (CVPR), 2019.                                                                     CAI), 2015.
 [4] Z. Wu, L. Su, and Q. Huang, “Cascaded partial decoder for fast and           [25] W. Wang, Q. Lai, H. Fu, J. Shen, H. Ling, and R. Yang, “Salient
     accurate salient object detection,” in Proceedings of the IEEE/CVF                object detection in the deep learning era: An in-depth survey,” IEEE
     conference on Computer Vision and Pattern Recognition (CVPR), 2019.               Transactions on Pattern Analysis and Machine Intelligence (TPAMI),
 [5] J.-X. Zhao, J.-J. Liu, D.-P. Fan, Y. Cao, J. Yang, and M.-M. Cheng,               pp. 1–1, 2021.
     “EGNet: Edge Guidance Network for salient object detection,” in              [26] X. Shen, “A survey of object classification and detection based on 2d/3d
     Proceedings of the IEEE/CVF International Conference on Computer                  data,” arXiv:1905.12683, 2019.
     Vision (ICCV), 2019.                                                         [27] Z.-Q. Zhao, P. Zheng, S.-t. Xu, and X. Wu, “Object detection with
 [6] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A single stream                 deep learning: A review,” IEEE Transactions on Neural Networks and
     network for robust and real-time RGB-D salient object detection,” in              Learning Systems (TNNLS), vol. 30, no. 11, pp. 3212–3232, 2019.
     Proceedings of the European Conference on Computer Vision (ECCV),            [28] R. Cong, J. Lei, H. Fu, M.-M. Cheng, W. Lin, and Q. Huang, “Review
     2020.                                                                             of visual saliency detection with comprehensive information,” IEEE
 [7] K. Fu, D.-P. Fan, G.-P. Ji, and Q. Zhao, “JL-DCF: Joint learning                  Transactions on Circuits and Systems for Video Technology (TCSVT),
     and densely-cooperative fusion framework for RGB-D salient object                 vol. 29, no. 10, pp. 2941–2959, 2018.
     detection,” in Proceedings of the IEEE/CVF conference on Computer            [29] A. Borji, M.-M. Cheng, Q. Hou, H. Jiang, and J. Li, “Salient object
     Vision and Pattern Recognition (CVPR), 2020.                                      detection: A survey,” Computational Visual Media (CVMJ), vol. 5, no. 2,
 [8] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. S. Saleh, T. Zhang, and                 pp. 117–150, 2019.
     N. Barnes, “Uc-net: Uncertainty inspired rgb-d saliency detection via        [30] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “RGB-D salient
     conditional variational autoencoders,” in Proceedings of the IEEE/CVF             object detection: A survey,” Computational Visual Media (CVMJ), pp.
     conference on Computer Vision and Pattern Recognition (CVPR), 2020.               1–33, 2021.
 [9] D.-P. Fan, Y. Zhai, A. Borji, J. Yang, and L. Shao, “BBS-Net: RGB-D          [31] K. Fu, D.-P. Fan, G.-P. Ji, Q. Zhao, J. Shen, and C. Zhu, “Siamese net-
     salient object detection with a bifurcated backbone strategy network,” in         work for rgb-d salient object detection and beyond,” IEEE transactions
     Proceedings of the European Conference on Computer Vision (ECCV),                 on pattern analysis and machine intelligence (TPAMI), 2021.
     2020.                                                                        [32] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Saleh, S. Aliakbarian,
[10] W. Ji, J. Li, S. Yu, M. Zhang, Y. Piao, S. Yao, Q. Bi, K. Ma,                     and N. Barnes, “Uncertainty inspired rgb-d saliency detection,” IEEE
     Y. Zheng, H. Lu et al., “Calibrated RGB-D salient object detection,”              Transactions on Pattern Analysis and Machine Intelligence (TPAMI),
     in Proceedings of the IEEE/CVF conference on Computer Vision and                  2021.
     Pattern Recognition (CVPR), 2021.                                            [33] Q. Chen, Z. Zhang, Y. Lu, K. Fu, and Q. Zhao, “3-d convolutional
[11] C. Zhang, R. Cong, Q. Lin, L. Ma, F. Li, Y. Zhao, and S. Kwong,                   neural networks for rgb-d salient object detection and beyond,” IEEE
     “Cross-modality discrepant interaction network for RGB-D salient object           Transactions on Neural Networks and Learning Systems (TNNLS), 2022.
     detection,” in Poceedings of the 29th ACM International Conference on        [34] Q. Chen, Z. Liu, Y. Zhang, K. Fu, Q. Zhao, and H. Du, “Rgb-d salient
     Multimedia (ACM MM), 2021.                                                        object detection via 3d convolutional neural networks,” in Proceedings
[12] J. Zhang, D.-P. Fan, Y. Dai, X. Yu, Y. Zhong, N. Barnes, and L. Shao,             of the AAAI Conference on Artificial Intelligence (AAAI), 2021.
     “RGB-D saliency detection via cascaded mutual information minimiza-          [35] J. Zhou, L. Wang, H. Lu, K. Huang, X. Shi, and B. Liu, “Mvsalnet:
     tion,” in Poceedings of the IEEE/CVF International Conference on                  Multi-view augmentation for rgb-d salient object detection,” in European
     Computer Vision (ICCV), 2021.                                                     Conference on Computer Vision (ECCV). Springer, 2022.
[13] T. Zhou, H. Fu, G. Chen, Y. Zhou, D.-P. Fan, and L. Shao, “Specificity-      [36] M. Lee, C. Park, S. Cho, and S. Lee, “Spsn: Superpixel prototype
     preserving RGB-D saliency detection,” in Poceedings of the IEEE/CVF               sampling network for rgb-d salient object detection,” in European
     International Conference on Computer Vision (ICCV), 2021.                         Conference on Computer Vision (ECCV). Springer, 2022.
[14] Z. Liu, W. Yuan, Z. Tu, Y. Xiao, and B. Tang, “TriTransNet: RGB-D            [37] C. Zhu, X. Cai, K. Huang, T. H. Li, and G. Li, “PDNet: Prior-model
     salient object detection with a triplet transformer embedding network,”           guided depth-enhanced network for salient object detection,” in IEEE
     Poceedings of the 29th ACM International Conference on Multimedia                 International Conference on Multimedia and Expo (ICME), 2019.
     (ACM MM), 2021.                                                              [38] Y. Zhai, D.-P. Fan, J. Yang, A. Borji, L. Shao, J. Han, and L. Wang,
[15] P. Sun, W. Zhang, H. Wang, S. Li, and X. Li, “Deep RGB-D saliency                 “Bifurcated backbone strategy for rgb-d salient object detection,” IEEE
     detection with depth-sensitive attention and automatic multi-modal fu-            Transactions on Image Processing (TIP), vol. 30, pp. 8727–8742, 2021.
     sion,” in Proceedings of the IEEE/CVF conference on Computer Vision          [39] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking
     and Pattern Recognition (CVPR), 2021.                                             RGB-D salient object detection: Models, datasets, and large-scale bench-
[16] W. Zhang, G.-P. Ji, Z. Wang, K. Fu, and Q. Zhao, “Depth quality-                  marks,” IEEE Transactions on neural networks and learning systems
     inspired feature manipulation for efficient RGB-D salient object de-              (TNNLS), vol. 32, no. 5, pp. 2075–2089, 2021.
     tection,” in Poceedings of the 29th ACM International Conference on          [40] Z. Wu, S. Gobichettipalayam, B. Tamadazte, G. Allibert, D. P. Paudel,
     Multimedia (ACM MM), 2021.                                                        and C. Demonceaux, “Robust rgb-d fusion for saliency detection,” 2022
[17] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon, “Cbam: Convolutional                 International Conference on 3D Vision (3DV), 2022.
     block attention module,” in Proceedings of the European conference on        [41] X. Cheng, X. Zheng, J. Pei, H. Tang, Z. Lyu, and C. Chen, “Depth-
     computer vision (ECCV), 2018.                                                     induced gap-reducing network for rgb-d salient object detection: An
[18] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in                 interaction, guidance and refinement approach,” IEEE Transactions on
     Proceedings of the IEEE/CVF conference on Computer Vision and                     Multimedia (TMM), 2022.
     Pattern Recognition (CVPR), 2018.                                            [42] N. Huang, Y. Luo, Q. Zhang, and J. Han, “Discriminative unimodal
[19] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image            feature selection and fusion for rgb-d salient object detection,” Pattern
     recognition,” in Proceedings of the IEEE conference on Computer Vision            Recognition (PR), vol. 122, p. 108359, 2022.
     and Pattern Recognition (CVPR), 2016.                                        [43] Z. Zhang, Z. Lin, J. Xu, W.-D. Jin, S.-P. Lu, and D.-P. Fan, “Bilateral
[20] W. Qilong, W. Banggu, Z. Pengfei, L. Peihua, Z. Wangmeng, and                     attention network for rgb-d salient object detection,” IEEE Transactions
     H. Qinghua, “ECA-Net: Efficient channel attention for deep convo-                 on Image Processing (TIP), vol. 30, pp. 1949–1961, 2021.
     lutional neural networks,” in The IEEE/CVF conference on Computer            [44] Y. Piao, Z. Rong, M. Zhang, W. Ren, and H. Lu, “A2dele: Adaptive and
     Vision and Pattern Recognition (CVPR), 2020.                                      attentive depth distiller for efficient RGB-D salient object detection,”
JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021                                                                                                     13

     in Proceedings of the IEEE/CVF conference on Computer Vision and                  Analysis and Machine Intelligence (TPAMI), vol. 33, no. 5, pp. 978–
     Pattern Recognition (CVPR), 2020.                                                 994, 2011.
[45] W. Ji, J. Li, M. Zhang, Y. Piao, and H. Lu, “Accurate RGB-D salient          [69] J. Wang, Y. Zhong, Y. Dai, K. Zhang, P. Ji, and H. Li, “Displacement-
     object detection via collaborative learning,” in Proceedings of the               invariant matching cost learning for accurate optical flow estimation,” in
     European Conference on Computer Vision (ECCV), 2020.                              Advances in Neural Information Processing Systems (NeurIPS), 2020.
[46] Z. Wu, G. Allibert, C. Stolz, C. Ma, and C. Demonceaux, “Modality-           [70] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-scale
     guided subnetwork for salient object detection,” in 2021 International            recurrent attention network for saliency detection,” in Proceedings of the
     Conference on 3D Vision (3DV). IEEE, 2021.                                        IEEE/CVF International Conference on Computer Vision (ICCV), 2019.
[47] W.-D. Jin, J. Xu, Q. Han, Y. Zhang, and M.-M. Cheng, “Cdnet:                 [71] C. Li, R. Cong, Y. Piao, Q. Xu, and C. C. Loy, “RGB-D salient object
     Complementary depth network for rgb-d salient object detection,” IEEE             detection with cross-modality modulation and selection,” in Proceedings
     Transactions on Image Processing (TIP), vol. 30, pp. 3376–3390, 2021.             of the European Conference on Computer Vision (ECCV), 2020.
[48] Y. Pang, L. Zhang, X. Zhao, and H. Lu, “Hierarchical dynamic filtering       [72] G. Li, Z. Liu, L. Ye, Y. Wang, and H. Ling, “Cross-modal weighting
     network for RGB-D salient object detection,” in Proceedings of the                network for rgb-d salient object detection,” in European Conference on
     European Conference on Computer Vision (ECCV), 2020.                              Computer Vision (ECCV). Springer, 2020.
[49] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,      [73] S. Chen and Y. Fu, “Progressively guided alternate refinement network
     Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances            for rgb-d salient object detection,” in European Conference on Computer
     in Neural Information Processing Systems (NeurIPS), 2017.                         Vision (ECCV). Springer, 2020.
[50] J. Fu, J. Liu, H. Tian, Y. Li, Y. Bao, Z. Fang, and H. Lu, “Dual attention   [74] M. Zhang, W. Ren, Y. Piao, Z. Rong, and H. Lu, “Select, supplement
     network for scene segmentation,” in Proceedings of the IEEE/CVF                   and focus for rgb-d saliency detection,” in Proceedings of the IEEE/CVF
     conference on Computer Vision and Pattern Recognition (CVPR), 2019.               conference on computer vision and pattern recognition (CVPR), 2020.
[51] N. Liu, N. Zhang, K. Wan, L. Shao, and J. Han, “Visual saliency              [75] A. Luo, X. Li, F. Yang, Z. Jiao, H. Cheng, and S. Lyu, “Cascade
     transformer,” in Proceedings of the IEEE/CVF International Conference             graph neural networks for rgb-d salient object detection,” in European
     on Computer Vision (ICCV), 2021.                                                  Conference on Computer Vision (ECCV). Springer, 2020.
[52] Y. Zhao, J. Zhao, J. Li, and X. Chen, “Rgb-d salient object detection with   [76] X. Wang, S. Li, C. Chen, Y. Fang, A. Hao, and H. Qin, “Data-level
     ubiquitous target awareness,” IEEE Transactions on Image Processing               recombination and lightweight fusion scheme for rgb-d salient object
     (TIP), vol. 30, pp. 7717–7731, 2021.                                              detection,” IEEE Transactions on Image Processing (TIP), vol. 30, pp.
[53] F. Wang, J. Pan, S. Xu, and J. Tang, “Learning discriminative cross-              458–471, 2020.
     modality features for rgb-d saliency detection,” IEEE Transactions on        [77] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned
     Image Processing (TIP), vol. 31, pp. 1285–1297, 2022.                             salient region detection,” in Proceedings of the IEEE conference on
[54] M. Zhang, S. Yao, B. Hu, Y. Piao, and W. Ji, “C2dfnet: Criss-                     Computer Vision and Pattern Recognition (CVPR), 2009.
     cross dynamic filter network for rgb-d salient object detection,” IEEE       [78] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-measure:
     Transactions on Multimedia (TMM), 2022.                                           A new way to evaluate foreground maps,” in Proceedings of the IEEE
                                                                                       International Conference on Computer Vision (ICCV), 2017.
[55] H. Wen, C. Yan, X. Zhou, R. Cong, Y. Sun, B. Zheng, J. Zhang,
                                                                                  [79] D.-P. Fan, C. Gong, Y. Cao, B. Ren, M.-M. Cheng, and A. Borji,
     Y. Bao, and G. Ding, “Dynamic selective network for rgb-d salient object
                                                                                       “Enhanced-alignment measure for binary foreground map evaluation,”
     detection,” IEEE Transactions on Image Processing (TIP), vol. 30, pp.
                                                                                       in Proceedings of the 27th International Joint Conference on Artificial
     9179–9192, 2021.
                                                                                       Intelligence (IJCAI), 2018.
[56] G. Li, Z. Liu, M. Chen, Z. Bai, W. Lin, and H. Ling, “Hierarchical
                                                                                  [80] K. Simonyan and A. Zisserman, “Very deep convolutional networks
     alternate interaction network for rgb-d salient object detection,” IEEE
                                                                                       for large-scale image recognition,” in 3rd International Conference on
     Transactions on Image Processing (TIP), vol. 30, pp. 3528–3542, 2021.
                                                                                       Learning Representations, (ICLR), 2015.
[57] S. Liu, D. Huang et al., “Receptive field block net for accurate and
                                                                                  [81] S.-H. Gao, M.-M. Cheng, K. Zhao, X.-Y. Zhang, M.-H. Yang, and
     fast object detection,” in Proceedings of the European Conference on
                                                                                       P. Torr, “Res2net: A new multi-scale backbone architecture,” IEEE
     Computer Vision (ECCV), 2018.
                                                                                       Transactions on Pattern Analysis and Machine Intelligence (TPAMI),
[58] J.-X. Zhao, Y. Cao, D.-P. Fan, M.-M. Cheng, X.-Y. Li, and L. Zhang,               vol. 43, no. 2, pp. 652–662, 2021.
     “Contrast prior and fluid pyramid integration for RGBD salient object
     detection,” in Proceedings of the IEEE/CVF conference on Computer
     Vision and Pattern Recognition (CVPR), 2019.
[59] M. Zhang, S. X. Fei, J. Liu, S. Xu, Y. Piao, and H. Lu, “Asymmetric two-
     stream architecture for accurate rgb-d saliency detection,” in Proceedings
     of the European Conference on Computer Vision (ECCV), 2020.
[60] X. Qin, Z. Zhang, C. Huang, C. Gao, M. Dehghan, and M. Jagersand,
     “Basnet: Boundary-aware salient object detection,” in Proceedings of
     the IEEE/CVF conference on Computer Vision and Pattern Recognition
     (CVPR), 2019.
[61] J. Wei, S. Wang, and Q. Huang, “F3 net: Fusion, feedback and focus
     for salient object detection,” in Proceedings of the AAAI Conference on
     Artificial Intelligence (AAAI), 2020.
[62] Z. Chen, Q. Xu, R. Cong, and Q. Huang, “Global context-aware progres-
     sive aggregation network for salient object detection,” in Proceedings of
     the AAAI Conference on Artificial Intelligence (AAAI), 2020.
[63] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based
     on anisotropic center-surround difference,” in 2014 IEEE International
     Conference on Image Processing (ICIP), 2014.
[64] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “RGBD salient object
     detection: a benchmark and algorithms,” in Proceedings of the European
     Conference on Computer Vision (ECCV), 2014.
[65] Y. Cheng, H. Fu, X. Wei, J. Xiao, and X. Cao, “Depth enhanced
     saliency detection method,” in Proceedings of International Conference
     on Internet Multimedia Computing and Service (ICIMCS), 2014.
[66] D. Sun, S. Roth, and M. J. Black, “Secrets of optical flow estimation and
     their principles,” in Proceedings of the IEEE conference on Computer
     Vision and Pattern Recognition (CVPR), 2010.
[67] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency
     analysis,” in IEEE Conference on Computer Vision and Pattern Recog-
     nition (CVPR), 2012.
[68] C. Liu, J. Yuen, and A. Torralba, “Sift flow: Dense correspondence
     across scenes and its applications,” IEEE Transactions on Pattern
