---
source_id: 176
bibtex_key: bhat2023zoedepth
title: ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth
year: 2023
domain_theme: Estimasi Kedalaman
verified_pdf: 176_ZoeDepth.pdf
char_count: 98524
---

ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth

                                              Shariq Farooq Bhat              Reiner Birkl           Diana Wofk             Peter Wonka            Matthias Müller
                                                   KAUST                         Intel                  Intel                 KAUST                     Intel
arXiv:2302.12288v1 [cs.CV] 23 Feb 2023

                                         Figure 1. Zero-shot transfer. Our single multi-domain metric depth estimation model can be applied across domains, indoor or outdoor,
                                         simulated or real. Top: Input RGB. Bottom: Predicted depth. From left to right: iBims-1, DIML Outdoor, Hypersim, DIODE Indoor,
                                         vKITTI2, SUN-RGBD, DIODE Outdoor and DDAD.

                                                                  Abstract                                    The code and pre-trained models are publicly available at
                                                                                                              https://github.com/isl-org/ZoeDepth.

                                             This paper tackles the problem of depth estimation from
                                         a single image. Existing work either focuses on gener-               1. Introduction
                                         alization performance disregarding metric scale, i.e. rel-
                                         ative depth estimation, or state-of-the-art results on spe-             Single-image depth estimation (SIDE) is a classic prob-
                                         cific datasets, i.e. metric depth estimation. We propose             lem in computer vision with many recent contributions.
                                         the first approach that combines both worlds, leading to             There are two branches of work: metric depth estimation
                                         a model with excellent generalization performance while              (MDE) and relative depth estimation (RDE). The dominant
                                         maintaining metric scale. Our flagship model, ZoeD-M12-              branch is MDE [5, 6, 26, 30, 50], where the goal is to es-
                                         NK, is pre-trained on 12 datasets using relative depth and           timate depth in absolute physical units, i.e. meters. The
                                         fine-tuned on two datasets using metric depth. We use a              advantage of predicting metric depth is the practical util-
                                         lightweight head with a novel bin adjustment design called           ity for many downstream applications in computer vision
                                         metric bins module for each domain. During inference,                and robotics, such as mapping, planning, navigation, object
                                         each input image is automatically routed to the appropri-            recognition, 3D reconstruction, and image editing. How-
                                         ate head using a latent classifier. Our framework admits             ever, training a single metric depth estimation model across
                                         multiple configurations depending on the datasets used for           multiple datasets often deteriorates the performance, espe-
                                         relative depth pre-training and metric fine-tuning. With-            cially when the collection includes images with large dif-
                                         out pre-training, we can already significantly improve the           ferences in depth scale, e.g. indoor and outdoor images.
                                         state of the art (SOTA) on the NYU Depth v2 indoor dataset.          As a result, current MDE models usually overfit to specific
                                         Pre-training on twelve datasets and fine-tuning on the NYU           datasets and do not generalize well to other datasets.
                                         Depth v2 indoor dataset, we can further improve SOTA for                The second branch of work, relative depth estima-
                                         a total of 21% in terms of relative absolute error (REL).            tion [30, 33], deals with the large depth scale variation in
                                         Finally, ZoeD-M12-NK is the first model that can jointly             multiple types of environments by factoring out the scale.
                                         train on multiple datasets (NYU Depth v2 and KITTI) with-            As a result, disparity is sufficient for supervision; metric
                                         out a significant drop in performance and achieve un-                scale and camera parameters are not required and do not
                                         precedented zero-shot generalization performance to eight            need to be consistent across datasets. In RDE, depth pre-
                                         unseen datasets from both indoor and outdoor domains.                dictions per pixel are only consistent relative to each other

                                                                                                          1
                                                                             MiDaS Depthmap
                                                                              Relative Depth
                                                Residual Connections
                                                                                                           Conv               LogBinomial
                                                                                   ×                       (1,1)                Softmax
                                                                                                                                            +
                                                                                    𝐻                              𝐻
                                          Encoder                Decoder
                                                                                                   𝐶+1                     𝑁!"#$
                                               MiDaS                                           𝑊                       𝑊

                                   BEiT

       RGB image                  Swin2                                                                                                         Zoe Depthmap
                                                                                       𝐻
                                                        Metric Bins Module                                                                       Metric Depth
                                                            (per pixel)
                                                                                                   𝑁!"#$
                                                                                               𝑊

Figure 2. ZoeDepth architecture. An RGB image is fed into the MiDaS depth estimation framework [33]. The bottleneck and succeeding
four hierarchy levels of the MiDaS decoder (at 1/32, 1/16, 1/8, 1/4 and 1/2 of the MiDaS in- and output resolution) are hooked into the
metric bins module (see Fig. 3). The metric bins module computes the per-pixel depth bin centers that are linearly combined to output the
metric depth. Different transformer backbones can be utilized for the MiDaS encoder; a state-of-the-art example is BEiT384 -L [3].

across image frames and the scale factor is unknown. This                                      Metric SIDE with relative depth pre-training. By
allows methods to be trained on a diverse set of scenes and                                conducting relative depth pre-training on 12 datasets and
datasets, even 3D movies [33], enabling model generaliz-                                   then conducting metric fine tuning on NYU Depth v2, our
ability across domains. The trade-off is that the predicted                                model ZoeD-M12-N can further improve on ZoeD-X-N by
depth has no metric meaning, limiting the applications.                                    8.5%, leading to 21% improvement over current published
    In this paper, we propose a two-stage framework that                                   SOTA. Existing architectures do not have an established
combines the two approaches (see Fig. 2). In the first                                     way to benefit from relative depth pre-training at a com-
stage, we train a common encoder-decoder architecture                                      petitive level.
for relative depth estimation using the standard training                                      Universal Metric SIDE with automatic routing. We
scheme [32]. Our model first learns from a large variety                                   make a step towards universal depth estimation in the wild.
of datasets in pre-training which leads to good generaliza-                                Our flagship architecture ZoeD-M12-NK uses relative pre-
tion. In the second stage, we add heads for metric depth es-                               training on 12 datasets combined with metric fine-tuning
timation to the encoder-decoder architecture and fine-tune                                 on indoor and outdoor datasets, i.e. NYU Depth v2 and
them on metric depth datasets, using one light-weight met-                                 KITTI, jointly. We evaluate this setup by first showing that
ric head per domain (a metric had has less than 1% of the                                  it significantly outperforms SOTA on datasets it was trained
parameters of the backbone). During inference, an image                                    on (NYU and KITTI) when compared to other models that
is automatically routed to the appropriate head using a clas-                              are also trained on these two datasets jointly; we achieve
sifier on encoder features. Adding these domain-specific                                   an overall improvement in absolute relative error (REL) of
heads helps the model learn metric depth while benefiting                                  24.3%. Second, our setup outperforms SOTA on 7 metric
from the relative depth pre-training. Our metric head de-                                  datasets it was not trained on, with up to 976.4% (∼11x) im-
sign (dubbed metric bins module) is inspired by a recently                                 provement in metrics; this demonstrates its unprecedented
introduced method for metric depth estimation [6] that esti-                               zero-shot capabilities.
mates a set of depth values instead of a single depth value
per pixel. Similarly, we estimate a set of depth values (bins)
                                                                                           2. Related Work
and subsequently transform this estimation at each layer of                                2.1. Single-Image Depth Estimation (SIDE)
the decoder using a novel concept we call attractors.
                                                                                              Supervised single-image depth estimation methods can
   Our framework is flexible and can be used in multi-                                     be categorized into regressing metric depth [5, 6, 16, 26, 30,
ple different configurations. We specifically want to high-                                50] and relative depth [21, 30, 32, 33]. Metric depth models
light three configurations, that improve the state-of-the-art                              are typically trained on singular datasets, are more prone
(SOTA) in different categories of metric SIDE. These three                                 to overfitting, and typically generalize poorly to unseen en-
configurations are the main contributions of this paper.                                   vironments or across varying depth ranges. Relative depth
   Metric SIDE. Without any relative pre-training, our                                     models tend to generalize better as they can be trained on
model ZoeD-X-N is trained only on NYU Depth v2 [37].                                       more diverse datasets with relative depth annotations us-
This configuration validates the design of our metric bins                                 ing scale-invariant losses. Yet, their utility for downstream
module and demonstrates that it can already improve upon                                   tasks requiring metric depth is limited, as relative depth
the current SOTA NeWCRFs [50] by 13.7% on indoor depth                                     models regress depth with unknown scale and shift. Re-
estimation without relative depth pre-training.                                            cent works have sought to resolve metric information in

                                                                                   2
regressed depth. For example, Yin et al. [49] recover 3D              3.1. Overview
scene shape from a single image via a two-stage framework
                                                                         We use the MiDaS [33] training strategy for relative
combining monocular depth estimation with 3D point cloud
                                                                      depth prediction. MiDaS uses a loss that is invariant to scale
encoders that are trained to predict missing depth shift and
                                                                      and shift. If multiple datasets are available, a multi-task loss
focal length. Jun et al. [16] decompose metric depth into
                                                                      that ensures pareto-optimality across the datasets is used.
normalized depth and scale features and propose a multi-
                                                                      The MiDaS training strategy can be applied to many differ-
decoder network where a metric depth decoder leverages
                                                                      ent network architectures. We use the DPT encoder-decoder
relative depth features from the gradient and normalized
                                                                      architecture as our base model [32], but replace the encoder
depth decoders. Universal depth prediction has also been
                                                                      with more recent transformer-based backbones [3]. After
investigated by the Robust Vision Challenge 1 that includes
                                                                      pre-training the MiDaS model for relative depth prediction,
indoor and outdoor domains. A popular idea is to dis-
                                                                      we add one or more heads for metric depth estimation by
cretize the target depth interval and reformulate the contin-
                                                                      attaching our proposed metric bins module to the decoder
uous depth regression as a classification task [11,23,24,34].
                                                                      (see Fig. 2 for the overall architecture). The metric bins
Ren et al. [34] propose a two-stage framework: first involv-
                                                                      module outputs metric depth and follows the adaptive bin-
ing training a classifier to distinguish low-depth-range and
                                                                      ning principle, originally introduced in [5] and subsequently
high-depth-range images. Two separate networks are then
                                                                      modified by [2,6,26,36]. In particular, we start out with the
trained for the respective depth ranges. We compare to the
                                                                      pixel-wise prediction design as in LocalBins [6] and pro-
best publicly available model based on DORN [11].
                                                                      pose modifications that further improve performance. Fi-
                                                                      nally, we fine-tune the complete architecture end-to-end.
2.2. Distribution learning for metric SIDE
                                                                      3.2. Architecture Details
    Many conventional learning-based monocular depth es-
                                                                         We first review LocalBins, and then introduce our novel
timation methods adopt encoder-decoder architectures with
                                                                      metric bins module with attractor layers, our bin aggrega-
convolutional layers, and more recently, transformer blocks.
                                                                      tion strategy, and loss function.
Depth estimation is commonly treated as a per-pixel regres-
sion task. An evolving line of work seeks to reformulate
depth estimation as a combined classification-regression              LocalBins review. Our metric bins module is inspired by
problem that reasons about distributions of depth values              the LocalBins architecture proposed in [6]. LocalBins uses
across an image. AdaBins [5] extends standard encoder-                a standard encoder-decoder as the base model and attaches a
decoder backbones with a transformer-based module that                module that takes the multi-scale features from the encoder-
discretizes predicted depth ranges into bins, where bin               decoder as input and predicts the bin centers at every pixel.
widths are determined adaptively per image; the final depth           Final depth at a pixel is obtained by a linear combination
estimation is computed as a linear combination of bin cen-            of the bin centers weighted by the corresponding predicted
ters. LocalBins [6] builds on this concept by considering             probabilities. The LocalBins module first predicts Nseed
depth distributions within local neighborhoods of a given             different seed bins at each pixel position at the bottleneck.
pixel instead of globally over the image, as well as com-             Each bin is then split into two at every decoder layer using
puting bin embeddings in a multi-scale fashion across de-             splitter MLPs. The number of bin centers is doubled at ev-
coder layers. PixelBins [36] simplifies AdaBins by replac-            ery decoder layer and we end up with 2n Nseed bins at each
ing transformer block with convolutions, reducing complex-            pixel at the end of n decoder layers. Simultaneously, the
ity. BinsFormer [26] incorporates an auxiliary scene clas-            probability scores (p) over Ntotal = 2n Nseed bin centers
sification query to guide bin generation and also utilizes            (c) are predicted from the decoder features using softmax
a multi-scale strategy to refine adaptively-generated bins.           and the final depth at pixel i is obtained using:
PixelFormer [2] treats depth estimation as pixel queries that                                     NX
                                                                                                   total

are refined via skip attention and that are used to predict bin                          d(i) =            pi (k)ci (k)           (1)
centers without leveraging decoded features.                                                       k=1

                                                                      Metric bins module. The metric bins module takes multi-
3. Methodology                                                        scale features from the MiDaS decoder as input and predicts
   In this section, we describe our architecture, design              the bin centers to be used for metric depth prediction (see
choices and training protocol in detail.                              Fig. 3). However, instead of starting with a small number
                                                                      of bins at the bottleneck and splitting them later, our metric
                                                                      bins module predicts all the bin centers at the bottleneck
  1 http://www.robustvision.net/                                      and adjusts them at subsequent decoder layers. This bin

                                                                  3
                                             Bin center                     tracting process while splitting is inherently dilative. Split-
 1    MLP                         MLP
 2
            +
                                                                            ting adds extra constraints of newly produced bins summing
                2x                                                          up to the original bin width, while attractors adjust freely
 1    MLP                         MLP         Attractor
                                                                            without such local constraints (only the total width is in-
            +

 4                                                                          variant). Intuitively, the prediction should get more refined
                2x      Bin
                     embeddings                                             and focused with decoder layers, which attractors achieve
 1    MLP                         MLP                                       without dealing with any local constraints.
            +

 8

                2x

1     MLP                         MLP                                       Log-binomial instead of softmax. To get the final met-
            +

16
                                                                            ric depth prediction, the bin centers are linearly combined,
                2x                                                          weighted by their probability scores as per Eq. (1). Prior
                                        Max depth          Min depth
1     MLP                         MLP                                       adaptive bins based models [2,5,6,26] use a softmax to pre-
32
                                                                            dict the probability distribution over the bin centers. The
                                                                            choice of softmax is mainly inspired from the discrete clas-
                                                                            sification analogy. Although the softmax plays well with
Figure 3. Metric Bins Module. Five incoming channels, corre-                unordered classes, since the bins are inherently ordered, it
sponding to different depth hierarchies (see Fig. 2), are converted
                                                                            intuitively makes sense to use an ordering-aware predic-
to 1-dimensional bin embeddings (green boxes) by MLPs, in com-
bination with upsampling and addition operations. The lowest bin
                                                                            tion of the probabilities. The softmax approach can re-
embedding yields metric bin centers (blue, vertical lines; not rep-         sult in vastly different probabilities for nearby bin centers
resentative of actual number 64), whereas the remaining embed-              (|pi − pi+1 | >> 0). Inspired by Beckham and Pal [4], we
dings provide attractors for their respective hierarchy levels (green       use a binomial distribution instead to address this issue and
dots). Going upwards in the metric bins module, the attractors pull         correctly consider ordinal relationships between bins.
the bin centers according to Eqs. (2) and (3).                                  The binomial distribution has one parameter q which
                                                                            controls the placement of the mode. We concatenate the
adjustment is implemented via our newly proposed building                   relative depth predictions with the decoder features and pre-
block, called attractor layers.                                             dict a 2-channel output (q - mode and t - temperature) from
                                                                            the decoder features to get the probability score over the k th
Attract instead of split. LocalBins implements multi-                       bin center by:
                                                                                                          
scale refinement of the bins by splitting them conditioned                                                 N k
                                                                                           p(k; N, q) =        q (1 − q)N −k           (4)
on the multi-scale features. In contrast, we implement the                                                 k
multi-scale refinement of the bins by adjusting them, mov-                  where N = Ntotal is the total number of bins. In prac-
ing them left or right on the depth interval. Using the multi-              tice, since we use large values of N , we take log (p),
scale features, we predict a set of points on the depth in-                 use Stirling’s approximation [1] for factorials and apply
terval towards which the bin centers get attracted. More                    softmax({log (pk )/t}N  k=1 ) to get normalized scores for nu-
specifically, at the lth decoder layer, an MLP takes the fea-               merical stability. The parameter t controls the temperature
tures at a pixel as input and predicts na attractor points                  of the resulting distribution. The softmax normalization
{ak : k = 1, ..., na } for that pixel position. The adjusted                preserves the unimodality of the logits. Finally, the result-
bin center is c0i = ci + ∆ci , with the adjustment given by:                ing probability scores and the bin centers from the metric
                          na                                                bins module are used to obtain the final depth as per Eq. (1).
                          X       ak − ci
                  ∆ci =                                   (2)
                             1 + α|ak − ci |γ
                                  k=1
where the hyperparameters α and γ determine the attractor                   Loss. We use the scale-invariant log loss (Lpixel ) for
strength. We name this attractor variant inverse attractor.                 pixel-level supervision as in LocalBins [6]. Unlike Local-
We also experiment with an exponential variant given by:                    Bins, we do not use the chamfer loss for bins due to the high
                    na                                                      memory requirement but only limited improvement.
                   X                         γ
            ∆ci =      (ak − ci )e−α|ak −ci |           (3)
                                                                            3.3. Training strategies
                          k=1
    Our experiments suggest that the inverse attractor leads                   As described previously, we have two stages for train-
to better performance. We let the number of attractor points                ing: relative depth pre-training for the MiDaS backbone
vary from one decoder layer to another, denoted together                    and metric depth fine-tuning for the prediction heads. We
as a set {nla }. We use Ntotal = 64 bins and {16, 8, 4, 1}                  compare models with and without pre-training for relative
attractors. Please refer to Sec. 5.4 for various ablations.                 depth as in [33]. We also explore different variations of
    The attracting strategy is preferred because it’s a con-                fine-tuning, using a single dataset and multiple datasets; in

                                                                        4
the case of multiple datasets, we also compare using a sin-         the 10 datasets used in [32]: HRWSI [46], Blend-
gle head, i.e. metric bins module, to using multiple heads.         edMVS [47], ReDWeb [45], DIML-Indoor [17], 3D
Please refer to Sec. 4.2 for more details about the exact           Movies [33], MegaDepth [25], WSVD [41], TartanAir [43],
model definitions. In the supplement, we report results for         ApolloScape [15] and IRS [42], plus 2 additional datasets:
additional variations.                                              KITTI [29] and NYU Depth v2 [37].
                                                                       To demonstrate generalizability, we evaluate zero-shot
Metric fine-tuning on multiple datasets Training a met-             performance on a number of real-world and synthetic
ric depth model on a mixture of datasets with a wide variety        datasets: SUN RGB-D [38], iBims [18], DIODE In-
of scenes, for example from indoor and outdoor domains,             door [40] and HyperSim [35] for the indoor domain;
is hard. The model not only has to handle images taken              DDAD [12], DIML Outdoor [17], DIODE Outdoor [40] and
with different cameras and camera settings but also has to          Virtual KITTI 2 [7] for the outdoor domain. We provide fur-
learn to adjust for the large variations in the overall scale       ther details about the datasets in the supplement.
of the scenes. Indoor scenes are usually limited to a maxi-         4.2. Models
mum depth of 10 meters while outdoor scenes can have in-
finite depth (capped at 80 meters in most prior works). We             The models are named according to the following con-
hypothesize that a backbone pre-trained for relative depth          vention: ZoeD-{RDPT}-{MFT}, where ZoeD is the ab-
estimation, alleviates the issues of fine-tuning on multiple        breviation for ZoeDepth, RDPT denotes the datasets used
datasets to some extent. We can also equip the model with           for relative depth pre-training (X denotes no pre-training)
multiple metric bins modules, one for each scene type (in-          and MFT denotes the datasets used for metric depth fine-
door versus outdoor). Different metric heads can be thought         tuning. We train and evaluate the following models: ZoeD-
of as scene-type experts. Note that the base model is still         X-N, ZoeD-X-K, ZoeD-M12-N, ZoeD-M12-K and ZoeD-
common to all metric heads; the complete model with mul-            M12-NK. All models use the BEiT384 -L backbone from
tiple heads is trained end-to-end. See Sec. 5.2 for a compar-       timm [44] that was pre-trained on ImageNet. The models
ison of our model with single head and multiple heads.              ZoeD-X-N and ZoeD-X-K are directly fine-tuned for metric
                                                                    depth on NYU Depth v2 and KITTI respectively without
                                                                    any pre-training for relative depth estimation. ZoeD-M12-N
Routing to metric heads. When the model has multiple
                                                                    and ZoeD-M12-K additionally include pre-training for rel-
metric heads, we need a router that chooses the metric head
                                                                    ative depth estimation on the M12 dataset mix before the
to use for a particular input. We employ commonly used
                                                                    fine-tuning stage for metric depth. ZoeD-M12-NK is also
routing mechanisms developed in other contexts, e.g., see
                                                                    pre-trained on M12, but has two separate heads fine-tuned
Fedus et al. [10] for a review. We explore three main vari-
                                                                    on both NYU Depth v2 and KITTI. ZoeD-M12-NK† is a
ants: (R.1) Labeled Router: In this variant, we provide
                                                                    variant of this model with a single head but otherwise the
scene type labels (indoor or outdoor) to the model at both
                                                                    same pre-training and fine-tuning procedure. In the supple-
training and inference times and manually map from the
                                                                    ment, we provide further results for models trained on addi-
scene type to the metric head. (R.2) Trained Router: Here,
                                                                    tional dataset combinations in pre-training and fine-tuning.
we train a classifier MLP that predicts the scene type of
the input image based on the bottleneck features and then           4.3. Evaluation Metrics
routes to the corresponding metric head. Therefore, this
variant only needs scene-type labels during training. (R.3)              We evaluate in metric depth space P    d by computing the
                                                                                                            1     M |d − d̂ |/d ,
Auto Router: In this setting, a router MLP (equivalent to           absolute relative error (REL) = M             i=1 P i       i   i
                                                                                                                     1      M |d −
a classifier in R.2) is used, but no labels are provided dur-       the root mean squared error (RMSE) = [ M                i=1   i
                                                                             1                                 1
                                                                    d̂i |2 ] 2 , the average log10 error = M
                                                                                                                 PM
ing either training or inference. Both the trainable router                                                         i=1 | log10 di −
types, Trained Router and Auto Router, are trained end-to-          log10 d̂i |, and the threshold accuracy δn = % of pixels
end with the whole model. See Sec. 5.4 for a performance            s.t. max (di /d̂i , d̂i /di ) < 1.25n for n = 1, 2, 3, where di
comparison of the discussed routing mechanisms.                     and d̂i refer to ground truth and predicted depth at pixel i,
                                                                    respectively, and M is the total number of pixels in the im-
4. Experimental Setup                                               age. We cap the evaluation depth at 10m for indoor datasets
                                                                    (8m for SUN RGB-D) and at 80m for outdoor datasets. Fi-
4.1. Datasets
                                                                    nal model outputs are computed as the average of an im-
   Our primary datasets for training ZoeDepth are NYU               age’s depth prediction and the prediction of its mirror image
Depth v2 (N) for indoor and KITTI (K) for outdoor                   and are evaluated at ground truth resolution.
scenes. We refer to the combination of both datasets                     In addition, we define two metrics to measure relative
as (NK). For pre-training the relative depth backbone,              improvement (RI) across datasets and metrics respectively.
we train on a mix of 12 datasets (M12) consisting of                For M datasets Di with i ∈ [1, M ], we compute mRID =

                                                                5
                Input              Ground Truth       NeWCRFs [50]           Ours              NeWCRFs ∆           Ours ∆
Figure 4. Qualitative comparison on NYU Depth v2. Our method consistently produces better predictions with much less error. When
looking closely at the depth maps it can also be observed that our predictions are much sharper with clear edges. ∆ indicates square error
ranging from lowest (dark blue) to highest (dark red) across predictions. Invalid regions are indicated as grey.

1
    PM
M     i=1 RIDi . Similarly, for N metrics θj with j ∈ [1, N ],             not pre-trained for relative depth; the backbone is initial-
                             PN
we compute mRIθ = N1 j=1 RIθi . For metrics where                          ized with the standard weights from ImageNet pre-training.
lower is better, RI = r−t                                                  Tab. 1 shows the performance of models on the official
                         r and for metrics where higher is
better RI = t−r                                                            NYU Depth v2 test set. This model already outperforms
              r , where r and t correspond to the reference
and target scores respectively.                                            NeWCRFs [50] by 13.7% (REL = 0.082), highlighting the
                                                                           contribution of our architecture design.
5. Results                                                                     Next, we verify that our architecture can benefit from rel-
                                                                           ative depth pre-training. Our corresponding model ZoeD-
5.1. Comparison to SOTA on NYU Depth V2                                    M12-N significantly outperforms the prior state-of-the-art
                                                                           NeWCRFs [50] by nearly 21% (REL = 0.075). Results are
   Our novel architecture beats SOTA without using any
                                                                           not just numerically better; the resulting depth maps also
additional data for pre-training. To demonstrate this, we
                                                                           have much sharper boundaries (see Fig. 4). We believe this
evaluate our model ZoeD-X-N on the popular metric depth
                                                                           is the first demonstration of successful relative depth pre-
estimation benchmark NYU Depth v2 [37]. ZoeD-X-N is
                                                                           training at a competitive level. While other architectures
                                                                           can also benefit from pre-training, some modifications are
Method              δ1 ↑    δ2 ↑      δ3 ↑    REL ↓   RMSE ↓ log10 ↓       required. In the next section, we show one such modifica-
                                                                           tion by combining our base model with architecture build-
Eigen et al. [9]    0.769   0.950     0.988   0.158   0.641     –
Laina et al. [19]   0.811   0.953     0.988   0.127   0.573   0.055        ing blocks proposed by other papers (see Tab. 2). This
Hao et al. [13]     0.841   0.966     0.991   0.127   0.555   0.053        shows that while other architectures benefit from our larger
DORN [11]           0.828   0.965     0.992   0.115   0.509   0.051        backbone and relative depth pre-training, they are still not
SharpNet [31]       0.836   0.966     0.993   0.139   0.502   0.047
Hu et al. [14]      0.866   0.975     0.993   0.115   0.530   0.050
                                                                           competitive with our complete framework.
Lee et al. [22]     0.837   0.971     0.994   0.131   0.538     –
Chen et al. [8]     0.878   0.977     0.994   0.111   0.514   0.048        5.2. Universal Metric SIDE
BTS [20]            0.885   0.978     0.994   0.110   0.392   0.047
Yin et al. [48]     0.875   0.976     0.994   0.108   0.416   0.048           Here, we evaluate our progress towards a universal met-
AdaBins [5]         0.903   0.984     0.997   0.103   0.364   0.044        ric depth estimation framework by analyzing our model
LocalBins [6]       0.907   0.987     0.998   0.099   0.357   0.042
Jun et al. [16]     0.913   0.987     0.998   0.098   0.355   0.042
                                                                           ZoeD-M12-NK which was trained across two different
NeWCRFs [50]        0.922   0.992     0.998   0.095   0.334   0.041        metric datasets and generalizes across indoor and out-
ZoeD-X-N            0.946   0.994     0.999   0.082   0.294   0.035
                                                                           door domains. Models trained across multiple metric
ZoeD-M12-N          0.955   0.995     0.999   0.075   0.270   0.032        datasets usually perform worse or diverge. In contrast, our
ZoeD-M12-NK         0.953   0.995     0.999   0.077   0.277   0.033
                                                                           model ZoeD-M12-NK still outperforms the previous SOTA
                                                                           NeWCRFs [50] on NYU Depth v2 by 18.9% (REL = 0.077,
Table 1. Quantitative comparison on NYU-Depth v2. The re-                  Tab. 1). While ZoeD-M12-NK is not as good as our model
ported numbers of prior art are from the corresponding original            (ZoeD-M12-N) fine-tuned only on NYU Depth v2, it pro-
papers. Best results are in bold, second best are underlined.              vides a very attractive trade-off between performance and

                                                                       6
Method                NYU     KITTI    iBims-1   vKITTI-2    mRID         NK (NYU and KITTI mixture) using a single metric head;
 Baselines: no modification                                               only the design of the metric head varies. Tab. 2 shows
                                                                          that previous models still fall behind in this setting. Since
DORN-X-NK†            0.156    0.115    0.287        0.259   -45.7%
LocalBins-X-NK†       0.245    0.133    0.296        0.265   -74.0%       DORN [11] and LocalBins [6] are light-weight and mod-
PixelBins-X-NK†         -        -        -            -        -         ular, they can be easily used in conjuction with our pre-
NeWCRFs-X-NK†         0.109    0.076    0.189        0.190    0.0%        trained relative depth model instead of our metric bins mod-
 Baselines: modified to use our pre-trained DPT-BEiT-L as backbone        ule. NeWCRFs [50] is originally a tightly-coupled decoder-
                                                                          focused design; however, to keep the base model exactly the
DORN-M12-NK†          0.110    0.081    0.242        0.215   -12.2%
LocalBins-M12-NK†     0.086    0.071    0.221        0.121   11.8%        same, we use an extra head with NeWCRFs layers that use
PixelBins-M12-NK†     0.088    0.071    0.232        0.119   10.1%        DPT decoder features as multi-scale input. This increases
NeWCRFs-M12-NK†       0.088    0.073    0.233        0.124    8.7%        the complexity significantly (∼40M more parameters than
 Ours: different configuations for fair comparison                        ours) yet still underperforms when compared to pixel-wise
ZoeD-X-NK†            0.095    0.074    0.187        0.184    4.9%
                                                                          bins-based methods: LocalBins, PixelBins and ZoeD-M12-
ZoeD-M12-NK†          0.081    0.061    0.210        0.112   18.8%        NK. This suggests that bins-based architectures are better
ZoeD-M12-NK           0.077    0.057    0.186        0.105   25.2%        suited for multi-domain training and can better exploit rel-
                                                                          ative depth pre-training. Our model performs best both on
Table 2. Comparison with existing works when trained on                   NYU and KITTI, as well as on iBims-1 and virtual KITTI-
NYU and KITTI. Results are reported using the REL metric. The             2 that have not been seen in training. These results indi-
mRID column denotes the mean relative improvement with re-                cate that our metric bins module exploits pre-training better
spect to NeWCRFs across datasets. X in the model name, means              than existing works, enabling improved domain adaptation
no architecture change and no pre-training. M12 means that the
                                                                          and generalization (zero-shot performance). We investigate
model was pre-trained (using our base model based on the DPT
                                                                          zero-shot performance in more detail next.
architecture with the BEiT-L encoder). All models are fine-tuned
on NYU and KITTI. † denotes a single metric head (shared);
single-head training allows us to adapt prior models without major
                                                                          5.3. Zero-shot Generalization
changes. Best results are in bold, second best are underlined. Pix-           We evaluate the generalization capabilities of our ap-
elBins [36] did not converge without modification. We also tried to       proach by comparing its zero-shot performance to prior
train AdaBins [5] across both datasets, but despite our best effort
                                                                          works on eight unseen indoor and outdoor datasets without
and extensive hyperparameter tuning, it did not converge.
                                                                          fine-tuning; we show qualitative results in Fig. 1 and report
generalization across domains.                                            quantitative results in Tab. 3 and Tab. 4.
    To underline the difficulty of cross-domain training, we                  Tab. 3 reports zero-shot generalization on indoor
perform a comparison to other models trained simultane-                   datasets. Even with fine-tuning across both the indoor
ously on indoor and outdoor datasets (NK). First, we evalu-               (NYU Depth v2) and outdoor (KITTI) domains, our model
ate recent methods trained on NK without any architectural                ZoeD-M12-NK demonstrates significantly better perfor-
modifications and compare them with our method in Tab. 2.                 mance than previous state-of-the-art models. The mean rel-
We find that existing works are unable to achieve competi-                ative improvement (mRIθ ) ranges from 5.3% for HyperSim
tive results in that setting. AdaBins [5] and PixelBins [36]              to 46.3% for DIODE Indoor. As expected, fine-tuning only
fail to converge at all, while the SOTA NeWCRFs’ [50] per-                on NYU Depth v2 so that the training and test domains are
formance degrades by nearly 15% (REL 0.095 to 0.109)                      both indoor, i.e. ZoeD-M12-N, leads to an increase in mRIθ
on NYU (compare Tab. 2 with Tab. 1). These experi-                        on all datasets. ZoeD-X-N scores lower in most datasets due
ments confirm that previous models significantly degrade                  to the lack of relative depth pre-training.
when being trained jointly on datasets from different do-                     Tab. 4 reports zero-shot generalization on outdoor
mains. In contrast, we only observe an 8% drop (REL 0.075                 datasets. Similar as for the indoor datasets, pre-training on
to 0.081) while using the shared head, demonstrating our                  M12 is generally beneficial. ZoeD-M12-NK improves from
model’s ability to deal with different domains at once. This              7.8% for Virtual KITTI 2 to 976.4% for DIML Outdoor
gap is further reduced to mere 2.6% (REL 0.075 vs 0.077)                  over NeWCRFs [50]. On DDAD, ZoeD-M12-NK performs
using our two-head model ZoeD-M12-NK, outperforming                       12.8% worse while NeWCRFs [50] is best. The metrics in
NeWCRFs [50] by 25.2% (mRID in REL).                                      Tab. 4 and the rightmost image in Fig. 1 show the quality of
    We conclude that previous models require changes to                   our results. Overall, our framework is the top performer in
successfully train on multiple datasets. We conduct ad-                   7 out of 8 datasets.
ditional experiments where we improve previous models                         Probably the most interesting result is the high mRIθ
by incorporating part of our framework. Specifically, we                  value of 976.4% that ZoeD-M12-NK achieves on DIML
use the same base model (DPT with a BEiT-L backbone),                     Outdoor. All other models are fine-tuned only on KITTI
with relative pre-training on M12, and with fine-tuning on                with large depth ranges but the DIML Outdoor dataset con-

                                                                      7
                          SUN RGB-D                      iBims-1 Benchmark                                                  DIODE Indoor                          HyperSim
Method          δ1 ↑    REL ↓ RMSE ↓ mRIθ ↑       δ1 ↑     REL ↓ RMSE ↓ mRIθ ↑                                     δ1 ↑    REL ↓ RMSE ↓ mRIθ ↑          δ1 ↑    REL ↓ RMSE ↓ mRIθ ↑
BTS [20]        0.740   0.172   0.515   -14.2%   0.538    0.231   0.919       -6.9%                                0.210    0.418    1.905    2.3%     0.225     0.476     6.404    -8.6%
AdaBins [5]     0.771   0.159   0.476    -7.0%   0.555    0.212   0.901       -2.1%                                0.174    0.443    1.963    -7.2%    0.221     0.483     6.546   -10.5%
LocalBins [6]   0.777   0.156   0.470    -5.6%   0.558    0.211   0.880       -0.7%                                0.229    0.412    1.853    7.1%     0.234     0.468     6.362    -6.6%
NeWCRFs [50]    0.798   0.151   0.424    0.0%    0.548    0.206   0.861       0.0%                                 0.187    0.404    1.867    0.0%     0.255     0.442     6.017    0.0%
ZoeD-X-N        0.857 0.124     0.363   13.2% 0.668 0.173         0.730       17.7% 0.400 0.324                                      1.581    49.7% 0.284 0.421            5.889   6.1%
ZoeD-M12-N      0.864 0.119     0.346   16.0% 0.658 0.169         0.711       18.5% 0.376 0.327                                      1.588    45.0% 0.292 0.410            5.771   8.6%
ZoeD-M12-NK 0.856 0.123         0.356   13.9%    0.615 0.186      0.777       10.6%                                0.386 0.331       1.598    46.3%    0.274 0.419         5.830    5.3%

Table 3. Quantitative results for zero-shot transfer to four unseen indoor datasets. mRIθ denotes the mean relative improvement with
respect to NeWCRFs across all metrics (δ1 , REL, RMSE). Evaluation depth is capped at 8m for SUN RGB-D, 10m for iBims and DIODE
Indoor, and 80m for HyperSim. Best results are in bold, second best are underlined.

                        Virtual KITTI 2                      DDAD                                                           DIML Outdoor                        DIODE Outdoor
Method          δ1 ↑    REL ↓ RMSE ↓ mRIθ ↑ δ1 ↑         REL ↓ RMSE ↓ mRIθ ↑ δ1 ↑                                          REL ↓ RMSE ↓ mRIθ ↑         δ1 ↑     REL ↓ RMSE ↓ mRIθ ↑
BTS [20]        0.831   0.115   5.368   2.5%     0.805    0.147   7.550   -17.8%                               0.016       1.785    5.908    24.3%     0.171    0.837    10.48     -4.8%
AdaBins [5]     0.826   0.122   5.420   0.0%     0.766    0.154   8.560   -26.7%                               0.013       1.941    6.272     9.7%     0.161    0.863    10.35     -7.2%
LocalBins [6]   0.810   0.127   5.981   -5.3%    0.777    0.151   8.139   -23.2%                               0.016       1.820    6.706    19.5%     0.170    0.821    10.27     -3.6%
NeWCRFs [50]    0.829   0.117   5.691   0.0%     0.874    0.119   6.183    0.0%                                0.010       1.918    6.283     0.0%     0.176    0.854    9.228     0.0%
ZoeD-X-K        0.837 0.112     5.338    3.8% 0.790 0.137         7.734   -16.6% 0.005 1.756                                        6.180    -13.3% 0.242 0.799          7.806     19.8%
ZoeD-M12-K      0.864 0.100     4.974   10.5% 0.835 0.129         7.108    -9.3% 0.003 1.921                                        6.978    -27.1% 0.269 0.852          6.898     26.1%
ZoeD-M12-NK 0.850 0.105         5.095   7.8%     0.824 0.138      7.225   -12.8% 0.292                                     0.641 3.610       976.4% 0.208 0.757          7.569     15.8%

Table 4. Quantitative results for zero-shot transfer to four unseen outdoor datasets. mRIθ denotes the mean relative improvement
with respect to NeWCRFs across all metrics (δ1 , REL, RMSE). Best results are in bold, second best are underlined.

tains mainly close-up images of outdoor scenarios making it                          benefit from new backbones as they get introduced in the
more similar to an indoor dataset. Since ZoeD-M12-NK was                             future.
also fine-tuned on NYU Depth v2 and automatically routes
inputs to different heads, it seems to leverage its knowledge                                                 90
                                                                                                                     Beit-L
of the indoor domain to improve predictions. This is also                                                     89     (345M)
                                                                               ImageNet - Top1 Accuracy (%)

supported by the low performance of ZoeD-X-K and ZoeD-                                                                                  Swin2-L                   Swin-L
                                                                                                              88                         (214M)                   (270M)
M12-K which were only fine-tuned on KITTI. This result
clearly shows the benefit of models fine-tuned across multi-                                                  87
ple domains for generalization to arbitrary datasets. We ex-                                                                                  Swin-L           Beit-B
                                                                                                              86                              (212M)           (112M)
pect that defining more granular domains and fine-tuning a
variant of our model with more than two heads across many                                                     85         ZoeD-M12-N                          EfficientNet-B5
metric datasets would lead to even better generalization per-                                                            NeWCRF                                    (74M)
formance.                                                                                                     84         LocalBins
                                                                                                                     0.075 0.080 0.085 0.090 0.095 0.100
5.4. Ablation Studies                                                                                                      NYUv2 Depth - Absolute Relative Error (REL)
   In this section we study the importance of various design                         Figure 5. Backbone ablation study. There is a strong correlation
choices in our models.                                                               between backbone performance in image classification and depth
                                                                                     estimation. Larger backbones achieve lower absolute relative error
                                                                                     (REL); with the same backbone and overall fewer parameters, our
Backbones. We study the effect of using different back-                              method still outperforms the current state-of-the-art NeWCRFs.
bones for our base MiDaS model. The results are summa-                               The area of the circles is proportional to the number of parameters.
rized in Fig. 5. We find that larger backbones with more                             The backbones shown are BEiT [3], Swin2 [27], Swin [28] and
parameters lead to improved performance, but our model                               EfficientNet B5 [39], where L stands for large and B for base.
still outperforms the previous state of the art when using
the same backbone [28]. Further, the image classification
performance of the backbone is highly correlated to the per-                         Metric Bins Module. We study the contribution to the
formance of our depth estimation model, i.e. lower absolute                          overall performance by various variants of our metric bins
relative error (REL). Hence, our architecture can directly                           module listed in Tab. 5. First, we remove our metric bins

                                                                          8
               Metric head type                 REL ↓    RMSE ↓                                 Labels required   REL ↓    RMSE ↓
                                                                                   Variant      Train Inference NYU KITTI NYU KITTI
    Type          Variant           Config
  Naive head          -                 -       0.096      0.335               Labeled Router    3      3     0.080 0.057 0.290 2.452
                   Splitter        factor = 2   0.085      0.301               Trained Router    3      7     0.077 0.057 0.277 2.362
                 Exponential                                                    Auto Router      7      7     0.102 0.075 0.377 2.584
                                  {16,8,4,1}    0.086      0.305
                  Attractor
 Metric bins                                                                 Table 6. Router variants. The reported results are all based on
                                   {8,8,8,8}    0.081      0.295
                  Inverse         {16,2,2,16}   0.081      0.291             ZoeD-M12-NK evaluated on NYU Depth v2 and KITTI. Best re-
                  Attractor       {1,4,8,16}    0.080      0.287             sults are in bold, second best are underlined.
                                  {16,8,4,1}    0.075      0.270

Table 5. Metric head variants. The “Config” column specifies
the split factor in case of the splitter variant and the number of           6. Conclusion
attractors {nla } for attractor variants. The reported results are all          Our proposed framework, ZoeDepth, bridges the gap be-
based on ZoeD-M12-N evaluated on NYU Depth v2. Best results
                                                                             tween relative and metric depth estimation. In the first stage,
are in bold, second best are underlined.
                                                                             we pre-train an encoder-decoder architecture using relative
                                                                             depth on a collection of datasets. In the second stage, we
module and attach a convolutional block to the decoder fea-                  add domain-specific heads based on our new metric bins
tures from the base DPT model and directly predict the met-                  module to the decoder and fine-tune the model on one or
ric depth (standard regression). We call this variant naive                  more datasets for metric depth prediction. Our proposed ar-
head. Our best attractor variant performs about 21% better                   chitecture decisively improves upon the state of the art for
than the naive head. Notably, the metric bins with the split-                NYU Depth v2 (21% in REL) and also significantly im-
ter design as in [6] improves upon the naive head by 11.4%,                  proves upon the state of the art in zero-shot transfer. We
which is consistent with the 10.8% improvement observed                      expect that defining more granular domains beyond indoor
by [6] when comparing a naive Unet design with the splitter                  and outdoor, and fine-tuning on more metric datasets can
LocalBins design (refer to Tab. 3 in [6]). Next, we com-                     improve our results further. In future work, we would like
pare our novel attractor design with the splitter design of                  to investigate a mobile architecture version of ZoeDepth,
LocalBins [6]. Our best attractor variant performs 11.7%                     e.g., for on-device photo editing, and extend our work to
better. All the inverse attractor variants perform decisively                stereo-image depth estimation.
better than the splitter variant while the exponential variant
performs slightly worse.

Routers. As discussed in Sec. 3.3, we test the three vari-
ants for routing the relative features to metric heads. The
results for the models with two metric heads, one for NYU
Depth v2 and one for KITTI, are provided in Tab. 6. Out of
the three variants, the Auto Router performs the worst. This
is expected as in this case the router never sees any domain
labels. Surprisingly, the Trained Router performs better on
NYU Depth v2 than the Labeled Router, even though do-
main labels are unavailable during inference. We hypothe-
size that the domain-level discriminatory supervision may
help in learning better representations. As we aim for a
generic model without special requirements during infer-
ence, we choose the Trained Router and use it in all our
multi-head models.

Log Binomial. We evaluate the effect of using a log bi-
nomial distribution by studying the performance of ZoeD-
M12-N on NYU-Depth-v2 with log binomial and softmax
probability heads. Consistent with [4], we observe that us-
ing log binomial (REL = 0.075) instead of softmax (REL =
0.077) leads to about 2% improvement. This highlights the
importance of unimodal distributions for ordinal problems.

                                                                         9
References                                                                       IEEE Winter Conference on Applications of Computer Vision
                                                                                 (WACV), pages 1043–1051, 2018. 6, 20
 [1] Miton Abramowitz. Stegun., ia (1972). handbook of mathe-               [15] Xinyu Huang, Peng Wang, Xinjing Cheng, Dingfu Zhou,
     matical functions. Formulas, Graphs and Mathematical Ta-                    Qichuan Geng, and Ruigang Yang. The apolloscape open
     bles, 2002. 4                                                               dataset for autonomous driving and its application. IEEE
 [2] Ashutosh Agarwal and Chetan Arora. Attention attention                      transactions on pattern analysis and machine intelligence,
     everywhere: Monocular depth prediction with skip attention.                 42(10):2702–2719, 2019. 5, 13
     arXiv preprint arXiv:2210.09071, 2022. 3, 4                            [16] Jinyoung Jun, Jae-Han Lee, Chul Lee, and Chang-Su Kim.
 [3] Hangbo Bao, Li Dong, and Furu Wei. Beit: BERT pre-                          Depth map decomposition for monocular depth estimation.
     training of image transformers. CoRR, abs/2106.08254,                       arXiv preprint arXiv:2208.10762, 2022. 2, 3, 6
     2021. 2, 3, 8, 12                                                      [17] Youngjung Kim, Hyungjoo Jung, Dongbo Min, and
 [4] Christopher Beckham and Christopher Pal. Unimodal prob-                     Kwanghoon Sohn. Deep monocular depth estimation via in-
     ability distributions for deep ordinal classification. In Doina             tegration of global and local predictions. IEEE transactions
     Precup and Yee Whye Teh, editors, Proceedings of the 34th                   on Image Processing, 27(8):4131–4144, 2018. 5, 12, 13, 16,
     International Conference on Machine Learning, volume 70                     18
     of Proceedings of Machine Learning Research, pages 411–                [18] Tobias Koch, Lukas Liebel, Friedrich Fraundorfer, and
     419. PMLR, 06–11 Aug 2017. 4, 9                                             Marco Körner. Evaluation of cnn-based single-image depth
 [5] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.                     estimation methods. In Proceedings ECCV 2018 Workshops,
     Adabins: Depth estimation using adaptive bins. In Proceed-                  2019. 5, 12, 13, 15
     ings of the IEEE/CVF Conference on Computer Vision and                 [19] Iro Laina, Christian Rupprecht, Vasileios Belagiannis, Fed-
     Pattern Recognition, pages 4009–4018, 2021. 1, 2, 3, 4, 6,                  erico Tombari, and Nassir Navab. Deeper depth prediction
     7, 8, 13, 14, 15, 16, 20                                                    with fully convolutional residual networks. 2016 Fourth In-
 [6] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.                     ternational Conference on 3D Vision (3DV), pages 239–248,
     Localbins: Improving depth estimation by learning local dis-                2016. 6, 20
     tributions. In European Conference on Computer Vision,                 [20] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and
     pages 480–496. Springer, 2022. 1, 2, 3, 4, 6, 7, 8, 9, 13,                  Il Hong Suh. From big to small: Multi-scale local planar
     14, 15, 16, 20                                                              guidance for monocular depth estimation. arXiv preprint
 [7] Yohann Cabon, Naila Murray, and Martin Humenberger. Vir-                    arXiv:1907.10326, 2019. 6, 8, 13, 14, 15, 16, 20
     tual kitti 2, 2020. 5, 12, 13, 15, 17                                  [21] Jae-Han Lee and Chang-Su Kim. Monocular depth es-
 [8] Xiaotian Chen, Xuejin Chen, and Zheng-Jun Zha. Structure-                   timation using relative depth maps. In Proceedings of
     aware residual pyramid network for monocular depth esti-                    the IEEE/CVF Conference on Computer Vision and Pattern
     mation. In Proceedings of the Twenty-Eighth International                   Recognition, pages 9729–9738, 2019. 2
     Joint Conference on Artificial Intelligence, IJCAI-19, pages           [22] Wonwoo Lee, Nohyoung Park, and Woontack Woo. Depth-
     694–700. International Joint Conferences on Artificial Intel-               assisted real-time 3d object detection for augmented reality.
     ligence Organization, 7 2019. 6, 20                                         ICAT’11, 2:126–132, 2011. 6, 20
 [9] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map              [23] Bo Li, Yuchao Dai, and Mingyi He. Monocular depth es-
     prediction from a single image using a multi-scale deep net-                timation with hierarchical fusion of dilated cnns and soft-
     work. In NIPS, 2014. 6, 20                                                  weighted-sum inference. Pattern Recognition, 83:328–339,
[10] William Fedus, Jeff Dean, and Barret Zoph. A review                         2018. 3
     of sparse expert models in deep learning. arXiv preprint               [24] Ruibo Li, Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, and
     arXiv:2209.01667, 2022. 5                                                   Lingxiao Hang. Deep attention-based classification network
[11] Huan Fu, Mingming Gong, Chaohui Wang, Nematollah Bat-                       for robust depth prediction. In C.V. Jawahar, Hongdong Li,
     manghelich, and Dacheng Tao. Deep ordinal regression net-                   Greg Mori, and Konrad Schindler, editors, Computer Vision
     work for monocular depth estimation. 2018 IEEE/CVF Con-                     – ACCV 2018, pages 663–678, Cham, 2019. Springer Inter-
     ference on Computer Vision and Pattern Recognition, pages                   national Publishing. 3
     2002–2011, 2018. 3, 6, 7, 20                                           [25] Zhengqi Li and Noah Snavely. Megadepth: Learning single-
[12] Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raven-                  view depth prediction from internet photos. In Computer
     tos, and Adrien Gaidon. 3d packing for self-supervised                      Vision and Pattern Recognition (CVPR), 2018. 5, 13
     monocular depth estimation. In IEEE Conference on Com-                 [26] Zhenyu Li, Xuyang Wang, Xianming Liu, and Junjun Jiang.
     puter Vision and Pattern Recognition (CVPR), 2020. 5, 12,                   Binsformer: Revisiting adaptive bins for monocular depth
     13, 15, 18                                                                  estimation. arXiv preprint arXiv:2204.00987, 2022. 1, 2, 3,
[13] Zhixiang Hao, Yu Li, Shaodi You, and Feng Lu. Detail pre-                   4
     serving depth estimation from a single image using attention           [27] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
     guided networks. 2018 International Conference on 3D Vi-                    Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, et al.
     sion (3DV), pages 304–313, 2018. 6, 20                                      Swin transformer v2: Scaling up capacity and resolution. In
[14] Junjie Hu, Mete Ozay, Yan Zhang, and Takayuki Okatani.                      Proceedings of the IEEE/CVF Conference on Computer Vi-
     Revisiting single image depth estimation: Toward higher                     sion and Pattern Recognition, pages 12009–12019, 2022. 8,
     resolution maps with accurate object boundaries. 2019                       12

                                                                       10
[28] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng                    Gregory Shakhnarovich. DIODE: A Dense Indoor and Out-
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:                    door DEpth Dataset. CoRR, abs/1908.00463, 2019. 5, 12,
     Hierarchical vision transformer using shifted windows. In                 13, 14, 16, 19
     Proceedings of the IEEE/CVF International Conference on              [41] Chaoyang Wang, Simon Lucey, Federico Perazzi, and Oliver
     Computer Vision, pages 10012–10022, 2021. 8                               Wang. Web stereo video supervision for depth prediction
[29] Moritz Menze and Andreas Geiger. Object scene flow for au-                from dynamic scenes. In 2019 International Conference on
     tonomous vehicles. In Proceedings of the IEEE Conference                  3D Vision (3DV), pages 348–357. IEEE, 2019. 5, 13
     on Computer Vision and Pattern Recognition (CVPR), June              [42] Qiang Wang, Shizhen Zheng, Qingsong Yan, Fei Deng,
     2015. 5, 12, 13                                                           Kaiyong Zhao, and Xiaowen Chu. Irs: A large naturalis-
[30] Alican Mertan, Damien Jade Duff, and Gozde Unal. Single                   tic indoor robotics stereo dataset to train deep models for
     image depth estimation: An overview. Digital Signal Pro-                  disparity and surface normal estimation. arXiv preprint
     cessing, 123:103441, 2022. 1, 2                                           arXiv:1912.09678, 2019. 5, 13
[31] Michael Ramamonjisoa and Vincent Lepetit. Sharpnet: Fast             [43] Wenshan Wang, Delong Zhu, Xiangwei Wang, Yaoyu Hu,
     and accurate recovery of occluding contours in monocular                  Yuheng Qiu, Chen Wang, Yafei Hu, Ashish Kapoor, and Se-
     depth estimation. In Proceedings of the IEEE/CVF Interna-                 bastian Scherer. Tartanair: A dataset to push the limits of
     tional Conference on Computer Vision (ICCV) Workshops,                    visual slam. In 2020 IEEE/RSJ International Conference
     Oct 2019. 6, 20                                                           on Intelligent Robots and Systems (IROS), pages 4909–4916.
[32] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-                 IEEE, 2020. 5, 13
     sion transformers for dense prediction. In Proceedings of            [44] Ross Wightman.        Pytorch image models.          https :
     the IEEE/CVF International Conference on Computer Vision                  / / github . com / rwightman / pytorch - image -
     (ICCV), pages 12179–12188, October 2021. 2, 3, 5                          models, 2019. 5, 12
[33] René Ranftl, Katrin Lasinger, David Hafner, Konrad                  [45] Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, Yang Xiao,
     Schindler, and Vladlen Koltun. Towards robust monocular                   Ruibo Li, and Zhenbo Luo. Monocular relative depth percep-
     depth estimation: Mixing datasets for zero-shot cross-dataset             tion with web stereo data supervision. In Proceedings of the
     transfer. IEEE Transactions on Pattern Analysis and Ma-                   IEEE Conference on Computer Vision and Pattern Recogni-
     chine Intelligence (TPAMI), 2020. 1, 2, 3, 4, 5, 12, 13                   tion, pages 311–320, 2018. 5, 13
[34] Haoyu Ren, Mostafa El-Khamy, and Jungwon Lee. Deep                   [46] Ke Xian, Jianming Zhang, Oliver Wang, Long Mai, Zhe Lin,
     robust single image depth estimation neural network using                 and Zhiguo Cao. Structure-guided ranking loss for single im-
     scene understanding. In CVPR Workshops, 2019. 3                           age depth prediction. In Proceedings of the IEEE/CVF Con-
[35] Mike Roberts, Jason Ramapuram, Anurag Ranjan, Atulit                      ference on Computer Vision and Pattern Recognition, pages
     Kumar, Miguel Angel Bautista, Nathan Paczan, Russ Webb,                   611–620, 2020. 5, 13
     and Joshua M. Susskind. Hypersim: A photorealistic syn-              [47] Yao Yao, Zixin Luo, Shiwei Li, Jingyang Zhang, Yufan Ren,
     thetic dataset for holistic indoor scene understanding. In                Lei Zhou, Tian Fang, and Long Quan. Blendedmvs: A large-
     International Conference on Computer Vision (ICCV) 2021,                  scale dataset for generalized multi-view stereo networks. In
     2021. 5, 12, 13, 14, 17                                                   Proceedings of the IEEE/CVF Conference on Computer Vi-
[36] Khalil Sarwari, Forrest Laine, and Claire Tomlin. Progress                sion and Pattern Recognition, pages 1790–1799, 2020. 5,
     and proposals: A case study of monocular depth estimation.                13
     Master’s thesis, EECS Department, University of California,
                                                                          [48] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     Berkeley, May 2021. 3, 7
                                                                               forcing geometric constraints of virtual normal for depth pre-
[37] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
                                                                               diction. In Proceedings of the IEEE/CVF International Con-
     Fergus. Indoor segmentation and support inference from
                                                                               ference on Computer Vision (ICCV), October 2019. 6, 20
     rgbd images. In Computer Vision – ECCV 2012, pages 746–
                                                                          [49] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus,
     760, Berlin, Heidelberg, 2012. Springer Berlin Heidelberg.
                                                                               Long Mai, Simon Chen, and Chunhua Shen. Learning to
     2, 5, 6, 12, 13
                                                                               recover 3d scene shape from a single image. In Proceed-
[38] S. Song, S. P. Lichtenberg, and J. Xiao. Sun rgb-d: A rgb-d
                                                                               ings of the IEEE/CVF Conference on Computer Vision and
     scene understanding benchmark suite. In 2015 IEEE Confer-
                                                                               Pattern Recognition, pages 204–213, 2021. 3
     ence on Computer Vision and Pattern Recognition (CVPR),
                                                                          [50] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and
     pages 567–576, 2015. 5, 12, 13, 14
                                                                               Ping Tan. New crfs: Neural window fully-connected
[39] Mingxing Tan and Quoc V. Le. Efficientnet: Rethinking
                                                                               crfs for monocular depth estimation.          arXiv preprint
     model scaling for convolutional neural networks. In Ka-
                                                                               arXiv:2203.01502, 2022. 1, 2, 6, 7, 8, 13, 14, 15, 16, 17,
     malika Chaudhuri and Ruslan Salakhutdinov, editors, Pro-
                                                                               18, 19, 20
     ceedings of the 36th International Conference on Machine
     Learning, ICML 2019, 9-15 June 2019, Long Beach, Cali-
     fornia, USA, volume 97 of Proceedings of Machine Learning
     Research, pages 6105–6114. PMLR, 2019. 8
[40] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,
     Haochen Wang, Falcon Z. Dai, Andrea F. Daniele, Moham-
     madreza Mostajabi, Steven Basart, Matthew R. Walter, and

                                                                     11
A. Appendix                                                            is an exception where our models share this behavior with
                                                                       NeWCRF.
A.1. Datasets Overview                                                     For the outdoor datasets, rows 1 to 3 of Figure 12 clearly
    We begin by providing a detailed overview of the prop-             demonstrate the advantage of our model ZoeD-M12-NK
erties of the datasets used for metric depth fine-tuning and           with respect to NeWCRF. As explained in Section 5.3 of
evaluation of the new ZoeDepth architecture (see Fig. 2 in             the main paper, ZoeD-M12-NK is not only fine-tuned on the
the main paper) in Table 7. These datasets consist of NYU              outdoor dataset KITTI but also on the indoor dataset NYU
Depth v2 [37] and KITTI [29] used for metric depth fine-               Depth v2, which better reflects the low depth values observ-
tuning as well as respectively four in- and outdoor datasets           able in the RGB and ground truth images of Figure 12. The
to test for generalization performance (see Sec. 4.1 of the            improved sharpness in predictions from our models when
main paper). The indoor datasets consist of SUN RGB-                   compared to NeWCRF, as mentioned in the caption of Fig-
D [38], the iBims benchmark [18], DIODE Indoor [40]                    ure 4 of the main paper, continues to hold across all 8 indoor
and HyperSim [35]. For the outdoor datasets, we use                    and outdoor datasets.
DDAD [12], DIML Outdoor [17], DIODE Outdoor [40] and
Virtual KITTI 2 [7].
                                                                       A.4. ZoeDepth with different backbones
    All ZoeDepth architectures and prior works are evalu-                 We achieve the best performance for ZoeDepth when us-
ated by resizing the input to the training resolution. Zoe-            ing the large BEiT384 -L [3] backbone for the MiDaS en-
*-N, Zoe-*-NK, and Zoe-*-K models are trained at resolu-               coder (see Fig. 2 of the main paper), which is responsi-
tions 384 × 512, 384 × 512 and 384 × 768 respectively.                 ble for the feature extraction of relative depth computa-
Predictions are resized to original ground truth resolution            tion. According to Table 17, this transformer backbone
before evaluation.                                                     causes ZoeDepth to consist of 345M parameters of which
                                                                       344M parameters are consumed by MiDaS. In MiDaS, the
A.2. Training Details                                                  BEiT384 -L [3] backbone takes up 305M of the 344M param-
   In Table 8, we show various training strategies (see Sec-           eters. The number of parameters of ZoeDepth is therefore
tion 3.3 of the main paper) applied to the ZoeDepth archi-             mainly influenced by the chosen MiDaS encoder backbone.
tecture. The training strategies differ by the datasets used              Due to the modularity of our architecture, we can swap
for relative depth pre-training of the MiDaS [33] encoder-             out the MiDaS encoder backbone. In Table 17, we compare
decoder, the datasets employed for metric depth fine-tuning            the number of parameters of ZoeDepth for different back-
in ZoeDepth and the number of used metric heads. Each                  bones. The timm [44] repository, which provides the back-
combination of these options provided in Tab. 8 defines a              bones, also offers the base BEiT384 -B transformer. Utilizing
different model of ZoeDepth. Results for these combina-                this variant reduces the number of parameters of ZoeDepth
tions are shown in Appendix A.3.                                       from 345M to 112M. Another type of transformer with
                                                                       good performance is the hierarchical transformer Swin2
A.3. Detailed Results                                                  [27] based on shifted windows. When using the base and
                                                                       tiny variants Swin2-B and Swin2-T, the number of parame-
   In Tables 3 and 4 of the main paper, we have provided
                                                                       ters of ZoeDepth drops to 102M and 42M, respectively. We
quantitative results for zero-shot transfer to the four in- and
                                                                       report the results of all the aforementioned models evalu-
outdoor datasets unseen during training, which are men-
                                                                       ated on NYU Depth V2 in Table 18.
tioned in Appendix A.1. These results are supplemented
by the threshold accuracies δ2 and δ3 as well as the aver-
age log10 error in Tables 9 to 16. Also, while the main pa-
per only shows our models ZoeD-X-K, ZoeD-M12-K and
ZoeD-M12-NK, Tables 9 to 16 contain the additional model
ZoeD-NK-N. This model uses only the dataset combination
of NYU Depth v2 (N) [37] and KITTI (K) [29] for the rela-
tive depth pre-training.
   Figures 6 to 13 show metric depth maps computed with
our ZoeDepth architecture for various example images of
the in- and outdoor datasets described in Appendix A.1.
   For the indoor datasets, NeWCRF shows a tendency to
underestimate the depth, e.g., the relatively bright images of
NeWCRF in rows 3 and 4 of Figure 6 as well as rows 1 and
3 of Figure 7. Our models Zoe-M12-NK and Zoe-M12-N
are much closer to the ground truth. Only row 4 of Figure 9

                                                                  12
                                                       Seen in   # Train # Eval Eval Depth [m] Crop
          Dataset                   Domain    Type    Training? Samples Samples Min     Max    Method
          NYU Depth v2 [37]         Indoor    Real        X     24k [20]   654  1e-3     10    Eigen
          SUN RGB-D [38]            Indoor    Real        7         -     5050  1e-3     8     Eigen
          iBims-1 [18]              Indoor    Real        7         -      100  1e-3     10    Eigen
          DIODE Indoor [40]         Indoor    Real        7         -      325  1e-3     10    Eigen
          HyperSim [35]             Indoor Synthetic      7         -     7690  1e-3     80    Eigen
          KITTI [29]                Outdoor   Real        X     26k [20]   697  1e-3     80    Garg‡
          Virtual KITTI 2 [7]       Outdoor Synthetic     7         -     1701  1e-3     80    Garg‡
          DDAD [12]                 Outdoor   Real        7         -     3950  1e-3     80     Garg
          DIML Outdoor [17]         Outdoor   Real        7         -      500  1e-3     80     Garg
          DIODE Outdoor [40]        Outdoor   Real        7         -      446  1e-3     80     Garg

Table 7. Overview of datasets used in metric depth fine-tuning and evaluation of ZoeDepth architectures. For demonstrating zero-shot
transfer, we evaluate across a total of 13165 indoor samples and 6597 outdoor samples. While HyperSim is predominantly an indoor
dataset, there are several samples exhibiting depth ranges exceeding 10 m, so we relax the maximum evaluation depth up to 80 m. ‡ : To
follow prior works [5, 50], we crop the sample and then use scaled Garg crop for evaluation. We verify the transforms by reproducing
results obtained by using respective pre-trained checkpoints provided by prior works.

                 Model                 Relative depth pre-training      Metric depth fine-tuning        # metric heads
                 ZoeD-X-N                          7                             NYU                          1
                 ZoeD-N-N                         NYU                            NYU                          1
                 ZoeD-NK-N                    NYU+KITTI                          NYU                          1
                 ZoeD-M12-N                       M12                            NYU                          1
                 ZoeD-X-K                          7                             KITTI                           1
                 ZoeD-K-K                        KITTI                           KITTI                           1
                 ZoeD-NK-K                     NYU+KITTI                         KITTI                           1
                 ZoeD-M12-K                      M12                             KITTI                           1
                 ZoeD-NK-NK†                   NYU+KITTI                      NYU+KITTI                          1
                 ZoeD-M12-NK†                    M12                          NYU+KITTI                          1
                 ZoeD-NK-NK                    NYU+KITTI                      NYU+KITTI                          2
                 ZoeD-M12-NK                     M12                          NYU+KITTI                          2

Table 8. Models are named according to the following convention: ZoeD-RDPT-MFT, where ZoeD is the abbreviation for ZoeDepth,
RDPT denotes the datasets used for relative depth pre-training and MFT denotes the datasets used for metric depth fine-tuning. Models
with an X do not use a relative depth pre-training. The collection M12 contains the datasets HRWSI [46], BlendedMVS [47], ReDWeb [45],
DIML-Indoor [17], 3D Movies [33], MegaDepth [25], WSVD [41], TartanAir [43], ApolloScape [15], IRS [42], KITTI (K) [29] and NYU
Depth v2 (N) [37].

Method           δ1 ↑   δ2 ↑    δ3 ↑   REL ↓ RMSE ↓ log10 ↓            Method            δ1 ↑   δ2 ↑     δ3 ↑        REL ↓ RMSE ↓ log10 ↓
BTS [20]         0.740 0.933   0.980   0.172    0.515     0.075        BTS [20]         0.538   0.863    0.948       0.231   0.919   0.112
AdaBins [5]      0.771 0.944   0.983   0.159    0.476     0.068        AdaBins [5]      0.555   0.873    0.960       0.212   0.901   0.107
LocalBins [6]    0.777 0.949   0.985   0.156    0.470     0.067        LocalBins [6]    0.558   0.877    0.966       0.211   0.880   0.104
NeWCRF [50]      0.798 0.967   0.992   0.151    0.424     0.064        NeWCRF [50]      0.548   0.884    0.979       0.206   0.861   0.102
ZoeD-X-N    0.857 0.979        0.995   0.124    0.363     0.054        ZoeD-X-N    0.668        0.944    0.983       0.173   0.730   0.084
ZoeD-NK-N   0.857 0.978        0.994   0.125    0.360     0.054        ZoeD-NK-N   0.671        0.939    0.983       0.172   0.735   0.084
ZoeD-M12-N 0.864 0.982         0.995   0.119    0.346     0.052        ZoeD-M12-N 0.658         0.947    0.985       0.169   0.711   0.083
ZoeD-M12-NK 0.856 0.979        0.995   0.123    0.356     0.053        ZoeD-M12-NK 0.615        0.928    0.982       0.186   0.777   0.092

Table 9. Zero-shot transfer to the SUN RGB-D dataset [38]. Best        Table 10. Zero-shot transfer to the iBims-1 benchmark [18]. Best
results are in bold, second best are underlined.                       results are in bold, second best are underlined.

                                                                  13
          RGB                  Ground Truth                 NeWCRF [50]               Zoe-M12-NK                   Zoe-M12-N
                  Figure 6. Zero-shot transfer to the SUN RGB-D dataset [38]. Invalid regions are indicated in gray.

Method           δ1 ↑   δ2 ↑   δ3 ↑ REL ↓ RMSE ↓ log10 ↓              Method            δ1 ↑   δ2 ↑    δ3 ↑ REL ↓ RMSE ↓ log10 ↓
BTS [20]        0.210 0.478 0.699     0.418    1.905     0.250        BTS [20]         0.225 0.419 0.582      0.476    6.404   0.329
AdaBins [5]     0.174 0.438 0.658     0.443    1.963     0.270        AdaBins [5]      0.221 0.410 0.568      0.483    6.546   0.345
LocalBins [6]   0.229 0.520 0.718     0.412    1.853     0.246        LocalBins [6]    0.234 0.432 0.594      0.468    6.362   0.320
NeWCRF [50]     0.187 0.498 0.748     0.404    1.867     0.241        NeWCRF [50]      0.255 0.464 0.638      0.442    6.017   0.283
ZoeD-X-N    0.400 0.704 0.808         0.324    1.581     0.181        ZoeD-X-N    0.284 0.502 0.692           0.421    5.889   0.267
ZoeD-NK-N   0.365 0.696 0.819         0.335    1.604     0.188        ZoeD-NK-N   0.291 0.519 0.700           0.414    5.838   0.260
ZoeD-M12-N 0.376 0.696 0.822          0.327    1.588     0.186        ZoeD-M12-N 0.292 0.514 0.706            0.410    5.771   0.257
ZoeD-M12-NK 0.386 0.695 0.807         0.331    1.598     0.185        ZoeD-M12-NK 0.274 0.494 0.696           0.419    5.830   0.262

Table 11. Zero-shot transfer to the DIODE Indoor dataset [40].        Table 12. Zero-shot transfer to the HyperSim dataset [35]. Best
Best results are in bold, second best are underlined.                 results are in bold, second best are underlined.

                                                                 14
          RGB                   Ground Truth                 NeWCRF [50]                Zoe-M12-NK                  Zoe-M12-N
                   Figure 7. Zero-shot transfer to the iBims-1 benchmark [18]. Invalid regions are indicated in gray.

Method           δ1 ↑    δ2 ↑   δ3 ↑ REL ↓ RMSE ↓ log10 ↓               Method           δ1 ↑    δ2 ↑   δ3 ↑ REL ↓ RMSE ↓ log10 ↓
BTS [20]         0.831 0.948 0.982     0.115    5.368     0.054         BTS [20]         0.805 0.945 0.982     0.147    7.550   0.067
AdaBins [5]      0.826 0.947 0.98      0.122     5.42     0.057         AdaBins [5]      0.766 0.918 0.972     0.154    8.560   0.074
LocalBins [6]    0.810 0.94 0.978      0.127    5.981     0.061         LocalBins [6]    0.777 0.930 0.978     0.151    8.139   0.071
NeWCRF [50]      0.829 0.951 0.984     0.117    5.691     0.056         NeWCRF [50]      0.874 0.974 0.991     0.119    6.183   0.054
ZoeD-X-K    0.837 0.965 0.991          0.112    5.338     0.053         ZoeD-X-K    0.790 0.95 0.985           0.137    7.734   0.066
ZoeD-NK-K   0.855 0.970 0.992          0.101    5.102     0.048         ZoeD-NK-K   0.824 0.957 0.987          0.134    7.249   0.062
ZoeD-M12-K 0.864 0.973 0.992           0.100    4.974     0.046         ZoeD-M12-K 0.835 0.962 0.988           0.129    7.108   0.060
ZoeD-M12-NK 0.850 0.965 0.991          0.105    5.095     0.050         ZoeD-M12-NK 0.824 0.951 0.980          0.138    7.225   0.066

Table 13. Zero-shot transfer to the Virtual KITTI 2 dataset [7].        Table 14. Zero-shot transfer to the DDAD dataset [12]. Best re-
Best results are in bold, second best are underlined.                   sults are in bold, second best are underlined.

                                                                   15
          RGB                   Ground Truth                NeWCRF [50]                Zoe-M12-NK                   Zoe-M12-N
                 Figure 8. Zero-shot transfer to the DIODE Indoor dataset [40]. Invalid regions are indicated in gray.

Method           δ1 ↑   δ2 ↑    δ3 ↑ REL ↓ RMSE ↓ log10 ↓              Method            δ1 ↑   δ2 ↑    δ3 ↑ REL ↓ RMSE ↓ log10 ↓
BTS [20]        0.016   0.042   0.123 1.785     5.908     0.428        BTS [20]         0.171 0.347 0.526      0.837      10.48   0.334
AdaBins [5]     0.013   0.038   0.107 1.941     6.272     0.451        AdaBins [5]      0.161 0.329 0.529      0.863      10.35   0.318
LocalBins [6]   0.016   0.044   0.124 1.82      6.706     0.434        LocalBins [6]    0.170 0.336 0.531      0.821     10.273   0.329
NeWCRF [50]     0.010   0.032   0.094 1.918     6.283     0.449        NeWCRF [50]      0.176 0.369 0.588      0.854      9.228   0.283
ZoeD-X-K    0.005       0.022 0.096   1.756     6.180     0.429        ZoeD-X-K    0.242 0.485 0.744           0.799     7.806    0.219
ZoeD-NK-K   0.004       0.012 0.047   2.068     7.432     0.473        ZoeD-NK-K   0.241 0.505 0.759           0.892     7.489    0.216
ZoeD-M12-K 0.003        0.010 0.048   1.921     6.978     0.455        ZoeD-M12-K 0.269 0.563 0.816            0.852     6.898    0.198
ZoeD-M12-NK 0.292       0.562 0.697   0.641     3.610     0.213        ZoeD-M12-NK 0.208 0.405 0.586           0.757     7.569    0.258

Table 15. Zero-shot transfer to the DIML Outdoor dataset [17].         Table 16. Zero-shot transfer to the DIODE Outdoor dataset [40].
Best results are in bold, second best are underlined.                  Best results are in bold, second best are underlined.

                                                                  16
RGB                 Ground Truth                  NeWCRF [50]                Zoe-M12-NK                    Zoe-M12-N
                            Figure 9. Zero-shot transfer to the HyperSim dataset [35].

RGB                 Ground Truth                  NeWCRF [50]                Zoe-M12-NK                    Zoe-M12-K
      Figure 10. Zero-shot transfer to the Virtual KITTI 2 dataset [7]. Invalid regions are indicated in gray.

                                                        17
RGB                            NeWCRF [50]                        Zoe-M12-NK                     Zoe-M12-K
  Figure 11. Zero-shot transfer to the DDAD dataset [12]. Ground truth depth is too sparse to visualize here.

RGB                Ground Truth                 NeWCRF [50]               Zoe-M12-NK                   Zoe-M12-K
                       Figure 12. Zero-shot transfer to the DIML Outdoor dataset [17].

                                                      18
RGB                  Ground Truth                 NeWCRF [50]               Zoe-M12-NK                   Zoe-M12-K
      Figure 13. Zero-shot transfer to the DIODE Outdoor dataset [40]. Invalid regions are indicated in gray.

                                                        19
   Method                    Encoder                # Params
   Eigen et al. [9]          -                           141M
   Laina et al. [19]         ResNet-50                    64M
   Hao et al. [13]           ResNet-101                   60M
   Lee et al. [22]           -                           119M
   Fu et al. [11]            ResNet-101                  110M
   SharpNet [31]             -                               -
   Hu et al. [14]            SENet-154                   157M
   Chen et al. [8]           SENet                       210M
   Yin et al. [48]           ResNeXt-101                 114M
   BTS [20]                  DenseNet-161                 47M
   AdaBins [5]               EfficientNet-B5              78M
   LocalBins [6]             EfficientNet-B5              74M
   NeWCRFs [50]              Swin-L                      270M
   ZoeDepth (S-L)            Swin-L                      212M
   ZoeDepth (S2-T)           Swin2-T                      42M
   ZoeDepth (S2-B)           Swin2-B                     102M
   ZoeDepth (S2-L)           Swin2-L                     214M
   ZoeDepth (B-B)            Beit-B                      112M
   ZoeDepth (B-L)            Beit-L                      345M

Table 17. Parameter comparison of ZoeDepth models with differ-
ent backbones and state of the art models. Note that the number
of parameters of ZoeDepth only varies with the backbone and is
the same for all variants trained on different dataset combinations,
e.g., ZoeD-X-N, ZoeD-M12-N and ZoeD-M12-NK, etc.

Method                  δ1 ↑ δ2 ↑ δ3 ↑ REL ↓ RMSE ↓ log10 ↓
BTS [20]               0.885 0.978 0.994 0.110       0.392     0.047
AdaBins [5]            0.903 0.984 0.997 0.103       0.364     0.044
LocalBins [6]          0.907 0.987 0.998 0.099       0.357     0.042
NeWCRFs [50]           0.922 0.992 0.998 0.095       0.334     0.041
ZoeD-M12-N (S-L) 0.937 0.992 0.998 0.086             0.310     0.037
ZoeD-M12-N (S2-T) 0.899 0.982 0.995 0.106            0.371     0.045
ZoeD-M12-N (S2-B) 0.927 0.992 0.999 0.090            0.313     0.038
ZoeD-M12-N (S2-L) 0.943 0.993 0.999 0.083            0.296     0.035
ZoeD-M12-N (B-B) 0.922 0.990 0.998 0.093             0.329     0.040
ZoeD-M12-N (B-L) 0.955 0.995 0.999 0.075             0.270     0.032

Table 18. Results on the NYU Depth V2 dataset with different
backbones. Best results are in bold, second best are underlined.

                                                                       20
