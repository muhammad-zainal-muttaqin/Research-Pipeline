---
source_id: 060
bibtex_key: wang2022tokenfusion
title: Multimodal Token Fusion for Vision Transformers
year: 2022
domain_theme: Segmentasi RGB-D
verified_pdf: 60_Multimodal Token Fusion.pdf
char_count: 85107
---

Multimodal Token Fusion for Vision Transformers

                                             Yikai Wang1 Xinghao Chen2 Lele Cao1 Wenbing Huang3 Fuchun Sun1B Yunhe Wang2
                                                  1
                                                    Beijing National Research Center for Information Science and Technology (BNRist),
                                                                  State Key Lab on Intelligent Technology and Systems,
                                                          Department of Computer Science and Technology, Tsinghua University
                                               2
                                                 Huawei Noah’s Ark Lab 3 Institute for AI Industry Research (AIR), Tsinghua University
arXiv:2204.08721v2 [cs.CV] 15 Jul 2022

                                                     wangyk17@mails.tsinghua.edu.cn, xinghao.chen@huawei.com, caolele@gmail.com,
                                                             hwenbing@126.com, fuchuns@tsinghua.edu.cn, yunhe.wang@huawei.com

                                                                   Abstract                               former variants have shown great potential in many single-
                                                                                                          modal vision tasks, such as classification [6, 21], segmenta-
                                             Many adaptations of transformers have emerged to ad-         tion [44, 47], detection [3, 8, 22, 48], image generation [16].
                                         dress the single-modal vision tasks, where self-attention           Yet up until the date of this work, the attempt of extend-
                                         modules are stacked to handle input sources like images.         ing vision transformers to handle multimodal data remains
                                         Intuitively, feeding multiple modalities of data to vision       scarce. When multimodal data with complicated alignment
                                         transformers could improve the performance, yet the inner-       relations are introduced, it poses great challenges in design-
                                         modal attentive weights may also be diluted, which could         ing the fusion scheme for model architectures. The key
                                         thus undermine the final performance. In this paper, we          question to answer is how and where the interaction of fea-
                                         propose a multimodal token fusion method (TokenFusion),          tures from different modalities should take place. There
                                         tailored for transformer-based vision tasks. To effectively      have been a few methods for transformer-based vision-
                                         fuse multiple modalities, TokenFusion dynamically detects        language fusion, e.g., VL-BERT [37] and ViLT [17]. In
                                         uninformative tokens and substitutes these tokens with pro-      these methods, vision and language tokens are directly con-
                                         jected and aggregated inter-modal features. Residual posi-       catenated before each transformer layer, making the overall
                                         tional alignment is also adopted to enable explicit utiliza-     architecture very similar to the original transformer. Such
                                         tion of the inter-modal alignments after fusion. The design      fusion is usually alignment-agnostic, which indicates the
                                         of TokenFusion allows the transformer to learn correlations      inter-modal alignments are not explicitly utilized. We also
                                         among multimodal features, while the single-modal trans-         try to apply similar fusion methods on multimodal vision
                                         former architecture remains largely intact. Extensive ex-        tasks (Sec. 4). Unfortunately, this intuitive transformer
                                         periments are conducted on a variety of homogeneous and          fusion cannot bring promising gains or may even result
                                         heterogeneous modalities and demonstrate that TokenFu-           in worse performance than the single-modal counterpart,
                                         sion surpasses state-of-the-art methods in three typical vi-     which is mainly due to the fact that the inter-modal inter-
                                         sion tasks: multimodal image-to-image translation, RGB-          action is not fully exploited. There are also several attempts
                                         depth semantic segmentation, and 3D object detection with        for fusing multiple vision modalities. For example, Trans-
                                         point cloud and images. Our code is available at https:          Fuser [26] leverages transformer modules to connect CNN
                                         //github.com/yikaiw/TokenFusion.                                 backbones of images and LiDAR points. Different from
                                                                                                          exising trials, our work aims to seek an effective and gen-
                                                                                                          eral method to combine multiple single-modal transformers
                                         1. Introduction
                                                                                                          while inserting inter-modal alignments into the models.
                                            Transformer is initially widely studied in the natural lan-      This work benefits the learning process by multimodal
                                         guage community as a non-recurrent sequence model [40]           data while leveraging inter-modal alignments. Such align-
                                         and it is soon extended to benefit vision-language tasks. Re-    ments are naturally available in many vision tasks, e.g., with
                                         cently, numerous studies have further adopted transform-         camera intrinsics/extrinsics, world-space points could be
                                         ers for computer vision tasks with well-adapted architec-        projected and correspond to pixels on the camera plane. Un-
                                         tures and optimization schedules. As a result, vision trans-     like the alignment-agnostic fusion (Sec. 3.1), the alignment-
                                            B Corresponding author: Fuchun Sun.                           aware fusion explicitly involves the alignment relations of
different modalities. Yet, since inter-modal projections are    signs. [2] and [20] process consecutive video frames with
introduced to the transformer, alignment-aware fusion may       transformers for spatial-temporal alignments and capturing
greatly alter the original model structure and data flow,       fine-grained patterns by correlating multiple frames. Re-
which potentially undermines the success of single-modal        garding multimodal data, [26, 41] utilize the dynamic prop-
architecture designs or learned attention during pretrain-      erty of transformer modules to combine CNN backbones
ing. Thus, one may have to determine the “correct” lay-         for fusing infrared/visible images or LiDAR points. [9] ex-
ers/tokens/channels for multimodal projection and fusion,       tends the coarse-to-fine experience from CNN fusion meth-
and also re-design the architecture or re-tune optimization     ods to transformers for image processing tasks. [14] adopts
settings for the new model. To avoid dealing with these         transformers to combine hyperspectral images by the simple
challenging matters and inherit the majority of the origi-      feature concatenation. [24] inserts intermediate tokens be-
nal single-modal design, we propose multimodal token fu-        tween image patches and audio spectrogram patches as bot-
sion, termed TokenFusion, which adaptively and effec-           tlenecks to implicitly learn inter-modal alignments. These
tively fuses multiple single-modal transformers.                works, however, differ from ours since we would like to
   The basic idea of our TokenFusion is to prune multiple       build a general fusion pipeline for combing off-the-rack
single-modal transformers and then re-utilize pruned units      vision transformers without the need of re-designing their
for multimodal fusion. We apply individual pruning to each      structures or re-tuning their optimization settings, while ex-
single-modal transformer and each pruned unit is substi-        plicitly leveraging inter-modal alignment relations.
tuted by projected alignment features from other modalities.
This fusion scheme is assumed to have a limited impact on       3. Methodology
the original single-modal transformers, as it maintains the
                                                                   This part intends to provide a full landscape of the pro-
relative attention relations of the important units. TokenFu-
                                                                posed methodology. We first introduce two naı̈ve multi-
sion also turns out to be superior in allowing multimodal
                                                                modal fusion methods for vision transformers in Sec. 3.1.
transformers to inherit the parameters from single-modal
                                                                Given the limitations of both intuitive methods, we then
pretraining, e.g., on ImageNet.
                                                                propose multimodal token fusion in Sec. 3.2. We elabo-
   To demonstrate the advantage of the proposed method,
                                                                rate the fusion designs for both homogeneous and heteroge-
we consider extensive tasks including multimodal image
                                                                neous modalities to evaluate the effectiveness and generality
translation, RGB-depth semantic segmentation, and 3D ob-
                                                                of our method in Sec. 3.4 and Sec. 3.5, respectively.
ject detection based on images and point clouds, covering
up to four public datasets and seven different modalities.      3.1. Basic Fusion for Vision Transformers
TokenFusion obtains state-of-the-art performance on these
                                                                    Suppose we have the i-th input data x(i) that contains
extensive tasks, demonstrating its great effectiveness and                                     (i)
generality. Specifically, TokenFusion achieves 64.9% and        M modalities: x(i) = {xm ∈ RN ×C }M          m=1 , where N and
70.8% mAP@0.25 for 3D object detection on the challeng-         C denote the number of tokens and input channels respec-
ing SUN RGB-D and ScanNetV2 benchmarks, respectively.           tively. For simplicity, we will omit the subscript (i) in the
                                                                upcoming sections. The goal of deep multimodal fusion is
2. Related Work                                                 to determine a multi-layer model f (x), and its output is ex-
                                                                pected to close to the target y as much as possible. Specif-
    Transformers in computer vision. Transformer is orig-       ically in this work, f (x) is approximated by a transformer-
inally designed for NLP research fields [40], which stack-      based network architecture. Suppose the model contains L
ing multi-head self-attention and feed-forward MLP layers       layers in total, we represent the input token feature of the l-
                                                                                                                   0
to capture the long-term correlation between words. Re-         th layer (l = 1, . . . , L) as el = {elm ∈ RN ×C }M  m=1 , where
cently, vision transformer (ViT) [6] reveals the great poten-   C 0 denotes the number of feature channels of the layer in
tial of transformer-based models in large-scale image clas-     scope. Initially, e1m is obtained using a linear projection of
sification. As a result, transformer has soon achieved pro-     xm , which is a widely adopted approach to vectorize the in-
found impacts in many other computer vision tasks such as       put tokens (e.g. image patches), so that the first transformer
segmentation [44, 47], detection [3, 8, 22, 48], image gener-   layer can accept tokens as input.
ation [16], video processing [20], etc.                             We use different transformers for input modalities and
    Fusion for vision transformers. Deep fusion with mul-       denote fm (x) = eL+1    m    as the final prediction of the m-th
timodal data has been an essential topic which potentially      transformer. Given the token feature elm of the m-th modal-
boosts the performance by leveraging multiple sources of        ity, the l-th layer computes
inputs, and it may also unleash the power of transform-
                                                                     êlm = MSA LN(elm ) , el+1                       l
                                                                                                                        
                                                                                                   m = MLP LN(êm ) ,        (1)
ers further. Yet it is challenging to combine multiple off-
the-rack single transformers while guaranteeing that such       where MSA, MLP, and LN denote the multi-head self-
combination will not impact their elaborate singe-modal de-     attention, multi-layer perception, and layer normalization,
receptively. êlm represents the output of MSA.                       As previously shown in [32], tokens of vision transform-
   During multimodal fusion for vision tasks, the alignment        ers could be pruned in a hierarchical manner while main-
relations of different modalities may be explicitly available.     taining the performance. Similarly, we can select less in-
For example, pixel positions are often used to determine the       formative tokens by adopting a scoring function sl (el ) =
image-depth correlation; and camera intrinsics/extrinsics          MLP(el ) ∈ [0, 1]N , which dynamically predicts the impor-
are important in projecting 3D points to images. Based on          tance of tokens for the l-th layer and the m-th modality. To
the involvement of alignment information, we consider two          enable the back propagation on sl (el ), we re-formulate the
kinds of transformer fusion methods as below.                      MSA output êlm in Eq. (1) as
   Alignment-agnostic fusion does not explicitly use the
                                                                                êlm = MSA LN(elm ) · sl (elm ) .
                                                                                                                
alignment relations among modalities. It expects the align-                                                                  (4)
ment may be implicitly learned from large amount of data.
A common method of the alignment-agnostic fusion is to di-            We use Lm to denote the task-specific loss for the m-th
rectly concatenate multimodal input tokens, which is widely        modality. To prune uninformative tokens, we further add a
applied in vision-language models. Similarly, the input fea-       token-wise pruning loss (an l1 -norm) on sl (elm ). Thus the
ture el for the l-th layer is also the token-wise concatenation    overall loss function for optimization is derived as
                                                                                      M             L
of different modalities. Although the alignment-agnostic                              X             X             
fusion is simple and may have minimal modification to the                       L=          Lm + λ       sl (elm ) ,        (5)
                                                                                     m=1             l=1
original transformer model, it is hard to directly benefit
from the known multimodal alignment relations.                     where λ is a hyper-parameter for balancing different losses.
                                                                                                           0
   Alignment-aware fusion explicitly utilizes inter-modal              For the feature elm ∈ RN ×C , token-wise pruning dy-
alignments. For instance, this can be achieved by selecting        namically detects unimportant tokens from all N tokens.
tokens that correspond to the same pixel or 3D coordinate.         Mutating unimportant tokens or substituting them with
Suppose xm [n] is the n-th token of the m-th modality input        other embeddings are expected to have limited impacts on
xm , where n = 1, · · · , Nm . We define the “token projec-        other informative tokens. We thus propose a token fu-
tion” from the m-th modality to the m0 -th modality as             sion process for multimodal transformers, which substitute
                                                                   unimportant tokens with their token projections (defined in
             ProjTm0 (xm [nm ]) = h(xm0 [nm0 ]),            (2)    Sec. 3.1) from other modalities. Since the pruning process
where h could simply be an identity function (for homoge-          is dynamic, i.e., conditioned on the input features, the fusion
neous modalities) or a shallow multi-layer perception (for         process is also dynamic. This process performs token sub-
heterogeneous modalities). And when considering the en-            stitution before each transformer layer, thus the input fea-
tire N tokens, we can conveniently define the “modality            ture of the l-th layer, i.e., elm , is re-formulated as
projection” as the concatenation of token projections:
                                                                     elm = elm     Isl (elm )≥θ + ProjM    l
                                                                                                      m0 (em )   Isl (elm )<θ , (6)
  ProjM                  T                     T
                                                           
       m0 (xm ) = Projm0 (xm [1]); · · · ; Projm0 (xm [N ]) .
                                                            (3)    where I is an indicator asserting the subscript condition,
    Eq. (3) only depicts the fusion strategy on the input side.    therefore it outputs a mask tensor ∈ {0, 1}N ; the parameter
We can also perform middle-layer or multi-layer fusion             θ is a small threshold (we adopt 10−2 in our experiments);
across different modality-specific models, by projecting and       and the operator resents the element-wise multiplication.
aggregating feature embeddings em which possibly enables               In Eq. (6), if there are only two modalities as input, m0
more diversified and accurate feature interactions. How-           will simply be the other modality other than m. With more
ever, with the growing complexity of transformer-based             than two modalities, we pre-allocate the tokens into M − 1
models, searching for optimal fusion strategies (e.g. layers       parts, each of which is bound with one of the other modal-
and tokens to apply projection and aggregation) for merely         ities than itself. More details of this pre-allocation will be
two modalities (e.g. 2D and 3D detection transformers) can         described in Sec. 3.4.
grow into an extremely hard problem to solve. To tackle
this issue, we propose multimodal token fusion in Sec. 3.2.
                                                                   3.3. Residual Positional Alignment
                                                                      Directly substituting tokens will risk completely under-
3.2. Multimodal Token Fusion
                                                                   mining their original positional information. Hence, the
   As described in Sec. 1, multimodal token fusion (Token-         model can still be ignorant of the alignment of the projected
Fusion) first prunes single-modal transformers and further         features from another modality. To mitigate this problem,
re-utilizes the pruned units for fusion. In this way, the infor-   we adopt Residual Positional Alignment (RPA) that lever-
mative units of original single-modal transformers are as-         ages Positional Embeddings (PEs) for the multimodal align-
sumed to be preserved to a large extent, while multimodal          ment. As depicted in Fig. 1 and Fig. 2 which will be detailed
interactions could be involved for boosting performance.           later, the key idea of RPA lies in injecting equivalent PEs to
                        Residual PEs for alignment after fusion                    group sizes. This pre-allocation is carried out prior to the
                                                                                   commence of training procedure, and the obtained groups

                                              A1

                                                                  A1
            PE1

                                                                        PE1
                                               B1

                                                                   B1
                                                                                   will be fixed throughout the training. We denote the group
                                                                                   allocation as am0 (m) ∈ {0, 1}N , where am0 (m)[n] = 1 in-

                                              A2

                                                                  B2
            PE2

                                                                        PE2
                                               B2

                                                                   B2
                  Multi-Head                                                       dicates that if the n-th token of the m-th modaltity is pruned,

                                              A3

                                                                  A3
            PE3

                                                                        PE3
                  Attention

                                                                                   it will be substituted by the corresponding token of the m0 -

                                                                   A3
                                               B3
                                  FFN
                                                         !"
                                                                                   th modality, otherwise am0 (m)[n] = 0. Having obtained

                                              A4

                                                                  A4
            PE4

                                                                        PE4
                                                                   A4
                                               B4
                                                                                   the pre-allocation strategy for M > 2 modalties, Eq. (6)

                                              A5

                                                                  A5
            PE5

                                                                        PE5
                                               B5

                                                                   B5
                                                                                   can be further developed into a more specific form:
                                              A6

                                                                  B6
            PE6

                                                                        PE6
                                               B6

                                                                   B6
                                                                              ×"
                                                                                      elm = elm       Isl (elm )≥θ
  Patches   PEs   Transformer blocks         Tokens      Token fusion   PEs                   M
                                                                                              X                          M
                                                                                          +           am0 (m)        Projm0 (elm )   Isl (elm )<θ .   (7)
Figure 1. Framework of TokenFusion for homogeneous modalities                                 m0 =1
                                                                                               0
with RGB and depth as an example. Both modalities are sent to a                               m 6=m
shared transformer with also shared positional embeddings.
                                                                                   3.5. Heterogeneous Modalities
subsequent layers. Moreover, the back propagation of PEs                              In this section, we further explore how TokenFusion han-
stops after the first layer, which means only the gradients of                     dles heterogeneous modalities, in which input modalities
PEs at the first layer are retained while for the rest of the                      exhibit quite different data formats and large structural dis-
layers are frozen throughout the training. In this way, PEs                        crepancies, e.g., different number of layers or embedding
serve a purpose of aligning multimodal tokens despite the                          dimensions for the transformer architectures. A concrete
substitution status of the original token. In summary, even                        example would be to learn 3D object detection (based on
if a token is substituted, we still reserve its original PEs that                  point cloud) and 2D object detection (based on images) si-
are added to the projected feature from another modality.                          multaneously with different transformers. Although there
                                                                                   are already specific transformer-based models designed for
3.4. Homogeneous Modalities                                                        3D or 2D object detection respectively, there still lacks a fast
                                                                                   and effective method to combine these models and tasks.
   In the common setup of either a generation task (mul-                              An overall structure of TokenFusion for fusing hetero-
timodal image-to-image translation) or a regression task                           geneous modalities is depicted in Fig. 2. Different from
(RGB-depth semantic segmentation), the homogeneous vi-                             the homogeneous case, we approximate the token projec-
sion modalities x1 , x2 , · · · , xM are typically aligned with                    tion function h in Eq. (2) with a shallow multi-layer per-
pixels, such that the pixels located at the same position                          ception (MLP), since transformers for these heterogeneous
in RGB or depth input should share the same label. We                              modalities may have different hidden embedding dimen-
also expect that such property allows the transformer-based                        sions. For the case of 3D object detection with 3D point
models to benefit from joint learning. Hence, we adopt                             cloud and 2D image, we project each point to the corre-
shared parameters in both MSA and MLP layers for differ-                           sponding image based on camera intrinsics and extrinsics.
ent modalities; yet rely on modality-specific layer normal-                        Likewise, we also project 3D object labels to the images
izations to uncouple the normalization process, since differ-                      for obtaining the corresponding 2D object labels. We train
ent modalities may vary drastically in their statistical means                     two standalone transformers with unshared parameters in
and variances by nature. In this scenario, we simply set                           an end-to-end manner. Regarding the 3D object detection
function h in Eq. (6) as an identity function, and we also let                     with point cloud as input, we follow the architecture used
nm0 = nm , which means we always substitute each pruned                            in Group-Free [22], where Npoint sampled seed points and
token with the token sharing the same position.                                    Kpoint learned proposal points are considered as input to-
   An overall illustration of TokenFusion for fusing homo-                         kens, which are sent to the transformer for predicting Kpoint
geneous modalities is depicted in Fig. 1. Regarding two in-                        3D bounding boxes and object categories. For the 2D object
put modalities, we adopt bi-directional projection and apply                       detection with images as input, we follow the framework in
token-wise pruning on both modalities respectively. Then                           YOLOS [8] which sends Nimg image patches and Kimg ob-
the token substitution process is performed according to                           ject queries to the transformer to predict Kimg 2D bounding
Eq. (6). When there are M > 2 modalities, we also apply                            boxes together with their associated object categories.
the token-wise pruning on all modalities with an additional                           The inter-modal projection maps seed points to image
pre-allocation strategy that selects m0 in based on m accord-                      patches, i.e., an Npoint -to-Nimg mapping. Specifically, the
ing to Eq. (6). To be specific, for the m-th modality, we ran-                     token-wise pruning is applied on the Npoint seed point to-
domly pre-allocate N tokens into M − 1 groups with equal                           kens. Once a certain token obtains a low importance score,
                                                                                 Residual PEs for alignment after fusion
                             Patches

   Image

                                         PE1

                                                                                                                                    PE1
                                                                                                  A1

                                                                                                                             B2

                                                                                                                                     PE1
                                          PE1

                                                                                                                              B1
                                                                                                   B1
                                                                                                                  MLP

                                              PE2

                                                                                                                                         PE2
                                                                                                                             A2
                                                                                                  A2

                                                                                                                                          PE2
                                               PE2

                                                                                                                              B2
                                                                                                   B2
                                                                    Multi-Head
                                                   PE3

                                                                    Attention

                                                                                                                                              PE3
                                                                                                                             A3
                                                                                                  A3

                                                                                                                                               PE3
                                                    PE3
 Point cloud
                                                                                                                                                               …

                                                                                                                              A5
                                                                                                   B3
                                                                                    FFN

                                                                                                                                                                    FFN
                                                                                                              !" Proj

                                                        PE4

                                                                                                                                                   PE4
                                                                                                                             A4
                                                                                                  A4

                                                                                                                                                    PE4
                                                         PE4

                                                                                                                              B4
                                                                                                   B4
                Sampling                                                                                          MLP

                                                             PE5

                                                                                                                                                        PE5
                                                                                                                             A5
                                                                                                  A5
                Backbone

                                                                                                                                                         PE5
                                                              PE5

                                                                                                                              A4
                                                                                                   B5
  Sampled

                                                                                                                                               PE6
                                                    PE6

                                                                                                                               A2
                                                                                                    B6
 point cloud                                                                                                                                                   ×"
                                   Points PEs                           Transformer blocks        Tokens             Token fusion        PEs

Figure 2. Framework of TokenFusion for heterogeneous modalities with point clouds and images. Both modalities are sent to individual
transformer modules with also individual positional embeddings. Additional inter-modal projections (Proj) are needed which is different
from the fusion for homogeneous modalities.

we project the 3D coordinate of this token to a 2D pixel on                                           ings. Taskonomy provides over 10 multimodal representa-
the corresponding image input. It is now viable to locate                                             tions in addition to each RGB image, such as depth (eu-
the specific image patch based on the 2D pixel. Suppose                                               clidean or z-buffering), normal, shade, texture, edge, prin-
this projection obtains the nimg -th image patch based on the                                         cipal curvature, etc. The resolution of each representation
npoint -th seed point which is pruned. We substitute m and                                            is 512 × 512. To facilitate comparison with the existing fu-
m0 in Eq. (2) with the subscripts “point” and “img” respec-                                           sion methods, we adopt the same sampling strategy as [42],
tively, i.e., ProjTimg (xpoint [npoint ]) = h(ximg [nimg ]). Thus                                     resulting in 1,000 high-quality multimodal images for train-
the relation between npoint and nimg captured by the token                                            ing, and 500 for validation.
projection satisfies                                                                                      Our implementation contains two transformers as the
           >                                         >                                            generator and discriminator respectively. We provide con-
     u, v, z = K · Rt · xnpoint , ynpoint , znpoint , 1 ,                                 (8)         figuration details in our supplementary materials. The reso-
                  j bv/zc k j W k j bu/zc k                                                           lution of the generator/discriminator input or the generator
           nimg =           ×      +                  ,                                   (9)         prediction is 256 × 256. We adopt two kinds of architec-
                      P       P              P
                                                                                                      ture settings, the tiny (Ti) version with 10 layers and the
where K ∈ R4×4 and Rt ∈ R4×4 are camera intrinsic                                                     small (S) version with 20 layers, and both settings are only
and extrinsic matrices, respectively; [xnpoint , ynpoint , znpoint ]                                  different in layer numbers. The learning rates of both trans-
denotes the 3D coordinate of the npoint -th
                                           point; u, v, z are                                        formers are set to 2 × 10−4 . We adopt overlapped patches
temporary variables with bu/zc, bv/zc actually being the                                              in both transformers inspired by [44].
projected pixel coordinate of the image; P is the patch size                                              In our experiments for this task, we adopt shared trans-
of the vision transformer and W denotes the image width.                                              formers for all input modalities with individual layer nor-
                                                                                                      malizations (LNs) that individually compute the means and
4. Experiments                                                                                        variances of different modalities. Specifically, parameters
    To evaluate the effectiveness of the proposed TokenFu-                                            in the linear projection on patches, all linear projections
sion, we conduct comprehensive experiments towards both                                               (e.g. for key, queries, etc) in MSA, and MLP are shared
homogeneous and heterogeneous modalities with state-of-                                               for different modalities. Such a mechanism largely reduces
the-art (SOTA) methods. Experiments are conducted on to-                                              the total model size which as discussed in the supplemen-
tally seven different modalities and four application scenar-                                         tary materials, even achieves better performance than using
ios, implemented with PyTorch [25] and MindSpore [15].                                                individual transformers. In addition, we also adopt shared
                                                                                                      positional embeddings for different modalities. We let the
4.1. Multimodal Image-to-Image Translation                                                            sparsity weight λ = 10−4 in Eq. (10) and the threshold
    The task of multimodal image-to-image translation aims                                            θ = 2 × 10−2 in Eq. (7) for all these experiments.
at generating a target image modality based on different im-                                              Our evaluation metrics include FID/KID for RGB pre-
age modalities as input (e.g. Normal+Depth→RGB). We                                                   dictions and MAE/MSE for other predictions. These met-
evaluate TokenFusion in this task using the Taskonomy [45]                                            rics are introduced in the supplementary materials.
dataset, which is a large-scale indoor scene dataset contain-                                             Results. In Table 1, we provide comparisons with ex-
ing about 4 million indoor images captured from 600 build-                                            tensive baseline methods and a SOTA method [42] with the
                                             Single-modal output                                  Multimodal output

                                    Transformer output Transformer output   State-of-the-art Transformer fusion Transformer fusion
        Input-1         Input-2                                                                                                          Ground truth
                                     from input-1 only  from input-2 only CNN fusion by CEN by feature concat    by TokenFusion

Figure 3. Comparison on the validation data split for image-to-image translation (Texture+Shade→RGB). The resolution of all input/output
images is 256×256. The third/forth column is predicted by the single modality, and the following three columns are predicted by CEN [42],
the intuitive transformer fusion by feature concatenation, and our TokenFusion, respectively. Best view in color and zoom in.

                                                                                                  Shade+Texture Depth+Normal RGB+Shade RGB+Normal RGB+Edge
same data settings. All methods adopt the learned ensem-                      Method
                                                                                                    →RGB          →RGB        →Normal   →Shade     →Depth
ble over the two predictions which are corresponded to the                                                   CNN-based models
two modality branches. In addition, all predictions have the                 Concat [42]           78.82/3.13 99.08/4.28 1.34/2.85    1.28/2.02 0.33/0.75
same resolution 256×256 for a fair comparison. Since most                    Self-Att. [39, 42]    73.87/2.46 96.73/3.95 1.26/2.76    1.18/1.76 0.30/0.70
                                                                             Align. [36, 42]       92.30/4.20 105.03/4.91 1.52/3.25   1.41/2.21 0.45/0.90
existing methods are based on CNNs, we further provide                       CEN [42]              62.63/1.65 84.33/2.70 1.12/2.51    1.10/1.72 0.28/0.66
two baselines for transformer-based models including the                                                  Transformer-based models
baseline without feature fusion (only uses ensemble for the                  Concat (Ti)           76.13/2.85 102.70/4.74 1.52/3.15   1.33/2.20 0.40/0.83
                                                                             Ours (Ti)             50.40/1.03 76.35/2.19 0.73/1.83    0.95/1.54 0.21/0.57
late fusion) and the feature fusion method. By comparison,                   Concat (S)            72.55/2.39 96.04/4.09 1.18/2.73    1.30/2.07 0.35/0.68
our TokenFusion surpasses all the other methods with large                   Ours (S)              43.92/0.94 70.13/1.92 0.58/1.51    0.79/1.33 0.16/0.47
margins. For example, in the Shade+Texture→RGB task,                        Table 1. Results on Taskonomy for multimodal image-to-image
our TokenFusion (S) achieves 43.92/0.94 FID/KID scores,                     translation. Evaluation metrics are FID/KID (×10−2 ) for RGB
remarkably better than the current SOTA method CEN [42]                     predictions and MAE (×10−1 )/MSE (×10−1 ) for other predic-
with 29.8% relative FID metric decrease.                                    tions. Lower values indicate better performance for all the metrics.
    In supplementary materials, we consider more modality
inputs up to 4 which evaluates our group allocation strategy.
    Visualization and analysis. We provide qualitative re-                  795/654 images for train/test splits to predict the standard
sults in Fig. 3, where we choose tough samples for com-                     40 classes [10]. SUN RGB-D is one of the most challeng-
parison. The predictions with our TokenFusion obtain bet-                   ing large-scale indoor datasets, and we adopt the standard
ter natural patterns and are also richer in colors and details.             5,285/5,050 images for train/test of 37 semantic classes.
In Fig. 4, we further visualize the process of TokenFusion                      Our models include TokenFusion (tiny) and TokenFu-
of which tokens are learned to be fused under our l1 spar-                  sion (small), of which the single-modal backbones follow
sity constraints. We observe that the tokens for fusion fol-                B2 and B3 settings of SegFormer [44]. Both tiny and small
low specific regularities. For example, the texture modality                versions adopt the pretrained parameters on ImageNet-1k
tends to preserve its advantage of detailed boundaries, and                 for initialization following [44]. Similar to our implemen-
meanwhile seek facial tokens from the shade modality. In                    tation in Sec. 4.1, we also adopt shared transformers and
this sense, TokenFusion combines complementary proper-                      positional embeddings for RGB and depth inputs with indi-
ties of different modalities.                                               vidual LNs. We let the sparsity weight λ = 10−3 in Eq. (10)
                                                                            and the threshold θ = 2 × 10−2 in Eq. (7) for all these ex-
4.2. RGB-Depth Semantic Segmentation                                        periments.
   We then evaluate TokenFusion on another homogeneous                         Results. Results provided in Table 2 conclude that cur-
scenario, semantic segmentation with RGB and depth as in-                   rent transformer-based models equipped with our Token-
put, which is a very common multimodal task and numerous                    Fusion surpass SOTA models using CNNs. Note that we
methods have been proposed towards better performance.                      choose relatively light backbone settings (B1 and B2 as
We choose the typical indoor datasets, NYUDv2 [33] and                      mentioned in Sec. 4.2). We expect that using larger back-
SUN RGB-D [34]. For NYUDv2, we follow the standard                          bones (e.g., B5) would yield better performance.
                            Fused tokens      Fused tokens                  Fused tokens         Fused tokens    Multimodal output
         Input-1                                                 Input-2                                                                Groud truth
                              (stage 1)         (stage 2)                     (stage 1)            (stage 2)     by TokenFusion

Figure 4. Illustrations of which tokens are fused in our TokenFusion, performed on the validation data split. We provide two cases including
Texture+Shade→RGB (first row) and Shade+RGB→Normal (second row). The resolution of all images is 256 × 256. We choose the last
layers in the first and second transformer stages respectively. Best view in color and zoom in.
          2D prediction               2D prediction                             3D prediction              3D prediction
         w/o TokenFusion            with TokenFusion         Ground Truth      w/o TokenFusion           with TokenFusion            Ground Truth

Figure 5. Results visualization on the validation data split for heterogeneous modalities including point clouds and images, where 3D
object detection and 2D object detection are learned simultaneously. We compare the performance without (w/o) or with our TokenFusion.
Our TokenFusion mainly benefits 3D object detection results.

Method             Inputs
                               NYUDv2               SUN RGB-D               has received great attention. We leverage 3D point clouds
                       Pixel Acc. mAcc. mIoU Pixel Acc. mAcc. mIoU
                        CNN-based models
                                                                            and 2D images to learn 3D and 2D detections, respectively,
FCN-32s [23]     RGB      60.0     42.2 29.2    68.4     41.1 29.0          and both processes are learned simultaneously. We expect
RefineNet [19]   RGB      74.4     59.6 47.6    81.1     57.7 47.0          the involvement of 2D learning boosts the 3D counterpart.
FuseNet [12]    RGB+D     68.1     50.4 37.9    76.3     48.3 37.3
SSMA [39]       RGB+D     75.2     60.5 48.7    81.0     58.1 45.7             We adopt SUN RGB-D [35] and ScanNetV2 [5] datasets.
RDFNet [18]     RGB+D     76.0     62.8 50.1    81.5     60.1 47.7
AsymFusion [43] RGB+D     77.0     64.0 51.2      -       -     -
                                                                            For SUN RGB-D, we follow the same train/test splits as in
CEN [42]        RGB+D     77.7     65.0 52.5    83.5     63.2 51.1          Sec. 4.2 and detect the 10 most common classes. For Scan-
                     Transformer-based models                               NetV2, we adopt the 1,201/312 scans as train/test splits to
w/o fusion (Ti)  RGB      75.2     62.5 49.7    82.3     60.6 47.0
Concat (Ti)     RGB+D     76.5     63.4 50.8    82.8     61.4 47.9          detect the 18 object classes. All these settings (splits and de-
Ours (Ti)       RGB+D     78.6     66.2 53.3    84.0     63.3 51.4          tected target classes) follow current works [22, 28] for a fair
w/o fusion (S)   RGB      76.0     63.0 50.6    82.9     61.3 48.1
Concat (S)      RGB+D     77.1     63.8 51.4    83.5     62.0 49.0          comparison. Note that different from SUN RGB-D, Scan-
Ours (S)        RGB+D     79.0     66.9 54.2    84.7     64.1 53.0          NetV2 provides multi-view images for each scene alongside
Table 2. Comparison results on the NYUDv2 and SUN RGB-D                     the point cloud. We randomly sample 10 frames per scene
datasets with SOTAs for RGB and depth (D) semantic segmenta-                from the scannet-frames-25k samples provided in [5].
tion. Evaluation metrics include pixel accuracy (Pixel Acc.) (%),              Our architectures for 3D detection and 2D detection fol-
mean accuracy (mAcc.) (%), and mean IoU (mIoU) (%).                         low GF [22] and YOLOS [8], respectively. We adopt the
                                                                            “L6, O256” or “L12, O512” versions of GF for the 3D de-
                                                                            tection branch. We combine GF with the tiny (Ti) and small
4.3. Vision and Point Cloud 3D Object Detection
                                                                            (S) versions of YOLOS, respectively, and adopt mAP@0.25
  We further apply TokenFusion for fusing heterogeneous                     and mAP@0.5 as evaluation metrics following [22, 28].
modalities, specifically, the 3D object detection task which                   Results. We provide results comparison in Table 3 and
 Method              Backbone      Inputs    mAP@0.25 mAP@0.5           Method                 Backbone       Inputs   mAP@0.25 mAP@0.5
                        CNN-based models                                                         CNN-based models
VoteNet [29]        PointNet++     Points       59.1        35.8       HGNet [4]                GU-net        Points      61.3        34.4
VoteNet [29]*       PointNet++ Points+RGB       58.0        34.3       GSDN [11]               MinkNet        Points      62.8        34.8
MLCVNet [31]        PointNet++     Points       59.8          -        3D-MPA [7]              MinkNet        Points      64.2        49.2
HGNet [4]             GU-net       Points       60.1        39.0       VoteNet [29]           PointNet++      Points      62.9        39.9
H3DNet [46]        4×PointNet++    Points       61.6          -        MLCVNet [31]           PointNet++      Points      64.5        41.4
imVoteNet [27]      PointNet++ Points+RGB       63.4          -        H3DNet [46]            PointNet++      Points      64.4        43.4
                    Transformer-based models                           H3DNet [46]           4×PointNet++     Points      67.2        48.1
GF [22] (L6, O256) PointNet++      Points    63.0 (62.6) 45.2 (44.4)                          Transformer-based models
GF [22] (L6, O256)* PointNet++ Points+RGB 62.1 (61.0) 42.7 (41.9)      GF [22] (L6, O256)     PointNet++      Points   67.3 (66.3) 48.9 (48.5)
Ours (L6, O256; Ti) PointNet++ Points+RGB 64.5 (64.2) 47.8 (47.3)      GF [22] (L6, O256)*    PointNet++ Points+RGB 66.3 (65.7) 47.5 (47.0)
Ours (L6, O256; S)  PointNet++ Points+RGB 64.9 (64.4) 48.3 (47.7)      GF [22] (L12, O512) PointNet++w2× Points        69.1 (68.6) 52.8 (51.8)
                                                                       GF [22] (L12, O512)* PointNet++w2× Points+RGB 68.2 (67.6) 50.3 (49.4)
Table 3. Comparison on SUN RGB-D with SOTAs for 3D object              Ours (L6, O256; Ti)    PointNet++ Points+RGB 68.8 (68.0) 51.9 (51.2)
                                                                       Ours (L12, O512; S) PointNet++w2× Points+RGB 70.8 (69.8) 54.2 (53.6)
detection, including best results and average results in brackets. *
indicates appending RGB to the points as described in Sec. 4.3.        Table 4. Comparison on ScanNetV2 with SOTAs for 3D object
                                                                       detection, including best results and average results in brackets.
Table 4. The main comparison is based on the best results                                         Seg. (NYUDv2)     3D det. (SUN RGB-D)
                                                                       l1 -norm Fusion strategy
of five experiments between different methods, and num-                                       Pixel Acc. mAcc. mIoU mAP@0.25 mAP@0.5
                                                                          ×           ×          75.2     62.5 49.7    62.8       45.1
bers within the brackets are the average results. Besides, we
                                                                          ×      Random (10%)    75.6     63.0 50.1    62.3       44.5
perform intuitive multimodal experiments by appending the                 ×      Random (30%)    74.2     61.0 48.2    59.5       42.4
3-channel RGB vectors to the sampled points after Point-                  X           ×          75.0     62.5 49.5    62.6       44.9
Net++ [30]. Such intuitive experiments are marked by the                  X       X(with RPA)    78.6     66.2 53.3    64.9       48.3

subscript * in both tables. We observe, however, that simply           Table 5. Effectiveness of l1 -norm and token fusion. Experiments
appending RGB information even leads to the performance                include RGB-depth segmentation (seg.) on NYUDv2 and 3D de-
drop, indicating the difficulty of such a heterogeneous fu-            tection (det.) with images and points on SUN RGB-D.
sion task. By comparison, our TokenFusion achieves new
records on both datasets, which are remarkably superior to               Token fusion
                                                                                        RPA
                                                                                                   Seg. (NYUDv2)    3D det. (SUN RGB-D)
                                                                        (with l1 -norm)       Pixel Acc. mAcc. mIoU mAP@0.25 mAP@0.5
previous CNN/transformer models in terms of both metrics.
                                                                               ×         ×       75.2     62.5 49.7   62.8        45.1
For example, with TokenFusion, YOLOS-Ti can be utilized                        ×         X       75.7     62.9 50.3   63.0        45.3
to boost the performance of GF by further 2.4 mAP@0.25                         X         ×       78.3     65.8 52.9   63.6        46.2
                                                                               X         X       78.6     66.2 53.3   64.9        48.3
improvements, and using YOLOS-S brings further gains.
   Visualizations. Fig. 5 illustrates the comparison of de-            Table 6. Effectiveness of RPA proposed in Sec. 3.4. Experimental
tection results when using TokenFusion for multimodal in-              tasks and datasets follow Table 5.
teractions against individual learning. We observe that To-
kenFusion benefits the 3D detection part. For example, with
the help of images, models with TokenFusion can locate 3D              6. Conclusion
objects even with sparse or missing point data (second row).              We propose TokenFusion, an adaptive method gener-
In addition, using images also benefits when the points of             ally applicable for fusing vision transformers with homo-
two objects are largely overlapped (first row). These obser-           geneous or heterogeneous modalities. TokenFusion ex-
vations demonstrate the advantages of our TokenFusion.                 ploits uninformative tokens and re-utilizes these tokens to
                                                                       strengthen the interaction of other informative multimodal
5. Ablation Study                                                      tokens. Alignment relations of different modalities can be
                                                                       explicitly utilized due to our residual positional alignment
    l1 -norm and token fusion. In Table 5, we demonstrate
                                                                       and inter-modal projection. TokenFusion surpasses state-
the advantages of l1 -norm and token fusion. We addition-
                                                                       of-the-art methods on a variety of tasks, demonstrating its
ally conduct experiments with random token fusion. We
                                                                       superiority and generality for multimodal fusion.
observe that applying l1 -norm itself has little effect on the
performance yet it is essential to reveal tokens for fusion.
                                                                       Acknowledgement
Our token fusion together with l1 -norm achieves much bet-
ter performance than the random fusion baselines.                         This work is funded by Major Project of the New Gen-
    Evaluation of RPA. Table 6 evaluates RPA proposed in               eration of Artificial Intelligence (No. 2018AAA0102900)
Sec. 3.3. Results indicate that only using RPA without token           and the Sino-German Collaborative Research Project Cross-
fusion does not noticeably affect the performance, but is              modal Learning (NSFC 62061136001/DFG TRR169). We
important when combined with the token fusion process for              gratefully acknowledge the support of MindSpore, CANN
alignments, especially for the 3D detection task.                      and Ascend AI Processor used for this research.
Appendix                                                                 MSA&MLP         LN
                                                                                                    Image translation    Seg. (NYUDv2)
                                                                                                   FID KID (×10−2 ) Pixel Acc. mAcc. mIoU
                                                                          Unshared     Unshared   49.73       1.06     78.3     65.6 52.9
A. Additional Results                                                      Shared       Shared    67.45       1.82     76.7     63.8 52.0
                                                                           Shared      Unshared   43.92       0.94     78.6     66.2 53.3
    Multiple input modalities. In Table 7, we further eval-
uate our TokenFusion with more modality inputs from 1 to                Table 8. Results comparison when using different network sharing
4. When the number of input modalities is larger than 2, we             schemes for image-to-image translation (Shade+Texture→RGB)
adopt the group allocation strategy as proposed in Sec. 3.4             on Taskonomy and RGB-depth segmentation (seg.) on NYUDv2.
                                                                        Lower FID or KID values indicate better performance.
of our main paper. By comparison, the performance is con-
sistently improved when using more modalities, and Token-                                                              Seg. (NYUDv2)
Fusion is again noticeably better than CEN [42], suggesting               Token-wise       Channel-wise
                                                                                                               Pixel Acc.     mAcc.  mIoU
the ability to absorb information from more modalities.                        ×                  ×               75.2         62.5  49.7
                                                                               X                  ×               78.6         66.2  53.3
 Modality                      CEN [42]      Ours (Ti)      Ours (S)           ×                  X               77.2         65.0  52.1
                                                                               X                  X               78.8         66.6  53.8
 Depth                        113.91/5.68   108.16/5.50    97.13/4.97
 Normal                       108.20/5.42   112.25/5.77   100.29/5.02
 Texture                       97.51/4.82    99.70/5.14    94.92/4.38   Table 9. RGB-depth segmentation results on the NYUDv2 dataset
 Shade                        100.96/5.17   104.73/5.43    97.35/4.77   when combining our TokenFusion with the channel-wise fusion.
 Depth+Normal                  84.33/2.70    71.82/2.36    64.20/1.69
 Depth+Normal+Texture          60.90/1.56    53.17/1.22    42.54/0.93    Input image                         3D det. (ScanNetV2)     Seconds per
                                                                                           Model
 Depth+Normal+Texture+Shade    57.19/1.33    47.69/1.01    39.15/0.81      frames                           mAP@0.25 mAP@0.5         100 scenes
                                                                              0      Ours (L6, O256; Ti)      67.3         49.0          4.7
Table 7. Results on the Taskonomy dataset for multimodal image-               5      Ours (L6, O256; Ti)      67.9         50.5          5.9
                                                                             10      Ours (L6, O256; Ti)      68.8         51.9          7.0
to-image translation (to RGB) with 1 ∼ 4 modalities.
                                                                        Table 10. Comparison of practical inference speed on ScanNetV2.
    Network sharing. As mentioned in Sec. 3.4 of our main
paper, we adopt shared parameters in both Multi-head Self-
Attention (MSA) and Multi-Layer Perception (MLP) for the                age the scaling factors γ of layer normalization (LN) to per-
fusion with homogeneous modalities, and rely on modality-               form channel-wise pruning, and apply sparsity constraints
specific Layer Normalization (LN) layers to uncouple the                on γ. LN in transformers performs normalization on its in-
normalization process. Such network sharing technique is                put xm,l .
evaluated by our experiments including multimodal image-                   To prune uninformative
                                                                                      PM PL channels,           we add a channel-wise
                                                                                                       l
to-image translation (in Sec. 4.1) and RGB-depth seman-                 pruning loss m=1 l=1 |γm         | to the main loss in Eq. (5)
tic segmentation (in Sec. 4.2), which largely reduces the               (main paper). The overall loss function is
model size, and also enables the reuse of attention weights                     M                    L                      L          
for different modalities. In Table 8, we further conduct abla-
                                                                                X                     X                      X
                                                                          L=            Lm + λ1             sl (elm ) + λ2           l
                                                                                                                                   |γm | , (10)
tion studies to demonstrate the effectiveness of our network                    m=1                   l=1                    l=1
sharing scheme. Fortunately, the comparison indicates that
our default setting (i.e., Shared MSA and MLP, individual               where λ1 , λ2 are hyper-parameters for balancing different
                                                                                  l
LN) achieves a win-win scenario: apart from the advan-                  losses; γm   is a vector with the length C, representing the
tage on storage efficiency, also achieves better results than           scaling factor of LN at the l-th layer of the m-th modality.
using individual MSA and MLP on both tasks. Note that                      We let λ1 = λ2 = 10−3 for RGB-depth segmentation
further sharing LN layers leads to the performance drop,                experiments. Results provided in Table 9 demonstrate that
especially on the image-to-image translation task. In addi-             our TokenFusion can be combined with the channel-wise
tion, we adopt shared Positional Embeddings (PEs) by de-                fusion to obtain a further improved performance. For ex-
fault for the fusion with homogeneous modalities, and we                ample, the segmentation on NYUDv2 with both token-wise
observe that sharing/unsharing PEs can achieve comparable               and channel-wise fusion achieves an additional 0.5 mIoU
performance in practice.                                                gain than TokenFusion. More detailed studies of such com-
    Combining TokenFusion with channel-wise fusion.                     bined framework, the relation between the overall pruning
Our TokenFusion detects uninformative tokens and re-                    rate and fusion performance gain, and the extension to fuse
utilizes these tokens for multimodal fusion. We may fur-                heterogeneous modalities are left to be the future works.
ther combine TokenFusion with an orthogonal method by                      Additional visualizations. In Fig. 6, we provide an-
channel-wise pruning which automatically detects uninfor-               other group of visualizations that depict the fused tokens
mative channels. Different from the token-wise fusion                   under the l1 sparsity constraints during training. We ob-
method in TokenFusion, the channel-wise fusion is not con-              serve that fused tokens follow the regularities mentioned in
ditional on input features. Inspired by CEN [42], we lever-             our main paper, e.g., the texture modality preserves its ad-
                       Fused tokens     Fused tokens                      Fused tokens    Fused tokens   Multimodal output
        Input-1                                            Input-2                                                           Groud truth
                         (stage 1)        (stage 2)                         (stage 1)       (stage 2)    by TokenFusion

Figure 6. Additional illustrations of the token fusion process as a supplement to Fig. 4 (main paper), performed on the validation data split
of Taskonomy. We provide two cases: Texture+Shade→RGB (first row) and Shade+RGB→Normal (second row). The resolution of all
images is 256 × 256. We choose the last layers in the first and second transformer stages respectively. Best view in color and zoom in.

vantage at boundaries while seeking facial tokens from the               reliable especially when there are much more inception fea-
shade modality.                                                          tures channels than image numbers. Lower KID indicates
   Inference speed. In Table 10, we test the real inference              more visual similarity between real and generated images.
speed (single V100, 256G RAM) with different numbers                     Regarding our implementation of KID, the hidden represen-
of input frames for 3D detection. We observe that addi-                  tations are derived from the Inception-v3 [38] pool3 layer.
tional time costs are mild, which is partly because the added
YOLOS-Ti is a light model (with only three multi-heads).                 References
                                                                           [1] Mikolaj Binkowski, Dougal J. Sutherland, Michael Arbel,
B. More Details of Image Translation                                           and Arthur Gretton. Demystifying MMD gans. In ICLR,
                                                                               2018. 10
   In this part, we discuss the implementation details for our
                                                                           [2] Aljaz Bozic, Pablo R. Palafox, Justus Thies, Angela Dai,
image-to-image translation task. Our implementation con-
                                                                               and Matthias Nießner. Transformerfusion: Monocular RGB
tains two transformers as the generator and discriminator re-                  scene reconstruction using transformers. In NeurIPS, 2021.
spectively. The resolution of the generator/discriminator in-                  2
put or the generator prediction is 256×256. Specifically, the              [3] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas
discriminator of our model is similar to [16], which adopts                    Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-
five stages with two layers for each, where the embedding                      end object detection with transformers. In ECCV, 2020. 1,
dimensions and head numbers gradually double from 32 to                        2
512 and from 1 to 16 respectively. The generator is com-                   [4] Jintai Chen, Biwen Lei, Qingyu Song, Haochao Ying,
posed of nine stages where the first five have the same con-                   Danny Z Chen, and Jian Wu. A hierarchical graph network
figurations with the discriminator, and the last four stages                   for 3d object detection on point clouds. In CVPR, 2020. 8
have reverse configurations of its first four stages.                      [5] Angela Dai, Angel X. Chang, Manolis Savva, Maciej Hal-
   We adopt four kinds of evaluation metrics including                         ber, Thomas A. Funkhouser, and Matthias Nießner. Scan-
Mean Square Error (MSE), Mean Absolute Error (MAE),                            net: Richly-annotated 3d reconstructions of indoor scenes.
Fréchet-Inception-Distance (FID), and Kernel-Inception-                       In CVPR, 2017. 7
Distance (KID). Here we briefly introduce FID and KID                      [6] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
scores. FID, proposed by [13], contrasts the statistics of                     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
                                                                               Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
generated samples against real samples. The FID fits a
                                                                               vain Gelly, et al. An image is worth 16x16 words: Trans-
Gaussian distribution to the hidden activations of Inception-                  formers for image recognition at scale. In ICLR, 2020. 1,
Net for each compared image set and then computes the                          2
Fréchet distance (also known as the Wasserstein-2 distance)               [7] Francis Engelmann, Martin Bokeloh, Alireza Fathi, Bastian
between those Gaussians. Lower FID is better, correspond-                      Leibe, and Matthias Nießner. 3d-mpa: Multi-proposal ag-
ing to generated images more similar to the real. KID, de-                     gregation for 3d semantic instance segmentation. In CVPR,
veloped by [1], is a metric similar to the FID but uses the                    2020. 8
squared Maximum-Mean-Discrepancy (MMD) between In-                         [8] Yuxin Fang, Bencheng Liao, Xinggang Wang, Jiemin Fang,
ception representations with a polynomial kernel. Unlike                       Jiyang Qi, Rui Wu, Jianwei Niu, and Wenyu Liu. You
FID, KID has a simple unbiased estimator, making it more                       only look at one sequence: Rethinking transformer in vision
     through object detection. arXiv preprint arXiv:2106.00666,          Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison,
     2021. 1, 2, 4, 7                                                    Andreas Köpf, Edward Yang, Zachary DeVito, Martin Rai-
 [9] Yu Fu, TianYang Xu, XiaoJun Wu, and Josef Kittler. Ppt              son, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner,
     fusion: Pyramid patch transformerfor a case study in image          Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An
     fusion. arXiv preprint arXiv:2107.13967, 2021. 2                    imperative style, high-performance deep learning library. In
[10] Saurabh Gupta, Pablo Arbelaez, and Jitendra Malik. Per-             NeurIPS, 2019. 5
     ceptual organization and recognition of indoor scenes from     [26] Aditya Prakash, Kashyap Chitta, and Andreas Geiger. Multi-
     RGB-D images. In CVPR, 2013. 6                                      modal fusion transformer for end-to-end autonomous driv-
[11] JunYoung Gwak, Christopher Choy, and Silvio Savarese.               ing. In CVPR, 2021. 1, 2
     Generative sparse detection networks for 3d single-shot ob-    [27] Charles R Qi, Xinlei Chen, Or Litany, and Leonidas J
     ject detection. arXiv preprint arXiv:2006.12356, 2020. 8            Guibas. Imvotenet: Boosting 3d object detection in point
[12] Caner Hazirbas, Lingni Ma, Csaba Domokos, and Daniel                clouds with image votes. In CVPR, 2020. 8
     Cremers. Fusenet: Incorporating depth into semantic seg-       [28] Charles R Qi, Or Litany, Kaiming He, and Leonidas J
     mentation via fusion-based CNN architecture. In ACCV,               Guibas. Deep hough voting for 3d object detection in point
     2016. 7                                                             clouds. In Proceedings of the IEEE/CVF International Con-
[13] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner,                 ference on Computer Vision, pages 9277–9286, 2019. 7
     Bernhard Nessler, and Sepp Hochreiter. Gans trained by a       [29] Charles R Qi, Or Litany, Kaiming He, and Leonidas J
     two time-scale update rule converge to a local nash equilib-        Guibas. Deep hough voting for 3d object detection in point
     rium. In NIPS, 2017. 10                                             clouds. In ICCV, 2019. 8
[14] Jin-Fan Hu, Ting-Zhu Huang, and Liang-Jian Deng.               [30] Charles R Qi, Li Yi, Hao Su, and Leonidas J. Guibas. Point-
     Fusformer: A transformer-based fusion approach for                  net++: Deep hierarchical feature learning on point sets in a
     hyperspectral image super-resolution.       arXiv preprint          metric space. In NIPS, 2017. 8
     arXiv:2109.02079, 2021. 2                                      [31] Xie Qian, Lai Yu-kun, Wu Jing, Wang Zhoutao, Zhang Yim-
                                                                         ing, Xu Kai, and Wang Jun. Mlcvnet: Multi-level context
[15] Huawei. Mindspore. https://www.mindspore.cn/,
                                                                         votenet for 3d object detection. In CVPR, 2020. 8
     2020. 5
                                                                    [32] Yongming Rao, Wenliang Zhao, Benlin Liu, Jiwen Lu, Jie
[16] Yifan Jiang, Shiyu Chang, and Zhangyang Wang. Transgan:
                                                                         Zhou, and Cho-Jui Hsieh. Dynamicvit: Efficient vision
     Two pure transformers can make one strong gan, and that can
                                                                         transformers with dynamic token sparsification. In NeurIPS,
     scale up. In NeurIPS, 2021. 1, 2, 10
                                                                         2021. 3
[17] Wonjae Kim, Bokyung Son, and Ildoo Kim. Vilt: Vision-
                                                                    [33] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
     and-language transformer without convolution or region su-
                                                                         Fergus. Indoor segmentation and support inference from
     pervision. arXiv preprint arXiv:2102.03334, 2021. 1
                                                                         RGBD images. In ECCV, 2012. 6
[18] Seungyong Lee, Seong-Jin Park, and Ki-Sang Hong. Rdfnet:       [34] Shuran Song, Samuel P. Lichtenberg, and Jianxiong Xiao.
     RGB-D multi-level residual feature fusion for indoor seman-         SUN RGB-D: A RGB-D scene understanding benchmark
     tic segmentation. In ICCV, 2017. 7                                  suite. In CVPR, 2015. 6
[19] Guosheng Lin, Fayao Liu, Anton Milan, Chunhua Shen, and        [35] Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao.
     Ian Reid. Refinenet: Multi-path refinement networks for             Sun rgb-d: A rgb-d scene understanding benchmark suite. In
     dense prediction. In IEEE Trans. PAMI, 2019. 7                      CVPR, 2015. 7
[20] Rui Liu, Hanming Deng, Yangyi Huang, Xiaoyu Shi, Lewei         [36] Sijie Song, Jiaying Liu, Yanghao Li, and Zongming Guo.
     Lu, Wenxiu Sun, Xiaogang Wang, Jifeng Dai, and Hong-                Modality compensation network: Cross-modal adaptation
     sheng Li. Fuseformer: Fusing fine-grained information in            for action recognition. In IEEE Trans. Image Process., 2020.
     transformers for video inpainting. In ICCV, 2021. 2                 6
[21] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei,               [37] Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu, Furu
     Zheng Zhang, Stephen Lin, and Baining Guo. Swin trans-              Wei, and Jifeng Dai. Vl-bert: Pre-training of generic visual-
     former: Hierarchical vision transformer using shifted win-          linguistic representations. In ICLR, 2019. 1
     dows. arXiv preprint arXiv:2103.14030, 2021. 1                 [38] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe,
[22] Ze Liu, Zheng Zhang, Yue Cao, Han Hu, and Xin Tong.                 Jonathon Shlens, and Zbigniew Wojna. Rethinking the in-
     Group-free 3d object detection via transformers. In ICCV,           ception architecture for computer vision. In CVPR, 2016.
     2021. 1, 2, 4, 7, 8                                                 10
[23] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully       [39] Abhinav Valada, Rohit Mohan, and Wolfram Burgard. Self-
     convolutional networks for semantic segmentation. In                supervised model adaptation for multimodal semantic seg-
     CVPR, 2015. 7                                                       mentation. In IJCV, 2020. 6, 7
[24] Arsha Nagrani, Shan Yang, Anurag Arnab, Aren Jansen,           [40] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     Cordelia Schmid, and Chen Sun. Attention bottlenecks for            reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
     multimodal fusion. arXiv preprint arXiv:2107.00135, 2021.           Polosukhin. Attention is all you need. In NIPS, 2017. 1, 2
     2                                                              [41] Vibashan VS, Jeya Maria Jose Valanarasu, Poojan Oza, and
[25] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer,                Vishal M Patel. Image fusion transformer. arXiv preprint
     James Bradbury, Gregory Chanan, Trevor Killeen, Zeming              arXiv:2107.09011, 2021. 2
[42] Yikai Wang, Wenbing Huang, Fuchun Sun, Tingyang Xu,
     Yu Rong, and Junzhou Huang. Deep multimodal fusion by
     channel exchanging. In NeurIPS, 2020. 5, 6, 7, 9
[43] Yikai Wang, Fuchun Sun, Ming Lu, and Anbang Yao. Learn-
     ing deep multimodal feature representation with asymmetric
     multi-layer fusion. In ACM MM, 2020. 7
[44] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar,
     Jose M Alvarez, and Ping Luo. Segformer: Simple and ef-
     ficient design for semantic segmentation with transformers.
     In NeurIPS, 2021. 1, 2, 5, 6
[45] Amir Roshan Zamir, Alexander Sax, William B. Shen,
     Leonidas J. Guibas, Jitendra Malik, and Silvio Savarese.
     Taskonomy: Disentangling task transfer learning. In CVPR,
     2018. 5
[46] Zaiwei Zhang, Bo Sun, Haitao Yang, and Qixing Huang.
     H3dnet: 3d object detection using hybrid geometric primi-
     tives. arXiv preprint arXiv:2006.05682, 2020. 8
[47] Sixiao Zheng, Jiachen Lu, Hengshuang Zhao, Xiatian Zhu,
     Zekun Luo, Yabiao Wang, Yanwei Fu, Jianfeng Feng, Tao
     Xiang, Philip H.S. Torr, and Li Zhang. Rethinking semantic
     segmentation from a sequence-to-sequence perspective with
     transformers. In CVPR, 2021. 1, 2
[48] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang
     Wang, and Jifeng Dai. Deformable detr: Deformable trans-
     formers for end-to-end object detection. arXiv preprint
     arXiv:2010.04159, 2020. 1, 2
