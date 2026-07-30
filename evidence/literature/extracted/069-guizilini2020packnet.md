---
source_id: 069
bibtex_key: guizilini2020packnet
title: 3D Packing for Self-Supervised Monocular Depth Estimation
year: 2020
domain_theme: Estimasi Kedalaman
verified_pdf: 69_PackNet.pdf
char_count: 70699
---

3D Packing for Self-Supervised Monocular Depth Estimation

                                                       Vitor Guizilini     Rares, Ambrus, Sudeep Pillai Allan Raventos                      Adrien Gaidon
                                                                                   Toyota Research Institute (TRI)
                                                                                         first.lastname@tri.global

                                                                  Abstract
arXiv:1905.02693v4 [cs.CV] 28 Mar 2020

                                             Although cameras are ubiquitous, robotic platforms typ-
                                         ically rely on active sensors like LiDAR for direct 3D per-
                                         ception. In this work, we propose a novel self-supervised
                                         monocular depth estimation method combining geometry
                                         with a new deep network, PackNet, learned only from unla-
                                         beled monocular videos. Our architecture leverages novel
                                         symmetrical packing and unpacking blocks to jointly learn
                                         to compress and decompress detail-preserving representa-
                                         tions using 3D convolutions. Although self-supervised, our
                                         method outperforms other self, semi, and fully supervised
                                         methods on the KITTI benchmark. The 3D inductive bias in
                                         PackNet enables it to scale with input resolution and num-
                                         ber of parameters without overfitting, generalizing better on
                                         out-of-domain data such as the NuScenes dataset. Further-
                                         more, it does not require large-scale supervised pretraining
                                         on ImageNet and can run in real-time. Finally, we release
                                         DDAD (Dense Depth for Automated Driving), a new urban
                                                                                                             Figure 1: Example metrically accurate PackNet predic-
                                         driving dataset with more challenging and accurate depth
                                                                                                             tion (map and textured point cloud) on our DDAD dataset.
                                         evaluation, thanks to longer-range and denser ground-truth
                                         depth generated from high-density LiDARs mounted on a               estimation have mostly focused on engineering the loss
                                         fleet of self-driving cars operating world-wide.†                   function [6, 34, 48, 54], we show that performance criti-
                                                                                                             cally depends on the model architecture, in line with the
                                         1. Introduction
                                                                                                             observations of [28] for other self-supervised tasks. Going
                                            Accurate depth estimation is a key prerequisite in many          beyond image classification models like ResNet [21], our
                                         robotics tasks, including perception, navigation, and plan-         main contribution is a new convolutional network archi-
                                         ning. Depth from monocular camera configurations can                tecture, called PackNet, for high-resolution self-supervised
                                         provide useful cues for a wide array of tasks [24, 31, 35,          monocular depth estimation. We propose new packing and
                                         37], producing dense depth maps that could complement               unpacking blocks that jointly leverage 3D convolutions to
                                         or eventually replace expensive range sensors. However,             learn representations that maximally propagate dense ap-
                                         learning monocular depth via direct supervision requires            pearance and geometric information while still being able
                                         ground-truth information from additional sensors and pre-           to run in real time. Our second contribution is a novel
                                         cise cross-calibration. Self-supervised methods do not suf-         loss that can optionally leverage the camera’s velocity when
                                         fer from these limitations, as they use geometrical con-            available (e.g., from cars, robots, mobile phones) to solve
                                         straints on image sequences as the sole source of supervi-          the inherent scale ambiguity in monocular vision. Our
                                         sion. In this work, we address the problem of jointly esti-         third contribution is a new dataset: Dense Depth for Au-
                                         mating scene structure and camera motion across RGB im-             tomated Driving (DDAD). It leverages diverse logs from a
                                         age sequences using a self-supervised deep network.                 fleet of well-calibrated self-driving cars equipped with cam-
                                            While recent works in self-supervised monocular depth            eras and high-accuracy long-range LiDARs. Compared to
                                            † Video: https://www.youtube.com/watch?v=b62iDkLgGSI
                                                                                                             existing benchmarks, DDAD enables much more accurate
                                            † Dataset:https://github.com/TRI-ML/DDAD                         depth evaluation at range, which is key for high resolution
                                            † Code: https://github.com/TRI-ML/packnet-sfm                    monocular depth estimation methods (cf. Figure 1).

                                                                                                         1
    Our experiments on the standard KITTI benchmark [17],          vided an alternative strategy involving training a monocu-
the recent NuScenes dataset [5], and our new proposed              lar depth network with stereo cameras, without requiring
DDAD benchmark show that our self-supervised monocu-               ground-truth depth labels. By leveraging Spatial Trans-
lar approach i) improves on the state of the art, especially at    former Networks [23], Godard et al [18] use stereo imagery
longer ranges; ii) is competitive with fully supervised meth-      to geometrically transform the right image plus a predicted
ods; iii) generalizes better on unseen data; iv) scales better     depth of the left image into a synthesized left image. The
with number of parameters, input resolution, and more unla-        loss between the resulting synthesized and original left im-
beled training data; v) can run in real time at high resolution;   ages is then defined in a fully-differentiable manner, using
and vi) does not require supervised pretraining on ImageNet        a Structural Similarity [45] term and additional depth regu-
to achieve state-of-the-art results; or test-time ground-truth     larization terms, thus allowing the depth network to be self-
scaling if velocity information is available at training time.     supervised in an end-to-end fashion.
                                                                      Following [18] and [43], Zhou et al. [53] generalize
2. Related Work                                                    this to self-supervised training in the purely monocular set-
   Depth estimation from a single image poses several chal-        ting, where a depth and pose network are simultaneously
lenges due to its ill-posed and ambiguous nature. However,         learned from unlabeled monocular videos. Several meth-
modern convolutional networks have shown that it is pos-           ods [6, 27, 34, 44, 47, 48, 52, 54] have advanced this line
sible to successfully leverage appearance-based patterns in        terms,of work by incorporatingthese methods, ad,ditional
large scale datasets in order to make accurate predictions.        loss and constraints. All, however, take advantage of con-
                                                                   straints in monocular Structure-from-Motion (SfM) training
                                                                   that only allow the estimation of depth and pose up to an
Depth Network Architectures Eigen et al. [14] proposed             unknown scale factor, and rely on the ground-truth LiDAR
one of the earliest works in convolutional-based depth esti-       measu,rements to scale their depth estimates appropriately
mation using a multi-scale deep network trained on RGB-            for evaluation purposes [53]. Instead, in this work we show
D sensor data to regress the depth directly from single im-        that, by simply using the instantaneous velocity of the cam-
ages. Subsequent works extended these network architec-            era during training, we are able to learn a scale-aware depth
tures to perform two-view stereo disparity estimation [36]         and pose model, alleviating the impractical need to use Li-
using techniques developed in the flow estimation litera-          DAR ground-truth depth measurements at test-time.
ture [13]. Following [13, 36], Umenhofer et al. [43] applied
these concepts to simultaneously train a depth and pose net-
                                                                   3. Self-Supervised Scale-Aware SfM
work to predict depth and camera ego-motion between suc-
cessive unconstrained image pairs.                                    In self-supervised monocular SfM training (Fig. 2), we
   Independently, dense pixel-prediction networks [3, 32,          aim to learn: (i) a monocular depth model fD : I → D,
49] have made significant progress towards improving the           that predicts the scale-ambiguous depth D̂ = fD (I(p)) for
flow of information between encoding and decoding lay-             every pixel p in the target image I; and (ii) a monocular
ers. Fractional pooling [20] was introduced to amortize the        ego-motion estimator fx : (It , IS ) → xt→S , that predicts
rapid spatial reduction during downsampling. Lee et al. [30]       the set of 6-DoF rigid transformations for all s ∈ S given
generalized the pooling function to allow the learning of          by xt→s = ( R     t
                                                                                   0 1 ) ∈ SE(3), between the target image It
more complex patterns, including linear combinations and           and the set of source images Is ∈ IS considered as part of
learnable pooling operations. Shi et al. [40] used sub-pixel       the temporal context. In practice, we use the frames It−1
convolutions to perform Single-Image-Super-Resolution,             and It+1 as source images, although using a larger context
synthesizing and super-resolving images beyond their in-           is possible. Note that in the case of monocular SfM both
put resolutions, while still operating at lower resolutions.       depth and pose are estimated up to an unknown scale factor,
Recent works [39, 52] in self-supervised monocular depth           due to the inherent ambiguity of the photometric loss.
estimation use this concept to super-resolve estimates and
further improve performance. Here, we go one step further          3.1. Self-Supervised Objective
and introduce new operations relying on 3D convolutions               Following the work of Zhou et al. [53], we train the depth
for learning to preserve and process spatial information in        and pose network simultaneously in a self-supervised man-
the features of encoding and decoding layers.                      ner. In this work, however, we learn to recover the inverse-
                                                                                      −1
                                                                   depth fd : I → fD     (I) instead, along with the ego-motion
Self-Supervised Monocular Depth and Pose As super-                 estimator fx . Similar to [53], the overall self-supervised
vised techniques for depth estimation advanced rapidly, the        objective consists of an appearance matching loss term Lp
availability of target depth labels became challenging, es-        that is imposed between the synthesized target image Iˆt and
pecially for outdoor applications. To this end, [16, 18] pro-      the target image It , and a depth regularization term Ls that
ensures edge-aware smoothing in the depth estimates D̂t .                                      Photometric Loss
The objective takes the following form:

   L(It , Iˆt ) = Lp (It , IS )   Mp       Mt + λ1 Ls (D̂t )     (1)                                                        View
                                                                                            PackNet
                                                                                                                          Synthesis

where Mt is a binary mask that avoids computing the pho-
tometric loss on the pixels that do not have a valid map-
ping, and      denotes element-wise multiplication. Addi-                                 Pose
                                                                                         ConvNet
tionally, λ1 enforces a weighted depth regularization on the
objective. The overall loss in Equation 1 is averaged per-
pixel, pyramid-scale and image batch during training. Fig. 2                            Velocity Supervision Loss
shows a high-level overview of our training pipeline.
   Appearance Matching Loss. Following [18, 53] the                    Figure 2: PackNet-SfM: Our proposed scale-aware self-
pixel-level similarity between the target image It and the             supervised monocular structure-from-motion architecture.
synthesized target image Iˆt is estimated using the Structural         We introduce PackNet as a novel depth network, and op-
Similarity (SSIM) [45] term combined with an L1 pixel-                 tionally include weak velocity supervision at training time
wise loss term, inducing an overall photometric loss given             to produce scale-aware depth and pose models.
by Equation 2 below.
                                                                       3.2. Scale-Aware SfM
                                   ˆ
  Lp (It , Iˆt ) = α 1−SSIM(I
                          2
                              t ,It )
                                      + (1 − α) kIt − Iˆt k (2)            As previously mentioned, both the monocular depth and
                                                                       ego-motion estimators fd and fx predict scale-ambiguous
While multi-view projective geometry provides strong cues              values, due to the limitations of the monocular SfM training
for self-supervision, errors due to parallax in the scene have         objective. In other words, the scene depth and the camera
an undesirable effect incurred on the photometric loss. We             ego-motion can only be estimated up to an unknown and
mitigate these undesirable effects by calculating the mini-            ambiguous scale factor. This is also reflected in the overall
mum photometric loss per pixel for each source image in                learning objective, where the photometric loss is agnostic to
the context IS , as shown in [19], so that:                            the metric depth of the scene. Furthermore, we note that all
                                                                       previous approaches which operate in the self-supervised
                  Lp (It , IS ) = min Lp (It , Iˆt )             (3)
                                    IS                                 monocular regime [6, 16, 18, 34] suffer from this limita-
                                                                       tion, and resort to artificially incorporating this scale factor
The intuition is that the same pixel will not be occluded or           at test-time, using LiDAR measurements.
out-of-bounds in all context images, and that the associa-
tion with minimal photometric loss should be the correct                   Velocity Supervision Loss. Since instantaneous veloc-
one. Furthermore, we also mask out static pixels by remov-             ity measurements are ubiquitous in most mobile systems to-
ing those which have a warped photometric loss Lp (It , Iˆt )          day, we show that they can be directly incorporated in our
higher than their corresponding unwarped photometric loss              self-supervised objective to learn a metrically accurate and
Lp (It , Is ), calculated using the original source image with-        scale-aware monocular depth estimator. During training,
out view synthesis. Introduced in [19], this auto-mask re-             we impose an additional loss Lv between the magnitude
moves pixels whose appearance does not change between                  of the pose-translation component of the pose network pre-
frames, which includes static scenes and dynamic objects               diction t̂ and the measured instantaneous velocity scalar v
with no relative motion, since these will have a smaller pho-          multiplied by the time difference between target and source
tometric loss when assuming no ego-motion.                             frames ∆Tt→s , as shown below:
                                                                                  Lv (t̂t→s , v) = kt̂t→s k − |v|∆Tt→s                   (6)
           Mp = min Lp (It , Is ) > min Lp (It , Iˆt )           (4)
                      IS                   IS
                                                                       Our final scale-aware self-supervised objective loss Lscale
    Depth Smoothness Loss. In order to regularize the                  from Equation 1 becomes:
depth in texture-less low-image gradient regions, we incor-                   Lscale (It , Iˆt , v) = L(It , Iˆt ) + λ2 Lv (t̂t→s , v)   (7)
porate an edge-aware term (Equation 5), similar to [18].
The loss is weighted for each of the pyramid-levels, and               where λ2 is a weight used to balance the different loss
is decayed by a factor of 2 on down-sampling, starting with            terms. This additional velocity loss allows the pose net-
a weight of 1 for the 0th pyramid level.                               work to make metrically accurate predictions, subsequently
                                                                       resulting in the depth network also learning metrically ac-
         Ls (D̂t ) = |δx D̂t |e−|δx It | + |δy D̂t |e−|δy It |   (5)   curate estimates to maintain consistency (cf. Section 5.4).
                                                                          Layer Description                                 K   Output Tensor Dim.
                                                                    #0    Input RGB image                                           3×H×W
                                                                                                     Encoding Layers
                                                                    #1    Conv2d                                            5        64×H×W
                                                                    #2    Conv2d → Packing                                  7      64×H/2×W/2
                                                                    #3    ResidualBlock (x2) → Packing                      3      64×H/4×W/4
                                                                    #4    ResidualBlock (x2) → Packing                      3     128×H/8×W/8
                                                                    #5    ResidualBlock (x3) → Packing                      3    256×H/16×W/16
                                                                    #6    ResidualBlock (x3) → Packing                      3    512×H/32×W/32
                                                                                                    Decoding Layers
                                                                    #7    Unpacking (#6) → Conv2d (⊕ #5)                    3    512×H/16×W/16
                                                                    #8    Unpacking (#7) → Conv2d (⊕ #4)                    3     256×H/8×W/8
                                                                    #9    InvDepth (#8)                                     3       1×H/8×W/8
                                                                    #10   Unpacking (#8) → Conv2d (⊕ #3 ⊕ Upsample(#9))     3     128×H/4×W/4
                                                                    #11   InvDepth (#10)                                    3       1×H/4×W/4
                                                                    #12   Unpacking (#10) → Conv2d (⊕ #2 ⊕ Upsample(#11))   3      64×H/2×W/2
                                                                    #13   InvDepth (#12)                                    3       1×H/2×W/2
                                                                    #14   Unpacking (#12) → Conv2d (⊕ #1 ⊕ Upsample(#13))   3        64×H×W
                                                                    #15   InvDepth (#14)                                    3         1×H×W

            (a) Packing                (b) Unpacking               Table 1: Summary of our PackNet architecture for self-
                                                                   supervised monocular depth estimation. The Packing and
Figure 3: Proposed 3D packing and unpacking blocks.                Unpacking blocks are described in Fig. 3, with kernel size
Packing replaces striding and pooling, while unpacking is          K = 3 and D = 8. Conv2d blocks include Group-
its symmetrical feature upsampling mechanism.                      Norm [46] with G = 16 and ELU non-linearities [8]. In-
                                                                   vDepth blocks include a 2D convolutional layer with K = 3
4. PackNet: 3D Packing for Depth Estimation                        and sigmoid non-linearities. Each ResidualBlock is a se-
                                                                   quence of 3 2D convolutional layers with K = 3/3/1 and
    Standard convolutional architectures use aggressive            ELU non-linearities, followed by GroupNorm with G = 16
striding and pooling to increase their receptive field size.       and Dropout [41] of 0.5 in the final layer. Upsample is a
However, this potentially decreases model performance for          nearest-neighbor resizing operation. Numbers in parenthe-
tasks requiring fine-grained representations [20, 50]. Simi-       ses indicate input layers, with ⊕ as channel concatenation.
larly, traditional upsampling strategies [7, 12] fail to prop-     Bold numbers indicate the four inverse depth output scales.
agate and preserve sufficient details at the decoder layers
to recover accurate depth predictions. In contrast, we pro-
pose a novel encoder-decoder architecture, called PackNet,         representation via a 3D convolutional layer. The result-
that introduces new 3D packing and unpacking blocks to             ing higher dimensional feature space is then flattened (by
learn to jointly preserve and recover important spatial in-        simple reshaping) before a final 2D convolutional contrac-
formation for depth estimation. This is in alignment with          tion layer. This structured feature expansion-contraction,
recent observations that information loss is not a necessary       inspired by invertible networks [4, 22] although we do not
condition to learn representations capable of generalizing to      ensure invertibility, allows our architecture to dedicate more
different scenarios [22]. In fact, progressive expansion and       parameters to learn how to compress key spatial details that
contraction in a fully invertible manner, without discard-         need to be preserved for high resolution depth decoding.
ing “uninformative” input variability, has been shown to in-
crease performance in a wide variety of tasks [4, 11, 26].         4.2. Unpacking Block
We first describe the different blocks of our proposed archi-          Symmetrically, the unpacking block (Fig. 3b) learns to
tecture, and then proceed to show how they are integrated          decompress and unfold packed convolutional feature chan-
together in a single model for monocular depth estimation.         nels back into higher resolution spatial dimensions dur-
                                                                   ing the decoding process. The unpacking block replaces
4.1. Packing Block
                                                                   convolutional feature upsampling, typically performed via
   The packing block (Fig. 3a) starts by folding the spatial       nearest-neighbor or with learnable transposed convolutional
dimensions of convolutional feature maps into extra feature        weights. It is inspired by sub-pixel convolutions [40], but
channels via a Space2Depth operation [40]. The result-             adapted to reverse the 3D packing process that the features
ing tensor is at a reduced resolution, but in contrast to strid-   went through in the encoder. First, we use a 2D convolu-
ing or pooling, this transformation is invertible and comes        tional layer to produce the required number of feature chan-
at no loss. Next, we learn to compress this concatenated           nels for a following 3D convolutional layer. Second, this
feature space in order to reduce its dimensionality to a de-       3D convolution learns to expand back the compressed spa-
sired number of output channels. As we show in our exper-          tial features. Third, these unpacked features are converted
iments (cf. Section 5.6), 2D convolutions are not designed         back to spatial details via a reshape and Depth2Space
to directly leverage the tiled structure of this feature space.    operation [40] to obtain a tensor with the desired number of
Instead, we propose to first learn to expand this structured       output channels and target higher resolution.
                                                                  information to handle moving objects, resulting in 652 high-
                                                                  quality depth maps.
                                                                      DDAD (Dense Depth for Automated Driving). As one
                                                                  of our contributions, we release a diverse dataset of urban,
    (a) Input Image    (b) Max Pooling +    (c) Pack + Unpack     highway, and residential scenes curated from a global fleet
                       Bilinear Upsample
                                                                  of self-driving cars. It contains 17,050 training and 4,150
Figure 4: Image reconstruction using different encoder-           evaluation frames with ground-truth depth maps generated
decoders: (b) standard max pooling and bilinear upsam-            from dense LiDAR measurements using the Luminar-H2
pling, each followed by 2D convolutions; (c) one packing-         sensor. This new dataset is a more realistic and challenging
unpacking combination (cf. Fig. 3) with D = 2. All kernel         benchmark for depth estimation, as it is diverse and cap-
sizes are K = 3 and C = 4 for intermediate channels.              tures precise structure across images (30k points per frame)
                                                                  at longer ranges (up to 200m vs 80m for previous datasets).
4.3. Detail-Preserving Properties                                 See supplementary material for more details.
   In Fig. 4, we illustrate the detail-preserving properties of       NuScenes [5]. To assess the generalization capability of
our packing / unpacking combination, showing we can get a         our approach w.r.t. previous ones, we evaluate KITTI mod-
near-lossless encoder-decoder for single image reconstruc-        els (without fine-tuning) on the official NuScenes validation
tion by minimizing the L1 loss. We train a simple network         dataset of 6019 front-facing images with ground-truth depth
composed of one packing layer followed by a symmetrical           maps generated by LiDAR reprojection.
unpacking one and show it is able to almost exactly recon-            CityScapes [9]. We also experiment with pretraining our
struct the input image (final loss of 0.0079), including sharp    monocular networks on the CityScapes dataset, before fine-
edges and finer details. In contrast, a comparable baseline       tuning on the KITTI dataset. This also allows us to explore
replacing packing / unpacking with max pooling / bilinear         the scalability and generalization performance of different
upsampling (and keeping the 2D convolutions) is only able         models, as they are trained with increasing amounts of un-
to learn a blurry reconstruction (final loss of 0.063). This      labeled data. A total of 88250 images were considered as
highlights how PackNet is able to learn more complex fea-         the training split for the CityScapes dataset, using the same
tures by preserving spatial and appearance information end-       training parameters as KITTI for 20 epochs.
to-end throughout the network.
                                                                  5.2. Implementation Details
4.4. Model Architecture                                              We use PyTorch [38] with all models trained across 8
   Our PackNet architecture for self-supervised monocular         Titan V100 GPUs. We use the Adam optimizer [25], with
depth estimation is detailed in Table 1. Our symmetrical          β1 = 0.9 and β2 = 0.999. The monocular depth and pose
encoder-decoder architecture incorporates several packing         networks are trained for 100 epochs, with a batch size of 4
and unpacking blocks, and is supplemented with skip con-          and initial depth and pose learning rates of 2 · 10−4 and 5 ·
nections [36] to facilitate the flow of information and gra-      10−4 respectively. Training sequences are generated using
dients throughout the network. The decoder produces inter-        a stride of 1, meaning that the previous t − 1, current t,
mediate inverse depth maps that are upsampled before being        and posterior t + 1 images are used in the loss calculation.
concatenated with their corresponding skip connections and        As training proceeds, the learning rate is decayed every 40
unpacked feature maps. These intermediate inverse depth           epochs by a factor of 2. We set the SSIM weight to α =
maps are also used at training time in the loss calculation,      0.85, the depth regularization weight to λ1 = 0.001 and,
after being upsampled to to the full output resolution using      where applicable, the velocity-scaling weight to λ2 = 0.05.
nearest neighbors interpolation.                                     Depth Network. Unless noted otherwise, we use our
                                                                  PackNet architecture as specified in Table 1. During train-
5. Experiments                                                    ing, all four inverse depth output scales are used in the loss
                                                                  calculation, and at test-time only the final output scale is
5.1. Datasets                                                     used, after being resized to the full ground-truth depth map
    KITTI [17]. The KITTI benchmark is the de facto stan-         resolution using nearest neighbor interpolation.
dard for depth evaluation. More specifically, we adopt the           Pose Network. We use the architecture proposed by [53]
training protocol used in Eigen et al. [14], with Zhou et         without the explainability mask, which we found not to im-
al.’s [53] pre-processing to remove static frames. This re-       prove results. The pose network consists of 7 convolutional
sults in 39810 images for training, 4424 for validation and       layers followed by a final 1 × 1 convolutional layer. The
697 for evaluation. We also consider the improved ground-         input to the network consists of the target view It and the
truth depth maps from [42] for evaluation, which uses 5           context views IS , and the output is the set of 6 DOF trans-
consecutive frames to accumulate LiDAR points and stereo          formations between It and Is , for s ∈ S.
5.3. Depth Estimation Performance
    First, we report the performance of our proposed monoc-
ular depth estimation method when considering longer dis-
tances, which is now possible due to the introduction of
our new DDAD dataset. Depth estimation results using this
dataset for training and evaluation, considering cumulative
distances up to 200m, can be found in Fig. 5 and Table 2.
Additionally, in Fig. 6 we present results for different depth
intervals calculated independently. From these results we        Figure 5: PackNet pointcloud reconstructions on DDAD.
can see that our PackNet-SfM approach significantly out-
performs the state-of-the-art [19], based on the ResNet fam-     Method              Abs Rel Sq Rel RMSE RMSElog δ1.25
ily, the performance gap consistently increasing when larger
                                                                 Monodepth2 (R18)      0.381   8.387   21.277   0.371   0.587
distances are considered.                                        Monodepth2‡ (R18)     0.213   4.975   18.051   0.340   0.761
    Second, we evaluate depth predictions on KITTI using         Monodepth2 (R50)      0.324   7.348   20.538   0.344   0.615
the metrics described in Eigen et al. [14]. We summarize         Monodepth2‡ (R50)     0.198   4.504   16.641   0.318   0.781
our results in Table 3, for the original depth maps from [14]    PackNet-SfM           0.162   3.917   13.452   0.269   0.823
and the accumulated depth maps from [42], and illustrate         Table 2: Depth Evaluation on DDAD, for 640 x 384 res-
their performance qualitatively in Fig. 7. In contrast to pre-   olution and distances up to 200m. While the ResNet fam-
vious methods [6, 19] that predominantly focus on modify-        ily heavily relies on large-scale supervised ImageNet [10]
ing the training objective, we show that our proposed Pack-      pretraining (denoted by ‡), PackNet achieves significantly
Net architecture can by itself bolster performance and es-       better results despite being trained from scratch.
tablish a new state of the art for the task of monocular depth
estimation, trained in the self-supervised monocular setting.
    Furthermore, we show that by simply introducing an ad-
ditional source of unlabeled videos, such as the publicly
available CityScapes dataset (CS+K) [9], we are able to fur-
ther improve monocular depth estimation performance. As
indicated by Pillai et al. [39], we also observe an improve-
ment in performance at higher image resolutions, which
we attribute to the proposed network’s ability to properly
preserve and process spatial information end-to-end. Our         Figure 6: Depth Evaluation on DDAD binned at differ-
best results are achieved when injecting both more unla-         ent intervals, calculated independently by only considering
beled data at training time and processing higher resolution     ground-truth depth pixels in that range (0-20m, 20-40m, ...).
input images, achieving performance comparable to semi-
supervised [29] and fully supervised [15] methods.               5.5. Network Complexity

5.4. Scale-Aware Depth Estimation Performance                       The introduction of packing and unpacking as alterna-
                                                                 tives to standard downsampling and upsampling operations
   Due to their inherent scale ambiguity, self-supervised        increases the complexity of the network, due to the num-
monocular methods [19, 34, 53] evaluate depth by scaling         ber of added parameters. To ensure that the gain in perfor-
their estimates to the median ground-truth as measured via       mance shown in our experiments is not only due to an in-
LiDAR. In Section 3.2 we propose to also recover the metric      crease in model capacity, we compare different variations of
scale of the scene from a single image by imposing a loss        our PackNet architecture (obtained by modifying the num-
on the magnitude of the translation for the pose network         ber of layers and feature channels) against available ResNet
output. Table 3 shows that introducing this weak velocity        architectures. These results are depicted in Fig. 8 and show
supervision at training time allows the generation of scale-     that, while the ResNet family stabilizes with diminishing
aware depth models with similar performance as their un-         returns as the number of parameters increase, the PackNet
scaled counterparts, with the added benefit of not requiring     family matches its performance at around 70M parameters
ground-truth depth scaling (or even velocity information) at     and further improves as more complexity is added. Finally,
test-time. Another benefit of scale-awareness is that we can     the proposed architecture (Table 1) reaches around 128M
compose metrically accurate trajectories directly from the       parameters with an inference time of 60ms on a Titan V100
output of the pose network. Due to space constraints, we         GPU, which can be further improved to < 30ms using Ten-
report pose estimation results in supplementary material.        sorRT [1], making it suitable for real-time applications.
                  Method                    Supervision Resolution Dataset Abs Rel Sq Rel RMSE RMSElog δ < 1.25 δ < 1.252 δ < 1.253
                  SfMLearner [53]               M      416 x 128 CS + K     0.198   1.836   6.565     0.275     0.718    0.901     0.960
                  Vid2Depth [34]                M      416 x 128 CS + K     0.159   1.231   5.912     0.243     0.784    0.923     0.970
                  DF-Net [54]                   M      576 x 160 CS + K     0.146   1.182   5.215     0.213     0.818    0.943     0.978
                  Struct2Depth [6]              M      416 x 128   K        0.141   1.026   5.291     0.215     0.816    0.945     0.979
                  Zhou et al.‡ [51]             M      1248 x 384  K        0.121   0.837   4.945     0.197     0.853    0.955     0.982
                  Monodepth2‡ [19]              M       640 x 192  K        0.115   0.903   4.863     0.193     0.877    0.959     0.981
  Original [14]

                  Monodepth2‡ [19]              M      1024 x 320  K        0.115   0.882   4.701     0.190     0.879    0.961     0.982
                  PackNet-SfM                  M       640 x 192   K        0.111   0.785   4.601     0.189     0.878    0.960     0.982
                  PackNet-SfM                 M+v      640 x 192   K        0.111   0.829   4.788     0.199     0.864    0.954     0.980
                  PackNet-SfM                  M       640 x 192 CS + K     0.108   0.727   4.426     0.184     0.885    0.963     0.983
                  PackNet-SfM                 M+v      640 x 192 CS + K     0.108   0.803   4.642     0.195     0.875    0.958     0.980
                  PackNet-SfM                  M       1280 x 384   K       0.107   0.802   4.538     0.186     0.889    0.962     0.981
                  PackNet-SfM                 M+v      1280 x 384   K       0.107   0.803   4.566     0.197     0.876    0.957     0.979
                  PackNet-SfM                  M       1280 x 384 CS + K    0.104   0.758   4.386     0.182     0.895    0.964     0.982
                  PackNet-SfM                 M+v      1280 x 384 CS + K    0.103   0.796   4.404     0.189     0.881    0.959     0.980
                  SfMLeaner [53]                M      416 x 128   CS + K   0.176   1.532   6.129     0.244     0.758    0.921     0.971
                  Vid2Depth [34]                M      416 x 128   CS + K   0.134   0.983   5.501     0.203     0.827    0.944     0.981
                  GeoNet [48]                   M      416 x 128   CS + K   0.132   0.994   5.240     0.193     0.883    0.953     0.985
  Improved [42]

                  DDVO [44]                     M      416 x 128   CS + K   0.126   0.866   4.932     0.185     0.851    0.958     0.986
                  EPC++ [33]                    M      640 x 192     K      0.120   0.789   4.755     0.177     0.856    0.961     0.987
                  Monodepth2‡ [19]              M      640 x 192     K      0.090   0.545   3.942     0.137     0.914    0.983     0.995
                  Kuznietsov et al.‡ [29]       D      621 x 187     K      0.089   0.478   3.610     0.138     0.906    0.980     0.995
                  DORN‡ [15]                    D      513 x 385     K      0.072   0.307   2.727     0.120     0.932    0.984     0.995
                  PackNet-SfM                  M        640 x 192   K       0.078   0.420   3.485     0.121     0.931    0.986     0.996
                  PackNet-SfM                  M       1280 x 384 CS + K    0.071   0.359   3.153     0.109     0.944    0.990     0.997
                  PackNet-SfM                 M+v      1280 x 384 CS + K    0.075   0.384   3.293     0.114     0.938    0.984     0.995

Table 3: Quantitative performance comparison of PackNet-SfM on the KITTI dataset for distances up to 80m. For
Abs Rel, Sq Rel, RMSE and RMSElog lower is better, and for δ < 1.25, δ < 1.252 and δ < 1.253 higher is better. In the
Dataset column, CS+K refers to pretraining on CityScapes (CS) and fine-tuning on KITTI (K). M refers to methods that train
using monocular (M) images, and M+v refers to added velocity weak supervision (v), as shown in Section 3.2. ‡ indicates
ImageNet [10] pretraining. Original uses raw depth maps from [14] for evaluation, and Improved uses annotated depth maps
from [42]. At test-time, all monocular methods (M) scale estimated depths with median ground-truth LiDAR information.
Velocity-scaled (M+v) and supervised (D) methods are not scaled in such way, since they are already metrically accurate.

                     Input image                PackNet-SfM          Monodepth2 [19]                DORN [15]           SfMLearner [53]

Figure 7: Qualitative monocular depth estimation performance comparing PackNet with previous methods, on frames
from the KITTI dataset (Eigen test split). Our method is able to capture sharper details and structure (e.g., on vehicles,
pedestrians, and thin poles) thanks to the learned preservation of spatial information.
                                                                   Depth Network       Abs Rel Sq Rel RMSE RMSElog δ1.25
                                                                   ResNet18             0.133   1.023   5.123     0.211     0.845
                                                                   ResNet18‡            0.120   0.896   4.869     0.198     0.868
                                                                   ResNet50             0.127   0.977   5.023     0.205     0.856
                                                                   ResNet50‡            0.117   0.900   4.826     0.196     0.873
                                                                   PackNet
                                                                   (w/o pack/unpack)    0.122   0.880 4.816       0.198     0.864
                                                                   PackNet (D = 0)      0.121   0.922   4.831     0.195     0.869
                                                                   PackNet (D = 2)      0.118   0.802   4.656     0.194     0.868
                                                                   PackNet (D = 4)      0.113   0.818   4.621     0.190     0.875
Figure 8: Performance of different depth network ar-               PackNet (D = 8)      0.111   0.785   4.601     0.189     0.878
chitectures for varying numbers of parameters on the
original KITTI Eigen split [14] with resolutions of 640 x         Table 4: Ablation study on the PackNet architecture,
192 (MR) and 1280 x 384 (HR). While the ResNet family             on the standand KITTI benchmark for 640 x 192 resolu-
plateaus at 70M parameters, the PackNet family matches its        tion. ResNetXX indicates that specific architecture [21] as
performance at the same number of parameters for MR, out-         encoder, with and without ImageNet [10] pretraining (de-
performs it clearly for HR, and improves significantly with       noted with ‡). We also show results with the proposed Pack-
more parameters in both cases without overfitting.                Net architecture, first without packing and unpacking (re-
                                                                  placed respectively with convolutional striding and bilinear
   The PackNet family is also consistently better at higher       upsampling) and then with increasing numbers of 3D con-
resolution, as it properly preserves and propagates spatial       volutional filters (D = 0 indicates no 3D convolutions and
information between layers. In contrast, as reported in prior     the corresponding reshape operations).
works [19], ResNet architectures do not scale well, with
only minor improvements at higher resolution.                         Method      Abs Rel Sq Rel RMSE RMSElog δ1.25
5.6. Ablation Studies                                                 ResNet18    0.218    2.053   8.154        0.355     0.650
                                                                      ResNet18‡   0.212    1.918   7.958        0.323     0.674
    To further study the performance improvements that                ResNet50    0.216    2.165   8.477        0.371     0.637
PackNet provides, we perform an ablative analysis on the              ResNet50‡   0.210    2.017   8.111        0.328     0.697
different architectural components introduced, as depicted            PackNet     0.187    1.852   7.636        0.289     0.742
in Table 4. We show that the base architecture, without
                                                                  Table 5: Generalization capability of different depth net-
the proposed packing and unpacking blocks, already pro-
                                                                  works, trained on both KITTI and CityScapes and evalu-
duces a strong baseline for the monocular depth estimation
                                                                  ated on NuScenes [5], for 640 x 192 resolution and dis-
task. The introduction of packing and unpacking boosts
                                                                  tances up to 80m. ‡ denotes ImageNet [10] pretraining.
depth estimation performance, especially as more 3D con-
volutional filters are added, with new state-of-the-art results   vehicles and countries (Germany for CS+K, USA + Singa-
being achieved by the architecture described in Table 1.          pore for NuScenes), outperforming standard architectures
    As mentioned in [15, 19], ResNet architectures highly         in all considered metrics without the need for large-scale
benefit from ImageNet pretraining, since they were origi-         supervised pretraining on ImageNet.
nally developed for classification tasks. Interestingly, we
also noticed that the performance of pretrained ResNet ar-
                                                                  6. Conclusion
chitectures degrades in longer training periods, due to catas-       We propose a new convolutional network architecture for
trophic forgetting that leads to overfitting. The proposed        self-supervised monocular depth estimation: PackNet. It
PackNet architecture, on the other hand, achieves state-of-       leverages novel, symmetrical, detail-preserving packing and
the-art results from randomly initialized weights, and can        unpacking blocks that jointly learn to compress and decom-
be further improved by self-supervised pretraining on other       press high resolution visual information for fine-grained
datasets, thus properly leveraging the large-scale availabil-     predictions. Although purely trained on unlabeled monoc-
ity of unlabeled information thanks to its structure.             ular videos, our approach outperforms other existing self-
                                                                  and semi-supervised methods and is even competitive with
5.7. Generalization Capability
                                                                  fully-supervised methods while able to run in real-time. It
   We also investigate the generalization performance of          also generalizes better to different datasets and unseen en-
PackNet, as evidence that it does not simply memorize train-      vironments without the need for ImageNet pretraining, es-
ing data but learns transferable discriminative features. To      pecially when considering longer depth ranges, as assessed
assess this, we evaluate on the recent NuScenes dataset [5]       up to 200m on our new DDAD dataset. Additionally, by
models trained on a combination of CityScapes and KITTI           leveraging during training only weak velocity information,
(CS+K), without any fine-tuning. Results in Table 5 show          we are able to make our model scale-aware, i.e. producing
PackNet indeed generalizes better across a large spectrum of      metrically accurate depth maps from a single image.
Acknowledgments                                                      B. Dense Depth for Automated Driving
   We would like to thank John Leonard and Wolfram Bur-
                                                                        (DDAD)
gard for their support and insightful comments during the                In this section, we provide a brief overview of our newly
development of this work.                                            introduced DDAD (Dense Depth for Automated Driving)
                                                                     dataset and the relevant properties that make it desirable as
A. Pose evaluation                                                   a dense depth estimation benchmark. It includes a high-
                                                                     resolution, long-range Luminar-H21 as the LiDAR sensor
   In Table 6 we show the results of our proposed PackNet-           used to generate pointclouds, with a maximum range of
SfM framework on the KITTI odometry benchmark [17].                  250m and sub-1cm range precision. Additionally, it con-
To compare with related methods, we train our framework              tains six calibrated cameras time-synchronized at 10 Hz,
from scratch on sequences 00-08 of the KITTI odometry                that together produce a 360◦ coverage around the vehicle.
benchmark, with exactly the same parameters and networks             Note that in our work we only use information from the
used for depth evaluation (Table 3, main text). For consis-          front-facing camera for training and evaluation.
tency with related methods, we compute the Absolute Tra-                 Examples of a Luminar-H2 pointcloud projected onto
jectory Error (ATE) averaged over all 5-frame snippets on            each of these six cameras are shown in Figures 10, 11 and
sequences 09 and 10. Note that our pose network only takes           12, for different urban settings. The depth maps generated
two frames as input, and outputs a single transformation be-         from projecting these Luminar pointclouds onto the cam-
tween that pair of frames. To evaluate our model on 5-frame          era frame allow us to evaluate depth estimation methods in
snippets we combine the relative transformations between             a much more challenging way, both in terms of denseness
the target frame and the first context frame into 5-frame long       and longer ranges. In Table 2 and Figure 6 of the main text
overlapping trajectories, stacking fx (It , It−1 ) = xt→t−1 to       we show how our proposed PackNet architecture outper-
create appropriately sized trajectories.                             forms other related methods under these conditions. In fact,
   The ATE results are summarized in Table 6, with our               the gap in performance increases when considering denser
proposed framework achieving competitive results relative            ground-truth information at longer ranges, both on the en-
to other related methods. We also note that all these related        tire interval and at discretized bins.
methods are trained in the monocular setting (M), and there-             DDAD is a cross-continental dataset with scenes drawn
fore scaled at test-time using ground truth information. Our         from urban settings in the United States (San Francisco
method, on the other hand, when trained with the proposed            Bay Area, Detroit and Ann Arbor) and Japan (Tokyo and
velocity supervision loss (M+v) does not require ground-             Odaiba). Each scene is 5 or 10 seconds long and consists of
truth scaling at test-time, as it is able to recover metrically      50 or 100 samples with corresponding Luminar-H2 point-
accurate scale purely from monocular imagery. Neverthe-              cloud and six image frames, including intrinsic and extrinsic
less, it is still able to achieve competitive results compared       calibration. The training set contains 194 scenes with a total
to other methods. Examples of reconstructed trajectories             of 17050 individual samples, and the validation set contains
obtained using PackNet-SfM for the test sequences can be
found in Figure 9.                                                      1 https://www.luminartech.com/technology

          Method                                 Supervision      Resolution     GT            Seq. 09             Seq. 10
          SfMLearner (Zhou et al. [53])              M            416 x 128       X       0.021 ± 0.017        0.020 ± 0.015
          Monodepth2 (Godard et al. [19])            M            640 x 192       X       0.017 ± 0.008        0.015 ± 0.010
          DF-Net (Zou et al. [54])                   M            576 x 160       X       0.017 ± 0.007        0.015 ± 0.009
          Vid2Depth (Mahjourian et al. [34])         M            416 x 128       X       0.013 ± 0.010        0.012 ± 0.011
          GeoNet (Yin et al. [48])                   M            416 x 128       X       0.012 ± 0.007        0.012 ± 0.009
          Struct2Depth (Casser et al. [6])           M            416 x 128       X       0.011 ± 0.006        0.011 ± 0.010
          TwoStreamNet (Ambrus et al. [2])           M            640 x 192       X       0.010 ± 0.002        0.009 ± 0.002
          PackNet-SfM                                M            640 x 192       X       0.011 ± 0.006        0.009 ± 0.007
          PackNet-SfM                               M+v           640 x 192       X       0.010 ± 0.005        0.009 ± 0.008
          PackNet-SfM                               M+v           640 x 192               0.014 ± 0.007        0.012 ± 0.008

Table 6: Average Absolute Trajectory Error (ATE) in meters on the KITTI Odometry Benchmark [17]: All methods
are trained on Sequences 00-08 and evaluated on Sequences 09-10. The ATE numbers are averaged over all overlapping
5-frame snippets in the test sequences. M+v refers to velocity supervision (v) in addition to monocular images (M). The GT
checkmark indicates the use of ground-truth translation to scale the estimates at test-time.
Figure 9: Pose evaluation on KITTI test sequences. Qualitative trajectory results of PackNet-SfM on test sequences 09 and
10 of the KITTI odometry benchmark.

60 senes with a total of 4150 samples. The six cameras are       [4] Jens Behrmann, Will Grathwohl, Ricky TQ Chen, David Du-
2.4 MP (1936 × 1216), global-shutter, and oriented at 60°            venaud, and Jörn-Henrik Jacobsen. Invertible residual net-
intervals. They are synchronized with 10 Hz scans from our           works. arXiv preprint arXiv:1811.00995, 2018. 4
Luminar-H2 sensors oriented at 90° intervals.                    [5] Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora,
                                                                     Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Gi-
                                                                     ancarlo Baldan, and Oscar Beijbom. nuscenes: A multi-
References                                                           modal dataset for autonomous driving. CoRR, 2019. 2, 5,
 [1] TensorRT python library.       https://developer.               8
     nvidia.com/tensorrt. Accessed: 2019-11-09. 8                [6] Vincent Casser, Soeren Pirk, Reza Mahjourian, and Anelia
 [2] Rares Ambrus, Vitor Guizilini, Jie Li, Sudeep Pillai, and       Angelova. Depth prediction without the sensors: Leveraging
     Adrien Gaidon. Two stream networks for self-supervised          structure for unsupervised learning from monocular videos.
     ego-motion estimation. In Proceedings of the Conference         In AAAI, 2019. 1, 2, 3, 6, 7, 9
     on Robot Learning (CoRL), 2019. 9                           [7] Yunjin Chen and Thomas Pock. Trainable nonlinear reaction
 [3] Aayush Bansal, Xinlei Chen, Bryan Russell, Abhinav Gupta,       diffusion: A flexible framework for fast and effective image
     and Deva Ramanan. Pixelnet: Representation of the pix-          restoration. IEEE Transactions on Pattern Analysis and Ma-
     els, by the pixels, and for the pixels. arXiv preprint          chine Intelligence, 39:1256–1272, 2017. 4
     arXiv:1702.06506, 2017. 2                                   [8] Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochre-

                                        Figure 10: DDAD sample from Tokyo, Japan.
                              Figure 11: DDAD sample from San Francisco Bay Area, California.

                                        Figure 12: DDAD sample from Detroit, Michigan.

     iter. Fast and accurate deep network learning by exponential    [12] Chao Dong, Chen Change Loy, Kaiming He, and Xiaoou
     linear units (elus). In ICLR, 2016. 4                                Tang. Image super-resolution using deep convolutional net-
 [9] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo                  works. IEEE Trans. Pattern Anal. Mach. Intell., 38(2):295–
     Rehfeld, Markus Enzweiler, Rodrigo Benenson, Uwe                     307, Feb. 2016. 4
     Franke, Stefan Roth, and Bernt Schiele. The cityscapes          [13] Alexey Dosovitskiy, Philipp Fischer, Eddy Ilg, Philip
     dataset for semantic urban scene understanding. In IEEE              Hausser, Caner Hazirbas, Vladimir Golkov, Patrick Van
     conference on computer vision and pattern recognition,               Der Smagt, Daniel Cremers, and Thomas Brox. Flownet:
     pages 3213–3223, 2016. 5, 6                                          Learning optical flow with convolutional networks. In Pro-
[10] Jia Deng, Wei Dong, Richard Socher, Li jia Li, Kai Li, and Li        ceedings of the IEEE international conference on computer
     Fei-fei. Imagenet: A large-scale hierarchical image database.        vision, pages 2758–2766, 2015. 2
     In Proceedings of the IEEE Conference on Computer Vision        [14] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map
     and Pattern Recognition, 2009. 6, 7, 8                               prediction from a single image using a multi-scale deep net-
[11] Laurent Dinh, Jascha Sohl-Dickstein, and Samy Bengio.                work. In Advances in neural information processing systems,
     Density estimation using real nvp. In ICLR, 2017. 4                  pages 2366–2374, 2014. 2, 5, 6, 7, 8
[15] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-                [31] Kuan-Hui Lee, German Ros, Jie Li, and Adrien Gaidon. Spi-
     manghelich, and Dacheng Tao. Deep ordinal regression net-             gan: Privileged adversarial learning from simulation. In
     work for monocular depth estimation. In Proceedings of the            ICLR, 2019. 1
     IEEE Conference on Computer Vision and Pattern Recogni-          [32] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully
     tion, pages 2002–2011, 2018. 6, 7, 8                                  convolutional networks for semantic segmentation. In Pro-
[16] Ravi Garg, Vijay Kumar BG, Gustavo Carneiro, and Ian                  ceedings of the IEEE conference on computer vision and pat-
     Reid. Unsupervised cnn for single view depth estimation:              tern recognition, pages 3431–3440, 2015. 2
     Geometry to the rescue. In European Conference on Com-           [33] C. Luo, Z. Yang, P. Wang, Y. Wang, W. Xu, R. Nevatia, and
     puter Vision, pages 740–756. Springer, 2016. 2, 3                     A. Yuille. Every pixel counts++: Joint learning of geometry
[17] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel            and motion with 3d holistic understanding. arXiv preprint
     Urtasun. Vision meets robotics: The kitti dataset. The Inter-         arXiv:1810.06125, 2018. 7
     national Journal of Robotics Research, 32(11):1231–1237,         [34] Reza Mahjourian, Martin Wicke, and Anelia Angelova. Un-
     2013. 2, 5, 9                                                         supervised learning of depth and ego-motion from monoc-
[18] Clément Godard, Oisin Mac Aodha, and Gabriel J Bros-                 ular video using 3d geometric constraints. In Proceedings
     tow. Unsupervised monocular depth estimation with left-               of the IEEE Conference on Computer Vision and Pattern
     right consistency. In CVPR, volume 2, page 7, 2017. 2,                Recognition, pages 5667–5675, 2018. 1, 2, 3, 6, 7, 9
     3                                                                [35] Fabian Manhardt, Wadim Kehl, and Adrien Gaidon. Roi-
[19] Clément Godard, Oisin Mac Aodha, Michael Firman, and                 10d: Monocular lifting of 2d detection to 6d pose and metric
     Gabriel J. Brostow. Digging into self-supervised monocular            shape. IEEE Conference on Computer Vision and Pattern
     depth prediction. In ICCV, 2019. 3, 6, 7, 8, 9                        Recognition, 2018. 1
[20] Benjamin Graham.                    Fractional max-pooling.      [36] Nikolaus Mayer, Eddy Ilg, Philip Hausser, Philipp Fischer,
     arXiv:1412.607, 2015. 2, 4                                            Daniel Cremers, Alexey Dosovitskiy, and Thomas Brox. A
[21] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.                large dataset to train convolutional networks for disparity,
     Deep residual learning for image recognition. In Proceed-             optical flow, and scene flow estimation. In Proceedings of the
     ings of the IEEE conference on computer vision and pattern            IEEE Conference on Computer Vision and Pattern Recogni-
     recognition, pages 770–778, 2016. 1, 8                                tion, pages 4040–4048, 2016. 2, 5
[22] Jrn-Henrik Jacobsen, Arnold W.M. Smeulders, and Edouard          [37] Jeff Michels, Ashutosh Saxena, and Andrew Y Ng. High
     Oyallon. i-revnet: Deep invertible networks. In International         speed obstacle avoidance using monocular vision and rein-
     Conference on Learning Representations, 2018. 4                       forcement learning. In 22nd international conference on Ma-
[23] Max Jaderberg, Karen Simonyan, Andrew Zisserman, et al.               chine learning, pages 593–600. ACM, 2005. 1
     Spatial transformer networks. In Advances in neural infor-       [38] Adam Paszke, Sam Gross, Soumith Chintala, Gregory
     mation processing systems, pages 2017–2025, 2015. 2                   Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Al-
[24] Alex Kendall, Yarin Gal, and Roberto Cipolla. Multi-task              ban Desmaison, Luca Antiga, and Adam Lerer. Automatic
     learning using uncertainty to weigh losses for scene geome-           differentiation in pytorch. In NIPS-W, 2017. 5
     try and semantics. In Proceedings of the IEEE Conference         [39] Sudeep Pillai, Rares Ambrus, and Adrien Gaidon. Su-
     on Computer Vision and Pattern Recognition, pages 7482–               perdepth: Self-supervised, super-resolved monocular depth
     7491, 2018. 1                                                         estimation. In Robotics and Automation (ICRA), 2019 IEEE
[25] Diederik P Kingma and Jimmy Ba. Adam: A method for                    International Conference on, 2018. 2, 6
     stochastic optimization. arXiv preprint arXiv:1412.6980,         [40] Wenzhe Shi, Jose Caballero, Ferenc Huszár, Johannes Totz,
     2014. 5                                                               Andrew P Aitken, Rob Bishop, Daniel Rueckert, and Zehan
[26] Durk P Kingma and Prafulla Dhariwal. Glow: Generative                 Wang. Real-time single image and video super-resolution
     flow with invertible 1x1 convolutions. In Advances in Neural          using an efficient sub-pixel convolutional neural network. In
     Information Processing Systems, 2018. 4                               Proceedings of the IEEE Conference on Computer Vision
[27] Maria Klodt and Andrea Vedaldi. Supervising the new with              and Pattern Recognition, pages 1874–1883, 2016. 2, 4
     the old: Learning sfm from sfm. In European Conference on        [41] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya
     Computer Vision, pages 713–728. Springer, 2018. 2                     Sutskever, and Ruslan Salakhutdinov. Dropout: A simple
[28] Alexander Kolesnikov, Xiaohua Zhai, and Lucas Beyer. Re-              way to prevent neural networks from overfitting. Journal of
     visiting self-supervised visual representation learning. arXiv        Machine Learning Research, 15:1929–1958, 2014. 4
     preprint arXiv:1901.09005, 2019. 1                               [42] J. Uhrig, N. Schneider, L. Schneider, U. Franke, T. Brox, and
[29] Yevhen Kuznietsov, Jörg Stückler, and Bastian Leibe. Semi-          A. Geiger. Sparsity invariant cnns. 3DV, 2017. 5, 6, 7
     supervised deep learning for monocular depth map predic-         [43] Benjamin Ummenhofer, Huizhong Zhou, Jonas Uhrig, Niko-
     tion. In IEEE Conference on Computer Vision and Pattern               laus Mayer, Eddy Ilg, Alexey Dosovitskiy, and Thomas
     Recognition, pages 6647–6655, 2017. 6, 7                              Brox. Demon: Depth and motion network for learning
[30] Chen-Yu Lee, Patrick Gallagher, and Zhuowen Tu. Gener-                monocular stereo. In IEEE Conference on computer vision
     alizing pooling functions in convolutional neural networks:           and pattern recognition (CVPR), volume 5, page 6, 2017. 2
     Mixed, gated, and tree. In International Conference on Arti-     [44] Chaoyang Wang, José Miguel Buenaposada, Rui Zhu, and
     ficial Intelligence and Statistics (AISTATS), 2016. 2                 Simon Lucey. Learning depth from monocular videos using
     direct methods. In IEEE Conference on Computer Vision and            Vision and Pattern Recognition (CVPR), July 2017. 2
     Pattern Recognition, pages 2022–2030, 2018. 2, 7
                                                                     [50] Hao Zhang and Jianwei Ma.      Hartley spectral pool-
[45] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and Eero P Si-              ing for deep learning. Computing Research Repository,
     moncelli. Image quality assessment: from error visibility to         abs/1810.04028, 2018. 4
     structural similarity. IEEE transactions on image processing,
     13(4):600–612, 2004. 2, 3                                       [51] Junsheng Zhou, Yuwang Wang, Naiyan Wang, and Wen-
[46] Yuxin Wu and Kaiming He. Group normalization. In Com-                jun Zeng. Unsupervised high-resolution depth learning from
     puter Vision - ECCV 2018 - 15th European Conference, Mu-             videos with dual networks. In Inter. Conf. on Computer Vi-
     nich, Germany, September 8-14, 2018, Proceedings, Part               sion. IEEE, IEEE, 2019. 7
     XIII, pages 3–19, 2018. 4                                       [52] Lipu Zhou, Jiamin Ye, Montiel Abello, Shengze Wang, and
[47] Nan Yang, Rui Wang, Jörg Stückler, and Daniel Cremers.             Michael Kaess. Unsupervised learning of monocular depth
     Deep virtual stereo odometry: Leveraging deep depth pre-             estimation with bundle adjustment, super-resolution and clip
     diction for monocular direct sparse odometry. arXiv preprint         loss. arXiv preprint arXiv:1812.03368, 2018. 2
     arXiv:1807.02570, 2018. 2
[48] Zhichao Yin and Jianping Shi. Geonet: Unsupervised learn-       [53] Tinghui Zhou, Matthew Brown, Noah Snavely, and David G
     ing of dense depth, optical flow and camera pose. In Pro-            Lowe. Unsupervised learning of depth and ego-motion from
     ceedings of the IEEE Conference on Computer Vision and               video. In CVPR, volume 2, page 7, 2017. 2, 3, 5, 6, 7, 9
     Pattern Recognition (CVPR), volume 2, 2018. 1, 2, 7, 9          [54] Yuliang Zou, Zelun Luo, and Jia-Bin Huang. Df-net: Un-
[49] Fisher Yu, Vladlen Koltun, and Thomas Funkhouser. Dilated            supervised joint learning of depth and flow using cross-task
     residual networks. In The IEEE Conference on Computer           consistency. In ECCV, 2018. 1, 2, 7, 9
