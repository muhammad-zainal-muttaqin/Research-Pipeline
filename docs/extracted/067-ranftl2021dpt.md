---
source_id: 067
bibtex_key: ranftl2021dpt
title: Vision Transformers for Dense Prediction
year: 2021
domain_theme: Estimasi Kedalaman
verified_pdf: 67_DPT (Dense Prediction Transformer).pdf
char_count: 81816
---

Vision Transformers for Dense Prediction

                                                               René Ranftl              Alexey Bochkovskiy                 Vladlen Koltun

                                                                                               Intel Labs
                                                                                       rene.ranftl@intel.com
arXiv:2103.13413v1 [cs.CV] 24 Mar 2021

                                                                 Abstract                               on the decoder and its aggregation strategy [6, 7, 50, 53].
                                                                                                        However, it is widely recognized that the choice of back-
                                            We introduce dense vision transformers, an architecture     bone architecture has a large influence on the capabilities
                                         that leverages vision transformers in place of convolutional   of the overall model, as any information that is lost in the
                                         networks as a backbone for dense prediction tasks. We as-      encoder is impossible to recover in the decoder.
                                         semble tokens from various stages of the vision transformer        Convolutional backbones progressively downsample the
                                         into image-like representations at various resolutions and     input image to extract features at multiple scales. Down-
                                         progressively combine them into full-resolution predictions    sampling enables a progressive increase of the receptive
                                         using a convolutional decoder. The transformer backbone        field, the grouping of low-level features into abstract high-
                                         processes representations at a constant and relatively high    level features, and simultaneously ensures that memory
                                         resolution and has a global receptive field at every stage.    and computational requirements of the network remain
                                         These properties allow the dense vision transformer to pro-    tractable. However, downsampling has distinct drawbacks
                                         vide finer-grained and more globally coherent predictions      that are particularly salient in dense prediction tasks: fea-
                                         when compared to fully-convolutional networks. Our ex-         ture resolution and granularity are lost in the deeper stages
                                         periments show that this architecture yields substantial im-   of the model and can thus be hard to recover in the decoder.
                                         provements on dense prediction tasks, especially when a        While feature resolution and granularity may not matter for
                                         large amount of training data is available. For monocular      some tasks, such as image classification, they are critical
                                         depth estimation, we observe an improvement of up to 28%       for dense prediction, where the architecture should ideally
                                         in relative performance when compared to a state-of-the-       be able to resolve features at or close to the resolution of the
                                         art fully-convolutional network. When applied to semantic      input image.
                                         segmentation, dense vision transformers set a new state of         Various techniques to mitigate the loss of feature gran-
                                         the art on ADE20K with 49.02% mIoU. We further show            ularity have been proposed. These include training at
                                         that the architecture can be fine-tuned on smaller datasets    higher input resolution (if the computational budget per-
                                         such as NYUv2, KITTI, and Pascal Context where it also         mits), dilated convolutions [49] to rapidly increase the re-
                                         sets the new state of the art. Our models are available at     ceptive field without downsampling, appropriately-placed
                                         https://github.com/intel-isl/DPT.                              skip connections from multiple stages of the encoder to
                                                                                                        the decoder [31], or, more recently, by connecting multi-
                                                                                                        resolution representations in parallel throughout the net-
                                         1. Introduction                                                work [42]. While these techniques can significantly im-
                                                                                                        prove prediction quality, the networks are still bottlenecked
                                            Virtually all existing architectures for dense prediction   by their fundamental building block: the convolution. Con-
                                         are based on convolutional networks [6, 31, 34, 42, 49,        volutions together with non-linearities form the fundamen-
                                         50, 53]. The design of dense prediction architectures com-     tal computational unit of image analysis networks. Convo-
                                         monly follows a pattern that logically separates the network   lutions, by definition, are linear operators that have a lim-
                                         into an encoder and a decoder. The encoder is frequently       ited receptive field. The limited receptive field and the lim-
                                         based on an image classification network, also called the      ited expressivity of an individual convolution necessitate se-
                                         backbone, that is pretrained on a large corpus such as Im-     quential stacking into very deep architectures to acquire suf-
                                         ageNet [9]. The decoder aggregates features from the en-       ficiently broad context and sufficiently high representational
                                         coder and converts them to the final dense predictions. Ar-    power. This, however, requires the production of many in-
                                         chitectural research on dense prediction frequently focuses    termediate representations that require a large amount of
memory. Downsampling the intermediate representations            sentation together with multiple lower-resolution represen-
is necessary to keep memory consumption at levels that are       tations throughout the network [37, 42].
feasible with existing computer architectures.                       Attention-based models [2] and in particular transform-
    In this work, we introduce the dense prediction trans-       ers [39] have been the architecture of choice for learning
former (DPT). DPT is a dense prediction architecture that is     strong models for natural language processing (NLP) [4,
based on an encoder-decoder design that leverages a trans-       10, 24] in recent years. Transformers are set-to-set mod-
former as the basic computational building block of the en-      els that are based on the self-attention mechanism. Trans-
coder. Specifically, we use the recently proposed vision         former models have been particularly successful when in-
transformer (ViT) [11] as a backbone architecture. We re-        stantiated as high-capacity architectures and trained on very
assemble the bag-of-words representation that is provided        large datasets. There have been several works that adapt at-
by ViT into image-like feature representations at various        tention mechanisms to image analysis [3, 28, 29, 41, 52]. In
resolutions and progressively combine the feature repre-         particular, it has recently been demonstrated that a direct ap-
sentations into the final dense prediction using a convolu-      plication of token-based transformer architectures that have
tional decoder. Unlike fully-convolutional networks, the vi-     been successful in NLP can yield competitive performance
sion transformer backbone foregoes explicit downsampling         on image classification [11]. A key insight of this work was
operations after an initial image embedding has been com-        that, like transformer models in NLP, vision transformers
puted and maintains a representation with constant dimen-        need to be paired with a sufficient amount of training data
sionality throughout all processing stages. It furthermore       to realize their potential.
has a global receptive field at every stage. We show that
these properties are especially advantageous for dense pre-      3. Architecture
diction tasks as they naturally lead to fine-grained and glob-
ally coherent predictions.                                           This section introduces the dense vision transformer. We
    We conduct experiments on monocular depth estimation         maintain the overall encoder-decoder structure that has been
and semantic segmentation. For the task of general-purpose       successful for dense prediction in the past. We leverage vi-
monocular depth estimation [30], where large-scale train-        sion transformers [11] as the backbone, show how the rep-
ing data is available, DPT provides a performance increase       resentation that is produced by this encoder can be effec-
of more than 28% when compared to the top-performing             tively transformed into dense predictions, and provide in-
fully-convolutional network for this task. The architecture      tuition for the success of this strategy. An overview of the
can also be fine-tuned to small monocular depth prediction       complete architecture is shown in Figure 1 (left).
datasets, such as NYUv2 [35] and KITTI [15], where it            Transformer encoder. On a high level, the vision trans-
also sets the new state of the art. We provide further evi-      former (ViT) [11] operates on a bag-of-words representa-
dence of the strong performance of DPT using experiments         tion of the image [36]. Image patches that are individually
on semantics segmentation. For this task, DPT sets a new         embedded into a feature space, or alternatively deep fea-
state of the art on the challenging ADE20K [54] and Pas-         tures extracted from the image, take the role of “words”.
cal Context [26] datasets. Our qualitative results indicate      We will refer to embedded “words” as tokens throughout
that the improvements can be attributed to finer-grained and     the rest of this work. Transformers transform the set of to-
more globally coherent predictions in comparison to convo-       kens using sequential blocks of multi-headed self-attention
lutional networks.                                               (MHSA) [39], which relate tokens to each other to trans-
                                                                 form the representation.
2. Related Work                                                      Importantly for our application, a transformer maintains
    Fully-convolutional networks [33, 34] are the prototyp-      the number of tokens throughout all computations. Since to-
ical architecture for dense prediction. Many variants of         kens have a one-to-one correspondence with image patches,
this basic pattern have been proposed over the years, how-       this means that the ViT encoder maintains the spatial reso-
ever, all existing architectures adopt convolution and sub-      lution of the initial embedding throughout all transformer
sampling as their fundamental elements in order to learn         stages. Additionally, MHSA is an inherently global oper-
multi-scale representations that can leverage an appropri-       ation, as every token can attend to and thus influence ev-
ately large context. Several works propose to progressively      ery other token. Consequently, the transformer has a global
upsample representations that have been pooled at differ-        receptive field at every stage after the initial embedding.
ent stages [1, 23, 27, 31], while others use dilated convo-      This is in stark contrast to convolutional networks, which
lutions [6, 7, 49] or parallel multi-scale feature aggregation   progressively increase their receptive field as features pass
at multiple scales [53] to recover fine-grained predictions      through consecutive convolution and downsampling layers.
while at the same time ensuring a sufficiently large context.        More specifically, ViT extracts a patch embedding from
More recent architectures maintain a high-resolution repre-      the image by processing all non-overlapping square patches
                                      Reassemble32    Fusion

                        Transformer

                                      Reassemble16    Fusion

                       Transformer                                                                            Residual Conv Unit       +

                                      Reassemble8     Fusion

                        Transformer                                                                                           Residual Conv Unit
                                                                       Read                      Resamples
                                      Reassemble4     Fusion
                                                                                                  Project                          Resample0.5
                        Transformer
                                                      Head
                                                                                 Concatenate                                         Project
                                                                                                             Fusion

                                                                                               Reassembles
              Embed

Figure 1. Left: Architecture overview. The input image is transformed into tokens (orange) either by extracting non-overlapping patches
followed by a linear projection of their flattened representation (DPT-Base and DPT-Large) or by applying a ResNet-50 feature extractor
(DPT-Hybrid). The image embedding is augmented with a positional embedding and a patch-independent readout token (red) is added.
The tokens are passed through multiple transformer stages. We reassemble tokens from different stages into an image-like representation
at multiple resolutions (green). Fusion modules (purple) progressively fuse and upsample the representations to generate a fine-grained
prediction. Center: Overview of the Reassembles operation. Tokens are assembled into feature maps with 1s the spatial resolution of the
input image. Right: Fusion blocks combine features using residual convolutional units [23] and upsample the feature maps.

of size p2 pixels from the image. The patches are flattened           projects the flattened patches to dimension D = 768 and
into vectors and individually embedded using a linear pro-            D = 1024, respectively. Since both feature dimensions are
jection. An alternative, more sample-efficient, variant of            larger than the number of pixels in an input patch, this
ViT extracts the embedding by applying a ResNet50 [16] to             means that the embedding procedure can learn to retain in-
the image and uses the pixel features of the resulting feature        formation if it is beneficial for the task. Features from the
maps as tokens. Since transformers are set-to-set functions,          input patches can in principle be resolved with pixel-level
they do not intrinsically retain the information of the spatial       accuracy. Similarly, the ViT-Hybrid architecture extracts
                                                                                   1
positions of individual tokens. The image embeddings are              features at 16  the input resolution, which is twice as high
thus concatenated with a learnable position embedding to              as the lowest-resolution features that are commonly used
add this information to the representation. Following work            with convolutional backbones.
in NLP, the ViT additionally adds a special token that is not         Convolutional decoder. Our decoder assembles the set
grounded in the input image and serves as the final, global           of tokens into image-like feature representations at various
image representation which is used for classification. We             resolutions. The feature representations are progressively
refer to this special token as the readout token. The result          fused into the final dense prediction. We propose a sim-
of applying the embedding procedure to an image of size               ple three-stage Reassemble operation to recover image-like
H × W pixels is a a set of t0 = {t00 , . . . , t0Np }, t0n ∈ RD       representations from the output tokens of arbitrary layers of
tokens, where Np = HW    p2 , t0 refers to the readout token,         the transformer encoder:
and D is the feature dimension of each token.
   The input tokens are transformed using L transformer               ReassembleD̂
                                                                                s (t) = (Resamples ◦ Concatenate ◦ Read)(t),
layers into new representations tl , where l refers to the out-
                                                                      where s denotes the output size ratio of the recovered rep-
put of the l-th transformer layer. Dosovitskiy et al. [11]
                                                                      resentation with respect to the input image, and D̂ denotes
define several variants of this basic blueprint. We use three
                                                                      the output feature dimension.
variants in our work: ViT-Base, which uses the patch-based
                                                                         We first map the Np + 1 tokens to a set of Np tokens
embedding procedure and features 12 transformer layers;
                                                                      that is amenable to spatial concatenation into an image-like
ViT-Large, which uses the same embedding procedure and
                                                                      representation:
has 24 transformer layers and a wider feature size D; and
ViT-Hybrid, which employs a ResNet50 to compute the im-                                 Read : RNp +1×D → RNp ×D .                                 (1)
age embedding followed by 12 transformer layers. We use
patch size p = 16 for all experiments. We refer the inter-            This operation is essentially responsible for appropriately
ested reader to the original work [11] for additional details         handling the readout token. Since the readout token doesn’t
on these architectures.                                               serve a clear purpose for the task of dense prediction, but
   The embedding procedure for ViT-Base and ViT-Large                 could potentially still be useful to capture and distribute
global information, we evaluate three different variants of       block [23, 45] (see Figure1 (right)) and progressively up-
this mapping:                                                     sample the representation by a factor of two in each fusion
                                                                  stage. The final representation size has half the resolution
               Readignore (t) = {t1 , . . . , tNp }         (2)   of the input image. We attach a task-specific output head to
                                                                  produce the final prediction. A schematic overview of the
simply ignores the readout token,
                                                                  complete architecture is shown in Figure 1.
           Readadd (t) = {t1 + t0 , . . . , tNp + t0 }      (3)   Handling varying image sizes. Akin to fully-convolutional
                                                                  networks, DPT can handle varying image sizes. As long as
passes the information from the readout token to all other        the image size is divisible by p, the embedding procedure
tokens by adding the representations, and                         can be applied and will produce a varying number of im-
                                                                  age tokens Np . As a set-to-set architecture, the transformer
  Readproj (t) = {mlp(cat(t1 , t0 )), . . . ,
                                                                  encoder can trivially handle a varying number of tokens.
                                       mlp(cat(tNp , t0 ))} (4)   However, the position embedding has a dependency on the
                                                                  image size as it encodes the locations of the patches in the
passes information to the other tokens by concatenating the
                                                                  input image. We follow the approach proposed in [11] and
readout to all other tokens before projecting the representa-
                                                                  linearly interpolate the position embeddings to the appro-
tion to the original feature dimension D using a linear layer
                                                                  priate size. Note that this can be done on the fly for every
followed by a GELU non-linearity [17].
                                                                  image. After the embedding procedure and the transformer
   After a Read block, the resulting Np tokens can be re-
                                                                  stages, both the reassemble and fusion modules can triv-
shaped into an image-like representation by placing each
                                                                  ially handle a varying number of tokens, provided that the
token according to the position of the initial patch in the
                                                                  input image is aligned to the stride of the convolutional de-
image. Formally, we apply a spatial concatenation opera-
                                                                  coder (32 pixels).
tion that results in a feature map of size H      W
                                             p × p with D
channels:
                                                                  4. Experiments
                                        H W
                              Np ×D      ×  ×D
           Concatenate : R            →Rp p    .            (5)       We apply DPT to two dense prediction tasks: monoc-
                                                                  ular depth estimation and semantic segmentation. For both
We finally pass this representation to a spatial resampling       tasks, we show that DPT can significantly improve accuracy
layer that scales the representation to size Hs × W
                                                  s with D̂       when compared to convolutional networks with a similar
features per pixel:                                               capacity, especially if a large training dataset is available.
                          H    W
                              × p ×D            H   W             We first present our main results using the default configu-
         Resamples : R p               → R s × s ×D̂ .      (6)   ration and show comprehensive ablations of different DPT
                                                                  configurations at the end of this section.
We implement this operation by first using 1 × 1 convolu-
tions to project the input representation to D̂, followed by a    4.1. Monocular Depth Estimation
(strided) 3 × 3 convolution when s ≥ p, or a strided 3 × 3
transpose convolution when s < p, to implement spatial                Monocular depth estimation is typically cast as a dense
downsampling and upsampling operations, respectively.             regression problem. It has been shown that massive meta-
    Irrespective of the exact transformer backbone, we re-        datasets can be constructed from existing sources of data,
assemble features at four different stages and four differ-       provided that some care is taken in how different represen-
ent resolutions. We assemble features from deeper lay-            tations of depth are unified into a common representation
ers of the transformer at lower resolution, whereas fea-          and that common ambiguities (such as scale ambiguity) are
tures from early layers are assembled at higher resolution.       appropriately handled in the training loss [30]. Since trans-
When using ViT-Large, we reassemble tokens from layers            formers are known to realize their full potential only when
l = {5, 12, 18, 24}, whereas with ViT-Base we use layers          an abundance of training data is available, monocular depth
l = {3, 6, 9, 12}. We use features from the first and sec-        estimation is an ideal task to test the capabilities of DPT.
ond ResNet block from the embedding network and stages            Experimental protocol. We closely follow the protocol of
l = {9, 12} when using ViT-Hybrid. Our default architec-          Ranftl et al. [30]. We learn a monocular depth prediction
ture uses projection as the readout operation and produces        network using a scale- and shift-invariant trimmed loss that
feature maps with D̂ = 256 dimensions. We will refer              operates on an inverse depth representation, together with
to these architectures as DPT-Base, DPT-Large, and DPT-           the gradient-matching loss proposed in [22]. We construct
Hybrid, respectively.                                             a meta-dataset that includes the original datasets that were
    We finally combine the extracted feature maps from            used in [30] (referred to as MIX 5 in that work) and extend
consecutive stages using a RefineNet-based feature fusion         it with with five additional datasets ([18, 43, 44, 46, 47]).
               Training set            DIW                 ETH3D             Sintel          KITTI             NYU             TUM
                                     WHDR                  AbsRel           AbsRel           δ>1.25           δ>1.25          δ>1.25
 DPT - Large      MIX 6          10.82 (-13.2%)        0.089 (-31.2%)   0.270 (-17.5%)    8.46 (-64.6%)    8.32 (-12.9%)    9.97 (-30.3%)
 DPT - Hybrid     MIX 6          11.06 (-11.2%)        0.093 (-27.6%)   0.274 (-16.2%)   11.56 (-51.6%)    8.69 (-9.0%)    10.89 (-23.2%)
 MiDaS            MIX 6          12.95 (+3.9%)         0.116 (-10.5%)   0.329 (+0.5%)    16.08 (-32.7%)    8.71 (-8.8%)    12.51 (-12.5%)
 MiDaS [30]       MIX 5          12.46                 0.129            0.327            23.90             9.55            14.29
 Li [22]         MD [22]         23.15                 0.181            0.385            36.29            27.52            29.54
 Li [21]         MC [21]         26.52                 0.183            0.405            47.94            18.57            17.71
 Wang [40]       WS [40]         19.09                 0.205            0.390            31.92            29.57            20.18
 Xian [45]       RW [45]         14.59                 0.186            0.422            34.08            27.00            25.02
 Casser [5]       CS [8]         32.80                 0.235            0.422            21.15            39.58            37.18
Table 1. Comparison to the state of the art on monocular depth estimation. We evaluate zero-shot cross-dataset transfer according to the
protocol defined in [30]. Relative performance is computed with respect to the original MiDaS model [30]. Lower is better for all metrics.

We refer to this meta-dataset as MIX 6. It contains about                 Zero-shot cross-dataset transfer. Table 1 shows the re-
1.4 million images and is, to the best of our knowledge, the              sults of zero-shot transfer to different datasets that were not
largest training set for monocular depth estimation that has              seen during training. We refer the interested reader to Ran-
ever been compiled.                                                       ftl et al. [30] for details of the evaluation procedure and
    We use multi-objective optimization [32] together with                error metrics. For all metrics, lower is better. Both DPT
Adam [19] and set a learning rate of 1e−5 for the back-                   variants significantly outperform the state of the art. The
bone and 1e−4 for the decoder weights. The encoder is                     average relative improvement over the best published archi-
initialized with ImageNet-pretrained weights, whereas the                 tecture, MiDaS, is more than 23% for DPT-Hybrid and 28%
decoder is initialized randomly. We use an output head that               for DPT-Large. DPT-Hybrid achieves this with a compara-
consists of 3 convolutional layers. The output head progres-              ble network capacity (Table 9), while DPT-Large is about 3
sively halves the feature dimension and upsamples the pre-                times larger than MiDaS. Note that both architectures have
dictions to the input resolution after the first convolutional            similar latency to MiDaS (Table 9).
layer (details in supplementary material). We disable batch                   To ensure that the observed improvements are not only
normalization in the decoder, as we found it to negatively                due to the enlarged training set, we retrain the fully-
influence results for regression tasks. We resize the image               convolutional network used by MiDaS on our larger meta-
such that the longer side is 384 pixels and train on random               dataset MIX 6. While the fully-convolutional network in-
square crops of size 384. We train for 60 epochs, where one               deed benefits from the larger training set, we observe that
epoch consists of 72,000 steps with a batch size of 16. As                both DPT variants still strongly outperform this network.
the batch size is not divisible by the number of datasets, we             This shows that DPT can better benefit from increased train-
construct a mini-batch by first drawing datasets uniformly                ing set size, an observation that matches previous findings
at random before sampling from the respective datasets.                   on transformer-based architectures in other fields.
We perform random horizontal flips for data augmentation.                     The quantitative results are supported by visual com-
Similar to [30], we first pretrain on a well-curated subset of            parisons in Figure 2. DPT can better reconstruct fine de-
the data [45, 46, 47] for 60 epochs before training on the                tails while also improving global coherence in areas that are
full dataset.                                                             challenging for the convolutional architecture (for example,
                                                                          large homogeneous regions or relative depth arrangement
              δ>1.25 δ>1.252 δ>1.253 AbsRel RMSE log10
                                                                          across the image).
 DORN [13]      0.828    0.965     0.992     0.115     0.509    0.051
 VNL [48]       0.875    0.976     0.994     0.111     0.416    0.048     Fine-tuning on small datasets. We fine-tune DPT-Hybrid
 BTS [20]       0.885    0.978     0.994     0.110     0.392    0.047     on the KITTI [15] and NYUv2 [35] datasets to further com-
 DPT-Hybrid     0.904    0.988     0.998     0.110     0.357    0.045     pare the representational power of DPT to existing work.
                                                                          Since the network was trained with an affine-invariant loss,
              Table 2. Evaluation on NYUv2 depth.                         its predictions are arbitrarily scaled and shifted and can have
                                                                          large magnitudes. Direct fine-tuning would thus be chal-
              δ>1.25 δ>1.252 δ>1.253 AbsRel RMSE RMSE log
                                                                          lenging, as the global mismatch in the magnitude of the
 DORN [13]    0.932     0.984    0.994     0.072     2.626     0.120
                                                                          predictions to the ground truth would dominate the loss.
 VNL [48]     0.938     0.990    0.998     0.072     3.258     0.117
 BTS [20]     0.956     0.993    0.998     0.059     2.756     0.096      We thus first align predictions of the initial network to each
 DPT-Hybrid   0.959     0.995    0.999     0.062     2.573     0.092
                                                                          training sample using the robust alignment procedure de-
                                                                          scribed in [30]. We then average the resulting scales and
          Table 3. Evaluation on KITTI (Eigen split).                     shifts across the training set and apply the average scale and
             Input                      MiDaS (MIX 6)                     DPT-Hybrid                        DPT-Large

Figure 2. Sample results for monocular depth estimation. Compared to the fully-convolutional network used by MiDaS, DPT shows better
global coherence (e.g., sky, second row) and finer-grained details (e.g., tree branches, last row).

shift to the predictions before passing the result to the loss.      both heads. We use SGD with momentum 0.9 and a poly-
We fine-tune with the loss proposed by Eigen et al. [12].            nomial learning rate scheduler with decay factor 0.9. We
We disable the gradient-matching loss for KITTI since this           use batch normalization in the fusion layers and train with
dataset only provides sparse ground truth.                           batch size 48. Images are resized to 520 pixels side length.
   Tables 2 and 3 summarize the results. Our architecture            We use random horizontal flipping and random rescaling in
matches or improves state-of-the-art performance on both             the range ∈ (0.5, 2.0) for data augmentation. We train on
datasets in all metrics. This indicates that DPT can also be         square random crops of size 480. We set the learning rate to
usefully applied to smaller datasets.                                0.002. We use multi-scale inference at test time and report
                                                                     both pixel accuracy (pixAcc) as well as mean Intersection-
4.2. Semantic Segmentation                                           over-Union (mIoU).
   We choose semantic segmentation as our second task                ADE20K. We train the DPT on the ADE20K semantic seg-
since it is representative of discrete labeling tasks and is         mentation dataset [54] for 240 epochs. Table 4 summa-
a very competitive proving ground for dense prediction ar-           rizes our results on the validation set. DPT-Hybrid outper-
chitectures. We employ the same backbone and decoder                 forms all existing fully-convolutional architectures. DPT-
structure as in previous experiments. We use an output head          Large performs slightly worse, likely because of the sig-
that predicts at half resolution and upsamples the logits to         nificantly smaller dataset compared to our previous experi-
full resolution using bilinear interpolation (details in sup-        ments. Figure 3 provides visual comparisons. We observe
plementary material). The encoder is again initialized from          that the DPT tends to produce cleaner and finer-grained de-
ImageNet-pretrained weights, and the decoder is initialized          lineations of object boundaries and that the predictions are
randomly.                                                            also in some cases less cluttered.
Experimental protocol. We closely follow the protocol es-            Fine-tuning on smaller datasets. We fine-tune DPT-
tablished by Zhang et al. [51]. We employ a cross-entropy            Hybrid on the Pascal Context dataset [26] for 50 epochs. All
loss and add an auxiliary output head together with an aux-          other hyper-parameters remain the same. Table 5 shows re-
iliary loss to the output of the penultimate fusion layer. We        sults on the validation set for this experiment. We again see
set the weight of the auxiliary loss to 0.2. Dropout with            that DPT can provide strong performance even on smaller
a rate of 0.1 is used before the final classification layer in       datasets.
ResNeSt-200 [51]
DPT-Hybrid

Figure 3. Sample results for semantic segmentation on ADE20K (first and second column) and Pascal Context (third and fourth column).
Predictions are frequently better aligned to object edges and less cluttered.

4.3. Ablations                                                       representation. Since the transformer backbone maintains a
                                                                     constant feature resolution, it is not clear at which points in
   We examine a number of aspects and technical choices in           the backbone features should be tapped. We evaluate sev-
DPT via ablation studies. We choose monocular depth esti-            eral possible choices in Table 6 (top). We observe that it is
mation as the task for our ablations and follow the same pro-        beneficial to tap features from layers that contain low-level
tocol and hyper-parameter settings as previously described.          features as well as deeper layers that contain higher-level
We use a reduced meta-dataset that is composed of three              features. We adopt the best setting for all further experi-
datasets [45, 46, 47] and consists of about 41,000 images.           ments.
We choose these datasets since they provide high-quality
                                                                        We perform a similar experiment with the hybrid archi-
ground truth. We split each dataset into a training set and
                                                                     tecture in Table 6 (bottom), where R0 and R1 refer to us-
a small validation set of about 1,000 images total. We re-
                                                                     ing features from the first and second downsampling stages
port results on the validation sets in terms of relative ab-
                                                                     of the ResNet50 embedding network. We observe that us-
solute deviation after affine alignment of the predictions to
                                                                     ing low-level features from the embedding network leads
the ground truth [30]. Unless specified otherwise, we use
                                                                     to better performance than using features solely from the
ViT-Base as the backbone architecture.
                                                                     transformer stages. We use this setting for all further exper-
Skip connections. Convolutional architectures offer natu-            iments that involve the hybrid architecture.
ral points of interest for passing features from the encoder
to the decoder, namely before or after downsampling of the           Readout token. Table 7 examines various choices for im-
                                                                     plementing the first stage of the Reassemble block to han-
                     Backbone                pixAcc [%]   mIoU [%]   dle the readout token. While ignoring the token yields
                                                                     good performance, projection provides slightly better per-
       OCNet         ResNet101    [50]           –         45.45
       ACNet         ResNet101    [14]         81.96       45.90     formance on average. Adding the token, on the other hand,
       DeeplabV3    ResNeSt-101   [7, 51]      82.07       46.91     yields worse performance than simply ignoring it. We use
       DeeplabV3    ResNeSt-200   [7, 51]      82.45       48.36     projection for all further experiments.
       DPT-Hybrid   ViT-Hybrid                 83.11       49.02     Backbones. The performance of different backbones is
       DPT-Large    ViT-Large                  82.70       47.63
Table 4. Semantic segmentation results on the ADE20K validation                    Layer l       HRWSI BlendedMVS ReDWeb      Mean
set.                                                                             {3, 6, 9, 12}   0.0793   0.0780   0.0892    0.0822
                                                                      Base

                                                                                {6, 8, 10, 12}   0.0801   0.0789   0.0904    0.0831
                     Backbone                pixAcc [%]   mIoU [%]             {9, 10, 11, 12}   0.0805   0.0766   0.0912    0.0828
      OCNet         HRNet-W48     [42, 50]        –          56.2
                                                                      Hybrid

                                                                                 {3, 6, 9, 12}   0.0747   0.0748   0.0865    0.0787
      DeeplabV3     ResNeSt-200   [7, 51]       82.50       58.37              {R0, R1, 9, 12}   0.0742   0.0751   0.0857    0.0733
      DeeplabV3     ResNeSt-269   [7, 51]       83.06       58.92
      DPT-Hybrid    ViT-Hybrid                  84.83       60.46
                                                                     Table 6. Performance of attaching skip connections to different
                                                                     encoder layers. Best results are achieved with a combination of
Table 5. Finetuning results on the Pascal Context validation set.    skip connections from shallow and deep layers.
                                                                                                   ViT-Hybrid   DeIT-Distilled         ResNext-101    ResNet-50
                 HRWSI BlendedMVS ReDWeb            Mean
                                                                                                 25.00
       Ignore    0.0793   0.0780   0.0892          0.0822
       Add       0.0799   0.0789   0.0904          0.0831

                                                                      Perfomrance decrease [%]
                                                                                                 20.00
       Project   0.0797   0.0764   0.0895          0.0819
                                                                                                 15.00
Table 7. Performance of approaches to handle the readout token.
Fusing the readout token to the individual input tokens using a                                  10.00
projection layer yields the best performance.
                                                                                                  5.00
shown in Table 8. ViT-Large outperforms all other back-
                                                                                                  0.00
bones but is also almost three times larger than ViT-Base                                                 416   448     480      512     544    576   608   640
and ViT-Hybrid. ViT-Hybrid outperforms ViT-Base with a                                                                           Resolution
similar number of parameters and has comparable perfor-             Figure 4. Relative loss in performance for different inference res-
mance to the large backbone. As such it provides a good             olutions (lower is better).
trade-off between accuracy and capacity.
    ViT-Base has comparable performance to ResNext101-              in every layer. We conjecture that this makes DPT less de-
WSL, while ViT-Hybrid and ViT-Large improve perfor-                 pendent on inference resolution. To test this hypothesis, we
mance even though they have been pretrained on signifi-             plot the loss in performance of different architectures when
cantly less data. Note that ResNext101-WSL was pretrained           performing inference at resolutions higher than the training
on a billion-scale corpus of weakly supervised data [25] in         resolution of 384×384 pixels. We plot the relative decrease
addition to ImageNet pretraining. It has been observed that         in performance in percent with respect to the performance
this pretraining boosts the performance of monocular depth          of performing inference at the training resolution in Fig-
prediction [30]. This architecture corresponds to the origi-        ure 4. We observe that the performance of DPT variants
nal MiDaS architecture.                                             indeed degrades more gracefully as inference resolution in-
    We finally compare to a recent variant of ViT called            creases.
DeIT [38]. DeIT trains the ViT architecture with a more             Inference speed. Table 9 shows inference time for differ-
data-efficient pretraining procedure. Note that the DeIT-           ent network architectures. Timings were conducted on an
Base architecture is identical to ViT-Base, while DeIT-             Intel Xeon Platinum 8280 CPU @ 2.70GHz with 8 physical
Base-Dist introduces an additional distillation token, which        cores and an Nvidia RTX 2080 GPU. We use square images
we ignore in the Reassemble operation. We observe that              with a width of 384 pixels and report the average over 400
DeIT-Base-Dist indeed improves performance when com-                runs. DPT-Hybrid and DPT-Large show comparable latency
pared to ViT-Base. This indicates that similarly to convo-          to the fully-convolutional architecture used by MiDaS. In-
lutional architectures, improvements in pretraining proce-          terestingly, while DPT-Large is substantially larger than the
dures for image classification can benefit dense prediction         other architectures in terms of parameter count, it has com-
tasks.                                                              petitive latency since it exposes a high degree of parallelism
Inference resolution. While fully-convolutional architec-           through its wide and comparatively shallow structure.
tures can have large effective receptive fields in their deepest
                                                                                                                  MiDaS DPT-Base DPT-Hybrid DPT-Large
layers, the layers close to the input are local and have small
receptive fields. Performance thus suffers heavily when              Parameters [million]                             105         112           123         343
performing inference at an input resolution that is signifi-         Time [ms]                                         32          17            38          35
cantly different from the training resolution. Transformer          Table 9. Model statistics. DPT has comparable inference speed to
encoders, on the other hand, have a global receptive field          the state of the art.

                     HRWSI BlendedMVS ReDWeb            Mean
  ResNet50           0.0890   0.0887   0.1029          0.0935       5. Conclusion
  ResNext101-WSL     0.0780   0.0751   0.0886          0.0806
  DeIT-Base          0.0798   0.0804   0.0925          0.0842          We have introduced the dense prediction transformer,
  DeIT-Base-Dist     0.0758   0.0758   0.0871          0.0796       DPT, a neural network architecture that effectively lever-
  ViT-Base           0.0797   0.0764   0.0895          0.0819       ages vision transformers for dense prediction tasks. Our
  ViT-Large          0.0740   0.0747   0.0846          0.0778       experiments on monocular depth estimation and semantic
  ViT-Hybrid         0.0738   0.0746   0.0864          0.0783       segmentation show that the presented architecture produces
Table 8. Ablation of backbones. The hybrid and large backbones      more fine-grained and globally coherent predictions when
consistently outperform the convolutional baselines. The base ar-   compared to fully-convolutional architectures. Similar to
chitecture can outperform the convolutional baseline with better    prior work on transformers, DPT unfolds its full potential
pretraining (DeIT-Base-Dist).                                       when trained on large-scale datasets.
References                                                          [17] Dan Hendrycks and Kevin Gimpel. Gaussian error linear
                                                                         units (GELUs). arXiv preprint arXiv:1606.08415, 2016.
 [1] Vijay Badrinarayanan, Alex Kendall, and Roberto Cipolla.       [18] Xinyu Huang, Peng Wang, Xinjing Cheng, Dingfu Zhou,
     SegNet: A deep convolutional encoder-decoder architec-              Qichuan Geng, and Ruigang Yang. The ApolloScape open
     ture for image segmentation. IEEE TIP, 39(12):2481–2495,            dataset for autonomous driving and its application. TPAMI,
     2017.                                                               42(10):2702–2719, 2020.
 [2] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio.            [19] Diederik P. Kingma and Jimmy Lei Ba. Adam: A method
     Neural machine translation by jointly learning to align and         for stochastic optimization. In ICLR, 2015.
     translate. In ICLR, 2015.                                      [20] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and
 [3] Irwan Bello, Barret Zoph, Ashish Vaswani, Jonathon Shlens,          Il Hong Suh. From big to small: Multi-scale local planar
     and Quoc V Le. Attention augmented convolutional net-               guidance for monocular depth estimation. arXiv preprint
     works. In ICCV, 2019.                                               arXiv:1907.10326, 2019.
 [4] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Sub-          [21] Zhengqi Li, Tali Dekel, Forrester Cole, Richard Tucker,
     biah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan,          Noah Snavely, Ce Liu, and William T. Freeman. Learning
     Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lan-             the depths of moving people by watching frozen people. In
     guage models are few-shot learners. In NeurIPS, 2020.               CVPR, 2019.
 [5] Vincent Casser, Soeren Pirk, Reza Mahjourian, and Anelia       [22] Zhengqi Li and Noah Snavely. MegaDepth: Learning single-
     Angelova. Unsupervised learning of depth and ego-motion:            view depth prediction from Internet photos. In CVPR, 2018.
     A structured approach. In AAAI, 2019.                          [23] Guosheng Lin, Anton Milan, Chunhua Shen, and Ian D.
 [6] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,              Reid. RefineNet: Multi-path refinement networks for high-
     Kevin Murphy, and Alan L. Yuille. DeepLab: Semantic im-             resolution semantic segmentation. In CVPR, 2017.
     age segmentation with deep convolutional nets, atrous con-     [24] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
     volution, and fully connected crfs. TPAMI, 40(4):834–848,           dar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke
     2018.                                                               Zettlemoyer, and Veselin Stoyanov. RoBERTa: A ro-
 [7] Liang-Chieh Chen, George Papandreou, Florian Schroff, and           bustly optimized BERT pretraining approach. arXiv preprint
     Hartwig Adam. Rethinking atrous convolution for seman-              arXiv:1907.11692, 2019.
     tic image segmentation. arXiv preprint arXiv:1706.05587,       [25] Dhruv Mahajan, Ross Girshick, Vignesh Ramanathan,
     2017.                                                               Kaiming He, Manohar Paluri, Yixuan Li, Ashwin Bharambe,
 [8] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo                 and Laurens van der Maaten. Exploring the limits of weakly
     Rehfeld, Markus Enzweiler, Rodrigo Benenson, Uwe                    supervised pretraining. In ECCV, 2018.
     Franke, Stefan Roth, and Bernt Schiele. The Cityscapes         [26] Roozbeh Mottaghi, Xianjie Chen, Xiaobai Liu, Nam-Gyu
     dataset for semantic urban scene understanding. In CVPR,            Cho, Seong-Whan Lee, Sanja Fidler, Raquel Urtasun, and
     2016.                                                               Alan L. Yuille. The role of context for object detection and
 [9] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,              semantic segmentation in the wild. In CVPR, 2014.
     and Fei-Fei Li. ImageNet: A large-scale hierarchical image     [27] Hyeonwoo Noh, Seunghoon Hong, and Bohyung Han.
     database. In CVPR, 2009.                                            Learning deconvolution network for semantic segmentation.
[10] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina              In ICCV, 2015.
     Toutanova. BERT: Pre-training of deep bidirectional trans-     [28] Niki Parmar, Ashish Vaswani, Jakob Uszkoreit, Lukasz
     formers for language understanding. In ACL, 2019.                   Kaiser, Noam Shazeer, Alexander Ku, and Dustin Tran. Im-
[11] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,              age transformer. In ICML, 2018.
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,            [29] Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-            Bello, Anselm Levskaya, and Jonathon Shlens. Stand-alone
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is          self-attention in vision models. In NeurIPS, 2019.
     worth 16x16 words: Transformers for image recognition at       [30] René Ranftl, Katrin Lasinger, David Hafner, Konrad
     scale. arXiv preprint arXiv:2010.11929, 2020.                       Schindler, and Vladlen Koltun. Towards robust monocular
[12] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map           depth estimation: Mixing datasets for zero-shot cross-dataset
     prediction from a single image using a multi-scale deep net-        transfer. TPAMI, 2020.
     work. In NeurIPS, 2014.                                        [31] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-
[13] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-                   Net: Convolutional networks for biomedical image segmen-
     manghelich, and Dacheng Tao. Deep ordinal regression net-           tation. In MICCAI, 2015.
     work for monocular depth estimation. In CVPR, 2018.            [32] Ozan Sener and Vladlen Koltun. Multi-task learning as
[14] Jun Fu, Jing Liu, Yuhang Wang, Yong Li, Yongjun Bao, Jin-           multi-objective optimization. In NeurIPS, 2018.
     hui Tang, and Hanqing Lu. Adaptive context network for         [33] Pierre Sermanet, David Eigen, Xiang Zhang, Michaël Math-
     scene parsing. In ICCV, 2019.                                       ieu, Rob Fergus, and Yann LeCun. OverFeat: Integrated
[15] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we             recognition, localization and detection using convolutional
     ready for autonomous driving? The KITTI vision benchmark            networks. In ICLR, 2014.
     suite. In CVPR, 2012.                                          [34] Evan Shelhamer, Jonathan Long, and Trevor Darrell. Fully
[16] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.              convolutional networks for semantic segmentation. CVPR,
     Deep residual learning for image recognition. In CVPR,              2015.
     2016.                                                          [35] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
     Fergus. Indoor segmentation and support inference from                CVPR, 2017.
     RGBD images. In ECCV, 2012.                                      [54] Bolei Zhou, Hang Zhao, Xavier Puig, Sanja Fidler, Adela
[36] Josef Sivic and Andrew Zisserman. Efficient visual search of          Barriuso, and Antonio Torralba. Scene parsing through
     videos cast as text retrieval. TPAMI, 31(4):591–606, 2009.            ADE20K dataset. In CVPR, 2017.
[37] Ke Sun, Bin Xiao, Dong Liu, and Jingdong Wang. Deep
     high-resolution representation learning for human pose esti-
     mation. In CVPR, 2019.
[38] Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco
     Massa, Alexandre Sablayrolles, and Hervé Jégou. Training
     data-efficient image transformers & distillation through at-
     tention. arXiv preprint arXiv:2012.12877, 2020.
[39] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     reit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia
     Polosukhin. Attention is all you need. In NeurIPS, 2017.
[40] Chaoyang Wang, Oliver Wang, Federico Perazzi, and Simon
     Lucey. Web stereo video supervision for depth prediction
     from dynamic scenes. In 3DV, 2019.
[41] Huiyu Wang, Yukun Zhu, Bradley Green, Hartwig Adam,
     Alan L. Yuille, and Liang-Chieh Chen. Axial-DeepLab:
     Stand-alone axial-attention for panoptic segmentation. In
     ECCV, 2020.
[42] Jingdong Wang, Ke Sun, Tianheng Cheng, Borui Jiang,
     Chaorui Deng, Yang Zhao, Dong Liu, Yadong Mu, Mingkui
     Tan, Xinggang Wang, Wenyu Liu, and Bin Xiao. Deep
     high-resolution representation learning for visual recogni-
     tion. TPAMI, 2020.
[43] Qiang Wang, Shizhen Zheng, Qingsong Yan, Fei Deng,
     Kaiyong Zhao, and Xiaowen Chu. IRS: A large synthetic
     indoor robotics stereo dataset for disparity and surface nor-
     mal estimation. arXiv preprint arXiv:1912.09678, 2019.
[44] Wenshan Wang, Delong Zhu, Xiangwei Wang, Yaoyu Hu,
     Yuheng Qiu, Chen Wang, Yafei Hu, Ashish Kapoor, and Se-
     bastian Scherer. TartanAir: A dataset to push the limits of
     visual slam. In IROS, 2020.
[45] Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, Yang Xiao,
     Ruibo Li, and Zhenbo Luo. Monocular relative depth per-
     ception with web stereo data supervision. In CVPR, 2018.
[46] Ke Xian, Jianming Zhang, Oliver Wang, Long Mai, Zhe Lin,
     and Zhiguo Cao. Structure-guided ranking loss for single
     image depth prediction. In CVPR, 2020.
[47] Yao Yao, Zixin Luo, Shiwei Li, Jingyang Zhang, Yufan
     Ren, Lei Zhou, Tian Fang, and Long Quan. BlendedMVS:
     A large-scale dataset for generalized multi-view stereo net-
     works. CVPR, 2020.
[48] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     forcing geometric constraints of virtual normal for depth pre-
     diction. In ICCV, 2019.
[49] Fisher Yu and Vladlen Koltun. Multi-scale context aggrega-
     tion by dilated convolutions. In ICLR, 2016.
[50] Yuhui Yuan, Xilin Chen, and Jingdong Wang. Object-
     contextual representations for semantic segmentation. In
     ECCV, 2020.
[51] Hang Zhang, Chongruo Wu, Zhongyue Zhang, Yi Zhu, Zhi
     Zhang, Haibin Lin, Yue Sun, Tong He, Jonas Muller, R.
     Manmatha, Mu Li, and Alexander Smola. ResNeSt: Split-
     attention networks. arXiv preprint arXiv:2004.08955, 2020.
[52] Hengshuang Zhao, Jiaya Jia, and Vladlen Koltun. Exploring
     self-attention for image recognition. In CVPR, 2020.
[53] Hengshuang Zhao, Jianping Shi, Xiaojuan Qi, Xiaogang
     Wang, and Jiaya Jia. Pyramid scene parsing network. In
                                           Supplementary Material

A. Architecture details                                             We observe more details and also better global depth ar-
                                                                    rangement in DPT predictions when compared to the fully-
   We provide additional technical details in this section.         convolutional baseline. Note that results for DPT and Mi-
Hybrid encoder. The hybrid encoder is based on a pre-               DaS are computed at the same input resolution (384 pixels).
activation ResNet50 with group norm and weight standard-            Semantic segmentation. We show per-class IoU scores for
ization [57]. It defines four stages after the initial stem, each   the ADE20K validation set in Figure A2. While we ob-
of which downsamples the representation before applying             serve a general trend of an improvement in per-class IoU in
multiple ResNet blocks. We refer by RN to the output of             comparison to the baseline [51], we do not observe a strong
the N -th stage. DPT-Hybrid thus taps skip connections af-          pattern across classes.
ter the first (R0) and second stage (R1).
                                                                    Attention maps. We show attention maps from different
Residual convolutional units. Figure A1 (a) shows a                 encoder layers in Figures A4 and A5. In both cases, we
schematic overview of the residual convolutional units [23]         show results from the monocular depth estimation models.
that are used in the decoder. Batch normalization is used for       We visualize the attention of two reference tokens (upper
semantic segmentation but is disabled for monocular depth           left corner and lower right corner, respectively) to all other
estimation. When using batch normalization, we disable bi-          tokens in the image across various layers in the encoder. We
ases in the preceding convolutional layer.                          show the average attention over all 12 attention heads.
Monocular depth estimation head. The output head for                    We observe the tendency that attention is spatially more
monocular depth estimation is shown in Figure A1 (b). The           localized close to the reference token in shallow layers (left-
initial convolution halves the feature dimensions, while the        most columns), whereas deeper layers (rightmost columns)
second convolution has an output dimension of 32. The fi-           frequently attend across the whole image.
nal linear layer projects this representation to a non-negative
scalar that represent the inverse depth prediction for every        References
pixel. Bilinear interpolation is used to upsample the repre-
                                                                    [55] D. J. Butler, J. Wulff, G. B. Stanley, and M. J. Black. A
sentation.
                                                                         naturalistic open source movie for optical flow evaluation.
Semantic segmentation head. The output head for seman-                   In ECCV, 2012.
tic segmentation is shown in Figure A1 (c). the first con-          [56] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
volutional block preserves the feature dimension, while the              ready for autonomous driving? The KITTI vision benchmark
final linear layer projects the representation to the number             suite. In CVPR, 2012.
of output classes. Dropout is used with a rate of 0.1. We           [57] Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Joan
                                                                         Puigcerver, Jessica Yung, Sylvain Gelly, and Neil Houlsby.
use bilinear interpolation for the final upsampling opera-
                                                                         Big transfer (bit): General visual representation learning. In
tion. The prediction thus represents the per-pixel logits of
                                                                         ECCV, 2020.
the classes.                                                        [58] Guosheng Lin, Anton Milan, Chunhua Shen, and Ian D.
                                                                         Reid. RefineNet: Multi-path refinement networks for high-
B. Additional results                                                    resolution semantic segmentation. In CVPR, 2017.
                                                                    [59] Thomas Schöps, Johannes L. Schönberger, Silvano Galliani,
    We provide additional qualitative and quantitative results           Torsten Sattler, Konrad Schindler, Marc Pollefeys, and An-
in this section.                                                         dreas Geiger. A multi-view stereo benchmark with high-
Monocular depth estimation. We notice that the biggest                   resolution images and multi-camera videos. In CVPR, 2017.
gains in performance for zero-shot transfer were achieved
for datasets that feature dense, high-resolution evalua-
tions [15, 55, 59]. This could be explained by more fine-
grained predictions. Visual inspection of sample results
(c.f . Figure A3) from these datasets confirms this intuition.
                                                                                     IoU

                                                                   0.0
                                                                         0.2
                                                                               0.4
                                                                                           0.6
                                                                                                 0.8
                                                               sky
                                                            bed
                                                   pool table
                                                           toilet
                                                               car
                                                      building
                                                            road
                                                        person
                                                        ceiling

                                                                                                                                                                                                           +
                                                            floor
                                               screen door
                                                             wall
                                                       curtain
                                                             tree
                                                                 tv
                                                      bathtub
                                                          towel
                                                              sea
                                                           hood

                                                                                                                                                                                                                                             ReLU
                                                                                                                                                                                                                                                                                ReLU
                                                             sink

                                                                                                                                                                                                                                Conv3x3
                                                                                                                                                                                                                                                                  Conv3x3

                                                                                                                                                                                                                    BatchNorm
                                                                                                                                                                                                                                                    BatchNorm
                                                         mirror
                                          projection screen
                                                refrigerator
                                                   computer
                                                     fireplace
                                                          stove
                                                            seat
                                                          water
                                                        picture
                                                     sidewalk
                                                               fan
                                                       window
                                                             sofa
                                                         bridge
                                          washing machine

                                                                                                                                                                    (a) Residual Convolutional Unit [23]
                                                              bus
                                                  motorbike
                                                 microwave
                                                          grass
                                                dishwasher
                                                               rug
                                                           lamp
                                                   mountain
                                                             tent
                                                       cabinet
                                           arcade machine
                                                           plate
                                                 skyscraper
                                                      radiator
                                                         house
                                                      cushion
                                                         barrel
                                                           chair
                                                        animal
                                                 countertop
                                                           table
                                                          pillow
                                                  chandelier
                                            swimming pool
                                                             lake
                                                           sand
                                                     fountain
                                                    sculpture
                                                            tank
                                                             ship
                                               coffee table
                                                           plant
                                                grandstand
                                                            light
                                                           book
                                                     waterfall
                                                                                                                                                                                                                                                                            Conv3x3

                                                           stool
                                                           palm
                                                                                                                                                                                                                                                    Resample0.5

                                                      airplane
                                                                                                                                                                                                               Conv1x1-ReLU
                                                                                                                                                                                                                                     Conv3x3-ReLU

                                                        sconce
                                                            case

                                      Class
                                             conveyer belt
                                                         cradle
                                                              van
                                                          chest
                                                    armchair
                                                       runway
                                                            vase
                                                            boat
                                                            door
                                                               pot
                                                        screen
                                                        basket
                                                                                                                          (b) Monocular depth estimation head

                                                               hut
                                                   trash can
                                                         flower
                                                            rock

Figure A2. Per class IoU on ADE20K.
                                                          fence
                                                            desk
                                             kitchen island
                                                           shelf
                                                              flag
                                                       ground
                                                      counter
                                                   bookcase
                                                             sign
                                                                                                                     Figure A1. Schematics of different architecture blocks.

                                                swivel chair
                                                       bicycle
                                                    dirt track
                                                         bench
                                                           oven
                                                       column
                                                            food
                                                          stairs
                                                         bottle
                                                             pier
                                                    staircase
                                                 traffic light
                                                  streetlight
                                                           clock
                                                           base
                                                         railing
                                                   wardrobe
                                                     ottoman
                                                       apparel
                                                                                                                                                                                                                                                    Dropout

                                                            path
                                                                                                                                                                                                                                     Conv1x1

                                                       canopy
                                                                                                                                                                                                               Resample0.5

                                                         buffet
                                                    escalator
                                                              box
                                                                                                                                                                                                                                                                            Conv3x3-BN-ReLU

                                                         brand
                                                            pole
                                                       awning
                                                      monitor
                                             bulletin board
                                                               toy
                                                               bar
                                                   bannister
                                                              bag
                                                            field
                                                                                                                                                                          (c) Semantic segmentation head

                                                            step
                                                         poster
                                                          stage
                                                              ball
                                                       blanket
                                                                hill
                                                           truck
                                                          tower
                                                           glass
                                                            river
                                                  crt screen
                                                          booth
                                                             tray
                                                                                                       DPT-Hybrid
                                                                                                       ResNeSt-200

                                                       shower
                                                            land
Input                          MiDaS (MIX 5)                                DPT-Large

        Figure A3. Additional comparisons for monocular depth estimation.
                      Input                              Prediction

                     Layer 6                             Layer 12                       Layer 18                       Layer 24
Upper left corner
Lower right corner

                      Input                              Prediction

                     Layer 6                             Layer 12                       Layer 18                       Layer 24
Upper left corner
Lower right corner

                               Figure A4. Sample attention maps of the DPT-Large monocular depth prediction network.
                      Input                             Prediction

                     Layer 3                             Layer 6                        Layer 9                        Layer 12
Upper left corner
Lower right corner

                      Input                             Prediction

                     Layer 3                             Layer 6                        Layer 9                        Layer 12
Upper left corner
Lower right corner

                              Figure A5. Sample attention maps of the DPT-Hybrid monocular depth prediction network.
