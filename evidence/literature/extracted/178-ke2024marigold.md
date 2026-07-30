---
source_id: 178
bibtex_key: ke2024marigold
title: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation
year: 2024
domain_theme: Estimasi Kedalaman
verified_pdf: 178_Marigold.pdf
char_count: 93248
---

Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

                                                                       Bingxin Ke            Anton Obukhov     Shengyu Huang
                                                                     Nando Metzger           Rodrigo Caye Daudt Konrad Schindler
                                                                               Photogrammetry and Remote Sensing, ETH Zürich
arXiv:2312.02145v2 [cs.CV] 3 Apr 2024

                                        Figure 1. We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core
                                        principle is to leverage the rich visual knowledge stored in modern generative image models. Our model, derived from Stable Diffusion and
                                        fine-tuned with synthetic data, can zero-shot transfer to unseen datasets, offering state-of-the-art monocular depth estimation results.

                                                                  Abstract                                      monocular depth estimation that is derived from Stable Dif-
                                                                                                                fusion and retains its rich prior knowledge. The estimator
                                            Monocular depth estimation is a fundamental computer                can be fine-tuned in a couple of days on a single GPU us-
                                        vision task. Recovering 3D depth from a single image is                 ing only synthetic training data. It delivers state-of-the-art
                                        geometrically ill-posed and requires scene understanding,               performance across a wide range of datasets, including over
                                        so it is not surprising that the rise of deep learning has led to       20% performance gains in specific cases. Project page:
                                        a breakthrough. The impressive progress of monocular depth              https://marigoldmonodepth.github.io.
                                        estimators has mirrored the growth in model capacity, from
                                        relatively modest CNNs to large Transformer architectures.
                                        Still, monocular depth estimators tend to struggle when pre-            1. Introduction
                                        sented with images with unfamiliar content and layout, since
                                        their knowledge of the visual world is restricted by the data           Monocular depth estimation aims to transform a photo-
                                        seen during training, and challenged by zero-shot general-              graphic image into a depth map, i.e., regress a range value for
                                        ization to new domains. This motivates us to explore whether            every pixel. The task arises whenever the 3D scene structure
                                        the extensive priors captured in recent generative diffusion            is needed, and no direct range or stereo measurements are
                                        models can enable better, more generalizable depth estima-              available. Clearly, undoing the projection from the 3D world
                                        tion. We introduce Marigold, a method for affine-invariant              to a 2D image is a geometrically ill-posed problem and can

                                                                                                            1
only be solved with the help of prior knowledge, such as typ-          1. A simple and resource-efficient fine-tuning protocol to
ical object shapes and sizes, likely scene layouts, occlusion             convert a pretrained LDM image generator into an image-
patterns, etc. In other words, monocular depth implicitly re-             conditional depth estimator;
quires scene understanding, and it is no coincidence that the          2. Marigold, a state-of-the-art, versatile monocular depth es-
advent of deep learning brought about a leap in performance.              timation module that offers excellent performance across
Depth estimation is nowadays cast as neural image-to-image                a wide variety of natural images.
translation and learned in a supervised (or semi-supervised)
fashion using collections of paired, aligned RGB images                2. Related Work
and depth maps. Early methods of this type were limited
to a narrow domain defined by their training data, often in-           2.1. Monocular Depth
door [47] or driving [18] scenes. More recently, there has
                                                                       At the technical level, monocular depth estimation is a
been a quest to train generic depth estimators that can be
                                                                       dense, structured regression task. The pioneering work
either used off-the-shelf across a broad range of scenes or
                                                                       of Eigen et al. [14] introduced a multi-scale network and
fine-tuned to a specific application scenario with a small
                                                                       showed that the result can be converted to metric depth
amount of data. These models generally follow the strategy
                                                                       for a dataset recorded with a single sensor. Successive im-
first employed by MiDAS [35] to achieve generality, namely
                                                                       provements have come from various fronts, including ordinal
to train a high-capacity model with data sampled from many
                                                                       regression [15], planar guidance maps [24], neural condi-
different RGB-D datasets (respectively, domains). The latest
                                                                       tional random fields [59], vision transformers [1, 27, 54], a
developments include moving from convolutional encoder-
                                                                       piecewise planarity prior [34], first-order variational con-
decoder networks [35] to increasingly large and powerful
                                                                       straints [28] and variational autoencoders [32]. Some
vision transformers [36], and training on more and more
                                                                       authors treat depth estimation as a combined regression-
data and with additional surrogate tasks [13] to amass even
                                                                       classification task, using various binning strategies like Ad-
more knowledge about the visual world, and consequently
                                                                       aBins [4] or BinsFormer [26] to discretize depth range. A
to produce better depth maps. Importantly, visual cues for
                                                                       notable recent trend involves training generative models,
depth depend not only on the scene content but also on the
                                                                       especially diffusion models [20, 49] for monocular depth
(generally unknown) camera intrinsics [58]. For general in-
                                                                       estimation [12, 22, 43, 44]. Recently, a few works [19, 58]
the-wild depth estimation, it is often preferred to estimate
                                                                       have revisited absolute depth estimation, by explicitly feed-
affine-invariant depth (i.e., depth values up to a global offset
                                                                       ing camera intrinsics as additional input.
and scale), which can also be determined without objects of
known sizes that could serve as “scale bars”.                             Estimating depth “in the wild” refers to methods that are
                                                                       successful across a wide range of (possibly unfamiliar) set-
    The intuition behind our work is the following: Modern             tings, a particularly challenging task. It has been addressed
image diffusion models have been trained on internet-scale             by constructing large and diverse depth datasets and design-
image collections specifically to generate high-quality im-            ing algorithms to handle that diversity. DIW [8] was perhaps
ages across a wide array of domains [3, 38, 41]. If the                the earliest work to introduce an uncontrolled dataset and
cornerstone of monocular depth estimation is indeed a com-             to predict relative (ordinal) depth for it. OASIS [9] intro-
prehensive, encyclopedic representation of the visual world,           duced relative depth and normals to better generalize across
then it should be possible to derive a broadly applicable              scenes. However, relative depth predictions (depth ordering)
depth estimator from a pretrained image diffusion model.               are of limited use for many downstream tasks, which has
In this paper, we set out to explore this option and develop           led several authors to consider affine-invariant depth. In
Marigold, a latent diffusion model (LDM) based on Stable               that setting, depth is estimated up to an unknown (global)
Diffusion [38], along with a fine-tuning protocol to adapt the         offset and scale. It offers a viable compromise between the
model for depth estimation. The key to unlocking the poten-            ordinal and metric cases: on the one hand, it can handle
tial of a pretrained diffusion model is to keep its latent space       general scenes consisting of unfamiliar objects; on the other
intact. We find this can be done efficiently by modifying and          hand, depth differences between different objects or scene
fine-tuning only the denoising U-Net. Turning Stable Diffu-            parts are still geometrically meaningful relative to each other.
sion into Marigold requires only synthetic RGB-D data (in              MegaDepth [25] and DiverseDepth [56] utilize large internet
our case, the Hypersim [37] and Virtual KITTI [7] datasets)            photo collections to train models that can adapt to unseen
and a few GPU days on a single consumer graphics card.                 data, while MiDaS [35] achieves generality by training on a
Empowered by the underlying diffusion prior of natural im-             mixture of multiple datasets. The step from CNNs to vision
ages, Marigold exhibits excellent zero-shot generalization:            transformers has further boosted performance, as evidenced
Without ever having seen real depth maps, it attains state-of-         by DPT [36] and Omnidata [13]. LeReS [57] proposed a
the-art performance on several real datasets. To summarize,            two-stage framework that first predicts affine-invariant depth,
our contributions are:                                                 then upgrades it to metric depth by estimating the shift and

                                                                   2
focal length. HDN [60] introduced multi-scale depth nor-             2.4. Foundation Models
malization to improve the prediction details and smoothness
                                                                     Vision foundation models (VFMs) are large neural networks
further. While this enables the depth estimator to handle
                                                                     trained on internet-scale data. The extreme scaling leads to
images captured with different known cameras, it does not
                                                                     the emergence of high-level visual understanding, such that
include the true in-the-wild setting, where the camera intrin-
                                                                     the model can then be used as is [52] or fine-tuned to a wide
sics of the test images are unknown. Our method addresses
                                                                     range of downstream tasks with minimal effort [6]. Prompt
affine-invariant depth estimation but does not focus on com-
                                                                     tuning methods [2, 55, 63] can efficiently adapt VFMs to-
piling an extensive, annotated training dataset. Rather, we
                                                                     wards dedicated scenarios by designing suitable prompts.
utilize the broader image priors in image LDMs and apply
                                                                     Feature adaptation methods [5, 16, 33, 62, 64, 65] can fur-
fine-tuning.
                                                                     ther pivot VFMs towards different tasks. E.g., VPD [64]
                                                                     showed the potential to extract features from a pre-trained
2.2. Diffusion Models                                                text-to-image model for (domain-specific) depth estimation.
Denoising Diffusion Probabilistic Models (DDPMs) [20]                Concurrently, I-LoRA [11] demonstrated the multi-modal
have emerged as a powerful class of generative models. They          capabilities of pre-trained image generators. Direct tun-
learn to reverse a diffusion process that progressively de-          ing enables more flexible adaptation, not only for few-shot
grades images with Gaussian noise so that they can draw sam-         customization scenarios like DreamBooth [39] but also for
ples from the data distribution by applying the reverse pro-         object detection, as in 3DiffTection [53].
cess to random noise. This idea was extended to DDIMs [49],             The Marigold depth estimator proposed here can be in-
which provide a non-Markovian shortcut for the diffusion             terpreted as an instance of such direct tuning, where Sta-
process. Conditional diffusion models are an extension of            bleDiffusion plays the role of the foundation model. With as
DDPMs [20, 49] that ingest additional information on which           few as 74k synthetic depth samples, we obtain state-of-the-
the output is then conditioned, similar to cGAN [29] and             art depth estimates on real image datasets, and convincing
cVAE [48]. Conditioning can take various forms, including            performance in the wild (cf . Fig. 1).
text [41], other images [40], or semantic maps [61].
   In the realm of text-based image generation, Rombach              3. Method
et al. [38] have trained a diffusion model on the large-scale        3.1. Generative Formulation
image and text dataset LAION-5B [46] and demonstrated
image synthesis with previously unattainable quality. The            We pose monocular depth estimation as a conditional denois-
cornerstone of their approach is a latent diffusion model            ing diffusion generation task and train Marigold to model the
(LDM), where the denoising process is run in an efficient la-        conditional distribution D(d | x) over depth d ∈ RW ×H ,
tent space, drastically reducing the complexity of the learned       where the condition x ∈ RW ×H×3 is an RGB image.
mapping. Such models distill internet-scale image sets into              In the forward process, which starts at d0 := d from the
model weights, thereby developing a rich scene understand-           conditional distribution, Gaussian noise is gradually added
ing prior, which we harness for monocular depth estimation.          at levels t ∈ {1, ..., T } to obtain noisy samples dt as

                                                                                         \depth _t = \sqrt {\bar {\alpha }_t} \depth _0 + \sqrt {1 - \bar {\alpha }_t} \noise  (1)
2.3. Diffusion for Monocular Depth Estimation
                                                                                                                            Qt
Several methods have tried to use DDPMs for metric depth             where ϵ ∼ N (0, I), ᾱt := s=1 1−βs , and {β1 , . . . , βT }
estimation. The DDP approach [22] proposes an architec-              is the variance schedule of a process with T steps. In the
ture to encode the image but decode a depth map and has              reverse process, the conditional denoising model ϵθ (·) pa-
obtained state-of-the-art results on the KITTI dataset. Diffu-       rameterized with learned parameters θ gradually removes
sionDepth [12] performs diffusion in the latent space, condi-        noise from dt to obtain dt−1 .
tioned on image features extracted with a SwinTransformer.               At training time, parameters θ are updated by taking a
DepthGen [44] extends a multi-task diffusion model to met-           data pair (x, d) from the training set, noising d with sam-
ric depth prediction, including handling noisy ground truth.         pled noise ϵ at a random timestep t, computing the noise
Its successor DDVM [43] emphasizes pretraining on syn-               estimate ϵ̂ = ϵθ (dt , x, t) and minimizing one of the denois-
thetic and real data for enhanced depth estimation. Finally,         ing diffusion objective functions. The canonical standard
VPD [64] employs a pretrained Stable Diffusion model as              noise objective L is given as follows [20]:
an image feature extractor with additional text input.                                      \mathcal {L} = \mathbb {E}_{\depth _0, \noise \sim \mathcal {N}(0,I),t \sim \mathcal {U}(T)} \left \| \noise - \hat {\noise } \right \|^2_2. \label {eq:diffusion_objective}    (2)
    Our approach advances beyond these methods, which
perform well but only in their specific training domains. We         At inference time, d := d0 is reconstructed starting from a
explore the potential of pretrained LDMs for single-image            normally-distributed variable dT , by iteratively applying the
depth estimation across diverse, real-world settings.                learned denoiser ϵθ (dt , x, t).

                                                                 3
                                                                                depth map into three channels to simulate an RGB image.
                  
                                           *)'*&(
                                                       
                                                     
                                                                                At this point, the data range of the depth data plays a sig-
                 
                                                         
                                                                                nificant role in enabling affine-invariance. We discuss our
                                                                                normalization approach in Sec. 3.3. We verified that without
                                                                                any modification of the VAE or the latent space structure,
                              C
                                                                       the depth map can be reconstructed from the encoded latent
                                                        0 
                                                                                code with a negligible error, i.e., d ≈ D(E(d)). At infer-
                                                       -   0,+/.
                                                                                ence time, the depth latent code is decoded once at the end
                %$ #                                                          of diffusion, and the average of three channels is taken as
                  
                                                                                the predicted depth map.
                                                                                Adapted denoising U-Net. To implement the conditioning
                                                                                                            (d)
Figure 2. Overview of the Marigold fine-tuning protocol. Start-                 of the latent denoiser ϵθ (zt , z(x) , t) on input image x, we
ing from pretrained Stable Diffusion, we encode the image x and                 concatenate the image and depth latent codes into a single
depth d into the latent space using the original Stable Diffusion                                (d)
                                                                                input zt = cat(zt , z(x) ) along the feature dimension. The
VAE. We fine-tune just the U-Net by optimizing the standard diffu-
sion objective relative to the depth latent code. Image conditioning            input channels of the latent denoiser are then doubled to
is achieved by concatenating the two latent codes before feeding                accommodate the expanded input zt . To prevent inflation
them into the U-Net. The first layer of the U-Net is modified to ac-            of activations magnitude of the first layer and keep the pre-
cept concatenated latent codes. See details in Sec. 3.2 and Sec. 3.3.           trained structure as faithfully as possible, we duplicate the
                                                                                weight tensor of the input layer and divide its values by two.

   Unlike diffusion models that work directly on the data,                      3.3. Fine-Tuning Protocol
latent diffusion models perform diffusion steps in a low-                       Affine-invariant depth normalization. For the ground
dimensional latent space, offering computational efficiency                     truth depth maps d, we implement a linear normalization
and suitability for high-resolution image generation [38].                      such that the depth primarily falls in the value range [−1, 1],
The latent space is constructed in the bottleneck of a varia-                   to match the designed input value range of the VAE. Such
tional autoencoder (VAE) trained independently of the de-                       normalization serves two purposes. First, it is the conven-
noiser to enable latent space compression and perceptual                        tion for working with the original Stable Diffusion VAE.
alignment with the data space. To translate our formulation                     Second, it enforces a canonical affine-invariant depth rep-
into the latent space, for a given depth map d, the corre-                      resentation independent of the data statistics – any scene
sponding latent code is given by the encoder E: z(d) = E(d).                    must be bounded by near and far planes with extreme depth
Given a depth latent code, a depth map can be recovered                         values. The normalization is achieved through an affine
with the decoder D: d̂ = D(z(d) ). The conditioning im-                         transformation computed as
age x is also naturally translated into the latent space as
z(x) = E(x). The denoiser is henceforth trained in the latent                                    \Tilde {\depth } = \left (\frac {\depth - \depth _{2}}{\depth _{98} - \depth _{2}} - 0.5\right ) \times 2, 
             (d)                                                                                                                                                                                               (3)
space: ϵθ (zt , z(x) , t). The adapted inference procedure
involves one extra step – the decoder D reconstructing the
                                         (d)          (d)                       where d2 and d98 correspond to the 2% and 98% per-
data d̂ from the estimated clean latent z0 : d̂ = D(z0 ).
                                                                                centiles of individual depth maps. This normalization allows
3.2. Network Architecture                                                       Marigold to focus on pure affine-invariant depth estimation.
                                                                                Training on synthetic data. Real depth datasets suffer from
One of our main objectives is training efficiency since diffu-                  missing depth values caused by the physical constraints of
sion models are often extremely resource-intensive to train.                    the capture rig and the physical properties of the sensors.
Therefore, we base our model on a pretrained text-to-image                      Specifically, the disparity between cameras and reflective
LDM (Stable Diffusion v2 [38]), which has learned very                          surfaces diverting LiDAR laser beams are inevitable sources
good image priors from LAION-5B [46]. With minimal                              of ground truth noise and missing pixels [21, 51]. In contrast
changes to the model components, we turn it into an image-                      to prior work that utilized diverse real datasets to achieve
conditioned depth estimator. Fig. 2 contains an overview of                     generalization [13, 35], we train exclusively with synthetic
the proposed fine-tuning procedure.                                             depth datasets. As with the depth normalization rationale,
Depth encoder and decoder. We take the frozen VAE to                            this decision has two objective reasons. First, synthetic
encode both the image and its corresponding depth map into                      depth is inherently dense and complete, meaning that every
a latent space for training our conditional denoiser. Given                     pixel has a valid ground truth depth value, allowing us to
that the encoder, which is designed for 3-channel (RGB)                         feed such data into the VAE, which can not handle data
inputs, receives a single-channel depth map, we replicate the                   with invalid pixels. Second, synthetic depth is the cleanest

                                                                            4
                                                                             Markovian sampling with re-spaced steps for accelerated
                                                                   inference. The final depth map is decoded from the latent
                                                  
                                                                             code using the VAE decoder and postprocessed by averaging
                                                                             channels.
                                                                             Test-time ensembling. The stochastic nature of the infer-
                 
                              &%#&"$
                                              
                                                            
                                                                             ence pipeline leads to varying predictions depending on the
                                           ,+ 0
                                                                                                      (d)
                                            )( 
                                                                             initialization noise in zT . Capitalizing on that, we propose
                                                                             the following test-time ensembling scheme, capable of com-
                                                                             bining multiple inference passes over the same input. For
                                                                             each input sample, we can run inference N times. To aggre-
Figure 3. Overview of the Marigold inference scheme. Given an
                                                                             gate these affine-invariant depth predictions {d̂1 , . . . , d̂N },
input image x, we encode it with the original Stable Diffusion VAE
                                                                   (d)       we jointly estimate the corresponding scale ŝi and shift t̂i ,
into the latent code z(x) , and concatenate with the depth latent zt
before giving it to the modified fine-tuned U-Net on every denoising         relative to some canonical scale and range, in an iterative
iteration. After executing the schedule of T steps, the resulting            manner. The proposed objective minimizes the distances be-
                (d)
depth latent z0 is decoded into an image, whose 3 channels are               tween each pair of scaled and shifted predictions (d̂′ i , d̂′ j ),
averaged to get the final estimation d̂. See Sec. 3.4 for details.           where d̂′ = d̂ × ŝ + t̂. In each optimization step, we cal-
                                                                             culate the merged depth map m by the taking pixel-wise
                                                                             median m(x, y) = median(d̂′ 1 (x, y), . . . , d̂′ N (x, y)). An
possible form of depth, which is guaranteed by the rendering                 extra regularization term R = |min(m)| + |1 − max(m)|, is
pipeline. If our assumption about the possibility of fine-                   added to prevent collapse to the trivial solution and enforce
tuning a generalizable depth estimation from a text-to-image                 the unit scale of m. Thus, the objective function can be
LDM is correct, then synthetic depth gives the cleanest set                  written as follows:
of examples and reduces noise in gradient updates during
the short fine-tuning protocol. Thus, the remaining concern                            \min _{\substack {s_1,\ldots ,s_N \\ t_1, \ldots , t_N}} \Bigg ( \sqrt {\frac {1}{b} \sum _{i=1}^{N-1} \sum _{j=i+1}^{N} \| \translated _i - \translated _j \|_2^2} + \lambda \mathcal {R} \Bigg ) \label {eq:align}    (4)
is the sufficient diversity or domain gaps between synthetic
and real data, which sometimes limits generalization ability.
                                                                             where the binominal coefficient b = N2 represents the
                                                                                                                         
As demonstrated in our experiments, our choice of synthetic
datasets leads to impressive zero-shot transfer.                             number of possible combinations of image pairs from N im-
Annealed multi-resolution noise. Previous works have                         ages. After the iterative optimization for spatial alignment,
explored deviations from the original DDPM formulations,                     the merged depth m is taken as our ensembled prediction.
such as non-Gaussian noise [30] or non-Markovian schedule                    Note that this ensembling step requires no ground truth for
shortcuts [49]. Our proposed setting and the fine-tuning pro-                aligning independent predictions. This scheme enables a
tocol outlined above are permissive to changes to the noise                  flexible trade-off between computation efficiency and pre-
schedule at the fine-tuning stage. We identified a combina-                  diction quality by choosing N accordingly.
tion of multi-resolution noise [23] and an annealed schedule
to converge faster and substantially improve performance
                                                                             4. Experiments
over the standard DDPM formulation. The multi-resolution                     4.1. Implementation
noise is composed by superimposing several random Gaus-
sian noise images of different scales, all upsampled to the                  We implement Marigold using PyTorch and utilize Stable
U-Net input resolution. The proposed annealed schedule                       Diffusion v2 [38] as our backbone, following the original
interpolates between the multi-resolution noise at t = T and                 pre-training setup with a v-objective [42]. We disable text
standard Gaussian noise at t = 0.                                            conditioning and perform the steps outlined in Sec. 3.2. Dur-
                                                                             ing training, we apply the DDPM noise scheduler [20] with
3.4. Inference                                                               1000 diffusion steps. At inference time, we apply the DDIM
                                                                             scheduler [49] and only sample 50 steps. For the final pre-
Latent diffusion denoising. The overall inference pipeline                   diction, we aggregate results from 10 inference runs with
is presented in Fig. 3. We encode the input image into the                   varying starting noise. Training our method takes 18K itera-
latent space, initialize depth latent as standard Gaussian                   tions using a batch size of 32. To fit one GPU, we accumulate
noise, and progressively denoise it with the same schedule                   gradients for 16 steps. We use the Adam optimizer with a
as during fine-tuning. We empirically find that initializing                 learning rate of 3 · 10−5 . Additionally, we apply random hor-
with standard Gaussian noise gives better results than with                  izontal flipping augmentation to the training data. Training
multi-resolution noise, although the model is trained on the                 our method to convergence takes approximately 2.5 days on
latter. We follow DDIM’s [49] approach to perform non-                       a single Nvidia RTX 4090 GPU card.

                                                                         5
Table 1. Quantitative comparison of Marigold with SOTA affine-invariant depth estimators on several zero-shot benchmarks. All metrics†
are presented in percentage terms; bold numbers are the best, underscored second best. Our method outperforms other methods on both
indoor and outdoor scenes in most cases, without having seen a real depth sample.

                          # Training samples             NYUv2                 KITTI               ETH3D                 ScanNet              DIODE
Method                                                                                                                                                          Avg. Rank
                            Real     Synthetic         AbsRel↓ δ1↑          AbsRel↓ δ1↑          AbsRel↓ δ1↑           AbsRel↓ δ1↑          AbsRel↓ δ1↑
DiverseDepth [56]          320K              —           11.7     87.5        19.0     70.4         22.8    69.4         10.9    88.2         37.6     63.1         7.6
MiDaS [35]                   2M              —           11.1     88.5        23.6     63.0         18.4    75.2         12.1    84.6         33.2     71.5         7.3
LeReS [57]                 300K             54K           9.0     91.6        14.9     78.4         17.1    77.7          9.1    91.7         27.1     76.6         5.2
Omnidata [13]             11.9M            310K           7.4     94.5        14.9     83.5         16.6    77.8          7.5    93.6         33.9     74.2         4.8
HDN [60]                   300K              —            6.9     94.8        11.5     86.7         12.1    83.3          8.0    93.9         24.6     78.0         3.2
DPT [36]                   1.2M            188K          9.8      90.3        10.0     90.1         7.8     94.6          8.2    93.4         18.2     75.8         3.9
Ours (w/o ensemble)               ∗                       6.0     95.9        10.5     90.4         7.1     95.1          6.9    94.5         31.0     77.2         2.5
                              —             74K
Ours (w/ ensemble)                                        5.5     96.4         9.9     91.6         6.5     96.0          6.4    95.1         30.8     77.3         1.4
  †
      Most baselines are sourced from Metric3D [58], except for the ScanNet benchmark. For ScanNet, Metric3D used a different random split that is not publicly accessible,
      therefore we re-ran all baselines on our split. For HDN [60] we show the ScanNet results from Metric3D, as no source code is available.
  ∗
      Image-text data is used in the pretrained model.

4.2. Evaluation                                                                           rics [35, 36, 57, 58] for assessing quality of depth estimation.
                                                                                          The first is Absolute   Mean Relative Error (AbsRel), calcu-
Training datasets. We train Marigold on two synthetic                                                1
                                                                                                        PM
                                                                                          lated as: M     i=1 |a i − di |/di , where M is the total num-
datasets covering both indoor and outdoor scenes. Hyper-
                                                                                          ber of pixels. The second metric, δ1 accuracy, measures the
sim [37] is a photorealistic dataset with 461 indoor scenes.
                                                                                          proportion of pixels satisfying max(ai /di , di /ai ) < 1.25.
We use the official split with around 54K samples from 365
scenes for training. Incomplete samples are filtered out.                                 Comparison with other methods. We compare Marigold
RGB images and depth maps are resized to 480 × 640 size.                                  to six baselines, each claiming zero-shot generalization. Di-
Additionally, we transform the original distances relative to                             verseDepth [56], LeReS [57] and HDN [60] estimate affine-
the focal point into conventional depth values relative to the                            invariant depth maps, while MiDaS [35], DPT [36], and Om-
focal plane. The second dataset, Virtual KITTI [7] is a                                   nidata [13] produce affine-invariant disparities. As shown
synthetic street-scene dataset featuring 5 scenes under vary-                             in Tab. 1, Marigold outperforms prior art in most cases and
ing conditions like weather or camera perspectives. Four                                  secures the highest overall ranking. Despite being trained
scenes containing a total of around 20K samples are used                                  solely on synthetic depth datasets, the model can well gen-
for training. We crop the images to the KITTI benchmark                                   eralize to a wide range of real scenes. This successful adap-
resolution [17] and set the far plane to 80 meters.                                       tation of diffusion-based image generation models toward
                                                                                          depth estimation confirms our initial hypothesis that a com-
Evaluation datasets. We evaluate Marigold on 5 real
                                                                                          prehensive representation of the visual world is the corner-
datasets that are not seen during training. NYUv2 [31] and
                                                                                          stone of monocular depth estimation. It also shows that
ScanNet [10] are both indoor scene datasets captured with an
                                                                                          our fine-tuning protocol was successful in adapting Stable
RGB-D Kinect sensor. For NYUv2, we utilize the designated
                                                                                          Diffusion for this task without unlearning such visual priors.
test split, comprising a total of 654 images. In the case of
the ScanNet dataset, we randomly sampled 800 images from                                      For a visual assessment, we present qualitative compar-
the 312 official validation scenes for testing. KITTI [17]                                ison in Fig. 4. Additionally, in Fig. 5, we provide 3D visu-
is a street-scene dataset with sparse metric depth captured                               alizations of reconstructed surface normals. Marigold not
by a LiDAR sensor. We employ the Eigen test split [14]                                    only correctly captures the scene layout, such as the spatial
made of 652 images. ETH3D [45] and DIODE [50] are two                                     relationships between walls and furniture in the first example
high-resolution datasets, both featuring depth maps derived                               in Fig. 5, but also captures fine-grained details, as indicated
from LiDAR sensor measurements. For ETH3D, we incor-                                      by the arrows in Fig. 4. Moreover, the reconstruction of flat
porate all 454 samples with available ground truth depth                                  surfaces, especially walls, is significantly better (see Fig. 4).
maps. For DIODE, we use the entire validation split, which                                Furthermore, our method effectively models common shapes
encompasses 325 indoor samples and 446 outdoor samples.                                   and their layouts, once again aligning with our expectations
                                                                                          regarding the generative prior.
Evaluation protocol. Following the protocol of affine-
invariant depth evaluation [35], we first align the estimated                              4.3. Ablation Studies
merged prediction m to the ground truth d with the least
squares fitting. This step gives us the absolute aligned                                  Two zero-shot validation sets are selected for the ablation
depth map a = m × s + t in the same units as the                                          studies – the official training split of NYUv2 [31], consist-
ground truth. Next, we apply two widely recognized met-                                   ing of 785 samples, and a randomly selected subset of 800

                                                                                      6
          Input RGB Image       MiDaS                Omnidata                 DPT             Marigold (ours)        Ground Truth
NYUv2
KITTI
ETH3D
Scannet
DIODE

Figure 4. Qualitative comparison (depth) of monocular depth estimation methods across different datasets. Marigold excels at capturing
thin structures (e.g., chair legs) and preserving overall layout of the scene (e.g., walls in ETH3D example and chairs in DIODE example).

          Input RGB Image       MiDaS                Omnidata                 DPT             Marigold (ours)        Ground Truth
NYUv2
ScanNet
DIODE

Figure 5. Qualitative comparison (unprojected, colored as normals) of monocular depth estimation methods across different datasets.
Marigold stands out for its superior reconstruction of flat surfaces and detailed structures.

                                                                   7
                        NYUv2                                                                                                    NYUv2
                 6.13                                                                   96.60                             35.2                                                                        98.9

                 5.97                                                                   96.43                             27.5                                                                        85.8

                                                                                                             AbsRel (%)
    AbsRel (%)

                                                                                                                                                                                                             δ1 (%)
                                                                                                δ1 (%)
                                                                              AbsRel                                                                                                         AbsRel
                 5.81                                                                   96.25                             19.7                                                                        72.7
                                                                              δ1                                                                                                             δ1
                 5.65                                                                   96.07                             11.9                                                                        59.5

                 5.49                                                                   95.90                              4.2                                                                        46.4
                        KITTI                                                                                                    KITTI
             11.89                                                                      88.82                             62.0                                                                        91.9

             11.72                                                                      88.50                             48.7                                                                        74.3

                                                                                                             AbsRel (%)
AbsRel (%)

                                                                                                                                                                                                             δ1 (%)
                                                                                                δ1 (%)
                                                                              AbsRel                                                                                                         AbsRel
             11.55                                                                      88.19                             35.5                                                                        56.6
                                                                              δ1                                                                                                             δ1
             11.39                                                                      87.87                             22.2                                                                        39.0

             11.22                                                                      87.55                              8.9                                                                        21.4
                          1     2     5           10                             20                                                1       2         4            10            25     50       100
                                               # Predictions                                                                                         # Inference Steps (log scale)

Figure 6. Ablation of ensemble size. We observe a monotonic                                                  Figure 7. Ablation of denoising steps. The performance improves
improvement with the growth of ensemble size. This improvement                                               as the number of denoising steps increases, while we observe satu-
starts to diminish after 10 predictions per sample.                                                          ration after 10 steps.

Table 2. Ablation of training noise. Multi-resolution noise im-                                              Table 3. Ablation of training datasets. Hypersim [37] delivers
proves over Gaussian noise; annealing yields further improvement.                                            strong results; Virtual KITTI [7] improves outdoor performance.

                    Multi-res.                     NYUv2                  KITTI                                                                Virtual           NYUv2                  KITTI
                                    Annealed                                                                                      Hypersim
                     noise                      AbsRel↓ δ1↑           AbsRel↓ δ1↑                                                              KITTI          AbsRel↓ δ1↑            AbsRel↓ δ1↑

                          ✗            -            7.7        93.4    14.2      82.1                                                  ✗         ✓               13.9       83.4      15.4     79.3
                          ✓            ✗            5.8        96.1    12.1      87.1                                                  ✓         ✗                5.7       96.3      13.7     82.5
                          ✓            ✓            5.6        96.5    11.3      88.7                                                  ✓         ✓                5.6       96.5      11.3     88.7

                                                                                                             on NYUv2 by ≈8% and ensembling 20 predictions brings
images from the KITTI Eigen [14] training split. Refer to
                                                                                                             an improvement of ≈9.5%. It has been observed as a sys-
supplementary sections for extra ablations and discussion.
                                                                                                             tematic effect that the performance is constantly improved
Training noise. We investigate the impact of three types of                                                  as the number of predictions increases, while the marginal
noise during the training phase. As shown in Tab. 2, training                                                improvement diminishes with more than 10 predictions.
with multi-resolution noise significantly improves the depth                                                 Number of denoising steps. We evaluate the effect of
prediction accuracy over using standard Gaussian noise. Fur-                                                 the re-spaced inference denoising steps driven by the DDIM
thermore, the gradual annealing of multi-resolution noise                                                    scheduler [49]. The results are shown in Fig. 7. Although
yields an additional improvement. We also noticed that                                                       trained with 1000 DDPM steps, the choice of 50 steps is
training with multi-resolution noise leads to more consistent                                                sufficient to produce accurate results during inference. As
predictions given different initial noise at inference time and                                              expected, we obtain better results when using more denois-
annealing further enhances this consistency.                                                                 ing steps. We observe that the elbow point of marginal
Training data domain. To better understand the impact                                                        returns given more denoising steps depends on the dataset
of the synthetic datasets used for our fine-tuning protocol,                                                 but is always under 10 steps. This implies that one can fur-
we ablate on a photorealistic street-scene Virtual KITTI [7],                                                ther reduce the denoising steps to 10 or even less to gain
and a more diverse and higher-quality indoor dataset Hyper-                                                  efficiency while keeping comparable performance. Interest-
sim [37]. The results are shown in Tab. 3. When fine-tuned                                                   ingly, this threshold is smaller than what is usually required
on a single synthetic dataset, the pretrained LDM can al-                                                    for diffusion-based image generators [38, 49], i.e., 50 steps.
ready be adapted for monocular depth estimation to a certain
degree, while the more diverse and photorealistic data leads                                                 5. Conclusion
to better performance on both indoor and outdoor scenes.
                                                                                                             We have presented Marigold, a fine-tuning protocol for Sta-
Interestingly, adding additional training data from a differ-
                                                                                                             ble Diffusion and a model for state-of-the-art affine-invariant
ent domain not only improves the performance on the new
                                                                                                             depth estimation. Our results confirm the importance of a de-
domain but also brings improvements in the original domain.
                                                                                                             tailed visual scene understanding prior for depth estimation,
Test-time ensembling. We test the effectiveness of the pro-                                                  which we source from the pretrained text-to-image diffusion
posed test-time ensembling scheme by aggregating various                                                     model. Future research directions to overcome current limi-
numbers of predictions. As shown in Fig. 6, a single pre-                                                    tations include improving inference efficiency, ensuring that
diction of Marigold already yields reasonably good results.                                                  similar inputs yield consistent outputs despite the model’s
Ensembling 10 predictions reduces the absolute relative error                                                generative nature, and better handling of distant scene parts.

                                                                                                         8
References                                                                     adapter: Better vision-language models with feature adapters.
                                                                               International Journal of Computer Vision, 2023. 3
 [1] Shubhra Aich, Jean Marie Uwabeza Vianney, Md Amirul Is-              [17] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
     lam, Mannat Kaur, and Bingbing Liu. Bidirectional attention               ready for autonomous driving? the KITTI vision benchmark
     network for monocular depth estimation. In ICRA, 2021. 2                  suite. In CVPR, 2012. 6, 11, 12, 24, 25, 26
 [2] Hyojin Bahng, Ali Jahanian, Swami Sankaranarayanan, and              [18] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel
     Phillip Isola. Exploring visual prompts for adapting large-               Urtasun. Vision meets robotics: The KITTI dataset. Interna-
     scale models. arXiv preprint arXiv:2203.17274, 2022. 3                    tional Journal of Robotics Research, 2013. 2
 [3] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng             [19] Vitor Guizilini, Igor Vasiljevic, Dian Chen, Rares, Ambrus, ,
     Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee,                  and Adrien Gaidon. Towards zero-shot scale-aware monocu-
     Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu,                  lar depth estimation. In ICCV, 2023. 2
     Yunxin Jiao, and Aditya Ramesh. Improving image genera-              [20] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffu-
     tion with better captions. https://cdn.openai.com/                        sion probabilistic models, 2020. 2, 3, 5
     papers/dall-e-3.pdf, 2023. 2                                         [21] Shengyu Huang, Zan Gojcic, Zian Wang, Francis Williams,
 [4] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.                   Yoni Kasten, Sanja Fidler, Konrad Schindler, and Or Litany.
     AdaBins: Depth estimation using adaptive bins. In CVPR,                   Neural lidar fields for novel view synthesis. In ICCV, 2023. 4
     2021. 2                                                              [22] Yuanfeng Ji, Zhe Chen, Enze Xie, Lanqing Hong, Xihui Liu,
 [5] Anand Bhattad, Daniel McKee, Derek Hoiem, and David                       Zhaoqiang Liu, Tong Lu, Zhenguo Li, and Ping Luo. DDP:
     Forsyth. Stylegan knows normal, depth, albedo, and more. In               Diffusion model for dense visual prediction. In ICCV, 2023.
     Advances in Neural Information Processing Systems, pages                  2, 3
     73082–73103. Curran Associates, Inc., 2023. 3                        [23] Kasiopy.      Multi-resolution noise for diffusion model
 [6] Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Alt-                   training. https : / / wandb . ai / johnowhitaker /
     man, Simran Arora, Sydney von Arx, Michael S. Bernstein,                  multires_noise/reports/Multi-Resolution-
     Jeannette Bohg, Antoine Bosselut, Emma Brunskill, Erik                    Noise - for - Diffusion - Model - Training --
     Brynjolfsson, et al. On the opportunities and risks of founda-            VmlldzozNjYyOTU2 ? s = 31, 2023.                 last accessed
     tion models. arXiv preprint arXiv:2108.07258, 2022. 3                     17.11.2023. 5
 [7] Yohann Cabon, Naila Murray, and Martin Humenberger. Vir-             [24] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and
     tual KITTI 2. arXiv preprint arXiv:2001.10773, 2020. 2, 6,                Il Hong Suh. From big to small: Multi-scale local planar
     8, 11, 12                                                                 guidance for monocular depth estimation. arXiv preprint
 [8] Weifeng Chen, Zhao Fu, Dawei Yang, and Jia Deng. Single-                  arXiv:1907.10326, 2019. 2
     image depth perception in the wild. NeurIPS, 29, 2016. 2             [25] Zhengqi Li and Noah Snavely. MegaDepth: Learning single-
 [9] Weifeng Chen, Shengyi Qian, David Fan, Noriyuki Kojima,                   view depth prediction from internet photos. In CVPR, 2018.
     Max Hamilton, and Jia Deng. OASIS: A large-scale dataset                  2
     for single image 3d in the wild. In CVPR, 2020. 2                    [26] Zhenyu Li, Xuyang Wang, Xianming Liu, and Junjun Jiang.
                                                                               Binsformer: Revisiting adaptive bins for monocular depth
[10] Angela Dai, Angel X. Chang, Manolis Savva, Maciej Halber,
                                                                               estimation. arXiv preprint arXiv:2204.00987, 2022. 2
     Thomas Funkhouser, and Matthias Nießner. ScanNet: Richly-
                                                                          [27] Zhenyu Li, Zehui Chen, Xianming Liu, and Junjun Jiang.
     annotated 3d reconstructions of indoor scenes. In CVPR,
                                                                               Depthformer: Exploiting long-range correlation and local in-
     2017. 6, 12, 28, 29
                                                                               formation for accurate monocular depth estimation. Machine
[11] Xiaodan Du, Nicholas Kolkin, Greg Shakhnarovich, and
                                                                               Intelligence Research, pages 1–18, 2023. 2
     Anand Bhattad. Generative models: What do they know?
                                                                          [28] Ce Liu, Suryansh Kumar, Shuhang Gu, Radu Timofte, and
     do they know things? let’s find out! arXiv, 2023. 3
                                                                               Luc Van Gool. VA-DepthNet: A variational approach to
[12] Yiqun Duan, Xianda Guo, and Zheng Zhu. DiffusionDepth:                    single image depth prediction. In ICLR, 2023. 2
     Diffusion denoising approach for monocular depth estimation.         [29] Mehdi Mirza and Simon Osindero. Conditional generative
     arXiv preprint arXiv:2303.05021, 2023. 2, 3                               adversarial nets. arXiv preprint arXiv:1411.1784, 2014. 3
[13] Ainaz Eftekhar, Alexander Sax, Jitendra Malik, and Amir              [30] Eliya Nachmani, Robin San Roman, and Lior Wolf. Non
     Zamir. Omnidata: A scalable pipeline for making multi-task                Gaussian denoising diffusion models.            arXiv preprint
     mid-level vision datasets from 3d scans. In ICCV, pages                   arXiv:2106.07582, 2021. 5
     10786–10796, 2021. 2, 4, 6, 11, 12                                   [31] Pushmeet Kohli Nathan Silberman, Derek Hoiem and Rob
[14] David Eigen, Christian Puhrsch, and Rob Fergus. Depth                     Fergus. Indoor segmentation and support inference from
     map prediction from a single image using a multi-scale deep               RGBD images. In ECCV, 2012. 6, 11, 12, 23, 24, 31
     network. In NeurIPS, 2014. 2, 6, 8, 11, 12                           [32] Jia Ning, Chen Li, Zheng Zhang, Chunyu Wang, Zigang
[15] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-                         Geng, Qi Dai, Kun He, and Han Hu. All in tokens: Unifying
     manghelich, and Dacheng Tao. Deep ordinal regression                      output space of visual tasks via soft token. In ICCV, pages
     network for monocular depth estimation. In CVPR, pages                    19900–19910, 2023. 2
     2002–2011, 2018. 2                                                   [33] Omiros Pantazis, Gabriel Brostow, Kate Jones, and Oisin
[16] Peng Gao, Shijie Geng, Renrui Zhang, Teli Ma, Rongyao                     Mac Aodha. SVL-adapter: Self-supervised adapter for vision-
     Fang, Yongfeng Zhang, Hongsheng Li, and Yu Qiao. CLIP-                    language pretrained models. In BMVC, 2022. 3

                                                                      9
[34] Vaishakh Patil, Christos Sakaridis, Alexander Liniger, and           [48] Kihyuk Sohn, Honglak Lee, and Xinchen Yan. Learning struc-
     Luc Van Gool. P3depth: Monocular depth estimation with a                  tured output representation using deep conditional generative
     piecewise planarity prior. In CVPR, 2022. 2                               models. In NIPS, 2015. 3
[35] René Ranftl, Katrin Lasinger, David Hafner, Konrad                  [49] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising
     Schindler, and Vladlen Koltun. Towards robust monocular                   diffusion implicit models. arXiv preprint arXiv:2010.02502,
     depth estimation: Mixing datasets for zero-shot cross-dataset             2020. 2, 3, 5, 8
     transfer. IEEE TPAMI, 2020. 2, 4, 6, 11, 12                          [50] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,
[36] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-                 Haochen Wang, Falcon Z. Dai, Andrea F. Daniele, Moham-
     sion transformers for dense prediction. In ICCV, 2021. 2, 6,              madreza Mostajabi, Steven Basart, Matthew R. Walter, and
     11, 12                                                                    Gregory Shakhnarovich. DIODE: A Dense Indoor and Out-
[37] Mike Roberts, Jason Ramapuram, Anurag Ranjan, Atulit Ku-                  door DEpth Dataset. arXiv preprint arXiv:1908.00463, 2019.
     mar, Miguel Angel Bautista, Nathan Paczan, Russ Webb, and                 6, 12, 29
     Joshua M. Susskind. Hypersim: A photorealistic synthetic             [51] Wolfgang Wagner, Andreas Ullrich, Vesna Ducic, Thomas
     dataset for holistic indoor scene understanding. In ICCV,                 Melzer, and Nick Studnicka. Gaussian decomposition and
     2021. 2, 6, 8, 11, 12                                                     calibration of a novel small-footprint full-waveform digitising
[38] Robin Rombach, Andreas Blattmann, Dominik Lorenz,                         airborne laser scanner. ISPRS journal of Photogrammetry
     Patrick Esser, and Björn Ommer. High-resolution image                    and Remote Sensing, 60(2):100–112, 2006. 4
     synthesis with latent diffusion models. In CVPR, pages 10684–        [52] Tianfu Wang, Menelaos Kanakis, Konrad Schindler, Luc Van
     10695, 2022. 2, 3, 4, 5, 8, 11                                            Gool, and Anton Obukhov. Breathing new life into 3d assets
                                                                               with generative repainting. In BMVC. BMVA Press, 2023. 3
[39] Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch,
     Michael Rubinstein, and Kfir Aberman. DreamBooth: Fine               [53] Chenfeng Xu, Huan Ling, Sanja Fidler, and Or Litany. 3Diff-
     tuning text-to-image diffusion models for subject-driven gen-             Tection: 3d object detection with geometry-aware diffusion
     eration. In CVPR, pages 22500–22510, 2023. 3                              features. arXiv, 2023. 3
                                                                          [54] Guanglei Yang, Hao Tang, Mingli Ding, Nicu Sebe, and Elisa
[40] Chitwan Saharia, William Chan, Huiwen Chang, Chris Lee,
                                                                               Ricci. Transformer-based attention networks for continuous
     Jonathan Ho, Tim Salimans, David Fleet, and Mohammad
                                                                               pixel-wise prediction. In ICCV, 2021. 2
     Norouzi. Palette: Image-to-image diffusion models. In ACM
                                                                          [55] Hantao Yao, Rui Zhang, and Changsheng Xu. Visual-
     SIGGRAPH, pages 1–10, 2022. 3
                                                                               language prompt tuning with knowledge-guided context opti-
[41] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li,
                                                                               mization. In CVPR, pages 6757–6767, 2023. 3
     Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael
                                                                          [56] Wei Yin, Xinlong Wang, Chunhua Shen, Yifan Liu, Zhi Tian,
     Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Pho-
                                                                               Songcen Xu, Changming Sun, and Dou Renyin. Diversedepth:
     torealistic text-to-image diffusion models with deep language
                                                                               Affine-invariant depth prediction using diverse data. arXiv
     understanding. NeurIPS, 35, 2022. 2, 3
                                                                               preprint arXiv:2002.00569, 2020. 2, 6, 11, 12
[42] Tim Salimans and Jonathan Ho. Progressive distillation               [57] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus, Long
     for fast sampling of diffusion models. arXiv preprint                     Mai, Simon Chen, and Chunhua Shen. Learning to recover
     arXiv:2202.00512, 2022. 5                                                 3d scene shape from a single image. In CVPR, 2021. 2, 6, 11,
[43] Saurabh Saxena, Charles Herrmann, Junhwa Hur, Abhishek                    12
     Kar, Mohammad Norouzi, Deqing Sun, and David J. Fleet.               [58] Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu, Kaix-
     The surprising effectiveness of diffusion models for opti-                uan Wang, Xiaozhi Chen, and Chunhua Shen. Metric3D:
     cal flow and monocular depth estimation. arXiv preprint                   Towards zero-shot metric 3d prediction from a single image.
     arXiv:2306.01923, 2023. 2, 3                                              In ICCV, 2023. 2, 6
[44] Saurabh Saxena, Abhishek Kar, Mohammad Norouzi, and                  [59] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and
     David J Fleet. Monocular depth estimation using diffusion                 Ping Tan. NeWCRFs: Neural window fully-connected CRFs
     models. arXiv preprint arXiv:2302.14816, 2023. 2, 3                       for monocular depth estimation. In CVPR, 2022. 2
[45] Thomas Schops, Johannes L Schonberger, Silvano Galliani,             [60] Chi Zhang, Wei Yin, Billzb Wang, Gang Yu, Bin Fu, and
     Torsten Sattler, Konrad Schindler, Marc Pollefeys, and An-                Chunhua Shen. Hierarchical normalization for robust monoc-
     dreas Geiger. A multi-view stereo benchmark with high-                    ular depth estimation. NeurIPS, 35, 2022. 3, 6, 11
     resolution images and multi-camera videos. In CVPR, pages            [61] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding
     3260–3269, 2017. 6, 12, 26, 27, 32                                        conditional control to text-to-image diffusion models. In
[46] Christoph Schuhmann, Romain Beaumont, Richard Vencu,                      ICCV, pages 3836–3847, 2023. 3
     Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes,              [62] Renrui Zhang, Rongyao Fang, Wei Zhang, Peng Gao,
     Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al.                   Kunchang Li, Jifeng Dai, Yu Qiao, and Hongsheng Li.
     LAION-5B: An open large-scale dataset for training next                   Tip-adapter: Training-free CLIP-adapter for better vision-
     generation image-text models. NeurIPS, 35:25278–25294,                    language modeling. arXiv:2111.03930, 2021. 3
     2022. 3, 4                                                           [63] Renrui Zhang, Xiangfei Hu, Bohao Li, Siyuan Huang, Hanqiu
[47] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob                    Deng, Yu Qiao, Peng Gao, and Hongsheng Li. Prompt, gener-
     Fergus. Indoor segmentation and support inference from                    ate, then cache: Cascade of foundation models makes strong
     RGBD images. In ECCV, pages 746–760, 2012. 2                              few-shot learners. In CVPR, pages 15211–15222, 2023. 3

                                                                     10
[64] Wenliang Zhao, Yongming Rao, Zuyan Liu, Benlin Liu, Jie             into the metric 3D space using the camera intrinsics. We
     Zhou, and Jiwen Lu. Unleashing text-to-image diffusion              manually estimate the scale, shift, and intrinsics of “in-the-
     models for visual perception. arXiv:2303.02153, 2023. 3             wild” samples, where ground truth and camera intrinsics
[65] Chong Zhou, Chen Change Loy, and Bo Dai. Extract free               are unavailable. For some samples, camera intrinsics can
     dense labels from CLIP. In ECCV, pages 696–712, 2022. 3             also be extracted from the EXIF metadata. To visualize nor-
                                                                         mals, we perform least squares plane fitting at each position,
                                                                         considering a neighborhood area of 3 × 3 pixels around it.
Appendix                                                                 B. Experimental Results
In this supplementary material, we provide additional im-
                                                                         B.1. Stable Diffusion VAE with Depth
plementation details in Appendix A and present additional
quantitative and qualitative results in Appendix B and Ap-               To assess how well the pre-trained image variational autoen-
pendix C, respectively.                                                  coder of Stable Diffusion [38] works with depth maps, we
                                                                         tested it with 800 samples from the Hypersim [37] training
A. Implementation Details                                                set. To this end, each sample is normalized to the operational
                                                                         range of VAE as explained in the main paper, and replicated
A.1. Mixed Dataset Training                                              three times to accommodate the RGB interface. Upon de-
We train on two synthetic datasets, Hypersim [37] and Vir-               coding the latents, the reconstructed depth map is derived by
tual KITTI [7], whose images have different resolutions and              averaging the three RGB channels. Over the chosen set of
aspect ratios. For each batch, we probabilistically choose               depth maps, the Mean Absolute Error (MAE) of reconstruc-
the dataset and then draw samples from it. We ablate the                 tions is 0.0095 ± 0.0091, which is safely below the current
Bernoulli parameter of dataset sampling in Appendix B.4.                 state-of-the-art depth estimation errors.

A.2. Annealed Multi-Resolution Noise                                     B.2. Consistency of Channels After VAE Decoder
In the standard multi-resolution noise, multiple Gaussian                To further understand the suitability of the Stable Diffu-
noise images are sampled to form a pyramid of resolutions                sion latent space for depth representation, we evaluate the
and then subsequently combined by upsampling, weighted                   agreement of depth channels obtained from the VAE de-
averaging, and renormalization. The weight for the i-th                  coder during inference. We validate with the training split of
pyramid level is computed as si , where 0 < s < 1 is a                   NYUv2 [31] and a subsampled Eigen training split [14] of
strength of influence of lower-resolution noise. To bring                the KITTI dataset [17]. As shown in Tab. S1, the channel-
such noise closer to the Gaussian used in the original DDPM              wise discrepancy resulting from decoding depth from the
formulation, we propose to anneal the weight of levels i > 0             latent space is small relative to the value range of the decoder
based on the diffusion schedule. Specifically, we assign the i-          output, i.e., [−1, 1]. This could be related to the ability of
th level at timestep t the weight (st/T )i , where T is the total        VAE to represent gray-scale RGB images.
number of diffusion steps. Thus, a smaller weight is given to            Table S1. Consistency of channels after VAE decoder. The
lower-resolution levels at timesteps closer to the noise-free            reported numbers are averaged over the respective datasets.
end of the schedule. In addition to the ablation study in
the main paper, we further demonstrate the effectiveness of                                         std     max − min
annealing and other noise settings in Appendix B.3.
                                                                                          NYU      0.0027    0.0062
                                                                                          KITTI    0.0022    0.0052
A.3. Alignment with Ground Truth Depth
Following the established evaluation protocol [35], we use
least squares fitting over pixels with valid ground truth values         B.3. Prediction Variance and Training Noise
to compute the scale and shift factors of the affine-invariant           Since Marigold is a generative model, the predictions vary
predictions. Note that, while some methods predict affine-               depending on the initial noise starting the diffusion process.
invariant disparities [13, 35, 36], others (including ours)              We evaluate the consistency of predictions of three models,
predict affine-invariant depth values [56, 57, 60]. We ap-               trained differently, i.e., with Gaussian noise, multi-resolution
ply least squares fitting accordingly, i.e. the disparities are          noise, and annealed multi-resolution noise. We train with
aligned to the inverse ground truth depth.                               two synthetic datasets and validate with the training split of
                                                                         NYUv2 [31] and a subsampled Eigen training split [14] of
A.4. Visualization in 3D
                                                                         the KITTI dataset [17]. Specifically, we perform inference
We compute the scale and shift scalars between the predic-               10 times for each sample and compute pixel-wise statis-
tion and ground truth. Subsequently, we unproject pixels                 tics over the resulting depth predictions. Subsequently, we

                                                                    11
aggregate these statistics across entire datasets and report              Table S3. Ablation study of the training dataset mixing strategy.
them in Tab. S2. As seen from the values, training with                   Our method trained with only Hypersim delivers strong results.
the multi-resolution noises increases the prediction consis-              Outdoor performance is further enhanced with a small portion of
                                                                          Virtual KITTI. The zero-shot transfer is attained at 10% ratio.
tency at inference, and the annealed version brings further
improvement. Fig. S1 demonstrates predictions for a single
                                                                                                            Virtual            NYUv2                KITTI
sample with three models and varying starting noise.                                           Hypersim
                                                                                                            KITTI           AbsRel↓ δ1↑          AbsRel↓ δ1↑
                                                                                                100%          0%              5.7       96.3        13.7           82.5
Table S2. Pixel-wise consistency of depth predictions made by                                   95%            5%            5.8        96.2        11.1           88.8
models trained with three different noise types. The reported                                   90%           10%            5.6        96.5        11.3           88.7
numbers are averaged over entire datasets, wherein each sample                                  50%           50%            6.0        96.0        12.8           85.5
was processed 10 times, starting from a new noise sample.                                        0%          100%            13.9       83.4        15.4           79.3

 Multi-res.                       NYUv2                KITTI
              Annealed
  noise                     std    max − min    std      max − min        B.5. Inference Speed
    ✗            ✗        0.086      0.260     0.050       0.152
    ✓            ✗        0.037      0.117     0.030       0.094
                                                                          In Fig. S2, we report inference runtime, aligned with the
    ✓            ✓        0.033      0.106     0.025       0.079          settings from Figs. 6, 7. We acknowledge the slower speed vs.
                                                                          higher quality trade-off compared to feed-forward methods.
                                                                          Speed can be enhanced in future research, e.g. distillation
                                                                          for 2- or 4-step denoising schedules, and reducing prediction
                                                                          variance for smaller ensemble sizes.

                                                                                         8.0
                                                                          (sec/sample)

                                                                                         6.0

                                                                                         4.0
                                                                                                                                                                   RTX 4090
                                                                                         2.0                                                                       RTX 3090

                                                                                                1   2         5                10   1   2       4                         10
                                                                                                          # Ensemble size                      # Inference steps

Figure S1. Example of predictions on the same input by models             Figure S2. Inference speed on a single GPU with NYUv2 dataset.
trained with (top-down) Gaussian, multi-resolution, and annealed
multi-resolution noise. The last row exhibits the least variance.

                                                                          C. Qualitative Comparisons
B.4. Ratio of Mixed Training Datasets                                     C.1. In-the-Wild
                                                                          We present the gallery of “in-the-wild” images and corre-
To further investigate the impact of the synthetic datasets
                                                                          sponding predictions in Fig. S3. The input images are taken
used in our fine-tuning protocol, we ablate the mixing ratio
                                                                          in daily life or downloaded from the internet. Our method,
of the datasets, discussed in Appendix A.1. We train with
                                                                          Marigold, predicts accurate depth maps, exhibiting better
two synthetic datasets, Hypersim [37] and Virtual KITTI [7],
                                                                          overall layout and fine details. We show the final predictions
and validate with the training split of NYUv2 [31] and a sub-
                                                                          for each method, that is, depth for Marigold and LeReS, and
sampled Eigen training split [14] of the KITTI dataset [17].
                                                                          disparity for MiDaS.
As shown in Tab. S3, training with a mixture of these two
synthetic datasets yields better results on both indoor and               C.2. Test Datasets
outdoor real datasets, than training with a single synthetic
dataset. Interestingly, based on the higher-quality indoor                We show additional qualitative comparisons with our com-
dataset, Hypersim [37], adding a small portion (5%) of Vir-               petitors [13, 35, 36, 56, 57], on 5 test datasets [10, 17, 31,
tual KITTI [7], a street-view dataset, can already increase               45, 50]. The depth maps are visualized in Fig. S4, and the
the performance on the outdoor dataset. We find a sweet spot              normal maps can be found in Fig. S5. Marigold excels at
at around 10% where the performance is improved on both                   capturing fine scene details and reflecting the global scene
indoor and outdoor scenes. When the ratio of Virtual KITTI                layout.
keeps increasing, the overall performance is impaired. This
is likely caused by the varying scene diversity and rendering
quality of these two datasets.

                                                                     12
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           13
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           14
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           15
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           16
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           17
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           18
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           19
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           20
Input RGB Image   Marigold (ours, depth)        LeReS (depth)   MiDaS (disparity)

                                           21
         Input RGB Image               Marigold (ours, depth)               LeReS (depth)                 MiDaS (disparity)

Figure S3. Qualitative comparison on in-the-wild scenes. Marigold and LeReS predict depth (with red indicating closer and blue indicating
farther distances), while MiDaS predicts disparity (with yellow signifying closer and purple signifying farther distances).

                                                                   22
             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
NYUv2 [31]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 23
             Input RGB Image   DiverseDepth           MiDaS    LeReS
NYUv2 [31]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
KITTI [17]

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 24
             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
KITTI [17]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 25
             Input RGB Image   DiverseDepth           MiDaS    LeReS
KITTI [17]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
ETH3D [45]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 26
             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
ETH3D [45]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 27
               Input RGB Image   DiverseDepth           MiDaS    LeReS

                Ground Truth     Marigold (ours)        DPT     Omnidata

               Input RGB Image   DiverseDepth           MiDaS    LeReS
ScanNet [10]

                Ground Truth     Marigold (ours)        DPT     Omnidata

               Input RGB Image   DiverseDepth           MiDaS    LeReS

                Ground Truth     Marigold (ours)        DPT     Omnidata

                                                   28
               Input RGB Image   DiverseDepth           MiDaS    LeReS
ScanNet [10]

                Ground Truth     Marigold (ours)        DPT     Omnidata

               Input RGB Image   DiverseDepth           MiDaS    LeReS

                Ground Truth     Marigold (ours)        DPT     Omnidata

               Input RGB Image   DiverseDepth           MiDaS    LeReS
DIODE [50]

                Ground Truth     Marigold (ours)        DPT     Omnidata

                                                   29
               Input RGB Image                DiverseDepth                       MiDaS                           LeReS

                Ground Truth                 Marigold (ours)                      DPT                          Omnidata

               Input RGB Image                DiverseDepth                       MiDaS                           LeReS
  DIODE [50]

                Ground Truth                 Marigold (ours)                      DPT                          Omnidata

               Input RGB Image                DiverseDepth                       MiDaS                           LeReS

                Ground Truth                 Marigold (ours)                      DPT                          Omnidata

Figure S4. Qualitative comparison (depth) of monocular depth estimation methods across different datasets. Predictions are aligned to
ground truth. For every sample, the color coding is consistent across all depth maps.

                                                                 30
             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
NYUv2 [31]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 31
             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS
ETH3D [45]

              Ground Truth     Marigold (ours)        DPT     Omnidata

             Input RGB Image   DiverseDepth           MiDaS    LeReS

              Ground Truth     Marigold (ours)        DPT     Omnidata

                                                 32
                 Input RGB Image             DiverseDepth                       MiDaS                          LeReS
  ScanNet [10]

                  Ground Truth              Marigold (ours)                      DPT                          Omnidata

                 Input RGB Image             DiverseDepth                       MiDaS                          LeReS

                  Ground Truth              Marigold (ours)                      DPT                          Omnidata

                 Input RGB Image             DiverseDepth                       MiDaS                          LeReS
  DIODE [50]

                  Ground Truth              Marigold (ours)                      DPT                          Omnidata
Figure S5. Qualitative comparison (unprojected, colored as normals) of monocular depth estimation methods across different datasets.
Ground truth normals are derived from the ground truth depth maps.

                                                                33
