---
source_id: 070
bibtex_key: ji2021monoindoor
title: MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments
year: 2021
domain_theme: Estimasi Kedalaman
verified_pdf: 70_MonoIndoor.pdf
char_count: 71275
---

MonoIndoor: Towards Good Practice of Self-Supervised
                                                               Monocular Depth Estimation for Indoor Environments

                                                                                   Pan Ji*1 , Runze Li*1,2 , Bir Bhanu2 , Yi Xu1
                                                                           1
                                                                               OPPO US Research Center, InnoPeak Technology, Inc.
                                                                                       2
                                                                                         University of California Riverside
arXiv:2107.12429v2 [cs.CV] 28 Jul 2021

                                                                     Abstract                                      scenarios where obtaining the ground-truth is not possible.
                                                                                                                      Recently, self-supervised methods [12] have achieved
                                             Self-supervised depth estimation for indoor environ-                  significant success, producing depth prediction that is com-
                                         ments is more challenging than its outdoor counterpart in                 parable to that produced by the supervised methods [14, 8].
                                         at least the following two aspects: (i) the depth range of in-            For example, on the KITTI dataset [10], Monodepth2 [12]
                                         door sequences varies a lot across different frames, making               achieves an absolute relative depth error (AbsRel) of 10.6%,
                                         it difficult for the depth network to induce consistent depth             which is not far from the AbsRel of 7.2% by supervised
                                         cues, whereas the maximum distance in outdoor scenes                      DORN [8]. However, most of these self-supervised depth
                                         mostly stays the same as the camera usually sees the sky;                 prediction methods [9, 46, 12] are only evaluated on outdoor
                                         (ii) the indoor sequences contain much more rotational mo-                datasets such as KITTI, leaving their performance opaque
                                         tions, which cause difficulties for the pose network, while               for indoor environments. A few methods [45, 44] have con-
                                         the motions of outdoor sequences are pre-dominantly trans-                sidered indoor self-supervised depth prediction, but their
                                         lational, especially for driving datasets such as KITTI. In               performance still trail far behind the one on the outdoor
                                         this paper, special considerations are given to those chal-               datasets by methods such as [9, 46, 12] or the supervised
                                         lenges and a set of good practices are consolidated for                   counterparts [8, 41] on indoor datasets. For instance, on the
                                         improving the performance of self-supervised monocular                    indoor NYUv2 dataset [33], the method by Zhao et al. [44]
                                         depth estimation in indoor environments. The proposed                     reaches an AbsRel of 18.9%, which is much higher than
                                         method mainly consists of two novel modules, i.e., a depth                what Monodepth2 can achieve on KITTI.
                                         factorization module and a residual pose estimation mod-                     In view of the performance discrepancies between the
                                         ule, each of which is designed to respectively tackle the                 indoor and outdoor scenes, we examine what makes in-
                                         aforementioned challenges. The effectiveness of each mod-                 door depth prediction more challenging than the outdoor
                                         ule is shown through a carefully conducted ablation study                 case. Our first conjecture is that this is partly due to the
                                         and the demonstration of the state-of-the-art performance                 fact that the scene depth range of indoor sequences varies
                                         on three indoor datasets, i.e., EuRoC, NYUv2 and 7-Scenes.                a lot more than in the outdoor. This results in more diffi-
                                                                                                                   culties for the depth network in inducing consistent depth
                                                                                                                   cues across images. Our second observation is that the pose
                                                                                                                   network, which is commonly used in self-supervised meth-
                                         1. Introduction                                                           ods [46, 12], tends to have large errors in rotation predic-
                                                                                                                   tion. A similar finding in [47] shows that predicted poses
                                            Depth estimation plays an essential role in a variety of               have much higher rotational errors (e.g., 10 times larger)
                                         3D perceptual tasks, such as autonomous driving, virtual                  than geometric SLAM [26] even after using a recurrent
                                         reality (VR), and augmented reality (AR). In this paper, we               pose network. This problem is not prominent on KITTI
                                         tackle the problem of estimating the depth map from a sin-                because the motions therein are mostly translational. How-
                                         gle image in a self-supervised manner. Compared to the su-                ever, since indoor datasets are often captured by hand-held
                                         pervised methods [5, 8], self-supervision [9, 46, 12] frees us            cameras [33] or MAVs [31] which inevitably undergo fre-
                                         from having to capture the ground-truth depth using depth                 quent rotations, the inaccurate rotation prediction becomes
                                         sensors (e.g., LiDAR) and therefore, it is more attractive in             detrimental to the self-supervised training of a depth model
                                             * Joint first authorship.
                                                                                                                   for indoor environments.
                                                                       P. Ji is the corresponding author (pe-
                                         terji530@gmail.com). R. Li’s contribution was made during an internship      Given the above considerations, we propose MonoIn-
                                         with OPPO US Research Center.                                             door, a monocular self-supervised depth estimation method
tailored for indoor environments. Our MonoIndoor consists        2.2. Self-Supervised Monocular Depth Estimation
of two novel modules: a depth factorization module and a
residual pose estimation module. In the depth factorization
                                                                     Self-supervised depth estimation has attracted a lot of
module, we factorize the depth map into a global depth scale
                                                                 attention recently as it does not require training with the
(for the current image) and a relative depth map. The depth
                                                                 ground truth. Along this line, Garg et al. [9] propose the
scale factor is separately predicted by an extra branch in the
                                                                 first self-supervised method to use color consistency loss
depth network. In such a way, the depth network has more
                                                                 between stereo images to train a monocular depth model.
model plasticity to adapt to the depth scale changes during
                                                                 Zhou et al. [46] employ two networks (i.e., one depth net-
training. In the residual pose estimation module, we miti-
                                                                 work and one pose network) to construct the photometric
gate the issue of inaccurate rotation prediction by perform-
                                                                 loss across temporal frames. Many follow-up methods then
ing residual pose estimation in addition to an initial large
                                                                 try to improve the self-supervision by new loss terms. Go-
pose prediction. Such a residual approach leads to more ac-
                                                                 dard et al. [11] incorporate a left-right depth consistency
curate computation of the photometric loss [12], which in
                                                                 loss for the stereo training. Bian et al. [1] put forth a tempo-
turn leads to better model training for the depth network.
                                                                 ral depth consistency loss to encourage neighboring frames
    In summary, our contributions are:                           to have consistent depth predictions. Wang et al. [37] ob-
                                                                 serve the diminishing issue of the depth model during train-
   • A novel depth factorization module that helps the           ing and come up with a simple normalization method to
     depth network adapt to the rapid scale changes;             counter this effect. Yin et al. [42] and Zou et al. [48]
   • A novel residual pose estimation module that mitigates      use three networks (i.e., one depth network, one pose net-
     the inaccurate rotation prediction issue in the pose net-   work, and one extra flow network) to enforce cross-task
     work and in turn improves depth prediction;                 consistency between optical flow and dense depth. Wang et
                                                                 al. [39] and Zou et al. [47] leverage recurrent neural net-
   • State-of-the-art performance of self-supervised depth       works, such as LSTMs, to model long-term dependency
     prediction on three publicly available indoor datasets,     in the pose network and/or the depth network. Tiwari et
     i.e., EuRoC [31], NYUv2 [33], and 7-Scenes [32].            al. [35] form a self-improving loop with monocular SLAM
                                                                 and a self-supervised depth model [12] to improve the per-
                                                                 formance of each one. Notably, Monodepth2 [12] signif-
2. Related Work                                                  icantly improves the performance over previous methods
   In this section, we review both supervised and self-          via a set of techniques: a per-pixel minimum photometric
supervised methods for monocular depth estimation.               loss to handle occlusions, an auto-masking method to mask
                                                                 out static pixels, and a multi-scale depth estimation strategy
2.1. Supervised Monocular Depth Estimation                       to mitigate the texture-copying issue in depth. Due to its
                                                                 good performance, we implement our self-supervised depth
   Early depth estimation methods are mostly supervised.         estimation framework based on Monodepth2, but make im-
Saxena et al. [30] regress the depth from a single image with    portant changes to both the depth and the pose networks.
superpixel features and a Markov Random Field (MRF).
Eigen et al. [6] propose the first deep-learning based method        Most of the aforementioned methods are only evalu-
for monocular depth estimation using a multi-scale con-          ated on outdoor datasets such as KITTI. A few other re-
volutional neural network (CNN). Later methods improve           cent methods [45, 44, 2] focus on indoor self-supervised
the performance of depth prediction either by better net-        depth estimation. Zhou et al. [45] propose an optical-flow
work architecture [19] or via more sophisticated training        based training paradigm and handle large rotational motions
losses [21, 8, 41]. A few methods [36, 34] rely on two           by a pre-processing step that removes all the image pairs
networks, one for depth prediction and the other for mo-         with “pure rotation”. Zhao et al. [44] adopt a geometry-
tion, to mimic geometric Structure-from-Motion (SfM) or          augmented strategy that solves for the depth via two-view
Simultaneous Localization and Mapping (SLAM) in a su-            triangulation and then uses the triangulated depth as super-
pervised framework. Training these methods needs ground-         vision. Bian et al. [2] argue that “the rotation behaves as
truth depth data, which is often expensive to capture. Some      noise during training” and thus propose a rectification step
other methods then resort to generating pseudo ground-           to remove the rotation between consecutive frames. We
truth depth labels with traditional 3D reconstruction meth-      have an observation similar to [45] and [2] that large rota-
ods [23, 22], such as SfM [31] and SLAM [26], or 3D              tions cause difficulties for the network. However, we take a
movies [28]. Such methods have better capacity of gen-           different strategy. Instead of removing rotations from train-
eralization across different datasets, but can not necessarily   ing data, we progressively estimate them via a novel resid-
achieve the best performance for the dataset at hand.            ual pose module. This in turn improves depth prediction.
3. Method                                                            image by Equation (2) to generate Dt0 →t , which is a corre-
                                                                     sponding depth map in the coordinate system of the source
   In this section, we give detailed descriptions of perform-        image. We then transform Dt0 →t to the coordinate system
ing self-supervised depth estimation using MonoIndoor.               of the target image via Equation (4) to produce a synthe-
Specifically, we first introduce the background of the self-         sized target depth map De t0 →t . The depth consistency loss
supervised depth estimation. Then, we describe the good              can be written as
practices in predicting depth with our MonoIndoor.
                                                                                                |Dt − D
                                                                                                      e t0 →t |
3.1. Self-Supervised Depth Estimation                                                    Lc =                   .               (6)
                                                                                                 Dt + Dt0 →t
                                                                                                      e
    Similar to [46, 12, 47], we also consider the self-
supervised depth estimation as a novel view-synthesis prob-             The overall objective to train the model is
lem by training a model to predict the target image from
different viewpoints of source images. The image synthesis                             L = LA + τ Ls + γLc ,                    (7)
process is trained and constrained by using the depth map
as the bridging variable. Such a system requires both the            where τ and γ are the weights for the edge-aware smooth-
predicted depth map of the target image and the estimated            ness loss and the depth consistency loss respectively.
relative pose between a pair of target and source images.               Even though existing monocular self-supervised meth-
Specifically, given a target image It and a source image It0         ods are able to produce competitive depth maps in outdoor
from another view, the system is jointly trained to predict a        environments, these methods still suffer from worse perfor-
dense depth map Dt of the target image and a relative cam-           mance in indoor environments, especially compared with
era pose Tt→t0 from the target to the source. The photomet-          fully-supervised methods. As discussed in Section 1, the
ric reprojection loss can then be constructed as follows:            main challenges in indoor environments come from the fact
                                                                     that the depth range changes a lot and indoor sequences con-
                          X
                   LA =       ρ(It , It0 →t ),            (1)        tain regular rotational motions which are difficult to predict.
                               t0                                    To handle these issues, we propose MonoIndoor, a monoc-
                                                                     ular self-supervised depth estimation framework, as shown
and                                                                  in Figure 1, to enable improved predicted depth quality in
              It0 →t = It0 hproj(Dt , Tt→t0 , K)i,             (2)   indoor environments.
where ρ denotes the photometric reconstruction error [46,               The system takes as input a single color image and out-
12]. It is a weighted combination of the L1 and Structured           puts a depth map via our MonoInoor which consists of two
SIMilarity (SSIM) loss defined as                                    core parts: a depth factorization module and a residual pose
                                                                     estimation module. We present our main contributions in
                α                                                   the following sections.
ρ(It , It0 →t ) =  1−SSIM(It , It0 →t ) +(1−α)kIt , It0 →t k1 .
                2
                                                          (3)        3.2. Depth Factorization
It0 →t is the source image warped to the target coordinate
frame based on the depth of the target image. proj() is the             We use the Monodepth2 [12] as the backbone model for
transformation function to map image coordinated pt from             depth prediction. The depth model in Monodepth2 employs
the target image to its pt0 on the source image following            an auto-encoder structure with skip connections between
                                                                     the encoder and the decoder. The depth encoder takes as in-
                    pt0 ∼ KTt→t0 Dt (pt )K −1 pt ,             (4)   put a color image I, and the decoder outputs its depth map.
                                                                     Note that the final depth prediction is not directly from the
and h·i is the bilinear sampling operator which is locally           convolutional layers, but after a sigmoid activation function
sub-differentiable. Following [12], the camera intrinsics K          and a linear scaling function as follows,
of all images are assumed to be the same, and an edge-ware
smoothness term is employed as                                                             d = 1/(aσ + b),                      (8)

            Ls = |∂x d∗t |e−|∂x It | + |∂y d∗t |e−|∂y It | ,   (5)   where σ is the value after the sigmoid function, a and b
                                                                     are specified to constrain the depth map D within a cer-
where d∗t = d/d¯t is the mean-normalized inverse depth               tain depth range. Practically, a and b are respectively pre-
from [37]. During training, we adopt the auto-masking                defined as a minimum depth value and a maximum depth
scheme [12] to handle static pixels.                                 value which can be obtained in a known environment. For
   Similar to [1], we use an additional depth consistency            instance, on the KITTI dataset [10], a is chosen as 0.1 and
loss to enforce consistent depth prediction across neighbor-         b as 100. The reason for setting a and b as fixed values is
ing frames. We first warp the depth image Dt0 of the source          that the depth range is consistent across the video sequences
                                                                                                                                 MonoIndoor
                       Depth Network
        𝑰𝒕                                         𝑫𝒕

                                                                                                   ⋯⋯
                                                                 𝑰𝒕"                            𝑰⋆𝒕!→𝒕                              𝑰𝒕!→𝒕
                  𝐸𝑛𝑐𝑜𝑑𝑒𝑟          𝐷𝑒𝑐𝑜𝑑𝑒𝑟
                                                                                    warp                             warp

      𝛿(𝑥)          𝑠𝑜𝑓𝑡𝑚𝑎𝑥                                    concat                           concat
                                                                                     𝑅|𝑡                               𝑅|𝑡 !"#

      𝜑(𝑥)                                                               𝑃𝑜𝑠𝑒𝑁𝑒𝑡                         𝑅𝑒𝑠𝑖𝑑𝑢𝑎𝑙𝑃𝑜𝑠𝑒𝑁𝑒𝑡

                                                   𝑺𝒕
      𝜔(𝑥)                                                       𝑰𝒕
                        Scale Network

                Depth Factorization Module                                         Residual Pose Estimation Module

Figure 1. Overview of the proposed MonoIndoor. Depth Factorization Module: We use an encoder-decoder based depth network to
predict a relative depth map and a non-local scale network to estimate a global scale factor. Residual Pose Estimation Module: We use
a pose network to predict an initial camera pose of a pair of frames and residual pose network to iteratively predict residual camera poses
based on the predicted initial pose.

when the camera always sees the sky at the far point. How-              output by
ever, this setting is not valid for most indoor environments.                                    ψ(F) = Wψ F,
As scene varies, the depth range varies a lot. For example,
                                                                                                 φ(F) = Wφ F,                                (9)
the depth range in a bathroom (e.g. 0.1m∼3m) can be very
different from the one in a lobby (e.g. 0.1m∼10m). Pre-                                          h(F) = Wh F,
setting depth range will act as an inaccurate guidance that
                                                                        where Wψ , Wφ and Wh are parameters to be learnt.
is harmful for the model to capture accurate depth scales.
                                                                        The query and key values are then combined in
This is especially true when there are rapid scale changes,
                                                                        GF = softmax(F T Wψ         T
                                                                                                      Wφ F)h(F) as the learnt self-
which are commonly observed in indoor scenes. To over-
                                                                        attentions. Finally, the self-attention GF and F jointly con-
come this problem, we propose a depth factorization mod-
                                                                        tribute to the output SF by using
ule (see Figure 1) to learn a disentangled representation in
the form of a relative depth map and a global scale factor.
                                                                                              SF = WSF GF + F.                              (10)
We employ the depth network of Monodepth2 [12] to pre-
dict relative depth and propose a self-attention-guided scale
                                                                        Once we obtain the attentive representations as SF , we ap-
regression network to predict the global scale factor for the
                                                                        ply two residual blocks including two convolutional lay-
current view.
                                                                        ers in each, followed by three fully-connected layers with
                                                                        dropout layers in-between, to output the global scale factor
                                                                        S for the current image.
                                                                        Probabilistic Scale Regression Head. To predict a global
Scale Network. We design the scale network as a new                     scale, a high-dimensional feature map has to be mapped into
branch which takes as input a color image and outputs its               a single positive number. One straightforward way is to let
global scale factor. Since the global scale factor is closely           the network directly regress the scale number. However,
informed by certain areas (e.g., the far point) in the images,          we observe unstable training using this approach. To mit-
we explore to use a self-attention block [40] so that the net-          igate this issue, inspired by [4], we propose to use a prob-
work can be guided to pay more attention to a certain area              abilistic scale regression head to estimate this continuous
which is informative to induce the depth scale factor of the            value. Given a maximum bound that the global scale factor
current view in a scene. Given the feature representations F            is within, the probability of each scale s is calculated from
learnt from the input image, we utilize a self-attention block          the output of the scale network Se via the softmax operation
to take F as input, forming the query, the key and the value            softmax(·). The predicted global scale S is calculated as
       inverse warping
                                                                    reconstructing a virtual view It00 →t which is expected to be
                         single-stage pose                          the same as the target image It if the correspondences match
                                                                    accurately. However, it will not be the case due to inaccu-
 𝑰𝒕"               initial pose     𝑰𝒕"      residual pose
                                                             𝑰𝒕     rate pose prediction. Note here the transformation is defined
   𝟎                                  𝒊
                                                                    as
                                                                                 It00 →t = It0 hproj(Dt , Tt−1
                                                                                                            0 →t , K)i.      (12)
                                                                                                                 0

                                                                    Next, we utilize a residual pose network (see Residual-
source view                        virtual view       target view   PoseNet in Figure 1) which takes the target image and the
                                                                    synthesized view It00 →t as input and outputs a residual cam-
Figure 2. Residual Pose Estimation. Here we give an illustrative    era pose T(tres
                                                                                 0 →t)→t , representing the camera pose of the
                                                                                 0
example of how a single-stage pose can be decomposed into an        synthesized image It00 →t with respect to the target image.
initial pose and a residual pose by virtual view synthesis.         Now, we bilinearly sample from the synthesized image as
                                                                                                                −1
                                                                        I(t00 →t)→t = It00 →t hproj(Dt , T(tres
                                                                                                             0 →t)→t , K)i.            (13)
the sum of each scale s weighted by its probability as                                                            0

                         DX
                          max
                                                                    Once we obtain a new synthesized view, we can continue to
                    S=          s × softmax(S).
                                            e                (11)   estimate the next residual poses for next view synthesis. For
                         s=0
                                                                    simplicity of notation in Equation (13), we replace the sub-
                                                                    script t00 → t with t01 to indicate that one warping transfor-
By doing so, the regression problem is smoothly resolved            mation is applied, and similarly for the ith transformation.
by a probabilistic classification-based strategy (see Sec-          Thus, a general form of Equation (13) is defined by
tion 4.1.1 for more ablation results).
                                                                      It0i →t = It0i hproj(Dt , Ttres−1
                                                                                                  0 →t , K)i, i = 0, 1, · · · .        (14)
3.3. Residual Pose Estimation                                                                       i

    As mentioned in Section 3.1, self-supervised depth es-          After we estimate multiple residual poses, the camera pose
timation is built upon the novel view synthesis, which re-          of source image It0 with respect to the target image It can
quires both accurate depth maps and camera poses. Es-               be written as Tt→t0 = Tt−1
                                                                                            0 →t where

timating accurate relative poses is key for the photomet-                               Y
ric reprojection loss because inaccurate poses might lead                    Tt0 →t =        Tt0i →t , i = · · · , k, · · · , 1, 0 .   (15)
to wrong correspondences between the target and source                                   i

pixels, causing problems in predicting the depth. Exist-            By iteratively estimating residual poses, we expect to ob-
ing methods mostly employ a standalone PoseNet to esti-             tain more accurate camera poses compared with the pose
mate the 6 Degrees-of-Freedom (DoF) pose between two                predicted from a single-stage pose network, so that a more
images. In outdoor environments (e.g., driving scenes like          accurate photometric reprojection loss can be built up for
KITTI), the relative camera poses are fairly simple because         better depth prediction.
the cars are mostly moving forward with large translations
but minor rotations. This means that pose estimation is nor-        4. Experiments
mally less challenging. In contrast, in indoor environments,
the sequences are typically recorded with hand-held devices         Datasets. We evaluate the proposed framework MonoIn-
(e.g., Kinect), so there are more complicated ego-motions           door on two challenging indoor datasets: the EuRoC
involved as well as much larger rotational motions. It is           MAV [31] dataset, the NYUv2 depth dataset [33] and RGB-
thus more difficult for the pose network to learn accurate          D 7-Scenes dataset [32].
camera poses.                                                       Evaluation Metrics. For evaluation, we follow [6] to
    Unlike existing methods [45, 2] that concentrate on “re-        use the mean absolute relative error (AbsRel), root mean
moving” or “reducing” rotational components during data             squared error (RMS), and the accuracy under threshold
preprocessing, we instead propose a residual pose estima-           (δi < 1.25i , i = 1, 2, 3) on both datasets.
tion module to learn the relative camera pose between the           Implementation Details. We implement our model using
target and source images in an iterative manner (see Fig-           PyTorch [27]. In the depth factorization module, we use the
ure 2). In the first stage, the pose network takes a target         same depth network as in [12]; for the scale network, we use
image It and a source image It00 as input and predicts an           two basic residual blocks followed by three fully-connected
initial camera pose Tt00 →t , where the subscript 0 in t00 indi-    layers with a dropout layer in-between. The dropout rate
cates that no transformation is applied yet. We then follow         is set to 0.5. In the residual pose module, we let the resid-
Equation (2) to bilinearly sample from the source image,            ual pose networks use a common architecture [12] which
Table 1. Ablation results of design choices and the effectiveness                           Input                     Monodepth2 [12]                   Ours
of components in the depth factorization module of our model
(MonoIndoor) on EuRoC [31]. Porb. Reg.: the probabilistic scale
regression block. Note: here we also use the residual pose estima-
tion module when experimenting with different network designs
for the depth factorization module.
                                   Prob.     Error Metric       Accuracy Metric
  Network Design       Attention
                                   Reg.    AbsRel RMSE         δ1     δ2      δ3
     I. ScaleCNN          3         3       0.140    0.518   0.821 0.956 0.985
      II. ScaleNet        3         3       0.141    0.519   0.817 0.959 0.988
 III. ScaleRegressor      7          7      0.139    0.508   0.817 0.960 0.987
 III. ScaleRegressor      3          7      0.135    0.501   0.825 0.964 0.989
 III. ScaleRegressor      3         3       0.125    0.466   0.840 0.965 0.993

consists of a shared pose encoder and an independent pose
regressor. Each experiment is trained for 40 epochs using
the Adam [17] optimizer and the learning rate is set to 10−4
for the first 20 epochs and it drops to 10−5 for remaining
epochs. The smoothness term τ and consistency term γ are
set as 0.001 and 0.05, respectively.
4.1. EuRoC MAV Dataset
                                                                                   Figure 3. Qualitative comparison of depth prediction on EuRoC.
   The EuRoC MAV Dataset [31] contains 11 video se-                                Our model produces more accurate and cleaner depth maps.
quences captured in two main scenes, a machine hall and
a vicon room. Sequences are categorized as easy, medium
and difficult according to the varying illumination and cam-                       formance gradually improves as we add more components
era motions. For the training, we use three sequences                              (i.e., attention and Prob. Reg.). Specifically, adding the
of “Machine hall” (MH 01, MH 02, MH 04) and two se-                                self-attention block improves the overall performance over
quences of “Vicon room” (V1 01 and V1 02). Images are                              the baseline backbone; adding the probabilistic regression
rectified with provided camera intrinsics to remove image                          block leads to a further improvement, which validates the
distortion. During training, images are resized to 512×256.                        effectiveness of our proposed sub-modules.
Following [13], we use the Vicon room sequence V2 01 for
testing where the ground-truth depths are generated by pro-
jecting Vicon 3D scans onto the image planes.                                      4.1.2    Quantitative Results

4.1.1     Ablation Study                                                           Since there are not many public results reported on the Eu-
                                                                                   RoC MAV [31] dataset, we mainly compare our model with
We perform ablation studies for our design choices of the                          the baseline model Monodepth2 [12] and validate the effec-
depth factorization module on the EuRoC MAV dataset.                               tiveness of each module of our MonoIndoor. As shown in
Firstly, we consider the following designs as the backbone                         Table 2, adding our depth factorization module reduces the
of our scale network: I) a pre-trained ResNet-18 [15] fol-                         AbsRel from 15.7% to 14.9%, and our residual pose module
lowed by a group of Conv-BN-ReLU layers; II) a pre-                                decreases the AbsRel to 14.1%, which verifies the useful-
trained ResNet-18 [15] followed by two residual blocks;                            ness of each module. Our full model achieves the best per-
III) a lightweight network with two residual blocks which                          formance across all evaluation metrics. Specifically, com-
shares the feature maps from the depth encoder as in-                              pared to Monodepth2, the AbsRel by our MonoIndoor is
put. These three choices are referred to as the ScaleCNN,                          significantly decreased from 15.7% to 12.5% and the δ1 is
ScaleNet and ScaleRegressor, respectively in Table 1. Next,                        improved by around 6%, from 78.6% to 84.0%.
we validate the effectiveness of adding new components
into our backbone design. As described in Section 3.2, we                          Table 2. Ablation results of our MonoIndoor and quantitative com-
mainly integrate two sub-modules: i) a self-attention block                        parison with the baseline on the test sequence V2 01 of EuRoC.
and ii) a probabilistic scale regression block.                                    Best results are in bold.
                                                                                                         Depth         Residual     Error Metric       Accuracy Metric
    As shown in Table 1, the best performance is achieved                               Method
                                                                                                      Factorization     Pose      AbsRel RMSE         δ1     δ2      δ3
by ScaleRegressor that uses self-attention and probabilis-                          Monodepth2 [12]        7              7        0.157    0.567   0.786 0.941 0.986
                                                                                     MonoIndoor            3              7        0.149    0.535   0.805 0.955 0.987
tic scale regression. It proves that sharing features with                           MonoIndoor            7              3        0.141    0.518   0.815 0.961 0.991
                                                                                     MonoIndoor            3              3        0.125    0.466   0.840 0.965 0.993
the depth encoder is beneficial to scale estimation. Com-
paring the results of three ScaleRegressor variants, the per-
4.1.3    Qualitative Results                                                              Table 4. Comparison of our method to existing supervised and self-
                                                                                          supervised methods on NYUv2 [33]. Best results among super-
Figure 3 gives a qualitative comparison of depth maps pre-                                vised and self-supervised methods are in bold.
                                                                                                                                    Error Metric        Accuracy Metric
dicted by Monodepth2 [12] and our MonoIndoor. From                                                Methods           Supervision
                                                                                                                                  AbsRel RMS          δ1      δ2      δ3
Figure 3, it is clear that the depth maps generated by                                        Make3D [30]               3          0.349    1.214   0.447 0.745 0.897
our model are much better than the ones by Monodepth2.                                     Depth Transfer [16]          3          0.349    1.210      -       -       -
                                                                                              Liu et al. [25]           3          0.335    1.060      -       -       -
For instance, in the first row, our model can predict pre-                                  Ladicky et al. [18]         3            -         -    0.542 0.829 0.941
cise depths for the hole region at the right-bottom corner                                     Li et al. [20]           3          0.232    0.821   0.621 0.886 0.968
                                                                                              Roy et al. [29]           3          0.187    0.744      -       -
whereas such a hole structure in the depth map by Mon-                                        Liu et al. [24]           3          0.213    0.759   0.650 0.906 0.976
odepth2 is missing. Besides, in the second row, our model                                    Wang et al. [38]           3          0.220    0.745   0.605 0.890 0.970
can predict much sharper depth map of the ladder at the                                      Eigen et al. [5]           3          0.158    0.641   0.769 0.950 0.988
                                                                                           Chakrabarti et al. [3]       3          0.149    0.620   0.806 0.958 0.987
right-top area while Monodepth2 cannot. These observa-                                       Laina et al. [19]          3          0.127    0.573   0.811 0.953 0.988
tions are also consistent with the better quantitative results                                 Li et al. [21]           3          0.143    0.635   0.788 0.958 0.991
                                                                                                DORN [8]                3          0.115    0.509   0.828 0.965 0.992
in Table 2, proving the superiority of our model.                                               VNL [41]                3          0.108    0.416   0.875 0.976 0.994
                                                                                              Fang et al. [7]           3          0.101    0.412   0.868 0.958 0.986
4.2. NYUv2 Depth Dataset                                                                     Zhou et al. [45]           7          0.208    0.712   0.674 0.900 0.968
                                                                                             Zhao et al. [44]           7          0.189    0.686   0.701 0.912 0.978
    In this section, we evaluate our MonoIndoor on the                                      Monodepth2 [12]             7          0.160    0.601   0.767 0.949 0.988
NYUv2 depth dataset [33] which contains 464 indoor video                                      Bian et al. [2]           7          0.147    0.536   0.804 0.950 0.986
                                                                                           MonoIndoor(Ours)             7          0.134    0.526   0.823 0.958 0.989
sequences captured by a hand-held Microsoft Kinect RGB-
D camera with a resolution of 640× 480. We use the official
training and validation splits which include 302 and 33 se-
                                                                                          the residual pose estimation module (i.e., our full MonoIn-
quences respectively. We rectify the images with provided
                                                                                          door), significant improvements can be achieved across all
camera parameters to remove distortions. Following [44, 2],
                                                                                          evaluation metrics. For instance, the AbsRel is reduced to
the raw dataset is firstly downsampled 10 times along the
                                                                                          13.4% and the δ1 is increased to 82.3%. These ablation
temporal dimension to remove redundant frames, resulting
                                                                                          results clearly prove the effectiveness of the proposed mod-
in ∼ 20K images for training. During training, images are
                                                                                          ules, which also align with the qualitative results in Figure 4
resized to 320×256. We use officially provided 654 images
                                                                                          where we visualize predictions on NYUv2 by our proposed
with dense labelled depth maps for testing.
                                                                                          modules. However, referring to the last two rows, when
Table 3. Ablation results of the effectiveness of each module of                          adding more residual pose blocks and training with/without
our MonoIndoor on NYUv2. “No. Residual Pose Block” means                                  the depth factorization module, the performance does not
the number of residual poses we estimate in the residual pose esti-                       significantly improve or even becomes worse. We will leave
mation module.                                                                            the investigation of this phenomenon for future work.
                      Depth        No. Residual     Error Metric       Accuracy Metric
     Model
                   Factorization    Pose Block    AbsRel RMS          δ1     δ2      δ3      We further visualize intermediate and final synthesized
 Monodepth2 [12]        7                0         0.16     0.601   0.767 0.949 0.988
  MonoIndoor            3                0         0.152    0.576   0.792 0.951 0.987     views compared with the current view on NYUv2 in the
  MonoIndoor            7                1         0.142    0.553   0.813 0.958 0.988
  MonoIndoor            3                1         0.134    0.526   0.823 0.958 0.989     Figure 5. Highlighted regions show that final synthesized
  MonoIndoor            7                2         0.141    0.548   0.814 0.958 0.988     views are better than the intermediate synthesized views and
  MonoIndoor            3                2         0.141    0.546   0.818 0.958 0.989
                                                                                          closer to the current view.

4.2.1    Ablation Study
                                                                                          4.2.2     Quantitative Results
We perform another ablation study for the depth factoriza-
tion module on NYUv2 [33]. In Table 3, comparing with                                     We present the quantitative results of our model MonoIn-
Monodepth2 which predicts depth without any guidance of                                   door and both state-of-the-art (SOTA) supervised and self-
global scales, using the depth factorization module with a                                supervised methods on NYUv2 in Table 4. It shows that our
separate scale network can improve the performance, de-                                   model outperforms previous self-supervised SOTA meth-
creasing the AbsRel from 16% to 15.2% and increasing                                      ods, reaching the best results across all metrics. Specif-
δ1 to 79.2%. Next, we experiment to validate the effec-                                   ically, compared to a recent self-supervised method by
tiveness of the residual pose estimation module. Compar-                                  Bian et al. [2] which removes rotations via “weak rectifi-
ing the rows in Table 3, by adding the residual pose esti-                                cation”, our method reduces AbsRel by 1.3% and increases
mation module with one residual pose block, we observe                                    δ1 by 1.9%, reaching an AbsRel of 13.4% and δ1 of 82.3%.
an improved performance from 16.0% down to 14.2% for                                      In addition to that, our model outperforms a group of super-
the AbsRel and from 76.7% up to 81.3% for δ1 . Further-                                   vised methods and close the performance gap between the
more, by applying both the depth factorization module and                                 self-supervised methods and fully-supervised methods.
          Input            Ours (w depth factorization)   Ours (w residual pose)         Ours (full model)             GT

Figure 4. Qualitative ablation comparisons of depth prediction on NYUv2. Our full model with both depth factorization and residual pose
modules produce better depth maps.

                          Intermediate                Final                                      Intermediate           Final
    Current view                                                         Current view
                        synthesized view        synthesized view                               synthesized view   synthesized view

                                          Figure 5. Intermediate synthesized views on NYUv2.

         Table 5. Comparison of our method to latest self-supervised methods on RGB-D 7-Scenes [32]. Best results are in bold
                                                Bian et al. [2]                    MonoIndoor (Ours)
                        Scenes      Before Fine-tuning After Fine-tuning Before Fine-tuning After Fine-tuning
                                    AbsRel     Acc δ1     AbsRel Acc δ1 AbsRel       Acc δ1   AbsRel Acc δ1
                         Chess       0.169     0.719       0.103     0.880   0.157   0.750     0.097     0.888
                          Fire       0.158     0.758       0.089     0.916   0.150   0.768     0.077     0.939
                   .
                        Heads        0.162     0.749       0.124     0.862   0.171   0.727     0.106     0.889
                        Office       0.132     0.833       0.096     0.912   0.130   0.837     0.083     0.934
                       Pumpkin       0.117     0.857       0.083     0.946   0.102   0.895     0.078     0.945
                      RedKitchen     0.151      0.78       0.101     0.896   0.144   0.795     0.094     0.915
                         Stairs      0.162     0.765       0.106     0.855   0.155   0.753     0.104     0.857

4.2.3   Qualitative Results                                             Following [2], for training, we first pre-train our MonoIn-
                                                                        door on NYUv2 dataset, and then fine-tune the model on
Figure 6 visualizes the predicted depth maps on NYUv2.                  this dataset; for testing, we extract one image from every 30
Compared with the results from the Monodepth2 [12],                     frames. Images are resized to 320 × 256 during training.
depth maps predicted from our model (MonoIndoor) are
more precise and closer to the ground-truth. For instance,
looking at the third column in the first row, the depth in the
region of chairs predicted from our model is much sharper               4.3.1      Quantitative Results
and cleaner, being close to the ground truth (the last col-
umn). On the rightmost area of the same image where there
is a shelf , our model can produce better depth predictions             We present the quantitative results of our model MonoIn-
that reflect its shape. These observations are consistent with          door and latest state-of-the-art (SOTA) self-supervised
our quantitative results in Table 4.                                    methods on 7-Scenes in Table 5. It shows that our model
                                                                        outperforms [2] on most scenes before and after fine-tuning,
4.3. RGB-D 7-Scenes Dataset                                             demonstrating better generalizability and capability of our
                                                                        model. Specifically, compared to a recent self-supervised
   In this section, we evaluate our MonoIndoor on the                   method by Bian et al. [2], on the scene “Fire”, our method
RGB-D 7-Scenes dataset [32] which contains several video                reduces AbsRel by 1.2% and increases δ1 by 2.3%, reach-
sequences with 500-1000 frame in each sequence. All                     ing an AbsRel of 7.7% and δ1 of 93.9%; on the scene
scenes are recorded using a handheld Kinect RGB-D cam-                  ”Heads”,our method reduces AbsRel by 1.8% and increases
era at 640×480 resolution. We use the official train/test split.        δ1 by 2.7%, reaching an AbsRel of 10.6% and δ1 of 88.9%.
             Input                      Monodepth2 [12]                        Ours                             GT

Figure 6. Qualitative comparison on NYUv2 [33]. Compared with Monodepth2 [12], our model produces accurate depth maps (in the third
column) that are closer to the ground-truth.

5. Conclusions                                                      propose a residual pose estimation module that decomposes
                                                                    a global pose into an initial pose and one or a few residual
   In this work, we have presented a novel monocular self-          poses, which in turn improves the depth model. We have
supervised depth estimation model, namely MonoIndoor,               shown that our model achieves the state-of-the-art perfor-
to study good practices towards predicting accurate depth           mance among the self-supervised methods on two challeng-
maps in indoor environments. We first introduce the depth           ing indoor datasets, i.e., EuRoC and NYUv2.
factorization module to jointly learn a global scale factor             It is to be noted that our depth factorization module is in
and a relative depth map from an input image. To esti-              itself agnostic to the types of supervision, so it may also be
mate accurate camera poses for novel view synthesis, we             helpful for supervised depth prediction. In the future, we
plan to investigate its effectiveness in a supervised setup.                    Input            Monodepth2 [1]             Ours
Another interesting future direction would be to train our
method on multiple datasets with various depth ranges and
then test it for zero-shot cross-dataset transfer as in [28].

Appendix
Network Details
    In the depth factorization module, we use the same depth
network of an auto-encoder structure as in [12] to predict
the relative depth, and employ a scale network consisting of
an encoder and a regressor. The encoder of the scale net-
work is shared with the depth encoder and the architecture
of the scale regressor is described in Table 6. In the resid-
ual pose module, we use one pose network and one resid-
ual pose network, both of which share the same structure.
The residual pose network shares parameters in the encoder
with the pose network but learns independent parameters in
its pose prediction head.                                              Figure 7. Additional qualitative comparison on EuRoC MAV[31].
Table 6. Scale regressor architecture. Here chns is the number
                                                                       Table 7. Odometry results on the EuRoC MAV [31] test set. Re-
of ouput channels, k is the kernal size, s is the stride, res is the
                                                                       sults show the average absolute trajectory error(ATE), and the rel-
downscaling factor for each layer with respect to the input image,
                                                                       ative pose error(RPE) in meters and degrees, respectively. Seq.:
and input is the input to each layer.
                                                                       sequence name.
                          Scale Regressor
                                                                           Seq.         Methods           ATE(m) RPE(m) RPE(°)
      Block          layer        chns-k-s    res        input
                                                                                    Monodepth2 [12]        0.0681     0.0686    1.3237
                    (query)      (512, 1, 1)           (econv5)           V1 03
                                                                                   MonoIndoor(Ours)         0.052     0.0637    0.7179
    Attention        (key)       (512, 1, 1)   32      (econv5)
                    (value)      (512, 1, 1)           (econv5)                     Monodepth2 [12]        0.0266     0.0199    1.1985
                                                                          V2 01
                  (convs1 0)     (512, 3, 1)                                       MonoIndoor(Ours) 0.0222            0.0109    1.1974
   ConvBlock1                                  32     Attention
                  (convs1 1)     (512, 3, 1)
   ConvBlock2      convs2 0      1024, 1, 2    64 ConvBlock1
                  (Convs3 0) (1024, 3, 1)                              0.0681 meters to 0.052 meters and PRE(°) is reduced by
   ConvBlock3                                  64 ConvBlock2
                  (Convs3 1) (1024, 3, 1)                              around half, from 1.3237°to 0.7179°.
                         FC1-1024-Dropout
                         FC2-1024-Dropout
                                                                       Additional Qualitative Results
                          Scale Regression
                                                                          We include additional qualitative results on both the Eu-
                                                                       RoC and NYUv2 test sets in Figure 7 and Figure 8, respec-
Odometry Evaluation                                                    tively. From both figures, we can see that our models gen-
    In Table 7, we evaluate the proposed residual pose es-             erate depth maps of higher quality.
timation module on the test sequences V1 03 and V2 01
of the EuRoC MAV [31]. We follow [43] to evaluate rela-                References
tive camera poses estimated by our residual pose estimation
                                                                        [1] Jia-Wang Bian, Zhichao Li, Naiyan Wang, Huangying Zhan,
module. We use the following evaluation metrics: absolute
                                                                            Chunhua Shen, Ming-Ming Cheng, and Ian Reid. Unsuper-
trajectory error (ATE) which measures the root-mean square                  vised scale-consistent depth and ego-motion learning from
error between predicted camera poses and ground-truth, and                  monocular video. arXiv preprint arXiv:1908.10553, 2019.
relative pose error (RPE) which measures frame-to-frame                     2, 3
relative pose error in meters and degrees, respectively. As             [2] Jia-Wang Bian, Huangying Zhan, Naiyan Wang, Tat-Jun
shown in Table 7, on both two test sequences, compared                      Chin, Chunhua Shen, and Ian Reid. Unsupervised depth
with the baseline model Monodepth2 [12] which employs                       learning in challenging indoor video: Weak rectification to
one-stage pose network, using our residual pose estimation                  rescue. arXiv preprint arXiv:2006.02708, 2020. 2, 5, 7, 8
module leads to improved relative pose estimation across all            [3] Ayan Chakrabarti, Jingyu Shao, and Greg Shakhnarovich.
evaluation metrics. Specifically, on the sequence V1 03, the                Depth from a single image by harmonizing overcomplete lo-
ATE by our MonoIndoor is significantly decreased from                       cal network predictions. In NeurIPS, 2016. 7
              Input                       Monodepth2 [1]                      Ours                            GT

                                    Figure 8. Additional qualitative comparison on NYUv2 [33].

[4] Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo                   manghelich, and Dacheng Tao. Deep ordinal regression net-
    matching network. In CVPR, pages 5410–5418, 2018. 4                 work for monocular depth estimation. In CVPR, June 2018.
[5] David Eigen and Rob Fergus. Predicting depth, surface nor-          1, 2, 7
    mals and semantic labels with a common multi-scale convo-       [9] Ravi Garg, Vijay Kumar Bg, Gustavo Carneiro, and Ian Reid.
    lutional architecture. In ICCV, December 2015. 1, 7                 Unsupervised cnn for single view depth estimation: Geome-
[6] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map           try to the rescue. In ECCV, pages 740–756, 2016. 1, 2
    prediction from a single image using a multi-scale deep net-   [10] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
    work. arXiv preprint arXiv:1406.2283, 2014. 2, 5                    ready for autonomous driving? the kitti vision benchmark
[7] Zhicheng Fang, Xiaoran Chen, Yuhua Chen, and Luc Van                suite. In CVPR, 2012. 1, 3
    Gool. Towards good practice for cnn-based monocular depth      [11] Clément Godard, Oisin Mac Aodha, and Gabriel J Bros-
    estimation. In WACV, March 2020. 7                                  tow. Unsupervised monocular depth estimation with left-
[8] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-                   right consistency. In CVPR, pages 270–279, 2017. 2
[12] Clément Godard, Oisin Mac Aodha, Michael Firman, and          [28] René Ranftl, Katrin Lasinger, David Hafner, Konrad
     Gabriel J Brostow. Digging into self-supervised monocular           Schindler, and Vladlen Koltun. Towards robust monocular
     depth estimation. In ICCV, pages 3828–3838, 2019. 1, 2, 3,          depth estimation: Mixing datasets for zero-shot cross-dataset
     4, 5, 6, 7, 8, 9, 10                                                transfer. arXiv preprint arXiv:1907.01341, 2019. 2, 10
[13] Ariel Gordon, Hanhan Li, Rico Jonschkowski, and Anelia         [29] Anirban Roy and Sinisa Todorovic. Monocular depth esti-
     Angelova. Depth from videos in the wild: Unsupervised               mation using neural regression forest. In CVPR, June 2016.
     monocular depth learning from unknown cameras. In CVPR,             7
     2019. 6                                                        [30] Ashutosh Saxena, Min Sun, and Andrew Y Ng. Make3d:
[14] Xiaoyang Guo, Hongsheng Li, Shuai Yi, Jimmy Ren, and                Learning 3d scene structure from a single still image.
     Xiaogang Wang. Learning monocular depth by distilling               TPAMI, 31(5):824–840, 2008. 2, 7
     cross-domain stereo networks. In ECCV, pages 484–500,          [31] Johannes L Schonberger and Jan-Michael Frahm. Structure-
     2018. 1                                                             from-motion revisited. In CVPR, pages 4104–4113, 2016. 1,
[15] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.              2, 5, 6, 10
     Deep residual learning for image recognition. In CVPR, June    [32] Jamie Shotton, Ben Glocker, Christopher Zach, Shahram
     2016. 6                                                             Izadi, Antonio Criminisi, and Andrew Fitzgibbon. Scene co-
[16] Kevin Karsch, Ce Liu, and Sing Bing Kang. Depthtransfer:            ordinate regression forests for camera relocalization in rgb-d
     Depth extraction from video using non-parametric sampling.          images. In Proceedings of the IEEE Conference on Com-
     TPAMI, 2014. 7                                                      puter Vision and Pattern Recognition (CVPR), June 2013. 2,
[17] Diederik P Kingma and Jimmy Lei Ba. Adam: A method for              5, 8
     stochastic gradient descent. In ICLR, pages 1–15, 2015. 6      [33] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
[18] Lubor Ladicky, Jianbo Shi, and Marc Pollefeys. Pulling              Fergus. Indoor segmentation and support inference from
     things out of perspective. In CVPR, June 2014. 7                    rgbd images. In ECCV, 2012. 1, 2, 5, 7, 9, 11
[19] Iro Laina, Christian Rupprecht, Vasileios Belagiannis, Fed-    [34] Zachary Teed and Jia Deng. Deepv2d: Video to depth
     erico Tombari, and Nassir Navab. Deeper depth prediction            with differentiable structure from motion. arXiv preprint
     with fully convolutional residual networks. In 3DV, pages           arXiv:1812.04605, 2018. 2
     239–248. IEEE, 2016. 2, 7                                      [35] Lokender Tiwari, Pan Ji, Quoc-Huy Tran, Bingbing Zhuang,
[20] Bo Li, Chunhua Shen, Yuchao Dai, Anton van den Hengel,              Saket Anand, and Manmohan Chandraker. Pseudo rgb-d
     and Mingyi He. Depth and surface normal estimation from             for self-improving monocular slam and depth prediction. In
     monocular images using regression on deep features and hi-          ECCV, pages 437–455, 2020. 2
     erarchical crfs. In CVPR, June 2015. 7                         [36] Benjamin Ummenhofer, Huizhong Zhou, Jonas Uhrig, Niko-
[21] Jun Li, Reinhard Klein, and Angela Yao. A two-streamed              laus Mayer, Eddy Ilg, Alexey Dosovitskiy, and Thomas
     network for estimating fine-scaled depth maps from single           Brox. Demon: Depth and motion network for learning
     rgb images. In ICCV, Oct 2017. 2, 7                                 monocular stereo. In CVPR, pages 5038–5047, 2017. 2
[22] Zhengqi Li, Tali Dekel, Forrester Cole, Richard Tucker,        [37] Chaoyang Wang, José Miguel Buenaposada, Rui Zhu, and
     Noah Snavely, Ce Liu, and William T Freeman. Learning               Simon Lucey. Learning depth from monocular videos using
     the depths of moving people by watching frozen people. In           direct methods. In CVPR, pages 2022–2030, 2018. 2, 3
     CVPR, pages 4521–4530, 2019. 2                                 [38] Peng Wang, Xiaohui Shen, Zhe Lin, Scott Cohen, Brian
[23] Zhengqi Li and Noah Snavely. Megadepth: Learning single-            Price, and Alan L. Yuille. Towards unified depth and se-
     view depth prediction from internet photos. In CVPR, pages          mantic prediction from a single image. In CVPR, June 2015.
     2041–2050, 2018. 2                                                  7
[24] Fayao Liu, Chunhua Shen, and Guosheng Lin. Deep con-           [39] Rui Wang, Stephen M Pizer, and Jan-Michael Frahm. Recur-
     volutional neural fields for depth estimation from a single         rent neural network for (un-) supervised learning of monocu-
     image. In CVPR, June 2015. 7                                        lar video visual odometry and depth. In CVPR, pages 5555–
[25] Miaomiao Liu, Mathieu Salzmann, and Xuming He.                      5564, 2019. 2
     Discrete-continuous depth estimation from a single image.      [40] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaim-
     In CVPR, June 2014. 7                                               ing He. Non-local neural networks. In CVPR, 2018. 4
[26] Raul Mur-Artal and Juan D Tardós. Orb-slam2: An open-         [41] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     source slam system for monocular, stereo, and rgb-d cam-            forcing geometric constraints of virtual normal for depth pre-
     eras. IEEE Transactions on Robotics, 33(5):1255–1262,               diction. In ICCV, October 2019. 1, 2, 7
     2017. 1, 2                                                     [42] Zhichao Yin and Jianping Shi. Geonet: Unsupervised learn-
[27] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer,                ing of dense depth, optical flow and camera pose. In CVPR,
     James Bradbury, Gregory Chanan, Trevor Killeen, Zeming              pages 1983–1992, 2018. 2
     Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison,         [43] Huangying Zhan, Chamara Saroj Weerasekera, Jia-Wang
     Andreas Kopf, Edward Yang, Zachary DeVito, Martin Rai-              Bian, and Ian Reid. Visual odometry revisited: What should
     son, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner,           be learnt? In ICRA, pages 4203–4210, 2020. 10
     Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An         [44] Wang Zhao, Shaohui Liu, Yezhi Shu, and Yong-Jin Liu. To-
     imperative style, high-performance deep learning library. In        wards better generalization: Joint depth-pose learning with-
     NeurIPS, pages 8024–8035. 2019. 5                                   out posenet. In CVPR, pages 9151–9161, 2020. 1, 2, 7
[45] Junsheng Zhou, Yuwang Wang, Kaihuai Qin, and Wenjun
     Zeng. Moving indoor: Unsupervised video depth learning
     in challenging environments. In ICCV, pages 8618–8627,
     2019. 1, 2, 5, 7
[46] Tinghui Zhou, Matthew Brown, Noah Snavely, and David G
     Lowe. Unsupervised learning of depth and ego-motion from
     video. In CVPR, pages 1851–1858, 2017. 1, 2, 3
[47] Yuliang Zou, Pan Ji, Quoc-Huy Tran, Jia-Bin Huang, and
     Manmohan Chandraker. Learning monocular visual odom-
     etry via self-supervised long-term modeling. arXiv preprint
     arXiv:2007.10983, 2020. 1, 2, 3
[48] Yuliang Zou, Zelun Luo, and Jia-Bin Huang. DF-Net: Un-
     supervised joint learning of depth and flow using cross-task
     consistency. In ECCV, 2018. 2
