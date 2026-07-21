---
source_id: 072
bibtex_key: ming2021depthsurvey
title: Deep Learning for Monocular Depth Estimation: A Review
year: 2021
domain_theme: Estimasi Kedalaman
verified_pdf: 72_Review_Depth_Monokular_Ming_dkk.pdf
char_count: 161670
---

Deep Learning for Monocular Depth Estimation: A Review. ⋆
Yue Minga,∗ , Xuyang Menga,∗ , Chunxiao Fana and Hui Yub,∗∗
a Beijing Key Laboratory of Work Safety and Intelligent Monitoring, School of Electronic Engineering, Beijing University of Posts and

Telecommunications, Beijing 100876, P.R. China.
b School of Creative Technologies, University of Portsmouth, UK

ARTICLE INFO                                          ABSTRACT
Keywords:                                             Depth estimation is a classic task in computer vision, which is of great significance for many appli-
Monocular depth estimation                            cations such as augmented reality, target tracking and autonomous driving. Traditional monocular
Deep learning                                         depth estimation methods are based on depth cues for depth prediction with strict requirements, e.g.
Supervised                                            shape-from-focus / defocus methods require low depth of field on the scenes and images. Recently,
Unsupervised                                          a large body of deep learning methods have been proposed and has shown great promise in handling
Multi-task learning                                   the traditional ill-posed problem. This paper aims to review the state-of-the-art development in deep
                                                      learning-based monocular depth estimation. We give an overview of published papers between 2014
                                                      and 2020 in terms of training manners and task types. We firstly summarize the deep learning mod-
                                                      els for monocular depth estimation. Secondly, we categorize various deep learning-based methods
                                                      in monocular depth estimation. Thirdly, we introduce the publicly available dataset and the evalua-
                                                      tion metrics. And we also analysis the properties of these methods and compare their performance.
                                                      Finally, we highlight the challenges in order to inform the future research directions.

1. Introduction                                                                 has brought great advantages to image processing [47, 68,
                                                                                148, 172] especially depth estimation.
    Scene depth estimation plays an important role in com-                          Traditional depth estimation methods of image-based depth
puter vision, which enhances the perception and understand-
                                                                                estimation are usually based on binocular camera, which cal-
ing of real three-dimensional scenes leading to a wide range
                                                                                culates the disparity of two 2D images (taken by a binocular
of applications such as robotic navigation, autonomous driv-                    camera) through stereo matching and triangulation to obtain
ing, and virtual reality. [1, 53, 139, 145, 166]. Active depth                  a depth map [40, 82, 117, 170, 180]. However, the binocu-
estimation methods usually utilize lasers, structured light and                 lar depth estimation method requires at least two fixed cam-
other reflections on the object surface to obtain depth point                   eras [185], and it is difficult to capture enough features in the
clouds, complete surface modeling and estimate scene depth
                                                                                image to match when the scene has less or no texture [84].
maps [61, 182]. However, obtaining dense and accurate depth
                                                                                Therefore, researchers turn their attention to monocular depth
maps usually requires extremely heavy costs of manpower                         estimation. Monocular depth estimation uses only one cam-
and computing resources [101, 178]. Therefore, image-based                      era to obtain an image or video sequence, which does not
depth estimation has become the mainstream of research,                         require additional complicated equipments and professional
and can be applied in a wide range of applications [89, 135].                   techniques. It has vast application demands due to the avail-
    The evolution of image-based depth estimation is shown
                                                                                ability of only one single camera in most application scenar-
in Figure 1. In the early period, researchers estimated depth
                                                                                ios. Thus,there is an increasing demand for monocular depth
maps depending on depth cues, such as vanishing points [142],                   estimation in recent years. Since monocular images lack
focus and defocus [138], and shadow [181]. However, most                        a reliable stereoscopic visual relationship, it is essentially
of these methods were applied in constraint scenes [138, 142,                   an ill-posed problem to regress depth in 3D space [102].
181]. With the development of computer vision, many hand-                       Therefore, researchers propose various methods for monoc-
made features and probabilistic graph models have been pro-
                                                                                ular depth estimation [8, 67].
posed, such as scale-invariant feature transform (SIFT) [88],
                                                                                    Monocular images adopt a two-dimensional form to re-
speeded up robust features (SURF) [7], pyramid histogram                        flect the three-dimensional world. However, one dimension
of oriented gradient (PHOG) [9], Conditional Random Field                       of the scene, namely depth, has missed in the imaging pro-
(CRF) [66], and Markov Random Field (MRF) [25], which                           cess, which makes it impossible to judge the size and dis-
were adopted to predict monocular depth maps with parame-
                                                                                tance of the object, nor to judge whether the object is oc-
ter and non-parameter learning in the machine learning pro-
                                                                                cluded by another object. Therefore, we need to recover the
cess [25, 66, 81]. The advent of deep learning technologies                     depth of the monocular image. Based on the depth map,
    ⋆
      The work presented in this paper was partly supported by Natural Sci-     we can judge the size and distance of the object to meet the
ence Foundation of China (Grant No. 62076030), Beijing Natural Science          needs of scene understanding. When the estimated depth
Foundation of China (Grant No. L182033) and the Fundamental Research            map can reflect the three-dimensional structure of the scene,
Funds for the Central Universities (2019PTB-001).
    ∗ Co-First author: Yue Ming and Xuyang Meng                                 we can consider that the depth estimation method is effec-
   ∗∗ Corresponding author                                                      tiveness.
        hui.yu@port.ac.uk (H. Yu)                                                   This paper focuses on the research of monocular depth
      ORCID (s):
                                       Deep Learning for Monocular Depth Estimation: A Review

                     Depth cues-based                      Machine learning                    Deep learning
                        Shape-from-X                       Parameter Learning                Single-task Learning
                                                         Non-parameter Learning              Multi-task Learning
                        Focus / Defocus
                                                           SIFT, SURF, PHOG                       Supervised
                            Motion

                           Shading                             CRF-based                        Unsupervised

                       Vanishing points                        MRF-based                       Semi-supervised

                          Properties                           Properties                         Properties

                      Low depth of field                  Texture requirement                   High accuracy

                    Complex and inefficient                 High complexity                   Strong practicality

                       Poor practicality                         Sparse                     Multi-scene application

                         Not real-time                        Not real-time                       Real time

                        Early period                       Machine learning                     Deep learning
                                                2009           period             2014             period

Figure 1: The evolution of depth estimation.      This paper divides the development of depth estimation into three periods: the
early period, the machine learning period, and the deep learning period, where the depth estimation method of monocular image
based on deep learning is mainly surveyed and summarized.

recent years, details their remarks, and compares their per-          activation function, which enable CNN to learn the two-dimensional
formances. Furthermore, this paper describes the limita-              spatial features of the input image. The convolutional layer
tions of these existing methods and briefly introduces the            transforms the input into depth features; the pooling layer
future trends. The remainder of this paper is as follows:             reduces the size of the input feature map in max-pooling or
Section 2 introduces some deep learning models for monoc-             average-pooling manner; the fully connected layer is usually
ular depth estimation; Section 3 summarizes deep learning-            located at the end of the CNN to output the results; and the
based methods of monocular depth estimation, from training            activation function is generally a continuously differentiable
manners and task types; Section 4 introduces the common               nonlinear function to avoid pure linear combinations. Repre-
datasets and evaluation metrics of depth estimation, and then         sentative CNNs include AlexNet [63], VGG [131], GoogLeNet [137],
analysis their properties and compares their performance;             ResNet [48], DenseNet [52], and some lightweight network,
Section 5 discusses the challenges and trends of monocular            such as MobileNet [51], ShuffleNet [183], and GhostNet [46],
depth estimation; Conclusions are drawn in Section 6.                 each of which is used as the backbone of the existing CNN-
                                                                      based depth estimation network.
2. Deep Learning models for monocular depth                           2.2. RNN
   estimation                                                              RNN is a sequence-to-sequence model with memory ca-
    This section mainly introduces common deep learning               pabilities [13, 41] as shown in Figure 2(a), which is intro-
models for monocular depth estimation: Convolutional Neu-             duced into monocular depth estimation so as to learn tempo-
ral Network (CNN) [63], Recurrent Neural Network (RNN)                ral features from video sequences. RNN includes three parts:
[122], and Generative Adversarial Network (GAN) [39].                 input unit, hidden unit, and output unit, where the input of
                                                                      the hidden unit consists of the outputs of both current input
2.1. CNN                                                              unit and previous hidden unit. Furthermore, Hochreiter et
    CNN can automatically extract spatial features represent-         al. [50] proposed a Long Short-Term Memory (LSTM) unit
ing depth in a scene. It is a type of feed-forward neural net-        as shown in Figure 2(b), which could learn long-term de-
work, which extracts depth features and reconstructs depth            pendences with a three-gate structure: input gate layer, for-
maps at the same time with fewer parameters compared to               get gate layer, and output gate layer. Representative RNNs
traditional methods [165, 159, 86]. CNN mainly includes               including BiRNN [126], GRU [22], ConvLSTM [162], G2 -
convolutional layer, pooling layer, fully connected layer and         LSTM [78], ON-LSTM [127], Mogrifier LSTM [96] and
                                            Deep Learning for Monocular Depth Estimation: A Review

            O(t-1)                   O(t)            O(t+1)
                                                                                 RGB               GT
            V                    V                   V

    W                       W                  W                W                                                              True?
            S(t-1)                   S(t)            S(t+1)                                                                    False?
                                                                                                               Discriminator

            U                    U                   U
                                                                              Generator      Predicted depth
            I(t-1)                   I(t)             I(t+1)

                                (a) RNN                                   Figure 3:   The general GAN-based framework for supervised
                                                                          monocular depth estimation.

                                                     h(t)

                                                                          learning depth maps from a single 2D color image through
   c(t-1)                                                       c(t)      a deep neural network, which was firstly proposed by Eigen
                                                     tanh                 et al. [29] in 2014. It was a coarse-to-fine framework, where
                                                                          the coarse network learned the global depth on the entire im-
                                                                          age to obtain a rough depth map and the fine network learned
                σ           σ    tanh          σ                          the local features to refine the depth map, as shown in Fig-
   h(t-1)                                                       h(t)
                                                                          ure 4. Since then, many researchers have carried out deep
                                                                          learning methods for monocular depth estimation [28, 30,
                     x(t)
                                                                          36, 69, 83, 169, 174, 189].
                                (b) LSTM                                       The framework of monocular depth estimation based on
                                                                          deep learning is an encoder-decoder network, with the RGB
Figure 2:   (a) The basic structure of RNN, where              𝑆 is the   image input and depth map output, as shown in Figure 5. The
internal status and the memory of the cell, 𝐼 is the input, 𝑂
                                                                          encoder network consists of convolution and pooling layers
is the output, and (𝑈 ,𝑉 ,𝑊 ) is the sharing parameters of the
                                                                          to capture the depth features, and the decoder network in-
cell. (b) The basic structure of LSTM [50].
                                                                          cludes deconvolution layers to regress the estimated pixel-
                                                                          level depth map, with the same size as the input. Addition-
                                                                          ally, in order to preserve the features of each scale, the cor-
others are introduced into deep learning models for monocu-               responding layers of encoder and decoder are concatenated
lar depth estimation, which are usually combined with CNNs                with skip-connections. The entire network is constrained
to extract spatial-temporal features to recover depth [54, 149].          and trained by the depth loss functions and converges when
                                                                          the desired depth map is generated.
2.3. GAN                                                                       Deep learning methods for monocular depth estimation
    The supervised depth estimation model needs to learn                  often utilize gradient descent to train deep neural networks,
the 3D mapping and scale information from the ground truth                and obtain a local minimum finally. The best local minimum
(GT) depth maps. However, it is difficult to obtain GT depth              depends on initialization and specific parameter settings. In
maps in real scenes so that researchers introduced GAN [39]               the initialization process, it is generally necessary to resize
to generate clearer and more realistic depth maps compared                the image to meet the needs of network learning. In addition,
to other models [177]. GAN includes two modules: the                      it also need to set the initial learning rate, optimizer param-
generator predicts the depth map as a depth estimation net-               eters, batchsize and mini-batchsize, to learn and save image
work, and the discriminator determines whether the input                  features. The commonly used learning method is stochas-
depth map is true or false, as shown in Figure 3. Represen-               tic gradient descent, and the optimizer is Adam. When the
tative GANs are introduced into depth estimation, including               gradient no longer changes and the loss function becomes
conditional GAN [99], DCGAN [111], WGAN [4], stacked                      stable, the network converges.
GAN [177], SimGAN [128], and Cycle GAN [196]. Depth                            Compared with traditional methods, deep learning meth-
estimation models with GANs can provide generation adver-                 ods for monocular depth estimation construct the multi-layer
sarial constraints for the estimated depth maps and the GT                neural network to learn deep features, which has higher accu-
depth maps [32, 45, 58].                                                  racy. When there is small occlusion in the monocular image
                                                                          or part of the ground-truth depth is missing, the deep learn-
3. Deep Learning Methods for Monocular                                    ing methods can still estimate the depth of the scene, and
                                                                          have low errors; when there is large occlusion in presence
   Depth Estimation
                                                                          in the scene or there is no ground-truth depth, deep learning
    Deep neural networks have played an important role in                 methods can learn the depth of the scene by adding network
various areas with their powerful feature learning ability.               constraints. In short, deep learning methods for monocular
Monocular depth estimation based deep learning is a task of               depth estimation have shown strong robustness.
                                         Deep Learning for Monocular Depth Estimation: A Review

                    Input
                                                                                                                                                 Coarse depth

                                             C      P             C           P        C           C           C          F       F

                                                                                                                                  Coarse

                                                                                                                                             Refined depth

                                                       C          P                            C           C

                                                                                                                   Fine

                      C      Convolution      P   Pooling             F   Fully connection                     Input/Output           Concatenation

Figure 4: The architecture of multi-scale network for monocular depth estimation proposed by Eigen et al. [29]. The top module

is the coarse network for coarse estimation and the bottom module is the ne network for rened depth map.

                                     C       P     C          C           C        C       D           D           D          D   D

                                                                                                                                            Depth

                     Input
                                                    Encoder                                                    Decoder

                               C    Convolution    P       Pooling            D   Deconvolution            Concatenation          Input/Output

Figure 5: The general pipeline of deep learning for monocular depth estimation.                                        The left module is encoder network learning
depth features layer-by-layer, and the decoder network in the right module recovers the depth map.

    This section reviews and summarizes deep learning meth-                            3.1.1. Supervised Learning Methods
ods for monocular depth estimation from 2014 to 2020, which                                Supervised learning networks for monocular depth es-
was classified into two different perspectives: the training                           timation are trained with the GT depth maps as shown in
manners with supervised, unsupervised and semi-supervised                              Figure 7. The purpose of learning is to penalize the errors
manner, and the tasks with single-task and multi-task learn-                           between the predictions and GT depth maps constrained by
ing of depth estimation models. The overall diagram of monoc-                          the loss functions formulated in Table 1, where the 𝑙𝑜𝑔(𝑑)
ular depth estimation based on deep learning is drawn in Fig-                          as Eq.(1) is based on 𝑙𝑜𝑔 depth [28], and the reverse Huber
ure 6.                                                                                 (Berhu) function as Eq.(1) combines the 𝐿1 and 𝐿2 norms at
                                                                                       the same time to reduce the influence of error changes on the
3.1. Training Manners                                                                  range of weights proposed by Laina et al. [69]. That is, the
    The supervised monocular depth estimation network es-                              depth model converges when the predicted depth value is as
timates the depth maps by learning the scene structure in-                             close to GT as possible, and other loss functions are variants
formation from the GT depth maps. The cost of obtain-                                  of the functions mentioned in Table 1.
ing the GT depth maps is very high, so that some monoc-
ular depth estimation networks need to be trained with less                            (1) CNNs-based Methods. Researchers have designed
or no GT to reconstruct depth maps, which are the semi-                                CNN-based monocular depth estimation networks to learn
supervised or unsupervised learning methods. This section                              depth features layer by layer through their convolution ker-
will review and classify deep learning methods from the per-                           nels and recover depth maps by deconvolution to meet the re-
spective of training manners: supervised, unsupervised, and                            quirements of scene understanding. This section introduces
semi-supervised models for monocular depth estimation.                                 two aspects based on the absolute depth or relative depth
                                                                  Deep Learning for Monocular Depth Estimation: A Review

                                                                                                       CNN-based               [19,70,76,163,197]

                                                                                Supervised
                                                                                                       RNN-based               [54,64,93,149,162]
                                                                                 leanring

                                                                                                       GAN-based                    [45,58]

                                                                                                     Stereo matching               [14,34,36]

                                                              Training         Unsupervised
                                                              manner             learning
                                                                                                       Monocular
                                                                                                                              [57,107,164,167,194]
                                                                                                       sequence
               Deep Learning for Monocular Depth Estimation

                                                                                                      Synthetic data            [94,140,189,191]

                                                                                   Semi-
                                                                                supervised               LIDAR                   [27,49,65,110]
                                                                                 learning

                                                                                                     Surface normal            [109,152,184,187]

                                                                                                       Regression             [76,162,176,188,191]
                                                                                 Single-task
                                                                                  learning
                                                                                                      Classification             [11,33,74,87]

                                                               Tasks

                                                                                                     Depth + Semantic
                                                                                                                                 [6,18,28,55,81]
                                                                                                       segmentation
                                                                                 Multi-task
                                                                                 learning
                                                                                                      Depth + others            [37,92,129,133]

Figure 6: The overall diagram of deep learning methods for monocular depth estimation. According to whether the network is

trained with GT, these deep learning methods are divided into supervised, unsupervised, and semi-supervised learning models;
according to the types of network prediction task, these methods are classied into single-task and multi-task learning methods.

learned from monocular images.                                                                 pairs in the image to infer depth information. They output
    For absolute depth learning, Li et al. [76] proposed a                                     the relative relationship between the point-pairs and utilized
two-streamed framework based on VGG-16 [131] for monoc-                                        the numerical optimization method to obtain the dense depth
ular depth estimation: one stream for depth regression and                                     maps. Chen et al. [19] proposed a multi-scale network that
other for depth gradients, which were combined through a                                       predicted pixel-level depth by learning relative depth. The
depth-gradient fusion module to obtain a coherent depth map.                                   network was trained with the relative depth loss function
The entire model was constrained by the depth loss and the                                     and performed depth recovery on monocular images in an
gradient loss functions, enhancing the generalization abili-                                   unconstrained environment, whose root mean square error
ties of each stream mutually for richer 3D projections. Fur-                                   (RMSE) was 1.10 comparable to the absolute depth estima-
thermore, there are many monocular depth estimation meth-                                      tion model [83]. Lee et al. [70] designed a CNN to esti-
ods based on more complex CNNs to learn pixel-level depth,                                     mate the relative depth at different scales, which was opti-
such as VGG-based models [62, 188], ResNet-based mod-                                          mally reorganized to reconstruct the final depth map. Their
els [69, 71, 188], and DenseNet-based models [71].                                             RMSE was better than most absolute depth methods men-
    For relative depth estimation, Zoran et al. [197] proposed                                 tioned above.
a method adopting the relative relationship between point-                                         The absolute depth learning has higher accuracy, and the
                                     Deep Learning for Monocular Depth Estimation: A Review

                   Table 1

                   The loss functions commonly used in supervised learning for monocular depth estimation,
                                                          ∗                     2                ∗
                   where 𝑑 respects the estimated depth, 𝑑 is the GT depth, 𝑦 = 𝑙𝑜𝑔(𝑑) − 𝑙𝑜𝑔(𝑑 ), 𝜆 is a
                                                                                𝑖
                   balance factor, and 𝑐 is a threshold.

                                    Name             Formulation
                                                                       ∑𝑁
                                    𝐿1 (𝑑, 𝑑 ∗ )     𝐿1 (𝑑, 𝑑 ∗ ) = 𝑁1 𝑖=1 ||𝑑𝑖 − 𝑑𝑖∗ ||1
                                                                       ∑𝑁
                                    𝐿2 (𝑑, 𝑑 ∗ )     𝐿2 (𝑑, 𝑑 ∗ ) = 𝑁1 𝑖=1 ||𝑑𝑖 − 𝑑𝑖∗ ||22
                                                                      ∑𝑁              (∑          )2
                                                                                           𝑁
                                    𝐿(𝑙𝑜𝑔𝑑)          𝐿(𝑑, 𝑑 ∗ ) = 𝑁1 𝑖=1 𝑦2𝑖 − 𝑁𝜆              𝑦𝑖
                                                                        {                  𝑖=1

                                                                            |𝑑 −    𝑑 ∗
                                                                                         |      𝑖𝑓 |𝑑 − 𝑑 ∗ | ≤ 𝑐,
                                    Berhu            𝐿𝐵𝑒𝑟ℎ𝑢 (𝑑, 𝑑 ∗ ) =    |𝑑−𝑑 ∗ |2 +𝑐 2
                                                                               2𝑐
                                                                                                𝑖𝑓 |𝑑 − 𝑑 ∗ | > 𝑐.

                                                                                   Based on CRF, Xu et al. [163] proposed an attention
                                   Back-propagation
      RGB                                                                      model to automatically learn robust multi-scale features through
                                                                               an integrated attention mechanism [85, 146, 155], where the
                                                                               cascade-CRFs module reduced the RMSE of 0.088 com-
                                             Depth
                                                             Depth loss        pared to the baseline based on ResNet-50. Ricci et al. [119]
                   Depth network                              (L1, L2)
                                                                               proposed two deep models for monocular depth estimation,
                                                                               one was based on multiple CRF cascading, and the other was
  Ground truth
                                                                               based on a unified graph model. Multi-scale features were
Figure 7: The general model of supervised learning for monoc-
                                                                               merged through CRF integration multi-level cascade. Addi-
ular depth estimation, whose inputs are the RGB and GT depth
                                                                               tionally, there are lots of CNNs combined with continuous
images and the output is the estimated depth map.                              CRF [75, 83], hierarchical CRF [151], FC-CRF [11, 100], to
                                                                               predict monocular depth in a supervised manner.
                                                                                   CNN has made great progress in monocular depth es-
                                                                               timation recently. On the one hand, it learns and fits deep
                                    Depth
                                                                               features to reconstruct the scene depth maps by designing
                                   network                                     deeper and more complex networks; on the other hand, it
                                                               CRF
                                                                               combines with CRF to analyze and optimize the predictions
                                    Depth                                      of the deep networks, to obtain refined depth map. How to
                                   network                       ...
    GT                                                                         reconstruct the novel networks to adapt to monocular depth
                    ...

                                     ...

                                                                               estimation is an important research direction.
                                    Depth
                                   network
                                                                               (2) RNNs-based Methods. RNN-based supervised learn-
    RGB                                                                        ing networks for monocular depth estimation capture the spa-
                                    Depth
    Input
                                   network                    Depth            tial features and temporal information from monocular im-
                                                                               age sequences [54, 149]. Different from CNN-based mod-
                 Patches     Fixed and shared weights
                                                                               els, the encoder of RNN-based network is designed with all
Figure 8: The general model of supervised methods with CRF
                                                                               LSTM (or ConvLSTM) layers or consists of convolution and
for monocular depth estimation, where each depth network
                                                                               LSTM (ConvLSTM) layers to extract and reserve spatial-
with xed and shared weights learns from each pair of patches.
                                                                               temporal features for monocular depth estimation, as shown
                                                                               in Figure 9.
                                                                                    Kumar et al. [64] proposed the DepthNet with ConvL-
                                                                               STM [162] layers to predict monocular depth maps and im-
relative depth learning models are more robust which aren’t                    plicitly learned the smooth temporal variation. The encoder
affected by the data homography.                                               of DepthNet only consisted of eight ConvLSTM layers likes
     Combined with CRF. Conditional Random Field (CRF)                         Figure 9(a), which made the network fully use the tempo-
is a conditional probability distribution model under the con-                 ral information in sequences, and the convolution operation
dition of a given input sequences [66]. CRF can establish a                    helped to maintain the spatial geometric relationships be-
structured connection between input and output, where the                      tween the cells. Furthermore, Mancini et al. [93] adopted
key is to construct a reasonable and correct feature for monoc-                LSTM units to exploit the input stream sequentiality and
ular image depth estimation. In order to regress continu-                      predict scene depth, where the LSTM layers followed the
ous depth, depth estimation networks with fixed and shared                     convolution layers in the encoder network, illustrated in Fig-
weights are constructed to learn different patches firstly. Then,              ure 9(b).
these estimations are propagated to the CRF module to ob-
tain the final depth, as shown in Figure 8.
                                                                Deep Learning for Monocular Depth Estimation: A Review

     L    LSTM(ConvLSTM)                      C Convolution                D Deconvolution                                                 P

                      L       L       ...         L         D    ...   D     D

          Input                                                                      Depth
                                                                                                                                                                     d
                                                      (a)
                                                                                                                 U(L)                                   U(R)
                                                                                                                                P(L)             P(R)
                                                                                                                I(L)                                     I(R)
                                                                                                                                                                f
           C      L       C       L         ...        C        L      D   ...   D     D

  Input                                                                                        Depth             O(L)                                   O(R)
                                                                                                                                          B
                                                      (b)

Figure 9: There are two general architectures of RNN-based                                             Figure 10: The principle of stereo matching methods for depth

methods for monocular depth estimation. In (a), the encoder                                            estimation, where 𝐼(𝐿) and 𝐼(𝑅) are stereo pair-wise images
is constructed by all LSTM (or ConvLSTM) layers, yet (b) is                                            taken by the left and the right cameras, respectively.
composed of convolution and LSTM (or ConvLSTM) layers.

                                                                                                            Left image                                    Disparity map
(3) GANs-based Methods. GAN-based supervised net-                                                                                      Depth Network
works can generate depth maps close to the GT [45, 58], as
shown in Figure 3. Specially, Jung et al. [58] introduced
                                                                                                         Reconstruction Error
GANs to the monocular depth estimation, where the gener-
ator consisted of a GlobalNet to extract global features and
a RefinementNet to estimate local structures from the input                                                                               Warping
image. The entire model was trained with an adversarial loss                                              Warped image                                     Right image
built on the estimated depth map and the GT depth map:
                                                                                                       Figure 11: The general model of unsupervised methods with

                                                                                                       stereo matching for monocular depth estimation.

   min max 𝔼𝑥∼𝑃𝐺𝑇 [𝑙𝑜𝑔𝐷(𝑥)] + 𝔼𝑥∗ ∼𝑃𝐺 [𝑙𝑜𝑔(1 − 𝐷(𝑥 ))] (1)                                 ∗
    𝐺     𝐷

where 𝐺 is the generator function, 𝐷 is the discriminator
function, 𝑥 is the depth estimated by the generator, 𝑥∗ is the                                         numerous equipments and intensive labor work. Therefore,
GT depth map, and 𝑃 represents the domain of pixel.                                                    researchers explore unsupervised deep learning methods for
                                                                                                       monocular depth estimation without GT depth maps. Un-
Summary. Supervised deep learning methods have been                                                    supervised monocular depth estimation are usually trained
widely studied and applied in monocular depth estimation,                                              with stereo pair-wise images or monocular image sequences,
mainly including CNN-based, RNN-based and GAN-based                                                    and tested on monocular images or sequences, which are
models, where the CNN mainly learns the spatial features                                               trained with scene geometric constraints.
of the scene, the RNN learns the temporal information from
the video sequences, and GAN is introduced to generate and                                             (1) Stereo Matching. Unsupervised learning methods are
discriminate depth maps. Because the supervised learning                                               inspired by traditional stereo matching methods as shown in
methods need plenty of GT depth maps as the supervision,                                               Figure 10, which usually utilize left and right images to cal-
the accuracy rate is high when scale of the predicted depth                                            culate depth value [136]. The learning model is trained with
map is close to the GT depth map. They can effectively map                                             stereo pair-wise images and tested on single image, as shown
the 3D structure of the scene. However, GT depth maps                                                  in Figure 11. The depth network estimates the disparity map
are difficult to obtain. Therefore, depth estimation methods                                           between the left and right images, where the new image can
based on virtual images have attracted many researchers, and                                           be constructed with image warping based on the disparity
many unsupervised learning methods have emerged, which                                                 map and the right image. The pixel 𝑝(𝑠) can be obtained
do not require GT and reduce the requirements for datasets                                             through
with GT.

3.1.2. Unsupervised Learning Methods                                                                          𝑝(𝑠) ∼ 𝐾𝑇 (𝑡 → 𝑠)𝐷(𝑡)𝐾 −1 𝑝(𝑡)                              (2)
    Supervised learning methods need to input a large num-                                             where 𝐾 is the camera intrinsics matrix, 𝑇 (𝑡 → 𝑠) is the
ber of images with GT depth maps during the training stage.                                            transformation between left and right images, 𝐷(𝑡) is the es-
However, high-resolution publicly labeled datasets still need                                          timated depth map, and 𝑝(𝑡) is the homogeneous coordinate
                                       Deep Learning for Monocular Depth Estimation: A Review

of a pixel in the reconstructed image.                                                                     Feature
    Therefore, the depth network is constrained by the dif-                                                concatenation
                                                                                     2D CNN
ference, a reconstruction error, between the source and the
                                                                          Left
reconstructed image. Common image reconstruction loss                             Weight sharing                         3D
functions are 𝐿1 and 𝑆𝑆𝐼𝑀 [156] as follow:                               Right
                                                                                                                        CNN              Depth
                                                                                     2D CNN
               ∑                                                         Input   Feature capture
      𝐿𝑟𝑒𝑐 =       |𝐼(𝑝) − 𝐼 𝑤 (𝑝)|1                         (3)                                                  Cost volume

               𝑝                                                    Figure 12: The general model based on unsupervised 2D with

                                                                    3D CNNs for monocular depth estimation, where the weights
                                                                    of these two 2D CNNs are shared and the cost volume is con-
         1 − 𝑆𝑆𝐼𝑀(𝐼(𝑝) − 𝐼 𝑤 (𝑝))                                   strained with context information to mapping the depth map.
𝐿𝑟𝑒𝑐 = 𝛼                          +(1−𝛼)|𝐼(𝑝)−𝐼 𝑤 (𝑝)|1
                  2
                                                    (4)

where 𝐼(𝑝) and 𝐼 𝑤 (𝑝) represents the source image and the                                     Depth Network

warped image reconstructed from the source image, respec-
tively. 𝛼 is a weight between 𝐿1 norm and 𝑆𝑆𝐼𝑀 term.                  I(t-1)

     Unsupervised learning methods based on stereo match-                                                              Estimated depth
ing usually adopt CNNs for monocular depth estimation. Garg            I(t)                                                         Projection
et al. [34] adopted the general model as shown in Figure 11
to learn monocular depth maps in an unsupervised manner
with the reconstruction loss in 𝐿1 norm as Eq.(3) in 2016.           I(t+1)

On this basis, a number of researchers began to utilize the                                                              Camera pose

left and right views to train networks with stereo matching                                        Pose Network

based on 2D CNNs and 3D CNNs.                                       Figure 13: The general model of unsupervised learning based
     For 2D CNNs, Godard et al. [36] proposed the left-right        on monocular sequences for depth estimation, where the entire
consistency constraints to train the unsupervised network,          model estimates depth and camera pose simultaneously, and
where they reconstructed the left and right view simultane-         they project and interact with each other.

ously. Their model was constrained by the reconstruction
loss, the disparity smoothness loss, and the left-right dis-
parity consistency. Experiments proved that the addition of
the new loss functions enhanced the accuracy of the pre-                 Unsupervised learning models based on stereo matching
dicted depth map from each view. Moreover, Xie et al. [161]         is mainly constrained by the projection and mapping rela-
added a selection layer in image reconstruction, Wong et            tionship between the left and right pair-wise images, which
al. [158] designed a global-to-local network for feature ex-        still require the datasets containing stereo images. There-
traction, Goldman et al. [38] constructed a Siamese network         fore, how to utilize only a single camera in the training stage
to learn stereo images, Andraghetti et al. [3] enhanced the         for unsupervised monocular depth estimation has attracted
depth estimation with traditional visual odometry. Watson et        the attention of researchers.
al. [157] strengthened stereo matching with depth hints. Ur
et al. [115] applied unsupervised pre-trained filter method.        (2) Monocular Sequences. Unsupervised learning mod-
     For 3D CNNs, some researchers adopted context infor-           els trained with monocular sequences consider the scene struc-
mation to constrain unsupervised networks in 3D convolu-            ture and camera motion at the same time, where camera pose
tion blocks for monocular depth estimation [14, 59, 60], as         estimation is similar to the images transformation estimation
shown in Figure 12. During training, two 2D CNNs with               and has a positive impact on monocular depth estimation
shared weights learn feature maps from left and right im-           [168, 190, 195]. Recently, researchers have introduced the
ages, respectively. And then, these two groups of feature           visual odometry [105, 125] into the depth estimation based
maps are concatenated to the 3D convolution network in a            on monocular sequences, where the scene depth can be learned
cost volume module [15, 143] to estimate the final depth            by predicting the camera motion.
map combined with context information [42, 175]. Spe-                    The general model of unsupervised learning based on
cially, Chang et al. [14] proposed the PSMNet, trained in           monocular sequences for depth estimation is shown in Fig-
a top-down / bottom-up manner to perform unsupervised               ure 13, which consists of two sub-networks, depth network
monocular depth estimation, where a spatial pyramid pool-           for depth estimation and pose network for visual odometry,
ing module was used as a matching cost volume by aggre-             respectively. During the training stage, these two networks
gating semi-global environment information and a 3D con-            are trained jointly, and the entire model is constrained by
volution module adjusted the matching cost volume by com-           image reconstruction loss similar to stereo matching meth-
bining multiple stacked hourglass-based 3D CNNs with in-            ods. The difference is that the image warping is built on
termediate supervision.                                             adjacent frames of the monocular sequence. For loss func-
                                   Deep Learning for Monocular Depth Estimation: A Review

    Synthetic image      Depth Network     Synthetic GT depth                                                      Depth
                                                                                                                 consistency
                                                                      Sparse depth

                                                Training Stage

                                                                       RGB image          Depth network       Estimated depth

                                                                   Figure 15: The general model for monocular depth estimation

                                                                   with LIDAR, where the sparse depth is captured by LIDAR.

      Real image       Trained Network    Real estimated depth
                                                     Test Stage

                                                                   (1) Combined with Synthetic Data. The synthetic data
Figure 14:   The general model of domain adaptive methods
                                                                   generated by the graphics engine provides a possible solu-
for monocular depth estimation combined with synthetic data,
where the network in test stage is trained on synthetic data
                                                                   tion for collecting a large amount of depth data. Thus, re-
with GT in training stage.                                         searchers introduce synthetic datasets with depth labels to
                                                                   monocular depth estimation. How to overcome the domain
                                                                   gap between synthetic and real data is a challenge during
                                                                   training [10, 118].
tions, the smoothness loss and the photometric consistency              With the development of image style transfer and its con-
loss in stereo matching methods are adopted in the unsuper-        nection with domain adaptation, researchers adopted the style
vised methods based on monocular sequences apart from the          transfer and adversarial training to estimate depth maps in
reconstruction loss.                                               real scenes [5, 103], which relied on the models trained with
    Zhou et al. [194] designed two networks to estimate depth      a large amounts of synthetic data, as shown in Figure 14. The
maps and camera motion in the monocular video indepen-             depth estimation network is trained with synthetic images
dently, which could be trained jointly or separately with re-      and corresponding GT depth maps. During the test stage,
construction loss and photometric consistency loss functions       the trained network is applied directly to predict the depth
[144, 154] and tested on one image or monocular sequence.          maps from real RGB images with transfer learning to mini-
Their work provided many useful references for subsequent          mize the gap between the real and synthetic domain.
works, such as, models trained with 3D geometric constraints            DispNet [94] was the first network that introduced im-
[91, 167, 193], estimation with uncertainty or confidence          age style transfer for depth estimation. It utilized a large
maps [16, 107], networks designed with self-attention [57],        comprehensive synthetic dataset to train, and fine-tuned the
and others [2, 164, 176].                                          model on the less available GT data. Based on the DispNet,
                                                                   Zheng et al. [192] proposed a two-module domain adaptive
Summary. Unsupervised learning methods for monocular               network, 𝑇 2 Net, where one module was trained with syn-
depth estimation directly learn depth information from ge-         thetic and real images and reconstructed each other with the
ometric constraints. It mainly includes two types: one is          reconstruction loss and generative adversarial loss [21, 26,
based on the stereo matching, where the geometric constraints      39], and these outputs were input into the other module to
are built on the left and right images; the other is based on      predict the real depth maps. Besides, there are more mod-
monocular sequences, where the geometric constraints are           els with self-attention [191], cycle consistency [189], cross-
built on adjacent frames. Compared with the supervised             domain [44, 140, 141], and others for domain adaptation to
learning methods, unsupervised learning methods don’t need         predict monocular depth maps.
GT depth maps, which reduces the cost of building depth la-             Domain adaptation methods can successfully solve the
bels yet suffer from lower accuracy.                               domain difference of the deep end-to-end disparity estima-
                                                                   tion network. However, when the illumination or the satura-
3.1.3. Semi-supervised Learning Methods                            tion of the style transfer changes suddenly, the accuracy of
    In order to effectively utilize a large amount of relatively   the estimated depth map will decrease accordingly.
cheap unlabeled data to improve learning performance, re-
searchers have proposed the semi-supervised learning meth-         (2) Combined with LIDAR. Researchers also adopt aux-
ods, which introduces other information, such as synthetic         iliary depth sensors to capture GT information, such as LI-
data, surface normals, and LIDAR, as the semi-supervised           DAR, for monocular depth estimation [27, 31, 49, 65, 110].
learning manners to reduce the model’s dependence on GT            Auxiliary depth sensors cause some noises and the measured
depth maps, which enhance the scale consistency and im-            depth values are usually sparser than GT depth maps. The
prove estimated accuracy of depth maps.                            general model for monocular depth estimation with LIDAR
                                                                   is shown in Figure 15. The depth network learns not only
                                     Deep Learning for Monocular Depth Estimation: A Review

            Normal Network                                         Furthermore, there are some models with depth-normal con-
                         Estimated normal
                                                                   sistency [110, 167], surface regularized constraints [152, 187],
                                                                   and depth completion [184], for monocular depth estimation
                                                                   combined with surface normal estimation.
                                             Normal-
                                             to-Depth              Summary. Semi-supervised learning methods for monoc-
   Input                                                Refined    ular depth estimation relies on auxiliary information, such as
                                                         depth
                                                                   virtual data, sparse depth, and surface normals, apart from
                           Estimated depth                         learning the depth features from the RGB image, which makes
           Depth Network
                                                                   the depth map more accurate than that estimated in unsuper-
Figure 16: The general model for monocular depth estimation        vised learning methods. Although auxiliary information is
combined with surface normal estimation, where the normal-         easier to obtain than GT depth maps, it still increases the
to-depth module is depended on the geometric relationship          amount of input data and the dependence of depth estima-
between the depth and normal.                                      tion on it.

                                                                   3.1.4. Summary
                                                                       This section mainly reviews and summarizes the deep
structure features but also depth and noise from sparse data       learning methods for monocular depth estimation from the
captured by LIDAR, where the entire mode needs to add the          networks training manners, including: supervised, unsuper-
depth consistency constraint built on the sparse data and es-      vised, and semi-supervised learning methods. Supervised
timated depth map as follow:                                       learning methods for monocular depth estimation have the
                                                                   highest accuracy, yet strong dependence on GT depth maps;
                     ∑                                             unsupervised learning methods build geometric constraints
      𝐿𝑑𝑒𝑝𝑡ℎ (𝑝) =       ||𝐷(𝑝) − 𝑍(𝑝)||1                    (5)   on the input images to predict depth maps without supervi-
                     𝑝                                             sion, but its accuracy is slightly inferior to supervised learn-
where 𝑝 is the depth pixel, 𝐷(𝑝) is the estimated depth map,       ing and semi-supervised learning methods, where scale am-
and 𝑍(𝑝) is the sparse data from LIDAR.                            biguity, occlusion, and other problems need to be overcome;
    Kuznietsov et al. [65] proposed a semi-supervised learn-       semi-supervised learning methods depend on auxiliary in-
ing network for monocular depth estimation with sparse data,       formation, which are easier to obtain than GT depth maps.
which input left and right images to the model and built a         The summaries for different learning manners are concluded
stereo alignment as a geometric constraint. Thus, the depth        in Table 2.
consistency losses include two parts: one is the error be-
                                                                   3.2. Tasks
tween the left estimated depth map and sparse data, and the
                                                                       From the perspective of task types, deep learning meth-
other is the error between the right estimated depth map and
                                                                   ods for monocular depth estimation can be divided into two
sparse data. Experiments proved that the added sparse data
                                                                   categories. On the one hand, we can train a single network
did improve the performance than supervised and unsuper-
                                                                   only for depth estimation, that is single-task learning; on the
vised methods [28, 34, 36, 83].
                                                                   other hand, we can combine depth estimation with other re-
(3) Combined with Surface Normal. There are still                  lated tasks to learn together for the features projection and
some features with similar information to depth extracted          improve the depth estimation performance, that is multi-task
from the input RGB image, which contribute to predict the          learning. This section will review the two aspects of single-
depth maps more accurately and conveniently, e.g. surface          task learning and multi-task learning methods.
normal.
                                                                   3.2.1. Single-task Learning Methods
     There is a strong correlation between the surface normal
                                                                       The core of the single-task learning methods is to con-
and the depth: the surface normal is determined by the local
                                                                   struct an association model between the RGB image and the
tangent plane of the 3D point, which can be estimated from
                                                                   depth map, that is, the model is learned from the RGB im-
the depth; the depth is constrained by the local tangent plane
                                                                   age, and recover the depth value. According to whether the
determined by the surface normal. The general model for
                                                                   depth value returned by the network is continuous or not,
monocular depth estimation combined with surface normal
                                                                   single-task learning methods can be divided into regression
estimation is shown in Figure 16. Qi et al. [109] proposed
                                                                   methods and classification methods.
the GeoNet, which consists of a depth-to-normal network
exploiting the least square solution of the surface normal         (1) Regression Methods. Regression methods based on
from depth and a normal-to-depth network refining the ini-         deep learning usually learn scene structure features from in-
tial depth map in a kernel regression module. They took the        puts and regress continuous depth values to fit the input.
advantage of the theory that surface normals change less in        Most of the existing monocular depth estimation methods
local plane to refine monocular depth estimation, where the        are regression methods, which can directly obtain a depth
specific derivation process could be found in Reference [109].     map containing continuous pixel-level depth values. The
                                        Deep Learning for Monocular Depth Estimation: A Review

                      Table 2

                      A summary of the deep learning methods for monocular estimation in supervised, unsu-
                      pervised, and semi-supervised learning manners.

   Methods          Models              Descriptions                             Remarks                             Papers
                                        GT depth maps are used as the su-
                                                                                 High precision, simple framework,
   Supervised       Figure 7            pervision signal of the deep learn-                                          [29] [33] [69] [163]
                                                                                 yet heavy dependence on GT.
                                        ing network.
                                        Using epipolar geometric con-            GT is not required, but there are
   Unsupervised     Figure 11           straints instead of GT as the super-     problems such as scale blur, dy-    [34] [36] [38]
                                        vision.                                  namic blur, and occlusion.
                    Figure 14           Relying on virtual data, sparse
   Semi-                                                                         Heavy dependence on the auxil-
                    Figure 15           depth, surface normal and other                                              [65] [109] [192]
   supervised                                                                    iary information.
                    Figure 16           auxiliary information.

                                Depth

                                                                                                                       Depth
                                                                     l1   l2      l3   l4    l5    ...

                RGB                       Discretization
                                                                                                                      Mapping
                                                                                                               ...

             Ground truth                                        Depth Network
                                                                                             Segmented depth

Figure 17: The general model of classication methods for monocular depth estimation, where the discretization module discretizes

continuous depth values, and the mapping module combines the segmented depth maps into the nal depth map.

general model of regression methods is similar to Figure 5,                (2) Classification Methods. Depth estimation and se-
where the estimated depth values are continuous.                           mantic segmentation are similar, and both are pixel-level
    According to the deep learning model used, it can be di-               predictions. Taking into account the characteristics of the
vided into CNN-based [27, 69, 76], RNN-based [64, 162,                     scene from far to near, classification is also used to estimate
176], and GAN-based regression methods [45, 191]. Zhang                    monocular depth maps, as shown in Figure 17. Firstly, the
et al. [188] proposed an end-to-end progressive hard mining                continuous depth values are discretized. Then, the depth es-
network (PHN) to regress depth maps, in which an intra-                    timation network learns the corresponding classification la-
scale module restored the depth information, an inter-scale                bels for discretized depth values and regresses segmented
module fused the depth cues, and a hard-mining refinement                  depth maps. Finally, these segmented depth maps are com-
module constrained the recursive refining and reduced error                bined into the final depth map.
propagation to fully learn boundaries of different scales and                  There are several deep learning models in classification
estimate depth maps in regression.                                         for monocular depth estimation, such as full convolutional
    Ideally, the estimated depth values should be continuous.              models [11], residual models [74, 116, 134], and ordinal
However, regression methods for monocular depth estima-                    classification models [33, 87]. Fu et al. [33] put forward
tion are usually faced with more complex network structures                a deep ordered classification network to estimate monocu-
and constraint functions. Therefore, some researchers began                lar depth maps. It performed linear sampling on the depth
to discretize the depth values and introduced the classifica-              value in logarithmic space, and arranged all categories in de-
tion methods to learn depth maps.                                          scending order according to the distance relationship, where
                                                                           the discrete depth values were used for ordered regression
                                   Deep Learning for Monocular Depth Estimation: A Review

                              Back-                             segmentation consists of one encoder network and two de-
                           propagation
                                                                coder networks for depth regression and semantic labels pre-
                                                      Loss
                                                                diction, where these two decoder networks share weights, as
                                                                shown in Figure 18. During training, we can train only one or
                                             Depth              two-both tasks at the same time. The shared encoder learns
                            Sharing weight  Semantic  Attention feature maps from the input, yet two decoders with shared
                                           segmentati Guidance  weights to recover depth maps and semantic segmentations,
    RGB                                        on               respectively. Furthermore, the whole model is constrained
                                                      Loss      by the attention guidance from context information, and the
                                                                predicted results will be back-propagation to update network
                                 Back-                          parameters and optimize the results.
                              propagation
                                                                    Eigen et al. [28] were the first to unify the three tasks of
Figure 18: The general model for monocular depth estimation     depth, surface normal, and semantic annotation. Based on
combined with semantic segmentation, where the shared en-       that, more and more methods have been proposed for monoc-
coder captures the scene structure features and two separate    ular depth estimation with semantic segmentation. Atapour-
decoders perform semantic segmentation and depth regression     Abarghouei et al. [6] considered depth estimation as a super-
respectively.
                                                                vised image-to-image translation problem with a generative
                                                                network and applied adversarial learning to force the model
                                                                to select a mode to overcome the multi-modal problem re-
                                                                sulting in blurry outputs. For semantic segmentation, they
network training. Experiments proved that treating depth es-    applied a fully supervised generative network trained with
timation as a regression problem might lead to larger errors    cross-entropy loss functions. What’s more, models with self-
in areas too far or too close to the camera, while treating as  attention [55], instance segmentation [17, 150], multi-scale
a classification problem could effectively avoid a relatively   learning [100], guidance manner [18, 43], and others [81,
large error for predicting a larger depth value.                187] are proposed to estimate monocular depth combined se-
                                                                mantic segmentation. Experiments proved that the addition
Summary. Single-task learning methods for monocular depth
                                                                of semantic information did increase the accuracy of monoc-
estimation mainly include regression and classification meth-
                                                                ular depth estimation.
ods, where the regression methods directly returns continu-
                                                                    Monocular depth estimation combined with semantic seg-
ous depth values, and the classification methods discretize
                                                                mentation can take advantage of the context information of
the depth values firstly and then regress those in piecewise.
                                                                the scene, overcoming problems such as object boundaries
However, the network and constraint functions of the regres-
                                                                blur and improving the accuracy of the predicted depth maps.
sion are becoming more and more complex, and it is easy
to cause local minima; and the classification method has a      (2) Combined with others. In addition to combining with
strong dependence on the discretization form and weight set-    semantic segmentation tasks, depth estimation based on monoc-
ting, otherwise the loss will be increased.                     ular video is often combined with other tasks, such as vi-
                                                                  sual odometry [20, 30, 179] and optical flow estimation [169,
3.2.2. Multi-task Learning Methods
                                                                  173].
    In order to make full use of the complementarity of the
                                                                      Visual odometry is similar to the images transformation
depth and other features, researchers have proposed to de-
                                                                  estimation and accurate camera pose estimation contributes
sign a unified framework for joint multi-task training, and the
                                                                  to image reconstruction and further helps depth estimation [168,
features extracted from different tasks are projected to each
                                                                  190, 195]. However, most early methods only consider static
other to enhance the final depth map. This section introduces
                                                                  scenes, which are no longer applicable in the dynamic scene
the depth estimation methods combined with semantic seg-
                                                                  actually. Because there are usually dynamic objects in real
mentation in monocular images and the methods combined
                                                                  scenes, such as cars and pedestrians. In order to better esti-
with visual odometry, optical flow estimation, and others in
                                                                  mate the depth maps of the dynamic scene, researchers have
monocular videos.
                                                                  introduced optical flow estimation into monocular depth es-
(1) Combined with Semantic Segmentation. Scene                    timation. Optical flow estimation can capture motion in-
perception includes many aspects, where depth information         formation in the scene, which contributes to the monocular
describes the geometric relationship in space, and the se-        depth estimation of dynamic scenes [92].
mantic information represents the entity meaning of different         Based on the combination with visual odometry and op-
parts in the scene [90, 106, 171]. These tasks share similar      tical flow estimation, there are a large quantity of works deal-
context information [24, 79]. Many works have been pro-           ing with dynamic objects in the scene and the problems of
posed to combine semantic segmentation with depth estima-         occlusion and motion blur [37, 112, 153]. The general model
tion, processing data under the same neural network [56, 98,      of monocular depth estimation with visual odometry and flow
113, 186].                                                        estimation is shown in Figure 19, which usually consists of
    The model for monocular depth estimation and semantic         multiple sub-networks and each sub-network performs a dif-
                                    Deep Learning for Monocular Depth Estimation: A Review

                                                                 the task types, including single-task learning and multi-task
                                                                 learning methods. Single-task learning methods usually es-
                                                        Depth
                                                                 timate monocular depth maps in regression or classification
                        Depth Network                            manner, distinguished from whether the returned depth val-
                                                                 ues are continuous or discrete. Multi-task learning methods
                                                                 usually combine depth estimation with semantic segmen-
                         Flow Network
                                                        Flow     tation, camera pose, and scene flow estimation, which are
                                                                 trained jointly and interact with each other. The summaries
     Input
                                                                 for different learning tasks are concluded in Table 3.

                         Pose Network            Pose
                                                                 4. Datasets and Metrics
Figure 19: The general model for monocular depth estimation

combined with visual odometry and ow estimation, which
                                                                     This section introduces the datasets and evaluation met-
includes three sub-networks: the depth network, the ow net-
                                                                 rics of deep learning models for monocular depth estimation.
work, and the pose network for depth, scene ow, and camera
pose estimation, respectively.                                   4.1. Datasets
                                                                     There are a number of datasets for monocular depth es-
                                                                 timation, with different types and depth ranges between in-
                                                                 door and outdoor scenes. This section introduces some com-
ferent task. All tasks are jointly trained and the estimation    mon datasets in deep learning methods for monocular deep
of each task project and promote each other.                     estimation.
    For dynamic objects and occlusion, Godard et al. [37]
proposed an automatic occlusion method, Monodepth2, which        KITTI. KITTI dataset [35] is an outdoor dataset for monoc-
minimized photometric error to reduce the artifacts at the       ular deep estimation and object detection and tracking based
object boundary, and improved the sharpness of the occlu-        on deep learning, which is jointly developed by Karlsruhe
sion boundary. At the same time, they put forward an auto-       Institute of Technology in Germany and Toyota Institute of
masking method to filter out some pixels that didn’t change      Technology in the United States, as shown in Figure 20(a).
in appearance when dynamic objects moved at the same speed       KITTI dataset is captured through a car equipped with 2
as the camera in the scene. Moreover, there are some meth-       high-resolution color cameras, 2 gray-scale cameras, laser
ods dealing dynamic objects with object masks [147], object      scanner and global positioning system (GPS), whose max-
motion estimation [12], flow consistency [97, 153], displace-    imum measuring distance is 120m. The dataset contains a
ment field [112], etc.                                           total of 93,000 RGB-D training samples, including five cate-
    In addition to combining visual odometry and optical         gories: “Road”, “City”, “Residential”, “Campus”, and “Per-
flow estimation, there are some works that combine features      son”, from the city of Karlsruhe, the wild area and the high-
estimation for further pixel-level depth maps estimation [129,   way. The original image size of KITTI is 1,242 × 375, and
133, 174]. For example, Spencer et al. [133] proposed an un-     its ground-truth depth maps are sparse.
supervised network framework, DeFeat-Net, that could si-
                                                                 NYU Depth V2. NYU Depth V2 dataset [130] is an in-
multaneously learn monocular depth, dense feature repre-
                                                                 door dataset for monocular depth estimation based on deep
sentation, and self-motion. It was robust and could work in
                                                                 learning, which is provided by Silbereman et al. at the New
many challenging environments, such as changing weather
                                                                 York University. NYU Depth V2 dataset contains 407,024
and light conditions, with established pixel-wise loss func-
                                                                 frames of RGB-D image pairs captured by a Red-Green-Blue
tions [23, 72, 132].
                                                                 (RGB) camera and the Microsoft Kinect depth camera to si-
Summary. Multi-task learning methods for monocular depth         multaneously collect the RGB and depth information of 464
estimation usually predict depth maps with other tasks, such     different indoor scenes. The original image size of NYU
as semantic segmentation, visual odometry, and scene opti-       Depth V2 is 640 × 480 and the depth of the dataset ranges
cal flow estimation. By capturing features related to depth      from 0.5m to 10m. Due to the positional deviation between
information in the scene, the accuracy of depth estimation       the RGB and the depth camera, the original depth maps con-
is improved and the scene understanding is enhanced. How-        tain missing parts or noises. Therefore, authors select 1,449
ever, there are still many challenges in multi-task learning     images from the dataset and use the coloring algorithm [73]
that need to be overcome, such as limited datasets with se-      to fill and obtain dense depth maps, which are manually la-
mantic labels or missing labels, motion blur and occlusion       beled with the semantic information. The 1,449 samples
caused by dynamic objects in the scene.                          are divided into 795 training samples and 654 test samples.
                                                                 Some samples of NYU Depth V2 dataset are shown in Fig-
3.2.3. Summary                                                   ure 20(b).
    This section mainly reviews and summarizes the deep
learning methods for monocular depth estimation based on         Make3D. Make3D dataset [123, 124] is another outdoor
                                                                 dataset for monocular depth estimation based on deep learn-
                                 Deep Learning for Monocular Depth Estimation: A Review

                  Table 3

                  A summary of the single-task and multi-task learning methods for monocular estimation,
                  where multi-task learning methods include depth estimation with semantic segmentation.

   Methods        Models          Descriptions                        Remarks                                Papers
                                  Only perform a single-task of       Predicting monocular depth maps
   Single-task    Figure 7                                                                                   [33] [87] [188]
                                  monocular depth estimation.         by regression or classification.
   Depth with                     Adopting the complementarity be-
                                                                      The accuracy of depth estimation
   semantic                       tween depth information and se-
                  Figure 18                                           is improved by applying context        [6] [18] [28] [55]
   segmenta-                      mantic information for multi-task
                                                                      information.
   tion                           learning.
                                  Using inter-frames geometric con-   No need for GT, but problems with
   Depth with                                                                                                [37] [133]        [169]
                  Figure 19       straints and image reconstruction   scale blur, re-projection, dynamic
   others                                                                                                    [194]
                                  to learn multi-task estimations.    blur, and occlusion.

                      (a)

                                                                                                           (c)

                     (b)

                                                                                                           (d)

Figure 20: Samples of monocular depth estimation datasets. (a) is KITTI dataset [35], (b) is NYU Depth V2 dataset [130], (c)

is Make3D dataset [123, 124], and (d) is SceneNet RGB-D dataset [95] (the left images are RGB images and the right are the
ground-truth depth maps).

ing, which is constructed by Saxena et al. in Stanford Uni-       ferent weather, environment, and lighting conditions. The
versity. Make3D dataset includes daytime city and natural         appropriate dataset should be selected according to the spe-
scenery, with depth maps being collected by a laser scanner.      cific task in research. Some samples of SceneNet RGB-D
The depth ranges from 5 m to 81 m, and the range larger           dataset are shown in Figure 20(d).
than that is uniformly mapped to 81 m. This dataset con-
tains a total of 534 RGB-D image pairs, 400 of which are          4.2. Metrics
used for training and 134 are used for testing. The original          Evaluation metrics proposed by Eigen et al. [29] is adopted
resolution of the RGB image is 2,272 × 1,704, and the res-        to evaluate and compare the performance of depth estima-
olution of the depth map is 55 × 305 pixels. Some samples         tion methods. Evaluation metrics include error and accuracy
of Make3D dataset are shown in Figure 20(c).                      metrics. The error metrics (smaller is better) include ab-
                                                                  solute relative error (Abs.rel), square relative error (Sq.rel),
Virtual Datasets. The above datasets, KITTI, NYU Depth            root mean square error (RMSE), and the logarithm root mean
V2, and Make3D, are all collected from real scenes. There         square error (log RMS); the accuracy rate metrics (the big-
are some virtual datasets generated by computers, such as         ger the better) include 𝛿 < 1.25𝑡 , where 𝑡 = 1,2,3. These
SceneNet RGB-D dataset [95], and SYNTHIA dataset [121].
These virtual datasets include various scene types under dif-
                                      Deep Learning for Monocular Depth Estimation: A Review

metrics are formulated as:                                                Integration and optimization of the network frame-
               √                                                          work. In many supervised learning models, semantic seg-
                  1∑
      𝑅𝑀𝑆 ∶             ||𝑑 − 𝑑𝑖𝑔𝑡 ||2                              (6)   mentation will be added with depth estimation, but it is still
                  𝑇 𝑖∈𝑇 𝑖                                                 an independent module that handles independent tasks. In
                                                                          the unsupervised learning methods, there are generally mul-
                    √
                        1∑         ( )      ( )                           tiple sub-networks which are able to learn depth estimation,
      𝑙𝑜𝑔 𝑅𝑀𝑆 ∶               ||𝑙𝑜𝑔 𝑑𝑖 − 𝑙𝑜𝑔 𝑑𝑖𝑔𝑡 ||2               (7)   visual odometry, and flow estimation, respectively. How-
                        𝑇 𝑖∈𝑇
                                                                          ever, these networks are not well connected, which leads to a
                                                                          large number of parameters increasing the memory require-
                        1 ∑ 𝑑𝑖 − 𝑑𝑖
                                          𝑔𝑡
                                                                          ments and calculations. How to better integrate the network
      𝑎𝑏𝑠. 𝑟𝑒𝑙𝑎𝑡𝑖𝑣𝑒 ∶                                               (8)   is a research direction and is worth exploring in the future.
                        𝑇 𝑖∈𝑇 𝑑 𝑔𝑡
                                  𝑖                                            We can obtain different features at the same time by us-
                                                                          ing the same deep learning network, such as semantic in-
                                          𝑔𝑡 2
                       1 ∑ ||𝑑𝑖 − 𝑑𝑖 ||                                   formation, optical flow features, and depth features. In the
      𝑠𝑞. 𝑟𝑒𝑙𝑎𝑡𝑖𝑣𝑒 ∶                                                (9)
                       𝑇 𝑖∈𝑇    𝑑 𝑔𝑡                                      encoding stage, different types of features are extracted and
                                      𝑖
                                                                          matched at the same time; in the decoding stage, they are
                                           (              )               decoded separately to meet the application requirements.
                                                     𝑔𝑡
                                               𝑑𝑖 𝑑𝑖
     𝑎𝑐𝑐𝑢𝑟𝑎𝑐𝑖𝑒𝑠 ∶ % 𝑜𝑓 𝑑𝑖 𝑠.𝑡. 𝑚𝑎𝑥                 ,          = 𝛿 < 𝑡ℎ𝑟   Datasets construction. The quality of datasets largely
                                               𝑑 𝑔𝑡 𝑑𝑖
                                                 𝑖                        determines the generalization ability and robustness of the
                                                                   (10)   deep learning model. In order to improve the results of depth
where 𝑑𝑖 and 𝑑𝑖𝑔𝑡 are the predicted and ground-truth depth re-            estimation, more data, with better quality and more scene
spectively at the pixel indexed by 𝑖, and T is the total number           types, is needed. However, these existing datasets used for
of pixels in all the evaluated images.                                    depth estimation are relatively limited, and the construction
                                                                          of a new dataset is time-consuming and expensive. At present,
4.3. Analysis and Comparisons                                             some researchers utilize computers to generate a large num-
    In order to evaluate and compare these monocular depth                ber of images for depth estimation, but the quality is uneven.
estimation methods based on deep learning, we adopted the                 How to construct a dataset for monocular depth estimation
publicly available pre-trained networks trained or tested on              that meets deep learning is a future research direction.
KITTI [35] dataset. Table 4 illustrates some properties of the
deep learning methods, including year, supervision, main                  Dynamic objects and occlusion problems. Realistic
contributions, tasks, and training data. The performance                  scenes are usually complicated, such as containing a large
comparison of various methods is listed in Table 5, includ-               number of moving objects, occlusions, illumination changes,
ing error metrics and accuracy metrics. We don’t describe                 weather changes. However, most of the existing depth esti-
the properties and performance of all the methods mentioned               mation models only consider the ideal conditions. Although
above, but only summarize some representative models.                     some researchers have begun to deal with dynamic objects
                                                                          and occlusion scenes and have made some progress recently,
                                                                          how to better estimate the depth of complex scenes to meet
5. Challenges and Trends                                                  practical applications is still a very challenging task, which
    Over the past several years, monocular depth estimation               is an important future research direction.
based on deep learning has been extensively researched and
developed. However, there are still some limitations needed               High-resolution depth map output. Depth estimation
to be overcome.                                                           is a fundamental step for practical applications such as aug-
    1) In order to improve the accuracy, researchers deepen               mented reality (AR) and virtual reality (VR), and it has a
the layers of the deep neural networks, which increases the               high demand for the accuracy and resolution of the depth
memory usage and space complexity.                                        map. However, the resolution of the depth predicted by most
    2) In multi-task learning, deep learning methods for monoc-           of the current depth estimation models is usually low, for the
ular depth estimation always apply multiple sub-networks or               purpose of improving calculation efficiency. At present, re-
sub-modules to process different sub-tasks, which increases               searchers have used color image super-resolution models [77,
the amount of calculation and memory consumption.                         80, 108] to refine the super-resolution of depth maps [104,
    3) Monocular depth estimation networks usually are enco-              120, 160]. But how to directly output the high-resolution
ding-decoding networks. After multiple layers of informa-                 depth map is still a direction that needs to be studied.
tion processing, the depth features are severely lost, which
leads to the low-accuracy estimated depth maps and cannot                 Real-time performance. Image depth estimation is the
meet the requirements of practical applications.                          basic module of SLAM, which is closely integrated with in-
    In this section, this paper summarizes the key challenges             dustrial applications, such as autonomous driving. There-
and looks at the directions for future research of monocular              fore, practical applications have high requirements for the
depth estimation.                                                         real-time performance of depth estimation. However, in or-
                                Deep Learning for Monocular Depth Estimation: A Review

                  Table 4

                  Properties of the deep learning methods for monocular depth estimation. Sup.           is S
                  representing the supervised, U representing the unsupervised, and Semi representing
                  the semi-supervised method. Data is the training data, where RGB-D means RGB and
                  depth maps, Stereo means stereo images, Mono.seq means monocular sequences, and
                  Stereo.seq means stereo sequences.

    Papers            Year    Sup.   Main Contributions                       Tasks                        Data

  Eigen [29]          2014     S     Coarse-to-ne, CNN                       Depth                        RGB-D
                                                                              depth, normal, semantic      RGB-D,       semantic
  Eigen [28]          2015     S     Multi-scale, CNN.
                                                                              annotation                   labels
                                     Relative dense depth, numerical
 Zoran [197]          2015     S                                              Depth                        RGB-D
                                     optimization, residual network
  Laina [69]          2016     S     BerHu loss, residual network             Depth                        RGB-D
                                     Two-stream framework, depth-
    Li [76]           2017     S                                              Depth                        RGB-D
                                     gradient fusion, CNN
   Xu [163]           2018     S     Cascade-CRFs, attention model            Depth                        RGB-D
 Mancini [93]         2017     S     Convolution+LSTM                         Depth                        Mono.seq+depth
  Kumar [64]          2018     S     ConvLSTM                                 Depth                        Mono.seq+depth
  Jung [58]           2017     S     GAN, global-to-local                     Depth                        RGB-D
   Garg [34]          2016     U     Image reconstruction, CNN                Depth                        Stereo
                                     Left-right photometric and dis-
 Godard [36]          2017     U     parities    consistency,     disparity   Depth                        Stereo.seq
                                     smoothness loss
                                     Reconstruction and photometric
  Zhou [194]          2017     U                                              Depth, camera pose           Mono.seq
                                     consistency loss
                                     Spatial pyramid pooling module,
  Chang [14]          2018     U                                              Depth                        Stereo
                                     2D+3D CNN
                                     Bundle      adjustment,        super-
  Zhou [193]          2018     U                                              Depth, camera pose           Mono.seq
                                     resolution, clip loss
                                     Siamese      network,      geometric
Goldman [38]          2019     U                                              Depth                        Stereo
                                     consistency
 Guizilini [42]       2020     U     3D packing, SfM-based                    Depth, camera pose           Mono.seq
 Poggi [107]          2020     U     Depth uncertainty estimation             Depth                        Mono.seq
 Zheng [192]          2018    Semi   Domain adaptive, GAN                     Depth                        Synthetic RGB-D
                                     Domain adaptive, cycle consis-
  Zhao [189]          2019    Semi                                            Depth                        Synthetic RGB-D
                                     tency, GAN
                                     LIDAR, stereo geometric con-
Kuznietsov [65]       2017    Semi                                            Depth                        Stereo, sparse GT
                                     straint
                                     LIDAR, binary mask, attenetion
  Qiu [110]           2019    Semi                                            Depth, normal                RGB, sparse GT
                                     map
                                     Normal-to-depth, depth-normal
   Qi [109]           2018    Semi                                            Depth, normal                RGB
                                     consistency
                                                                              Depth, normal, semantic      RGB, semantic la-
 Zhang [187]          2019    Semi   Cross-task, anity learning
                                                                              segmentation                 bels
                                     Sparse-to-Continuous,         Hilbert
   Dos [27]           2019    Semi                                            Depth                        RGB, sparse GT
                                     maps [114], occupancy map
                                     Progressive    hard     mining    net-
 Zhang [188]          2018     S     work,       learning       multi-scale   Depth                        RGB-D
                                     boundaries
    Fu [33]           2018     S     Ordered regression                       Depth                        RGB-D
                                     ConvLSTM,       ordinal     classica-
   Liu [87]           2020     S                                              Depth                        Mono.seq
                                     tion
                                     Temporally     consistency,      depth   Depth,   ow,    semantic
 Atapour [6]          2019     U                                                                           Mono.seq
                                     completion, GAN                          segmentation
                                     Semantic      Divide-and-Conquer         Depth, semantic and in-
 Wang [150]           2020     U                                                                           Mono.seq
                                     Network                                  stance segmentation
                                     Per-pixel minimum re-projection
 Godard [37]          2019     U     and multi-scale estimation for           Depth, camera pose           Mono.seq
                                     occlusion
                                     Minimun      re-projection,      auto-   Depth,   dense    feature,
Spencer [133]         2020     U                                                                           Mono.seq
                                     masking                                  camera pose
                                    Deep Learning for Monocular Depth Estimation: A Review

                   Table 5

                   Evaluation on KITTI dataset and best result is emboldened and bolded. The slower of the
                   error metrics, the better; and the higher of the accuracy metrics, the better. Sup. is S
                   representing a supervised method, U representing an unsupervised method, and Semi
                   representing a semi-supervised method.

             Methods            Sup.     Abs.rel   Sq.rel   RMSE      log RMS        𝛿 < 1.25      𝛿 < 1.252      𝛿 < 1.253
             Eigen [29]         S        0.203     1.548    6.307     0.282          0.702         0.890          0.958
             Liu [83]           S        0.201     1.584    6.471     0.273          0.680         0.898          0.967
             Mancini [93]       S        0.312     0.107    5.654     0.366          0.512         0.786          0.911
             Kumar [64]         S        0.137     1.019    5.187     0.218          0.809         0.928          0.971
             Xu [163]           S        0.122     0.897    4.677     -              0.818         0.954          0.985
             Fu [33]            S        0.072     0.307    2.727     0.120          0.932         0.984          0.994
             Chen [18]          S        0.118     0.905    5.096     0.211          0.839         0.945          0.977

             Garg [34]          U        0.152     1.226    5.849     0.246          0.784         0.921          0.967
             Godard [36]        U        0.148     1.344    5.927     0.247          0.862         0.960          0.964
             Wong [158]         U        0.133     1.126    5.515     0.231          0.826         0.934          0.969
             Goldman [38]       U        0.113     0.898    5.048     0.208          0.853         0.948          0.976
             Andraghetti [3]    U        0.091     0.548    3.690     0.181          0.892         0.956          0.979
             Watson [157]       U        0.106     0.780    4.695     0.193          0.875         0.958          0.980
             Guizilini [42]     U        0.078     0.420    3.485     0.121          0.931         0.986          0.996
             Atapour [6]        U        0.193     1.438    5.887     0.234          0.836         0.930          0.958
             Zhou [194]         U        0.208     1.768    6.856     0.283          0.678         0.885          0.957
             Yin [169]          U        0.155     1.296    5.857     0.233          0.793         0.931          0.973
             Casser [12]        U        0.109     0.825    4.750     0.1866         0.874         0.958          0.983
             Wang [153]         U        0.112     0.418    2.320     0.153          0.882         0.974          0.992
             Godard [37]        U        0.115     0.903    4.863     0.193          0.877         0.959          0.981
             Johnston [57]      U        0.106     0.861    4.699     0.185          0.889         0.962          0.982
             Spencer [133]      U        0.126     0.925    5.035     0.200          0.862         0.954          0.980
             Shu [129]          U        0.104     0.729    4.481     0.179          0.893         0.965          0.984

             Dos [27]           Semi     0.123     0.641    4.525     0.199          0.881         0.966          0.986
             Atapour [5]        Semi     0.110     0.929    4.726     0.194          0.923         0.967          0.984
             Zhao [189]         Semi     0.143     0.756    3.846     0.217          0.836         0.946          0.976
             Zhao [191]         Semi     0.143     0.927    4.679     0.246          0.798         0.922          0.968

der to obtain higher accuracy, researchers often construct          References
deeper networks, with more parameters and more constraints,
                                                                     [1] Alam, M., Samad, M.D., Vidyaratne, L., Glandon, A., Iftekharud-
to perform depth estimation, which requires more calcula-                din, K.M., 2020. Survey on deep neural networks in speech and
tion time and thus cannot meet the real-time requirements of             vision systems. Neurocomputing .
practical applications. Therefore, how to apply a lighter net-       [2] Almalioglu, Y., Saputra, M.R.U., de Gusmao, P.P., Markham, A.,
work for real-time estimation while ensuring the accuracy of             Trigoni, N., 2019. Ganvo: Unsupervised deep monocular vi-
                                                                         sual odometry and depth estimation with generative adversarial net-
prediction is a future research direction.                               works, in: 2019 International Conference on Robotics and Automa-
                                                                         tion (ICRA), IEEE. pp. 5474–5480.
                                                                     [3] Andraghetti, L., Myriokefalitakis, P., Dovesi, P.L., Luque, B., Poggi,
6. Conclusion                                                            M., Pieropan, A., Mattoccia, S., 2019. Enhancing self-supervised
    Monocular depth estimation plays an important role in                monocular depth estimation with traditional visual odometry, in:
                                                                         2019 International Conference on 3D Vision (3DV), IEEE. pp. 424–
scene understanding and high-accuracy depth maps are ben-
                                                                         433.
eficial to the realization of multiple applications. This pa-        [4] Arjovsky, M., Chintala, S., Bottou, L., 2017. Wasserstein gan. arXiv
per introduces related deep learning models and summarizes               preprint arXiv:1701.07875 .
deep learning-based monocular depth estimation algorithms,           [5] Atapour-Abarghouei, A., Breckon, T.P., 2018. Real-time monoc-
from training manners to task types. Furthermore, this pa-               ular depth estimation using synthetic data with domain adaptation
                                                                         via image style transfer, in: Proceedings of the IEEE Conference on
per also summarizes the properties and performance of these
                                                                         Computer Vision and Pattern Recognition, pp. 2800–2810.
monocular depth estimation methods. Finally, this paper              [6] Atapour-Abarghouei, A., Breckon, T.P., 2019. Veritatem dies aperit-
identifies the potential challenges and suggests some future             temporally consistent depth prediction enabled by a multi-task geo-
research directions of the monocular depth estimation based              metric and semantic scene understanding approach, in: Proceedings
on deep learning.                                                        of the IEEE Conference on Computer Vision and Pattern Recogni-
                                                                         tion, pp. 3373–3384.
                                                                     [7] Bay, H., Tuytelaars, T., Van Gool, L., 2006. Surf: Speeded up robust
                                          Deep Learning for Monocular Depth Estimation: A Review

     features, in: European conference on computer vision, Springer. pp.            continuous: Enhancing monocular depth estimation using occu-
     404–417.                                                                       pancy maps, in: 2019 19th International Conference on Advanced
 [8] Bhoi, A., 2019. Monocular depth estimation: A survey. arXiv                    Robotics (ICAR), IEEE. pp. 793–800.
     preprint arXiv:1901.09402 .                                               [28] Eigen, D., Fergus, R., 2015. Predicting depth, surface normals and
 [9] Bosch, A., Zisserman, A., Munoz, X., 2007. Image classification                semantic labels with a common multi-scale convolutional architec-
     using random forests and ferns, in: 2007 IEEE 11th international               ture, in: Proceedings of the IEEE international conference on com-
     conference on computer vision, Ieee. pp. 1–8.                                  puter vision, pp. 2650–2658.
[10] Cao, X., Chen, B., Zeng, N., 2020. A deep domain adaption model           [29] Eigen, D., Puhrsch, C., Fergus, R., 2014. Depth map prediction
     with multi-task networks for planetary gearbox fault diagnosis. Neu-           from a single image using a multi-scale deep network, in: Advances
     rocomputing 409, 173–190.                                                      in neural information processing systems, pp. 2366–2374.
[11] Cao, Y., Wu, Z., Shen, C., 2017. Estimating depth from monocu-            [30] Facil, J.M., Ummenhofer, B., Zhou, H., Montesano, L., Brox, T.,
     lar images as classification using deep fully convolutional residual           Civera, J., 2020. Cam-convs: Camera-aware multi-scale convolu-
     networks. IEEE Transactions on Circuits and Systems for Video                  tions for single-view depth, in: Proceedings of the IEEE Conference
     Technology 28, 3174–3182.                                                      on Computer Vision and Pattern Recognition, IEEE. pp. 11826–
[12] Casser, V., Pirk, S., Mahjourian, R., Angelova, A., 2019. Depth pre-           11835.
     diction without the sensors: Leveraging structure for unsupervised        [31] Fei, X., Wong, A., Soatto, S., 2019. Geo-supervised visual depth
     learning from monocular videos, in: Proceedings of the AAAI Con-               prediction. IEEE Robotics and Automation Letters 4, 1661–1668.
     ference on Artificial Intelligence, pp. 8001–8008.                        [32] Feng, T., Gu, D., 2019. Sganvo: Unsupervised deep visual odometry
[13] Ceni, A., Ashwin, P., Livi, L., 2020. Interpreting recurrent neu-              and depth estimation with stacked generative adversarial networks.
     ral networks behaviour via excitable network attractors. Cognitive             IEEE Robotics and Automation Letters 4, 4431–4437.
     Computation 12, 330–356.                                                  [33] Fu, H., Gong, M., Wang, C., Batmanghelich, K., Tao, D., 2018.
[14] Chang, J.R., Chen, Y.S., 2018. Pyramid stereo matching network,                Deep ordinal regression network for monocular depth estimation,
     in: Proceedings of the IEEE Conference on Computer Vision and                  in: Proceedings of the IEEE Conference on Computer Vision and
     Pattern Recognition, pp. 5410–5418.                                            Pattern Recognition, pp. 2002–2011.
[15] Chen, C., Chen, X., Cheng, H., 2019a. On the over-smoothing prob-         [34] Garg, R., Bg, V.K., Carneiro, G., Reid, I., 2016. Unsupervised cnn
     lem of cnn based disparity estimation, in: Proceedings of the IEEE             for single view depth estimation: Geometry to the rescue, in: Euro-
     International Conference on Computer Vision, pp. 8997–9005.                    pean conference on computer vision, Springer. pp. 740–756.
[16] Chen, L., Tang, W., Wan, T.R., John, N.W., 2020a. Self-supervised         [35] Geiger, A., Lenz, P., Urtasun, R., 2012. Are we ready for au-
     monocular image depth learning and confidence estimation. Neuro-               tonomous driving? the kitti vision benchmark suite, in: 2012 IEEE
     computing 381, 272–281.                                                        Conference on Computer Vision and Pattern Recognition, IEEE. pp.
[17] Chen, L., Yang, Z., Ma, J., Luo, Z., 2018. Driving scene perception            3354–3361.
     network: Real-time joint detection, depth estimation and semantic         [36] Godard, C., Mac Aodha, O., Brostow, G.J., 2017. Unsupervised
     segmentation, in: 2018 IEEE Winter Conference on Applications of               monocular depth estimation with left-right consistency, in: Proceed-
     Computer Vision (WACV), IEEE. pp. 1283–1291.                                   ings of the IEEE Conference on Computer Vision and Pattern Recog-
[18] Chen, P.Y., Liu, A.H., Liu, Y.C., Wang, Y.C.F., 2019b. Towards                 nition, pp. 270–279.
     scene understanding: Unsupervised monocular depth estimation              [37] Godard, C., Mac Aodha, O., Firman, M., Brostow, G.J., 2019. Dig-
     with semantic-aware representation, in: Proceedings of the IEEE                ging into self-supervised monocular depth estimation, in: Proceed-
     Conference on Computer Vision and Pattern Recognition, pp. 2624–               ings of the IEEE international conference on computer vision, pp.
     2632.                                                                          3828–3838.
[19] Chen, W., Fu, Z., Yang, D., Deng, J., 2016. Single-image depth per-       [38] Goldman, M., Hassner, T., Avidan, S., 2019. Learn stereo, infer
     ception in the wild, in: Advances in neural information processing             mono: Siamese networks for self-supervised, monocular, depth es-
     systems, pp. 730–738.                                                          timation, in: Proceedings of the IEEE Conference on Computer Vi-
[20] Chen, W., Qian, S., Deng, J., 2019c. Learning single-image depth               sion and Pattern Recognition Workshops, pp. 0–0.
     from videos using quality assessment networks, in: Proceedings of         [39] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley,
     the IEEE Conference on Computer Vision and Pattern Recognition,                D., Ozair, S., Courville, A., Bengio, Y., 2014. Generative adversar-
     pp. 5604–5613.                                                                 ial nets, in: Advances in neural information processing systems, pp.
[21] Chen, Y., Zhao, Y., Jia, W., Cao, L., Liu, X., 2020b. Adversarial-             2672–2680.
     learning-based image-to-image transformation: A survey. Neuro-            [40] Gorban, A.N., Mirkes, E.M., Tyukin, I.Y., 2019. How deep should
     computing 411, 468–486.                                                        be the depth of convolutional neural networks: A backyard dog case
[22] Cho, K., Van Merriënboer, B., Gulcehre, C., Bahdanau, D.,                      study. Cognitive Computation , 1–10.
     Bougares, F., Schwenk, H., Bengio, Y., 2014. Learning phrase rep-         [41] Gregor, K., Danihelka, I., Graves, A., Rezende, D.J., Wierstra, D.,
     resentations using rnn encoder-decoder for statistical machine trans-          2015. Draw: A recurrent neural network for image generation. arXiv
     lation. arXiv preprint arXiv:1406.1078 .                                       preprint arXiv:1502.04623 .
[23] Choy, B.C., Gwak, J., Savarese, S., Chandraker, M., 2016. Uni-            [42] Guizilini, V., Ambrus, R., Pillai, S., Raventos, A., Gaidon, A.,
     versal correspondence network, in: Advances in neural information              2020a. 3d packing for self-supervised monocular depth estimation,
     processing systems, pp. 2414–2422.                                             in: Proceedings of the IEEE/CVF Conference on Computer Vision
[24] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2001. In-              and Pattern Recognition, pp. 2485–2494.
     troduction to algorithms, third edition thomas h. cormen, charles e.      [43] Guizilini, V., Hou, R., Li, J., Ambrus, R., Gaidon, A., 2020b.
     leiserson, ronald l. rivest, clifford stein. Journal of the Operational        Semantically-guided representation learning for self-supervised
     Research Society 42.                                                           monocular depth. arXiv preprint arXiv:2002.12319 .
[25] Cross, G.R., Jain, A.K., 1983. Markov random field texture models.        [44] Guo, X., Li, H., Yi, S., Ren, J., Wang, X., 2018. Learning monocular
     IEEE Transactions on Pattern Analysis and Machine Intelligence ,               depth by distilling cross-domain stereo networks, in: Proceedings of
     25–39.                                                                         the European Conference on Computer Vision (ECCV), pp. 484–
[26] CS Kumar, A., Bhandarkar, S.M., Prasad, M., 2018. Monocular                    500.
     depth prediction using generative adversarial networks, in: Proceed-      [45] Gwn Lore, K., Reddy, K., Giering, M., Bernal, E.A., 2018. Gener-
     ings of the IEEE Conference on Computer Vision and Pattern Recog-              ative adversarial networks for depth map estimation from rgb video,
     nition Workshops, pp. 300–308.                                                 in: Proceedings of the IEEE Conference on Computer Vision and
[27] Dos Santos Rosa, N., Guizilini, V., Grassi, V., 2019. Sparse-to-               Pattern Recognition Workshops, pp. 1177–1185.
                                        Deep Learning for Monocular Depth Estimation: A Review

[46] Han, K., Wang, Y., Tian, Q., Guo, J., Xu, C., Xu, C., 2020. Ghost-     [66] Lafferty, J., McCallum, A., Pereira, F.C., 2001. Conditional random
     net: More features from cheap operations, in: Proceedings of the            fields: Probabilistic models for segmenting and labeling sequence
     IEEE/CVF Conference on Computer Vision and Pattern Recogni-                 data , 282–289.
     tion, pp. 1580–1589.                                                   [67] Laga, H., 2019. A survey on deep learning architectures for image-
[47] Hao, S., Zhou, Y., Guo, Y., 2020. A brief survey on semantic seg-           based depth reconstruction. arXiv preprint arXiv:1906.06113 .
     mentation with deep learning. Neurocomputing .                         [68] Lai, Z., Lu, E., Xie, W., 2020. Mast: A memory-augmented self-
[48] He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep residual learning           supervised tracker, in: Proceedings of the IEEE/CVF Conference
     for image recognition, in: Proceedings of the IEEE conference on            on Computer Vision and Pattern Recognition, pp. 6479–6488.
     computer vision and pattern recognition, pp. 770–778.                  [69] Laina, I., Rupprecht, C., Belagiannis, V., Tombari, F., Navab, N.,
[49] He, L., Chen, C., Zhang, T., Zhu, H., Wan, S., 2018. Wearable depth         2016. Deeper depth prediction with fully convolutional residual net-
     camera: Monocular depth estimation via sparse optimization under            works, in: 2016 Fourth international conference on 3D vision (3DV),
     weak supervision. IEEE Access 6, 41337–41345.                               IEEE. pp. 239–248.
[50] Hochreiter, S., Schmidhuber, J., 1997. Long short-term memory.         [70] Lee, J., Kim, C.S., 2019. Monocular depth estimation using relative
     Neural computation 9, 1735–1780.                                            depth maps, in: Proceedings of the IEEE Conference on Computer
[51] Howard, A.G., Zhu, M., Chen, B., Kalenichenko, D., Wang, W.,                Vision and Pattern Recognition, IEEE. pp. 9729–9738.
     Weyand, T., Andreetto, M., Adam, H., 2017. Mobilenets: Efficient       [71] Lee, J.H., Han, M.K., Ko, D.W., Suh, I.H., 2019. From big to small:
     convolutional neural networks for mobile vision applications. arXiv         Multi-scale local planar guidance for monocular depth estimation.
     preprint arXiv:1704.04861 .                                                 arXiv preprint arXiv:1907.10326 .
[52] Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q., 2017.        [72] Lei, G., Xia, Y., Zhai, D.H., Zhang, W., Chen, D., Wang, D., 2020.
     Densely connected convolutional networks, in: Proceedings of the            Staincnns: An efficient stain feature learning method. Neurocom-
     IEEE conference on computer vision and pattern recognition, pp.             puting .
     4700–4708.                                                             [73] Levin, A., Lischinski, D., Weiss, Y., 2004. Colorization using opti-
[53] Huang, W., Cheng, J., Yang, Y., Guo, G., 2019. An improved deep             mization, in: ACM SIGGRAPH 2004 Papers, pp. 689–694.
     convolutional neural network with multi-scale information for bear-    [74] Li, B., Dai, Y., Chen, H., He, M., 2017a. Single image depth es-
     ing fault diagnosis. Neurocomputing 359, 77–92.                             timation by dilated deep residual convolutional neural network and
[54] Ji, S., Xu, W., Yang, M., Yu, K., 2012. 3d convolutional neural             soft-weight-sum inference. arXiv preprint arXiv:1705.00534 .
     networks for human action recognition. IEEE transactions on pattern    [75] Li, B., Shen, C., Dai, Y., Van Den Hengel, A., He, M., 2015. Depth
     analysis and machine intelligence 35, 221–231.                              and surface normal estimation from monocular images using regres-
[55] Jiao, J., Cao, Y., Song, Y., Lau, R., 2018. Look deeper into depth:         sion on deep features and hierarchical crfs, in: Proceedings of the
     Monocular depth estimation with semantic booster and attention-             IEEE conference on computer vision and pattern recognition, pp.
     driven loss, in: Proceedings of the European conference on computer         1119–1127.
     vision (ECCV), pp. 53–69.                                              [76] Li, J., Klein, R., Yao, A., 2017b. A two-streamed network for esti-
[56] Jiao, X., Chen, Y., Dong, R., 2020. An unsupervised image seg-              mating fine-scaled depth maps from single rgb images, in: Proceed-
     mentation method combining graph clustering and high-level feature          ings of the IEEE International Conference on Computer Vision, pp.
     representation. Neurocomputing .                                            3372–3380.
[57] Johnston, A., Carneiro, G., 2020. Self-supervised monocular trained    [77] Li, T., Dong, X., Chen, H., 2019. Single image super-resolution in-
     depth estimation using self-attention and discrete disparity volume,        corporating example-based gradient profile estimation and weighted
     in: Proceedings of the IEEE/CVF Conference on Computer Vision               adaptive p-norm. Neurocomputing 355, 105–120.
     and Pattern Recognition, pp. 4756–4765.                                [78] Li, Z., He, D., Tian, F., Chen, W., Qin, T., Wang, L., Liu, T.Y.,
[58] Jung, H., Kim, Y., Min, D., Oh, C., Sohn, K., 2017. Depth prediction        2018. Towards binary-valued gates for robust lstm training, in: Pro-
     from a single image with conditional adversarial networks, in: 2017         ceedings of the International Conference on Machine Learning, pp.
     IEEE International Conference on Image Processing (ICIP), IEEE.             4662–4671.
     pp. 1717–1721.                                                         [79] Lin, T.Y., Maire, M., Belongie, S., Hays, J., Zitnick, C.L., 2014. Mi-
[59] Kendall, A., Martirosyan, H., Dasgupta, S., Henry, P., Kennedy, R.,         crosoft coco: Common objects in context, in: European Conference
     Bachrach, A., Bry, A., 2017. End-to-end learning of geometry and            on Computer Vision, Springer. pp. 740–755.
     context for deep stereo regression, in: Proceedings of the IEEE In-    [80] Liu, B., Ait-Boudaoud, D., 2020. Effective image super resolution
     ternational Conference on Computer Vision, pp. 66–75.                       via hierarchical convolutional neural network. Neurocomputing 374,
[60] Khamis, S., Fanello, S., Rhemann, C., Kowdle, A., Valentin, J.,             109–116.
     Izadi, S., 2018. Stereonet: Guided hierarchical refinement for real-   [81] Liu, B., Gould, S., Koller, D., 2010. Single image depth estimation
     time edge-aware depth prediction, in: Proceedings of the European           from predicted semantic labels, in: 2010 IEEE Computer Society
     Conference on Computer Vision (ECCV), pp. 573–590.                          Conference on Computer Vision and Pattern Recognition, IEEE. pp.
[61] Kim, G., Park, B., Kim, A., 2019. 1-day learning, 1-year localiza-          1253–1260.
     tion: Long-term lidar localization using scan context image. IEEE      [82] Liu, C., Gu, J., Kim, K., Narasimhan, S., Kautz, J., 2019a. Neu-
     Robotics and Automation Letters 4, 1948–1955.                               ral rgb->d sensing: Depth and uncertainty from a video camera, in:
[62] Kim, Y., Jung, H., Min, D., Sohn, K., 2018. Deep monocular depth            Proceedings of the IEEE Conference on Computer Vision and Pat-
     estimation via integration of global and local predictions. IEEE            tern Recognition, IEEE. pp. 10986–10995.
     transactions on Image Processing 27, 4131–4144.                        [83] Liu, F., Shen, C., Lin, G., 2015. Deep convolutional neural fields for
[63] Krizhevsky, A., Sutskever, I., Hinton, G.E., 2012. Imagenet classi-         depth estimation from a single image, in: Proceedings of the IEEE
     fication with deep convolutional neural networks, in: Advances in           conference on computer vision and pattern recognition, pp. 5162–
     neural information processing systems, pp. 1097–1105.                       5170.
[64] Kumar, A.C., Bhandarkar, S.M., Prasad, M., 2018. Depthnet: A re-       [84] Liu, F., Zhou, S., Wang, Y., Hou, G., Sun, Z., Tan, T., 2019b. Binoc-
     current neural network architecture for monocular depth prediction,         ular light-field: Imaging theory and occlusion-robust depth percep-
     in: 2018 IEEE/CVF Conference on Computer Vision and Pattern                 tion application. IEEE Transactions on Image Processing 29, 1628–
     Recognition Workshops (CVPRW), pp. 283–291.                                 1640.
[65] Kuznietsov, Y., Stuckler, J., Leibe, B., 2017. Semi-supervised deep    [85] Liu, S., Johns, E., Davison, A.J., 2019c. End-to-end multi-task learn-
     learning for monocular depth map prediction, in: Proceedings of the         ing with attention, in: Proceedings of the IEEE Conference on Com-
     IEEE conference on computer vision and pattern recognition, pp.             puter Vision and Pattern Recognition, IEEE. pp. 1871–1880.
     6647–6655.                                                             [86] Liu, X., Xia, Y., Yu, H., Dong, J., Jian, M., Pham, T.D., 2020. Re-
                                           Deep Learning for Monocular Depth Estimation: A Review

      gion based parallel hierarchy convolutional neural network for auto-             Proceedings of the 2004 IEEE Computer Society Conference on
      matic facial nerve paralysis evaluation. IEEE Transactions on Neural             Computer Vision and Pattern Recognition, 2004. CVPR 2004., Ieee.
      Systems and Rehabilitation Engineering 28, 2325–2332.                            pp. 964–971.
 [87] Liu, Y., 2020. Multi-scale spatio-temporal feature extraction and          [106] Park, S.J., Hong, K.S., Lee, S., 2017. Rdfnet: Rgb-d multi-level
      depth estimation from sequences by ordinal classification. Sensors               residual feature fusion for indoor semantic segmentation, in: Pro-
      20, 1979.                                                                        ceedings of the IEEE international conference on computer vision,
 [88] Lowe, D.G., 1999. Object recognition from local scale-invariant fea-             pp. 4980–4989.
      tures, in: Proceedings of the seventh IEEE international conference        [107] Poggi, M., Aleotti, F., Tosi, F., Mattoccia, S., 2020. On the uncer-
      on computer vision, Ieee. pp. 1150–1157.                                         tainty of self-supervised monocular depth estimation, in: Proceed-
 [89] Luo, H., Gao, Y., Wu, Y., Liao, C., Yang, X., Cheng, K.T., 2018.                 ings of the IEEE/CVF Conference on Computer Vision and Pattern
      Real-time dense monocular slam with online adapted depth predic-                 Recognition, pp. 3227–3237.
      tion network. IEEE Transactions on Multimedia 21, 470–483.                 [108] Purohit, K., Mandal, S., Rajagopalan, A., 2020. Mixed-dense con-
 [90] Lyu, H., Fu, H., Hu, X., Liu, L., 2019. Esnet: Edge-based segmenta-              nection networks for image and video super-resolution. Neurocom-
      tion network for real-time semantic segmentation in traffic scenes, in:          puting 398, 360–376.
      2019 IEEE International Conference on Image Processing (ICIP),             [109] Qi, X., Liao, R., Liu, Z., Urtasun, R., Jia, J., 2018. Geonet: Geo-
      IEEE. pp. 1855–1859.                                                             metric neural network for joint depth and surface normal estimation,
 [91] Mahjourian, R., Wicke, M., Angelova, A., 2018. Unsupervised                      in: Proceedings of the IEEE Conference on Computer Vision and
      learning of depth and ego-motion from monocular video using 3d                   Pattern Recognition, pp. 283–291.
      geometric constraints, in: Proceedings of the IEEE Conference on           [110] Qiu, J., Cui, Z., Zhang, Y., Zhang, X., Liu, S., Zeng, B., Pollefeys,
      Computer Vision and Pattern Recognition, pp. 5667–5675.                          M., 2019. Deeplidar: Deep surface normal guided depth prediction
 [92] Mancini, M., Costante, G., Valigi, P., Ciarfuglia, T.A., 2016. Fast              for outdoor scene from sparse lidar data and single color image, in:
      robust monocular depth estimation for obstacle detection with fully              Proceedings of the IEEE Conference on Computer Vision and Pat-
      convolutional networks, in: 2016 IEEE/RSJ International Confer-                  tern Recognition, pp. 3313–3322.
      ence on Intelligent Robots and Systems (IROS), IEEE. pp. 4296–             [111] Radford, A., Metz, L., Chintala, S., 2015. Unsupervised represen-
      4303.                                                                            tation learning with deep convolutional generative adversarial net-
 [93] Mancini, M., Costante, G., Valigi, P., Ciarfuglia, T.A., Delmerico, J.,          works. arXiv preprint arXiv:1511.06434 .
      Scaramuzza, D., 2017. Toward domain independence for learning-             [112] Ramamonjisoa, M., Du, Y., Lepetit, V., 2020. Predicting sharp and
      based monocular depth estimation. IEEE Robotics and Automation                   accurate occlusion boundaries in monocular depth estimation using
      Letters 2, 1778–1785.                                                            displacement fields, in: Proceedings of the IEEE/CVF Conference
 [94] Mayer, N., Ilg, E., Hausser, P., Fischer, P., Cremers, D., Dosovitskiy,          on Computer Vision and Pattern Recognition, pp. 14648–14657.
      A., Brox, T., 2016. A large dataset to train convolutional networks        [113] Ramirez, P.Z., Poggi, M., Tosi, F., Mattoccia, S., Di Stefano, L.,
      for disparity, optical flow, and scene flow estimation, in: Proceedings          2018. Geometry meets semantics for semi-supervised monocu-
      of the IEEE conference on computer vision and pattern recognition,               lar depth estimation, in: Asian Conference on Computer Vision,
      pp. 4040–4048.                                                                   Springer. pp. 298–313.
 [95] McCormac, J., Handa, A., Leutenegger, S., Davison, A.J., 2017.             [114] Ramos, F., Ott, L., 2016. Hilbert maps: scalable continuous occu-
      Scenenet rgb-d: Can 5m synthetic images beat generic imagenet pre-               pancy mapping with stochastic gradient descent. The International
      training on indoor segmentation?, in: Proceedings of the IEEE In-                Journal of Robotics Research 35, 1717–1730.
      ternational Conference on Computer Vision, pp. 2678–2687.                  [115] ur Rehman, S., Tu, S., Waqas, M., Huang, Y., ur Rehman, O., Ah-
 [96] Melis, G., Kočiskỳ, T., Blunsom, P., 2019. Mogrifier lstm. arXiv                mad, B., Ahmad, S., 2019. Unsupervised pre-trained filter learning
      preprint arXiv:1909.01792 .                                                      approach for efficient convolution neural network. Neurocomputing
 [97] Meng, X., Fan, C., Ming, Y., Shen, Y., Yu, H., 2019a. Un-vdnet: un-              365, 171–190.
      supervised network for visual odometry and depth estimation. Jour-         [116] Ren, H., El-Khamy, M., Lee, J., 2019a. Deep robust single im-
      nal of Electronic Imaging 28, 063015.                                            age depth estimation neural network using scene understanding., in:
 [98] Meng, Y., Lu, Y., Raj, A., Sunarjo, S., Guo, R., Javidi, T., Bansal, G.,         CVPR Workshops, pp. 37–45.
      Bharadia, D., 2019b. Signet: Semantic instance aided unsupervised          [117] Ren, J., Hussain, A., Han, J., Jia, X., 2019b. Cognitive modelling
      3d geometry perception, in: Proceedings of the IEEE Conference on                and learning for multimedia mining and understanding. Cognitive
      Computer Vision and Pattern Recognition, pp. 9810–9820.                          Computation 11, 761–762.
 [99] Mirza, M., Osindero, S., 2014. Conditional generative adversarial          [118] Ren, J., Hussain, A., Zheng, J., Liu, C.L., Luo, B., 2020. Special is-
      nets. arXiv preprint arXiv:1411.1784 .                                           sue on recent advances in cognitive learning and data analysis. Cog-
[100] Mousavian, A., Pirsiavash, H., Košecká, J., 2016. Joint semantic seg-            nitive Computation , 1–2.
      mentation and depth estimation with deep convolutional networks,           [119] Ricci, E., Ouyang, W., Wang, X., Sebe, N., et al., 2018. Monocu-
      in: 2016 Fourth International Conference on 3D Vision (3DV),                     lar depth estimation using multi-scale continuous crfs as sequential
      IEEE. pp. 611–619.                                                               deep networks. IEEE transactions on pattern analysis and machine
[101] Mueller, F., Bernard, F., Sotnychenko, O., Verschoor, M., Otaduy,                intelligence 41, 1426–1440.
      M.A., Casas, D., Theobalt, C., 2019. Real-time pose and shape re-          [120] Riegler, G., Ferstl, D., Rüther, M., Bischof, H., 2016. A deep primal-
      construction of two interacting hands with a single depth camera.                dual network for guided depth super-resolution. arXiv preprint
      ACM Transactions on Graphics (TOG) 38, 1–13.                                     arXiv:1607.08569 .
[102] Mur-Artal, R., Montiel, J.M.M., Tardos, J.D., 2015. Orb-slam: a            [121] Ros, G., Sellart, L., Materzynska, J., Vazquez, D., Lopez, A.M.,
      versatile and accurate monocular slam system. IEEE transactions                  2016. The synthia dataset: A large collection of synthetic images
      on robotics 31, 1147–1163.                                                       for semantic segmentation of urban scenes, in: Proceedings of the
[103] Nath Kundu, J., Krishna Uppala, P., Pahuja, A., Venkatesh Babu,                  IEEE conference on computer vision and pattern recognition, pp.
      R., 2018. Adadepth: Unsupervised content congruent adaptation                    3234–3243.
      for depth estimation, in: Proceedings of the IEEE Conference on            [122] Rumelhart, D.E., Hinton, G.E., Williams, R.J., 1986. Learning rep-
      Computer Vision and Pattern Recognition, pp. 2656–2665.                          resentations by back-propagating errors. nature 323, 533–536.
[104] Ni, M., Lei, J., Cong, R., Zheng, K., Peng, B., Fan, X., 2017. Color-      [123] Saxena, A., Chung, S.H., Ng, A.Y., 2006. Learning depth from sin-
      guided depth map super resolution using convolutional neural net-                gle monocular images, in: Advances in neural information process-
      work. IEEE Access 5, 26666–26672.                                                ing systems, pp. 1161–1168.
[105] Nistér, D., Naroditsky, O., Bergen, J., 2004. Visual odometry, in:         [124] Saxena, A., Schulte, J., Ng, A.Y., et al., 2007. Depth estimation
                                          Deep Learning for Monocular Depth Estimation: A Review

      using monocular and stereo cues., in: IJCAI, pp. 2197–2203.                    Schoenberg, M., Verma, V., Csaszar, A., Turner, E., Dryanovski, I.,
[125] Scaramuzza, D., Fraundorfer, F., 2011. Visual odometry [tutorial].             et al., 2018. Depth from motion for smartphone ar. ACM Transac-
      IEEE robotics & automation magazine 18, 80–92.                                 tions on Graphics (TOG) 37, 1–19.
[126] Schuster, M., Paliwal, K.K., 1997. Bidirectional recurrent neural        [146] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L.,
      networks. IEEE transactions on Signal Processing 45, 2673–2681.                Gomez, A.N., Kaiser, Ł., Polosukhin, I., 2017. Attention is all you
[127] Shen, Y., Tan, S., Sordoni, A., Courville, A., 2018. Ordered neurons:          need, in: Advances in neural information processing systems, pp.
      Integrating tree structures into recurrent neural networks. arXiv              5998–6008.
      preprint arXiv:1810.09536 .                                              [147] Vijayanarasimhan, S., Ricco, S., Schmid, C., Sukthankar, R., Fragki-
[128] Shrivastava, A., Pfister, T., Tuzel, O., Susskind, J., Wang, W., Webb,         adaki, K., 2017. Sfm-net: Learning of structure and motion from
      R., 2017. Learning from simulated and unsupervised images through              video. arXiv preprint arXiv:1704.07804 .
      adversarial training, in: Proceedings of the IEEE conference on com-     [148] Wang, K., Peng, X., Yang, J., Lu, S., Qiao, Y., 2020a. Suppressing
      puter vision and pattern recognition, pp. 2107–2116.                           uncertainties for large-scale facial expression recognition, in: Pro-
[129] Shu, C., Yu, K., Duan, Z., Yang, K., 2020. Feature-metric loss for             ceedings of the IEEE/CVF Conference on Computer Vision and Pat-
      self-supervised learning of depth and egomotion , 1–16.                        tern Recognition, pp. 6897–6906.
[130] Silberman, N., Hoiem, D., Kohli, P., Fergus, R., 2012. Indoor seg-       [149] Wang, L., Li, W., Li, W., Van Gool, L., 2018a. Appearance-and-
      mentation and support inference from rgbd images, in: European                 relation networks for video classification, in: Proceedings of the
      conference on computer vision, Springer. pp. 746–760.                          IEEE conference on computer vision and pattern recognition, pp.
[131] Simonyan, K., Zisserman, A., 2014.               Very deep convolu-            1430–1439.
      tional networks for large-scale image recognition. arXiv preprint        [150] Wang, L., Zhang, J., Wang, O., Lin, Z., Lu, H., 2020b. Sdc-depth:
      arXiv:1409.1556 .                                                              Semantic divide-and-conquer network for monocular depth estima-
[132] Spencer, J., Bowden, R., Hadfield, S., 2019. Scale-adaptive neural             tion, in: Proceedings of the IEEE/CVF Conference on Computer
      dense features: Learning via hierarchical context aggregation, in:             Vision and Pattern Recognition, pp. 541–550.
      Proceedings of the IEEE Conference on Computer Vision and Pat-           [151] Wang, P., Shen, X., Lin, Z., Cohen, S., Price, B., Yuille, A., 2015.
      tern Recognition, pp. 6200–6209.                                               Towards unified depth and semantic prediction from a single image,
[133] Spencer, J., Bowden, R., Hadfield, S., 2020. Defeat-net: Gen-                  in: Proceedings of the IEEE Conference on Computer Vision and
      eral monocular depth via simultaneous unsupervised representation              Pattern Recognition, IEEE. pp. 2800–2809.
      learning, in: Proceedings of the IEEE/CVF Conference on Computer         [152] Wang, P., Shen, X., Russell, B., Cohen, S., Price, B., Yuille, A.L.,
      Vision and Pattern Recognition, pp. 14402–14413.                               2016. Surge: Surface regularized geometry estimation from a single
[134] Su, W., Zhang, H., Li, J., Yang, W., Wang, Z., 2019. Monocular                 image, in: Advances in Neural Information Processing Systems, pp.
      depth estimation as regression of classification using piled residual          172–180.
      networks, in: Proceedings of the 27th ACM International Confer-          [153] Wang, R., Pizer, S.M., Frahm, J.M., 2019. Recurrent neural network
      ence on Multimedia, pp. 2161–2169.                                             for (un-) supervised learning of monocular video visual odometry
[135] Sun, J., Wang, Z., Yu, H., Zhang, S., Dong, J., Gao, P., 2020. Two-            and depth, in: Proceedings of the IEEE Conference on Computer
      stage deep regression enhanced depth estimation from a single rgb              Vision and Pattern Recognition, pp. 5555–5564.
      image. IEEE Transactions on Emerging Topics in Computing .               [154] Wang, S., Clark, R., Wen, H., Trigoni, N., 2017. Deepvo: Towards
[136] Sun, J., Zheng, N.N., Shum, H.Y., 2003. Stereo matching using be-              end-to-end visual odometry with deep recurrent convolutional neu-
      lief propagation. IEEE Transactions on pattern analysis and machine            ral networks, in: 2017 International Conference on Robotics and Au-
      intelligence 25, 787–800.                                                      tomation (ICRA), IEEE. pp. 2043–2050.
[137] Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D.,     [155] Wang, X., Girshick, R., Gupta, A., He, K., 2018b. Non-local neu-
      Erhan, D., Vanhoucke, V., Rabinovich, A., 2015. Going deeper with              ral networks, in: Proceedings of the IEEE Conference on Computer
      convolutions, in: Proceedings of the IEEE conference on computer               Vision and Pattern Recognition, IEEE. pp. 7794–7803.
      vision and pattern recognition, pp. 1–9.                                 [156] Wang, Z., Bovik, A.C., Sheikh, H.R., Simoncelli, E.P., 2004. Im-
[138] Tang, C., Hou, C., Song, Z., 2015. Depth recovery and refinement               age quality assessment: from error visibility to structural similarity.
      from a single image using defocus cues. Journal of Modern Optics               IEEE transactions on image processing 13, 600–612.
      62, 441–448.                                                             [157] Watson, J., Firman, M., Brostow, G., Turmukhambetov, D., 2019.
[139] Tian, G., Liu, L., Ri, J., Liu, Y., Sun, Y., 2019. Objectfusion: An            Self-supervised monocular depth hints , 2162–2171.
      object detection and segmentation framework with rgb-d slam and          [158] Wong, A., Soatto, S., 2019. Bilateral cyclic constraint and adaptive
      convolutional neural networks. Neurocomputing 345, 3–14.                       regularization for unsupervised monocular depth prediction, in: Pro-
[140] Tonioni, A., Poggi, M., Mattoccia, S., Di Stefano, L., 2019a. Unsu-            ceedings of the IEEE Conference on Computer Vision and Pattern
      pervised domain adaptation for depth prediction from images. IEEE              Recognition, pp. 5644–5653.
      transactions on pattern analysis and machine intelligence .              [159] Xia, Y., Yu, H., Wang, F.Y., 2019. Accurate and robust eye center
[141] Tonioni, A., Tosi, F., Poggi, M., Mattoccia, S., Stefano, L.D., 2019b.         localization via fully convolutional networks. IEEE/CAA Journal of
      Real-time self-adaptive deep stereo, in: Proceedings of the IEEE               Automatica Sinica 6, 1127–1138.
      Conference on Computer Vision and Pattern Recognition, pp. 195–          [160] Xiao, Y., Cao, X., Zhu, X., Yang, R., Zheng, Y., 2018. Joint convolu-
      204.                                                                           tional neural pyramid for depth map super-resolution. arXiv preprint
[142] Tsai, Y.M., Chang, Y.L., Chen, L.G., 2006. Block-based vanishing               arXiv:1801.00968 .
      line and vanishing point detection for 3d scene reconstruction, in:      [161] Xie, J., Girshick, R., Farhadi, A., 2016. Deep3d: Fully automatic 2d-
      2006 international symposium on intelligent signal processing and              to-3d video conversion with deep convolutional neural networks, in:
      communications, IEEE. pp. 586–589.                                             European Conference on Computer Vision, Springer. pp. 842–857.
[143] Tulyakov, S., Ivanov, A., Fleuret, F., 2018. Practical deep stereo       [162] Xingjian, S., Chen, Z., Wang, H., Yeung, D.Y., Wong, W.K., Woo,
      (pds): Toward applications-friendly deep stereo matching, in: Ad-              W.c., 2015. Convolutional lstm network: A machine learning ap-
      vances in Neural Information Processing Systems, pp. 5871–5881.                proach for precipitation nowcasting, in: Advances in neural infor-
[144] Ummenhofer, B., Zhou, H., Uhrig, J., Mayer, N., Ilg, E., Dosovit-              mation processing systems, pp. 802–810.
      skiy, A., Brox, T., 2017. Demon: Depth and motion network for            [163] Xu, D., Wang, W., Tang, H., Liu, H., Sebe, N., Ricci, E., 2018.
      learning monocular stereo, in: Proceedings of the IEEE/CVF Con-                Structured attention guided convolutional neural fields for monoc-
      ference on Computer Vision and Pattern Recognition, pp. 5038–                  ular depth estimation, in: Proceedings of the IEEE Conference on
      5047.                                                                          Computer Vision and Pattern Recognition, pp. 3917–3925.
[145] Valentin, J., Kowdle, A., Barron, J.T., Wadhwa, N., Dzitsiuk, M.,        [164] Yang, D., Zhong, X., Gu, D., Peng, X., Hu, H., 2020. Unsupervised
                                          Deep Learning for Monocular Depth Estimation: A Review

      framework for depth estimation and camera motion prediction from         [184] Zhang, Y., Funkhouser, T., 2018. Deep depth completion of a single
      video. Neurocomputing 385, 169–185.                                            rgb-d image, in: Proceedings of the IEEE Conference on Computer
[165] Yang, X., Gao, Y., Luo, H., Liao, C., Cheng, K.T., 2019a. Bayesian             Vision and Pattern Recognition, pp. 175–185.
      denet: monocular depth prediction and frame-wise fusion with syn-        [185] Zhang, Z., 2000. A flexible new technique for camera calibration.
      chronized uncertainty. IEEE Transactions on Multimedia 21, 2701–               IEEE Transactions on pattern analysis and machine intelligence 22,
      2713.                                                                          1330–1334.
[166] Yang, X., Luo, H., Wu, Y., Gao, Y., Liao, C., Cheng, K.T., 2019b.        [186] Zhang, Z., Cui, Z., Xu, C., Jie, Z., Li, X., Yang, J., 2018b. Joint task-
      Reactive obstacle avoidance of monocular quadrotors with online                recursive learning for semantic segmentation and depth estimation,
      adapted depth prediction network. Neurocomputing 325, 142–158.                 in: European Conference on Computer Vision, Springer. pp. 235–
[167] Yang, Z., Wang, P., Xu, W., Zhao, L., Nevatia, R., 2017. Unsuper-              251.
      vised learning of geometry with edge-aware depth-normal consis-          [187] Zhang, Z., Cui, Z., Xu, C., Yan, Y., Sebe, N., Yang, J., 2019c.
      tency. arXiv preprint arXiv:1711.03665 .                                       Pattern-affinitive propagation across depth, surface normal and se-
[168] Ye, X., Ji, X., Sun, B., Chen, S., Wang, Z., Li, H., 2020. Drm-slam:           mantic segmentation, in: Proceedings of the IEEE Conference on
      Towards dense reconstruction of monocular slam with scene depth                Computer Vision and Pattern Recognition, pp. 4106–4115.
      fusion. Neurocomputing .                                                 [188] Zhang, Z., Xu, C., Yang, J., Gao, J., Cui, Z., 2018c. Progressive
[169] Yin, Z., Shi, J., 2018. Geonet: Unsupervised learning of dense                 hard-mining network for monocular depth estimation. IEEE Trans-
      depth, optical flow and camera pose, in: Proceedings of the IEEE               actions on Image Processing 27, 3691–3702.
      Conference on Computer Vision and Pattern Recognition, pp. 1983–         [189] Zhao, S., Fu, H., Gong, M., Tao, D., 2019. Geometry-aware sym-
      1992.                                                                          metric domain adaptation for monocular depth estimation, in: Pro-
[170] Žbontar, J., LeCun, Y., 2016. Stereo matching by training a convo-             ceedings of the IEEE Conference on Computer Vision and Pattern
      lutional neural network to compare image patches. The journal of               Recognition, pp. 9788–9798.
      machine learning research 17, 2287–2318.                                 [190] Zhao, W., Zhang, S., Guan, Z., Luo, H., Tang, L., Peng, J., Fan, J.,
[171] Zeng, N., Li, H., Wang, Z., Liu, W., Liu, S., Alsaadi, F.E., Liu, X.,          2020a. 6d object pose estimation via viewpoint relation reasoning.
      2020. Deep-reinforcement-learning-based images segmentation for                Neurocomputing .
      quantitative analysis of gold immunochromatographic strip. Neuro-        [191] Zhao, Y., Kong, S., Shin, D., Fowlkes, C., 2020b. Domain declutter-
      computing .                                                                    ing: Simplifying images to mitigate synthetic-real domain shift and
[172] Zeng, N., Zhang, H., Song, B., Liu, W., Li, Y., Dobaie, A.M., 2018.            improve depth estimation, in: Proceedings of the IEEE/CVF Confer-
      Facial expression recognition via learning deep sparse autoencoders.           ence on Computer Vision and Pattern Recognition, pp. 3330–3340.
      Neurocomputing 273, 643–649.                                             [192] Zheng, C., Cham, T.J., Cai, J., 2018. T2net: Synthetic-to-realistic
[173] Zhai, M., Xiang, X., Zhang, R., Lv, N., El Saddik, A., 2019. Opti-             translation for solving single-image depth estimation tasks, in: Pro-
      cal flow estimation using channel attention mechanism and dilated              ceedings of the European Conference on Computer Vision (ECCV),
      convolutional neural networks. Neurocomputing 368, 124–132.                    pp. 767–783.
[174] Zhan, H., Garg, R., Saroj Weerasekera, C., Li, K., Agarwal, H., Reid,    [193] Zhou, L., Ye, J., Abello, M., Wang, S., Kaess, M., 2018. Un-
      I., 2018. Unsupervised learning of monocular depth estimation and              supervised learning of monocular depth estimation with bun-
      visual odometry with deep feature reconstruction, in: Proceedings of           dle adjustment, super-resolution and clip loss. arXiv preprint
      the IEEE Conference on Computer Vision and Pattern Recognition,                arXiv:1812.03368 .
      pp. 340–349.                                                             [194] Zhou, T., Brown, M., Snavely, N., Lowe, D.G., 2017. Unsupervised
[175] Zhang, F., Prisacariu, V., Yang, R., Torr, P.H., 2019a. Ga-net:                learning of depth and ego-motion from video, in: Proceedings of the
      Guided aggregation net for end-to-end stereo matching, in: Proceed-            IEEE Conference on Computer Vision and Pattern Recognition, pp.
      ings of the IEEE Conference on Computer Vision and Pattern Recog-              1851–1858.
      nition, pp. 185–194.                                                     [195] Zhu, A.Z., Yuan, L., Chaney, K., Daniilidis, K., 2019. Unsupervised
[176] Zhang, H., Shen, C., Li, Y., Cao, Y., Liu, Y., Yan, Y., 2019b. Ex-             event-based learning of optical flow, depth, and egomotion, in: Pro-
      ploiting temporal consistency for real-time video depth estimation,            ceedings of the IEEE Conference on Computer Vision and Pattern
      in: Proceedings of the IEEE International Conference on Computer               Recognition, pp. 989–997.
      Vision, pp. 1725–1734.                                                   [196] Zhu, J.Y., Park, T., Isola, P., Efros, A.A., 2017. Unpaired image-
[177] Zhang, H., Xu, T., Li, H., Zhang, S., Wang, X., Huang, X., Metaxas,            to-image translation using cycle-consistent adversarial networks, in:
      D.N., 2017. Stackgan: Text to photo-realistic image synthesis                  Proceedings of the IEEE international conference on computer vi-
      with stacked generative adversarial networks, in: Proceedings of the           sion, pp. 2223–2232.
      IEEE international conference on computer vision, pp. 5907–5915.         [197] Zoran, D., Isola, P., Krishnan, D., Freeman, W.T., 2015. Learn-
[178] Zhang, J., Su, Q., Wang, C., Gu, H., 2020a. Monocular 3d vehi-                 ing ordinal relationships for mid-level vision, in: Proceedings of the
      cle detection with multi-instance depth and geometry reasoning for             IEEE International Conference on Computer Vision, pp. 388–396.
      autonomous driving. Neurocomputing .
[179] Zhang, M., Ye, X., Fan, X., Zhong, W., 2020b. Unsupervised depth
      estimation from monocular videos with hybrid geometric-refined
      loss and contextual attention. Neurocomputing 379, 250–261.
[180] Zhang, P., Liu, J., Wang, X., Pu, T., Fei, C., Guo, Z., 2020c. Stereo-
      scopic video saliency detection based on spatiotemporal correlation
      and depth confidence optimization. Neurocomputing 377, 256–268.
[181] Zhang, R., Tsai, P.S., Cryer, J.E., Shah, M., 1999. Shape-from-
      shading: a survey. IEEE transactions on pattern analysis and ma-
      chine intelligence 21, 690–706.
[182] Zhang, T., Yang, Y., Zeng, Y., Zhao, Y., 2020d. Cognitive template-
      clustering improved linemod for efficient multi-object pose estima-
      tion. Cognitive Computation , 1–10.
[183] Zhang, X., Zhou, X., Lin, M., Sun, J., 2018a. Shufflenet: An ex-
      tremely efficient convolutional neural network for mobile devices,
      in: Proceedings of the IEEE conference on computer vision and pat-
      tern recognition, pp. 6848–6856.
