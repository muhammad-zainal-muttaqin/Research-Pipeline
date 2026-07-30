---
source_id: 066
bibtex_key: bhat2021adabins
title: AdaBins: Depth Estimation Using Adaptive Bins
year: 2021
domain_theme: Estimasi Kedalaman
verified_pdf: 66_AdaBins.pdf
char_count: 68678
---

AdaBins: Depth Estimation using Adaptive Bins

                                                     Shariq Farooq Bhat                            Ibraheem Alhashim                            Peter Wonka
                                                          KAUST                                         KAUST                                     KAUST
                                                shariq.bhat@kaust.edu.sa                  ibraheem.alhashim@kaust.edu.sa                     pwonka@gmail.com
arXiv:2011.14141v1 [cs.CV] 28 Nov 2020

                                                                  Abstract

                                             We address the problem of estimating a high quality
                                         dense depth map from a single RGB input image. We start
                                         out with a baseline encoder-decoder convolutional neu-
                                         ral network architecture and pose the question of how the
                                         global processing of information can help improve overall
                                         depth estimation. To this end, we propose a transformer-
                                         based architecture block that divides the depth range into
                                         bins whose center value is estimated adaptively per image.
                                         The final depth values are estimated as linear combinations
                                         of the bin centers. We call our new building block AdaBins.
                                         Our results show a decisive improvement over the state-of-
                                         the-art on several popular depth datasets across all metrics.
                                         We also validate the effectiveness of the proposed block with
                                         an ablation study and provide the code and corresponding              Figure 1: Illustration of AdaBins: Top: input RGB im-
                                         pre-trained weights of the new state-of-the-art model 1 .             ages. Middle: depth predicted by our model. Bottom:
                                                                                                               histogram of depth values of the ground truth (blue) and
                                                                                                               histogram of the predicted adaptive depth-bin-centers (red)
                                         1. Introduction                                                       with depth values increasing from left to right. Note that
                                                                                                               the predicted bin-centers are focused near smaller depth val-
                                             This paper tackles the problem of estimating a high qual-         ues for closeup images but are widely distributed for images
                                         ity dense depth map from a single RGB input image. This               with a wider range of depth values.
                                         is a classical problem in computer vision that is essential
                                         for many applications [27, 31, 17, 7]. In this work, we pro-
                                         pose a new architecture building block, called AdaBins that
                                                                                                               idea, we propose to analyze and modify the distribution of
                                         leads to a new state-of-the-art architecture for depth estima-
                                                                                                               the depth values.
                                         tion on the two most popular indoor and outdoor datasets,
                                         NYU [37] and KITTI [14].                                                 Depth distribution corresponding to different RGB in-
                                             The motivation for our work is the conjecture that current        puts can vary to a large extent (see Fig. 1). Some images
                                         architectures do not perform enough global analysis of the            have most of the objects located over a very small range of
                                         output values. A drawback of convolutional layers is that             depth values. Closeup images of furniture will, for example,
                                         they only process global information once the tensors reach           contain pixels most of which are close to the camera while
                                         a very low spatial resolution at or near the bottleneck. How-         other images may have depth values distributed over a much
                                         ever, we believe that global processing is a lot more power-          broader range, e.g. a corridor, where depth values range
                                         ful when done at high resolution. Our general idea is to              from a small value to the maximum depth supported by the
                                         perform a global statistical analysis of the output of a tradi-       network. Along with the ill-posed nature of the problem,
                                         tional encoder-decoder architecture and to refine the output          such a variation in depth distribution makes depth regres-
                                         with a learned post-processing building block that operates           sion in an end-to-end manner an even more difficult task.
                                         at the highest resolution. As a particular realization of this        Recent works have proposed to exploit assumptions about
                                                                                                               indoor environments such as planarity constraints [26, 22]
                                           1 https://github.com/shariqfarooq123/AdaBins                        to guide the network, which may or may not hold for a real-

                                                                                                           1
                       Standard Encoder-Decoder                                           AdaBins Module
                                                                                                        Hybrid Regression

Input RGB                                                                                 R                  Softmax                Depth image
                  Encoder                   Decoder                    mViT                      Conv                        Eq.3
 H×W × 3                                                                                                     N classes                h ×w ×1

                                                                          Bin widths: b                       Bin centers: c(b)
                                                                                                 Eq.2

Figure 2: Overview of our proposed network architecture. Our architecture consists of two major components: an encoder-
decoder block and our proposed adaptive bin-width estimator block called AdaBins. The input to our network is an RGB
image of spatial dimensions H and W , and the output is a single channel h × w depth image (e.g., half the spatial resolution).

world environment, especially for outdoors scenes.
    Instead of imposing such assumptions, we investigate an
approach where the network learns to adaptively focus on
regions of the depth range which are more probable to occur
in the scene of the input image.
    Our main contributions are the following:

   • We propose an architecture building block that per-
     forms global processing of the scene’s information.
     We propose to divide the predicted depth range into                Figure 3: Choices for bin widths. Uniform and Log-
     bins where the bin widths change per image. The fi-                uniform bins are pre-determined. ‘Trained bins’ vary from
     nal depth estimation is a linear combination of the bin            one dataset to another. Adaptive bins vary for each input
     center values.                                                     image.

   • We show a decisive improvement for supervised single
     image depth estimation across all metrics for the two              the bottleneck. Our results section compares to these (and
     most popular datasets, NYU [37] and KITTI [14].                    many other) methods.
                                                                            Encoder-decoder networks have made significant con-
   • We analyze our findings and investigate different mod-             tributions in many vision related problems such as image
     ifications on the proposed AdaBins block and study                 segmentation [35], optical flow estimation [10], and im-
     their effect on the accuracy of the depth estimation.              age restoration [28]. In recent years, the use of such ar-
                                                                        chitectures have shown great success both in the supervised
2. Related Work                                                         and the unsupervised setting of the depth estimation prob-
                                                                        lem [15, 41, 21, 48, 1]. Such methods typically use one or
    The problem of 3D scene reconstruction from RGB im-                 more encoder-decoder networks as a sub part of their larger
ages is an ill-posed problem. Issues such as lack of scene              network. In this paper we adapted the baseline encoder-
coverage, scale ambiguities, translucent or reflective ma-              decoder network architecture used by [1]. This allows us
terials all contribute to ambiguous cases where geometry                to more explicitly study the performance attribution of our
cannot be derived from appearance. Recently, methods that               proposed extension on the pipeline which is typically a dif-
rely on convolutional neural networks (CNNs) are able to                ficult task.
produce reasonable depth maps from a single RGB input                       Transformer networks are gaining greater attention as a
image at real-time speeds.                                              viable building block outside of their traditional use in NLP
    Monocular depth estimation has been considered by                   tasks and into computer vision tasks [32, 43, 2, 6]. Follow-
many CNN methods as a regression of a dense depth map                   ing the success of recent trends that combine CNNs with
from a single RGB image [8, 25, 45, 16, 46, 11, 19, 1, 26,              Transformers [2], we propose to leverage a Transformer en-
22].                                                                    coder as a building block for non-local processing on the
    As the two most important competitors, we consider                  output of a CNN.
BTS [26] and DAV [22]. BTS uses local planar guidance
layers to guide the features to full resolution instead of stan-        3. Methodology
dard upsampling layers during the decoding phase. DAV
uses a standard encoder-decoder scheme and proposes to                     In this section, we present the motivation for this work,
exploit co-planarity of objects in the scene via attention at           provide details of the AdaBins architecture, and describe

                                                                   2
the corresponding loss functions used.                                                 Conv
                                                                                                           Pixel-wise dot product            R
                                                                                       3×3

3.1. Motivation
                                                                     Features Map                                                            Bin widths: b
                                                                           Cd
   Our idea could be seen as a generalization of depth es-
timation via an ordinal regression network as proposed by                                     MLP Head          1×1 kernels         Misc.

Fu et al. [11]. Fu et al. observed that a performance im-                                                               ...            ...

provement could be achieved if the depth regression task is                                          Transformer Encoder
transformed into a classification task. They proposed to di-
vide the depth range into a fixed number of bins of predeter-                          Conv
                                                                                       p×p
                                                                      Embedding Conv
mined width. Our generalization solves multiple limitations                                              Patch embeddings

of the initial approach. First, we propose to compute adap-
                                                                     Figure 4: An overview of the mini-ViT block. The input to
tive bins that dynamically change depending on the features
                                                                     the block is a multi-channel feature map of the input image.
of the input scene. Second, a classification approach leads
                                                                     The block includes a Transformer encoder that is applied on
to a discretization of depth values which results in poor vi-
                                                                     patch embeddings of the input for the purpose of learning
sual quality with obvious sharp depth discontinuities. This
                                                                     to estimate bin widths b and a set of convolutional kernels
might still lead to good results with regard to the standard
                                                                     needed to compute our Range-Attention-Maps R.
evaluation metrics, but it can present a challenge for down-
stream applications, e.g. computational photography or 3D
reconstruction. Therefore, we propose to predict the final              Second, discretizing the depth interval D into bins and
depth values as a linear combination of bin centers. This            assigning each pixel to a single bin leads to depth discretiza-
allows us to combine the advantages of classification with           tion artifacts. We therefore predict the final depth as a linear
the advantages of depth-map regression. Finally, compared            combination of bin centers enabling the model to estimate
to other architectures, e.g. DAV [22], we compute informa-           smoothly varying depth values.
tion globally at a high resolution and not primarily in the             Third, several previous architectures propose perform-
bottleneck part at a low resolution.                                 ing global processing using attention blocks to process in-
3.2. AdaBins design                                                  formation after an encoder block in the architecture (e.g.,
                                                                     image captioning [5, 18] or object detection [2]). Also, the
   Here, we discuss four design choices of our proposed              current state-of-the-art in depth estimation uses this strat-
architecture that are most important for the obtained results.       egy [22]. Such an architecture consists of three blocks or-
   First, we employ an adaptive binning strategy to dis-             dered as such: encoder, attention, followed by a decoder.
cretize the depth interval D = (dmin , dmax ) into N bins.           We initially followed this approach but noticed that better
This interval is fixed for a given dataset and is determined         results can be achieved when using attention at the spatially
by dataset specification or manually set to a reasonable             higher resolution tensors. We therefore propose an architec-
range. To illustrate our idea of dividing a depth interval           ture that also has these three blocks, but ordered as follows:
into bins, we would like to contrast our final solution with         encoder, decoder, and finally attention.
three other possible design choices we evaluated:                       Fourth, we would like to build on the simplest possible
   • Fixed bins with a uniform bin width: the depth interval         architecture to isolate the effects of our newly proposed Ad-
     D is divided into N bins of equal size.                         aBins concept. We therefore build on a modern encoder-
                                                                     decoder [1] using EfficientNet B5 [40] as the backbone for
   • Fixed bins with a log scale bin width: the depth inter-         the encoder.
     val D is divided into bins of equal size in log scale.             In the next subsection, we provide a description of the
   • Trained bin widths: the bin widths are adaptive and             entire architecture.
     can be learned for a particular dataset. While the bin
                                                                     3.3. Architecture description
     widths are general, all images finally share the same
     bin subdivision of the depth interval D.                            Fig. 2 shows an overview of our proposed depth esti-
                                                                     mating architecture. Our architecture consists of two major
   • AdaBins: the bin widths b are adaptively computed for
                                                                     components: 1) an encoder-decoder block built on a pre-
     each image.
                                                                     trained EfficientNet B5 [40] encoder and a standard fea-
We recommend the strategy of AdaBins as the best option              ture upsampling decoder; 2) our proposed adaptive bin-
and our ablation study validates this choice by showing the          width estimator block called AdaBins. The first compo-
superiority of this design over its alternatives. An illustra-       nent is primarily based on the simple depth regression net-
tion of the four design choices for bin widths can be seen in        work of Alhashim and Wonka [1] with some modifications.
Fig. 3.                                                              The two basic modifications are switching the encoder from

                                                                 3
Patch                       num             MLP                    E. Thus, the result of this convolution is a tensor of size
           E      Layers             C               Params        h/p × w/p × E (assuming both h and w are divisible by
size (p)                    heads           Size
                                                                   p). The result is reshaped into a spatially flattened tensor
16         128    4         4        128    1024     5.8 M         xp ∈ RS×E , where S = hw       p2 serves as the effective se-
                                                                   quence length for the transformer. We refer to this sequence
           Table 1: Mini-ViT architecture details.                 of E-dimensional vectors as patch embeddings.
                                                                       Following common practice [2, 6], we add learned po-
                                                                   sitional encodings to the patch embeddings before feeding
DenseNet [20] to EfficientNet B5 and using a different ap-
                                                                   them to the transformer. Our transformer is a small trans-
propriate loss function for the new architecture. In addi-
                                                                   former encoder (see Table. 1 for details) and outputs a se-
tion, the output of the decoder is a tensor xd ∈ Rh×w×Cd ,
                                                                   quence of output embeddings xo ∈ RS×E . We use an
not a single channel image representing the final depth val-
                                                                   MLP head over the first output embedding (we also exper-
ues. We refer to this tensor as the “decoded features”. The
                                                                   imented with a version that has an additional special token
second component is a key contribution in this paper, the
                                                                   as first input, but did not see an improvement). The MLP
AdaBins module. The input to the AdaBins module are de-
                                                                   head uses a ReLU activation and outputs an N-dimensional
coded features of size h×w ×Cd and the output tensor is of
                                                                   vector b0 . Finally, we normalize the vector b0 such that it
size h × w × 1. Due to memory limitations of current GPU
                                                                   sums up to 1, to obtain the bin-widths vector b as follows:
hardware, we use h = H/2 and w = W/2 to facilitate bet-
ter learning with larger batch sizes. The final depth map is                                  b0 + 
computed by simply bilinearly upsampling to H × W × 1.                                 bi = PN i          ,                   (1)
                                                                                                   0
    The first block in the AdaBins module is called mini-                                    j=1 (bj + )

ViT. An overview of this block is shown in Fig. 4. It is a
                                                                   where  = 10−3 . The small positive  ensures each bin-
simplified version of a recently proposed technique of using
                                                                   width is strictly positive. The normalization introduces a
transformers for image recognition [6] with minor modifi-
                                                                   competition among the bin-widths and conceptually forces
cations. The details of mini-ViT are explained in the next
                                                                   the network to focus on sub-intervals within D by predicting
paragraph. There are two outputs of mini-ViT: 1) a vector
                                                                   smaller bin-widths at interesting regions of D.
b of bin-widths, which defines how the depth interval D is
                                                                      In the next subsection, we describe how the Range-
to be divided for the input image, and 2) Range-Attention-
                                                                   Attention-Maps R are obtained from the decoded features
Maps R of size h × w × C, that contain useful information
                                                                   and the transformer output embeddings.
for pixel-level depth computation.

                                                                   Range attention maps. At this point, the decoded fea-
Mini-ViT. Estimating sub-intervals within the depth                tures represent a high-resolution and local pixel-level infor-
range D which are more probable to occur for a given image         mation while the transformer output embeddings effectively
would require a combination of local structural information        contain more global information. As shown in Fig. 4, out-
and global distributional information at the same time. We         put embeddings 2 through C + 1 from the transformer are
propose to use global attention in order to calculate a bin-       used as a set of 1 × 1 convolutional kernels and are con-
widths vector b for each input image. Global attention is          volved with the decoded features (following a 3 × 3 con-
expensive both in terms of memory and computational com-           volutional layer) to obtain the Range-Attention Maps R.
plexity, especially at higher resolutions. However, recent         This is equivalent to calculating the Dot-Product attention
rapid advances in transformers provide some efficient alter-       weights between pixel-wise features treated as ‘keys’ and
natives. We take inspiration from the Vision Transformer           transformer output embeddings as ‘queries’. This simple
ViT [6] in designing our AdaBins module with transform-            design of using output embeddings as convolutional kernels
ers. We also use a much smaller version of the transformer         lets the network integrate adaptive global information from
proposed as our dataset is smaller and refer to this trans-        the transformer into the local information of the decoded
former as mini-ViT or mViT in the following description.           features. R and b are used together to obtain the final depth
                                                                   map.
Bin-widths. We first describe how the bin-widths vector
b is obtained using mViT. The input to the mViT block is           Hybrid regression. Range-Attention Maps R are passed
a tensor of decoded features xd ∈ Rh×w×Cd . However,               through a 1 × 1 convolutional layer to obtain N -channels
a transformer takes a sequence of fixed size vectors as in-        which is followed by a Softmax activation. We inter-
put. We first pass the decoded features through a convolu-         pret the N Softmax scores pk , k = 1, ..., N , at each
tional block, named as Embedding Conv (see Fig 4), with            pixel as probabilities over N depth-bin-centers c(b) :=
kernel size p × p, stride p and number of output channels          {c(b1 ), c(b2 ), ..., c(bN )} calculated from bin-widths vector

                                                               4
                                                                         Finally, we define the total loss as:

                                                                                          Ltotal = Lpixel + βLbins                (6)

                                                                            We set β = 0.1 for all our experiments. We experi-
                                                                         mented with different loss functions including the RMSE
                                                                         loss, and the combined SSIM [42] plus L1 loss suggested
                                                                         by [1]. However, we were able to achieve the best results
                                                                         with our proposed loss. We offer a comparison of the dif-
                                                                         ferent loss functions and their performance in our ablation
         RGB             Fu et al. [11]          Ours                    study.
Figure 5: Demonstration of artifacts introduced by the dis-              4. Experiments
cretization of the depth interval. Our hybrid regression re-
sults in smoother depth maps.                                               We conducted an extensive set of experiments on the
                                                                         standard depth estimation from a single image datasets for
                                                                         both indoor and outdoor scenes. In the following, we first
b as follows:                                                            briefly describe the datasets and the evaluation metrics, and
                                                  i−1
                                                  X                      then present quantitative comparisons to the state-of-the-art
      c(bi ) = dmin + (dmax − dmin )(bi /2 +            bj )   (2)       in supervised monocular depth estimation.
                                                  j=1
                                                                         4.1. Datasets and evaluation metrics
   Finally, at each pixel, the final depth value d˜ is calculated
from the linear combination of Softmax scores at that pixel              NYU Depth v2 is a dataset that provides images and
and the depth-bin-centers c(b) as follows:                               depth maps for different indoor scenes captured at a pixel
                                                                         resolution of 640 × 480 [37]. The dataset contains 120K
                              N
                              X                                          training samples and 654 testing samples [8]. We train our
                       d˜ =         c(bk )pk                   (3)       network on a 50K subset. The depth maps have an upper
                              k=1                                        bound of 10 meters. Our network outputs depth prediction
Compared to Fu et al. [11] we do not predict the depth as the            having a resolution of 320 × 240 which we then upsam-
bin center of the most likely bin. This enables us to predict            ple by 2× to match the ground truth resolution during both
smooth depth maps without the discretization artifacts as                training and testing. We evaluate on the pre-defined center
can bee seen in Fig. 5.                                                  cropping by Eigen et al. [8]. At test time, we compute the
                                                                         final output by taking the average of an image’s prediction
3.4. Loss function                                                       and the prediction of its mirror image which is commonly
   Pixel-wise depth loss. Inspired by [26], we use a                     used in previous work.
scaled version of the Scale-Invariant loss (SI) introduced by
Eigen et al. [8]:                                                        KITTI is a dataset that provides stereo images and corre-
                      s                                                  sponding 3D laser scans of outdoor scenes captured using
                         1X 2          λ X 2
          Lpixel = α           gi − 2 (        gi )       (4)            equipment mounted on a moving vehicle [14]. The RGB
                         T i          T     i                            images have a resolution of around 1241 × 376 while the
                                                                         corresponding depth maps are of very low density with lots
where gi = log d˜i − log di and the ground truth depth di                of missing data. We train our network on a subset of around
and T denotes the number of pixels having valid ground                   26K images, from the left view, corresponding to scenes not
truth values. We use λ = 0.85 and α = 10 for all our                     included in the 697 test set specified by [8]. The depth maps
experiments.                                                             have an upper bound of 80 meters. We train our network on
   Bin-center density loss. This loss term encourages the                a random crop of size 704 × 352. For evaluation, we use the
distribution of bin centers to follow the distribution of depth          crop as defined by Garg et al. [13] and bilinearly upsample
values in the ground truth. We would like to encourage the               the prediction to match the ground truth resolution. The fi-
bin centers to be close to the actual ground truth depth val-            nal output is computed by taking the average of an image’s
ues and the other way around. We denote the set of bin                   prediction and the prediction of its mirror image.
centers as c(b) and the set of all depth values in the ground
truth image as X and use the bi-directional Chamfer Loss
                                                                         SUN RGB-D is an indoor dataset consisting of around
[9] as a regularizer:
                                                                         10K images with high scene diversity collected with four
  Lbins = chamf er(X, c(b)) + chamf er(c(b), X)                (5)       different sensors [39, 44, 23]. We use this dataset only for

                                                                     5
            Method                     δ1 ↑             δ2 ↑             δ3 ↑            REL ↓             RMS ↓     log10 ↓
            Eigen et al. [8]           0.769            0.950            0.988           0.158             0.641        –
            Laina et al. [25]          0.811            0.953            0.988           0.127             0.573      0.055
            Hao et al. [16]            0.841            0.966            0.991           0.127             0.555      0.053
            Lee et al. [27]            0.837            0.971            0.994           0.131             0.538        –
            Fu et al. [11]             0.828            0.965            0.992           0.115             0.509      0.051
            SharpNet [34]              0.836            0.966            0.993           0.139             0.502      0.047
            Hu et al. [19]             0.866            0.975            0.993           0.115             0.530      0.050
            Chen et al. [4]            0.878            0.977            0.994           0.111             0.514      0.048
            Yin et al. [47]            0.875            0.976            0.994           0.108             0.416      0.048
            BTS [26]                   0.885            0.978            0.994           0.110             0.392      0.047
            DAV [22]                   0.882            0.980            0.996           0.108             0.412        –
            AdaBins (Ours)             0.903            0.984            0.997           0.103             0.364      0.044

Table 2: Comparison of performances on the NYU-Depth-v2 dataset. The reported numbers are from the corresponding
original papers. Best results are in bold, second best are underlined.

Method                          δ1 ↑           δ2 ↑             δ3 ↑             REL ↓           Sq Rel ↓          RMS ↓       RMS log ↓
Saxena et al. [36]          0.601              0.820            0.926            0.280            3.012            8.734         0.361
Eigen et al. [8]            0.702              0.898            0.967            0.203            1.548            6.307         0.282
Liu et al. [29]             0.680              0.898            0.967            0.201            1.584            6.471         0.273
Godard et al. [15]          0.861              0.949            0.976            0.114            0.898            4.935         0.206
Kuznietsov et al. [24]      0.862              0.960            0.986            0.113            0.741            4.621         0.189
Gan et al. [12]             0.890              0.964            0.985            0.098            0.666            3.933         0.173
Fu et al. [11]              0.932              0.984            0.994            0.072            0.307            2.727         0.120
Yin et al. [47]             0.938              0.990            0.998            0.072              –              3.258         0.117
BTS[26]                     0.956              0.993            0.998            0.059            0.245            2.756         0.096
AdaBins (Ours)              0.964              0.995            0.999            0.058            0.190            2.360         0.088

Table 3: Comparison of performances on the KITTI dataset. We compare our network against the state-of-the-art on this
dataset. The reported numbers are from the corresponding original papers. Measurements are made for the depth range from
0m to 80m. Best results are in bold, second best are underlined.

                                                                                         q P
                                                                                             1  n             2
Loss       δ1 ↑    δ2 ↑     δ3 ↑       REL↓     RMS↓       log10 ↓       error (RMS):        n  p (yp − ŷp ) ); average (log10 ) error:
                                                                         1
                                                                           P  n
                                                                              p |log10 (yp ) − log10 (ŷp )|; threshold accuracy (δi ):
L1 /SSIM   0.888   0.980    0.995      0.107    0.384      0.046         n
SI         0.897   0.984    0.997      0.106    0.368      0.044                                  y   ŷ
                                                                         % of yp s.t. max( ŷpp , ypp ) = δ < thr for thr =
SI+Bins    0.903   0.984    0.997      0.103    0.364      0.044
                                                                         1.25, 1.252 , 1.253 ; where yp is a pixel in depth image y,
Table 4: Comparison of performance with respect to the                   ŷp is a pixel in the predicted depth image ŷ, and n is the
choice of loss function.                                                 total number of pixels for each depth image. Additionally
                                                                         for KITTI, we use the two standard metrics: Squared Rela-
                                                                                                          Pn ky −ŷ k2
                                                                         tive Difference (Sq. Rel): n1 p p y p ; and RMSE log:
                                                                         q P
cross-evaluating pre-trained models on the official test set                 1    n                     2
                                                                             n    p k log yp − log ŷp k .
of 5050 images. We do not use it for training.
                                                                         4.2. Implementation details
Evaluation metrics. We use the standard six metrics used                    We implement the proposed network in PyTorch [33].
in prior work [8] to compare our method against state-                   For training, we use the AdamW optimizer [30] with
of-the-art. These error metrics are defined as: average
                        Pn |y −ŷ |                                      weight-decay 10−2 . We use the 1-cycle policy [38] for the
relative error (REL): n1 p p y p ; root mean squared                     learning rate with max lr = 3.5 × 10−4 , linear warm-up

                                                                     6
                                                                                Method      δ1 ↑    δ2 ↑       δ3 ↑       REL↓      RMS↓     log10 ↓
                                                                                Chen [4]    0.757   0.943      0.984      0.166     0.494    0.071
                                                                                Yin [47]    0.696   0.912      0.973      0.183     0.541    0.082
                                                                                BTS [26]    0.740   0.933      0.980      0.172     0.515    0.075
                                                                                Ours        0.771   0.944      0.983      0.159     0.476    0.068

                                                                                Table 5: Results of models trained on the NYU-Depth-v2
Figure 6: Effect of number of bins (N) on performance as
                                                                                dataset and tested on the SUN RGB-D dataset [39] without
measured by Absolute Relative Error metric. we can ob-
                                                                                fine-tuning.
serve interesting behaviour for lower values of N. As N in-
creases, performance starts to saturate.
                                                                                Variant                 δ1 ↑      δ2 ↑      δ3 ↑     REL ↓   RMS ↓
                                                                                Base + R                0.881     0.980     0.996    0.111   0.419
from max lr/25 to max lr for the first 30% of iterations                        Base + Uniform-Fix-HR   0.892     0.981     0.995    0.107   0.383
followed by cosine annealing to max lr/75. Total number                         Base + Log-Fix-HR       0.896     0.981     0.995    0.108   0.379
                                                                                Base + Train-Fix-HR     0.893     0.981     0.995    0.109   0.381
of epochs is set to 25 with batch size 16. Training our model
                                                                                Base + AdaBins-HR       0.903     0.984     0.997    0.103   0.364
takes 20 min per epoch on a single node with four NVIDIA
V100 32GB GPUs. For all results presented we train for 25                       Table 6: Comparison of different design choices for bin-
epochs. Our main model has about 78M parameters: 28M                            widths and regression. AdaBins module results in a signif-
for the CNN encoder, 44M for the CNN decoder, and 5.8M                          icant boost in performance. Base: encoder-decoder with an
for the new AdaBins module.                                                     EfficientNet B5 encoder. R: standard regression. HR: Hy-
                                                                                brid Regression. (Log)Uniform-Fix: Fixed (log) uniform
4.3. Comparison to the state-of-the-art
                                                                                bin-widths. Train-Fix: Trained bin-widths but Fixed for
   We consider the following two methods to be our main                         each dataset.
competitors: BTS [26] and DAV [22]. For completeness,
we also include selected previous related methods in the
comparison tables. For BTS and DAV we report the cor-                           our network on the NYU-Depth-v2 dataset and evaluate it
responding evaluation numbers from their papers. For BTS                        on the test set of the SUN RGB-D dataset without any fine-
we also verified these numbers by retraining their network                      tuning. For comparison, we also used the same strategy for
using the authors code. DAV did not have code available by                      competing methods for which pretrained models are avail-
the deadline, but the authors sent us the resulting depth im-                   able [26, 47, 4] and report results in Table. 5.
ages used in our figures. In our tables we report the numbers
given by the authors in their paper 2 .                                         4.4. Ablation study
   NYU-Depth-v2: See Table 2 for the comparison of the                             For our ablation study, we evaluate the influence of the
performance on the official NYU-Depth-v2 test set. While                        following design choices on our results:
the state of the art performance on NYU has been saturated                         AdaBins: We first evaluate the importance of our Ad-
for quite some time, we were able to significantly outper-                      aBins module. We remove the AdaBins block from the ar-
form the state of the art in all metrics. The large gap to the                  chitecture and use the encoder-decoder to directly predict
previous state of the art emphasises that our proposed archi-                   the depth map by setting Cd = 1. We then use the loss
tecture addition makes an important contribution to improv-                     given by Eq. 4 to train the network. We call this design
ing the results.                                                                standard regression and compare it against variants of our
   KITTI: Table 3 lists the performance metrics on the                          AdaBins module. Table. 6 shows that the architecture with-
KITTI dataset. Our proposed architecture significantly out-                     out AdaBins (Row 1) performs worse than all other variants
performs previous state-of-the-art across all metrics. In                       (Rows 2-5).
particular, our method improves the RMS score by about                             Bin types: In this set of experiments we examine the
13.5% and Squared Relative Difference by 22.4% over the                         performance of adaptive bins over other choices as stated
previous state-of-the-art.                                                      in Sec. 3.2. Table. 6 lists results for all the discussed vari-
   SUN RGB-D: To compare the generalisation perfor-                             ants. The Trained-but-Fixed variant performs worst among
mance, we perform a cross-dataset evaluation by training                        all choices and our final choice employing adaptive bins
                                                                                significantly improves the performance and outperforms all
   2 The authors of DAV clarified in an email that they compute the depth
                                                                                other variants.
maps at 1/4th the resolution and then downsample the ground truth for
evaluation. However, we believe that all other methods, including ours,            Number of bins (N ): To study the influence of the num-
evaluate at the full resolution.                                                ber of bins, we train our network for various values of N

                                                                            7
                             (a) RGB      (b) BTS [26]   (c) DAV [4]        (d) Ours        (e) GT

                 Figure 7: Qualitative comparison with the state-of-the-art on the NYU-Depth-v2 dataset.

                   (a) RGB                               (b) BTS [26]                                (c) Ours

                      Figure 8: Qualitative comparison with the state-of-the-art on the KITTI dataset.

and measure the performance in terms of Absolute Rela-             solute Relative Error from 10.6% to 10.3%.
tive Error metric. Results are plotted in Fig. 6. Interest-
ingly, starting from N = 20, the error first increases with
increasing N and then decreases significantly. As we keep
increasing N above 256, and with higher values the gain in
                                                                   5. Conclusion
performance starts to diminish. We use N = 256 for our
final model.
                                                                      We introduced a new architecture block, called AdaBins
   Loss function: Table. 4 lists performance corresponding         for depth estimation from a single RGB image. AdaBins
to the three choices of loss function. Firstly, the L1 /SSIM       leads to a decisive improvement in the state of the art for the
combination does not lead to the state-of-the-art perfor-          two most popular datasets, NYU and KITTI. In future work,
mance in our case. Secondly, we trained our network with           we would like to investigate if global processing of informa-
and without the proposed Chamfer loss (Eq. 5). Introducing         tion at a high resolution can also improve performance on
the Chamfer loss clearly gives a boost to the performance.         other tasks, such as segmentation, normal estimation, and
For example, introducing the Chamfer loss reduces the Ab-          3D reconstruction from multiple images.

                                                               8
References                                                               [12] Yukang Gan, Xiangyu Xu, Wenxiu Sun, and Liang Lin.
                                                                              Monocular depth estimation with affinity, vertical pooling,
 [1] Ibraheem Alhashim and Peter Wonka.             High quality              and label enhancement. In Vittorio Ferrari, Martial Hebert,
     monocular depth estimation via transfer learning. CoRR,                  Cristian Sminchisescu, and Yair Weiss, editors, Computer
     abs/1812.11941, 2018. 2, 3, 5                                            Vision – ECCV 2018, pages 232–247, Cham, 2018. Springer
 [2] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas               International Publishing. 6
     Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-          [13] Ravi Garg, Vijay Kumar B.G., Gustavo Carneiro, and Ian
     end object detection with transformers. In Andrea Vedaldi,               Reid. Unsupervised cnn for single view depth estimation:
     Horst Bischof, Thomas Brox, and Jan-Michael Frahm, edi-                  Geometry to the rescue. In Bastian Leibe, Jiri Matas, Nicu
     tors, Computer Vision – ECCV 2020, pages 213–229, Cham,                  Sebe, and Max Welling, editors, Computer Vision – ECCV
     2020. Springer International Publishing. 2, 3, 4                         2016, pages 740–756, Cham, 2016. Springer International
 [3] Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian                  Publishing. 5
     Schroff, and Hartwig Adam. Encoder-decoder with atrous              [14] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel
     separable convolution for semantic image segmentation. In                Urtasun. Vision meets robotics: The kitti dataset. I. J.
     ECCV, 2018. 11                                                           Robotics Res., 32:1231–1237, 2013. 1, 2, 5
 [4] Xiaotian Chen, Xuejin Chen, and Zheng-Jun Zha. Structure-           [15] Clément Godard, Oisin Mac Aodha, and Gabriel J. Bros-
     aware residual pyramid network for monocular depth esti-                 tow. Unsupervised monocular depth estimation with left-
     mation. In Proceedings of the Twenty-Eighth International                right consistency. 2017 IEEE Conference on Computer Vi-
     Joint Conference on Artificial Intelligence, IJCAI-19, pages             sion and Pattern Recognition (CVPR), pages 6602–6611,
     694–700. International Joint Conferences on Artificial Intel-            2017. 2, 6
     ligence Organization, 7 2019. 6, 7, 8                               [16] Zhixiang Hao, Yu Li, Shaodi You, and Feng Lu. Detail pre-
 [5] Marcella Cornia, Matteo Stefanini, Lorenzo Baraldi, and                  serving depth estimation from a single image using attention
     Rita Cucchiara. Meshed-memory transformer for image cap-                 guided networks. 2018 International Conference on 3D Vi-
     tioning. In IEEE/CVF Conference on Computer Vision and                   sion (3DV), pages 304–313, 2018. 2, 6
     Pattern Recognition (CVPR), June 2020. 3                            [17] Caner Hazirbas, Lingni Ma, Csaba Domokos, and Daniel
 [6] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                   Cremers. Fusenet: Incorporating depth into semantic seg-
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,                      mentation via fusion-based cnn architecture. In ACCV, 2016.
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-                 1
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is          [18] Simao Herdade, Armin Kappeler, Kofi Boakye, and Joao
     worth 16x16 words: Transformers for image recognition at                 Soares. Image captioning: Transforming objects into words.
     scale. arXiv preprint arXiv:2010.11929, 2020. 2, 4                       In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-
                                                                              Buc, E. Fox, and R. Garnett, editors, Advances in Neural
 [7] Ruofei Du, Eric Lee Turner, Maksym Dzitsiuk, Luca Prasso,
                                                                              Information Processing Systems, volume 32, pages 11137–
     Ivo Duarte, Jason Dourgarian, Joao Afonso, Jose Pascoal,
                                                                              11147. Curran Associates, Inc., 2019. 3
     Josh Gladstone, Nuno Moura e Silva Cruces, Shahram Izadi,
                                                                         [19] Junjie Hu, Mete Ozay, Yan Zhang, and Takayuki Okatani.
     Adarsh Kowdle, Konstantine Nicholas John Tsotsos, and
                                                                              Revisiting single image depth estimation: Toward higher
     David Kim. Depthlab: Real-time 3d interaction with depth
                                                                              resolution maps with accurate object boundaries. 2019
     maps for mobile augmented reality. In Proceedings of the
                                                                              IEEE Winter Conference on Applications of Computer Vision
     33rd Annual ACM Symposium on User Interface Software
                                                                              (WACV), pages 1043–1051, 2018. 2, 6
     and Technology, page 15, 2020. 1
                                                                         [20] Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kil-
 [8] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map                ian Q. Weinberger. Densely connected convolutional net-
     prediction from a single image using a multi-scale deep net-             works. 2017 IEEE Conference on Computer Vision and Pat-
     work. In NIPS, 2014. 2, 5, 6                                             tern Recognition (CVPR), pages 2261–2269, 2017. 4
 [9] H. Fan, H. Su, and L. Guibas. A point set generation network        [21] Po-Han Huang, Kevin Matzen, Johannes Kopf, Narendra
     for 3d object reconstruction from a single image. In 2017                Ahuja, and Jia-Bin Huang. Deepmvs: Learning multi-view
     IEEE Conference on Computer Vision and Pattern Recogni-                  stereopsis. 2018 IEEE/CVF Conference on Computer Vision
     tion (CVPR), pages 2463–2471, 2017. 5                                    and Pattern Recognition, pages 2821–2830, 2018. 2
[10] Philipp Fischer, Alexey Dosovitskiy, Eddy Ilg, Philip               [22] Lam Huynh, Phong Nguyen-Ha, Jiri Matas, Esa Rahtu, and
     Häusser, Caner Hazirbas, Vladimir Golkov, Patrick van der               Janne Heikkila. Guiding monocular depth estimation using
     Smagt, Daniel Cremers, and Thomas Brox. Flownet: Learn-                  depth-attention volume. arXiv preprint arXiv:2004.02760,
     ing optical flow with convolutional networks. 2015 IEEE                  2020. 1, 2, 3, 6, 7, 11, 12
     International Conference on Computer Vision (ICCV), pages           [23] Allison Janoch, Sergey Karayev, Yangqing Jia, Jonathan T
     2758–2766, 2015. 2                                                       Barron, Mario Fritz, Kate Saenko, and Trevor Darrell. A
[11] Huan Fu, Mingming Gong, Chaohui Wang, Nematollah Bat-                    category-level 3d object dataset: Putting the kinect to work.
     manghelich, and Dacheng Tao. Deep ordinal regression net-                In Consumer depth cameras for computer vision, pages 141–
     work for monocular depth estimation. 2018 IEEE/CVF Con-                  165. Springer, 2013. 5
     ference on Computer Vision and Pattern Recognition, pages           [24] Yevhen Kuznietsov, Jörg Stückler, and Bastian Leibe. Semi-
     2002–2011, 2018. 2, 3, 5, 6                                              supervised deep learning for monocular depth map predic-

                                                                     9
     tion. 2017 IEEE Conference on Computer Vision and Pattern                 Intervention – MICCAI 2015, pages 234–241, Cham, 2015.
     Recognition (CVPR), pages 2215–2223, 2017. 6                              Springer International Publishing. 2
[25] Iro Laina, Christian Rupprecht, Vasileios Belagiannis, Fed-          [36] Ashutosh Saxena, Sung H. Chung, and Andrew Y. Ng.
     erico Tombari, and Nassir Navab. Deeper depth prediction                  Learning depth from single monocular images. In Pro-
     with fully convolutional residual networks. 2016 Fourth In-               ceedings of the 18th International Conference on Neural In-
     ternational Conference on 3D Vision (3DV), pages 239–248,                 formation Processing Systems, NIPS’05, page 1161–1168,
     2016. 2, 6                                                                Cambridge, MA, USA, 2005. MIT Press. 6
[26] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and                        [37] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
     Il Hong Suh. From big to small: Multi-scale local planar                  Fergus. Indoor segmentation and support inference from
     guidance for monocular depth estimation. arXiv preprint                   rgbd images. In Computer Vision – ECCV 2012, pages 746–
     arXiv:1907.10326, 2019. 1, 2, 5, 6, 7, 8, 11, 12, 13                      760, Berlin, Heidelberg, 2012. Springer Berlin Heidelberg.
[27] Wonwoo Lee, Nohyoung Park, and Woontack Woo. Depth-                       1, 2, 5, 11
     assisted real-time 3d object detection for augmented reality.        [38] Leslie N. Smith and Nicholay Topin. Super-convergence:
     ICAT’11, 2:126–132, 2011. 1, 6                                            Very fast training of residual networks using large learning
[28] Jaakko Lehtinen, Jacob Munkberg, Jon Hasselgren, Samuli                   rates. CoRR, abs/1708.07120, 2017. 6
     Laine, Tero Karras, Miika Aittala, and Timo Aila.                    [39] S. Song, S. P. Lichtenberg, and J. Xiao. Sun rgb-d: A rgb-d
     Noise2Noise: Learning image restoration without clean data.               scene understanding benchmark suite. In 2015 IEEE Confer-
     In Jennifer Dy and Andreas Krause, editors, Proceedings                   ence on Computer Vision and Pattern Recognition (CVPR),
     of the 35th International Conference on Machine Learning,                 pages 567–576, 2015. 5, 7, 11
     volume 80 of Proceedings of Machine Learning Research,               [40] Mingxing Tan and Quoc V. Le. Efficientnet: Rethinking
     pages 2965–2974, Stockholmsmässan, Stockholm Sweden,                     model scaling for convolutional neural networks. In Ka-
     10–15 Jul 2018. PMLR. 2                                                   malika Chaudhuri and Ruslan Salakhutdinov, editors, Pro-
                                                                               ceedings of the 36th International Conference on Machine
[29] Fayao Liu, Chunhua Shen, Guosheng Lin, and I. Reid.
                                                                               Learning, ICML 2019, 9-15 June 2019, Long Beach, Cali-
     Learning depth from single monocular images using deep
                                                                               fornia, USA, volume 97 of Proceedings of Machine Learning
     convolutional neural fields. IEEE Transactions on Pattern
                                                                               Research, pages 6105–6114. PMLR, 2019. 3
     Analysis and Machine Intelligence, 38:2024–2039, 2016. 6
                                                                          [41] Benjamin Ummenhofer, Huizhong Zhou, Jonas Uhrig, Niko-
[30] I. Loshchilov and F. Hutter. Decoupled weight decay regu-
                                                                               laus Mayer, Eddy Ilg, Alexey Dosovitskiy, and Thomas
     larization. In ICLR, 2019. 6
                                                                               Brox. Demon: Depth and motion network for learning
[31] Francesc Moreno-Noguer, Peter N. Belhumeur, and Shree K.                  monocular stereo. 2017 IEEE Conference on Computer Vi-
     Nayar. Active refocusing of images and videos. ACM Trans.                 sion and Pattern Recognition (CVPR), pages 5622–5631,
     Graph., 26(3), July 2007. 1                                               2017. 2
[32] Niki Parmar, Ashish Vaswani, Jakob Uszkoreit, Lukasz                 [42] Jiheng Wang, Alan C. Bovik, Hamid R. Sheikh, and Eero P.
     Kaiser, Noam Shazeer, Alexander Ku, and Dustin Tran. Im-                  Simoncelli. Image quality assessment: from error visibility
     age transformer. In Jennifer Dy and Andreas Krause, edi-                  to structural similarity. IEEE Transactions on Image Pro-
     tors, Proceedings of Machine Learning Research, volume 80                 cessing, 13:600–612, 2004. 5
     of Proceedings of Machine Learning Research, pages 4055–             [43] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaim-
     4064, Stockholmsmässan, Stockholm Sweden, 10–15 Jul                      ing He. Non-local neural networks. In Proceedings of the
     2018. PMLR. 2                                                             IEEE Conference on Computer Vision and Pattern Recogni-
[33] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer,                      tion (CVPR), June 2018. 2
     James Bradbury, Gregory Chanan, Trevor Killeen, Zeming               [44] J. Xiao, A. Owens, and A. Torralba. Sun3d: A database of
     Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison,                    big spaces reconstructed using sfm and object labels. In 2013
     Andreas Kopf, Edward Yang, Zachary DeVito, Martin Rai-                    IEEE International Conference on Computer Vision, pages
     son, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner,                 1625–1632, 2013. 5
     Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An               [45] Dan Xu, Elisa Ricci, Wanli Ouyang, Xiaogang Wang, and
     imperative style, high-performance deep learning library. In              Nicu Sebe. Multi-scale continuous crfs as sequential deep
     H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc,               networks for monocular depth estimation. In Proceedings
     E. Fox, and R. Garnett, editors, Advances in Neural Infor-                of the IEEE Conference on Computer Vision and Pattern
     mation Processing Systems, volume 32, pages 8026–8037.                    Recognition, pages 5354–5362, 2017. 2
     Curran Associates, Inc., 2019. 6                                     [46] Dong Xu, Wei Wang, Hao Tang, Hong W. Liu, Nicu
[34] Michael Ramamonjisoa and Vincent Lepetit. Sharpnet: Fast                  Sebe, and Elisa Ricci. Structured attention guided convo-
     and accurate recovery of occluding contours in monocular                  lutional neural fields for monocular depth estimation. 2018
     depth estimation. In Proceedings of the IEEE/CVF Interna-                 IEEE/CVF Conference on Computer Vision and Pattern
     tional Conference on Computer Vision (ICCV) Workshops,                    Recognition, pages 3917–3925, 2018. 2
     Oct 2019. 6                                                          [47] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
[35] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-                    forcing geometric constraints of virtual normal for depth pre-
     net: Convolutional networks for biomedical image segmen-                  diction. In Proceedings of the IEEE/CVF International Con-
     tation. In Medical Image Computing and Computer-Assisted                  ference on Computer Vision (ICCV), October 2019. 6, 7

                                                                     10
[48] Huizhong Zhou, Benjamin Ummenhofer, and Thomas Brox.             Layer   Input Dimension   Output Dimension   Activation
     Deeptam: Deep tracking and mapping. In Proceedings of the                                                     LeakyReLU
     European Conference on Computer Vision (ECCV), pages             FC            E                 256
                                                                                                                   (negative slope=0.01)
     822–838, 2018. 2                                                                                              LeakyReLU
                                                                      FC           256                256
                                                                                                                   (negative slope=0.01)
                                                                      FC           256                 N           ReLU
A. Appendix
                                                                      Table 7: Architecture details of MLP head. FC: Fully Con-
A.1. Geometric Consistency                                            nected layer, E: Embedding dimension, N: Number of bins

    We provide a qualitative evaluation of the geometric con-
sistency of depth maps predicted by our model. Surface nor-
mal maps provide a good way to visualize the orientation
and texture details of surfaces present in the scene. Fig 9
shows the visualization of the normals extracted from the
depth maps for our model and for DAV [22] and BTS [26].
Although the orientations predicted by DAV seems to be
consistent, the texture details are almost completely lost.
BTS, on the other hand, preserves the texture but sometimes
results in erroneous orientation details. Our method exhibits
detailed texture and consistent orientations without explic-
itly imposing geometric constraints, such as co-planarity,
used by other methods [22, 26].

A.2. Generlization Analysis

   Here we qualitatively analyze the capability of our
method to generalise to unseen data. We use the models
(AdaBins and BTS [26]) trained on NYU-Depth-v2 [37] but
show predictions on SUN RGB-D [39] dataset in Fig 10.
Depth maps predicted by BTS have conspicuous artifacts
whereas our method provides consistent results on the un-
seen data.

A.3. More Results on KITTI dataset

   Fig 11 shows a qualitative comparison of BTS [26] and
our method on the KITTI dataset. For better visualization,
we have removed the sky regions from the visualized depth
maps using segmentation masks predicted by a pretrained
segmentation model[3]. We can observe that our method
demonstrates superior performance particularly in predict-
ing extents and edges of the on-road vehicles, sign-boards
and thin poles. Additionally, BTS tends to blend the far-
ther away objects with background whereas our method pre-
serves the structure with clear separation.

A.4. MLP Head Details

    We use a three-layer MLP on the first output embedding
of the transformer in the mini-ViT module. The architecture
details with parameters are given in Table 7.

                                                                 11
RGB                         DAV [22]                       BTS [26]                     Ours

      Figure 9: Visualization of surface normals extracted from predicted depth maps.

                                            12
                    RGB                    BTS [26]                  Ours                     GT

Figure 10: Qualitative comparison of generalization from NYU-Depth-v2 to SUN RGB-D dataset. Darker pixels are farther.
Missing ground truth values are shown in white.

                RGB                                    BTS [26]                                    Ours

                                 Figure 11: Qualitative comparison on KITTI dataset.

                                                         13
