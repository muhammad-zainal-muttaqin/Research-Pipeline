---
source_id: 179
bibtex_key: yuan2022newcrfs
title: Neural Window Fully-connected CRFs for Monocular Depth Estimation
year: 2022
domain_theme: Estimasi Kedalaman
verified_pdf: 179_NeWCRFs.pdf
char_count: 78317
---

NeW CRFs: Neural Window Fully-connected CRFs for Monocular Depth
                                                                      Estimation

                                                           Weihao Yuan          Xiaodong Gu Zuozhuo Dai                 Siyu Zhu        Ping Tan
                                                                                          Alibaba Group
                                                                Abstract
arXiv:2203.01502v2 [cs.CV] 6 Jun 2022

                                            Estimating the accurate depth from a single image is
                                        challenging since it is inherently ambiguous and ill-posed.
                                        While recent works design increasingly complicated and
                                        powerful networks to directly regress the depth map, we take
                                        the path of CRFs optimization. Due to the expensive com-
                                        putation, CRFs are usually performed between neighbor-
                                        hoods rather than the whole graph. To leverage the poten-
                                        tial of fully-connected CRFs, we split the input into windows
                                        and perform the FC-CRFs optimization within each win-
                                        dow, which reduces the computation complexity and makes         Figure 1. The neural window fully-connected CRFs take image
                                        FC-CRFs feasible. To better capture the relationships be-       feature F and upper-level prediction X as input, and compute the
                                        tween nodes in the graph, we exploit the multi-head atten-      fully-connected energy E in each window, which is then fed to the
                                                                                                        networks to output an optimized depth map.
                                        tion mechanism to compute a multi-head potential function,
                                        which is fed to the networks to output an optimized depth
                                        map. Then we build a bottom-up-top-down structure, where
                                        this neural window FC-CRFs module serves as the decoder,        no geometric constraints of multi-view [9,40,43] to exploit,
                                        and a vision transformer serves as the encoder. The ex-         the focus of most works is designing more powerful and
                                        periments demonstrate that our method significantly im-         more complicated networks. This renders this task a diffi-
                                        proves the performance across all metrics on both the KITTI     cult fitting problem without the help of other guidance.
                                        and NYUv2 datasets, compared to previous methods. Fur-             In traditional monocular depth estimation, some meth-
                                        thermore, the proposed method can be directly applied to        ods build the energy function from Markov Random Fields
                                        panorama images and outperforms all previous panorama           (MRFs) or Conditional Random Fields (CRFs) [30, 31, 37].
                                        methods on the MatterPort3D dataset. 1                          They exploit the observation cues, such as the texture and
                                                                                                        position information, along with the last prediction to build
                                                                                                        the energy function, and then optimize this energy to ob-
                                        1. Introduction                                                 tain a depth prediction. This approach is demonstrated to
                                                                                                        be effective in guiding the estimation of the depth, and is
                                           Depth prediction is a classical task in computer vision      also introduced in some deep methods [11,20,29,38]. How-
                                        and is essential for numerous applications such as 3D recon-    ever, they are all limited in neighbor CRFs rather than fully-
                                        struction, autonomous driving, and robotics [8, 13, 41, 42].    connected CRFs (FC-CRFs) due to the expensive computa-
                                        Such a vision task aims to estimate the depth map from          tion, while the fully-connected CRFs capture the relation-
                                        a single color image, which is an ill-posed and inherently      ship between any node in a graph and are much stronger.
                                        ambiguous problem since infinitely many 3D scenes can be           To address the above challenge, in this work we seg-
                                        projected to the same 2D scene. Therefore, this task is chal-   ment the input to multiple windows, and build the fully-
                                        lenging for traditional methods [22, 23, 30], which are usu-    connected CRFs energy within each window, in which way
                                        ally limited to low-dimension and sparse distances [22], or     the computation complexity is reduced considerably and the
                                        known and fixed objects [23].                                   fully-connected CRFs becomes feasible. To capture more
                                           Recently, many works have employed the deep networks         relationships between the nodes in the graph, we exploit the
                                        to directly regress the depth maps and achieved good per-       multi-head attention mechanism [35] to compute the pair-
                                        formances [1, 2, 6, 7, 17, 18]. Nevertheless, since there are   wise potential of the CRFs, and build a new neural CRFs
                                          1 Project page: https://weihaosky.github.io/newcrfs           module, as is shown in Figure 1. By employing this neural
window FC-CRFs module as decoder, and a vision trans-             depths at different pixels. In this way, they infer good depth
former as encoder, we build a straightforward bottom-up-          maps from the monocular cues like colors, pixel positions,
top-down network to estimate the depth. To make up for            occlusion, known object sizes, haze, defocus, etc. Since
the isolation of each window, a window shift action [21]          then, MRFs [31] and CRFs [37] have been well used in
is performed, and the lack of global information in these         monocular depth estimation in traditional methods. How-
window FC-CRFs is addressed by aggregating the global             ever, the traditional approaches still suffer from estimating
features from global average pooling layers [45].                 accurate high-resolution dense depth maps.
   In the experiments, our method is demonstrated to out-
perform previous methods by a significant margin on both          2.2. Neural Networks Based Monocular Depth
the outdoor dataset, KITTI [8], and the indoor dataset,               In monocular depth estimation, neural network based
NYUv2 [32]. Although the state-of-the-art performance             methods have dominated most benchmarks. There are
on KITTI and NYUv2 has been saturated for a while, our            mainly two kinds of approaches for learning the mapping
method further reduces the errors considerably on both            from images to depth maps. The first approach directly re-
datasets. Specifically, the Abs-Rel error and the RMS er-         gresses the continuous depth map from the aggregation of
ror of KITTI are decreased by 10.3% and 9.8%, and that            the information in an image [1, 6, 12, 17, 18, 26, 28, 39]. In
of NYUv2 are decreased by 7.8% and 8.2%. Our method               this approach, coarse and fine networks are first introduced
now ranks first among all submissions on the KITTI on-            in [6] and then improved by multi-stage local planar guid-
line benchmark. In addition, we evaluate our method on            ance layers in [17]. A bidirectional attention module is pro-
the panorama images. As is well-known, the networks de-           posed in [1] to utilize the feed-forward feature maps and
signed for perspective images usually perform poorly on           incorporate the global context to filter out ambiguity. Re-
the panorama dataset [14, 33, 34, 36]. Remarkably, our            cently, more methods have begun to employ vision trans-
method also sets a new state-of-the-art performance on the        formers to aggregate the information of images [28]. The
panorama dataset, MatterPort3D [3]. This demonstrates             second approach tries to discretize the depth space and con-
that our method can handle the common scenarios in the            vert the depth prediction to a classification or ordinal re-
monocular depth prediction task.                                  gression problem [2, 7]. A spacing-increasing quantization
   The main contributions of this work are then summarized        strategy is used in [7] to discretize the depth space more rea-
as follows:                                                       sonably. Then, an adaptive bins division is computed by the
   • We split the input image into sub-windows and per-           neural networks for better depth quantization. Also, other
form fully-connected CRFs optimization within each win-           approaches bring in auxiliary information to help the train-
dow, which reduces the high computation complexity and            ing of the depth network, such as sparse depth [10] or seg-
makes the FC-CRFs feasible.                                       mentation information [15,24,27,44]. All these approaches
   • We employ the multi-head attention to capture the pair-      try to directly regress the depth map from the image feature,
wise relationships in the window FC-CRFs, and embed this          which falls into a difficult fitting problem. The structures of
neural CRFs module in a network to serve as the decoder.          their networks become increasingly complex. In contrast
   • We build a new bottom-up-top-down network for                to these works, we build an energy with the fully-connected
monocular depth estimation and show a significant im-             CRFs, and then optimize this energy to obtain a high-quality
provement of the monocular depth across all metrics on            depth map.
KITTI, NYUv2, and MatterPort3D datasets.
                                                                  2.3. Neural CRFs for Monocular Depth
2. Related Work                                                       Since the graph models, like MRFs and CRFs, are ef-
                                                                  fective in traditional depth estimation, some methods try to
2.1. Traditional Monocular Depth Estimation
                                                                  embed them into neural networks [11, 19, 20, 29, 38]. These
    Prior to the emergence of deep learning, monocular            methods regard the patches of pixels as nodes and perform
depth estimation is a challenging task. Many published            the graph optimization. One such approach first uses net-
works limit themselves in either estimating 1-D distances         works to regress a coarse depth map and then utilizes CRFs
of obstacles [22] or limited in several known and fixed ob-       to refine it [19], where the post-processing function of CRFs
jects [23]. Then Saxena et al. [30] claim that local features     is proven to be effective. However, the CRFs are sepa-
alone are insufficient to predict the depth of a pixel, and the   rated from neural networks. To better combine CRFs and
global context of the whole image needs to be considered          networks, other methods integrate CRFs into the layers of
to infer the depth. Therefore, they use a discriminatively-       the neural networks and train the whole framework end-
trained Markov Random Field (MRF) to incorporate mul-             to-end [11, 20, 29, 38]. But they are all limited to CRFs
tiscale local and global image features, and model both           rather than fully-connected CRFs due to the high computa-
depths at individual pixels as well as the relation between       tion complexity.
                                                                  is computed for each node by the predictor according to the
                                                                  image features.
                                                                      The pairwise potential function ψp connects pairs of
                                                                  nodes as

                                                                          ψp = µ(xi , xj )f (xi , xj )g(Ii , Ij )h(pi , pj ),   (2)

                                                                  where µ(xi , xj ) = 1 if i 6= j and µ(xi , xj ) = 0 otherwise,
                                                                  Ii is the color of node i, pi is the position of node i. The
                                                                  pairwise potential usually considers the color and position
Figure 2. Graph model of fully-connected CRFs and window          information to enforce some heuristic punishments, which
fully-connected CRFs. In a fully-connected CRFs graph (a), tak-   make the predicted values xi , xj more reasonable and logi-
ing the orange node as an example, it is connected to all other   cal.
nodes in the graph. In a window fully-connected CRFs, however,       In regular CRFs, the pairwise potential only computes
the orange node is only connected to all other nodes within one   the edge connection between the current node and neigh-
window.                                                           boring nodes. In fully-connected CRFs, however, the con-
                                                                  nections between the current node and any other nodes in a
    In this work, different from previous methods, we split
                                                                  graph need to be computed, as shown in Figure 2 (a).
the whole graph into multiple sub-windows, such that the
fully-connected CRFs become feasible. Also, inspired by           3.2. Window Fully-connected CRFs
recent works in vision transformer [5, 21, 35], we use the
multi-head attention mechanism to capture the pairwise re-           Although the fully-connected CRFs can bring global-
lationship in FC-CRFs and propose a neural window fully-          range connections, its disadvantage is also obvious. On the
connected CRFs module. This module is embedded into the           one hand, the number of edges connecting all pixels in an
network to play the role of the decoder, such that the whole      image is large, which makes the computation of this kind of
framework can be trained end-to-end.                              pairwise potential quite resource-consuming. On the other
                                                                  hand, the depth of a pixel is usually not determined by dis-
3. Neural Window Fully-connected CRFs                             tant pixels. Only pixels within some distance need to be
                                                                  considered.
    This section first introduces the window fully-connected         Therefore, in this work we propose the window-based
CRFs, followed by its integration with neural networks. Af-       fully-connected CRFs. We segment an image into multiple
terward, the network structure is displayed, where the neu-       patch-based windows. Each window includes N ×N image
ral window FC-CRFs module is embedded into a top-down-            patches, of which each patch is composed of n × n pixels.
bottom-up network to serve as the decoder.                        In our graph model, each patch rather than each pixel is
3.1. Fully-connected Conditional Random Fields                    regarded as one node. All patches within one window are
                                                                  fully-connected with edges, while the patches of different
   In traditional methods, Markov random fields (MRFs)            windows are not connected, as displayed in Figure 2 (b). In
or conditional random fields (CRFs) are leveraged to han-         this case, the computation of pairwise potential only consid-
dle dense prediction tasks such as monocular depth estima-        ers the patches within one window, so that the computation
tion [30] and semantic segmentation [4]. They are shown to        complexity is reduced significantly.
be effective in correcting the erroneous predictions based on        Taking an image with h × w patches as an example,
the information of the current and adjacent nodes. Specif-        the computation complexity of FC-CRFs and window FC-
ically, in a graph model, these methods favor similar label       CRFs for one iteration are
assignments to nodes that are proximal in space and color.
   Thus, in this work we employ CRFs to help the depth               Ω(FC-CRFs) = hw × Ω(ψu ) + hw(hw − 1) × Ω(ψp )
prediction. Since the depth prediction of the current pixel is    Ω(Window FC) = hw × Ω(ψu ) + hw(N 2 − 1) × Ω(ψp ),
determined by long-range pixels in one image, to increase                                                                 (3)
the receptive field, we use fully-connected CRFs [16] to          where N is the window size, Ω(µu ) and Ω(µp ) are the com-
build the energy. In a graph model, the energy function of        putation complexity of one unary potential and one pairwise
the fully-connected CRFs is usually defined as                    potential, respectively.
                     X              X                                In the window fully-connected CRFs, all windows are
            E(x) =       ψu (xi ) +    ψp (xi , xj ),     (1)     non-overlapped, which means there is no information con-
                      i             ij
                                                                  nection between any windows. The adjacent windows,
where xi is the predicted value of node i, and j denotes all      however, are physically connected. To resolve the isolation
other nodes in the graph. The unary potential function ψu         of windows, we shift the windows by ( N2 , N2 ) patches in
Figure 3. Network structure of the proposed framework. The encoder first extracts the features in four levels. A PPM head aggregates
the global and local information and makes the initial prediction X from the top image feature F. Then in each level, the neural window
fully-connected CRFs module builds multi-head energy from X and F, and optimizes it to a better prediction X 0 . Between each level a
rearrange upscale is performed considering the sharpness and network weight.

the image and calculate the energy function of shifted win-                             For the pairwise potential, we realize that it is composed
dows after computing that of the original windows, similar                           of values of the current node and other nodes, and a weight
to swin-transformer [21]. In this way, the isolated neigh-                           computed based on the color and position information of
boring pixels are connected in the shifted windows. Hence,                           the node pairs. So we reformulate it as
each time we calculate the energy function, we calculate
two energy functions successively, one for the original win-                                  ψp (xi , xj ) = w(Fi , Fj , pi , pj )||xi − xj ||,   (7)
dows and the other one for the shifted windows.
                                                                                     where F is the feature map and w is the weighting function.
3.3. Neural Window FC-CRFs                                                           We calculate the pairwise potential node by node. For each
                                                                                     node i, we sum all its pairwise potentials and obtain
   In traditional CRFs, the unary potential is usually acted
by a distribution over the predicted values, e.g.,                                                                    X
                                                                                      ψpi = α(Fi , Fj , pi , pj )xi +   β(Fi , Fj , pi , pj )xj , (8)
                  ψu (xi ) = − log P (xi |I),                                  (4)                                      j6=i

where I is the input color image and P is the probability                            where α, β are the weighting functions and will be com-
distribution of the value prediction. The pairwise potential                         puted by the networks.
is usually computed according to the colors and positions of                            Inspired by recent works in transformer [5, 35], we cal-
pixel pairs, e.g.,                                                                   culate a query vector q and a key vector k from the feature
                                              ||Ii −Ij ||        ||pi −pj ||
                                                                                     map of each patch in a window and combine vectors of all
  ψp (xi , xj ) = µ(xi , xj )||xi − xj ||e−      2σ 2      .e−      2σ 2             patches to matrices Q and K. Then we calculate the dot
                                                          (5)                        product of matrices Q and K to get the potential weight
This potential encourages distinct-color and distant pixels                          between any pair, after which the predicted values X are
to have various value predictions while punishing the value                          multiplied by the weights to get the final pairwise potential.
discrepancies in similar-color and adjacent pixels.                                  To introduce the position information, we also add a rela-
   These potential functions are designed by hands and can-                          tive position embedding P . Therefore, the equation 8 can
not be too complicated. Thus they are hard to represent                              be calculated as
high-dimensional information and describe complex con-
nections. So in this work, we propose to use neural net-                                             ψpi = SoftMax(q · K T + P ) · X
                                                                                                X                                                  (9)
works to perform the potential functions.                                                            ψpi = SoftMax(Q · K T + P ) · X,
   For the unary potential, it is computed from the image                                        i
features such that it can be directly obtained by the network                        where · denotes dot production. Thus, the output of the
as                                                                                   SoftMax gets the weights α and β of Equation 8. Therefore,
                     ψu (xi ) = θu (I, xi ),              (6)                        the dot product between Q and K calculates the scores be-
where θ is the parameters of a unary network.                                        tween each node with any other node, which determines the
             Input image                       DORN                              Ours                          Error map
                Figure 4. Qualitative results on the KITTI online benchmark, which are generated by the online server.

message passing weights with P , while the dot product be-            puted by a convolutional network and the pairwise poten-
tween previous prediction X and the output of the SoftMax             tial is computed according to equation 9. In each CRFs
performs the message passing.                                         optimization, multiple-head Q and K are calculated to ob-
                                                                      tain multi-head potentials, which can enhance the relation-
3.4. Network Structure                                                ship capturing ability of the energy function. From the top
Overview. To embed the neural window fully-connected                  level to the bottom level, a structure of 32, 16, 8, 4 heads
CRFs into a depth prediction network, we build a bottom-              is adopted. Then the energy function is fed into an opti-
up-top-down structure, where four levels of CRFs optimiza-            mization network composed of two fully-connected layers
tions are performed, as is shown in Figure 3. We embed this           to output the optimized depth map X 0 .
neural window FC-CRFs module into the network to act as               Upscale Module. After the neural window FC-CRFs de-
a decoder, which predicts the next-level depth according to           coders at the top three levels, a shuffle operation is per-
the coarse depth and image features. For the encoder, we              formed to rearrange the pixels, by which the image is up-
employ the swin-transformer [21] to extract the features.             scaled from h2 × w2 × d to h × w × d4 . On the one hand, this
   For an image with the size of H × W , there are four               operation increases the flow to the next level with a larger
levels of image patches for the feature extraction encoder            scale without losing the sharpness like upsampling. On the
and the CRFs optimization decoder, from 4 × 4 pixels to               other hand, this reduces the feature dimension to lighten the
32 × 32 pixels. At each level, N × N patches make up a                subsequent networks.
window. The window size N is fixed at all levels, so there
                                                                      Training Loss. Following previous works [2, 17, 18], we
will be 4N
         H    W
           × 4N  windows at the bottom level and 32N
                                                  H     W
                                                     × 32N
                                                                      use a Scale-Invariant Logarithmic (SILog) loss proposed by
windows at the top level.
                                                                      [6] to supervise the training. Given the ground-truth depth
Global Information Aggregation. At the top level, to                  map, we first calculate the logarithm difference between the
make up for the lack of global information of the window              predicted depth map and the real depth:
FC-CRFs, we use the pyramid pooling module (PPM) [45]
                                                                                          ∆di = log dˆi − log d∗i ,            (10)
to aggregate the information of the whole image. Similar
to [45], we use global averaging pooling of scales 1, 2, 3, 6         where d∗i is the ground-truth depth value and dˆi is the pre-
to extract the global information, which is then concate-             dicted depth at pixel i.
nated with the input feature to map to the top-level predic-             Then for K pixels with valid depth values in an image,
tion X by a convolutional layer.                                      the scale-invariant loss is computed as
                                                                                       s
Neural Window FC-CRFs Module. In each neural win-                                          1 X            λ X
dow FC-CRFs block, there are two successive CRFs opti-                          L=α               ∆d2i − 2 (     ∆di )2 ,      (11)
                                                                                          K i            K    i
mizations, one for regular windows and the other one for
shifted windows. To cooperate with the transformer en-                where λ is a variance minimizing factor, and α is a scale
coder, the window size N is set to 7, which means each                constant. In our experiments, λ is set to 0.85 and α is set to
window contains 7 × 7 patches. The unary potential is com-            10 following previous works [17].
                      Method          cap    Abs Rel ↓ Sq Rel ↓ RMSE ↓ RMSElog ↓ δ < 1.25 ↑ δ < 1.252 ↑ δ < 1.253 ↑
             Eigen et al. [6]     0-80m       0.190     1.515     7.156        0.270        0.692         0.899         0.967
              Liu et al. [20]     0-80m       0.217       −       7.046          −          0.656         0.881         0.958
              Xu et al. [38]      0-80m       0.122     0.897     4.677          −          0.818         0.954         0.985
                 DORN [7]         0-80m       0.072     0.307     2.727        0.120        0.932         0.984         0.995
              Yin et al. [39]     0-80m       0.072       −       3.258        0.117        0.938         0.990         0.998
                  BTS [17]        0-80m       0.059     0.241     2.756        0.096        0.956         0.993         0.998
          PackNet-SAN [10]        0-80m       0.062       −       2.888          −          0.955           −             −
                 Adabin [2]       0-80m       0.058     0.190     2.360        0.088        0.964         0.995         0.999
                 DPT* [28]        0-80m       0.062       −       2.573        0.092        0.959         0.995         0.999
                  PWA [18]        0-80m       0.060     0.221     2.604        0.093        0.958         0.994         0.999
                        Ours      0-80m       0.052     0.155     2.129        0.079        0.974         0.997         0.999
Table 1. Quantitative results on the Eigen split of KITTI dataset. Seven widely used metrics are reported. “Abs Rel” error is the main
ranking metric. Note that the “Sq Rel” error is calculated in a different way here. “*” means using additional data for training.

                Method       dataset        SILog ↓ Abs Rel ↓ Sq Rel ↓ iRMSE ↓ RMSE ↓ δ < 1.25 ↑ δ < 1.252 ↑ δ < 1.253 ↑
             DORN [7]           val         12.22     11.78      3.03      11.68       3.80       0.913         0.985         0.995
              BTS [17]          val         10.67      7.51      1.59       8.10       3.37       0.938         0.987         0.996
            BA-Full [1]         val         10.64      8.25      1.81       8.47       3.30       0.938         0.988         0.997
                 Ours           val         8.31      5.54       0.89      6.34        2.55       0.968         0.995         0.998
            DORN [7]       online test      11.77     8.78       2.23      12.98        −           −             −             −
             BTS [17]      online test      11.67     9.04       2.21      12.23        −           −             −             −
           BA-Full [1]     online test      11.61     9.38       2.29      12.23        −           −             −             −
     PackNet-SAN [10]      online test      11.54     9.12       2.35      12.38        −           −             −             −
             PWA [18]      online test      11.45     9.05       2.30      12.32        −           −             −             −
                Ours       online test      10.39     8.37       1.83      11.03        −           −             −             −
Table 2. Quantitative results on the official split of KITTI dataset. Eight widely used metrics are reported for the validation set while only
four metrics are available from the online evaluation server for the test set. “SILog” error is the main ranking metric. Our method ranks
1st among all submissions on the KITTI depth prediction online benchmark at the submission time of this paper.

4. Experiments                                                               NYUv2 dataset. NYUv2 [32] is an indoor datasets with
                                                                          120K RGB-D videos captured from 464 indoor scenes.
4.1. Implementation Details                                               We follow the official training/testing split to evaluate our
   Our work is implemented in Pytorch and experimented                    method, where 249 scenes are used for training and 654 im-
on Nvidia GTX 2080 Ti GPUs. The network is opti-                          ages from 215 scenes are used for testing.
mized end-to-end with the Adam optimizer (β1 = 0.9,                          MatterPort3D dataset. To verify the effectiveness
β1 = 0.999). The training runs for 20 epochs with the batch               of our method on more domains, we also evaluate our
size of 8 and the learning rate decreasing from 1 × 10−4 to               method on the panorama images. MatterPort3D [3] is the
1 × 10−5 . The output depth map of our network is of 14 × 14              biggest real-world dataset among all widely used datasets in
size of the original image, which is then resized to the full             panorama depth estimation. Following the official split, we
resolution.                                                               use 7829 images from 61 houses to train our network and
                                                                          then evaluate the model on the merged set of 957 validation
4.2. Datasets                                                             images and 2014 testing images. All images are resized to
                                                                          1024 × 512 in both training and evaluation.
   KITTI dataset. KITTI dataset [8] is the most used
benchmark with outdoor scenes captured from a moving                      4.3. Evaluations
vehicle. There are two mainly used splits for monocular
depth estimation. One is the training/testing split proposed                  Evaluation on KITTI. For outdoor scenes, we evalu-
by Eigen et al. [6] with 23488 training image pairs and 697               ate our method on the KITTI dataset. We first perform the
testing images. The other one is the official split proposed              training and testing on the Eigen split, of which the test-
by Geiger et al. [8] with 42949 training image pairs, 1000                ing images are available so that the network can be bet-
validation images, and 500 testing images. For the official               ter tuned. The results are reported in Table 1, where we
split, the ground-truth depth maps for the testing images are             can see that our method outperforms previous methods by a
withheld by the online evaluation benchmark.                              significant margin. Almost all errors are reduced by about
                     Input image              BTS               Adabins               Ours           Ground truth
                                           Figure 5. Qualitative results on the NYUv2 dataset.
                      Method Abs Rel ↓ Sq Rel ↓ RMSE ↓ RMSElog ↓ log10 ↓ δ < 1.25 ↑ δ < 1.252 ↑ δ < 1.253 ↑
               Liu et al. [20]     0.230       −       0.824         −        0.095      0.614      0.883           0.971
               Xu et al. [38]      0.125       −       0.593         −        0.057      0.806      0.952           0.986
                  DORN [7]         0.115       −       0.509         −        0.051      0.828      0.965           0.992
               Yin et al. [39]     0.108       −       0.416         −        0.048      0.875      0.976           0.994
                   BTS [17]        0.110     0.066     0.392       0.142      0.047      0.885      0.978           0.994
                   DAV [12]        0.108       −       0.412         −          −        0.882      0.980           0.996
          PackNet-SAN* [10]        0.106       −       0.393         −          −        0.892      0.979           0.995
                  Adabin [2]       0.103       −       0.364         −        0.044      0.903      0.984           0.997
                  DPT* [28]        0.110       −       0.357         −        0.045      0.904      0.988           0.998
                   PWA [18]        0.105       −       0.374         −        0.045      0.892      0.985           0.997
                         Ours      0.095     0.045     0.334       0.119      0.041      0.922      0.992           0.998
    Table 3. Quantitative results on NYUv2. “Abs Rel” and “RMSE” are the main ranking metrics. “*” means using additional data.

10%. Specifically, the “Abs-Rel”, “Sq Rel”, “RMSE” and                 our method on the NYUv2 dataset. Since the state-of-the-
“RMSElog ” errors are decreased by 10.3%, 18.4%, 9.8%,                 art performance on NYUv2 dataset has been saturated for
and 10.2%, respectively. Although our method is trained                a while, some methods have begun to use additional data
without additional data, it can outperform previous meth-              to pretrain the model and then finetune it on NYUv2 train-
ods trained with additional training data.                             ing set [10, 28]. Differently, without any additional data,
    We then evaluate our method on the KITTI official split,           our method can significantly improve the performance in all
where the testing images are hidden. The results on the                metrics, as is shown in Table 3. Specifically, the “Abs Rel”
validation set and the testing set are all presented in Ta-            error is reduced to within 0.1 and the “δ < 1.252 ” accu-
ble 2. The results of the testing set are cited from the on-           racy reaches 99%. This emphasizes the contribution of our
line benchmark and the results of the validation set are cited         method in improving the results. The qualitative results in
from BANet [1]. Here we can see that our method reduces                Figure 5 illustrate that our method estimates better depth es-
the main ranking metric, the SILog error, markedly. Our                pecially in difficult regions, such as repeated texture, messy
method now ranks 1st among all submissions on the KITTI                environment, and bad light.
depth prediction online server. The colorful visualizations                Evaluation on MatterPort3D. As is studied in previ-
of the predicted depth maps and the error maps generated by            ous works, directly applying a deep network for perspective
the online server are shown in Figure 4. Our method pre-               images to the standard representation of spherical panora-
dicts cleaner and smoother depth while maintaining sharper             mas, i.e., the equirectangular projection, is suboptimal, as
edges of objects, e.g., the edges of the humans.                       it becomes distorted towards the poles [14, 33, 34, 36]. As
   Evaluation on NYUv2. For indoor scenes, we evaluate                 such, methods in this task try all kinds of ways to con-
                           Method Abs Rel ↓      Abs ↓    RMSE ↓ RMSElog ↓ δ < 1.25 ↑ δ < 1.252 ↑ δ < 1.253 ↑
                  OmniDepth [46]    0.2901      0.4838     0.7643      0.1450        0.6830        0.8794         0.9429
                     BiFuse [36]    0.2048      0.3470     0.6259      0.1134        0.8452        0.9319         0.9632
                    SliceNet [25]   0.1764      0.3296     0.6133      0.1045        0.8716        0.9483         0.9716
                   HoHoNet [33]     0.1488      0.2862     0.5138      0.0871        0.8786        0.9519         0.9771
                    UniFuse [14]    0.1063      0.2814     0.4941      0.0701        0.8897        0.9623         0.9831
                            Ours    0.0906      0.2252     0.4778      0.0638        0.9197        0.9761         0.9909
                            Ours*   0.0793      0.1970     0.4279      0.0575        0.9376        0.9812         0.9933
                   Table 4. Quantitative results on the Matterport3D dataset. “*” means using additional data for training.

       Setting Abs Rel Sq Rel RMSE Rlog              1.25 1.252           the well-used convolutional decoder. Then based on this
                                                                          baseline, we only replace the decoder with our neural win-
    Baseline       0.069    0.256   2.610   0.103 0.947 0.993
 Neural CRFs       0.055    0.185   2.322   0.086 0.965 0.995             dow FC-CRFs module, and obtain a noticeable performance
         +S        0.054    0.174   2.297   0.084 0.968 0.996             improvement as shown in Table 5. The “Abs Rel” error is
     +S+R          0.054    0.168   2.271   0.083 0.970 0.996             reduced from 0.069 to 0.055, and then to 0.054 by adding
  +S+R+P           0.052    0.155   2.129   0.079 0.974 0.997             the shift action. This demonstrates the effectiveness of the
                                                                          neural window FC-CRFs in estimating accurate depths.
     8, 4, 2, 1    0.055    0.165   2.203 0.083 0.970 0.996
    16, 8, 4, 2    0.054    0.162   2.172 0.081 0.972 0.997                   Rearrange upscale.           On top of the basic neural
   32, 16, 8, 4    0.052    0.155   2.129 0.079 0.974 0.997               FC-CRFs structure, we add the rearrange upscale mod-
                                                                          ule. The performance increment gained from this module
Table 5. Ablation study on the Eigen split of KITTI dataset. The          is not large, but visually the output depth maps have sharper
first six metrics of those used in Table 1 are reported here. “S”         edges, and the parameters of the network are reduced.
refers to window shift, “R” refers to rearrange upscale, and “P”              PPM head. The PPM head aggregates the global infor-
refers to PPM head. The last three rows display the results of            mation, which is lacking in window FC-CRFs. This mod-
using different numbers of heads.                                         ule can help in some regions that are difficult for estimating
                                                                          with only local information, e.g., the complex texture and
vert the panorama images to distortion-free shape, e.g., the
                                                                          the white walls. From the results in Table 5, we see this
cubemap projection [14, 36], the horizontal feature repre-
                                                                          module contributes to the performance of our framework.
sentation [33], and spherical convolutional filters [34]. In
comparison to the above-mentioned methods, we directly                        Multi-head energy. The CRFs energy is calculated
apply our network designed for perspective images to the                  in a multi-head manner. With more heads, the ability of
panorama images, and outperforms all previous methods,                    capturing the pairwise relationship would be stronger but
as is presented in Table 4. Specifically, the “Abs Rel” and               the weight of the network would be heavier. In previous
“Abs” errors are decreased by 14.8% and 20.0%.                            experiments, the numbers of the heads in four levels are
                                                                          set to 32, 16, 8, 4. Here we use fewer heads to see how a
    In addition, we realize that the number of the training set
                                                                          lightweight structure performs. From the results in Table 5,
of MatterPort3D is small, so we collect more data in the real
                                                                          fewer heads lead to a small performance decrease.
world. We use 50K images to pretrain the network and then
finetune it on the MatterPort3D training set, which results in
a better performance, as shown in Table 4. The model pre-                 5. Conclusion
trained with more data is denoted by “Ours*”. This demon-
                                                                             We propose a neural window fully-connected CRFs
strates the pretraining with more images can clearly boost
                                                                          module to address the monocular depth estimation problem.
the performance in panorama depth estimation.
                                                                          To solve the expensive computation of FC-CRFs, we split
4.4. Abalation Study                                                      the input into sub-windows and calculate the pairwise po-
                                                                          tential within each window. To capture the relationships
   To better inspect the effect of each module in our                     between nodes of the graph, we exploit the multi-head at-
method, we evaluate each component by an ablation study                   tention to compute a neural potential function. This neu-
and present the results in Table 5.                                       ral window FC-CRFs module can be directly embedded
   Baseline vs. Neural CRFs. To verify the effectiveness                  into a bottom-up-top-down structure and serves as a de-
of the proposed neural window fully-connected FC-CRFs,                    coder, which cooperates with a transformer encoder and
we build a baseline model. This model is a well-used UNet                 predicts accurate depth maps. The experiments show that
structure with the same encoder as ours. In other words,                  our method significantly outperforms previous methods and
compared to our full method, the PPM head and the rear-                   sets a new state-of-the-art performance on KITTI, NYUv2,
range upscale are removed, and the decoder is replaced by                 and MatterPort3D datasets.
References                                                               Conference on Computer Vision, pages 581–597. Springer,
                                                                         2020. 2, 7
 [1] Shubhra Aich, Jean Marie Uwabeza Vianney, Md Amirul Is-        [13] Shahram Izadi, David Kim, Otmar Hilliges, David
     lam, Mannat Kaur, and Bingbing Liu. Bidirectional attention         Molyneaux, Richard Newcombe, Pushmeet Kohli, Jamie
     network for monocular depth estimation. In Proceedings of           Shotton, Steve Hodges, Dustin Freeman, Andrew Davison,
     the IEEE International Conference on Robotics and Automa-           et al. Kinectfusion: real-time 3d reconstruction and inter-
     tion, pages 11746–11752, 2021. 1, 2, 6, 7                           action using a moving depth camera. In Proceedings of the
 [2] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.             24th annual ACM symposium on User interface software and
     Adabins: Depth estimation using adaptive bins. In Proceed-          technology, pages 559–568, 2011. 1
     ings of the IEEE Conference on Computer Vision and Pattern     [14] Hualie Jiang, Zhe Sheng, Siyu Zhu, Zilong Dong, and Rui
     Recognition, pages 4009–4018, 2021. 1, 2, 5, 6, 7                   Huang. Unifuse: Unidirectional fusion for 360 panorama
 [3] Angel Chang, Angela Dai, Thomas Funkhouser, Maciej                  depth estimation. IEEE Robotics and Automation Letters,
     Halber, Matthias Niessner, Manolis Savva, Shuran Song,              6(2):1519–1526, 2021. 2, 7, 8
     Andy Zeng, and Yinda Zhang. Matterport3d: Learning             [15] Marvin Klingner, Jan-Aike Termöhlen, Jonas Mikolajczyk,
     from rgb-d data in indoor environments. arXiv preprint              and Tim Fingscheidt. Self-supervised monocular depth es-
     arXiv:1709.06158, 2017. 2, 6                                        timation: Solving the dynamic object problem by semantic
 [4] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,              guidance. In Proceedings of the European Conference on
     Kevin Murphy, and Alan L Yuille. Deeplab: Semantic image            Computer Vision, pages 582–600. Springer, 2020. 2
     segmentation with deep convolutional nets, atrous convolu-     [16] Philipp Krähenbühl and Vladlen Koltun. Efficient inference
     tion, and fully connected crfs. IEEE Transactions on Pattern        in fully connected crfs with gaussian edge potentials. Ad-
     Analysis and Machine Intelligence, 40(4):834–848, 2017. 3           vances in Neural Information Processing Systems, 24:109–
 [5] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,              117, 2011. 3
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,            [17] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-            Il Hong Suh. From big to small: Multi-scale local planar
     vain Gelly, et al. An image is worth 16x16 words: Trans-            guidance for monocular depth estimation. arXiv preprint
     formers for image recognition at scale. In Proceedings of           arXiv:1907.10326, 2019. 1, 2, 5, 6, 7
     the International Conference on Learning Representations,      [18] Sihaeng Lee, Janghyeon Lee, Byungju Kim, Eojindl Yi, and
     2020. 3, 4                                                          Junmo Kim. Patch-wise attention network for monocular
 [6] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map           depth estimation. In Proceedings of the AAAI Conference on
     prediction from a single image using a multi-scale deep net-        Artificial Intelligence, volume 35, pages 1873–1881, 2021.
     work. In Advances in Neural Information Processing Sys-             1, 2, 5, 6, 7
     tems, pages 2366–2374, 2014. 1, 2, 5, 6                        [19] Bo Li, Chunhua Shen, Yuchao Dai, Anton Van Den Hen-
 [7] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Bat-                   gel, and Mingyi He. Depth and surface normal estimation
     manghelich, and Dacheng Tao. Deep ordinal regression net-           from monocular images using regression on deep features
     work for monocular depth estimation. In Proceedings of the          and hierarchical crfs. In Proceedings of the IEEE Conference
     IEEE Conference on Computer Vision and Pattern Recogni-             on Computer Vision and Pattern Recognition, pages 1119–
     tion, pages 2002–2011, 2018. 1, 2, 6, 7                             1127, 2015. 2
                                                                    [20] Fayao Liu, Chunhua Shen, and Guosheng Lin. Deep con-
 [8] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
                                                                         volutional neural fields for depth estimation from a single
     ready for autonomous driving? the kitti vision benchmark
                                                                         image. In Proceedings of the IEEE Conference on Computer
     suite. In Proceedings of the IEEE Conference on Computer
                                                                         Vision and Pattern Recognition, pages 5162–5170, 2015. 1,
     Vision and Pattern Recognition, pages 3354–3361. IEEE,
                                                                         2, 6, 7
     2012. 1, 2, 6
                                                                    [21] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei,
 [9] Xiaodong Gu, Weihao Yuan, Zuozhuo Dai, Chengzhou                    Zheng Zhang, Stephen Lin, and Baining Guo. Swin trans-
     Tang, Siyu Zhu, and Ping Tan.           Dro: Deep recur-            former: Hierarchical vision transformer using shifted win-
     rent optimizer for structure-from-motion. arXiv preprint            dows. arXiv preprint arXiv:2103.14030, 2021. 2, 3, 4, 5
     arXiv:2103.13201, 2021. 1                                      [22] Jeff Michels, Ashutosh Saxena, and Andrew Y Ng. High
[10] Vitor Guizilini, Rares Ambrus, Wolfram Burgard, and                 speed obstacle avoidance using monocular vision and rein-
     Adrien Gaidon. Sparse auxiliary networks for unified                forcement learning. In Proceedings of the International Con-
     monocular depth prediction and completion. In Proceed-              ference on Machine Learning, pages 593–600, 2005. 1, 2
     ings of the IEEE Conference on Computer Vision and Pattern     [23] Takaaki Nagai, Takumi Naruse, Masaaki Ikehara, and Akira
     Recognition, pages 11078–11088, 2021. 2, 6, 7                       Kurematsu. Hmm-based surface reconstruction from single
[11] Yan Hua and Hu Tian. Depth estimation with convolu-                 images. In Proceedings of the International Conference on
     tional conditional random field network. Neurocomputing,            Image Processing, volume 2, pages II–II. IEEE, 2002. 1, 2
     214:546–554, 2016. 1, 2                                        [24] Matthias Ochs, Adrian Kretz, and Rudolf Mester. Sdnet:
[12] Lam Huynh, Phong Nguyen-Ha, Jiri Matas, Esa Rahtu, and              Semantically guided depth estimation network. In Ger-
     Janne Heikkilä. Guiding monocular depth estimation us-             man Conference on Pattern Recognition, pages 288–302.
     ing depth-attention volume. In Proceedings of the European          Springer, 2019. 2
[25] Giovanni Pintore, Marco Agus, Eva Almansa, Jens Schnei-               image using foe crf. Multimedia Tools and Applications,
     der, and Enrico Gobbetti. Slicenet: deep dense depth estima-          74(21):9491–9506, 2015. 1, 2
     tion from a single indoor panorama using a slice-based repre-    [38] Dan Xu, Wei Wang, Hao Tang, Hong Liu, Nicu Sebe, and
     sentation. In Proceedings of the IEEE Conference on Com-              Elisa Ricci. Structured attention guided convolutional neural
     puter Vision and Pattern Recognition, pages 11536–11545,              fields for monocular depth estimation. In Proceedings of the
     2021. 8                                                               IEEE Conference on Computer Vision and Pattern Recogni-
[26] Xiaojuan Qi, Renjie Liao, Zhengzhe Liu, Raquel Urtasun,               tion, pages 3917–3925, 2018. 1, 2, 6, 7
     and Jiaya Jia. Geonet: Geometric neural network for joint        [39] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     depth and surface normal estimation. In Proceedings of the            forcing geometric constraints of virtual normal for depth pre-
     IEEE Conference on Computer Vision and Pattern Recogni-               diction. In Proceedings of the IEEE/CVF International Con-
     tion, pages 283–291, 2018. 2                                          ference on Computer Vision, pages 5684–5693, 2019. 2, 6,
[27] Siyuan Qiao, Yukun Zhu, Hartwig Adam, Alan Yuille, and                7
     Liang-Chieh Chen. Vip-deeplab: Learning visual perception        [40] Weihao Yuan, Rui Fan, Michael Yu Wang, and Qifeng Chen.
     with depth-aware video panoptic segmentation. In Proceed-             Mfusenet: Robust depth estimation with learned multiscopic
     ings of the IEEE Conference on Computer Vision and Pattern            fusion. IEEE Robotics and Automation Letters, 5(2):3113–
     Recognition, pages 3997–4008, 2021. 2                                 3120, 2020. 1
[28] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-        [41] Weihao Yuan, Kaiyu Hang, Danica Kragic, Michael Y
     sion transformers for dense prediction. In Proceedings of the         Wang, and Johannes A Stork. End-to-end nonprehen-
     International Conference on Computer Vision, pages 12179–             sile rearrangement with deep reinforcement learning and
     12188, 2021. 2, 6, 7                                                  simulation-to-reality transfer. Robotics and Autonomous Sys-
[29] Elisa Ricci, Wanli Ouyang, Xiaogang Wang, Nicu Sebe,                  tems, 119:119–134, 2019. 1
     et al. Monocular depth estimation using multi-scale contin-      [42] Weihao Yuan, Kaiyu Hang, Haoran Song, Danica Kragic,
     uous crfs as sequential deep networks. IEEE Transactions              Michael Y Wang, and Johannes A Stork. Reinforcement
     on Pattern Analysis and Machine Intelligence, 41(6):1426–             learning in topology-based representation for human body
     1440, 2018. 1, 2                                                      movement with whole arm manipulation. In Proceedings of
[30] Ashutosh Saxena, Sung H Chung, Andrew Y Ng, et al.                    the IEEE International Conference on Robotics and Automa-
     Learning depth from single monocular images. In Advances              tion, 2019. 1
     in Neural Information Processing Systems, volume 18, pages       [43] Weihao Yuan, Yazhan Zhang, Bingkun Wu, Siyu Zhu, Ping
     1–8, 2005. 1, 2, 3                                                    Tan, Michael Yu Wang, and Qifeng Chen. Stereo matching
[31] Ashutosh Saxena, Min Sun, and Andrew Y Ng. Make3d:                    by self-supervision of multiscopic vision. In Proceedings of
     Learning 3d scene structure from a single still image. IEEE           the IEEE/RSJ International Conference on Intelligent Robots
     Transactions on Pattern Analysis and Machine Intelligence,            and Systems, pages 5702–5709. IEEE, 2021. 1
     31(5):824–840, 2008. 1, 2
                                                                      [44] Zhenyu Zhang, Zhen Cui, Chunyan Xu, Yan Yan, Nicu Sebe,
[32] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob                and Jian Yang. Pattern-affinitive propagation across depth,
     Fergus. Indoor segmentation and support inference from                surface normal and semantic segmentation. In Proceedings
     rgbd images. In Proceedings of the European Conference                of the IEEE Conference on Computer Vision and Pattern
     on Computer Vision, pages 746–760. Springer, 2012. 2, 6               Recognition, pages 4106–4115, 2019. 2
[33] Cheng Sun, Min Sun, and Hwann-Tzong Chen. Hohonet:
                                                                      [45] Hengshuang Zhao, Jianping Shi, Xiaojuan Qi, Xiaogang
     360 indoor holistic understanding with latent horizontal fea-
                                                                           Wang, and Jiaya Jia. Pyramid scene parsing network. In Pro-
     tures. In Proceedings of the IEEE Conference on Computer
                                                                           ceedings of the IEEE Conference on Computer Vision and
     Vision and Pattern Recognition, pages 2573–2582, 2021. 2,
                                                                           Pattern Recognition, pages 2881–2890, 2017. 2, 5
     7, 8
                                                                      [46] Nikolaos Zioulis, Antonis Karakottas, Dimitrios Zarpalas,
[34] Keisuke Tateno, Nassir Navab, and Federico Tombari.
                                                                           and Petros Daras. Omnidepth: Dense depth estimation for
     Distortion-aware convolutional filters for dense prediction in
                                                                           indoors spherical panoramas. In Proceedings of the Euro-
     panoramic images. In Proceedings of the European Confer-
                                                                           pean Conference on Computer Vision, pages 448–465, 2018.
     ence on Computer Vision, pages 707–722, 2018. 2, 7, 8
                                                                           8
[35] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
     Polosukhin. Attention is all you need. In Advances in Neural
     Information Processing Systems, pages 5998–6008, 2017. 1,
     3, 4
[36] Fu-En Wang, Yu-Hsuan Yeh, Min Sun, Wei-Chen Chiu, and
     Yi-Hsuan Tsai. Bifuse: Monocular 360 depth estimation
     via bi-projection fusion. In Proceedings of the IEEE Con-
     ference on Computer Vision and Pattern Recognition, pages
     462–471, 2020. 2, 7, 8
[37] Xiaoyan Wang, Chunping Hou, Liangzhou Pu, and
     Yonghong Hou. A depth estimating method from a single
                                              NeW CRFs: Neural Window Fully-connected CRFs for Monocular Depth
                                                                       Estimation

                                                                   Weihao Yuan                    Xiaodong Gu Zuozhuo Dai                                                        Siyu Zhu                   Ping Tan
                                                                                                            Alibaba Group
                                        A. Network Structure                                                                                    0.055 when N = 7, but the increase of the cost grows up
                                                                                                                                                exponentially, costing 250 ms and 5.3 G when N = 48.
arXiv:2203.01502v2 [cs.CV] 6 Jun 2022

                                            More details of our network are shown in Figure 1. The                                              Our window FC-CRFs of window size N = 2 is equivalent
                                        top-level output of the encoder is fed into the PPM head [8]                                            to traditional CRFs, and that of window size 352 × 1216
                                        for aggregating the local and global information. Then in                                               is equivalent to the FC-CRFs. FC-CRFs consumes much
                                        each level, a graph with patches as nodes is built, which is                                            more memory and computation than our window FC-CRF,
                                        split into k windows with size of N × N . From the top level                                            even of large N (e.g. 48). In traditional graph-based meth-
                                        to the bottom level, a combination of 32, 16, 8, 4 is adopted                                           ods, the CRFs for depth estimation costs 59.1 s in [7], and
                                        for the head numbers.                                                                                   the FC-CRFs for segmentation costs 0.5 s in [2, 3], while
                                                                                                                                                our window FC-CRFs of 7 × 7 costs only 29 ms (without
                                        B. Efficiency Experiments                                                                               considering the feature extraction).

                                           To inspect the efficiency of the neural window FC-CRFs,                                              C. More Qualitative Results
                                        we perform the experiments of different window size and
                                        report the efficiency and accuracy in Table 1. The window                                                  To make more comparisons to previous state-of-the-art
                                        FC-CRFs of window size 2 costs 121 − 95 = 26 ms and                                                     methods, we display more qualitative results of BTS [4],
                                        2.7 − 2.6 = 0.1 G without considering the feature extrac-                                               Adabins [1], and our method on the test set of NYUv2 [6]
                                        tion. With the increase of window size N , the improving                                                dataset, as is shown in Figure 2. From the results, our
                                        of the accuracy gradually tapers and is almost saturated at                                             method estimates better depth and recover more details, es-
                                             Shift window fully connected CRF

                                               Encoder                                      PPM Head
                                                                     H W                     H W                                                                                                                 H W
                                                                       × ×1536                 × ×1536                                                                                                             × ×3584
                                                                     32 32                   32 32                                                                                                               32 32
                                                      Encoder                                                                                                                                                C                Conv 3x3
                                                                                                                                                                                                H W
                                                                     H W                                                        1×1×1536                              1×1×512                     × ×512
                                                                       × ×768                                                                                                                   32 32
                                                                     16 16                                          AvgPool2d                       Conv 1x1                      Resize                               H W
                                                      Encoder                                                                                                                                                            × ×512
                                                                                                                                                                                                H W                    32 32
                                                                      H W                                                       2×2×1536                              2×2×512                     × ×512
                                                                       × ×384                                                                                                                   32 32
                                                                      8 8                                           AvgPool2d                       Conv 1x1                      Resize
                                                      Encoder
                                                                                                                                                                                                H W
                                                                      H W                                                       3×3×1536                              3×3×512                     × ×512
                                                                       × ×192                                                                                                                   32 32
                                                                      4 4                                           AvgPool2d                       Conv 1x1                      Resize
                                                      Encoder
                                                                                                                                                                                                H W
                                                                                                                                6×6×1536                              6×6×512                     × ×512
                                                                                                                                                                                                32 32
                                                                                                                    AvgPool2d                       Conv 1x1                      Resize
                                                         Image

                                               Pairwise Potential
                                                                                                                                               𝑁 ! ×𝑁 ! 𝑘× 𝑁 ! ×32              H W                         H W
                                                                                                                                                                                  × ×1024                     × ×512
                                                                                                                                                                                32 32                       32 32
                                                                                                                       𝑘×𝑁 ! ×32                    𝑃             𝑋        S                     Conv 3x3
                                                                                                                          𝑄
                                                                                              𝑘×𝑁 ! ×32    QK                          𝑘×𝑁 ! ×𝑁 !                              𝑘×𝑁 ! ×32
                                                H W                                                       Head-1
                                                                                                                                   X                +             X                        𝜓"                           X   Dot product
                                                                            H W
                                                                                                                                                        SoftMax

                                                  × ×1536                     × ×1024                                     𝐾
                                                32 32
                                                                 Conv 3x3
                                                                            32 32
                                                                                        S                                                                                                                               + Addition
                                                                                                                       𝑘×𝑁 ! ×32
                                                                                                            QK                                                                                                          C   Concat
                                                                                              𝑘×𝑁 ! ×32   Head-32                                                                                                       S   Split

                                        Figure 1. Network details of encoder, PPM head, and pairwise potential. The pairwise potential in the top level is computed with 32 heads,
                                        each of which is of 32 channels. The graph of the image is split into k windows of size N × N .

                                                                                                                                          1
 Window size Image size Time Memory Abs Rel RMSE
Feature extract 352 × 1216 95ms  2.6G                                     Analysis and Machine Intelligence, 40(4):834–848, 2017. 1,
              2 352 × 1216 121ms 2.7 G  0.061 2.524                       2
              4 352 × 1216 122ms 2.7 G  0.058 2.358                   [3] Philipp Krähenbühl and Vladlen Koltun. Efficient inference in
            7/8 352 × 1216 124ms 2.7 G  0.055 2.234                       fully connected crfs with gaussian edge potentials. Advances
             16 352 × 1216 136ms 2.9 G  0.055 2.188                       in Neural Information Processing Systems, 24:109–117, 2011.
             24 352 × 1216 149ms 3.5 G  0.055 2.201                       1, 2
             32 352 × 1216 192ms 5.1 G  0.054 2.232                   [4] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and
             48 352 × 1216 345ms 7.3 G OOM in training                    Il Hong Suh. From big to small: Multi-scale local planar
            [5] 86 × 107    7.5s   -                                      guidance for monocular depth estimation. arXiv preprint
            [7] 55 × 305 59.1s     -                                      arXiv:1907.10326, 2019. 1, 3
         [2, 3] 480 × 640 0.5s     -                                  [5] Ashutosh Saxena, Sung H Chung, Andrew Y Ng, et al. Learn-
                                                                          ing depth from single monocular images. In Advances in Neu-
Table 1. Efficiency experiments on the Eigen split of KITTI               ral Information Processing Systems, volume 18, pages 1–8,
dataset. The first row is the time of other modules except the CRFs       2005. 2
decoder, and then we add that of different window size. Models        [6] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
are retrained with a random crop of 352 × 352 of original images          Fergus. Indoor segmentation and support inference from rgbd
due to the high memory consumption of large window FC-CRFs.               images. In Proceedings of the European Conference on Com-
“OOM” denotes out of memory. BTS, DPT, and our models are                 puter Vision, pages 746–760. Springer, 2012. 1
all tested on RTX 2080 Ti. The time of [4] is only the CRFs post-     [7] Xiaoyan Wang, Chunping Hou, Liangzhou Pu, and Yonghong
processing.                                                               Hou. A depth estimating method from a single image using
                                                                          foe crf. Multimedia Tools and Applications, 74(21):9491–
                                                                          9506, 2015. 1, 2
pecially in difficult regions, such as repeated texture, messy        [8] Hengshuang Zhao, Jianping Shi, Xiaojuan Qi, Xiaogang
environment, and bad light.                                               Wang, and Jiaya Jia. Pyramid scene parsing network. In
                                                                          Proceedings of the IEEE Conference on Computer Vision and
                                                                          Pattern Recognition, pages 2881–2890, 2017. 1
D. Point Cloud Visualization
    To better see the 3D shape of the estimated depth map,
we project the 2D pixels of the color image back to the
3D world utilizing the estimated depth map. The generated
point clouds on the test set of NYUv2 dataset are displayed
in Figure 3, where the structures of the 3D world are recov-
ered reasonably.
    Furthermore, to recover the complete scenarios, we col-
lect some new indoor panorama images in the real world,
and apply our model to these unseen images. The estimated
depth maps and the projected 3D point clouds are displayed
in Figure 4, where the whole structures of the rooms are suc-
cessfully reconstructed. The floors, ceilings, and the walls
keep flat from the near to far. The straight lines are kept
straight and the right angles are kept right. The decent per-
formance on the unseen images shows the generalization
ability of our model, which has the potential to be applied
to real-world applications.

References
[1] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.
    Adabins: Depth estimation using adaptive bins. In Proceed-
    ings of the IEEE Conference on Computer Vision and Pattern
    Recognition, pages 4009–4018, 2021. 1, 3
[2] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,
    Kevin Murphy, and Alan L Yuille. Deeplab: Semantic im-
    age segmentation with deep convolutional nets, atrous convo-
    lution, and fully connected crfs. IEEE Transactions on Pattern
Input image        BTS [4]              Adabins [1]              Ours           Ground truth

              Figure 2. Qualitative results on the test set of NYUv2 dataset.
Input image             Estimated depth

                                                                             Point cloud

              Figure 3. Point cloud visualization on the test set of NYUv2 dataset.
Figure 4. Point cloud visualization on unseen panorama images.
