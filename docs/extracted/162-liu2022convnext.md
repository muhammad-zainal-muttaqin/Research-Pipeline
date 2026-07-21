---
source_id: 162
bibtex_key: liu2022convnext
title: A ConvNet for the 2020s
year: 2022
domain_theme: Fondasi RGB
verified_pdf: 162_ConvNeXt.pdf
char_count: 104173
---

A ConvNet for the 2020s

                                        Zhuang Liu1,2 * Hanzi Mao1 Chao-Yuan Wu1 Christoph Feichtenhofer1 Trevor Darrell2 Saining Xie1†
                                                                                1                                      2
                                                                                    Facebook AI Research (FAIR)            UC Berkeley
                                                                           Code: https://github.com/facebookresearch/ConvNeXt

                                                                    Abstract
arXiv:2201.03545v2 [cs.CV] 2 Mar 2022

                                           The “Roaring 20s” of visual recognition began with the
                                        introduction of Vision Transformers (ViTs), which quickly
                                        superseded ConvNets as the state-of-the-art image classifica-
                                        tion model. A vanilla ViT, on the other hand, faces difficulties
                                        when applied to general computer vision tasks such as object
                                        detection and semantic segmentation. It is the hierarchical
                                        Transformers (e.g., Swin Transformers) that reintroduced sev-
                                        eral ConvNet priors, making Transformers practically viable                                                       Diameter

                                                                                                                                                            4 8      16   256 GFLOPs
                                        as a generic vision backbone and demonstrating remarkable
                                        performance on a wide variety of vision tasks. However,
                                        the effectiveness of such hybrid approaches is still largely
                                        credited to the intrinsic superiority of Transformers, rather      Figure 1. ImageNet-1K classification results for • ConvNets and
                                        than the inherent inductive biases of convolutions. In this        ◦ vision Transformers. Each bubble’s area is proportional to FLOPs
                                        work, we reexamine the design spaces and test the limits of        of a variant in a model family. ImageNet-1K/22K models here
                                        what a pure ConvNet can achieve. We gradually “modernize”          take 2242 /3842 images respectively. ResNet and ViT results were
                                        a standard ResNet toward the design of a vision Transformer,       obtained with improved training procedures over the original papers.
                                        and discover several key components that contribute to the         We demonstrate that a standard ConvNet model can achieve the
                                        performance difference along the way. The outcome of this          same level of scalability as hierarchical vision Transformers while
                                        exploration is a family of pure ConvNet models dubbed Con-         being much simpler in design.
                                        vNeXt. Constructed entirely from standard ConvNet modules,         visual feature learning. The introduction of AlexNet [40]
                                        ConvNeXts compete favorably with Transformers in terms of          precipitated the “ImageNet moment” [59], ushering in a new
                                        accuracy and scalability, achieving 87.8% ImageNet top-1           era of computer vision. The field has since evolved at a
                                        accuracy and outperforming Swin Transformers on COCO               rapid speed. Representative ConvNets like VGGNet [64],
                                        detection and ADE20K segmentation, while maintaining the           Inceptions [68], ResNe(X)t [28, 87], DenseNet [36], Mo-
                                        simplicity and efficiency of standard ConvNets.                    bileNet [34], EfficientNet [71] and RegNet [54] focused on
                                                                                                           different aspects of accuracy, efficiency and scalability, and
                                                                                                           popularized many useful design principles.
                                        1. Introduction                                                        The full dominance of ConvNets in computer vision was
                                                                                                           not a coincidence: in many application scenarios, a “sliding
                                           Looking back at the 2010s, the decade was marked by
                                                                                                           window” strategy is intrinsic to visual processing, particu-
                                        the monumental progress and impact of deep learning. The
                                                                                                           larly when working with high-resolution images. ConvNets
                                        primary driver was the renaissance of neural networks, partic-
                                                                                                           have several built-in inductive biases that make them well-
                                        ularly convolutional neural networks (ConvNets). Through
                                                                                                           suited to a wide variety of computer vision applications. The
                                        the decade, the field of visual recognition successfully
                                                                                                           most important one is translation equivariance, which is a de-
                                        shifted from engineering features to designing (ConvNet)
                                                                                                           sirable property for tasks like objection detection. ConvNets
                                        architectures. Although the invention of back-propagation-
                                                                                                           are also inherently efficient due to the fact that when used in
                                        trained ConvNets dates all the way back to the 1980s [42],
                                                                                                           a sliding-window manner, the computations are shared [62].
                                        it was not until late 2012 that we saw its true potential for
                                                                                                           For many decades, this has been the default use of ConvNets,
                                           * Work done during an internship at Facebook AI Research.       generally on limited object categories such as digits [43],
                                           † Corresponding author.                                         faces [58, 76] and pedestrians [19, 63]. Entering the 2010s,
the region-based detectors [23, 24, 27, 57] further elevated       attributed to the superior scaling behavior of Transformers,
ConvNets to the position of being the fundamental building         with multi-head self-attention being the key component.
block in a visual recognition system.                                  Unlike ConvNets, which have progressively improved
    Around the same time, the odyssey of neural network            over the last decade, the adoption of Vision Transformers
design for natural language processing (NLP) took a very           was a step change. In recent literature, system-level com-
different path, as the Transformers replaced recurrent neural      parisons (e.g. a Swin Transformer vs. a ResNet) are usually
networks to become the dominant backbone architecture.             adopted when comparing the two. ConvNets and hierar-
Despite the disparity in the task of interest between language     chical vision Transformers become different and similar at
and vision domains, the two streams surprisingly converged         the same time: they are both equipped with similar induc-
in the year 2020, as the introduction of Vision Transformers       tive biases, but differ significantly in the training procedure
(ViT) completely altered the landscape of network architec-        and macro/micro-level architecture design. In this work,
ture design. Except for the initial “patchify” layer, which        we investigate the architectural distinctions between Con-
splits an image into a sequence of patches, ViT introduces no      vNets and Transformers and try to identify the confounding
image-specific inductive bias and makes minimal changes            variables when comparing the network performance. Our
to the original NLP Transformers. One primary focus of             research is intended to bridge the gap between the pre-ViT
ViT is on the scaling behavior: with the help of larger model      and post-ViT eras for ConvNets, as well as to test the limits
and dataset sizes, Transformers can outperform standard            of what a pure ConvNet can achieve.
ResNets by a significant margin. Those results on image                To do this, we start with a standard ResNet (e.g. ResNet-
classification tasks are inspiring, but computer vision is not     50) trained with an improved procedure. We gradually “mod-
limited to image classification. As discussed previously,          ernize” the architecture to the construction of a hierarchical
solutions to numerous computer vision tasks in the past            vision Transformer (e.g. Swin-T). Our exploration is directed
decade depended significantly on a sliding-window, fully-          by a key question: How do design decisions in Transformers
convolutional paradigm. Without the ConvNet inductive              impact ConvNets’ performance? We discover several key
biases, a vanilla ViT model faces many challenges in being         components that contribute to the performance difference
adopted as a generic vision backbone. The biggest chal-            along the way. As a result, we propose a family of pure
lenge is ViT’s global attention design, which has a quadratic      ConvNets dubbed ConvNeXt. We evaluate ConvNeXts on a
complexity with respect to the input size. This might be           variety of vision tasks such as ImageNet classification [17],
acceptable for ImageNet classification, but quickly becomes        object detection/segmentation on COCO [44], and semantic
intractable with higher-resolution inputs.                         segmentation on ADE20K [92]. Surprisingly, ConvNeXts,
    Hierarchical Transformers employ a hybrid approach to          constructed entirely from standard ConvNet modules, com-
bridge this gap. For example, the “sliding window” strategy        pete favorably with Transformers in terms of accuracy, scal-
(e.g. attention within local windows) was reintroduced to          ability and robustness across all major benchmarks. Con-
Transformers, allowing them to behave more similarly to            vNeXt maintains the efficiency of standard ConvNets, and
ConvNets. Swin Transformer [45] is a milestone work in this        the fully-convolutional nature for both training and testing
direction, demonstrating for the first time that Transformers      makes it extremely simple to implement.
can be adopted as a generic vision backbone and achieve                We hope the new observations and discussions can chal-
state-of-the-art performance across a range of computer vi-        lenge some common beliefs and encourage people to rethink
sion tasks beyond image classification. Swin Transformer’s         the importance of convolutions in computer vision.
success and rapid adoption also revealed one thing: the
essence of convolution is not becoming irrelevant; rather, it      2. Modernizing a ConvNet: a Roadmap
remains much desired and has never faded.                             In this section, we provide a trajectory going from a
    Under this perspective, many of the advancements of            ResNet to a ConvNet that bears a resemblance to Transform-
Transformers for computer vision have been aimed at bring-         ers. We consider two model sizes in terms of FLOPs, one is
ing back convolutions. These attempts, however, come               the ResNet-50 / Swin-T regime with FLOPs around 4.5×109
at a cost: a naive implementation of sliding window self-          and the other being ResNet-200 / Swin-B regime which has
attention can be expensive [55]; with advanced approaches          FLOPs around 15.0 × 109 . For simplicity, we will present
such as cyclic shifting [45], the speed can be optimized but       the results with the ResNet-50 / Swin-T complexity models.
the system becomes more sophisticated in design. On the            The conclusions for higher capacity models are consistent
other hand, it is almost ironic that a ConvNet already satisfies   and results can be found in Appendix C.
many of those desired properties, albeit in a straightforward,        At a high level, our explorations are directed to inves-
no-frills way. The only reason ConvNets appear to be losing        tigate and follow different levels of designs from a Swin
steam is that (hierarchical) Transformers surpass them in          Transformer while maintaining the network’s simplicity as
many vision tasks, and the performance difference is usually       a standard ConvNet. The roadmap of our exploration is as
                                                                            GFLOPs
   ResNet-50/200                    78.9
                                  78.8                                          4.1                  only did vision Transformers bring a new set of modules
                                         79.5
                                                                                                     and architectural design decisions, but they also introduced
                    stage ratio        79.4                                          4.5
   Macro                                                                                             different training techniques (e.g. AdamW optimizer) to vi-
   Design                                   79.5
                “patchify” stem            79.5                                      4.4
                                                                                                     sion. This pertains mostly to the optimization strategy and
                               78.5
                   depth conv 78.3                             78.9 2.4                              associated hyper-parameter settings. Thus, the first step
 ResNeXt
                       width ↑
                                                      80.4
                                                      80.5                                     5.3
                                                                                                     of our exploration is to train a baseline model with the vi-
  Inverted                                               80.7
                                                                                                     sion Transformer training procedure, in this case, ResNet-
                inverting dims                         80.6                              4.6
 Bottleneck                                                                                          50/200. Recent studies [7, 81] demonstrate that a set of
                                              79.8
               move ↑ d. conv                 79.9                                 4.1               modern training techniques can significantly enhance the
                                                     80.3
                kernel sz. → 5                       80.4                          4.1
                                                                                                     performance of a simple ResNet-50 model. In our study,
   Large
                                                        80.6                                         we use a training recipe that is close to DeiT’s [73] and
                kernel sz. → 7                         80.6                        4.2
   Kernel                                               80.6                                         Swin Transformer’s [45]. The training is extended to 300
                kernel sz. → 9                         80.6                        4.2               epochs from the original 90 epochs for ResNets. We use the
                                                        80.6
               kernel sz. → 11                        80.5                          4.3              AdamW optimizer [46], data augmentation techniques such
                                                             80.8
                                                                                                     as Mixup [90], Cutmix [89], RandAugment [14], Random
                 ReLU➝GELU                             80.6                        4.2
                                                                    81.2                             Erasing [91], and regularization schemes including Stochas-
              fewer activations                                  81.3              4.2               tic Depth [36] and Label Smoothing [69]. The complete set
                                                                    81.5
   Micro
   Design         fewer norms                                       81.4
                                                                       81.6
                                                                                   4.2               of hyper-parameters we use can be found in Appendix A.1.
                                                                                                     By itself, this enhanced training recipe increased the perfor-
                      BN ➝ LN                                        81.581.7      4.2

                sep. d.s. conv
                                                                                                     mance of the ResNet-50 model from 76.1% [1] to 78.8%
                                                                            82.0     4.5
    ConvNeXt-T/B                                                           81.8                      (+2.7%), implying that a significant portion of the perfor-
                                  …                                                                  mance difference between traditional ConvNets and vision
                                                                                                     Transformers may be due to the training techniques. We will
               Swin-T/B                                           81.3
                                                                 81.3                    4.5
                                                                                                     use this fixed training recipe with the same hyperparameters
                 ImageNet
                Top1 Acc (%)                                                                         throughout the “modernization” process. Each reported ac-
Figure 2. We modernize a standard ConvNet (ResNet) towards                                           curacy on the ResNet-50 regime is an average obtained from
the design of a hierarchical vision Transformer (Swin), without                                      training with three different random seeds.
introducing any attention-based modules. The foreground bars are
model accuracies in the ResNet-50/Swin-T FLOP regime; results                                        2.2. Macro Design
for the ResNet-200/Swin-B regime are shown with the gray bars. A
hatched bar means the modification is not adopted. Detailed results                                     We now analyze Swin Transformers’ macro network de-
for both regimes are in the appendix. Many Transformer archi-                                        sign. Swin Transformers follow ConvNets [28, 65] to use a
tectural choices can be incorporated in a ConvNet, and they lead                                     multi-stage design, where each stage has a different feature
to increasingly better performance. In the end, our pure ConvNet                                     map resolution. There are two interesting design considera-
model, named ConvNeXt, can outperform the Swin Transformer.                                          tions: the stage compute ratio, and the “stem cell” structure.

follows. Our starting point is a ResNet-50 model. We first                                           Changing stage compute ratio. The original design of the
train it with similar training techniques used to train vision                                       computation distribution across stages in ResNet was largely
Transformers and obtain much improved results compared to                                            empirical. The heavy “res4” stage was meant to be compat-
the original ResNet-50. This will be our baseline. We then                                           ible with downstream tasks like object detection, where a
study a series of design decisions which we summarized                                               detector head operates on the 14×14 feature plane. Swin-T,
as 1) macro design, 2) ResNeXt, 3) inverted bottleneck, 4)                                           on the other hand, followed the same principle but with a
large kernel size, and 5) various layer-wise micro designs. In                                       slightly different stage compute ratio of 1:1:3:1. For larger
Figure 2, we show the procedure and the results we are able                                          Swin Transformers, the ratio is 1:1:9:1. Following the de-
to achieve with each step of the “network modernization”.                                            sign, we adjust the number of blocks in each stage from
Since network complexity is closely correlated with the fi-                                          (3, 4, 6, 3) in ResNet-50 to (3, 3, 9, 3), which also aligns
nal performance, the FLOPs are roughly controlled over the                                           the FLOPs with Swin-T. This improves the model accuracy
course of the exploration, though at intermediate steps the                                          from 78.8% to 79.4%. Notably, researchers have thoroughly
FLOPs might be higher or lower than the reference models.                                            investigated the distribution of computation [53, 54], and a
All models are trained and evaluated on ImageNet-1K.                                                 more optimal design is likely to exist.
                                                                                                        From now on, we will use this stage compute ratio.
2.1. Training Techniques
                                                                                                     Changing stem to “Patchify”. Typically, the stem cell de-
    Apart from the design of the network architecture, the                                           sign is concerned with how the input images will be pro-
training procedure also affects the ultimate performance. Not                                        cessed at the network’s beginning. Due to the redundancy
inherent in natural images, a common stem cell will aggres-          1×1, 384➝96             1×1, 96➝384              d3×3, 96➝96
sively downsample the input images to an appropriate feature
map size in both standard ConvNets and vision Transformers.          d3×3, 96➝96            d3×3, 384➝384             1×1, 96➝384
The stem cell in standard ResNet contains a 7×7 convolution
layer with stride 2, followed by a max pool, which results           1×1, 96➝384             1×1, 384➝96              1×1, 384➝96
in a 4× downsampling of the input images. In vision Trans-
                                                                         (a)                      (b)                     (c)
formers, a more aggressive “patchify” strategy is used as
the stem cell, which corresponds to a large kernel size (e.g.    Figure 3. Block modifications and resulted specifications. (a) is
kernel size = 14 or 16) and non-overlapping convolution.         a ResNeXt block; in (b) we create an inverted bottleneck block and
Swin Transformer uses a similar “patchify” layer, but with       in (c) the position of the spatial depthwise conv layer is moved up.
a smaller patch size of 4 to accommodate the architecture’s
multi-stage design. We replace the ResNet-style stem cell        (see Figure 4). Interestingly, this Transformer design is con-
with a patchify layer implemented using a 4×4, stride 4 con-     nected to the inverted bottleneck design with an expansion
volutional layer. The accuracy has changed from 79.4% to         ratio of 4 used in ConvNets. The idea was popularized by
79.5%. This suggests that the stem cell in a ResNet may be       MobileNetV2 [61], and has subsequently gained traction in
substituted with a simpler “patchify” layer à la ViT which       several advanced ConvNet architectures [70, 71].
will result in similar performance.                                  Here we explore the inverted bottleneck design. Figure 3
   We will use the “patchify stem” (4×4 non-overlapping          (a) to (b) illustrate the configurations. Despite the increased
convolution) in the network.                                     FLOPs for the depthwise convolution layer, this change
                                                                 reduces the whole network FLOPs to 4.6G, due to the signif-
2.3. ResNeXt-ify                                                 icant FLOPs reduction in the downsampling residual blocks’
                                                                 shortcut 1×1 conv layer. Interestingly, this results in slightly
   In this part, we attempt to adopt the idea of ResNeXt [87],
                                                                 improved performance (80.5% to 80.6%). In the ResNet-200
which has a better FLOPs/accuracy trade-off than a vanilla
                                                                 / Swin-B regime, this step brings even more gain (81.9% to
ResNet. The core component is grouped convolution, where
                                                                 82.6%) also with reduced FLOPs.
the convolutional filters are separated into different groups.
                                                                     We will now use inverted bottlenecks.
At a high level, ResNeXt’s guiding principle is to “use more
groups, expand width”. More precisely, ResNeXt employs           2.5. Large Kernel Sizes
grouped convolution for the 3×3 conv layer in a bottleneck
                                                                    In this part of the exploration, we focus on the behav-
block. As this significantly reduces the FLOPs, the network
                                                                 ior of large convolutional kernels. One of the most distin-
width is expanded to compensate for the capacity loss.
                                                                 guishing aspects of vision Transformers is their non-local
   In our case we use depthwise convolution, a special case
                                                                 self-attention, which enables each layer to have a global
of grouped convolution where the number of groups equals
                                                                 receptive field. While large kernel sizes have been used in
the number of channels. Depthwise conv has been popular-
                                                                 the past with ConvNets [40, 68], the gold standard (popular-
ized by MobileNet [34] and Xception [11]. We note that
                                                                 ized by VGGNet [65]) is to stack small kernel-sized (3×3)
depthwise convolution is similar to the weighted sum op-
                                                                 conv layers, which have efficient hardware implementations
eration in self-attention, which operates on a per-channel
                                                                 on modern GPUs [41]. Although Swin Transformers rein-
basis, i.e., only mixing information in the spatial dimension.
                                                                 troduced the local window to the self-attention block, the
The combination of depthwise conv and 1 × 1 convs leads
                                                                 window size is at least 7×7, significantly larger than the
to a separation of spatial and channel mixing, a property
                                                                 ResNe(X)t kernel size of 3×3. Here we revisit the use of
shared by vision Transformers, where each operation either
                                                                 large kernel-sized convolutions for ConvNets.
mixes information across spatial or channel dimension, but
not both. The use of depthwise convolution effectively re-       Moving up depthwise conv layer. To explore large kernels,
duces the network FLOPs and, as expected, the accuracy.          one prerequisite is to move up the position of the depthwise
Following the strategy proposed in ResNeXt, we increase the      conv layer (Figure 3 (b) to (c)). That is a design decision
network width to the same number of channels as Swin-T’s         also evident in Transformers: the MSA block is placed prior
(from 64 to 96). This brings the network performance to          to the MLP layers. As we have an inverted bottleneck block,
80.5% with increased FLOPs (5.3G).                               this is a natural design choice — the complex/inefficient
   We will now employ the ResNeXt design.                        modules (MSA, large-kernel conv) will have fewer channels,
                                                                 while the efficient, dense 1×1 layers will do the heavy lifting.
2.4. Inverted Bottleneck                                         This intermediate step reduces the FLOPs to 4.1G, resulting
   One important design in every Transformer block is that it    in a temporary performance degradation to 79.9%.
creates an inverted bottleneck, i.e., the hidden dimension of    Increasing the kernel size. With all of these preparations,
the MLP block is four times wider than the input dimension       the benefit of adopting larger kernel-sized convolutions is sig-
nificant. We experimented with several kernel sizes, includ-       Swin Transformer Block
ing 3, 5, 7, 9, and 11. The network’s performance increases                           96-d
from 79.9% (3×3) to 80.6% (7×7), while the network’s                                  LN

FLOPs stay roughly the same. Additionally, we observe that                   1×1, 96×3
the benefit of larger kernel sizes reaches a saturation point at
7×7. We verified this behavior in the large capacity model              + rel. pos.    win. shift   ResNet Block       ConvNeXt Block
too: a ResNet-200 regime model does not exhibit further                 MSA, w7×7, H=3
gain when we increase the kernel size beyond 7×7.                                                           256-d               96-d

    We will use 7×7 depthwise conv in each block.                                                       1×1, 64             d7×7, 96
                                                                               1×1, 96
    At this point, we have concluded our examination of
                                                                                                            BN, ReLU             LN
network architectures on a macro scale. Intriguingly, a sig-
nificant portion of the design choices taken in a vision Trans-                                         3×3, 64             1×1, 384
                                                                                      96-d
former may be mapped to ConvNet instantiations.                                                             BN, ReLU            GELU
                                                                                      LN

2.6. Micro Design                                                                                       1×1, 256            1×1, 96
                                                                              1×1, 384
                                                                                                             BN
   In this section, we investigate several other architectural                        GELU
differences at a micro scale — most of the explorations here                                                 ReLU
are done at the layer level, focusing on specific choices of                   1×1, 96

activation functions and normalization layers.
Replacing ReLU with GELU One discrepancy between
NLP and vision architectures is the specifics of which ac-
tivation functions to use. Numerous activation functions           Figure 4. Block designs for a ResNet, a Swin Transformer, and a
have been developed over time, but the Rectified Linear Unit       ConvNeXt. Swin Transformer’s block is more sophisticated due to
(ReLU) [49] is still extensively used in ConvNets due to its       the presence of multiple specialized modules and two residual con-
simplicity and efficiency. ReLU is also used as an activation      nections. For simplicity, we note the linear layers in Transformer
                                                                   MLP blocks also as “1×1 convs” since they are equivalent.
function in the original Transformer paper [77]. The Gaus-
sian Error Linear Unit, or GELU [32], which can be thought
of as a smoother variant of ReLU, is utilized in the most          that we have even fewer normalization layers per block than
advanced Transformers, including Google’s BERT [18] and            Transformers, as empirically we find that adding one ad-
OpenAI’s GPT-2 [52], and, most recently, ViTs. We find             ditional BN layer at the beginning of the block does not
that ReLU can be substituted with GELU in our ConvNet              improve the performance.
too, although the accuracy stays unchanged (80.6%).                Substituting BN with LN. BatchNorm [38] is an essen-
Fewer activation functions. One minor distinction be-              tial component in ConvNets as it improves the convergence
tween a Transformer and a ResNet block is that Transform-          and reduces overfitting. However, BN also has many in-
ers have fewer activation functions. Consider a Transformer        tricacies that can have a detrimental effect on the model’s
block with key/query/value linear embedding layers, the pro-       performance [84]. There have been numerous attempts at
jection layer, and two linear layers in an MLP block. There        developing alternative normalization [60, 75, 83] techniques,
is only one activation function present in the MLP block. In       but BN has remained the preferred option in most vision
comparison, it is common practice to append an activation          tasks. On the other hand, the simpler Layer Normaliza-
function to each convolutional layer, including the 1 × 1          tion [5] (LN) has been used in Transformers, resulting in
convs. Here we examine how performance changes when                good performance across different application scenarios.
we stick to the same strategy. As depicted in Figure 4, we             Directly substituting LN for BN in the original ResNet
eliminate all GELU layers from the residual block except           will result in suboptimal performance [83]. With all the mod-
for one between two 1 × 1 layers, replicating the style of a       ifications in network architecture and training techniques,
Transformer block. This process improves the result by 0.7%        here we revisit the impact of using LN in place of BN. We
to 81.3%, practically matching the performance of Swin-T.          observe that our ConvNet model does not have any difficul-
    We will now use a single GELU activation in each block.        ties training with LN; in fact, the performance is slightly
                                                                   better, obtaining an accuracy of 81.5%.
Fewer normalization layers. Transformer blocks usually                 From now on, we will use one LayerNorm as our choice
have fewer normalization layers as well. Here we remove            of normalization in each residual block.
two BatchNorm (BN) layers, leaving only one BN layer
before the conv 1 × 1 layers. This further boosts the perfor-      Separate downsampling layers. In ResNet, the spatial
mance to 81.4%, already surpassing Swin-T’s result. Note           downsampling is achieved by the residual block at the start of
each stage, using 3×3 conv with stride 2 (and 1×1 conv with      • ConvNeXt-T: C = (96, 192, 384, 768), B = (3, 3, 9, 3)
stride 2 at the shortcut connection). In Swin Transformers, a    • ConvNeXt-S: C = (96, 192, 384, 768), B = (3, 3, 27, 3)
separate downsampling layer is added between stages. We          • ConvNeXt-B: C = (128, 256, 512, 1024), B = (3, 3, 27, 3)
explore a similar strategy in which we use 2×2 conv layers       • ConvNeXt-L: C = (192, 384, 768, 1536), B = (3, 3, 27, 3)
with stride 2 for spatial downsampling. This modification        • ConvNeXt-XL: C = (256, 512, 1024, 2048), B = (3, 3, 27, 3)
surprisingly leads to diverged training. Further investigation
shows that, adding normalization layers wherever spatial         3.1. Settings
resolution is changed can help stablize training. These in-         The ImageNet-1K dataset consists of 1000 object classes
clude several LN layers also used in Swin Transformers: one      with 1.2M training images. We report ImageNet-1K top-1
before each downsampling layer, one after the stem, and one      accuracy on the validation set. We also conduct pre-training
after the final global average pooling. We can improve the       on ImageNet-22K, a larger dataset of 21841 classes (a super-
accuracy to 82.0%, significantly exceeding Swin-T’s 81.3%.       set of the 1000 ImageNet-1K classes) with ∼14M images
    We will use separate downsampling layers. This brings        for pre-training, and then fine-tune the pre-trained model on
us to our final model, which we have dubbed ConvNeXt.            ImageNet-1K for evaluation. We summarize our training
    A comparison of ResNet, Swin, and ConvNeXt block struc-      setups below. More details can be found in Appendix A.
tures can be found in Figure 4. A comparison of ResNet-50,
Swin-T and ConvNeXt-T’s detailed architecture specifica-         Training on ImageNet-1K. We train ConvNeXts for 300
tions can be found in Table 9.                                   epochs using AdamW [46] with a learning rate of 4e-3.
                                                                 There is a 20-epoch linear warmup and a cosine decaying
Closing remarks. We have finished our first “playthrough”        schedule afterward. We use a batch size of 4096 and a
and discovered ConvNeXt, a pure ConvNet, that can outper-        weight decay of 0.05. For data augmentations, we adopt
form the Swin Transformer for ImageNet-1K classification         common schemes including Mixup [90], Cutmix [89], Ran-
in this compute regime. It is worth noting that all design       dAugment [14], and Random Erasing [91]. We regularize
choices discussed so far are adapted from vision Transform-      the networks with Stochastic Depth [37] and Label Smooth-
ers. In addition, these designs are not novel even in the        ing [69]. Layer Scale [74] of initial value 1e-6 is applied.
ConvNet literature — they have all been researched sepa-         We use Exponential Moving Average (EMA) [51] as we find
rately, but not collectively, over the last decade. Our Con-     it alleviates larger models’ overfitting.
vNeXt model has approximately the same FLOPs, #params.,          Pre-training on ImageNet-22K. We pre-train ConvNeXts
throughput, and memory use as the Swin Transformer, but          on ImageNet-22K for 90 epochs with a warmup of 5 epochs.
does not require specialized modules such as shifted window      We do not use EMA. Other settings follow ImageNet-1K.
attention or relative position biases.
   These findings are encouraging but not yet completely         Fine-tuning on ImageNet-1K. We fine-tune ImageNet-
convincing — our exploration thus far has been limited to        22K pre-trained models on ImageNet-1K for 30 epochs. We
a small scale, but vision Transformers’ scaling behavior is      use AdamW, a learning rate of 5e-5, cosine learning rate
what truly distinguishes them. Additionally, the question of     schedule, layer-wise learning rate decay [6, 12], no warmup,
whether a ConvNet can compete with Swin Transformers             a batch size of 512, and weight decay of 1e-8. The default
on downstream tasks such as object detection and semantic        pre-training, fine-tuning, and testing resolution is 2242 . Ad-
segmentation is a central concern for computer vision practi-    ditionally, we fine-tune at a larger resolution of 3842 , for
tioners. In the next section, we will scale up our ConvNeXt      both ImageNet-22K and ImageNet-1K pre-trained models.
models both in terms of data and model size, and evaluate            Compared with ViTs/Swin Transformers, ConvNeXts are
them on a diverse set of visual recognition tasks.               simpler to fine-tune at different resolutions, as the network
                                                                 is fully-convolutional and there is no need to adjust the input
                                                                 patch size or interpolate absolute/relative position biases.
3. Empirical Evaluations on ImageNet
                                                                 3.2. Results
   We construct different ConvNeXt variants, ConvNeXt-
T/S/B/L, to be of similar complexities to Swin-T/S/B/L [45].     ImageNet-1K. Table 1 (upper) shows the result compari-
ConvNeXt-T/B is the end product of the “modernizing” pro-        son with two recent Transformer variants, DeiT [73] and
cedure on ResNet-50/200 regime, respectively. In addition,       Swin Transformers [45], as well as two ConvNets from
we build a larger ConvNeXt-XL to further test the scalabil-      architecture search - RegNets [54], EfficientNets [71] and
ity of ConvNeXt. The variants only differ in the number          EfficientNetsV2 [72]. ConvNeXt competes favorably with
of channels C, and the number of blocks B in each stage.         two strong ConvNet baselines (RegNet [54] and Efficient-
Following both ResNets and Swin Transformers, the number         Net [71]) in terms of the accuracy-computation trade-off, as
of channels doubles at each new stage. We summarize the          well as the inference throughputs. ConvNeXt also outper-
configurations below:                                            forms Swin Transformer of similar complexities across the
                      image               throughput IN-1K             B over Swin-B becomes larger when the resolution increases
model                       #param. FLOPs
                       size               (image / s) top-1 acc.       from 2242 to 3842 . Additionally, we observe an improved
                      ImageNet-1K trained models                       result of 85.5% when further scaling to ConvNeXt-L.
• RegNetY-16G [54] 2242 84M 16.0G                     334.7   82.9
• EffNet-B7 [71]   6002 66M 37.0G                      55.1   84.3     ImageNet-22K. We present results with models fine-tuned
• EffNetV2-L [72] 4802 120M 53.0G                      83.7   85.7     from ImageNet-22K pre-training at Table 1 (lower). These
◦ DeiT-S [73]      2242 22M 4.6G                      978.5   79.8     experiments are important since a widely held view is that
◦ DeiT-B [73]      2242 87M 17.6G                     302.1   81.8     vision Transformers have fewer inductive biases thus can per-
◦ Swin-T           2242 28M 4.5G                      757.9   81.3     form better than ConvNets when pre-trained on a larger scale.
• ConvNeXt-T       2242 29M 4.5G                      774.7   82.1     Our results demonstrate that properly designed ConvNets
◦ Swin-S           2242 50M 8.7G                      436.7   83.0     are not inferior to vision Transformers when pre-trained
• ConvNeXt-S       2242 50M 8.7G                      447.1   83.1
                                                                       with large dataset — ConvNeXts still perform on par or
◦ Swin-B           2242 88M 15.4G                     286.6   83.5
• ConvNeXt-B       2242 89M 15.4G                     292.1   83.8
                                                                       better than similarly-sized Swin Transformers, with slightly
◦ Swin-B           3842 88M 47.1G                      85.1   84.5     higher throughput. Additionally, our ConvNeXt-XL model
• ConvNeXt-B       3842 89M 45.0G                     95.7    85.1     achieves an accuracy of 87.8% — a decent improvement
• ConvNeXt-L       2242 198M 34.4G                    146.8   84.3     over ConvNeXt-L at 3842 , demonstrating that ConvNeXts
• ConvNeXt-L       3842 198M 101.0G                   50.4    85.5     are scalable architectures.
                    ImageNet-22K pre-trained models                       On ImageNet-1K, EfficientNetV2-L, a searched architec-
• R-101x3 [39]      3842      388M 204.6G               -     84.4     ture equipped with advanced modules (such as Squeeze-and-
• R-152x4 [39]      4802      937M 840.5G               -     85.4     Excitation [35]) and progressive training procedure achieves
• EffNetV2-L [72] 4802        120M 53.0G               83.7   86.8     top performance. However, with ImageNet-22K pre-training,
• EffNetV2-XL [72] 4802       208M 94.0G               56.5   87.3     ConvNeXt is able to outperform EfficientNetV2, further
◦ ViT-B/16 (T) [67] 3842       87M 55.5G               93.1   85.4     demonstrating the importance of large-scale training.
◦ ViT-L/16 (T) [67] 3842      305M 191.1G              28.5   86.8
                                                                          In Appendix B, we discuss robustness and out-of-domain
• ConvNeXt-T        2242       29M 4.5G               774.7   82.9
                                                                       generalization results for ConvNeXt.
• ConvNeXt-T        3842       29M 13.1G              282.8   84.1
• ConvNeXt-S        2242       50M 8.7G               447.1   84.6     3.3. Isotropic ConvNeXt vs. ViT
• ConvNeXt-S        3842       50M 25.5G              163.5   85.8
◦ Swin-B            2242       88M 15.4G              286.6   85.2         In this ablation, we examine if our ConvNeXt block de-
• ConvNeXt-B        2242       89M 15.4G              292.1   85.8     sign is generalizable to ViT-style [20] isotropic architec-
◦ Swin-B            3842       88M 47.0G               85.1   86.4     tures which have no downsampling layers and keep the
• ConvNeXt-B        3842       89M 45.1G              95.7    86.8     same feature resolutions (e.g. 14×14) at all depths. We
◦ Swin-L            2242      197M 34.5G              145.0   86.3     construct isotropic ConvNeXt-S/B/L using the same feature
• ConvNeXt-L        2242      198M 34.4G              146.8   86.6
                                                                       dimensions as ViT-S/B/L (384/768/1024). Depths are set
◦ Swin-L            3842      197M 103.9G              46.0   87.3
• ConvNeXt-L        3842      198M 101.0G             50.4    87.5
                                                                       at 18/18/36 to match the number of parameters and FLOPs.
• ConvNeXt-XL       2242      350M 60.9G              89.3    87.0     The block structure remains the same (Fig. 4). We use the
• ConvNeXt-XL       3842      350M 179.0G             30.2    87.8     supervised training results from DeiT [73] for ViT-S/B and
                                                                       MAE [26] for ViT-L, as they employ improved training
Table 1. Classification accuracy on ImageNet-1K. Similar to            procedures over the original ViTs [20]. ConvNeXt models
Transformers, ConvNeXt also shows promising scaling behavior           are trained with the same settings as before, but with longer
with higher-capacity models and a larger (pre-training) dataset. In-   warmup epochs. Results for ImageNet-1K at 2242 resolution
ference throughput is measured on a V100 GPU, following [45]. On       are in Table 2. We observe ConvNeXt can perform generally
an A100 GPU, ConvNeXt can have a much higher throughput than           on par with ViT, showing that our ConvNeXt block design
Swin Transformer. See Appendix E. (T)ViT results with 90-epoch
                                                                       is competitive when used in non-hierarchical models.
AugReg [67] training, provided through personal communication
with the authors.
                                                                                                        throughput training IN-1K
                                                                       model             #param. FLOPs
                                                                                                        (image / s) mem. (GB) acc.
board, sometimes with a substantial margin (e.g. 0.8% for
                                                                       ◦ ViT-S              22M    4.6G    978.5       4.9    79.8
ConvNeXt-T). Without specialized modules such as shifted               • ConvNeXt-S (iso.) 22M     4.3G   1038.7       4.2    79.7
windows or relative position bias, ConvNeXts also enjoy                ◦ ViT-B              87M   17.6G    302.1       9.1    81.8
improved throughput compared to Swin Transformers.                     • ConvNeXt-B (iso.) 87M    16.9G    320.1       7.7    82.0
                                                                       ◦ ViT-L             304M   61.6G     93.1      22.5    82.6
   A highlight from the results is ConvNeXt-B at 3842 : it             • ConvNeXt-L (iso.) 306M   59.7G     94.4      20.4    82.6
outperforms Swin-B by 0.6% (85.1% vs. 84.5%), but with
12.5% higher inference throughput (95.7 vs. 85.1 image/s).             Table 2. Comparing isotropic ConvNeXt and ViT. Training
We note that the FLOPs/throughput advantage of ConvNeXt-               memory is measured on V100 GPUs with 32 per-GPU batch size.
backbone       FLOPs FPS APbox APbox  box
                                 50 AP75 AP
                                            mask APmask APmask
                                                   50     75               backbone            input crop. mIoU #param. FLOPs
                      Mask-RCNN 3× schedule                                                   ImageNet-1K pre-trained
◦ Swin-T        267G 23.1 46.0     68.1   50.3     41.6   65.1   44.9
                                                                           ◦ Swin-T                5122        45.8      60M    945G
• ConvNeXt-T    262G 25.6 46.2     67.9   50.8     41.7   65.0   44.9
                                                                           • ConvNeXt-T            5122        46.7      60M    939G
                   Cascade Mask-RCNN 3× schedule
• ResNet-50    739G 16.2    46.3   64.3   50.5     40.1   61.7   43.4
                                                                           ◦ Swin-S                5122        49.5      81M   1038G
• X101-32      819G 13.8    48.1   66.5   52.4     41.6   63.9   45.2      • ConvNeXt-S            5122        49.6      82M   1027G
• X101-64      972G 12.6    48.3   66.4   52.3     41.7   64.0   45.1      ◦ Swin-B                5122        49.7     121M   1188G
◦ Swin-T       745G 12.2    50.4   69.2   54.7     43.7   66.6   47.3      • ConvNeXt-B            5122        49.9     122M   1170G
• ConvNeXt-T   741G 13.5    50.4   69.1   54.8     43.7   66.5   47.3                    ImageNet-22K pre-trained
◦ Swin-S       838G 11.4    51.9   70.7   56.3     45.0   68.2   48.8      ◦ Swin-B‡               6402        51.7     121M   1841G
• ConvNeXt-S   827G 12.0    51.9   70.8   56.5     45.0   68.4   49.1      • ConvNeXt-B‡           6402        53.1     122M   1828G
◦ Swin-B       982G 10.7    51.9   70.5   56.4     45.0   68.1   48.9
                                                                           ◦ Swin-L‡               6402        53.5     234M   2468G
• ConvNeXt-B   964G 11.4    52.7   71.3   57.2     45.6   68.9   49.5
◦ Swin-B‡      982G 10.7    53.0   71.8   57.5     45.8   69.4   49.7
                                                                           • ConvNeXt-L‡           6402        53.7     235M   2458G
• ConvNeXt-B‡ 964G 11.5     54.0   73.1   58.8     46.9   70.6   51.3      • ConvNeXt-XL‡          6402        54.0     391M   3335G
◦ Swin-L‡      1382G 9.2    53.9   72.4   58.8     46.7   70.1   50.8
• ConvNeXt-L‡ 1354G 10.0    54.8   73.8   59.8     47.6   71.3   51.7   Table 4. ADE20K validation results using UperNet [85]. ‡ in-
• ConvNeXt-XL‡ 1898G 8.6    55.2   74.2   59.9     47.7   71.6   52.2
                                                                        dicates IN-22K pre-training. Swins’ results are from its GitHub
                                                                        repository [2]. Following Swin, we report mIoU results with multi-
Table 3. COCO object detection and segmentation results using
                                                                        scale testing. FLOPs are based on input sizes of (2048, 512) and
Mask-RCNN and Cascade Mask-RCNN. ‡ indicates that the model
                                                                        (2560, 640) for IN-1K and IN-22K pre-trained models, respectively.
is pre-trained on ImageNet-22K. ImageNet-1K pre-trained Swin
results are from their Github repository [3]. AP numbers of the
ResNet-50 and X101 models are from [45]. We measure FPS on
an A100 GPU. FLOPs are calculated with image size (1280, 800).          convolutions. It is natural to ask whether the design of
                                                                        ConvNeXt will render it practically inefficient. As demon-
                                                                        strated throughout the paper, the inference throughputs of
4. Empirical Evaluation on Downstream Tasks                             ConvNeXts are comparable to or exceed that of Swin Trans-
                                                                        formers. This is true for both classification and other tasks
Object detection and segmentation on COCO. We fine-                     requiring higher-resolution inputs (see Table 1,3 for com-
tune Mask R-CNN [27] and Cascade Mask R-CNN [9] on                      parisons of throughput/FPS). Furthermore, we notice that
the COCO dataset with ConvNeXt backbones. Following                     training ConvNeXts requires less memory than training Swin
Swin Transformer [45], we use multi-scale training, AdamW               Transformers. For example, training Cascade Mask-RCNN
optimizer, and a 3× schedule. Further details and hyper-                using ConvNeXt-B backbone consumes 17.4GB of peak
parameter settings can be found in Appendix A.3.                        memory with a per-GPU batch size of 2, while the reference
   Table 3 shows object detection and instance segmentation             number for Swin-B is 18.5GB. In comparison to vanilla ViT,
results comparing Swin Transformer, ConvNeXt, and tradi-                both ConvNeXt and Swin Transformer exhibit a more favor-
tional ConvNet such as ResNeXt. Across different model                  able accuracy-FLOPs trade-off due to the local computations.
complexities, ConvNeXt achieves on-par or better perfor-                It is worth noting that this improved efficiency is a result of
mance than Swin Transformer. When scaled up to bigger                   the ConvNet inductive bias, and is not directly related to the
models (ConvNeXt-B/L/XL) pre-trained on ImageNet-22K,                   self-attention mechanism in vision Transformers.
in many cases ConvNeXt is significantly better (e.g. +1.0 AP)
than Swin Transformers in terms of box and mask AP.                     5. Related Work
Semantic segmentation on ADE20K. We also evaluate                       Hybrid models. In both the pre- and post-ViT eras, the
ConvNeXt backbones on the ADE20K semantic segmen-                       hybrid model combining convolutions and self-attentions
tation task with UperNet [85]. All model variants are trained           has been actively studied. Prior to ViT, the focus was
for 160K iterations with a batch size of 16. Other experimen-           on augmenting a ConvNet with self-attention/non-local
tal settings follow [6] (see Appendix A.3 for more details).            modules [8, 55, 66, 79] to capture long-range dependen-
In Table 4, we report validation mIoU with multi-scale test-            cies. The original ViT [20] first studied a hybrid config-
ing. ConvNeXt models can achieve competitive performance                uration, and a large body of follow-up works focused on
across different model capacities, further validating the ef-           reintroducing convolutional priors to ViT, either in an ex-
fectiveness of our architecture design.                                 plicit [15, 16, 21, 82, 86, 88] or implicit [45] fashion.
Remarks on model efficiency. Under similar FLOPs, mod-                  Recent convolution-based approaches. Han et al. [25]
els with depthwise convolutions are known to be slower                  show that local Transformer attention is equivalent to in-
and consume more memory than ConvNets with only dense                   homogeneous dynamic depthwise conv. The MSA block in
Swin is then replaced with a dynamic or regular depthwise            For experiments in “modernizing a ConvNet” (Section 2),
convolution, achieving comparable performance to Swin.            we also use Table 5’s setting for ImageNet-1K, except EMA
A concurrent work ConvMixer [4] demonstrates that, in             is disabled, as we find using EMA severely hurts models
small-scale settings, depthwise convolution can be used as a      with BatchNorm layers.
promising mixing strategy. ConvMixer uses a smaller patch            For isotropic ConvNeXts (Section 3.3), the setting for
size to achieve the best results, making the throughput much      ImageNet-1K in Table A is also adopted, but warmup is ex-
lower than other baselines. GFNet [56] adopts Fast Fourier        tended to 50 epochs, and layer scale is disabled for isotropic
Transform (FFT) for token mixing. FFT is also a form of con-      ConvNeXt-S/B. The stochastic depth rates are 0.1/0.2/0.5
volution, but with a global kernel size and circular padding.     for isotropic ConvNeXt-S/B/L.
Unlike many recent Transformer or ConvNet designs, one
primary goal of our study is to provide an in-depth look at                                     ConvNeXt-T/S/B/L ConvNeXt-T/S/B/L/XL
the process of modernizing a standard ResNet and achieving                                         ImageNet-1K        ImageNet-22K
                                                                  (pre-)training config
state-of-the-art performance.                                                                           2242                2242
                                                                  weight init                   trunc. normal (0.2) trunc. normal (0.2)
                                                                  optimizer                           AdamW               AdamW
6. Conclusions                                                    base learning rate                     4e-3                4e-3
                                                                  weight decay                           0.05                0.05
   In the 2020s, vision Transformers, particularly hierar-        optimizer momentum            β1 , β2 =0.9, 0.999 β1 , β2 =0.9, 0.999
chical ones such as Swin Transformers, began to overtake          batch size                            4096                4096
ConvNets as the favored choice for generic vision backbones.      training epochs                        300                  90
                                                                  learning rate schedule            cosine decay        cosine decay
The widely held belief is that vision Transformers are more
                                                                  warmup epochs                           20                   5
accurate, efficient, and scalable than ConvNets. We propose       warmup schedule                       linear              linear
ConvNeXts, a pure ConvNet model that can compete favor-           layer-wise lr decay [6, 12]           None                None
ably with state-of-the-art hierarchical vision Transformers       randaugment [14]                     (9, 0.5)            (9, 0.5)
across multiple computer vision benchmarks, while retaining       mixup [90]                              0.8                 0.8
                                                                  cutmix [89]                             1.0                 1.0
the simplicity and efficiency of standard ConvNets. In some       random erasing [91]                    0.25                0.25
ways, our observations are surprising while our ConvNeXt          label smoothing [69]                    0.1                 0.1
model itself is not completely new — many design choices          stochastic depth [37]            0.1/0.4/0.5/0.5  0.0/0.0/0.1/0.1/0.2
have all been examined separately over the last decade, but       layer scale [74]                       1e-6                1e-6
                                                                  head init scale [74]                  None                None
not collectively. We hope that the new results reported in this   gradient clip                         None                None
study will challenge several widely held views and prompt         exp. mov. avg. (EMA) [51]            0.9999               None
people to rethink the importance of convolution in computer
vision.                                                           Table 5. ImageNet-1K/22K (pre-)training settings. Multiple
                                                                  stochastic depth rates (e.g., 0.1/0.4/0.5/0.5) are for each model
Acknowledgments. We thank Kaiming He, Eric Mintun,                (e.g., ConvNeXt-T/S/B/L) respectively.
Xingyi Zhou, Ross Girshick, and Yann LeCun for valuable
discussions and feedback.
                                                                  A.2. ImageNet Fine-tuning
Appendix
                                                                     We list the settings for fine-tuning on ImageNet-1K in
   In this Appendix, we provide further experimental details      Table 6. The fine-tuning starts from the final model weights
(§A), robustness evaluation results (§B), more modernization      obtained in pre-training, without using the EMA weights,
experiment results (§C), and a detailed network specification     even if in pre-training EMA is used and EMA accuracy is
(§D). We further benchmark model throughput on A100               reported. This is because we do not observe improvement if
GPUs (§E). Finally, we discuss the limitations (§F) and           we fine-tune with the EMA weights (consistent with observa-
societal impact (§G) of our work.                                 tions in [73]). The only exception is ConvNeXt-L pre-trained
                                                                  on ImageNet-1K, where the model accuracy is significantly
A. Experimental Settings                                          lower than the EMA accuracy due to overfitting, and we
                                                                  select its best EMA model during pre-training as the starting
A.1. ImageNet (Pre-)training                                      point for fine-tuning.
    We provide ConvNeXts’ ImageNet-1K training and                   In fine-tuning, we use layer-wise learning rate decay [6,
ImageNet-22K pre-training settings in Table 5. The settings       12] with every 3 consecutive blocks forming a group. When
are used for our main results in Table 1 (Section 3.2). All       the model is fine-tuned at 3842 resolution, we use a crop ratio
ConvNeXt variants use the same setting, except the stochas-       of 1.0 (i.e., no cropping) during testing following [2, 74, 80],
tic depth rate is customized for model variants.                  instead of 0.875 at 2242 .
                           ConvNeXt-B/L             ConvNeXt-T/S/B/L/XL     B. Robustness Evaluation
                             ImageNet-1K                ImageNet-22K
pre-training config
                                  2242                        2242             Additional robustness evaluation results for ConvNeXt
                             ImageNet-1K                 ImageNet-1K
fine-tuning config
                                  3842                  2242 and 3842
                                                                            models are presented in Table 8. We directly test our
optimizer                       AdamW                       AdamW           ImageNet-1K trained/fine-tuned classification models on sev-
base learning rate                5e-5                        5e-5          eral robustness benchmark datasets such as ImageNet-A [33],
weight decay                      1e-8                        1e-8          ImageNet-R [30], ImageNet-Sketch [78] and ImageNet-
optimizer momentum        β1 , β2 =0.9, 0.999        β1 , β2 =0.9, 0.999    C/C̄ [31, 48] datasets. We report mean corruption error
batch size                         512                         512
training epochs                    30                          30           (mCE) for ImageNet-C, corruption error for ImageNet-C̄,
learning rate schedule        cosine decay                cosine decay      and top-1 Accuracy for all other datasets.
layer-wise lr decay                0.7                         0.8             ConvNeXt (in particular the large-scale model variants)
warmup epochs                     None                        None          exhibits promising robustness behaviors, outperforming
warmup schedule                    N/A                         N/A
randaugment                      (9, 0.5)                    (9, 0.5)       state-of-the-art robust transformer models [47] on several
mixup                             None                        None          benchmarks. With extra ImageNet-22K data, ConvNeXt-
cutmix                            None                        None          XL demonstrates strong domain generalization capabilities
random erasing                    0.25                        0.25          (e.g. achieving 69.3%/68.2%/55.0% accuracy on ImageNet-
label smoothing                    0.1                         0.1
stochastic depth                0.8/0.95              0.0/0.1/0.2/0.3/0.4
                                                                            A/R/Sketch benchmarks, respectively). We note that these ro-
layer scale                    pre-trained                 pre-trained      bustness evaluation results were acquired without using any
head init scale                   0.001                       0.001         specialized modules or additional fine-tuning procedures.
gradient clip                     None                        None
exp. mov. avg. (EMA)              None              None(T-L)/0.9999(XL)     Model         Data/Size FLOPs / Params Clean C (↓) C̄ (↓)      A    R   SK
                                                                             ResNet-50     1K/2242      4.1 / 25.6    76.1   76.7   57.7   0.0 36.1 24.1
Table 6. ImageNet-1K fine-tuning settings. Multiple values (e.g.,
0.8/0.95) are for each model (e.g., ConvNeXt-B/L) respectively.              Swin-T [45]   1K/2242      4.5 / 28.3    81.2   62.0    -     21.6 41.3 29.1
                                                                             RVT-S* [47]   1K/2242      4.7 / 23.3    81.9   49.4   37.5   25.7 47.7 34.7
                                                                             ConvNeXt-T    1K/2242      4.5 / 28.6    82.1   53.2   40.0   24.2 47.2 33.8
                                                                             Swin-B [45]   1K/2242     15.4 / 87.8    83.4   54.4    -     35.8 46.6 32.4
A.3. Downstream Tasks                                                        RVT-B* [47]   1K/2242     17.7 / 91.8    82.6   46.8   30.8   28.5 48.7 36.0
                                                                             ConvNeXt-B    1K/2242     15.4 / 88.6    83.8   46.8   34.4   36.7 51.3 38.2
   For ADE20K and COCO experiments, we follow the                            ConvNeXt-B 22K/3842       45.1 / 88.6    86.8   43.1   30.7 62.3 64.9 51.6
training settings used in BEiT [6] and Swin [45]. We also                    ConvNeXt-L 22K/3842      101.0 / 197.8   87.5   40.2   29.9 65.5 66.7 52.8
use MMDetection [10] and MMSegmentation [13] toolboxes.                      ConvNeXt-XL 22K/3842     179.0 / 350.2   87.8   38.8   27.1 69.3 68.2 55.0
We use the final model weights (instead of EMA weights)
                                                                            Table 8. Robustness evaluation of ConvNeXt. We do not make
from ImageNet pre-training as network initializations.
                                                                            use of any specialized modules or additional fine-tuning procedures.
   We conduct a lightweight sweep for COCO experiments
including learning rate {1e-4, 2e-4}, layer-wise learning rate
decay [6] {0.7, 0.8, 0.9, 0.95}, and stochastic depth rate
{0.3, 0.4, 0.5, 0.6, 0.7, 0.8}. We fine-tune the ImageNet-22K               C. Modernizing ResNets: detailed results
pre-trained Swin-B/L on COCO using the same sweep. We                           Here we provide detailed tabulated results for the mod-
use the official code and pre-trained model weights [3].                    ernization experiments, at both ResNet-50 / Swin-T and
   The hyperparameters we sweep for ADE20K experiments                      ResNet-200 / Swin-B regimes. The ImageNet-1K top-1 ac-
include learning rate {8e-5, 1e-4}, layer-wise learning rate                curacies and FLOPs for each step are shown in Table 10
decay {0.8, 0.9}, and stochastic depth rate {0.3, 0.4, 0.5}.                and 11. ResNet-50 regime experiments are run with 3 ran-
We report validation mIoU results using multi-scale testing.                dom seeds.
Additional single-scale testing results are in Table 7.
                                                                                For ResNet-200, the initial number of blocks at each stage
               backbone              input crop. mIoU
                                                                            is (3, 24, 36, 3). We change it to Swin-B’s (3, 3, 27, 3) at
                         ImageNet-1K pre-trained
                                                                            the step of changing stage ratio. This drastically reduces the
               • ConvNeXt-T              5122         46.0                  FLOPs, so at the same time, we also increase the width from
               • ConvNeXt-S              5122         48.7                  64 to 84 to keep the FLOPs at a similar level. After the step
               • ConvNeXt-B              5122         49.1                  of adopting depthwise convolutions, we further increase the
                         ImageNet-22K pre-trained                           width to 128 (same as Swin-B’s) as a separate step.
               • ConvNeXt-B‡             6402         52.6                      The observations on the ResNet-200 regime are mostly
               • ConvNeXt-L‡             6402         53.2                  consistent with those on ResNet-50 as described in the main
               • ConvNeXt-XL‡            6402         53.6                  paper. One interesting difference is that inverting dimensions
                                                                            brings a larger improvement at ResNet-200 regime than at
 Table 7. ADE20K validation results with single-scale testing.              ResNet-50 regime (+0.79% vs. +0.14%). The performance
                            output size       • ResNet-50             • ConvNeXt-T                ◦ Swin-T
                                            7×7, 64, stride 2
                   stem       56×56                                4×4, 96, stride 4          4×4, 96, stride 4
                                          3×3 max pool, stride 2                                              
                                                                                         1×1, 96×3
                                               1×1, 64              d7×7, 96        MSA, w7×7, H=3, rel. pos.
                    res2      56×56           3×3, 64  × 3       1×1, 384 × 3                                ×2
                                                                                          1×1, 96 
                                              1×1, 256               1×1, 96                  1×1, 384
                                                                                              1×1, 96         
                                                                                        1×1, 192×3
                                              1×1, 128              d7×7, 192        MSA, w7×7, H=6, rel. pos.
                    res3      28×28          3×3, 128 × 4         1×1, 768  × 3                              ×2
                                                                                          1×1, 192 
                                              1×1, 512               1×1, 192                 1×1, 768
                                                                                             1×1, 192         
                                                                                        1×1, 384×3
                                              1×1, 256              d7×7, 384       MSA, w7×7, H=12, rel. pos.
                    res4      14×14          3×3, 256  × 6       1×1, 1536 × 9                               ×6
                                                                                          1×1, 384 
                                             1×1, 1024               1×1, 384                1×1, 1536
                                                                                             1×1, 384         
                                                                                        1×1,   768×3
                                              1×1, 512              d7×7, 768       MSA, w7×7, H=24, rel. pos.
                    res5       7×7           3×3, 512  × 3       1×1, 3072 × 3                               ×2
                                                                                          1×1, 768 
                                             1×1, 2048               1×1, 768                1×1, 3072
                                                                                              1×1, 768
                        FLOPs                    4.1 × 109            4.5 × 109                  4.5 × 109
                       # params.                 25.6 × 106           28.6 × 106                28.3 × 106

                           Table 9. Detailed architecture specifications for ResNet-50, ConvNeXt-T and Swin-T.

 model                                     IN-1K acc.        GFLOPs           model                               IN-1K acc.   GFLOPs
 ResNet-50 (PyTorch [1])                      76.13           4.09            ResNet-200 [29]                       78.20       15.01
 ResNet-50 (enhanced recipe)              78.82 ± 0.07        4.09            ResNet-200 (enhanced recipe)          81.14       15.01
 stage ratio                              79.36 ± 0.07        4.53            stage ratio and increase width        81.33       14.52
 “patchify” stem                          79.51 ± 0.18        4.42            “patchify” stem                       81.59       14.38
 depthwise conv                           78.28 ± 0.08        2.35            depthwise conv                        80.54        7.23
 increase width                           80.50 ± 0.02        5.27            increase width                        81.85       16.76
 inverting dimensions                     80.64 ± 0.03        4.64            inverting dimensions                  82.64       15.68
 move up depthwise conv                   79.92 ± 0.08        4.07            move up depthwise conv                82.04       14.63
 kernel size → 5                          80.35 ± 0.08        4.10            kernel size → 5                       82.32       14.70
 kernel size → 7                          80.57 ± 0.14        4.15            kernel size → 7                       82.30       14.81
 kernel size → 9                          80.57 ± 0.06        4.21            kernel size → 9                       82.27       14.95
 kernel size → 11                         80.47 ± 0.11        4.29            kernel size → 11                      82.18       15.13
 ReLU → GELU                              80.62 ± 0.14        4.15            ReLU → GELU                           82.19       14.81
 fewer activations                        81.27 ± 0.06        4.15            fewer activations                     82.71       14.81
 fewer norms                              81.41 ± 0.09        4.15            fewer norms                           83.17       14.81
 BN → LN                                  81.47 ± 0.09        4.46            BN → LN                               83.35       14.81
 separate d.s. conv (ConvNeXt-T)          81.97 ± 0.06        4.49            separate d.s. conv (ConvNeXt-B)       83.60       15.35
 Swin-T [45]                                  81.30           4.50            Swin-B [45]                           83.50       15.43

Table 10. Detailed results for modernizing a ResNet-50. Mean                   Table 11. Detailed results for modernizing a ResNet-200.
and standard deviation are obtained by training the network with
three different random seeds.
                                                                            D. Detailed Architectures
gained by increasing kernel size also seems to saturate at                     We present a detailed architecture comparison between
kernel size 5 instead of 7. Using fewer normalization layers                ResNet-50, ConvNeXt-T and Swin-T in Table 9. For differ-
also has a bigger gain compared with the ResNet-50 regime                   ently sized ConvNeXts, only the number of blocks and the
(+0.46% vs. +0.14%).                                                        number of channels at each stage differ from ConvNeXt-T
(see Section 3 for details). ConvNeXts enjoy the simplic-       feature interactions across many modalities. Additionally,
ity of standard ConvNets, but compete favorably with Swin       Transformers may be more flexible when used for tasks re-
Transformers in visual recognition.                             quiring discretized, sparse, or structured outputs. We believe
                                                                the architecture choice should meet the needs of the task at
E. Benchmarking on A100 GPUs                                    hand while striving for simplicity.
   Following Swin Transformer [45], the ImageNet models’
inference throughputs in Table 1 are benchmarked using a
                                                                G. Societal Impact
V100 GPU, where ConvNeXt is slightly faster in inference            In the 2020s, research on visual representation learn-
than Swin Transformer with a similar number of parameters.      ing began to place enormous demands on computing re-
We now benchmark them on the more advanced A100 GPUs,           sources. While larger models and datasets improve per-
which support the TensorFloat32 (TF32) tensor cores. We         formance across the board, they also introduce a slew of
employ PyTorch [50] version 1.10 to use the latest “Channel     challenges. ViT, Swin, and ConvNeXt all perform best with
Last” memory layout [22] for further speedup.                   their huge model variants. Investigating those model designs
   We present the results in Table 12. Swin Transformers and    inevitably results in an increase in carbon emissions. One
ConvNeXts both achieve faster inference throughput than         important direction, and a motivation for our paper, is to
V100 GPUs, but ConvNeXts’ advantage is now significantly        strive for simplicity — with more sophisticated modules,
greater, sometimes up to 49% faster. This preliminary study     the network’s design space expands enormously, obscuring
shows promising signals that ConvNeXt, employed with            critical components that contribute to the performance dif-
standard ConvNet modules and simple in design, could be         ference. Additionally, large models and datasets present
practically more efficient models on modern hardwares.          issues in terms of model robustness and fairness. Further
                                                                investigation on the robustness behavior of ConvNeXt vs.
              image        throughput     IN-1K / 22K           Transformer will be an interesting research direction. In
model               FLOPs
               size         (image / s) trained, 1K acc.        terms of data, our findings indicate that ConvNeXt models
◦ Swin-T       2242 4.5G      1325.6       81.3 / –             benefit from pre-training on large-scale datasets. While our
• ConvNeXt-T   2242 4.5G 1943.5 (+47%)     82.1 / –             method makes use of the publicly available ImageNet-22K
◦ Swin-S       2242 8.7G       857.3       83.0 / –             dataset, individuals may wish to acquire their own data for
• ConvNeXt-S   2242 8.7G 1275.3 (+49%)     83.1 / –
                                                                pre-training. A more circumspect and responsible approach
◦ Swin-B       2242 15.4G      662.8       83.5 / 85.2
                                                                to data selection is required to avoid potential concerns with
• ConvNeXt-B   2242 15.4G 969.0 (+46%)     83.8 / 85.8
◦ Swin-B       3842 47.1G      242.5       84.5 / 86.4          data biases.
• ConvNeXt-B   3842 45.0G 336.6 (+39%)     85.1 / 86.8
◦ Swin-L       2242 34.5G      435.9         – / 86.3           References
• ConvNeXt-L   2242 34.4G 611.5 (+40%)     84.3 / 86.6
◦ Swin-L       3842 103.9G     157.9         – / 87.3            [1] PyTorch Vision Models. https://pytorch.org/
• ConvNeXt-L   3842 101.0G 211.4 (+34%)    85.5 / 87.5               vision/stable/models.html. Accessed: 2021-10-
• ConvNeXt-XL 2242 60.9G       424.4         – / 87.0                01.
• ConvNeXt-XL 3842 179.0G      147.4         – / 87.8            [2] GitHub repository: Swin transformer. https://github.
                                                                     com/microsoft/Swin-Transformer, 2021.
Table 12. Inference throughput comparisons on an A100 GPU.       [3] GitHub repository: Swin transformer for object detection.
Using TF32 data format and “channel last” memory layout, Con-        https://github.com/SwinTransformer/Swin-
vNeXt enjoys up to ∼49% higher throughput compared with a            Transformer-Object-Detection, 2021.
Swin Transformer with similar FLOPs.                             [4] Anonymous. Patches are all you need? Openreview, 2021.
                                                                 [5] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton.
                                                                     Layer normalization. arXiv:1607.06450, 2016.
F. Limitations                                                   [6] Hangbo Bao, Li Dong, and Furu Wei. BEiT: BERT pre-
                                                                     training of image transformers. arXiv:2106.08254, 2021.
   We demonstrate ConvNeXt, a pure ConvNet model, can
                                                                 [7] Irwan Bello, William Fedus, Xianzhi Du, Ekin Dogus Cubuk,
perform as good as a hierarchical vision Transformer on              Aravind Srinivas, Tsung-Yi Lin, Jonathon Shlens, and Barret
image classification, object detection, instance and semantic        Zoph. Revisiting resnets: Improved training and scaling
segmentation tasks. While our goal is to offer a broad range         strategies. NeurIPS, 2021.
of evaluation tasks, we recognize computer vision applica-       [8] Irwan Bello, Barret Zoph, Ashish Vaswani, Jonathon Shlens,
tions are even more diverse. ConvNeXt may be more suited             and Quoc V Le. Attention augmented convolutional networks.
for certain tasks, while Transformers may be more flexible           In ICCV, 2019.
for others. A case in point is multi-modal learning, in which    [9] Zhaowei Cai and Nuno Vasconcelos. Cascade R-CNN: Delv-
a cross-attention module may be preferable for modeling              ing into high quality object detection. In CVPR, 2018.
[10] Kai Chen, Jiaqi Wang, Jiangmiao Pang, Yuhang Cao, Yu              [26] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr
     Xiong, Xiaoxiao Li, Shuyang Sun, Wansen Feng, Ziwei Liu,               Dollár, and Ross Girshick. Masked autoencoders are scalable
     Jiarui Xu, Zheng Zhang, Dazhi Cheng, Chenchen Zhu, Tian-               vision learners. arXiv:2111.06377, 2021.
     heng Cheng, Qijie Zhao, Buyu Li, Xin Lu, Rui Zhu, Yue             [27] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-
     Wu, Jifeng Dai, Jingdong Wang, Jianping Shi, Wanli Ouyang,             shick. Mask R-CNN. In ICCV, 2017.
     Chen Change Loy, and Dahua Lin. MMDetection: Open                 [28] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     mmlab detection toolbox and benchmark. arXiv:1906.07155,               Deep residual learning for image recognition. In CVPR, 2016.
     2019.                                                             [29] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
[11] François Chollet. Xception: Deep learning with depthwise               Identity mappings in deep residual networks. In ECCV, 2016.
     separable convolutions. In CVPR, 2017.                            [30] Dan Hendrycks, Steven Basart, Norman Mu, Saurav Kada-
[12] Kevin Clark, Minh-Thang Luong, Quoc V Le, and Christo-                 vath, Frank Wang, Evan Dorundo, Rahul Desai, Tyler Zhu,
     pher D Manning. ELECTRA: Pre-training text encoders as                 Samyak Parajuli, Mike Guo, et al. The many faces of robust-
     discriminators rather than generators. In ICLR, 2020.                  ness: A critical analysis of out-of-distribution generalization.
[13] MMSegmentation contributors. MMSegmentation: Openmm-                   In ICCV, 2021.
     lab semantic segmentation toolbox and benchmark. https:           [31] Dan Hendrycks and Thomas Dietterich. Benchmarking neural
     / / github . com / open - mmlab / mmsegmentation,                      network robustness to common corruptions and perturbations.
     2020.                                                                  In ICLR, 2018.
                                                                       [32] Dan Hendrycks and Kevin Gimpel. Gaussian error linear
[14] Ekin D Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V
                                                                            units (gelus). arXiv:1606.08415, 2016.
     Le. Randaugment: Practical automated data augmentation
                                                                       [33] Dan Hendrycks, Kevin Zhao, Steven Basart, Jacob Steinhardt,
     with a reduced search space. In CVPR Workshops, 2020.
                                                                            and Dawn Song. Natural adversarial examples. In CVPR,
[15] Zihang Dai, Hanxiao Liu, Quoc V Le, and Mingxing Tan.                  2021.
     Coatnet: Marrying convolution and attention for all data sizes.   [34] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry
     NeurIPS, 2021.                                                         Kalenichenko, Weijun Wang, Tobias Weyand, Marco An-
[16] Stéphane d’Ascoli, Hugo Touvron, Matthew Leavitt, Ari Mor-             dreetto, and Hartwig Adam. MobileNets: Efficient con-
     cos, Giulio Biroli, and Levent Sagun. ConViT: Improving                volutional neural networks for mobile vision applications.
     vision transformers with soft convolutional inductive biases.          arXiv:1704.04861, 2017.
     ICML, 2021.                                                       [35] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation
[17] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li          networks. In CVPR, 2018.
     Fei-Fei. ImageNet: A large-scale hierarchical image database.     [36] Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kil-
     In CVPR, 2009.                                                         ian Q Weinberger. Densely connected convolutional networks.
[18] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina                 In CVPR, 2017.
     Toutanova. BERT: Pre-training of deep bidirectional trans-        [37] Gao Huang, Yu Sun, Zhuang Liu, Daniel Sedra, and Kilian Q
     formers for language understanding. In NAACL, 2019.                    Weinberger. Deep networks with stochastic depth. In ECCV,
[19] Piotr Dollár, Serge Belongie, and Pietro Perona. The fastest           2016.
     pedestrian detector in the west. In BMVC, 2010.                   [38] Sergey Ioffe. Batch renormalization: Towards reducing mini-
[20] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                 batch dependence in batch-normalized models. In NeurIPS,
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,                    2017.
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-          [39] Alexander Kolesnikov, Lucas Beyer, Xiaohua Zhai, Joan
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is             Puigcerver, Jessica Yung, Sylvain Gelly, and Neil Houlsby.
     worth 16x16 words: Transformers for image recognition at               Big Transfer (BiT): General visual representation learning. In
     scale. In ICLR, 2021.                                                  ECCV, 2020.
                                                                       [40] Alex Krizhevsky, Ilya Sutskever, and Geoff Hinton. Imagenet
[21] Haoqi Fan, Bo Xiong, Karttikeya Mangalam, Yanghao Li,
                                                                            classification with deep convolutional neural networks. In
     Zhicheng Yan, Jitendra Malik, and Christoph Feichtenhofer.
                                                                            NeurIPS, 2012.
     Multiscale vision transformers. ICCV, 2021.
                                                                       [41] Andrew Lavin and Scott Gray. Fast algorithms for convolu-
[22] Vitaly Fedyunin. Tutorial: Channel last memory format
                                                                            tional neural networks. In CVPR, 2016.
     in PyTorch. https://pytorch.org/tutorials/
                                                                       [42] Yann LeCun, Bernhard Boser, John S Denker, Donnie Hen-
     intermediate/memory_format_tutorial.html,
                                                                            derson, Richard E Howard, Wayne Hubbard, and Lawrence D
     2021. Accessed: 2021-10-01.
                                                                            Jackel. Backpropagation applied to handwritten zip code
[23] Ross Girshick. Fast R-CNN. In ICCV, 2015.                              recognition. Neural computation, 1989.
[24] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra         [43] Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner,
     Malik. Rich feature hierarchies for accurate object detection          et al. Gradient-based learning applied to document recogni-
     and semantic segmentation. In CVPR, 2014.                              tion. Proceedings of the IEEE, 1998.
[25] Qi Han, Zejia Fan, Qi Dai, Lei Sun, Ming-Ming Cheng, Ji-          [44] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     aying Liu, and Jingdong Wang. Demystifying local vision                Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
     transformer: Sparse connectivity, weight sharing, and dy-              Zitnick. Microsoft COCO: Common objects in context. In
     namic weight. arXiv:2106.04263, 2021.                                  ECCV. 2014.
[45] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng          [63] Pierre Sermanet, Koray Kavukcuoglu, Soumith Chintala, and
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:               Yann LeCun. Pedestrian detection with unsupervised multi-
     Hierarchical vision transformer using shifted windows. 2021.         stage feature learning. In CVPR, 2013.
[46] Ilya Loshchilov and Frank Hutter. Decoupled weight decay        [64] Karen Simonyan and Andrew Zisserman. Two-stream convo-
     regularization. In ICLR, 2019.                                       lutional networks for action recognition in videos. In NeurIPS,
[47] Xiaofeng Mao, Gege Qi, Yuefeng Chen, Xiaodan Li, Ranjie              2014.
     Duan, Shaokai Ye, Yuan He, and Hui Xue. Towards robust          [65] Karen Simonyan and Andrew Zisserman. Very deep convolu-
     vision transformer. arXiv preprint arXiv:2105.07926, 2021.           tional networks for large-scale image recognition. In ICLR,
[48] Eric Mintun, Alexander Kirillov, and Saining Xie. On in-             2015.
     teraction between augmentations and corruptions in natural      [66] Aravind Srinivas, Tsung-Yi Lin, Niki Parmar, Jonathon
     corruption robustness. NeurIPS, 2021.                                Shlens, Pieter Abbeel, and Ashish Vaswani. Bottleneck trans-
                                                                          formers for visual recognition. In CVPR, 2021.
[49] Vinod Nair and Geoffrey E Hinton. Rectified linear units
                                                                     [67] Andreas Steiner, Alexander Kolesnikov, Xiaohua Zhai, Ross
     improve restricted boltzmann machines. In ICML, 2010.
                                                                          Wightman, Jakob Uszkoreit, and Lucas Beyer. How to train
[50] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer,                 your vit? data, augmentation, and regularization in vision
     James Bradbury, Gregory Chanan, Trevor Killeen, Zeming               transformers. arXiv preprint arXiv:2106.10270, 2021.
     Lin, Natalia Gimelshein, Luca Antiga, et al. PyTorch: An        [68] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet,
     imperative style, high-performance deep learning library. In         Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent
     NeurIPS, 2019.                                                       Vanhoucke, and Andrew Rabinovich. Going deeper with
[51] Boris T Polyak and Anatoli B Juditsky. Acceleration of               convolutions. In CVPR, 2015.
     stochastic approximation by averaging. SIAM Journal on          [69] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe,
     Control and Optimization, 1992.                                      Jonathon Shlens, and Zbigniew Wojna. Rethinking the incep-
[52] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario             tion architecture for computer vision. In CVPR, 2016.
     Amodei, and Ilya Sutskever. Language models are unsuper-        [70] Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan,
     vised multitask learners. 2019.                                      Mark Sandler, Andrew Howard, and Quoc V Le. Mnasnet:
[53] Ilija Radosavovic, Justin Johnson, Saining Xie, Wan-Yen              Platform-aware neural architecture search for mobile. In
     Lo, and Piotr Dollár. On network design spaces for visual            CVPR, 2019.
     recognition. In ICCV, 2019.                                     [71] Mingxing Tan and Quoc Le. Efficientnet: Rethinking model
[54] Ilija Radosavovic, Raj Prateek Kosaraju, Ross Girshick, Kaim-        scaling for convolutional neural networks. In ICML, 2019.
     ing He, and Piotr Dollár. Designing network design spaces.      [72] Mingxing Tan and Quoc Le. Efficientnetv2: Smaller models
     In CVPR, 2020.                                                       and faster training. In ICML, 2021.
[55] Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan         [73] Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco
     Bello, Anselm Levskaya, and Jonathon Shlens. Stand-alone             Massa, Alexandre Sablayrolles, and Hervé Jégou. Training
     self-attention in vision models. NeurIPS, 2019.                      data-efficient image transformers & distillation through atten-
[56] Yongming Rao, Wenliang Zhao, Zheng Zhu, Jiwen Lu, and                tion. arXiv:2012.12877, 2020.
     Jie Zhou. Global filter networks for image classification.      [74] Hugo Touvron, Matthieu Cord, Alexandre Sablayrolles,
     NeurIPS, 2021.                                                       Gabriel Synnaeve, and Hervé Jégou. Going deeper with
                                                                          image transformers. ICCV, 2021.
[57] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
                                                                     [75] Dmitry Ulyanov, Andrea Vedaldi, and Victor Lempitsky. In-
     Faster R-CNN: Towards real-time object detection with region
                                                                          stance normalization: The missing ingredient for fast styliza-
     proposal networks. In NeurIPS, 2015.
                                                                          tion. arXiv:1607.08022, 2016.
[58] Henry A Rowley, Shumeet Baluja, and Takeo Kanade. Neural
                                                                     [76] Régis Vaillant, Christophe Monrocq, and Yann Le Cun. Orig-
     network-based face detection. TPAMI, 1998.
                                                                          inal approach for the localisation of objects in images. Vision,
[59] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, San-            Image and Signal Processing, 1994.
     jeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy,         [77] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li          reit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia
     Fei-Fei. ImageNet Large Scale Visual Recognition Challenge.          Polosukhin. Attention is all you need. In NeurIPS, 2017.
     IJCV, 2015.                                                     [78] Haohan Wang, Songwei Ge, Eric P Xing, and Zachary C
[60] Tim Salimans and Diederik P Kingma. Weight normalization:            Lipton. Learning robust global representations by penalizing
     A simple reparameterization to accelerate training of deep           local predictive power. NeurIPS, 2019.
     neural networks. In NeurIPS, 2016.                              [79] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaiming
[61] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zh-                He. Non-local neural networks. In CVPR, 2018.
     moginov, and Liang-Chieh Chen. Mobilenetv2: Inverted            [80] Ross Wightman. GitHub repository: Pytorch image mod-
     residuals and linear bottlenecks. In CVPR, 2018.                     els. https://github.com/rwightman/pytorch-
[62] Pierre Sermanet, David Eigen, Xiang Zhang, Michael Math-             image-models, 2019.
     ieu, Rob Fergus, and Yann LeCun. Overfeat: Integrated           [81] Ross Wightman, Hugo Touvron, and Hervé Jégou. Resnet
     recognition, localization and detection using convolutional          strikes back: An improved training procedure in timm.
     networks. In ICLR, 2014.                                             arXiv:2110.00476, 2021.
[82] Haiping Wu, Bin Xiao, Noel Codella, Mengchen Liu, Xiyang
     Dai, Lu Yuan, and Lei Zhang. Cvt: Introducing convolutions
     to vision transformers. ICCV, 2021.
[83] Yuxin Wu and Kaiming He. Group normalization. In ECCV,
     2018.
[84] Yuxin Wu and Justin Johnson. Rethinking "batch" in batch-
     norm. arXiv:2105.07576, 2021.
[85] Tete Xiao, Yingcheng Liu, Bolei Zhou, Yuning Jiang, and
     Jian Sun. Unified perceptual parsing for scene understanding.
     In ECCV, 2018.
[86] Tete Xiao, Mannat Singh, Eric Mintun, Trevor Darrell, Piotr
     Dollár, and Ross Girshick. Early convolutions help transform-
     ers see better. In NeurIPS, 2021.
[87] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
     Kaiming He. Aggregated residual transformations for deep
     neural networks. In CVPR, 2017.
[88] Weijian Xu, Yifan Xu, Tyler Chang, and Zhuowen Tu. Co-
     scale conv-attentional image transformers. ICCV, 2021.
[89] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk
     Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regu-
     larization strategy to train strong classifiers with localizable
     features. In ICCV, 2019.
[90] Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and David
     Lopez-Paz. mixup: Beyond empirical risk minimization. In
     ICLR, 2018.
[91] Zhun Zhong, Liang Zheng, Guoliang Kang, Shaozi Li, and
     Yi Yang. Random erasing data augmentation. In AAAI, 2020.
[92] Bolei Zhou, Hang Zhao, Xavier Puig, Tete Xiao, Sanja Fidler,
     Adela Barriuso, and Antonio Torralba. Semantic understand-
     ing of scenes through the ADE20K dataset. IJCV, 2019.
