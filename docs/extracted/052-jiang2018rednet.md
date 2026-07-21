---
source_id: 052
bibtex_key: jiang2018rednet
title: RedNet: Residual Encoder-Decoder Network for Indoor RGB-D Semantic Segmentation
year: 2018
domain_theme: Segmentasi RGB-D
verified_pdf: 52_RedNet.pdf
char_count: 41289
---

RedNet: Residual Encoder-Decoder Network for
                                           indoor RGB-D Semantic Segmentation

                                                    Jindong Jiang, Lunan Zheng, Fei Luo, and Zhijun Zhang

                                            The School of Automation Science and Engineering, South China University of
                                                               Technology, Guangzhou 510640, China
arXiv:1806.01054v2 [cs.CV] 6 Aug 2018

                                                             jdpshq@gmail.com, aulnzheng@sina.com,
                                                                {aufeiluo,auzjzhang}@scut.edu.cn

                                               Abstract. Indoor semantic segmentation has always been a difficult
                                               task in computer vision. In this paper, we propose an RGB-D residual
                                               encoder-decoder architecture, named RedNet, for indoor RGB-D seman-
                                               tic segmentation. In RedNet, the residual module is applied to both the
                                               encoder and decoder as the basic building block, and the skip-connection
                                               is used to bypass the spatial feature between the encoder and decoder. In
                                               order to incorporate the depth information of the scene, a fusion struc-
                                               ture is constructed, which makes inference on RGB image and depth
                                               image separately, and fuses their features over several layers. In order
                                               to efficiently optimize the network’s parameters, we propose a ‘pyra-
                                               mid supervision’ training scheme, which applies supervised learning over
                                               different layers in the decoder, to cope with the problem of gradients van-
                                               ishing. Experiment results show that the proposed RedNet(ResNet-50)
                                               achieves a state-of-the-art mIoU accuracy of 47.8% on the SUN RGB-D
                                               benchmark dataset.

                                        1    Introduction

                                        Indoor space is likely to be the main workplace for service robots in the near
                                        future. In order to work well in an indoor space, the robots should possesses the
                                        ability of visual scene understanding. To do so, the semantic segmentation in
                                        indoor scene is becoming one of the most popular tasks in computer vision.
                                            Over the pass few years, fully convolutional networks (FCNs) type architec-
                                        tures have shown great potential on semantic segmentation task [27,28,1,4,38,25,39],
                                        and have dominated the semantic segmentation task of many datasets [11,5,34].
                                        Some of this FCNs-type architectures focus on indoor environment, and usu-
                                        ally utilize the depth information as the complementary information for RGB to
                                        improve the segmentation [27,6,14,15]. In general, the FCNs architectures can
                                        be generally divide into two categories, i.e., the encoder-decoder type architec-
                                        tures and dilated convolution architectures. The encoder-decoder architectures
                                        [27,28,1,25,15] have a downsample path to extract the semantic information from
                                        images and a upsample path to recover a full-resolution semantic segmentation
                                        map. By contrast, the dilated convolution architectures [4,38,39] employ dilated
2      J. Jiang et al.

         RGB                                                            Output

                                     Skip Connection

                             Depth Fusion              Pyramid Output
         Depth

                 Fig. 1. Overall structure of the proposed network.

convolution such that the convolutional network expands receptive field expo-
nentially without downsampling. With less or even zero downsampling operation,
dilated architectures keep the spatial information in the image through out the
whole networks, so the architectures serve as a discriminative model that clas-
sify every pixel on the image. Encoder-decoder architectures, on the other hand,
lost spatial information during the discriminative encoder, and thus some of the
networks apply skip-architecture to recover the spatial information during the
generative decoder path.
   Even though the dilated convolution architectures have the advantage of
keeping the spatial information, they generally have higher memory consumption
on the training step. Because the spatial resolution of the activation map is not
downsampled as the network proceed and it needs to be stored for gradient
computation. Therefore, the high memory consumption stops the network from
having a deeper structure. This could cause disadvantages on this method, since
convolutional networks learn richer features as the structure gets deeper, which
would benefit the inference of the semantic information.
    In this paper, we propose a novel structure named RedNet that employ the
encoder-decoder network structure for indoor RGB-D semantic segmentation. In
RedNet, the residual block is used as the building module to avoid the model
degradation problem [16]. This allows the performance of networks to improve
as the structure goes deeper. Moreover, we apply fusion structure to incorpo-
rate depth information into the network, and use skip-architecture to bypass
the spatial information from encoder to decoder. Further, inspired by the train-
ing scheme in [35], we propose the pyramid supervision that apply supervised
learning over different layers on the decoder for better optimization. The overall
structure of RedNet is illustrated in Fig. 1.
                         RedNet for indoor RGB-D Semantic Segmentation          3

    The remainder of this paper is organized in four sections. In section 2, the
literature on residual networks and indoor RGB-D semantic segmentation is
previewed. The architecture of RedNet and the idea of pyramid supervision
are stated in detail in section 3. In section 4, the comparative experiments are
conducted to evaluate the efficiency of the model. Finally, we draw a conclusion
of this paper in section 5.
    Before ending this section, the main contributions of this paper are listed as
the following.

1. A novel residual encoder-decoder architecture (termed RedNet) is proposed
   for indoor RGB-D semantic segmentation, which applies residual module as
   the basic building block in both the encoder path and decoder path.
2. A pyramid supervision training scheme is proposed to optimize the network,
   which applies supervised learning over different layers on the upsample path
   of the model.
3. Two comparison experiments are conducted on SUN RGB-D benchmark to
   verify the effectiveness of the proposed RedNet architecture and the pyramid
   supervision training scheme.

2     Related Work

2.1   Residual Networks

Residual network was first proposed by He et al. in [16]. In their work, they
analyzed the problem of model degradation, which present as saturation and
then degradation of accuracy as the network depth increasing. They argued
that the degradation problem is an optimization problem, and as the depth of
the network increase, the network gets harder to train. It was assumed that the
desired mapping of a convnet is comprised of an identity mapping and a residual
mapping. Therefore, a deep residual learning framework is proposed. Instead of
letting a convnet learn the desired mapping, it fits the residual mapping and uses
shortcut connection to merge it with the identity input. With this configuration,
the residual network become easy to optimize and can enjoy accuracy gains from
greatly increased depth. Veit et al. [36] presented a complementary explanation
of the increased performance of residual networks, i.e., the residual networks
avoid the vanishing gradient problem by introducing the short paths between
input and output. Later, He et al. [17] analyzed the propagation formulations
behind the connection mechanisms of residual networks and proposed a new
structure of residual unit. In their work, they extended the depth of a deep
residual networks to 1001 layers. Zagoruyko et al. [40] investigated the memory
consumption of residual networks and propose a novel residual unit that aims
to decrease depth and increase width of a deep residual network.
    The idea of residual learning was later adopted to architectures for seman-
tic segmentation task. Pohlen et al. [30] proposed a fully convolutional network
with residual learning for semantic segmentation in street scenes. The network
4      J. Jiang et al.

has an encoder-decoder architecture and applies residual module on the skip-
connection structure with the full-resolution residual units (FRRUs). Quan et
al. [31] presented a FCN architecture, named FusionNet, for connectomics image
segmentation. Instead of using residual block on skip-connection structure, Fu-
sionNet applies them on each layer in the encoder and decoder path along with
standard convolution, max-pooling, and transpose of convolution [28]. Similarly,
Drozdzal et al. [8] studied the importance of skip-connection in biomedical image
segmentation, showing that the “short skip connections” in residual module is
more effective than the “long skip connections” between encoder and decoder
on biomedical image analyzing. Yu et al. [39] combined the idea of residual net-
works and dilated convolution to build a dilated residual networks for semantic
segmentation. In their paper, they also studied the gridding artifact introduced
by dilation convolution and developed a ‘degridding’ method to removing these
artifacts. Dai et al. [7] used ResNet-101 as the basic network and apply the
Multi-task Network Cascades for instance segmentation. Lin et al. [25] and Lin
et al. [24] also used ResNet structure as a feature extractor and employed a
multi-path refinement network to exploits information along the down-sampling
process for full resolution semantic segmentation.
     In 2017, Chaurasia et al. [3] proposed a encoder-decoder architecture (named
LinkNet) for efficient semantic segmentation. The LinkNet architecture uses
ResNet18 as the encoder and applies the bottleneck unit in the decoder for
feature upsample. Under this efficient configuration, the network achieve state-
of-the-art accuracy on several uban street dataset [5,2]. Inspired by this work,
we propose a straightforward encoder-decoder structure that apply residual unit
on both the downsample path and upsample path, and employs the pyramid
supervision to optimize it.

2.2   Indoor RGB-D Semantic Segmentation

Currently, the accurate indoor semantic segmentation is still a challenging prob-
lem due to the high similarity of color and structure between objects, and the
non-uniform illumination in indoor environment. Therefore, some work started
utilizing the depth information as the complementary information to solve the
problem. For instance, Koppula et al. [22] and Huang et al. [18] used depth in-
formation to build 3D point clouds of full indoor scenes, and applied graphical
model to capture features and contextual relations of objects in RGB-D data
for semantic labeling. Gupta et al. [13] proposed a superpixel-based architec-
ture for RGB-D semantic segmentation in indoor scene. Their method applied
superpixel regions extraction on RGB image and feature extraction of each su-
perpixel on RGB-D data, then employ Random Forest (RF) and Support Vector
Machine (SVM) to classify each superpixel and build a full-resolution semantic
map. Later, Gupta et al. [14] improved this segmentation model by introduc-
ing a HHA encoding for depth information and use a Convolutional Neural
Network (CNN) for feature extraction. In HHA encoding, depth information is
encoded into three channel, i.e., horizontal disparity, height above ground, and
                          RedNet for indoor RGB-D Semantic Segmentation           5

angle between gravity & surface normal. These implied that the HHA encoding
emphasize the geocentric discontinuities in the image.
    After the release of several indoor RGB-D datasets [32,20,33,34], many re-
searches started employing deep learning architectures for indoor semantic seg-
mentation. Couprie et al. [6] presented a multi-scale convolutional network for
indoor semantic segmentation. The study showed that the recognition of object
classes with similar depth appearance and location is improved when incorpo-
rating the depth information. Long et al. [27] applied FCNs structure on indoor
semantic segmentation and compare different inputs to the network, includ-
ing three channel RGB, stacked four channel RGB-D, and stacked six channel
RGB-HHA. The research further showed that the RGB-HHA input outperform
all other input form, while the RGB-D have similar accuracy with RGB input.
Hazirbas et al. [15] presented a fusion-based encoder-decoder FCNs for indoor
RGB-D semantic segmentation. Their work shows that the HHA encoding does
not hold more information than the depth itself. In order to fully utilize the depth
information, they apply two branches of convolutional network to compute RGB
and depth image respectively and apply features fusion on different layers. Based
on the same depth fusion structure, our previous work [21] proposed a DeepLab-
type architecture [4] that applies depth incorporation on a dilated FCNs and
build a RGB-D conditional random field (CRF) as the post-process.
    In this work, we will also apply depth fusion structure on the downsample
part of the network, and apply skip-connection to bypass the fused information
to the decoder for full-resolution semantic prediction.

3     Approach

3.1   RedNet Architecture

The architecture of RedNet is presented in Fig. 2. For clear illustration, we use
blocks with different color to indicate different kinds of layers. Notice that each
convolution operation in RedNet is followed by a batch normalization layer [19]
before relu function, and it is omitted in the figure for simplification.
    The upper half of the figure up to Layer4/Layer4 d is the encoder of the
network, it has two convolutional branches, i.e., the RGB branch and the Depth
branch. Structures of both encoder branches can be adopted from one of the
five ResNet architectures proposed in [16], in which we remove the last two
layers of ResNet, i.e., the global average pooling layer and fully-connected layer.
The RGB branch and the Depth branch in the model have the same network
configuration, except that the convolution kernel of Conv1 d on Depth branch
has only one feature channel, since the Depth input presented as an one channel
gray image. The encoder starts with two downsample operation, which is the
7 × 7 convolution layer with stride two and a 3 × 3 max-pooling layer with stride
two. This max-pooling is the only pooling layer in the whole architecture, all
other downsample and upsample operations in the network are implemented
with two-stride convolution and transpose of convolution. The following layers
6      J. Jiang et al.

                                     RGB        Depth
                                    Conv1       Conv1_d

                                     Pool1      Pool1_d

                                    Layer1      Layer1_d
                                                           Convolution Layer

                                    Layer2      Layer2_d

                                                           MaxPooling Layer
                                    Layer3      Layer3_d

                                    Layer4      Layer4_d
             Agent0                                         Residual Layer

                 Agent1

                      Agent2        Agent4

                          Agent3
                                    Trans1                     ResLayer
                                                           with Downsample

                                                ConvO1
                                    Trans2
                                                 Out1

                                                ConvO2        ResLayer
                                    Trans3
                                                 Out2       with Upsample

                                                ConvO3
                                    Trans4
                                                 Out3
                                                           Transpose of Conv
                                    Trans5
                                   Final Conv   ConvO4

                                   Output        Out4

         Fig. 2. Layer configuration of the proposed RedNet (ResNet-50).

in encoder are residual layers with different numbers of residual unit. It is worth
pointing out that only Layer1 in the encoder does not have downsample unit,
and all other ResLayer have one residual unit that downsample the feature map
and increase the feature channel by a factor of 2. The Depth branch ending
at Layer4 d, and its features are fused into RGB branch on five layers. Here,
element-wise summation is performed as the feature fusion method.
                                                   RedNet for indoor RGB-D Semantic Segmentation                                                                         7

                                Conv [(1, 1), 1, /2]
                                                                                        Conv [(3, 3), 2, *2]                                      Conv [(3, 3), 1, *1]
                                  relu
   Conv [(1, 1), 2, *2]         Conv [(3, 3), 2, *1]       Conv [(1, 1), 2, *2]           relu                     Conv [(2, 2), 0.5, /2]           relu
                                  relu
                                                                                        Conv [(3, 3), 1, *1]                                  Conv [(3, 3), 0.5, /2]
                                Conv [(1, 1), 1, *4]

                                  relu                                                    relu                                                      relu

                          (a)                                                     (b)                                                       (c)

Fig. 3. Downsample and upsample residual unit. (a): a downsample residual unit in
(ResNet-50) encoder. (b): a downsample residual unit in (ResNet-34) encoder. (c): a
upsample residual unit we propose in decoder.

    The lower half of Fig. 2, starting with Trans1 layer, is the decoder of the
network. Here, except the Final Conv layer, which is a single 2 × 2 transpose of
convolution layer, all other layers in the decoder are residual layers. The first four
layers, i.e., the Trans1, Trans2, Trans3, and Trans4, have one upsample residual
unit to upsample the feature map by a factor of 2. Different from the bottleneck
building block in the encoder, we employ the standard residual building block [16]
in the decoder that have two consecutive 3 × 3 convolution layers for residual
computation. With regard to the upsample operation, we present a upsample
residual unit that is shown in Fig. 3(c). In Fig. 3, we compare the downsample
unit in ResNet-50 and ResNet-34, as well as the upsample unit we propose in
the decoder. Here, for Conv[(k, k), s, ∗/c], (k, k) means the spatial size of the
convolution kernel. Parameter s is the stride of the convolution, and c is the
increase or decrease factor of the output feature channel. Red block denotes
the convolution that changes the spatial size of the input feature map, i.e.,
downsample or upsample. For example, a Conv[(2, 2), 0.5, /2] in red means a
2 × 2 kernel size transpose of convolution that upsample the width and height
of the feature map by a factor of 2 and decrease the feature channel by a factor
of 2.

                      Table 1. Encoder (ResNet-50) and Decoder configuration

                                                  Encoder                                                               Decoder
                   Block                                                                  Block
                                         m             n         lunit                                         m          n            lunit
                   Layer4                1024          2048      3                        Trans1               512        256          6
                   Layer3                512           1024      6                        Trans2               256        128          4
                   Layer2                256           512       4                        Trans3               128        64           3
                   Layer1                64            256       3                        Trans4               64         64           3
                   Conv1                 3             64        -                        Trans5               64         64           3
8       J. Jiang et al.

    Table 1 shows the network configuration when using ResNet-50 as the en-
coder, here m denotes the number of input feature channel, n denote the number
of output feature channel, and lunit denote the number of residual unit in that
layer. The upsample ResLayer has different residual unit order compared with
the downsample ResLayer. The downsample layer starts with a downsample
residual unit and followed by several residual units, by contrast, the upsam-
ple layer starts with several residual unit and ends with one upsample residual
unit. As shown in the table, the output of residual layer in ResNet-50 encoder
has large channel size since it use channel expansion. Therefore, we employ the
Agent layers shown in Fig. 2, which are single 1 × 1 convolutional layer with
strides one. It is designed to project the feature map for lower channel size, al-
lowing the decoder to have a lower memory consumption. Notice that the agent
layers only exist when ResNet-50 is employed, they will be removed when the
encoder employ ResNet-34 structure. This is because it does not have channel
expansion on residual unit. In addition, we also remove skip-connection between
output of Conv1 and output of Trans4 on ResNet-34 encoder setting for better
performance.

3.2   Pyramid Supervision
The pyramid supervision training scheme alleviate the gradient vanishing prob-
lem by introducing supervised learning over five different layers. As shown in
Fig. 2, the algorithm compute four intermediate outputs from feature maps of
four upsample ResLayer in addition to the final output, these intermediate out-
puts are called side outputs. Each side output score map is computed using a
convolution layer with 1 × 1 kernel size and stride one. Therefore, all outputs
have different spatial resolutions. The final Output of RedNet is a full resolution
score map, while the side outputs Out4, Out3, Out2, and Out1 are downsampled.
For instance, the Out1 has 1/16 the height and width of the Output. The four
side outputs and the final output are then feed into a softmax layer and cross
entropy function to build the loss function.
                                                               
                                  1 X            exp(si [gi ])
                   Loss(s, g) =         − log P                                 (1)
                                 N i              k exp(si [k])

    More concretely, the loss function of each output has the same form shown
in Eq. 1. Here, gi ∈ R denote the class index on the groundtruth semantic
map on location i. si ∈ RNc denote the score vector of the network output on
location i with Nc being the number of classes in the dataset. N denotes the
spatial resolution of the specific output. When dealing with the loss function of
Out1 to Out4, the groundtruth map g is downsampled using nearest-neighbor
interpolation. The overall cross entropy loss is thus the summation of all five
cross entropy losses over five outputs. Notice that instead of assigning equally-
weighted loss on pixels in different outputs, these overall loss configuration assign
more weight on pixels of downsampled output, e.g., Out1. In practice, we find
that this configuration provide better performance than the equally-weighted
loss configuration.
                           RedNet for indoor RGB-D Semantic Segmentation          9

4     Experiment

In this section, we evaluate the RedNet architectures with ResNet-34 and ResNet-
50 as the encoder using the SUN RGB-D indoor scene understanding benchmark
suit [34]. The SUN RGB-D dataset is currently the largest RGB-D indoor scene
semantic segmentation dataset It has 10,335 densely annotated RGB-D images
taken from 20 different scenes, at a similar scale as the PASCAL VOC RGB
dataset [10]. It also include all images data from NYU Depth v2 dataset [33],
and selected images data from Berkeley B3DO [20] and SUN3D [37] dataset.
To improve the quality of the depth map, the paper proposes a algorithm that
estimates the 3D structure of the scene from multiple frames to conduct depth
denoising and fill in the missing values. Each pixel in the RGB-D images is as-
signed a semantic label in one of the 37 classes or the ‘unknown’ class. In the
experiment evaluation, we use the default trainval-test split of the dataset that
has 5285 training/validation instances and 5050 testing instances to evaluation
our proposed RedNet architecture.
    Training Images in SUN RGB-D dataset were captured by four different
kinds of sensors with different resolutions and fields of view. In the training
step, we resize all RGB images, Depth images, and the Groundtruth seman-
tic maps into a 480 × 640 height and width spatial resolution, additionally, the
Groundtruth maps are further resized into four downsampled maps with resolu-
tion from 240 × 320 to 30 × 40 for pyramid supervision of the side output. Here,
the RGB images are applied bilinear interpolation while the Depth images and
Groundtruth maps are applied nearest-neighbor interpolation. During training,
the inputs and Groundtruths data are augmented by applying random scale and
crop and the input RGB images are further augmented by applying random
hue, brightness, and saturation adjustment. In addition, we calculate the mean
and standard deviation of the RGB and Depth images in the whole dataset to
normalize each input value.
    The two networks in the experiment, i.e., the RedNet (ResNet-34) and Red-
Net (ResNet-50), share the same training strategy and have the identical val-
ues of all hyperparameters. We use the PyTorch deep learning framework [29]
for implementation and training of the architecture1 . The encoder of the net-
work is pretrained on the ImageNet object classification dataset [23], while the
parameters on other layers are initialized by the Xavier initializer [12]. Since
the imbalance of pixels of each class presented in the dataset, we reweight the
training loss of each class in the cross-entropy function using the median fre-
quency setting proposed in [9]. That is, we weight each pixel by a factor of
αc = median prob/prob(c), where c is the groundtruth class of the pixel, prob(c)
is the pixel probability of that class, median prob is the median of all the prob-
abilities of these classes. The network is training with momentum SGD as the
optimization algorithm. The initial learning rate of all layers are set to 0.002
and will decay by a factor of 0.8 in every 100 epochs. The momentum of the
optimizer is set to 0.9, and a weight decay of 0.0004 is applied for regularization.
1
    Our source code will be avaliable at https://github.com/JindongJiang/RedNet
10     J. Jiang et al.

               Table 2. Comparison of SUN RGB-D testing results

                  Model                      Pixel Mean mIoU
                  FCN-32s [27]               68.4     41.1     29.0
                  SegNet [1]                 71.2     45.9     30.7
                  Context-CRF [26]           78.4     53.4     42.3
                  RefineNet-152 [25]         80.6     58.5     45.9
                  CFN (RefineNet-152) [24]      -        -     48.1
                  FuseNet-SF5 [15]           76.3     48.3     37.3
                  DFCN-DCRF [21]             76.6     50.6     39.3
                  RedNet(ResNet-34)          80.8    58.3     46.8
                  RedNet(ResNet-50)          81.3    60.3     47.8

           Table 3. SUN RGB-D testing results on pyramid supervision

            Model                                   Pixel Mean mIoU
            RedNet(ResNet-34) without pyramid       80.3     55.5     45.0
            RedNet(ResNet-34)                       80.8     58.3     46.8
            RedNet(ResNet-50) without pyramid       80.5     57.4     46.0
            RedNet(ResNet-50)                       81.3     60.3     47.8

The network is trained on a NVIDIA GeForce GTX 1080 GPU with a batch size
of 5, and we stop the training when the loss no longer decrease.
    Evaluation The network is evaluated on the default testing set of SUN
RGB-D dataset. Three criterias for segmentation tasks are used to measure the
performance of the network under 5050 testing instances, i.e., the pixel accuracy,
the mean accuracy and the intersection-over-union (IoU) score.
    Table 2 shows the comparison result of RedNet and other state-of-the-art
methods on SUN RGB-D testing set. As we can see in the table, the proposed
RedNet(ResNet-34) and RedNet(ResNet-50) architecture outperform most of
the exist methods. Here, the FuseNet-SF5 [15] and DFCN-DCRF [21] networks
use the same depth fusion technique in RedNet for depth incorporation. The
RefineNet-152 [25] and CFN (RefineNet-152) [24] architecture use the same
residual network in RedNet for feature extraction. Notice that, these two ar-
chitectures are both using ResNet-152 structure for feature extraction, while
RedNet performs a 47.8% accuracy using the ResNet-50 as the encoder. It also
worth notice that the RedNet(ResNet-34) network and the RedNet(ResNet-50)
network share the same decoder structure, and the comparison result shows
that the deeper structure of encoder in RedNet(ResNet-50) provides a better
performance.
    In addition, to show that the pyramid supervision training scheme is able to
effectively improve the performance of the network, a experiment is conducted
to compare the performance of the proposed RedNet architectures trained with
and without pyramid supervision. The result is shown in Table 3. It shows that
                            RedNet for indoor RGB-D Semantic Segmentation     11

             RGB images

             Side Output1

             Side Output2

             Side Output3

             Side Output4

             Final Output

             GroundTruth

                 Fig. 4. Prediction of side outputs and final output

the pyramid supervision improve the performance of the network on all three
criterias. Notice that the ResNet-34 encoder RedNet with pyramid supervision
training scheme outperform the ResNet-50 encoder RedNet without pyramid
supervision, this fully demonstrate the effectiveness of pyramid supervision. The
testing prediction of side outputs and final output can be obtained in Fig. 4.

5   Conclusion

In this work, we propose a RGB-D encoder-decoder residual network named Red-
Net for indoor RGB-D semantic segmentation. The RedNet combines the short
skip-connection in residual unit and the long skip-connection between encoder
and decoder for an accurate semantic inference. It also applies fusion structure
in the encoder to incorporate the depth information. Moreover, we present the
pyramid supervision training scheme that apply supervised learning over sev-
eral layers on the decoder to improve the performance of the encoder-decoder
network. The comparative experiment shows that the proposed RedNet architec-
ture with pyramid supervision achieves state-of-the-art result on SUN RGB-D
dataset.
12      J. Jiang et al.

References

 1. Badrinarayanan, V., Kendall, A., Cipolla, R.: Segnet: A deep convolutional
    encoder-decoder architecture for scene segmentation. IEEE Transactions on Pat-
    tern Analysis and Machine Intelligence PP(99), 1–1 (2015)
 2. Brostow, G.J., Shotton, J., Fauqueur, J., Cipolla, R.: Segmentation and recogni-
    tion using structure from motion point clouds. In: Proceedings of the European
    Conference on Computer Vision. pp. 44–57. Springer (2008)
 3. Chaurasia, A., Culurciello, E.: Linknet: Exploiting encoder representations for ef-
    ficient semantic segmentation. arXiv preprint arXiv:1707.03718 (2017)
 4. Chen, L.C., Papandreou, G., Kokkinos, I., Murphy, K., Yuille, A.L.: Deeplab: Se-
    mantic image segmentation with deep convolutional nets, atrous convolution, and
    fully connected crfs. arXiv preprint arXiv:1606.00915 (2016)
 5. Cordts, M., Omran, M., Ramos, S., Rehfeld, T., Enzweiler, M., Benenson, R.,
    Franke, U., Roth, S., Schiele, B.: The cityscapes dataset for semantic urban scene
    understanding. In: Proceedings of the IEEE Conference on Computer Vision and
    Pattern Recognition. pp. 3213–3223 (2016)
 6. Couprie, C., Farabet, C., Najman, L., LeCun, Y.: Indoor semantic segmentation
    using depth information. arXiv preprint arXiv:1301.3572 (2013)
 7. Dai, J., He, K., Sun, J.: Instance-aware semantic segmentation via multi-task net-
    work cascades. In: Proceedings of the IEEE Conference on Computer Vision and
    Pattern Recognition. pp. 3150–3158 (2016)
 8. Drozdzal, M., Vorontsov, E., Chartrand, G., Kadoury, S., Pal, C.: The importance
    of skip connections in biomedical image segmentation. In: Deep Learning and Data
    Labeling for Medical Applications, pp. 179–187. Springer (2016)
 9. Eigen, D., Fergus, R.: Predicting depth, surface normals and semantic labels with
    a common multi-scale convolutional architecture. In: Proceedings of the IEEE In-
    ternational Conference on Computer Vision. pp. 2650–2658 (2015)
10. Everingham, M., Eslami, S.A., Van Gool, L., Williams, C.K., Winn, J., Zisser-
    man, A.: The pascal visual object classes challenge: A retrospective. International
    Journal of Computer Vision 111(1), 98–136 (2015)
11. Everingham, M., Van Gool, L., Williams, C.K., Winn, J., Zisserman, A.: The pascal
    visual object classes (voc) challenge. International Journal of Computer Vision
    88(2), 303–338 (2010)
12. Glorot, X., Bengio, Y.: Understanding the difficulty of training deep feedforward
    neural networks. In: Proceedings of the International Conference on Artificial In-
    telligence and Statistics. pp. 249–256 (2010)
13. Gupta, S., Arbelaez, P., Malik, J.: Perceptual organization and recognition of in-
    door scenes from rgb-d images. In: Proceedings of the IEEE Conference on Com-
    puter Vision and Pattern Recognition. pp. 564–571. IEEE (2013)
14. Gupta, S., Girshick, R., Arbeláez, P., Malik, J.: Learning rich features from rgb-d
    images for object detection and segmentation. In: Proceedings of the European
    Conference on Computer Vision. pp. 345–360. Springer (2014)
15. Hazirbas, C., Ma, L., Domokos, C., Cremers, D.: Fusenet: Incorporating depth
    into semantic segmentation via fusion-based cnn architecture. In: Proceedings of
    the Asian Conference on Computer Vision. vol. 2 (2016)
16. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In:
    Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
    pp. 770–778 (2016)
                           RedNet for indoor RGB-D Semantic Segmentation            13

17. He, K., Zhang, X., Ren, S., Sun, J.: Identity mappings in deep residual networks.
    In: Proceedings of the European Conference on Computer Vision. pp. 630–645.
    Springer (2016)
18. Huang, H., Jiang, H., Brenner, C., Mayer, H.: Object-level segmentation of rgbd
    data. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Infor-
    mation Sciences 2(3), 73 (2014)
19. Ioffe, S., Szegedy, C.: Batch normalization: Accelerating deep network training by
    reducing internal covariate shift. arXiv preprint arXiv:1502.03167 (2015)
20. Janoch, A., Karayev, S., Jia, Y., Barron, J.T., Fritz, M., Saenko, K., Darrell, T.:
    A category-level 3d object dataset: Putting the kinect to work. In: Proceedings of
    the IEEE International Conference on Computer Vision Workshops on Consumer
    Depth Cameras for Computer Vision, pp. 1168–1174 (2011)
21. Jiang, J., Zhang, Z., Huang, Y., Zheng, L.: Incorporating depth into both cnn and
    crf for indoor semantic segmentation. arXiv preprint arXiv:1705.07383 (2017)
22. Koppula, H.S., Anand, A., Joachims, T., Saxena, A.: Semantic labeling of 3d point
    clouds for indoor scenes. In: Advances in Neural Information Processing Systems.
    pp. 244–252 (2011)
23. Krizhevsky, A., Sutskever, I., Hinton, G.E.: Imagenet classification with deep con-
    volutional neural networks. In: Proceedings of the International Conference on
    Neural Information Processing Systems. pp. 1097–1105 (2012)
24. Lin, D., Chen, G., Cohen-Or, D., Heng, P.A., Huang, H.: Cascaded feature network
    for semantic segmentation of rgb-d images. In: Proceedings of the IEEE Conference
    on Computer Vision and Pattern Recognition. pp. 1311–1319 (2017)
25. Lin, G., Milan, A., Shen, C., Reid, I.: Refinenet: Multi-path refinement networks
    for high-resolution semantic segmentation. In: Proceedings of the IEEE Conference
    on Computer Vision and Pattern Recognition (2017)
26. Lin, G., Shen, C., Hengel, A.v.d., Reid, I.: Exploring context with deep structured
    models for semantic segmentation. arXiv preprint arXiv:1603.03183 (2016)
27. Long, J., Shelhamer, E., Darrell, T.: Fully convolutional networks for semantic
    segmentation. In: Proceedings of the IEEE Conference on Computer Vision and
    Pattern Recognition. pp. 3431–3440 (2015)
28. Noh, H., Hong, S., Han, B.: Learning deconvolution network for semantic segmen-
    tation. In: Proceedings of the IEEE International Conference on Computer Vision.
    pp. 1520–1528 (2015)
29. Paszke, A., Gross, S., Chintala, S., Chanan, G., Yang, E., DeVito, Z., Lin, Z.,
    Desmaison, A., Antiga, L., Lerer, A.: Automatic differentiation in pytorch (2017)
30. Pohlen, T., Hermans, A., Mathias, M., Leibe, B.: Full-resolution residual networks
    for semantic segmentation in street scenes. arXiv preprint arXiv:1611.08323 (2017)
31. Quan, T.M., Hilderbrand, D.G., Jeong, W.K.: Fusionnet: A deep fully residual con-
    volutional neural network for image segmentation in connectomics. arXiv preprint
    arXiv:1612.05360 (2016)
32. Silberman, N., Fergus, R.: Indoor scene segmentation using a structured light sen-
    sor. In: Proceedings of IEEE International Conference on Computer Vision Work-
    shops. pp. 601–608. IEEE (2011)
33. Silberman, N., Hoiem, D., Kohli, P., Fergus, R.: Indoor segmentation and support
    inference from rgbd images. Proceedings of the European Conference on Computer
    Vision pp. 746–760 (2012)
34. Song, S., Lichtenberg, S.P., Xiao, J.: Sun rgb-d: A rgb-d scene understanding
    benchmark suite. In: Proceedings of the IEEE Conference on Computer Vision
    and Pattern Recognition. pp. 567–576 (2015)
14      J. Jiang et al.

35. Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D.,
    Vanhoucke, V., Rabinovich, A.: Going deeper with convolutions. In: Proceedings
    of the IEEE Conference on Computer Vision and Pattern Recognition. pp. 1–9
    (2015)
36. Veit, A., Wilber, M.J., Belongie, S.: Residual networks behave like ensembles of rel-
    atively shallow networks. In: Advances in Neural Information Processing Systems.
    pp. 550–558 (2016)
37. Xiao, J., Owens, A., Torralba, A.: Sun3d: A database of big spaces reconstructed
    using sfm and object labels. In: Proceedings of the IEEE International Conference
    on Computer Vision. pp. 1625–1632 (2013)
38. Yu, F., Koltun, V.: Multi-scale context aggregation by dilated convolutions. arXiv
    preprint arXiv:1511.07122 (2015)
39. Yu, F., Koltun, V., Funkhouser, T.: Dilated residual networks. In: Proceedings of
    the IEEE Conference on Computer Vision and Pattern Recognition. vol. 1 (2017)
40. Zagoruyko, S., Komodakis, N.: Wide residual networks. arXiv preprint
    arXiv:1605.07146 (2016)
