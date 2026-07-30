---
source_id: 064
bibtex_key: godard2019monodepth2
title: Digging into Self-Supervised Monocular Depth Estimation
year: 2019
domain_theme: Estimasi Kedalaman
verified_pdf: 64_Monodepth2.pdf
char_count: 112379
---

Digging Into Self-Supervised Monocular Depth Estimation

                                                    Clément Godard1       Oisin Mac Aodha2     Michael Firman3  Gabriel Brostow3,1
                                                                            1           2              3
                                                                              UCL         Caltech        Niantic
                                                                      www.github.com/nianticlabs/monodepth2
arXiv:1806.01260v4 [cs.CV] 17 Aug 2019

                                                                 Abstract

                                            Per-pixel ground-truth depth data is challenging to ac-                                   Input               Monodepth2 (M)
                                         quire at scale. To overcome this limitation, self-supervised
                                         learning has emerged as a promising alternative for train-
                                         ing models to perform monocular depth estimation. In this                        Monodepth2 (S)                Monodepth2 (MS)
                                         paper, we propose a set of improvements, which together re-
                                         sult in both quantitatively and qualitatively improved depth
                                         maps compared to competing self-supervised methods.
                                            Research on self-supervised monocular training usually                     Zhou et al. [76] (M)             Monodepth [15] (S)
                                         explores increasingly complex architectures, loss functions,
                                         and image formation models, all of which have recently
                                         helped to close the gap with fully-supervised methods. We                    Zhan et al. [73] (MS)                DDVO [62] (M)
                                         show that a surprisingly simple model, and associated de-
                                         sign choices, lead to superior predictions. In particular, we
                                         propose (i) a minimum reprojection loss, designed to ro-                    Ranjan et al. [51] (M)               EPC++ [38] (MS)
                                         bustly handle occlusions, (ii) a full-resolution multi-scale
                                         sampling method that reduces visual artifacts, and (iii) an     Figure 1. Depth from a single image. Our self-supervised model,
                                                                                                         Monodepth2, produces sharp, high quality depth maps, whether
                                         auto-masking loss to ignore training pixels that violate cam-
                                                                                                         trained with monocular (M), stereo (S), or joint (MS) supervision.
                                         era motion assumptions. We demonstrate the effectiveness
                                         of each component in isolation, and show high quality,          approaches have shown that it is instead possible to train
                                         state-of-the-art results on the KITTI benchmark.                monocular depth estimation models using only synchro-
                                                                                                         nized stereo pairs [12, 15] or monocular video [76].
                                                                                                            Among the two self-supervised approaches, monocular
                                         1. Introduction                                                 video is an attractive alternative to stereo-based supervision,
                                            We seek to automatically infer a dense depth image from      but it introduces its own set of challenges. In addition to
                                         a single color input image. Estimating absolute, or even        estimating depth, the model also needs to estimate the ego-
                                         relative depth, seems ill-posed without a second input image    motion between temporal image pairs during training. This
                                         to enable triangulation. Yet, humans learn from navigating      typically involves training a pose estimation network that
                                         and interacting in the real-world, enabling us to hypothesize   takes a finite sequence of frames as input, and outputs the
                                         plausible depth estimates for novel scenes [18].                corresponding camera transformations. Conversely, using
                                            Generating high quality depth-from-color is attractive       stereo data for training makes the camera-pose estimation a
                                         because it could inexpensively complement LIDAR sensors         one-time offline calibration, but can cause issues related to
                                         used in self-driving cars, and enable new single-photo appli-   occlusion and texture-copy artifacts [15].
                                         cations such as image-editing and AR-compositing. Solv-            We propose three architectural and loss innovations that
                                         ing for depth is also a powerful way to use large unlabeled     combined, lead to large improvements in monocular depth
                                         image datasets for the pretraining of deep networks for         estimation when training with monocular video, stereo
                                         downstream discriminative tasks [23]. However, collecting       pairs, or both: (1) A novel appearance matching loss to ad-
                                         large and varied training datasets with accurate ground truth   dress the problem of occluded pixels that occur when us-
                                         depth for supervised learning [55, 9] is itself a formidable    ing monocular supervision. (2) A novel and simple auto-
                                         challenge. As an alternative, several recent self-supervised    masking approach to ignore pixels where no relative camera
                                                                     step decoupled from learning. Recently, [65] built upon our
                                                                     model by incorporating noisy depth hints from traditional
                            Input                Geonet [71] (M)     stereo algorithms, improving depth predictions.
                                                                     2.2. Self-supervised Depth Estimation
                  Ranjan [51] (M)               EPC++ [38] (MS)          In the absence of ground truth depth, one alternative is to
                                                                     train depth estimation models using image reconstruction as
                                                                     the supervisory signal. Here, the model is given a set of im-
                     Baseline (M)               Monodepth2 (M)
                                                                     ages as input, either in the form of stereo pairs or monocu-
Figure 2. Moving objects. Monocular methods can fail to predict
                                                                     lar sequences. By hallucinating the depth for a given image
depth for objects that were often observed to be in motion dur-      and projecting it into nearby views, the model is trained by
ing training e.g. moving cars – including methods which explicitly   minimizing the image reconstruction error.
model motion [71, 38, 51]. Our method succeeds here where oth-       Self-supervised Stereo Training
ers, and our baseline with our contributions turned off, fail.
                                                                          One form of self-supervision comes from stereo pairs.
                                                                     Here, synchronized stereo pairs are available during train-
motion is observed in monocular training. (3) A multi-scale          ing, and by predicting the pixel disparities between the pair,
appearance matching loss that performs all image sampling            a deep network can be trained to perform monocular depth
at the input resolution, leading to a reduction in depth ar-         estimation at test time. [67] proposed such a model with dis-
tifacts. Together, these contributions yield state-of-the-art        cretized depth for the problem of novel view synthesis. [12]
monocular and stereo self-supervised depth estimation re-            extended this approach by predicting continuous disparity
sults on the KITTI dataset [13], and simplify many compo-            values, and [15] produced results superior to contemporary
nents found in the existing top performing models.                   supervised methods by including a left-right depth consis-
                                                                     tency term. Stereo-based approaches have been extended
2. Related Work                                                      with semi-supervised data [30, 39], generative adversarial
  We review models that, at test time, take a single color           networks [1, 48], additional consistency [50], temporal in-
image as input and predict the depth of each pixel as output.        formation [33, 73, 3], and for real-time use [49].
2.1. Supervised Depth Estimation                                         In this work, we show that with careful choices regarding
                                                                     appearance losses and image resolution, we can reach the
    Estimating depth from a single image is an inherently ill-
                                                                     performance of stereo training using only monocular train-
posed problem as the same input image can project to mul-
                                                                     ing. Further, one of our contributions carries over to stereo
tiple plausible depths. To address this, learning based meth-
                                                                     training, resulting in increased performance there too.
ods have shown themselves capable of fitting predictive
models that exploit the relationship between color images            Self-supervised Monocular Training
and their corresponding depth. Various approaches, such as                A less constrained form of self-supervision is to use
combining local predictions [19, 55], non-parametric scene           monocular videos, where consecutive temporal frames pro-
sampling [24], through to end-to-end supervised learning             vide the training signal. Here, in addition to predicting
[9, 31, 10] have been explored. Learning based algorithms            depth, the network has to also estimate the camera pose be-
are also among some of the best performing for stereo esti-          tween frames, which is challenging in the presence of object
mation [72, 42, 60, 25] and optical flow [20, 63].                   motion. This estimated camera pose is only needed during
    Many of the above methods are fully supervised, requir-          training to help constrain the depth estimation network.
ing ground truth depth during training. However, this is                 In one of the first monocular self-supervised approaches,
challenging to acquire in varied real-world settings. As a           [76] trained a depth estimation network along with a sep-
result, there is a growing body of work that exploits weakly         arate pose network. To deal with non-rigid scene motion,
supervised training data, e.g. in the form of known object           an additional motion explanation mask allowed the model
sizes [66], sparse ordinal depths [77, 6], supervised appear-        to ignore specific regions that violated the rigid scene as-
ance matching terms [72, 73], or unpaired synthetic depth            sumption. However, later iterations of their model available
data [45, 2, 16, 78], all while still requiring the collection       online disabled this term, achieving superior performance.
of additional depth or other annotations. Synthetic train-           Inspired by [4], [61] proposed a more sophisticated motion
ing data is an alternative [41], but it is not trivial to generate   model using multiple motion masks. However, this was not
large amounts of synthetic data containing varied real-world         fully evaluated, making it difficult to understand its utility.
appearance and motion. Recent work has shown that con-               [71] also decomposed motion into rigid and non-rigid com-
ventional structure-from-motion (SfM) pipelines can gen-             ponents, using depth and optical flow to explain object mo-
erate sparse training signal for both camera pose and depth          tion. This improved the flow estimation, but they reported
[35, 28, 68], where SfM is typically run as a pre-processing         no improvement when jointly training for flow and depth
               Depth encoder Depth decoder

                                                                                                                                                                             Depth decoder

                                                                    Looking up pixels using the correct depth

          (a) Depth network                                         (c) Our appearance loss                                        (d) Our full-res multi-scale
                                                                                                                                                                    Depth
 color                                depth   Occluded pixel                                                                                                       decoder
                                                                                                                Good match

                                                                It-1                        It                       It+1
            (b) Pose network                                                                                                                         Upscale
                                              pe(       ,      )=           Baseline: avg(          ,      )=          ❌            ⊗                          ⊗
                                                                    error

                                              pe(       ,      )=                                                                       loss
                                                                    error   Ours:       min(         ,     )=         ✓                                                loss
                                                                                                                                  Baseline         Ours

Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between
                                                                                                              SSIM
a pair of frames is predicted with a separate pose network. (c) Per-pixel minimum reprojection: When correspondences are good, the
reprojection loss should be low. However, occlusions and disocclusions result in pixels from the current time step not appearing in both the                                          Baseline
previous and next frames. The baseline average loss forces the network to match occluded pixels, whereas our minimum reprojection loss
only matches each pixel to the view in which it is visible, leading to sharper results. (d) Full-resolution multi-scale: We upsample depth                                                   SSIM
predictions at intermediate layers and compute all losses at the input resolution, reducing texture-copy artifacts.                                                                     ⊗
              (b) Pose network

estimation. In the context of optical flow estimation, [22]                         work to predict the appearance of a target image from the
showed that it helps to explicitly model occlusion.
    Recent approaches have begun to close the performance
                                                                                                                c
                                                                                    viewpoint of another image. By constraining the network
                                                                                    to perform image synthesis using an intermediary variable,
                                                                                                                                               d
    Baseline                     Ours
gap between monocular and stereo-based self-supervision.                                                        o                              e
                                                                                    in our case depth or disparity, we can then extract this in-
                                                                                    terpretable depth from the model. This is an ill-posed prob-
[70] constrained the predicted depth to be consistent with
                                                                                                                l                              p
predicted surface normals, and [69] enforced edge con-
                                                                                                                  De De
                                                                                    lem as there is an extremely large number of possible in-
sistency. [40] proposed an approximate geometry based                                                           o
                                                                                    correct depths per pixel which can correctly reconstruct   t
matching loss to encourage temporal depth consistency.                                                            pth pth
                                                                                    the novel view given the relative pose between those two
[62] use a depth normalization layer to overcome the pref-                                                      r
                                                                                    views. Classical binocular and multi-view stereo methods   h
erence for smaller depth values that arises from the com-                                                         enc dec
                                                                                    typically address this ambiguity by enforcing smoothness
monly used depth smoothness term from [15]. [5] make use                                                          od od
                                                                                    in the depth maps, and by computing photo-consistency on
of pre-computed instance segmentation masks for known                               patches when solving for per-pixel depth via global opti-
categories to help deal with moving objects.                                        mization e.g. [11].            er  er
                                                                                        Similar to [12, 15, 76], we also formulate our problem
Appearance Based Losses
                                                                                    as the minimization of a photometric reprojection error at
    Self-supervised training typically relies on making as-
                                                                                    training time. We express the relative pose for each source
sumptions about the appearance (i.e. brightness constancy)
                                                                                    view It0 , with respect to the target image It ’s pose, as Tt→t0 .
and material properties (e.g. Lambertian) of object surfaces
                                                                                    We predict a dense depth map Dt that minimizes the photo-
between frames. [15] showed that the inclusion of a local
                                                                                    metric reprojection error Lp , where
structure based appearance loss [64] significantly improved                                                      X
depth estimation performance compared to simple pairwise                                              Lp =           pe(It , It0 →t ),            (1)
pixel differences [67, 12, 76]. [28] extended this approach                                                                  t0
to include an error fitting term, and [43] explored combining
                                                                                                                            D                    E
                                                                                                 and      It0 →t       = It0 proj(Dt , Tt→t0 , K) .                     (2)
it with an adversarial based loss to encourage realistic look-
ing synthesized images. Finally, inspired by [72], [73] use                         Here pe is a photometric reconstruction error, e.g. the L1
ground truth depth to train an appearance matching term.                            distance in pixel space; proj() are the resulting 2D coordi-
                                                                                    nates of the projected depths Dt in It0 and       is the sam-
3. Method                                                                           pling operator. For simplicity of notation we assume the
                                                                                    pre-computed intrinsics K of all the views are identical,
   Here, we describe our depth prediction network that                              though they can be different. Following [21] we use bilin-
takes a single color input It and produces a depth map Dt .                         ear sampling to sample the source images, which is locally
We first review the key ideas behind self-supervised train-                         sub-differentiable, and we follow [75, 15] in using L1 and
ing for monocular depth estimation, and then describe our                           SSIM [64] to make our photometric error function pe, i.e.
depth estimation network and joint training loss.
                                                                                                     α
                                                                                       pe(Ia , Ib ) = (1 − SSIM(Ia , Ib )) + (1 − α)kIa − Ib k1 ,
3.1. Self-Supervised Training                                                                        2
                                                                                    where α = 0.85. As in [15] we use edge-aware smoothness
   Self-supervised depth estimation frames the learning
problem as one of novel view-synthesis, by training a net-                                       Ls       = |∂x d∗t | e−|∂x It | + |∂y d∗t | e−|∂y It | ,               (3)
                                                         Colors here
                                                         show which
ow                                                       source frame
 ixel                                                    each pixel in L
  ith             L                                      is matched to.
 rcled
  in R
 mono
                                                                                  Figure 5. Auto-masking. We show auto-masks computed after
                                                                                  one epoch, where black pixels are removed from the loss (i.e. µ =
                                                                                  0). The mask prevents objects moving at similar speeds to the
                  R                 -1                 +1
                                                                                  camera (top) and whole frames where the camera is static (bottom)
         Figure 4. Benefit of min. reprojection loss in MS training. Pix-         from contaminating the loss. The mask is computed from the input
         els in the the circled region are occluded in IR so no loss is applied   frames and network predictions using Eqn. 5.
         between (IL , IR ). Instead, the pixels are matched to I−1 where
         they are visible. Colors in the top right image indicate which of the    at once. At each pixel, instead of averaging the photometric
         source images on the bottom are selected for matching by Eqn. 4.         error over all source images, we simply use the minimum.
                                                                                  Our final per-pixel photometric loss is therefore
         where d∗t = dt /dt is the mean-normalized inverse depth                                       Lp = min pe(It , It0 →t ).              (4)
                                                                                                             0 t
         from [62] to discourage shrinking of the estimated depth.
             In stereo training, our source image It0 is the second               See Fig. 4 for an example of this loss in practice. Using our
         view in the stereo pair to It , which has known relative pose.           minimum reprojection loss significantly reduces artifacts at
         While relative poses are not known in advance for monocu-                image borders, improves the sharpness of occlusion bound-
         lar sequences, [76] showed that it is possible to train a sec-           aries, and leads to better accuracy (see Table 2).
         ond pose estimation network to predict the relative poses
                                                                                  Auto-Masking Stationary Pixels
         Tt→t0 used in the projection function proj. During train-
                                                                                  Self-supervised monocular training often operates under the
         ing, we solve for camera pose and depth simultaneously,
                                                                                  assumptions of a moving camera and a static scene. When
         to minimize Lp . For monocular training, we use the two
                                                                                  these assumptions break down, for example when the cam-
         frames temporally adjacent to It as our source frames, i.e.
                                                                                  era is stationary or there is object motion in the scene, per-
         It0 ∈ {It−1 , It+1 }. In mixed training (MS), It0 includes the
                                                                                  formance can suffer greatly. This problem can manifest it-
         temporally adjacent frames and the opposite stereo view.
                                                                                  self as ‘holes’ of infinite depth in the predicted test time
         3.2. Improved Self-Supervised Depth Estimation                           depth maps, for objects that are typically observed to be
                                                                                  moving during training [38] (Fig. 2). This motivates our
            Existing monocular methods produce lower quality                      second contribution: a simple auto-masking method that fil-
         depths than the best fully-supervised models. To close this              ters out pixels which do not change appearance from one
         gap, we propose several improvements that significantly in-              frame to the next in the sequence. This has the effect of
         crease predicted depth quality, without adding additional                letting the network ignore objects which move at the same
         model components that also require training (see Fig. 3).                velocity as the camera, and even to ignore whole frames in
                                                                                  monocular videos when the camera stops moving.
         Per-Pixel Minimum Reprojection Loss
                                                                                      Like other works [76, 61, 38], we also apply a per-pixel
         When computing the reprojection error from multiple
                                                                                  mask µ to the loss, selectively weighting pixels. However
         source images, existing self-supervised depth estimation
                                                                                  in contrast to prior work, our mask is binary, so µ ∈ {0, 1},
         methods average together the reprojection error into each
                                                                                  and is computed automatically on the forward pass of the
         of the available source images.This can cause issues with
                                                                                  network, instead of being learned or estimated from object
         pixels that are visible in the target image, but are not vis-
                                                                                  motion. We observe that pixels which remain the same be-
         ible in some of the source images (Fig. 3(c)). If the net-
                                                                                  tween adjacent frames in the sequence often indicate a static
         work predicts the correct depth for such a pixel, the corre-
                                                                                  camera, an object moving at equivalent relative translation
         sponding color in an occluded source image will likely not
                                                                                  to the camera, or a low texture region. We therefore set µ to
         match the target, inducing a high photometric error penalty.
                                                                                  only include the loss of pixels where the reprojection error
         Such problematic pixels come from two main categories:
                                                                                  of the warped image It0 →t is lower than that of the original,
         out-of-view pixels due to egomotion at image boundaries,
                                                                                  unwarped source image It0 , i.e.
         and occluded pixels. The effect of out-of-view pixels can
         be reduced by masking such pixels in the reprojection loss
                                                                                                                                         
                                                                                           µ = min  0
                                                                                                      pe(It , It0 →t ) < min
                                                                                                                          0
                                                                                                                             pe(It , It0 ) , (5)
                                                                                                   t                       t
         [40, 61], but this does not handle disocclusion, where aver-
         age reprojection can result in blurred depth discontinuities.            where [ ] is the Iverson bracket. In cases where the camera
            We propose an improvement that deals with both issues                 and another object are both moving at a similar velocity,
µ prevents the pixels which remain stationary in the image          Our depth decoder is similar to [15], with sigmoids at the
from contaminating the loss. Similarly, when the camera is          output and ELU nonlinearities [7] elsewhere. We convert
static, the mask can filter out all pixels in the image (Fig. 5).   the sigmoid output σ to depth with D = 1/(aσ + b), where
We show experimentally that this simple and inexpensive             a and b are chosen to constrain D between 0.1 and 100 units.
modification to the loss brings significant improvements.           We make use of reflection padding, in place of zero padding,
                                                                    in the decoder, returning the value of the closest border pix-
Multi-scale Estimation                                              els in the source image when samples land outside of the
Due to the gradient locality of the bilinear sampler [21], and      image boundaries. We found that this significantly reduces
to prevent the training objective getting stuck in local min-       the border artifacts found in existing approaches, e.g. [15].
ima, existing models use multi-scale depth prediction and               For pose estimation, we follow [62] and predict the rota-
image reconstruction. Here, the total loss is the combina-          tion using an axis-angle representation, and scale the rota-
tion of the individual losses at each scale in the decoder.         tion and translation outputs by 0.01. For monocular train-
[12, 15] compute the photometric error on images at the             ing, we use a sequence length of three frames, while our
resolution of each decoder layer. We observe that this has          pose network is formed from a ResNet18, modified to ac-
the tendency to create ‘holes’ in large low-texture regions         cept a pair of color images (or six channels) as input and to
in the intermediate lower resolution depth maps, as well as         predict a single 6-DoF relative pose. We perform horizon-
texture-copy artifacts (details in the depth map incorrectly        tal flips and the following training augmentations, with 50%
transferred from the color image). Holes in the depth can           chance: random brightness, contrast, saturation, and hue jit-
occur at low resolution in low-texture regions where the            ter with respective ranges of ±0.2, ±0.2, ±0.2, and ±0.1.
photometric error is ambiguous. This complicates the task           Importantly, the color augmentations are only applied to the
for the depth network, now freed to predict incorrect depths.       images which are fed to the networks, not to those used to
    Inspired by techniques in stereo reconstruction [56], we        compute Lp . All three images fed to the pose and depth
propose an improvement to this multi-scale formulation,             networks are augmented with the same parameters.
where we decouple the resolutions of the disparity images               Our models are implemented in PyTorch [46], trained for
and the color images used to compute the reprojection er-           20 epochs using Adam [26], with a batch size of 12 and an
ror. Instead of computing the photometric error on the              input/output resolution of 640 × 192 unless otherwise spec-
ambiguous low-resolution images, we first upsample the              ified. We use a learning rate of 10−4 for the first 15 epochs
lower resolution depth maps (from the intermediate layers)          which is then dropped to 10−5 for the remainder. This was
to the input image resolution, and then reproject, resam-           chosen using a dedicated validation set of 10% of the data.
ple, and compute the error pe at this higher input resolution       The smoothness term λ is set to 0.001. Training takes 8,
(Fig. 3 (d)). This procedure is similar to matching patches,        12, and 15 hours on a single Titan Xp, for the stereo (S),
as low-resolution disparity values will be responsible for          monocular (M), and monocular plus stereo models (MS).
warping an entire ‘patch’ of pixels in the high resolution
image. This effectively constrains the depth maps at each           4. Experiments
scale to work toward the same objective i.e. reconstructing
                                                                       Here, we validate that (1) our reprojection loss helps with
the high resolution input target image as accurately as pos-
                                                                    occluded pixels compared to existing pixel-averaging, (2)
sible.
                                                                    our auto-masking improves results, especially when train-
Final Training Loss                                                 ing on scenes with static cameras, and (3) our multi-scale
We combine our per-pixel smoothness and masked photo-               appearance matching loss improves accuracy. We evaluate
metric losses as L = µLp + λLs , and average over each              our models, named Monodepth2, on the KITTI 2015 stereo
pixel, scale, and batch.                                            dataset [13], to allow comparison with previously published
                                                                    monocular methods.
3.3. Additional Considerations
                                                                    4.1. KITTI Eigen Split
   Our depth estimation network is based on the general
U-Net architecture [53], i.e. an encoder-decoder network,              We use the data split of Eigen et al. [8]. Except in
with skip connections, enabling us to represent both deep           ablation experiments, for training which uses monocular
abstract features as well as local information. We use a            sequences (i.e. monocular and monocular plus stereo) we
ResNet18 [17] as our encoder, which contains 11M pa-                follow Zhou et al.’s [76] pre-processing to remove static
rameters, compared to the larger, and slower, DispNet               frames. This results in 39,810 monocular triplets for train-
and ResNet50 models used in existing work [15]. Simi-               ing and 4,424 for validation. We use the same intrinsics
lar to [30, 16], we start with weights pretrained on Ima-           for all images, setting the principal point of the camera to
geNet [54], and show that this improves accuracy for our            the image center and the focal length to the average of all
compact model compared to training from scratch (Table 2).          the focal lengths in KITTI. For stereo and mixed training
                                                                                                                      Table 1. Quantitative results. Com-
 Method                              Train   Abs Rel   Sq Rel   RMSE    RMSE log   δ < 1.25   δ < 1.252   δ < 1.253
 Eigen [9]                             D      0.203    1.548    6.307    0.282       0.702      0.890       0.890     parison of our method to existing
 Liu [36]                              D      0.201    1.584    6.471    0.273       0.680      0.898       0.967     methods on KITTI 2015 [13] using
 Klodt [28]                          D*M      0.166    1.490    5.998      -         0.778      0.919       0.966
 AdaDepth [45]                        D*      0.167    1.257    5.578    0.237       0.771      0.922       0.971
                                                                                                                      the Eigen split. Best results in each
 Kuznietsov [30]                      DS      0.113    0.741    4.621    0.189       0.862      0.960       0.986     category are in bold; second best are
 DVSO [68]                            D*S     0.097    0.734    4.442    0.187       0.888      0.958       0.980     underlined.
 SVSM FT [39]                         DS      0.094    0.626    4.252    0.177       0.891      0.965       0.984
 Guo [16]                             DS      0.096    0.641    4.095    0.168       0.892      0.967       0.986     All results here are presented with-
 DORN [10]                             D      0.072    0.307    2.727    0.120       0.932      0.984       0.994     out post-processing [15]; see supple-
 Zhou [76]†                            M      0.183    1.595    6.709    0.270       0.734      0.902       0.959
 Yang [70]                             M      0.182    1.481    6.501    0.267       0.725      0.906       0.963
                                                                                                                      mentary Section F for improved post-
 Mahjourian [40]                       M      0.163    1.240    6.220    0.250       0.762      0.916       0.968     processed results. While our contribu-
 GeoNet [71]†                          M      0.149    1.060    5.567    0.226       0.796      0.935       0.975     tions are designed for monocular train-
 DDVO [62]                             M      0.151    1.257    5.583    0.228       0.810      0.936       0.974
 DF-Net [78]                           M      0.150    1.124    5.507    0.223       0.806      0.933       0.973     ing, we still gain high accuracy in the
 LEGO [69]                             M      0.162    1.352    6.276    0.252         -          -           -       stereo-only category.
 Ranjan [51]                           M      0.148    1.149    5.464    0.226       0.815      0.935       0.973
 EPC++ [38]                            M      0.141    1.029    5.350    0.216       0.816      0.941       0.976     We additionally show we can get
 Struct2depth ‘(M)’ [5]                M      0.141    1.026    5.291    0.215       0.816      0.945       0.979     higher scores at a larger 1024 × 320
 Monodepth2 w/o pretraining            M      0.132    1.044    5.142    0.210       0.845      0.948       0.977
 Monodepth2                            M      0.115    0.903    4.863    0.193       0.877      0.959       0.981
                                                                                                                      resolution, similar to [47] – see sup-
 Monodepth2 (1024 × 320)               M      0.115    0.882    4.701    0.190       0.879      0.961       0.982     plementary Section G. These high res-
 Garg [12]†                            S      0.152    1.226    5.849    0.246       0.784      0.921       0.967     olution numbers are bolded if they beat
 Monodepth R50 [15]†                   S      0.133    1.142    5.533    0.230       0.830      0.936       0.970
 StrAT [43]                            S      0.128    1.019    5.403    0.227       0.827      0.935       0.971     all other models, including our low-res
 3Net (R50) [50]                       S      0.129    0.996    5.281    0.223       0.831      0.939       0.974     versions.
 3Net (VGG) [50]                       S      0.119    1.201    5.888    0.208       0.844      0.941       0.978
 SuperDepth + pp [47] (1024 × 382)     S      0.112    0.875    4.958    0.207       0.852      0.947       0.977
                                                                                                                      Legend
 Monodepth2 w/o pretraining            S      0.130    1.144    5.485    0.232       0.831      0.932       0.968
 Monodepth2                            S      0.109    0.873    4.960    0.209       0.864      0.948       0.975     D – Depth supervision
 Monodepth2 (1024 × 320)               S      0.107    0.849    4.764    0.201       0.874      0.953       0.977     D* – Auxiliary depth supervision
 UnDeepVO [33]                        MS      0.183    1.730     6.57    0.268         -          -           -
 Zhan FullNYU [73]                   D*MS     0.135    1.132    5.585    0.229       0.820      0.933       0.971     S – Self-supervised stereo supervision
 EPC++ [38]                           MS      0.128    0.935    5.011    0.209       0.831      0.945       0.979     M – Self-supervised mono supervision
 Monodepth2 w/o pretraining           MS      0.127    1.031    5.266    0.221       0.836      0.943       0.974
 Monodepth2                           MS      0.106    0.818    4.750    0.196       0.874      0.957       0.979
                                                                                                                      † – Newer results from github.
 Monodepth2 (1024 × 320)              MS      0.106    0.806    4.630    0.193       0.876      0.958       0.980     + pp – With post-processing

(monocular plus stereo), we set the transformation between                            training, we find that the in the stereo-only case we still
the two stereo frames to be a pure horizontal translation of                          perform well. We achieve high accuracy despite using a
fixed length. During evaluation, we cap depth to 80m per                              lower resolution than [47]’s 1024 × 384, with substantially
standard practice [15]. For our monocular models, we re-                              less training time (20 vs. 200 epochs) and no use of post-
port results using the per-image median ground truth scaling                          processing.
introduced by [76]. See also supplementary material Sec-
tion D.2 for results where we apply a single median scaling
                                                                                      4.1.1     KITTI Ablation Study
to the whole test set, instead of scaling each image indepen-
dently. For results that use any stereo supervision we do not                         To better understand how the components of our model con-
perform median scaling as scale can be inferred from the                              tribute to the overall performance in monocular training,
known camera baseline during training.                                                in Table 2(a) we perform an ablation study by changing
    We compare the results of several variants of our model,                          various components of our model. We see that the base-
trained with different types of self-supervision: monocular                           line model, without any of our contributions, performs the
video only (M), stereo only (S), and both (MS). The results                           worst. When combined together, all our components lead
in Table 1 show that our monocular method outperforms                                 to a significant improvement (Monodepth2 (full)). More
all existing state-of-the-art self-supervised approaches. We                          experiments turning parts of our full model off in turn are
also outperform recent methods ([38, 51]) that explicitly                             shown in supplementary material Section C.
compute optical flow as well as motion masks. Qualitative                             Benefits of auto-masking The full Eigen [8] KITTI split
results can be seen in Fig. 7 and supplementary Section E.                            contains several sequences where the camera does not move
However, as with all image reconstruction based approaches                            between frames e.g. where the data capture car was stopped
to depth estimation, our model breaks when the scene con-                             at traffic lights. These ‘no camera motion’ sequences can
tains objects that violate the Lambertian assumptions of our                          cause problems for self-supervised monocular training, and
appearance loss (Fig. 8).                                                             as a result, they are typically excluded at training time using
    As expected, the combination of M and S training data                             expensive to compute optical flow [76]. We report monoc-
increases accuracy, which is especially noticeable on met-                            ular results trained on the full Eigen data split in Table 2(c),
rics that are sensitive to large depth errors e.g. RMSE. De-                          i.e. without removing frames. The baseline model trained
spite our contributions being designed around monocular                               on the full KITTI split performs worse than our full model.
                                          Auto-     Min.      Full-res                  Full Eigen                               RMSE
                                                                           Pretrained                Abs Rel   Sq Rel   RMSE             δ <1.25   δ <1.252   δ < 1.253
                                         masking   reproj.   multi-scale                   split                                  log
 (a)   Baseline                                                               X                       0.140    1.610    5.512    0.223    0.852     0.946       0.973
       Baseline + min reproj.                        X                        X                       0.122    1.081    5.116    0.199    0.866     0.957       0.980
       Baseline + automasking              X                                                          0.124    0.936    5.010    0.206    0.858     0.952       0.977
       Baseline + full-res m.s.                                  X            X                       0.124    1.170    5.249    0.203    0.865     0.953       0.978
       Monodepth2 w/o min reprojection     X                     X            X                       0.117    0.878    4.846    0.196    0.870     0.957       0.980
       Monodepth2 w/o auto-masking                   X           X            X                       0.120    1.097    5.074    0.197    0.872     0.956       0.979
       Monodepth2 w/o full-res m.s.        X         X                        X                       0.117    0.866    4.864    0.196    0.871     0.957       0.981
       Monodepth2 with [76]’s mask                   X           X            X                       0.123    1.177    5.210    0.200    0.869     0.955       0.978
       Monodepth2 smaller (416 × 128)      X         X           X            X                       0.128    1.087    5.171    0.204    0.855     0.953       0.978
       Monodepth2 (full)                   X         X           X            X                       0.115    0.903    4.863    0.193    0.877     0.959       0.981
 (b)   Baseline w/o pt                                                                                0.150    1.585    5.671    0.234    0.827     0.938       0.971
       Monodepth2 w/o pt                   X         X           X                                    0.132    1.044    5.142    0.210    0.845     0.948       0.977
 (c)   Baseline (full Eigen dataset)                                          X             X         0.146    1.876    5.666    0.230    0.848     0.945       0.972
       Monodepth2 (full Eigen dataset)     X         X           X            X             X         0.116    0.918    4.872    0.193    0.874     0.959       0.981

Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen
split. (a) The baseline model, with none of our contributions, performs poorly. The addition of our minimum reprojection, auto-masking
and full-res multi-scale components, significantly improves performance. (b) Even without ImageNet pretrained weights, our much simpler
model brings large improvements above the baseline – see also Table 1. (c) If we train with the full Eigen dataset (instead of the subset
introduced for monocular training by [76]) our improvement over the baseline increases.

       Input    Zhou et al. [76]   DDVO [62]   Monodepth2 (M) Ground truth
                                                                                                                   Type         Abs Rel Sq Rel RMSE log10
                                                                                            Karsch [24]             D            0.428  5.079 8.389 0.149
                                                                                            Liu [37]                D            0.475  6.562 10.05 0.165
                                                                                            Laina [31]              D            0.204  1.840 5.683 0.084
                                                                                            Monodepth [15]          S            0.544  10.94 11.760 0.193
Figure 6. Qualitative Make3D results. All methods were trained                              Zhou [76]               M            0.383  5.321 10.470 0.478
on KITTI using monocular supervision.                                                       DDVO [62]               M            0.387  4.720 8.090 0.204
                                                                                            Monodepth2              M            0.322  3.589 7.417 0.163
Further, in Table 2(a), we replace our auto-masking loss                                    Monodepth2             MS            0.374  3.792 8.238 0.201
with a re-implementation of the predictive mask from [76].
                                                                                         Table 3. Make3D results. All M results benefit from median scal-
We find that this ablated model is worse than using no mask-
                                                                                         ing, while MS uses the unmodified network prediction.
ing at all, while our auto-masking improves results in all
cases. We see an example of how auto-masking works in
practice in Fig. 5.                                                                      dard split. We train models using this new benchmark split,
                                                                                         and evaluate it using the online server [27], and provide re-
Effect of ImageNet pretraining We follow previous work                                   sults in supplementary Section D.3. Additionally, 93% of
[14, 30, 16] in initializing our encoders with weights pre-                              the Eigen split test frames have higher quality ground truth
trained on ImageNet [54]. While some other monocular                                     depths provided by [59]. Like [1], we use these instead
depth prediction works have elected not to use ImageNet                                  of the reprojected LIDAR scans to compare our method
pretraining, we show in Table 1 that even without pretrain-                              against several existing baseline algorithms, still showing
ing, we still achieve state-of-the-art results. We train these                           superior performance.
‘w/o pretraining’ models for 30 epochs to ensure conver-
gence. Table 2 shows the benefit our contributions bring                                 Make3D In Table 3 we report performance on the Make3D
both to pretrained networks and those trained from scratch;                              dataset [55] using our models trained on KITTI. We out-
see supplementary material Section C for more ablations.                                 perform all methods that do not use depth supervision, with
                                                                                         the evaluation criteria from [15]. However, caution should
4.2. Additional Datasets                                                                 be taken with Make3D, as its ground truth depth and input
KITTI Odometry In Section A of the supplementary ma-                                     images are not well aligned, causing potential evaluation is-
terial we show odometry evaluation on KITTI. While our                                   sues. We evaluate on a center crop of 2 × 1 ratio, and apply
focus is better depth estimation, our pose network performs                              median scaling for our M model. Qualitative results can be
on par with competing methods. Competing methods typ-                                    seen in Fig. 6 and in supplementary Section E.
ically feed more frames to their pose network which may
improve their ability to generalize.                                                     5. Conclusion
KITTI Depth Prediction Benchmark We also perform ex-                                        We have presented a versatile model for self-supervised
periments on the recently introduced KITTI Depth Predic-                                 monocular depth estimation, achieving state-of-the-art
tion Evaluation dataset [59], which features more accurate                               depth predictions. We introduced three contributions: (i) a
ground truth depth, addressing quality issues with the stan-                             minimum reprojection loss, computed for each pixel, to deal
  Input
  Zhou et al. [76] Monodepth [15]
   DDVO [62]
   GeoNet [71]
  3Net - R50 [38] Ranjan et al. [51] Zhan et al. [73]
   EPC++ (MS)[38]
       MD2 M
  MD2 M (no p/t)
      MD2 S
      MD2 MS

Figure 7. Qualitative results on the KITTI Eigen split. Our models (MD2) in the last four rows produce the sharpest depth maps, which
are reflected in the superior quantitative results in Table 1. Additional results can be seen in the supplementary materiale Section E.

                                                        Monodepth2 (M)   with occlusions between frames in monocular video, (ii)
                                                                         an auto-masking loss to ignore confusing, stationary pixels,
                                                                         and (iii) a full-resolution multi-scale sampling method. We
                                                        Monodepth2 (M)   showed how together they give a simple and efficient model
                                                                         for depth estimation, which can be trained with monocular
                                                                         video data, stereo data, or mixed monocular and stereo data.
Figure 8. Failure cases. Top: Our self-supervised loss fails to
learn good depths for distorted, reflective and color-saturated re-      Acknowledgements Thanks to the authors who shared their
gions. Bottom: We can fail to accurately delineate objects where         results, and Peter Hedman, Daniyar Turmukhambetov, and
boundaries are ambiguous (left) or shapes are intricate (right).         Aron Monszpart for their helpful discussions.
References                                                           [20] Eddy Ilg, Nikolaus Mayer, Tonmoy Saikia, Margret Keuper,
                                                                          Alexey Dosovitskiy, and Thomas Brox. FlowNet2: Evolu-
 [1] Filippo Aleotti, Fabio Tosi, Matteo Poggi, and Stefano Mat-          tion of optical flow estimation with deep networks. In CVPR,
     toccia. Generative adversarial networks for unsupervised             2017.
     monocular depth prediction. In ECCV Workshops, 2018.
                                                                     [21] Max Jaderberg, Karen Simonyan, Andrew Zisserman, and
 [2] Amir Atapour-Abarghouei and Toby Breckon. Real-time                  Koray Kavukcuoglu. Spatial transformer networks. In
     monocular depth estimation using synthetic data with do-             NeurIPS, 2015.
     main adaptation via image style transfer. In CVPR, 2018.
                                                                     [22] Joel Janai, Fatma Güney, Anurag Ranjan, Michael Black,
 [3] V Madhu Babu, Kaushik Das, Anima Majumdar, and Swagat
                                                                          and Andreas Geiger. Unsupervised learning of multi-frame
     Kumar. Undemon: Unsupervised deep network for depth and
                                                                          optical flow with occlusions. In ECCV, 2018.
     ego-motion estimation. In IROS, 2018.
                                                                     [23] Huaizu Jiang, Erik Learned-Miller, Gustav Larsson, Michael
 [4] Arunkumar Byravan and Dieter Fox. Se3-nets: Learning
                                                                          Maire, and Greg Shakhnarovich. Self-supervised relative
     rigid body motion using deep neural networks. In ICRA,
                                                                          depth learning for urban scene understanding. In ECCV,
     2017.
                                                                          2018.
 [5] Vincent Casser, Soeren Pirk, Reza Mahjourian, and Anelia
                                                                     [24] Kevin Karsch, Ce Liu, and Sing Bing Kang. Depth transfer:
     Angelova. Depth prediction without the sensors: Leveraging
                                                                          Depth extraction from video using non-parametric sampling.
     structure for unsupervised learning from monocular videos.
                                                                          PAMI, 2014.
     In AAAI, 2019.
                                                                     [25] Alex Kendall, Hayk Martirosyan, Saumitro Dasgupta, Peter
 [6] Weifeng Chen, Zhao Fu, Dawei Yang, and Jia Deng. Single-
                                                                          Henry, Ryan Kennedy, Abraham Bachrach, and Adam Bry.
     image depth perception in the wild. In NeurIPS, 2016.
                                                                          End-to-end learning of geometry and context for deep stereo
 [7] Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochre-
                                                                          regression. In ICCV, 2017.
     iter. Fast and accurate deep network learning by exponential
                                                                     [26] Diederik P Kingma and Jimmy Ba. Adam: A method for
     linear units (elus). arXiv, 2015.
                                                                          stochastic optimization. arXiv, 2014.
 [8] David Eigen and Rob Fergus. Predicting depth, surface nor-
     mals and semantic labels with a common multi-scale convo-       [27] KITTI        Single       Depth       Evaluation       Server.
     lutional architecture. In ICCV, 2015.                                http://www.cvlibs.net/datasets/kitti/eval depth.php?
                                                                          benchmark=depth prediction. 2017.
 [9] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map
     prediction from a single image using a multi-scale deep net-    [28] Maria Klodt and Andrea Vedaldi. Supervising the new with
     work. In NeurIPS, 2014.                                              the old: learning SFM from SFM. In ECCV, 2018.
[10] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-               [29] Shu Kong and Charless Fowlkes. Pixel-wise attentional gat-
     manghelich, and Dacheng Tao. Deep ordinal regression net-            ing for parsimonious pixel labeling. arXiv, 2018.
     work for monocular depth estimation. In CVPR, 2018.             [30] Yevhen Kuznietsov, Jörg Stückler, and Bastian Leibe. Semi-
[11] Yasutaka Furukawa and Carlos Hernández. Multi-view                  supervised deep learning for monocular depth map predic-
     stereo: A tutorial. Foundations and Trends in Computer               tion. In CVPR, 2017.
     Graphics and Vision, 2015.                                      [31] Iro Laina, Christian Rupprecht, Vasileios Belagiannis, Fed-
[12] Ravi Garg, Vijay Kumar BG, and Ian Reid. Unsupervised                erico Tombari, and Nassir Navab. Deeper depth prediction
     CNN for single view depth estimation: Geometry to the res-           with fully convolutional residual networks. In 3DV, 2016.
     cue. In ECCV, 2016.                                             [32] Bo Li, Yuchao Dai, and Mingyi He. Monocular depth es-
[13] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we              timation with hierarchical fusion of dilated cnns and soft-
     ready for Autonomous Driving? The KITTI Vision Bench-                weighted-sum inference. Pattern Recognition, 2018.
     mark Suite. In CVPR, 2012.                                      [33] Ruihao Li, Sen Wang, Zhiqiang Long, and Dongbing Gu.
[14] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra            UnDeepVO: Monocular visual odometry through unsuper-
     Malik. Rich feature hierarchies for accurate object detection        vised deep learning. arXiv, 2017.
     and semantic segmentation. In CVPR, 2014.                       [34] Ruibo Li, Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, and
[15] Clément Godard, Oisin Mac Aodha, and Gabriel J Bros-                Lingxiao Hang. Deep attention-based classification network
     tow. Unsupervised monocular depth estimation with left-              for robust depth prediction. ACCV, 2018.
     right consistency. In CVPR, 2017.                               [35] Zhengqi Li and Noah Snavely. Megadepth: Learning single-
[16] Xiaoyang Guo, Hongsheng Li, Shuai Yi, Jimmy Ren, and                 view depth prediction from internet photos. In CVPR, 2018.
     Xiaogang Wang. Learning monocular depth by distilling           [36] Fayao Liu, Chunhua Shen, Guosheng Lin, and Ian Reid.
     cross-domain stereo networks. In ECCV, 2018.                         Learning depth from single monocular images using deep
[17] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.               convolutional neural fields. PAMI, 2015.
     Deep residual learning for image recognition. In CVPR,          [37] Miaomiao Liu, Mathieu Salzmann, and Xuming He.
     2016.                                                                Discrete-continuous depth estimation from a single image.
[18] Carol Barnes Hochberg and Julian E Hochberg. Familiar                In CVPR, 2014.
     size and the perception of depth. The Journal of Psychology,    [38] Chenxu Luo, Zhenheng Yang, Peng Wang, Yang Wang, Wei
     1952.                                                                Xu, Ram Nevatia, and Alan Yuille. Every pixel counts++:
[19] Derek Hoiem, Alexei A Efros, and Martial Hebert. Auto-               Joint learning of geometry and motion with 3D holistic un-
     matic photo pop-up. TOG, 2005.                                       derstanding. arXiv, 2018.
[39] Yue Luo, Jimmy Ren, Mude Lin, Jiahao Pang, Wenxiu Sun,         [56] Daniel Scharstein and Richard Szeliski. A taxonomy and
     Hongsheng Li, and Liang Lin. Single view stereo matching.           evaluation of dense two-frame stereo correspondence algo-
     In CVPR, 2018.                                                      rithms. IJCV, 2002.
[40] Reza Mahjourian, Martin Wicke, and Anelia Angelova. Un-        [57] Karen Simonyan and Andrew Zisserman. Very deep convo-
     supervised learning of depth and ego-motion from monocu-            lutional networks for large-scale image recognition. In ICLR,
     lar video using 3D geometric constraints. In CVPR, 2018.            2015.
[41] Nikolaus Mayer, Eddy Ilg, Philipp Fischer, Caner Hazir-        [58] Deqing Sun, Xiaodong Yang, Ming-Yu Liu, and Jan Kautz.
     bas, Daniel Cremers, Alexey Dosovitskiy, and Thomas Brox.           PWC-Net: CNNs for optical flow using pyramid, warping,
     What makes good synthetic training data for learning dispar-        and cost volume. In CVPR, 2018.
     ity and optical flow estimation? IJCV, 2018.                   [59] Jonas Uhrig, Nick Schneider, Lukas Schneider, Uwe Franke,
[42] Nikolaus Mayer, Eddy Ilg, Philip Häusser, Philipp Fischer,         Thomas Brox, and Andreas Geiger. Sparsity invariant CNNs.
     Daniel Cremers, Alexey Dosovitskiy, and Thomas Brox. A              In 3DV, 2017.
     large dataset to train convolutional networks for disparity,   [60] Benjamin Ummenhofer, Huizhong Zhou, Jonas Uhrig, Niko-
     optical flow, and scene flow estimation. In CVPR, 2016.             laus Mayer, Eddy Ilg, Alexey Dosovitskiy, and Thomas
[43] Ishit Mehta, Parikshit Sakurikar, and PJ Narayanan. Struc-          Brox. DeMoN: Depth and motion network for learning
     tured adversarial training for unsupervised monocular depth         monocular stereo. In CVPR, 2017.
     estimation. In 3DV, 2018.                                      [61] Sudheendra Vijayanarasimhan, Susanna Ricco, Cordelia
[44] Raul Mur-Artal, Jose Maria Martinez Montiel, and Juan D             Schmid, Rahul Sukthankar, and Katerina Fragkiadaki. SfM-
     Tardos. ORB-SLAM: a versatile and accurate monocular                Net: Learning of structure and motion from video. arXiv,
     SLAM system. Transactions on Robotics, 2015.                        2017.
[45] Jogendra Nath Kundu, Phani Krishna Uppala, Anuj Pahuja,        [62] Chaoyang Wang, Jose Miguel Buenaposada, Rui Zhu, and
     and R. Venkatesh Babu. AdaDepth: Unsupervised content               Simon Lucey. Learning depth from monocular videos using
     congruent adaptation for depth estimation. In CVPR, 2018.           direct methods. In CVPR, 2018.
                                                                    [63] Yang Wang, Yi Yang, Zhenheng Yang, Liang Zhao, and Wei
[46] Adam Paszke, Sam Gross, Soumith Chintala, Gregory
                                                                         Xu. Occlusion aware unsupervised learning of optical flow.
     Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Al-
                                                                         In CVPR, 2018.
     ban Desmaison, Luca Antiga, and Adam Lerer. Automatic
     differentiation in PyTorch. In NeurIPS-W, 2017.                [64] Zhou Wang, Alan Conrad Bovik, Hamid Rahim Sheikh, and
                                                                         Eero P Simoncelli. Image quality assessment: from error
[47] Sudeep Pillai, Rares Ambrus, and Adrien Gaidon. Su-
                                                                         visibility to structural similarity. TIP, 2004.
     perdepth: Self-supervised, super-resolved monocular depth
                                                                    [65] Jamie Watson, Michael Firman, Gabriel J Brostow, and
     estimation. In ICRA, 2019.
                                                                         Daniyar Turmukhambetov. Self-supervised monocular depth
[48] Andrea Pilzer, Dan Xu, Mihai Marian Puscas, Elisa Ricci,            hints. In ICCV, 2019.
     and Nicu Sebe. Unsupervised adversarial depth estimation
                                                                    [66] Yiran Wu, Sihao Ying, and Lianmin Zheng. Size-to-depth:
     using cycled generative networks. In 3DV, 2018.
                                                                         A new perspective for single image depth estimation. arXiv,
[49] Matteo Poggi, Filippo Aleotti, Fabio Tosi, and Stefano Mat-         2018.
     toccia. Towards real-time unsupervised monocular depth es-     [67] Junyuan Xie, Ross Girshick, and Ali Farhadi. Deep3D: Fully
     timation on cpu. In IROS, 2018.                                     automatic 2D-to-3D video conversion with deep convolu-
[50] Matteo Poggi, Fabio Tosi, and Stefano Mattoccia. Learning           tional neural networks. In ECCV, 2016.
     monocular depth estimation with unsupervised trinocular as-    [68] Nan Yang, Rui Wang, Jörg Stückler, and Daniel Cremers.
     sumptions. In 3DV, 2018.                                            Deep virtual stereo odometry: Leveraging deep depth predic-
[51] Anurag Ranjan, Varun Jampani, Kihwan Kim, Deqing Sun,               tion for monocular direct sparse odometry. In ECCV, 2018.
     Jonas Wulff, and Michael J Black. Competitive collabora-       [69] Zhenheng Yang, Peng Wang, Yang Wang, Wei Xu, and Ram
     tion: Joint unsupervised learning of depth, camera motion,          Nevatia. LEGO: Learning edge with geometry all at once by
     optical flow and motion segmentation. In CVPR, 2019.                watching videos. In CVPR, 2018.
[52] Zhe Ren, Junchi Yan, Bingbing Ni, Bin Liu, Xiaokang Yang,      [70] Zhenheng Yang, Peng Wang, Wei Xu, Liang Zhao, and Ra-
     and Hongyuan Zha. Unsupervised deep learning for optical            makant Nevatia. Unsupervised learning of geometry with
     flow estimation. In AAAI, 2017.                                     edge-aware depth-normal consistency. In AAAI, 2018.
[53] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-         [71] Zhichao Yin and Jianping Shi. GeoNet: Unsupervised learn-
     Net: Convolutional networks for biomedical image segmen-            ing of dense depth, optical flow and camera pose. In CVPR,
     tation. In MICCAI, 2015.                                            2018.
[54] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, San-      [72] Jure Žbontar and Yann LeCun. Stereo matching by training
     jeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy,             a convolutional neural network to compare image patches.
     Aditya Khosla, Michael Bernstein, et al. Imagenet large             JMLR, 2016.
     scale visual recognition challenge. IJCV, 2015.                [73] Huangying Zhan, Ravi Garg, Chamara Saroj Weerasekera,
[55] Ashutosh Saxena, Min Sun, and Andrew Ng. Make3d:                    Kejie Li, Harsh Agarwal, and Ian Reid. Unsupervised learn-
     Learning 3d scene structure from a single still image. PAMI,        ing of monocular depth estimation and visual odometry with
     2009.                                                               deep feature reconstruction. In CVPR, 2018.
[74] Zhenyu Zhang, Chunyan Xu, Jian Yang, Ying Tai, and Liang
     Chen. Deep hierarchical guidance and regularization learn-
     ing for end-to-end depth estimation. Pattern Recognition,
     2018.
[75] Hang Zhao, Orazio Gallo, Iuri Frosio, and Jan Kautz. Loss
     functions for image restoration with neural networks. Trans-
     actions on Computational Imaging, 2017.
[76] Tinghui Zhou, Matthew Brown, Noah Snavely, and David
     Lowe. Unsupervised learning of depth and ego-motion from
     video. In CVPR, 2017.
[77] Daniel Zoran, Phillip Isola, Dilip Krishnan, and William T
     Freeman. Learning ordinal relationships for mid-level vi-
     sion. In ICCV, 2015.
[78] Yuliang Zou, Zelun Luo, and Jia-Bin Huang. DF-Net: Un-
     supervised joint learning of depth and flow using cross-task
     consistency. In ECCV, 2018.
Supplementary Material                                             ORB-Slam [44]
                                                                                                       Sequence 09
                                                                                                       0.014±0.008
                                                                                                                     Sequence 10 # frames
                                                                                                                     0.012±0.011     -
                                                                   DDVO [62]                           0.045±0.108   0.033±0.074     3
                                                                   Zhou* [76]                          0.050±0.039   0.034±0.028 5 → 2
Note on arXiv versions In an earlier pre-print of this pa-         Zhou [76]                           0.021±0.017   0.020±0.015     5
per, 1806.01260v1, we included a shared encoder for pose           Zhou [76]†                          0.016±0.009   0.013±0.009     5
and depth. While this reduced the number of training pa-           Mahjourian [40]                     0.013±0.010   0.012±0.011     3
                                                                   GeoNet [71]                         0.012±0.007   0.012±0.009     5
rameters, we have since found that we can gain even higher
                                                                   EPC++ M [38]                        0.013±0.007   0.012±0.008     3
results with a separate ResNet pose encoder which accepts          Ranjan [51]                         0.012±0.007   0.012±0.008     5
a stack of two frames as input (see ablation study in Sec-         EPC++ MS [38]                       0.012±0.006   0.012±0.008     3
tion H). Since v1, we have also introduced auto-masking            Monodepth2 M*                       0.017±0.008   0.015±0.010     2
                                                                   Monodepth2 MS*                      0.017±0.008   0.015±0.010     2
to help the model ignore pixels that violate our motion as-
                                                                   Monodepth2 M w/o pretraining*       0.018±0.010   0.015±0.010     2
sumptions.                                                         Monodepth2 MS w/o pretraining*      0.018±0.009   0.015±0.010     2

A. Odometry Evaluation                                            Table 4.    Odometry results on the KITTI [13] odometry
                                                                  dataset. Results show the average absolute trajectory error, and
    In Table 4 we evaluate our pose estimation network fol-       standard deviation, in meters.
lowing the protocol in [76]. We trained our models on se-         † – newer results from the respective online implementations.
quences 0-8 from the KITTI odometry split and tested on           * – evaluation on trajectories made from pairwise predictions – see text for
sequences 9 and 10. As in [76], the absolute trajectory error     details.
is then averaged over all overlapping five-frame snippets in      ‘# frames’ is the number of input frames used for pose prediction. To eval-
the test sequences. Here, unlike [76] and others who use          uate our method we chain integrate the poses from four pairs to make five
custom models for the odometry task, we use the same ar-          frames for evaluation.
chitecture for this task as our other results, and simply train
it again from scratch on these new sequences.                        Depth Decoder
    Baselines such as [76] use a pose network which pre-             layer   k s chns            res    input                 activation
dicts transformations between sets of five frames simulta-           upconv5 3 1 256             32     econv5                ELU [7]
neously. Our pose network only takes two frames as in-               iconv5  3 1 256             16     ↑upconv5, econv4      ELU
                                                                     upconv4 3 1 128             16     iconv5                ELU
put, and ouputs a single transformation between that pair of
                                                                     iconv4  3 1 128             8      ↑upconv4, econv3      ELU
frames. In order to evaluate our two-frame model on the              disp4   3 1 1               1      iconv4                Sigmoid
five-frame test sequences, we make separate predictions for          upconv3 3 1 64              8      iconv4                ELU
each of the four frame-to-frame transformation for each set          iconv3  3 1 64              4      ↑upconv3, econv2      ELU
of five frames and combine them to form local trajectories.          disp3   3 1 1               1      iconv3                Sigmoid
For completeness we repeat the same process with [76] pre-           upconv2 3 1 32              4      iconv3                ELU
dicted poses, which we denote as ‘Zhou∗ ’. As we can see in          iconv2  3 1 32              2      ↑upconv2, econv1      ELU
Table 4, our frame-to-frame poses come close to the accu-            disp2   3 1 1               1      iconv2                Sigmoid
racy of methods trained on blocks of five frames at a time.          upconv1 3 1 16              2      iconv2                ELU
                                                                     iconv1  3 1 16              1      ↑upconv1              ELU
                                                                     disp1   3 1 1               1      iconv1                Sigmoid
B. Network Details
                                                                     Pose Decoder
   Except where stated, for all experiments we use a stan-           layer   k s       chns    res     input    activation
dard ResNet18 [17] encoder for both depth and pose net-              pconv0 1 1        256     32      econv5   ReLU
works. Our pose encoder is modified to accept a pair of              pconv1 3 1        256     32      pconv0   ReLU
frames, or six channels, as input. Our pose encoder there-           pconv2 3 1        256     32      pconv1   ReLU
fore has convolutional weights in the first layer of shape           pconv3 1 1        6       32      pconv3   -
6×64×3×3, instead of the ResNet default of 3×64×3×3.
                                                                  Table 5. Our network architecture Here k is the kernel size, s
When using pretrained weights for our pose encoder, we            the stride, chns the number of output channels for each layer, res
duplicate the first pretrained filter tensor along the channel    is the downscaling factor for each layer relative to the input image,
dimension to make a filter of shape 6 × 64 × 3 × 3. This          and input corresponds to the input of each layer where ↑ is a 2×
allows for a six-channel input image. All weights in this         nearest-neighbor upsampling of the layer.
new expanded filter are divided by 2 to make the output of
the convolution in the same numerical range as the origi-
nal, one-image ResNet. In Table 5 we describe the param-
eters of each layer used in our depth decoder and pose net-
work. Our pose network is larger and deeper than previous
works [76, 62], and we only feed two frames at a time to the
                                             Auto-     Min.      Full-res                                                       RMSE
                                                                              Encoder   Pretrained   Abs Rel   Sq Rel   RMSE            δ < 1.25   δ < 1.252   δ < 1.253
                                            masking   reproj.   multi-scale                                                      log
 (a)   Baseline                                                                R18         X          0.140    1.610    5.512   0.223    0.852       0.946       0.973
       Monodepth2 w/o min reprojection        X                     X          R18         X          0.117    0.878    4.846   0.196    0.870       0.957       0.980
       Monodepth2 w/o auto-masking                      X           X          R18         X          0.120    1.097    5.074   0.197    0.872       0.956       0.979
       Monodepth2 w/o full-res m.s.           X         X                      R18         X          0.117    0.866    4.864   0.196    0.871       0.957       0.981
       Monodepth2 w/o SSIM                    X         X           X          R18         X          0.118    0.853    4.824   0.198    0.868       0.956       0.980
       Monodepth2 with [76]’s mask                      X           X          R18         X          0.123    1.177    5.210   0.200    0.869       0.955       0.978
       Monodepth2 (full)                      X         X           X          R18         X          0.115    0.903    4.863   0.193    0.877       0.959       0.981
 (b)   Baseline w/o pt                                                         R18                    0.150    1.585    5.671   0.234    0.827       0.938       0.971
       Monodepth2 w/o pt or auto-masking                X           X          R18                    0.138    1.197    5.369   0.215    0.842       0.945       0.975
       Monodepth2 w/o pt or min reproj        X                     X          R18                    0.133    1.021    5.219   0.214    0.841       0.945       0.976
       Monodepth2 w/o pt or full-res m.s.     X         X                      R18                    0.131    1.030    5.206   0.210    0.846       0.948       0.978
       Monodepth2 w/o pt                      X         X           X          R18                    0.132    1.044    5.142   0.210    0.845       0.948       0.977
 (c)   Monodepth2 ResNet18 w/o pt             X         X           X          R18                    0.132    1.044    5.142   0.210    0.845       0.948       0.977
       Monodepth2 ResNet18                    X         X           X          R18         X          0.115    0.903    4.863   0.193    0.877       0.959       0.981
       Monodepth2 ResNet 50 w/o pt            X         X           X          R50                    0.131    1.023    5.064   0.206    0.849       0.951       0.979
       Monodepth2 ResNet 50                   X         X           X          R50         X          0.110    0.831    4.642   0.187    0.883       0.962       0.982

Table 6. Ablation. Results for different variants of our model (Monodepth2) with monocular training (except where specified) on KITTI
2015 [13].

Figure 9. Qualitative ablation study. We can see that our model with all components added result in the smallest amount of depth artifacts.
‘Baseline (M)’ is our model without our full-resolution multi-scale appearance loss, minimum reprojection loss, or auto-masking loss.

pose network in contrast to previous works which use three                                results with ResNet 50 are even higher than our ResNet18
[76, 62] or more for their depth estimation experiments. In                               models. ResNet 50 is a standard encoder used by previ-
Section H we validate the benefit of bringing additional pa-                              ous works e.g. [15, 50]. However, training with a 50-layer
rameters to the pose network.                                                             ResNet comes at the expense of longer training and test
                                                                                          times. In Fig. 9 we show additional qualitative results for
                                                                                          the monocular trained variants of our model from Table 6.
C. Additional Ablation Experiments
                                                                                          We observe ‘depth holes’ in both non-pretrained and pre-
    In Table 6 we show a full ablation study on our algo-                                 trained versions of the baseline model compared to ours.
rithm, turning on and off different components of the sys-
tem. We confirm the finding of the main paper, that all our
components together gives the highest quality model, and
that pretraining helps. We observe in Table 6 (d) that our
                                                                                                Table 7. KITTI improved ground
 Method                     Train   Abs Rel Sq Rel RMSE RMSE log δ < 1.25 δ < 1.252 δ < 1.253   truth. Comparison to existing meth-
 Zhou [76]†                  M       0.176  1.532 6.129  0.244     0.758    0.921     0.971     ods on KITTI 2015 [13] using 93%
 Mahjourian [40]             M       0.134  0.983 5.501  0.203     0.827    0.944     0.981
 GeoNet [71]                 M       0.132  0.994 5.240  0.193     0.833    0.953     0.985
                                                                                                of the Eigen split and the improved
 DDVO [62]                   M       0.126  0.866 4.932  0.185     0.851    0.958     0.986     ground truth from [59]. Baseline meth-
 Ranjan [51]                 M       0.123  0.881 4.834  0.181     0.860    0.959     0.985     ods were evaluated using their pro-
 EPC++ [38]                  M       0.120  0.789 4.755  0.177     0.856    0.961     0.987     vided disparity files, which were either
 Monodepth2 w/o pretraining  M       0.112  0.715 4.502  0.167     0.876    0.967     0.990
 Monodepth2                  M       0.090  0.545 3.942  0.137     0.914    0.983     0.995
                                                                                                available publicly or from private com-
 Monodepth [15]               S      0.109  0.811 4.568  0.166     0.877    0.967     0.988     munication with the authors.
 3net [50] (VGG)              S      0.119  0.920 4.824  0.182     0.856    0.957     0.985
 3net [50] (ResNet 50)        S      0.102  0.675 4.293  0.159     0.881    0.969     0.991     Legend
 SuperDepth [47] + pp         S      0.090  0.542 3.967  0.144     0.901    0.976     0.993     D* – Auxiliary depth supervision
 Monodepth2 w/o pretraining   S      0.110  0.849 4.580  0.173     0.875    0.962     0.986
                                                                                                S – Self-supervised stereo supervision
 Monodepth2                   S      0.085  0.537 3.868  0.139     0.912    0.979     0.993
 Zhan FullNYU [73]          D*MS     0.130  1.520 5.184  0.205     0.859    0.955     0.981     M – Self-supervised mono supervision
 EPC++ [38]                  MS      0.123  0.754 4.453  0.172     0.863    0.964     0.989     † – Newer results from the respective on-
 Monodepth2 w/o pretraining MS       0.107  0.720 4.345  0.161     0.890    0.971     0.989     line implementations.
 Monodepth2                  MS      0.080  0.466 3.681  0.127     0.926    0.985     0.995
                                                                                                + pp – With post-processing

D. Additional Evaluation                                               age. This is in contrast to stereo based training where the
                                                                       scale is known and as a result no additional scaling is re-
D.1. Improved Ground Truth                                             quired during the evaluation e.g. [12, 15]. This per-image
    As mentioned in the main paper, the evaluation method              depth scaling hides unstable scale estimation in both depth
introduced by Eigen [8] for KITTI uses the reprojected LI-             and pose estimation and presents a best-case scenario for the
DAR points but does not handle occlusions, moving objects,             monocular training case. If a method outputs wildly varying
or the fact that the car is moving. [59] introduced a set of           scales for each sequence, then this evaluation protocol will
high quality depth maps for the KITTI dataset, making use              hide the issue. This gives an unfair advantage over stereo
of 5 consecutive frames and handling moving objects using              trained methods that do not perform per-image scaling.
the stereo pair. This improved ground truth depth is pro-                  We thus modified the original protocol to instead use a
vided for 652 (or 93%) of the 697 test frames contained in             single scale for all predicted depth maps of each method.
the Eigen test split [8]. We evaluate our results on these 652         For each method, we compute this single scale by taking
improved ground truth frames and compare to existing pub-              the median of all the individual ratios of the depth medians
lished methods without having to retrain each method, see              on the test set. While this is still not ideal as it makes use
Table 7. We present results for all other methods for which            of the ground truth depth, we believe it to be fairer and rep-
we have obtained predictions from the authors. We use the              resentative of the performance of each method. We also
same error metrics from the standard evaluation, and clip              calculated the standard deviation σscale of the individual
the predicted depths to 80 meters to match the Eigen evalu-            scales, where lower values indicate more consistent output
ation. We evaluate on the full image and do not crop, unlike           depth map scales. As can be seen in Table 8, our method
with the Eigen evaluation. We can see that our method still            outperforms previously published self-supervised monocu-
significantly outperforms all previously published methods             lar methods, especially in the near range depth values i.e.
on all metrics. While Superdepth [47] comes a close sec-               δ < 1.25, and is more stable overall.
ond to our algorithm in the S category, they are run at high
resolution (1024 × 384 vs. our 640 × 192), and in Table 1              D.3. KITTI Evaluation Server Benchmark
we show that at higher resolutions our model’s performance                Here, we report the performance of our self-supervised
also increases.                                                        monocular plus stereo model on the online KITTI single
                                                                       image depth prediction benchmark evaluation server [27].
D.2. Single-Scale Evaluation
                                                                       [27] uses a different split of the data, which is not the same
   Our monocular trained approach, like all self-supervised            as the Eigen split. As a result, we train a new model on the
baselines, has no guarantee of producing results with a                provided training data. At the time of writing, there were
metric scale. Nonetheless, we anticipate that there could              no published self-supervised approaches among the sub-
be value in estimating depth-outputs that are, without spe-            missions on the leaderboard. Despite not using any ground
cial measures, consistent with each other across all predic-           truth data during training, our monocular only predictions
tions. In [76], the authors independently scale each pre-              are competitive with fully supervised methods, see Table 9.
dicted depth map by the ratio of the median of the ground              Adding stereo data and a more powerful encoder at train-
truth and predicted depth map – for each individual test im-           ing time results in even better performance (Monodepth2
                                                                                                               Table 8. Single scale monocular
  Method            σscale      Abs Rel Sq Rel RMSE RMSE log δ < 1.25 δ < 1.252 δ < 1.253                      evaluation.    Comparison to exist-
  Zhou [76]†        0.210        0.258  2.338 7.040  0.309     0.601    0.853     0.940
                                                                                                               ing monocular supervised methods on
  Mahjourian [40]   0.189        0.221  1.663 6.220  0.265     0.665    0.892     0.962
  GeoNet [71]       0.172        0.202  1.521 5.829  0.244     0.707    0.913     0.970                        KITTI 2015 [13] using the Eigen split
  Ranjan [51]       0.162        0.188  1.298 5.467  0.232     0.724    0.927     0.974                        with improved ground truth from [59]
  EPC++ [38]        0.123        0.153  0.998 5.080  0.204     0.805    0.945     0.982                        using a single scale for each method.
  DDVO [62]         0.108        0.147  1.014 5.183  0.204     0.808    0.946     0.983                        † indicates newer results from the on-
  Monodepth2        0.093        0.109  0.623 4.136  0.154     0.873    0.977     0.994                        line implementation.

       Method           Train    SILog   sqErrorRel   absErrorRel   iRMSE         Input     Zhou et al. [76]    DDVO [62]      MD2 M     Ground truth
      DORN [10]          D       11.77      2.23         8.78        12.98
      DABC [34]          D       14.49      4.08         12.72       15.53
     APMoE [29]          D       14.74      3.88         11.74       15.63
      CSWS [32]          D       14.85      3.48         11.84       16.38
     DHGRL [74]          D       15.47      4.04         12.52       15.72
    Monodepth [15]        S      22.02     20.58         17.79       21.84
     Monodepth2          M       15.57      4.52         12.98       16.70
     Monodepth2          MS      15.07      4.16         11.64       15.27
 Monodepth2 (ResNet 50) MS       14.41      3.67         11.22       14.73

Table 9. KITTI depth prediction benchmark. Comparison of
our monocular plus stereo approaches to fully supervised methods
on the KITTI depth prediction benchmark [27]. D indicates mod-
els that were trained with ground truth depth supervision, while M           Figure 10. Additional Make3D results. Our model (MD2 M)
and S are monocular and stereo self-supervision respectively.                trained on KITTI results in plausible depths, predicting more detail
                                                                             than existing monocular methods. The last row is an interesting
                                                                             failure for all methods as it contains an image that is very different
(ResNet50)).                                                                 than those from the KITTI training set.
   Because the evaluation server does not do median scaling
(required for monocular methods), we needed a way to find
the correct scaling for our mono-only model, which makes                     estimation methods by running each test image through
unscaled predictions. We make predictions with our mono-                     the network twice, once unflipped and then flipped. The
model on 1,000 images from the KITTI training set which                      two predictions are then masked and averaged. This has
have ground truth depths available, and for each of the 1,000                been shown to bring significant gains in accuracy for stereo
images we find the scale factor which best align the depth                   results, at the expense of requiring two forward-passes
maps [76]. Finally, we take the median of these 1,000 scale                  through the network at test time [15, 50]. In Table 10 we
factors as the single factor which we use to scale all pre-                  show, for the first time, that post-processing also improves
dictions from our mono model. Note that, to remain true                      quantitative performance in the monocular only (M) and
to our ‘self-supervised’ philosophy, we never do any other                   mixed (MS) training cases.
form of validation, model selection or parameter tuning us-
ing ground truth depths. For comparison, we trained a ver-                   G. Effect of Image Resolution
sion of the original Monodepth [15] using the online code1
                                                                                 In the main paper, we presented results at our standard
on the same benchmark split.
                                                                             resolution (640 × 192). We also showed additional results
E. Additional Qualitative Comparisons                                        at higher (1024×320) and lower (416×128) resolutions. In
                                                                             Table 11 we show a full set of results at all three resolutions.
    We include additional qualitative results from the KITTI                 We see that higher resolution helps, confirming the finding
test set in Fig. 13. We can see that our models generate                     in [47]. We also include an ablation showing that, even at
higher quality outputs and do not produce ‘holes’ in the                     the highest resolution, our full-res multi-scale still provides
depth maps or border artifacts that can be seen in many ex-                  benefit beyond just higher resolution training (vs. ‘Ours w/o
isting baselines e.g. [76, 51, 15, 73]. We also show addi-                   full-res multi-scale’).
tional results from Make3D in Fig. 10.                                           Our high resolution models were initialized using the
                                                                             weights from our standard resolution (640 × 192) model
F. Results with Post-Processing                                              after 10 epochs of training. We then trained our high reso-
                                                                             lution models for 5 epochs with a learning rate of 10−5 . We
   Post-processing, introduced by [15], is a technique to im-
                                                                             used a batch size of 4 to enable this higher resolution model
prove test time results on stereo-trained monocular depth
                                                                             to fit on a single 12GB Titan X GPU.
   1 https://github.com/mrharicot/monodepth                                      Qualitative results of the effect of resolution are illus-
             Method                              Train       Abs Rel   Sq Rel   RMSE     RMSE log   δ < 1.25   δ < 1.252   δ < 1.253
             Monodepth2 w/o pretraining           M           0.132    1.044    5.142     0.210       0.845      0.948       0.977
             Monodepth2 w/o pretraining + pp      M           0.129    1.003    5.072     0.207       0.848      0.949       0.978
             Monodepth2                           M           0.115    0.903    4.863     0.193       0.877      0.959       0.981
             Monodepth2 + pp                      M           0.112    0.851    4.754     0.190       0.881      0.960       0.981
             Monodepth2 (1024 × 320)              M           0.115    0.882    4.701     0.190       0.879      0.961       0.982
             Monodepth2 (1024 × 320) + pp         M           0.112    0.838    4.607     0.187       0.883      0.962       0.982
             Monodepth2 w/o pretraining            S          0.130    1.144     5.485    0.232      0.831       0.932       0.968
             Monodepth2 w/o pretraining + pp       S          0.128    1.089     5.385    0.229      0.832       0.934       0.969
             Monodepth2                            S          0.109    0.873     4.960    0.209      0.864       0.948       0.975
             Monodepth2 + pp                       S          0.108    0.842     4.891    0.207      0.866       0.949       0.976
             Monodepth2 (1024 × 320)               S          0.107    0.849     4.764    0.201      0.874       0.953       0.977
             Monodepth2 (1024 × 320) + pp          S          0.105    0.822     4.692    0.199      0.876       0.954       0.977
             Monodepth2 w/o pretraining           MS          0.127    1.031     5.266    0.221      0.836       0.943       0.974
             Monodepth2 w/o pretraining + pp      MS          0.125    1.000     5.205    0.218      0.837       0.944       0.974
             Monodepth2                           MS          0.106    0.818     4.750    0.196      0.874       0.957       0.979
             Monodepth2 + pp                      MS          0.104    0.786     4.687    0.194      0.876       0.958       0.980
             Monodepth2 (1024 × 320)              MS          0.106    0.806     4.630    0.193      0.876       0.958       0.980
             Monodepth2 (1024 × 320) + pp         MS          0.104    0.775     4.562    0.191      0.878       0.959       0.981
Table 10. Effect of post-processing. We observe that post-processing, originally motivated only for stereo training, also brings consistent
benefits to all our monocular-trained models. Interestingly, for some metrics post-processing results in a larger quantitative gain than
models trained at higher resolution.

                     Train Resolution Full-res multi-scale    Abs Rel Sq Rel RMSE RMSE log δ < 1.25 δ < 1.252 δ < 1.253       Train. time (h)
        Monodepth2    M     416 × 128          X               0.128  1.087 5.171  0.204     0.855    0.953     0.978                9
        Monodepth2    M     640 × 192          X               0.115  0.903 4.863  0.193     0.877    0.959     0.981               12
        Monodepth2    M 1024 × 320             X               0.115  0.882 4.701  0.190     0.879    0.961     0.982             6+9†
        Monodepth2     S    416 × 128          X               0.118  0.971 5.231  0.218     0.848    0.943     0.973                6
        Monodepth2     S    640 × 192          X               0.109  0.873 4.960  0.209     0.864    0.948     0.975                8
        Monodepth2     S   1024 × 320          X               0.105  0.822 4.692  0.199     0.876    0.954     0.977             4+8†
        Monodepth2    MS 416 × 128             X               0.118  0.935 5.119  0.210     0.852    0.949     0.976               11
        Monodepth2    MS 640 × 192             X               0.106  0.818 4.750  0.196     0.874    0.957     0.979               15
        Monodepth2    MS 1024 × 320            X               0.106  0.806 4.630  0.193     0.876    0.958     0.980           7.5 + 10 †
Table 11. Ablation study on the input/output resolutions of our model. †Timings for the highest resolution models comprise 10 epochs
training of the 640 × 192 model and 5 epochs of the 1024 × 320 model.

               Input                   Monodepth2 MS 128 × 416                  Monodepth2 MS 192 × 640         Monodepth2 MS 320 × 1024

Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for
visualization. Our lowest resolution model (128 × 416) captures the broad shape of the scene successfully, but struggles with thin objects
and sometimes fails to accurately capture the shape of depth discontinuities around object boundaries.

trated in Fig. 11. It is clear that all resolutions accurately                  thin objects.
capture the overall shape of the scene. However, only the
highest resolution model accurately represents the shape of
                                                                                                  RMSE
                      Pose network architecture Input frames Pretrained   Abs Rel Sq Rel RMSE           δ <1.25 δ <1.252 δ < 1.253
                                                                                                   log
                    PoseCNN [62]                     2           X        0.138   1.122   5.308   0.209  0.840    0.950    0.978
                    PoseCNN [62]                     3           X        0.148   1.211   5.595   0.219  0.815    0.942    0.976
                    Shared encoder (arXiv v1)        2           X        0.125   0.986   5.070   0.201  0.857    0.954    0.979
                    Shared encoder (arXiv v1)        3           X        0.123   1.031   5.052   0.199  0.863    0.954    0.979
       Monodepth2 ⇒ Separate ResNet                  2           X        0.115   0.919   4.863   0.193  0.877    0.959    0.981
                    Separate ResNet                  3           X        0.115   0.902   4.847   0.193  0.877    0.960    0.981
                    PoseCNN [62]                     2                    0.147   1.164   5.445   0.221  0.818    0.940    0.974
                    PoseCNN [62]                     3                    0.147   1.117   5.403   0.222  0.815    0.940    0.976
                    Shared encoder (arXiv v1)        2                    0.149   1.153   5.567   0.229  0.807    0.934    0.972
                    Shared encoder (arXiv v1)        3                    0.145   1.159   5.482   0.224  0.818    0.937    0.973
       Monodepth2 ⇒ Separate ResNet                  2                    0.132   1.044   5.142   0.210  0.845    0.948    0.977
                    Separate ResNet                  3                    0.132   1.017   5.169   0.211  0.842    0.947    0.977
Table 12. Ablation of the effect of pose networks on depth prediction. Results shown are on depth prediction on the KITTI dataset,
when trained from monocular sequences only. ‘Input Frames’ indicate how many frames are fed to the pose network. ‘Shared encoder
(arXiv v1)’ denotes the architecture proposed in v1 of this paper.

H. Comparison of Pose Encoder
   In Table 12 we evaluate different pose encoders. In an
earlier version of this paper, we proposed the use of a shared
pose encoder that shared features with the depth network.
This resulted in fewer parameters to optimize during train-
ing, but also results in a decrease in depth prediction accu-
racy, see Table 12. As a baseline we compare against the
pose network used by [62], which builds upon [76] with
an additional scaling of the translation by the mean of the
inverse depth. Overall, our separate encoder is superior for
both pretrained and non-pretrained variants, whether we use
two or three frames as input.

I. Supplementary Video Results
    In the supplementary video, we show results on ‘Wan-
der’, a monocular dataset collected from the ‘Wind Walk
Travel Videos’ YouTube channel.2 This dataset is quite dif-
ferent from the car mounted videos of KITTI as it only fea-
tures a monocular hand-held camera in a non-European en-
vironment. We train on four sequences and present results
on a fifth unseen sequence. We use an input/output reso-
lution of 128 × 224. As with our KITTI experiments we
train for 20 epochs with a batch size of 12, with a learn-
ing rate of 10−4 which is reduced by a factor of 10 for the
final 5 epochs. For these handheld videos we found that                   Figure 12. Additional Wander results. We observe that our
the SSIM loss produced artifacts at object edges. As a re-                model (Ours M) results in fewer visual artifacts when compared
sult, we used a feature reconstruction loss in the appearance             to the the baseline (i.e. the same model including VGG loss, but
                                                                          without our contributions).
matching term, as in [52, 58, 73], by computing the L1 dis-
tance on the reprojected and normalized relu1 1 features
from an ImageNet pretrained VGG16 [57] as our pe func-
tion. This takes significantly longer to train, but results in
qualitatively better depth maps on this dataset. Examples of
predicted depths can be seen in Fig. 12.

  2 https://www.youtube.com/channel/

UCPur06mx78RtwgHJzxpu2ew
        Input
        DDVO [62] Zhan et al. [73] Zhou et al. [76] Monodepth [15] Garg et al. [12]
          GeoNet [71] Mahjourian et al. [40]
        Ranjan et al. [51]
          EPC++ [38]
          3Net [50]
                Baseline M
               Ours M
               Ours S
               Ours MS

Figure 13. Additional KITTI Eigen split test results. We can see that our approaches in the last three rows produce the sharpest depth
maps. ‘Baseline M’ is our model without our contributions.
