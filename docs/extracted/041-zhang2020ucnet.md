---
source_id: 041
bibtex_key: zhang2020ucnet
title: UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders
year: 2020
domain_theme: RGB-D SOD
verified_pdf: 41_UC-Net.pdf
char_count: 71995
---

UC-Net: Uncertainty Inspired RGB-D Saliency Detection
                                                                   via Conditional Variational Autoencoders

                                                                                                                          3
                                                           Jing Zhang1,4,5 Deng-Ping Fan2,6,∗ Yuchao Dai Saeed Anwar1,5
                                                                  Fatemeh Sadat Saleh1,4 Tong Zhang1 Nick Barnes1
                                          1
                                            Australian National University 2 CS, Nankai University 3 Northwestern Polytechnical University
                                              4
                                                ACRV 5 Data61 6 Inception Institute of Artificial Intelligence (IIAI), Abu Dhabi, UAE
arXiv:2004.05763v1 [cs.CV] 13 Apr 2020

                                                                   Abstract

                                            In this paper, we propose the first framework (UC-
                                         Net) to employ uncertainty for RGB-D saliency detection
                                         by learning from the data labeling process. Existing RGB-
                                         D saliency detection methods treat the saliency detection
                                         task as a point estimation problem, and produce a single            Image       Depth         GT        Ours (1)     Ours (2)
                                         saliency map following a deterministic learning pipeline.      Figure 1. Provided GT compared with UC-Net (ours) predicted
                                         Inspired by the saliency data labeling process, we propose     saliency maps. For images with a single salient object (1 st row),
                                         probabilistic RGB-D saliency detection network via condi-      we can produce consistent prediction. When multiple salient ob-
                                         tional variational autoencoders to model human annota-         jects exist (2nd row), we can produce diverse predictions.
                                         tion uncertainty and generate multiple saliency maps for
                                         each input image by sampling in the latent space. With the     saliency maps provided by the corresponding benchmark
                                         proposed saliency consensus process, we are able to gener-     datasets, where the GT saliency maps are obtained through
                                         ate an accurate saliency map based on these multiple pre-      human consensus or by the dataset creators [18]. Building
                                         dictions. Quantitative and qualitative evaluations on six      upon large scale RGB-D datasets, deep convolutional neural
                                         challenging benchmark datasets against 18 competing al-        network based models [21, 61, 6, 24] have made profound
                                         gorithms demonstrate the effectiveness of our approach in      progress in learning the mapping from an RGB-D image
                                         learning the distribution of saliency maps, leading to a new   pair to the corresponding GT saliency map. Considering the
                                         state-of-the-art in RGB-D saliency detection1 .                progress for RGB-D saliency detection under this pipeline,
                                                                                                        in this paper, we would like to argue that this pipeline fails
                                                                                                        to capture the uncertainty in labeling the GT saliency maps.
                                         1. Introduction                                                    According to research in human visual perception [33],
                                                                                                        visual saliency detection is subjective to some extent. Each
                                            Object-level visual saliency detection involves separat-    person could have specific preferences in labeling the
                                         ing the most conspicuous objects that attract humans from      saliency map (which has been previous discussed in user-
                                         the background [27, 2, 55, 63, 38, 29, 62]. Recently, vi-      specific saliency detection [26]). Existing approaches to
                                         sual saliency detection from RGB-D images have attracted       RGB-D saliency detection treat saliency detection as a point
                                         lots of interest due to the importance of depth information    estimation problem, and produce a single saliency map for
                                         in human vision system and the popularity of depth sensing     each input image pair following a deterministic learning
                                         technologies [61, 64]. Given a pair of RGB-D images, the       pipeline, which fails to capture the stochastic characteris-
                                         task of RGB-D saliency detection aims to predict a saliency    tic of saliency, and may lead to a partisan saliency model as
                                         map by exploring the complementary information between         shown in second row of Fig. 1. Instead of obtaining only
                                         color image and depth data.                                    a single saliency prediction (point estimation), we are in-
                                            The de-facto standard for RGB-D saliency detection is       terested in how the network produces multiple predictions
                                         to train a deep neural network using ground truth (GT)         (distribution estimation), which are then processed further
                                           ∗ Corresponding author: Deng-Ping Fan (dengpfan@gmail.com)
                                                                                                        to generate a single prediction in a similar way to how the
                                           1 Our code is publicly available at:   https://github.com/
                                                                                                        GT saliency maps are created.
                                         JingZhang617/UCNet.                                                In this paper, inspired by human perceptual uncertainty,
we propose a conditional variational autoencoders [50]                        fused the RGB and depth information through fully con-
(CVAE) based RGB-D saliency detection model UC-Net to                         nected layers. Chen et al. [7] used a multi-scale multi-path
produce multiple saliency predictions by modeling the dis-                    network for different modality information fusion. Chen et
tribution of output space as a generative model conditioned                   al. [5] proposed a complementary-aware RGB-D saliency
on the input RGB-D images to account for the human un-                        detection model by fusing features from the same stage of
certainty in annotation.                                                      each modality with a complementary-aware fusion block.
    However, there still exists one obstacle before we could                  Chen et al. [6] presented attention-aware cross-level com-
apply the probabilistic framework, that is existing RGB-                      bination blocks for multi-modality fusion. Zhao et al. [64]
D benchmark datasets generally only provide a single GT                       integrated a contrast prior to enhance depth cues, and em-
saliency map for each RGB-D image pair. To produce di-                        ployed a fluid pyramid integration framework to achieve
verse and accurate predictions2 , we resort to the “hide and                  multi-scale cross-modal feature fusion. To effectively incor-
seek” [49] principle following the orientation shifting the-                  porate geometric and semantic information within a recur-
ory [26] by iteratively hiding the salient foreground from                    rent learning framework, Li et al. [61] introduced a depth-
the RGB image for testing, which forces the deep network                      induced multi-scale RGB-D saliency detection network.
to learn the saliency map with diversity. Through this it-
erative hiding strategy, we obtain multiple saliency maps
                                                                              2.2. VAE or CVAE based Deep Probabilistic Models
for each input RGB-D image pair, which reflects the diver-                        Ever since the seminal work by Kingma et al. [31] and
sity/uncertainty from human labeling.                                         Rezende et al. [45], variational autoencoder (VAE) and its
    Moreover, depth data in the RGB-D saliency dataset can                    conditional counterpart CVAE [50] have been widely ap-
be noisy, and a direct fusion of RGB and depth informa-                       plied in various computer vision problems. To train a VAE,
tion may overwhelm the network to fit noise. To deal with                     a reconstruction loss and a regularizer are needed to penal-
the noisy depth problem, a depth correction network is pro-                   ize the disagreement of the prior and posterior distribution
posed as an auxiliary component to produce depth images                       of the latent representation. Instead of defining the prior dis-
with rich semantic and geometric information. We also in-                     tribution of the latent representation as a standard Gaussian
troduce a saliency consensus module to mimic the majority                     distribution, CVAE utilizes the input observation to modu-
voting mechanism for saliency GT generation.                                  late the prior on Gaussian latent variables to generate the
    Our main contributions are summarized as: 1) We pro-                      output. In low-level vision, VAE and CVAE have been ap-
pose a conditional probabilistic RGB-D saliency prediction                    plied to the tasks such as image background modeling [34],
model that can produce diverse saliency predictions instead                   latent representations with sharp samples [25], difference of
of a single saliency map; 2) We provide a mechanism via                       motion modes [57], medical image segmentation model [3],
saliency consensus to better model how saliency detection                     and modeling inherent ambiguities of an image [32]. Mean-
works; 3) We present a depth correction network to decrease                   while, VAE and CVAE have been explored in more complex
noise that is inherent in depth data; 4) Extensive experi-                    vision tasks such as uncertain future forecast [1, 53], hu-
mental results on six RGB-D saliency detection benchmark                      man motion prediction [47], and shape-guided image gen-
datasets demonstrate the effectiveness of our UC-Net.                         eration [12]. Recently, VAE algorithms have been extened
                                                                              to 3D domain targeting applications such as 3D meshes de-
2. Related Work                                                               formation [52], and point cloud instance segmentation [59].
                                                                                  To the best of our knowledge, CVAE has not been
2.1. RGB-D Saliency Detection                                                 exploited in saliency detection. Although Li et al. [34]
    Depend on how the complementary information between                       adopted VAE in their saliency prediction framework, they
RGB images and depth images is fused, existing RGB-D                          used VAE to model the image background, and separated
saliency detection models can be roughly classified into                      salient objects from the background through the reconstruc-
three categories: early-fusion models [43], late-fusion mod-                  tion residuals. In contrast, we use CVAE to model labeling
els [54, 24] and cross-level fusion models [61, 5, 7, 6, 64].                 variants, indicating human uncertainty of labeling. We are
Qu et al. [43] proposed an early-fusion model to generate                     the first to employ CVAE in saliency prediction network by
feature for each superpixel of the RGB-D pair, which was                      considering the human uncertainty in annotation.
then fed to a CNN to produce saliency of each superpixel.
Recently, Wang et al. [54] introduced a late-fusion network                   3. Our Model
(i.e. AFNet) to fuse predictions from the RGB and depth                           In this section, we present our probabilistic RGB-D
branch adaptively. In a similar pipeline, Han et al. [24]                     saliency detection model based on a conditional variational
   2 Diversity of prediction is related to the content of image. Image with   autoencoder, which learns the distribution of saliency maps
clear content may lead to consistent prediction (1st row in Fig. 1), while    rather than a single prediction. Let ξ = {Xi , Yi }N
                                                                                                                                 i=1 be the
complex image may produce diverse predictions (2nd row of Fig. 1).            training dataset, where Xi = {Ii , Di } denotes the RGB-D
                                                                                            KL Divergence

                                                                                               Feature
                                                                                              Expanding
                                                                                                                     Cross-entropy
                                                                                                                         Loss

                                                             Semantic Guided
                                                                           C                      C

                                                                  Loss
                                    C                                                           DepthCorrectionNet       C       Concatenation

                                                                                               PriorNet                              PosteriorNet

                                                                                                SaliencyNet                          PredictionNet

Figure 2. Network training pipeline. Four main modules are included, namely a LatentNet (PriorNet (µprior , σprior ) and PosteriorNet
(µpost , σpost )), a SaliencyNet, a DepthCorrectionNet and a PredictionNet. The LatentNet maps the RGB-D image pair X (or together
with GT Y for the PosteriorNet) to low dimensional Gaussian latent variable z. The DepthCorrectionNet refines the raw depth with a
semantic guided loss. The SaliencyNet takes the RGB image and the refined depth as input to generate a saliency feature map. The
PredictionNet takes both stochastic features and deterministic features to produce a final saliency map. We perform saliency consensus in
the testing stage, as shown in Fig. 3 to generate the final saliency map according to the mechanism of GT saliency map generation.

            PriorNet
                                   Sampling                                                conditioned on the input data X. There are three types of
                           …
      DepthCorrectionNet                                             Saliency   Saliency
                                                                                           variables in the conditional generative model: condition-
RGB-D         &                C         PredictionNet
 data    SaliencyNet                …                    …          Concensus     Map      ing variable X (RGB-D image pair in our setting), latent
                                                                                           variable z, and output variable Y . For the latent variable z
Figure 3. Overview of the proposed framework during testing. We                            drawn from the Gaussian distribution Pθ (z|X), the output
sample the PriorNet multiple times to generate diverse and accu-                           variable Y is generated from Pω (Y |X, z), then the poste-
rate predictions. The saliency consensus module is then used to                            rior of z is formulated as Qφ (z|X, Y ). The loss of CVAE is
obtain the majority voting of the final predictions.
                                                                                           defined as:
input (consisting of the RGB image Ii and the depth image                                          LCVAE = Ez∼Qφ (z|X,Y ) [− log Pω (Y |X, z)]
Di ), Yi denotes the ground truth saliency map. The whole                                                                                            (1)
pipeline of our model during training and testing are illus-                                                    +DKL (Qφ (z|X, Y )||Pθ (z|X)),
trated in Fig. 2 and Fig. 3, respectively.                                                 where Pω (Y |X, z) is the likelihood of P (Y ) given la-
    Our network is composed of five main modules: 1) La-                                   tent variable z and conditioning variable X, the Kullback-
tentNet (PriorNet and PosteriorNet) that maps the RGB-D                                    Leibler Divergence DKL (Qφ (z|X, Y )||Pθ (z|X)) works as
input Xi (for PriorNet) or Xi and Yi (for PosteriorNet) to                                 a regularization loss to reduce the gap between the prior
the low dimensional latent variables zi ∈ RK (K is dimen-                                  Pθ (z|X) and the auxiliary posterior Qφ (z|X, Y ). In this
sion of the latent space); 2) DepthCorrectionNet that takes                                way, CVAE aims to model the log likelihood P (Y ) un-
Ii and Di as input to generate a refined depth image Di0 ;                                 der encoding error DKL (Qφ (z|X, Y )||Pθ (z|X)). Follow-
3) SaliencyNet that maps the RGB image Ii and the refined                                  ing the standard practice in conventional CVAE [50], we
depth image Di0 to saliency feature maps Sid ; 4) Prediction-                              design a CVAE-based RGB-D saliency detection network,
Net that employs stochastic features Sis from LatentNet and                                and describe each component of our model in the following.
deterministic features Sid from SaliencyNet to produce our                                 LatentNet: We define Pθ (z|X) as PriorNet that maps the
saliency map prediction Pi ; 5) A saliency consensus module                                input RGB-D image pair X to a low-dimensional latent fea-
in the testing stage that mimics the mechanism of saliency                                 ture space, where θ is the parameter set of PriorNet. With
GT generation to evaluate the performance with the pro-                                    the same network structure and provided GT saliency map
vided single GT saliency map Yi . We will introduce each                                   Y , we define Qφ (z|X, Y ) as PosteriorNet, with φ being
module as follows.                                                                         the posterior net parameter set. In the LatentNet (Prior-
                                                                                           Net and PosteriorNet), we use five convolutional layers to
3.1. Probabilistic RGB-D Saliency Model via CVAE
                                                                                           map the input RGB-D image X (or concatenation of X
   The Conditional Variational Autoencoder (CVAE) mod-                                     and Y for the PosteriorNet) to the latent Gaussian variable
ulates the prior as a Gaussian distribution with parameters                                z ∼ N (µ, diag(σ 2 )), where µ, σ ∈ RK , representing the
                                                   c1_K          GAP
      c1_4K         c1_3K         c1_2K
                                                   c1_K          GAP

Figure 4. Detailed structure of LatentNet, where K is dimension
of the latent space, “c1 4K” represents a 1 × 1 convolutional layer
of output channel size 4K, “GAP” is global average pooling.

mean and standard deviation of the latent Gaussian variable,
as shown in Fig. 4.                                                               Figure 5. New label generation. The 1st row: we iteratively hide
    Let us define parameter set of PriorNet and PosteriorNet                      the predicted salient region, where no region is hidden in the first
as (µprior , σprior ) and (µpost , σpost ) respectively. The KL-                  image. The 2nd row: the corresponding GT of the hidden image.
Divergence in Eq. (1) is used to measure the distribution
mismatch between the prior net Pθ (z|X) and posterior net                                    S1          S2          S3          S4          S5

Qφ (z|X, Y ), or how much information is lost when using
                                                                                            daspp       daspp       daspp       daspp       daspp
Qφ (z|X, Y ) to represent Pθ (z|X). Typical using of CVAE
involves multiple versions of ground truth Y [32] to pro-                                                             C

duce informative z ∈ RK , with each position in z represents
possible labeling variants or factors that may cause diverse                                                        c1_M

saliency annotations. As we have only one version of GT,
                                                                                  Figure 6. SaliencyNet, where “S1” represents the first stage of the
directly training with the provided single GT may fail to                         VGG16 network, “daspp” is the DenseASPP module [58].
produce diverse predictions as the network will simply fit
the provided annotation Y .                                                       map with the receptive field of the whole image on each
Generate Multiple Predictions: To produce diverse and ac-                         stage of the VGG16 network. We then concatenate those
curate predictions, we propose an iterative hiding technique                      feature maps and feed it to another convolutional layer to
inspired by [49] following the orientation shifting theory                        obtain S d . The detail of the SaliencyNet is illustrated in
[26] to generate more annotations as shown in Fig. 5. We                          Fig. 6, where “c1 M” represents convolutional layer of ker-
iteratively hide the salient region in the RGB image with                         nel size 1 × 1, and M is channel size of S d .
mean of the training dataset. The RGB image and its cor-                          Feature Expanding: Statistics (z ∼ N (µ, diag(σ 2 )) in
responding GT are set as the starting point of the “new la-                       particular) from the LatentNet (PriorNet during testing as
bel generation” technique. We first hide the ground truth                         shown in Fig. 3 “Sampling”, or PosteriorNet during training
salient object in the RGB image, and feed the modified im-                        in Fig. 2) form the input to the Feature Expanding module.
age to an existing RGB saliency detection model [42] to                           Given a pair of (µk , σ k ) in each position of the K dimen-
produce a saliency map and treat it as one candidate anno-                        sional vector, we obtain latent vector z k = σ k  + µk ,
tation. We repeat salient object hiding technique three times                     where  ∈ N (0, I). To fuse with deterministic feature S d ,
for each training image3 to obtain four different sets of an-                     we expand z k to feature map of the same spatial size as S d
notations in total (including the provided GT), and we term                       by defining  as two-dimensional Gaussian noise map. With
this dataset as “AugedGT”, which is our training dataset.                         k = 1, ..., K, we can obtain a K (size of the latent space)
    During training, different annotations (as shown in Fig.                      channel stochastic feature S s representing labeling variants.
5) in Qφ (z|X, Y ) can force the PriorNet Pθ (z|X) to en-                         PredictionNet: The LatentNet produces stochastic features
code labeling variants of a given input X. As we have al-                         S s representing labeling variants, while the SaliencyNet
ready obtained diverse annotations with the proposed hiding                       outputs deterministic saliency features S d of input X. We
technique, we are expecting the network to produce diverse                        propose the PredictionNet, as shown in Fig. 2 to fuse fea-
predictions for images with complicated context. During                           tures from mentioned branches. A naive concatenation of
testing, we can obtain one stochastic feature S s (input of                       S s and S d may lead the network to learn only from the de-
the “PredictionNet”) of channel size K each time we sam-                          terministic features, thus fail to model labeling variants. In-
ple as shown in Fig. 3.                                                           spired by [47], we mix S s and S d channel-wise; thus, the
SaliencyNet: We design SaliencyNet to produce a deter-                            network cannot distinguish between features of the deter-
ministic saliency feature map S d from the input RGB-D                            ministic branch and the probabilistic branch. We concate-
data, where the refined depth data comes from the Depth-                          nate S d and S s to form a K + M channel feature map S sd .
CorrectionNet. We use VGG16 [48] as our encoder, and                              We define K + M dimensional variable r (a learnable pa-
remove layers after the fifth pooling layer. To enlarge the re-                   rameter) representing possible ranking of 1, 2, ..., K + M ,
ceptive field, we follow DenseASPP [58] to obtain feature                         and then S sd is mixed channel-wisely according to r to ob-
   3 We found that usually after three times of hiding, there exists no salient   tain the mixed feature S msd . Three 1 × 1 convolutional lay-
objects in the hidden image.                                                      ers with output channel sizes of K, K/2, 1, are included in
the PredictionNet to map S msd to a single channel saliency       version of saliency prediction P . To obtain C different pre-
map P . During testing, with multiple stochastic features S s ,   dictions P 1 , ..., P C , we sample PriorNet C times. We si-
we can obtain multiple predictions by sampling S s from the       multaneously feed these multiple predictions to the saliency
                             2
LatentNet N (µprior , diag(σprior )) multiple times.              consensus module to obtain the consensus of predictions.
                                                                      Given multiple predictions {P c }C              c
                                                                                                         c=1 , where P ∈ [0, 1],
3.2. DepthCorrectionNet                                                                          4           c
                                                                  we first compute the binary version Pb of the predictions
    Two main approaches are employed to acquire depth             by performing adaptive threshold [4] on P c . For each pixel
data for RGB-D saliency detection: through depth sensors          (u, v), we obtain a C dimensional feature vector Pu,v ∈
such as Microsoft Kinect, e.g., DES [8], and NLPR [41]            {0, 1}. We define Pbmjv ∈ {0, 1} as a one-channel saliency
datasets; or computing depth from stereo cameras, exam-           map representing majority voting of Pu,v . We define an in-
ples of such datasets are SSB [40] and NJU2K [28]. Re-            dicator 1c (u, v) = 1(Pbc (u, v) = Pbmjv (u, v)) representing
gardless of the capturing technique, noise is inherent in the     whether the binary prediction is consistent with the majority
depth data. We propose a semantic guided depth correc-            voting of the predictions. If Pbc (u, v) = Pbmjv (u, v), then
tion network to produce refined depth information as shown        1c (u, v) = 1. Otherwise, 1c (u, v) = 0. We obtain one gray
in Fig. 2, termed as “DepthCorrectionNet”. The encoder            saliency map after saliency consensus as:
part of the DepthCorrectionNet is the same as the “Salien-
cyNet”, while the decoder part is composed of four sequen-                          PC      c       C
                                                                                       c=1 1 (u, v)
                                                                                                    X
tial convolutional layers and bilinear upsampling operation.      Pgmjv (u, v) =                             (Pbc (u, v)} × 1c (u, v)).
                                                                                            C          c=1
    We assume that edges of the depth map should be aligned
                                                                                                                                    (4)
with edges of the RGB image. We adopt the boundary IOU
loss [39] as a regularizer for DepthCorrectionNet to achieve      3.4. Objective Function
a refined depth, which is guided by intensity of the RGB              At this stage, our loss function is composed of two parts
image. The full loss for DepthCorrectionNet is defined as:        i.e. LCVAE and LDepth . Furthermore, we propose to use
                  LDepth = Lsl + LIoub ,                   (2)    the smoothness loss [9] as a regularizer to achieve edge-
                                                                  aware saliency detection, based on the assumption of inter-
where Lsl is the smooth `1 loss between the refined depth         class distinction and intra-class similarity. Following [56],
D0 and the raw depth D, Lioub is the boundary IOU loss            we define first-order derivatives of the saliency map in the
between the refined depth D0 and intensity Ig of the RGB          smoothness term as
image I. Given the predicted depth map D0 and intensity
                                                                                  X X
of RGB image Ig, we follow [39] to compute the first-order            LSmooth =                Ψ(|∂d Pu,v |e−α|∂d Ig(u,v)| ), (5)
derivatives of D0 and Ig. Subsequently, we calculate the                            u,v d∈→
                                                                                          −
                                                                                          x ,→
                                                                                             −
                                                                                             y
magnitude gD0 and gI of the gradients of D0 and Ig, and                                              √
define the boundary IOU loss as:                                  where Ψ is defined as Ψ(s) = s2 + 1e−6 , Pu,v is the
                                                                  predicted saliency map at position (u, v), and Ig(u, v) is
                LIoub = 1 − 2
                                 |gD0 ∩ gI|
                                              .            (3)    the image intensity, d indexes over partial derivative on →
                                                                                                                            −
                                                                                                                            x
                                |gD0 | + |gI|                          →
                                                                       −
                                                                  and y directions. We set α = 10 following [56].
3.3. Saliency Consensus Module                                       Both the smoothness loss (Eq. (5)) and the boundary
                                                                  IOU loss (Eq. (3)) need intensity Ig. We convert the RGB
    Saliency detection is subjective to some extent, and it is    image I to a gray-scale intensity image Ig as [60]:
common to have multiple annotators to label one image, and
the final ground truth saliency map is obtained through ma-         Ig = 0.2126 × I lr + 0.7152 × I lg + 0.0722 × I lb , (6)
jority voting strategy [18]. Although it is well known in the
saliency detection community about how the ground truth           where I lr , I lg and I lb represent the color components in
is acquired; yet, there exists no research on embedding this      the linear color space after Gamma function been removed
mechanism into deep saliency frameworks. Current mod-             from the original color space. I lr is achieved via:
els define saliency detection as a point estimation problem                        
                                                                                              Ir
instead of a distribution estimation problem. We, instead,
                                                                                   
                                                                                                  ,           I r ≤ 0.04045,
                                                                                            12.92
use CVAE to obtain the saliency distribution. Next, we em-                  I lr =  r        2.4                                  (7)
                                                                                    I + 0.055
                                                                                                               I r > 0.04045.
                                                                                  
bed saliency consensus into our probabilistic framework to
                                                                                  
                                                                                                  ,
                                                                                       1.055
compute the majority voting of different predictions in the
testing stage as shown in Fig. 3.                                 where I r is the original red channel of image I, and we
    During testing, we sample PriorNet with fixed µprior and      compute I g and I b in the same way as Eq. (7).
σprior to obtain a stochastic feature S s . With each S s and        4 As the GT map Y ∈ {0, 1}, we produce series of binary predictions

deterministic feature S d from SaliencyNet, we obtain one         with each one representing annotation from one saliency annotator.
  With smoothness loss LSmooth , depth loss LDepth and        and MC-dropout respectively. Results in Fig. 8 show that
CVAE loss LCVAE , our final loss function is defined as:      our method can not only produce high accuracy predictions
                                                              (compared with DMRA [61]), but also diverse predictions
        Lsal = LCVAE + λ1 LDepth + λ2 LSmooth .         (8)   (compared with M-head based and MC-dropout based mod-
In our experiments, we set λ1 = λ2 = 0.3.                     els) for images with complex background (image in the first
Training details: We set channel size of S d as M = 32,       and last rows).
and scale of latent space as K = 8. We trained our
                                                              4.3. Ablation Study
model using Pytorch, and initialized the encoder of Salien-
cyNet and DepthCorrectionNet with VGG16 parameters                We carried out eight experiments (shown in Table 2)
pre-trained on ImageNet. Weights of new layers were ini-      to thoroughly analyse our framework, including network
tialized with N (0, 0.01), and bias was set as constant. We   structure (“M1”, “M2”, “M3”), probabilistic model selec-
used the Adam method with momentum 0.9 and decreased          tion (“M4”, “M5”, “M6”), data source selection (“M7”) and
the learning rate 10% after each epoch. The base learning     effectiveness of the new label generation technique (“M8”).
rate was initialized as 1e-4. The whole training took 13      We make the number bold when it’s better than ours.
hours with training batch size 6 and maximum epoch 30 on      Scale of Latent Space: We investigate the influence of the
a PC with an NVIDIA GeForce RTX GPU. For input image          scale of the Gaussian latent space K in our network. In this
size 352 × 352, the inference time is 0.06s on average.       paper, after parameter tuning, we find K = 8 works best.
                                                              We show performance with K = 32 as “M1”. Performance
4. Experimental Results                                       of “M1” is worse than our reported results, which indicates
                                                              that scale of the latent space is an important parameter in
4.1. Setup
                                                              our framework. We further carried out more experiments
Datasets: We perform experiments on six datasets includ-      with K ∈ [2, 12], and found relative stable predictions with
ing five widely used RGB-D saliency detection datasets        K ∈ [6, 10].
(namely NJU2K [28], NLPR [41], SSB [40], LFSD [35],           Effect of DepthCorrectionNet: To illustrate the effective-
DES [8]) and one newly released dataset (SIP [18]).           ness of the proposed DepthCorrectionNet, we remove this
Competing Methods: We compare our method with 18 al-          branch and feed the concatenation of the RGB image and
gorithms, including ten handcrafted conventional methods      depth data to the SaliencyNet, shown as “M2”, which is
and eight deep RGB-D saliency detection models.               worse than our method. On DES [8] dataset, we observe
Evaluation Metrics: Four evaluation metrics are used, in-     the proposed solution achieves around 4% improvement on
cluding two widely used: 1) Mean Absolute Error (MAE          S-measure, E-measure and F-measure, which demonstrates
M); 2) mean F-measure (Fβ ) and two recently proposed:        the effectiveness of the depth correction net.
3) Enhanced alignment measure (mean E-measure, Eξ ) [15]      Saliency Consencus Module: To mimic the saliency label-
and 4) Structure measure (S-measure, Sα ) [14].               ing process, we embed a saliency consensus module during
                                                              test in our framework (as shown in Fig. 3) to obtain the ma-
4.2. Performance Comparison                                   jority voting of the multiple predictions. We remove it from
Quantitative Comparison: We report performance of our         our framework and test the network performance by random
method and competing methods in Table 1. It shows that our    sample from the latent PriorNet Pθ (z|X), and performance
method consistently achieves the best performance on all      is shown in “M3”, which is the best compared with compet-
datasets, especially on SSB [40] and SIP [18], our method     ing methods. While, with the saliency consensus module
achieves significant S-measure, E-measure, and F-measure      embedded, we achieve even better performance, which il-
performance boost and a decrease in MAE by a large mar-       lustrates effectiveness of the saliency consencus module.
gin. We show E-measure and F-measure curves of compet-        VAE vs. CVAE: We use CVAE to model labeling variants,
ing methods and ours in Fig. 7. We observe that our method    and a PosteriorNet is used to estimate parameters for the
produces not only stable E-measure and F-measure but also     PriorNet. To test how our model performs with prior of z
best performance.                                             as a standard normal distribution, and the posterior of z as
Qualitative Comparisons: In Fig. 8, we show five im-          Pθ (z|X). VAE performance is shown as “M4”, which is
ages comparing results of our method with one newly re-       comparable with SOTA RGB-D models. With the CVAE
leased RGB-D saliency detection method (DMRA [61]),           [50] based model proposed, we further boost performance
and two widely used methods to produce structured outputs,    of “M4”, which proves effectiveness of the our solution.
namely M-head [46] and MC-dropout [30] (we will discuss       Multi-head vs. CVAE: Multi-head models [46] generate
these two methods in detail in the ablation study section).   multiple predictions with different decoders and a shared
We design both M-head and MC-dropout based structured         encoder, and the loss function is always defined as the clos-
saliency detection models by replacing CVAE with M-head       est of the multiple predictions. We remove the LatentNet,
Table 1. Benchmarking results of ten leading handcrafted feature-based models and eight deep models on six RGBD saliency datasets.
↑ & ↓ denote larger and smaller is better, respectively. Here, we adopt mean Fβ and mean Eξ [15].
                                              Handcrafted Feature based Models                          Deep Models
                      Metric LHM    CDB DESM GP CDCP ACSD LBE DCMC MDSF SE DF AFNet CTMF MMCI PCF TANet CPFP DMRA UC-Net
                             [41]   [36]  [8]   [44] [66]      [28] [20] [10]  [51] [22] [43] [54] [24]  [7]  [5]   [6] [64] [61] Ours
                      Sα ↑ .514     .632 .665 .527 .669        .699 .695 .686  .748 .664 .763 .822 .849 .858 .877 .879 .878  .886 .897
                      Fβ ↑ .328     .498 .550 .357 .595        .512 .606 .556  .628 .583 .653 .827 .779 .793 .840 .841 .850  .873 .886
  NJU2K [28]
                      Eξ ↑ .447     .572 .590 .466 .706        .594 .655 .619  .677 .624 .700 .867 .846 .851 .895 .895 .910  .920 .930
                      M ↓ .205      .199 .283 .211 .180        .202 .153 .172  .157 .169 .140 .077 .085 .079 .059 .061 .053  .051 .043
                      Sα ↑ .562     .615 .642 .588 .713        .692 .660 .731  .728 .708 .757 .825 .848 .873 .875 .871 .879  .835 .903
                      Fβ ↑ .378     .489 .519 .405 .638        .478 .501 .590  .527 .611 .617 .806 .758 .813 .818 .828 .841  .837 .884
           SSB [40]
                      Eξ ↑ .484     .561 .579 .508 .751        .592 .601 .655  .614 .664 .692 .872 .841 .873 .887 .893 .911  .879 .938
                      M ↓ .172      .166 .295 .182 .149        .200 .250 .148  .176 .143 .141 .075 .086 .068 .064 .060 .051  .066 .039
                      Sα ↑ .578     .645 .622 .636 .709        .728 .703 .707  .741 .741 .752 .770 .863 .848 .842 .858 .872  .900 .934
                      Fβ ↑ .345     .502 .483 .412 .585        .513 .576 .542  .523 .618 .604 .713 .756 .735 .765 .790 .824  .873 .919
            DES [8]
                      Eξ ↑ .477     .572 .566 .503 .748        .613 .650 .631  .621 .706 .684 .809 .826 .825 .838 .863 .888  .933 .967
                      M ↓ .114      .100 .299 .168 .115        .169 .208 .111  .122 .090 .093 .068 .055 .065 .049 .046 .038  .030 .019
                      Sα ↑ .630     .632 .572 .655 .727        .673 .762 .724  .805 .756 .806 .799 .860 .856 .874 .886 .888  .899 .920
                      Fβ ↑ .427     .421 .430 .451 .609        .429 .636 .542  .649 .624 .664 .755 .740 .737 .802 .819 .840  .865 .891
      NLPR [41]
                      Eξ ↑ .560     .567 .542 .571 .782        .579 .719 .684  .745 .742 .757 .851 .840 .841 .887 .902 .918  .940 .951
                      M ↓ .108      .108 .312 .146 .112        .179 .081 .117  .095 .091 .079 .058 .056 .059 .044 .041 .036  .031 .025
                      Sα ↑ .557     .520 .722 .640 .717        .734 .736 .753  .700 .698 .791 .738 .796 .787 .794 .801 .828  .847 .864
                      Fβ ↑ .396     .376 .612 .519 .680        .566 .612 .655  .521 .640 .679 .736 .756 .722 .761 .771 .811  .845 .855
          LFSD [35]
                      Eξ ↑ .491     .465 .638 .584 .754        .625 .670 .682  .588 .653 .725 .796 .810 .775 .818 .821 .863  .893 .901
                      M ↓ .211      .218 .248 .183 .167        .188 .208 .155  .190 .167 .138 .134 .119 .132 .112 .111 .088  .075 .066
                      Sα ↑ .511     .557 .616 .588 .595        .732 .727 .683  .717 .628 .653 .720 .716 .833 .842 .835 .850  .806 .875
                      Fβ ↑ .287     .341 .496 .411 .482        .542 .572 .500  .568 .515 .465 .702 .608 .771 .814 .803 .821  .811 .867
           SIP [18]
                      Eξ ↑ .437     .455 .564 .511 .683        .614 .651 .598  .645 .592 .565 .793 .704 .845 .878 .870 .893  .844 .914
                      M ↓ .184      .192 .298 .173 .224        .172 .200 .186  .167 .164 .185 .118 .139 .086 .071 .075 .064  .085 .051

 1                                               1                                 1                                         1

0.8                                          0.8                                  0.8                                       0.8

                                                                                  0.6
0.6                                          0.6                                                                            0.6

                                                                                  0.4
0.4                                          0.4                                                                            0.4

                                                                                  0.2
0.2
                              NJU2K
                                             0.2
                                                                   SSB                                        DES
                                                                                                                            0.2
                                                                                                                                            NLPR
                                                                                   0
      0               100                  256       0    100               256         0            100              256         0   100           256

                                                                                   1                                         1
0.8                                          0.8

                                                                                  0.8                                       0.8

0.6                                          0.6
                                                                                  0.6                                       0.6

0.4                                          0.4
                                                                                  0.4                                       0.4

0.2                                          0.2
                                                                                  0.2                                       0.2

                                NJU2K                                 SSB                                       DES                          NLPR
 0                                               0                                 0                                         0
      0               100                  256       0    100               256         0            100              256         0   100           256

                                    Figure 7. E-measure (1st row) and F-measure (2nd row) curves on four testing datasets.

and copy the decoder of the SaliencyNet multiple times                                      SaliencyNet in the testing stage. We repeats five times of
to achieve multiple predictions (“M5” in this paper). We                                    random dropout (dropout ratio = 0.1), and report the mean
report performance in “M5” as mean of the multiple pre-                                     performance as “M6”. Similar to “M5”, “M6” also achieves
dictions. “M5” is better than SOTA models (e.g., DMRA)                                      the best performance comparing with SOTA models (e.g.,
while there still exists gap between M-head based method                                    CPFP and DMRA), while the proposed CVAE based model
(“M5”) and our CVAE based model (UC-Net).                                                   achieves even better performance.
Monte-Carlo Dropout vs. CVAE: Monte-Carlo Dropout                                           HHA vs. Depth: HHA [23] is a widely used technique that
[30] uses dropout during the testing stage to introduce                                     encodes the depth data to three channels: horizontal dis-
stochastic to the network. We follow [30] to remove the La-                                 parity, height above ground, and the angle the pixels local
tentNet, and use dropout in the encoder and decoder of the                                  surface normal makes with the inferred gravity direction.
                Image             Depth        GT        DMRA          MH1          MH2         DP1         DP2      Ours (1)    Ours (2)    UC-Net
Figure 8. Comparisons of saliency maps. “MH1” and “MH2” are two predictions from M-head. “DP1” and “DP2” are predictions of
two random MC-dropout during test. “Ours(1)” and “Ours(2)” are two predictions sampled from our CVAE based model. Different from
M-head and MC-dropout, which produce consistent predictions for ambiguous images (5th row), UC-Net can produce diverse predictions.
                        Table 2. Ablation study on RGB-D saliency datasets.               ing dataset and augmented training data respectively. We
                       Metric UC-Net M1 M2 M3 M4 M5 M6 M7 M8 M9
                                                                                          observe performance improvement of “M9” compared with
 SSB [40] NJU2K [28]

                       Sα ↑    .897  .866 .893 .905 .871 .885 .881 .893 .838 .866
                       Fβ ↑    .886  .858 .887 .884 .851 .878 .878 .884 .787 .812         “M8”, which indicates effectiveness of the new label gener-
                       Eξ ↑    .930  .905 .930 .927 .910 .923 .927 .932 .840 .866
                                                                                          ation technique.
                       M↓      .043  .060 .046 .045 .059 .047 .046 .044 .084 .075
                       Sα ↑    .903  .854 .893 .900 .867 .891 .893 .898 .855 .872
                       Fβ ↑    .884  .831 .876 .868 .834 .864 .876 .882 .793 .805
                       Eξ ↑    .938  .894 .911 .922 .907 .921 .931 .934 .854 .870
                                                                                          5. Conclusion
                       M↓      .039  .060 .043 .047 .057 .047 .043 .040 .073 .068             Inspired by human uncertainty in ground truth (GT) an-
                       Sα ↑    .934  .876 .896 .928 .897 .911 .896 .918 .811 .911
                                                                                          notation, we proposed the first uncertainty network named
 DES [8]

                       Fβ ↑    .919  .844 .868 .902 .867 .897 .868 .904 .724 .843
                       Eξ ↑    .967  .906 .928 .947 .930 .945 .928 .953 .794 .910         UC-Net for RGB-D saliency detection based on a con-
                       M↓      .019  .035 .026 .024 .033 .024 .026 .023 .065 .036         ditional variational autoencoder. Different from existing
                       Sα ↑
 LFSD [35] NLPR [41]

                               .920  .878 .919 .918 .890 .899 .910 .915 .850 .883
                       Fβ ↑    .891  .846 .897 .878 .845 .875 .867 .889 .759 .795
                                                                                          methods, which generally treat saliency detection as a point
                       Eξ ↑    .951  .911 .953 .941 .924 .937 .933 .951 .841 .883         estimation problem, we propose to learn the distribution
                       M↓      .025  .039 .024 .029 .037 .029 .028 .025 .057 .045         of saliency maps. Under our formulation, our model is
                       Sα ↑    .864  .799 .847 .862 .820 .838 .847 .853 .729 .823
                       Fβ ↑    .855  .791 .838 .841 .802 .833 .838 .848 .661 .779
                                                                                          able to generate multiple labels which have been discarded
                       Eξ ↑    .901  .829 .879 .885 .865 .875 .879 .891 .720 .818         in the GT annotation generation process through saliency
                       M↓      .066  .101 .079 .075 .093 .079 .079 .073 .145 .108         consensus. Quantitative and qualitative evaluations on six
                       Sα ↑    .875  .846 .867 .870 .851 .859 .867 .865 .810 .845
                                                                                          standard and challenging benchmark datasets demonstrated
 SIP [18]

                       Fβ ↑    .867  .837 .860 .848 .821 .853 .860 .855 .751 .795
                       Eξ ↑    .914  .884 .908 .901 .893 .905 .908 .908 .816 .852         the superiority of our approach in learning the distribution
                       M↓      .051  .068 .056 .059 .067 .057 .056 .056 .094 .079         of saliency maps. In the future, we would like to extend
                                                                                          our approach to other saliency detection problems (e.g.,
HHA is widely used in RGB-D related dense prediction                                      VSOD [19], RGB SOD [13, 65], Co-SOD [17]). Further-
models [11, 24] to obtain better feature representation. To                               more, we plan to capture new datasets with multiple human
test if HHA also works in our scenario, we replace depth                                  annotations to further model the statistics of human uncer-
with HHA, and performance is shown in “M7”. We observe                                    tainty in interactive image segmentation [37], camouflaged
similar performance achieved with HHA instead of the raw                                  object detection [16], etc.
depth data.
                                                                                          Acknowledgments. This research was supported in part
New Label Generation: To produce diverse predictions,
                                                                                          by Natural Science Foundation of China grants (61871325,
we follow [49] and generate diverse annotations for the                                   61420106007, 61671387), the Australia Research Council Centre
training dataset. To illustrate the effectiveness of this strat-                          of Excellence for Robotics Vision (CE140100016), and the Na-
egy, we train with only the SaliencyNet to produce single                                 tional Key Research and Development Program of China under
channel saliency map with RGB-D image as input for sim-                                   Grant 2018AAA0102803. We thank all reviewers and Area Chairs
plicity. “M8” and “M9” represent using the provided train-                                for their constructive comments.
References                                                          [17] Deng-Ping Fan, Zheng Lin, Ge-Peng Ji, Dingwen Zhang,
                                                                         Huazhu Fu, and Ming-Ming Cheng. Taking a Deeper Look
 [1] Abubakar Abid and James Y. Zou. Contrastive Vari-                   at the Co-salient Object Detection. In IEEE CVPR, 2020.
     ational Autoencoder Enhances Salient Features. CoRR,
                                                                    [18] Deng-Ping Fan, Zheng Lin, Zhao Zhang, Menglong Zhu, and
     abs/1902.04601, 2019.
                                                                         Ming-Ming Cheng. Rethinking RGB-D salient object detec-
 [2] Radhakrishna Achanta, Sheila Hemami, Francisco Estrada,             tion: Models, datasets, and large-scale benchmarks. IEEE
     and Sabine Susstrunk. Frequency-tuned salient region detec-         TNNLS, 2020.
     tion. In IEEE CVPR, pages 1597–1604, 2009.
                                                                    [19] Deng-Ping Fan, Wenguan Wang, Ming-Ming Cheng, and
 [3] Christian F. Baumgartner, Kerem Can Tezcan, Krishna Chai-
                                                                         Jianbing Shen. Shifting more attention to video salient object
     tanya, Andreas M. Hötker, Urs J. Muehlematter, Khoschy
                                                                         detection. In IEEE CVPR, pages 8554–8564, 2019.
     Schawkat, Anton S. Becker, Olivio Donati, and Ender
                                                                    [20] David Feng, Nick Barnes, Shaodi You, and Chris McCarthy.
     Konukoglu. PHiSeg: Capturing Uncertainty in Medical Im-
                                                                         Local background enclosure for RGB-D salient object detec-
     age Segmentation. In MICCAI, pages 119–127, 2019.
                                                                         tion. In IEEE CVPR, pages 2343–2350, 2016.
 [4] Ali Borji, Ming-Ming Cheng, Huaizu Jiang, and Jia Li.
                                                                    [21] Keren Fu Fu, Deng-Ping Fan, Ge-Peng Ji, and Qijun Zhao.
     Salient Object Detection: A Benchmark.            IEEE TIP,
                                                                         JL-DCF: Joint Learning and Densely-Cooperative Fusion
     24(12):5706–5722, 2015.
                                                                         Framework for RGB-D Salient Object Detection. In IEEE
 [5] Hao Chen and Youfu Li. Progressively complementarity-
                                                                         CVPR, 2020.
     aware fusion network for RGB-D Salient Object Detection.
     In IEEE CVPR, pages 3051–3060, 2018.                           [22] Jingfan Guo, Tongwei Ren, and Jia Bei. Salient object detec-
                                                                         tion for rgb-d image via saliency evolution. In ICME, pages
 [6] Hao Chen and Youfu Li. Three-stream Attention-aware Net-
                                                                         1–6, 2016.
     work for RGB-D Salient Object Detection. IEEE TIP, pages
     2825–2835, 2019.                                               [23] Saurabh Gupta, Ross Girshick, Pablo Arbeláez, and Jitendra
                                                                         Malik. Learning rich features from RGB-D images for object
 [7] Hao Chen, Youfu Li, and Dan Su. Multi-modal fusion net-
                                                                         detection and segmentation. In ECCV, pages 345–360, 2014.
     work with multi-scale multi-path and cross-modal interac-
     tions for RGB-D salient object detection. PR, 86:376–385,      [24] Junwei Han, Hao Chen, Nian Liu, Chenggang Yan, and Xue-
     2019.                                                               long Li. CNNs-based RGB-D saliency detection via cross-
 [8] Yupeng Cheng, Huazhu Fu, Xingxing Wei, Jiangjian Xiao,              view transfer and multiview fusion. IEEE TCYB, pages
     and Xiaochun Cao. Depth enhanced saliency detection                 3171–3183, 2018.
     method. In ACM ICIMCS, pages 23–27, 2014.                      [25] Faruk Ahmed Adrien Ali Taga Francesco Visin David
 [9] Gabriel J. Brostow Clment Godard, Oisin Mac Aodha. Unsu-            Vzquez Aaron C. Courville Ishaan Gulrajani, Kundan Ku-
     pervised Monocular Depth Estimation with Left-Right Con-            mar. PixelVAE: A Latent Variable Model for Natural Images.
     sistency. In IEEE CVPR, pages 6602–6611, 2017.                      In ICLR, 2016.
[10] Runmin Cong, Jianjun Lei, Changqing Zhang, Qingming            [26] Laurent Itti and Christof Koch. A saliency-based search
     Huang, Xiaochun Cao, and Chunping Hou. Saliency detec-              mechanism for overt and covert shifts of visual attention. VR,
     tion for stereoscopic images based on depth confidence anal-        40(10):1489 – 1506, 2000.
     ysis and multiple cues fusion. IEEE SPL, 23(6):819–823,        [27] Laurent Itti, Christof Koch, and Ernst Niebur. A model
     2016.                                                               of saliency-based visual attention for rapid scene analysis.
[11] Dapeng Du, Limin Wang, Huiling Wang, Kai Zhao, and                  IEEE TPAMI, 20(11):1254–1259, 1998.
     Gangshan Wu. Translate-to-Recognize Networks for RGB-          [28] Ran Ju, Ling Ge, Wenjing Geng, Tongwei Ren, and Gang-
     D Scene Recognition. In IEEE CVPR, pages 11836–11845,               shan Wu. Depth saliency based on anisotropic center-
     2019.                                                               surround difference. In ICIP, pages 1115–1119, 2014.
[12] Patrick Esser, Ekaterina Sutter, and Bjrn Ommer. A Varia-      [29] Shuhui Wang Jun Wei and Qingming Huang. F3Net: Fusion,
     tional U-Net for Conditional Appearance and Shape Gener-            Feedback and Focus for Salient Object Detection. In AAAI,
     ation. In IEEE CVPR, pages 8857–8865, 2018.                         2020.
[13] Deng-Ping Fan, Ming-Ming Cheng, Jiang-Jiang Liu, Shang-        [30] Alex Kendall, Vijay Badrinarayanan, , and Roberto Cipolla.
     Hua Gao, Qibin Hou, and Ali Borji. Salient objects in clut-         Bayesian SegNet: Model Uncertainty in Deep Convolutional
     ter: Bringing salient object detection to the foreground. In        Encoder-Decoder Architectures for Scene Understanding. In
     ECCV, pages 186–202, 2018.                                          BMVC, 2017.
[14] Deng-Ping Fan, Ming-Ming Cheng, Yun Liu, Tao Li, and Ali       [31] Diederik P Kingma and Max Welling. Auto-Encoding Vari-
     Borji. Structure-measure: A new way to evaluate foreground          ational Bayes. In ICLR, 2013.
     maps. In IEEE ICCV, pages 4548–4557, 2017.                     [32] Simon Kohl, Bernardino Romera-Paredes, Clemens Meyer,
[15] Deng-Ping Fan, Cheng Gong, Yang Cao, Bo Ren, Ming-                  Jeffrey De Fauw, Joseph R. Ledsam, Klaus Maier-Hein,
     Ming Cheng, and Ali Borji. Enhanced-alignment Measure               S. M. Ali Eslami, Danilo Jimenez Rezende, and Olaf Ron-
     for Binary Foreground Map Evaluation. In IJCAI, pages               neberger. A Probabilistic U-Net for Segmentation of Am-
     698–704, 2018.                                                      biguous Images. In NeurIPS, pages 6965–6975, 2018.
[16] Deng-Ping Fan, Ge-Peng Ji, Guolei Sun, Ming-Ming Cheng,        [33] Olivier Le Meur and Thierry Baccino. Methods for compar-
     Jianbing Shen, and Ling Shao. Camouflaged Object Detec-             ing scanpaths and saliency maps: strengths and weaknesses.
     tion. In IEEE CVPR, 2020.                                           Behavior Research Methods, 45(1):251–266, 2013.
[34] Bo Li, Zhengxing Sun, and Yuqi Guo. SuperVAE: Superpix-        [51] Hangke Song, Zhi Liu, Huan Du, Guangling Sun, Olivier
     elwise Variational Autoencoder for Salient Object Detection.        Le Meur, and Tongwei Ren. Depth-aware salient ob-
     In AAAI, pages 8569–8576, 2019.                                     ject detection and segmentation via multiscale discrimina-
[35] Nianyi Li, Jinwei Ye, Yu Ji, Haibin Ling, and Jingyi Yu.            tive saliency fusion and bootstrap learning. IEEE TIP,
     Saliency detection on light field. In IEEE CVPR, pages              26(9):4204–4216, 2017.
     2806–2813, 2014.                                               [52] Qingyang Tan, Lin Gao, Yu-Kun Lai, and Shihong Xia. Vari-
[36] Fangfang Liang, Lijuan Duan, Wei Ma, Yuanhua Qiao, Zhi              ational Autoencoders for Deforming 3D Mesh Models. In
     Cai, and Laiyun Qing. Stereoscopic saliency model using             IEEE CVPR, 2018.
     contrast and depth-guided-background prior. Neurocomput-       [53] Jacob Walker, Carl Doersch, Harikrishna Mulam, and Mar-
     ing, 275:2227–2238, 2018.                                           tial Hebert. An Uncertain Future: Forecasting from Static
[37] Zheng Lin, Zhao Zhang, Lin-Zhuo Chen, Ming-Ming                     Images Using Variational Autoencoders. In ECCVW, pages
     Cheng, and Shao-Ping Lu. Interactive Image Segmentation             835–851, 2016.
     with First Click Attention. In IEEE CVPR, 2020.                [54] Ningning Wang and Xiaojin Gong. Adaptive Fusion for
[38] Yi Liu, Qiang Zhang, Dingwen Zhang, and Jungong Han.                RGB-D Salient Object Detection. IEEE Access, 7:55277–
     Employing Deep Part-Object Relationships for Salient Ob-            55284, 2019.
     ject Detection. In IEEE ICCV, 2019.                            [55] Wenguan Wang, Jianbing Shen, Ming-Ming Cheng, and
[39] Zhiming Luo, Akshaya Mishra, Andrew Achkar, Justin                  Ling Shao. An Iterative and Cooperative Top-Down and
     Eichel, Shaozi Li, and Pierre-Marc Jodoin. Non-Local Deep           Bottom-Up Inference Network for Salient Object Detection.
     Features for Salient Object Detection. In IEEE CVPR, 2017.          In IEEE CVPR, 2019.
[40] Yuzhen Niu, Yujie Geng, Xueqing Li, and Feng Liu. Lever-       [56] Yang Wang, Yi Yang, Zhenheng Yang, Liang Zhao, Peng
     aging stereopsis for saliency analysis. In IEEE CVPR, pages         Wang, and Wei Xu. Occlusion Aware Unsupervised Learn-
     454–461, 2012.                                                      ing of Optical Flow. In IEEE CVPR, 2018.
[41] Houwen Peng, Bing Li, Weihua Xiong, Weiming Hu, and            [57] Rastogi Akash Villegas Ruben Sunkavalli Kalyan Shecht-
     Rongrong Ji. Rgbd salient object detection: a benchmark             man Eli Hadap Sunil Yumer Ersin Lee Honglak Yan,
     and algorithms. In ECCV, pages 92–109, 2014.                        Xinchen. MT-VAE: Learning Motion Transformations to
[42] Xuebin Qin, Zichen Zhang, Chenyang Huang, Chao                      Generate Multimodal Human Dynamics. In ECCV, pages
     Gao, Masood Dehghan, and Martin Jagersand. BASNet:                  276–293, 2018.
     Boundary-Aware Salient Object Detection. In IEEE CVPR,         [58] Maoke Yang, Kun Yu, Chi Zhang, Zhiwei Li, and Kuiyuan
     2019.                                                               Yang. DenseASPP for Semantic Segmentation in Street
[43] Liangqiong Qu, Shengfeng He, Jiawei Zhang, Jiandong                 Scenes. In IEEE CVPR, pages 3684–3692, 2018.
     Tian, Yandong Tang, and Qingxiong Yang. RGBD salient           [59] Li Yi, Wang Zhao, He Wang, Minhyuk Sung, and Leonidas J.
     object detection via deep fusion. IEEE TIP, 26(5):2274–             Guibas. GSPN: Generative Shape Proposal Network for 3D
     2285, 2017.                                                         Instance Segmentation in Point Cloud. In IEEE CVPR, 2019.
[44] Jianqiang Ren, Xiaojin Gong, Lu Yu, Wenhui Zhou, and           [60] Shivanthan A. C. Yohanandan, Adrian G. Dyer, Dacheng
     Michael Ying Yang. Exploiting Global Priors for RGB-D               Tao, and Andy Song. Saliency Preservation in Low-
     Saliency Detection. In IEEE CVPRW, pages 25–32, 2015.               Resolution Grayscale Images. In ECCV, 2018.
[45] Danilo Jimenez Rezende, Shakir Mohamed, and Daan Wier-         [61] Jingjing Li Miao Zhang Huchuan Lu Yongri Piao, Wei Ji.
     stra. Stochastic Backpropagation and Approximate Inference          Depth-induced Multi-scale Recurrent Attention Network for
     in Deep Generative Models. In ICML, pages 1278–1286,                Saliency Detection. In IEEE ICCV, 2019.
     2014.                                                          [62] Jing Zhang, Xin Yu, Aixuan Li, Peipei Song, Bowen Liu, and
[46] Christian Rupprecht, Iro Laina, Maximilian Baust, Federico          Yuchao Dai. Weakly-Supervised Salient Object Detection
     Tombari, Gregory D. Hager, and Nassir Navab. Learning in            via Scribble Annotations. In IEEE CVPR, 2020.
     an Uncertain World: Representing Ambiguity Through Mul-        [63] Jing Zhang, Tong Zhang, Yuchao Dai, Mehrtash Harandi,
     tiple Hypotheses. In IEEE ICCV, pages 3611–3620, 2017.              and Richard Hartley. Deep Unsupervised Saliency Detec-
[47] Mohammad Sadegh Aliakbarian, Fatemeh Sadat Saleh,                   tion: A Multiple Noisy Labeling Perspective. In IEEE
     Mathieu Salzmann, Lars Petersson, Stephen Gould, and                CVPR, pages 9029–9038, 2018.
     Amirhossein Habibian. Learning Variations in Human Mo-         [64] Jia-Xing Zhao, Yang Cao, Deng-Ping Fan, Ming-Ming
     tion via Mix-and-Match Perturbation. arXiv e-prints, page           Cheng, Xuan-Yi Li, and Le Zhang. Contrast Prior and Fluid
     arXiv:1908.00733, 2019.                                             Pyramid Integration for RGBD Salient Object Detection. In
[48] Karen Simonyan and Andrew Zisserman. Very Deep Con-                 IEEE CVPR, 2019.
     volutional Networks for Large-Scale Image Recognition. In      [65] Jia-Xing Zhao, Jiang-Jiang Liu, Deng-Ping Fan, Yang Cao,
     ICLR, 2014.                                                         Jufeng Yang, and Ming-Ming Cheng. EGNet: Edge guid-
[49] Krishna Kumar Singh and Yong Jae Lee. Hide-and-Seek:                ance network for salient object detection. In IEEE ICCV,
     Forcing a Network to be Meticulous for Weakly-supervised            pages 8779–8788, 2019.
     Object and Action Localization. In IEEE ICCV, 2017.
                                                                    [66] Chunbiao Zhu, Ge Li, Wenmin Wang, and Ronggang Wang.
[50] Kihyuk Sohn, Honglak Lee, and Xinchen Yan. Learning                 An innovative salient object detection using center-dark
     Structured Output Representation using Deep Conditional             channel prior. In IEEE ICCVW, 2017.
     Generative Models. In NeurIPS, pages 3483–3491, 2015.
