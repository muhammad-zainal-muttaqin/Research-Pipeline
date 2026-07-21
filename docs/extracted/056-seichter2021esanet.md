---
source_id: 056
bibtex_key: seichter2021esanet
title: Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis
year: 2021
domain_theme: Segmentasi RGB-D
verified_pdf: 56_ESANet.pdf
char_count: 73516
---

© 2021 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media,
                                          including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to
                                                                          servers or lists, or reuse of any copyrighted component of this work in other works.

                                               Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis
                                                  Daniel Seichter, Mona Köhler, Benjamin Lewandowski, Tim Wengefeld and Horst-Michael Gross

                                           Abstract— Analyzing scenes thoroughly is crucial for mobile

                                                                                                                        Semantic Segmentation
                                        robots acting in different environments. Semantic segmentation                                                                                 RGB Encoder         Decoder
                                        can enhance various subsequent tasks, such as (semantically
                                        assisted) person perception, (semantic) free space detection, (se-
                                                                                                                                                                                                           ESANet
                                        mantic) mapping, and (semantic) navigation. In this paper, we                                                                                  Depth Encoder       Efﬁcient RGB-D
                                        propose an efficient and robust RGB-D segmentation approach                                                       Time                                             Segmentation
arXiv:2011.06961v3 [cs.CV] 7 Apr 2021

                                        that can be optimized to a high degree using NVIDIA TensorRT
                                        and, thus, is well suited as a common initial processing step

                                                                                                                        Subsequent Scene Analysis Tasks
                                        in a complex system for scene analysis on mobile robots. We
                                        show that RGB-D segmentation is superior to processing RGB                                                         Stronger Multi-Task                                              Semantic
                                                                                                                                                                                 Free Space Detection
                                        images solely and that it can still be performed in real time                                                       Person Perception
                                                                                                                                                                                                           Floor
                                                                                                                                                                                                                            Mapping
                                        if the network architecture is carefully designed. We evaluate                                                                                                   Reﬁnement

                                        our proposed Efficient Scene Analysis Network (ESANet) on
                                        the common indoor datasets NYUv2 and SUNRGB-D and show
                                        that we reach state-of-the-art performance while enabling faster
                                        inference. Furthermore, our evaluation on the outdoor dataset
                                                                                                                                                                 Single Frame                           Multiple Frames
                                        Cityscapes shows that our approach is suitable for other areas
                                        of application as well. Finally, instead of presenting benchmark
                                        results only, we also show qualitative results in one of our indoor            Fig. 1: Our proposed efficient RGB-D segmentation approach
                                        application scenarios.                                                         can serve as a common preprocessing step for subsequent
                                                                                                                       tasks such as person perception, free space detection to avoid
                                                                 I. I NTRODUCTION                                      even small obstacles below the laser, or semantic mapping.
                                           Semantic scene perception and understanding is essen-
                                        tial for mobile robots acting in various environments. In
                                        our research projects, covering public environments from                       small obstacles below the laser. For mapping [8], we can
                                        supermarkets [1], [2] to hospitals [3], [4] and domestic                       include semantics and ignore image regions segmented as
                                        applications [5], [6], our robots need to perform several tasks                dynamic classes such as person.
                                        in parallel such as obstacle avoidance, semantic mapping,                         Our segmentation approach relies on both RGB and depth
                                        navigation to semantic entities, and person perception. Most                   images as input. Especially in indoor environments, cluttered
                                        of the tasks require to be handled in real time given limited                  scenes may impede semantic segmentation. Incorporating
                                        computing and battery capabilities. Hence, an efficient and                    depth images can alleviate this effect by providing comple-
                                        shared initial processing step can facilitate subsequent tasks.                mentary geometric information, as shown in [9], [10], [11].
                                        Semantic segmentation is well suited for such an initial step,                 In contrast to processing RGB images solely, this design
                                        as it provides precise pixel-wise information that can be used                 decision comes with some additional computational cost.
                                        for numerous subsequent tasks.                                                 However, in this paper, we show that two carefully designed
                                           In this paper, we propose an efficient and robust encoder-                  shallow encoder branches (one for RGB and one for depth
                                        decoder-based semantic segmentation approach that can be                       data) can achieve better segmentation performance while still
                                        embedded in complex systems for semantic scene analysis                        enabling faster inference (application of network) than a sin-
                                        such as shown in Fig. 1. The segmentation output enriches                      gle deep encoder branch for RGB images solely. Moreover,
                                        the robot’s visual perception and facilitates subsequent pro-                  our Efficient Scene Analysis Network (ESANet) enables
                                        cessing steps by providing individual semantic masks. For                      much faster inference than most other RGB-D segmentation
                                        our person perception [7], computations can be restricted to                   methods, while performing on par or even better as shown
                                        image regions segmented as person, instead of processing                       by our experiments.
                                        the entire image. Furthermore, the floor class indicates free                     We evaluate our ESANet on the commonly used indoor
                                        space that can be used for inpainting invalid depth pixels as                  datasets NYUv2 [12] and SUNRGB-D [13] and further
                                        well as serves as additional information for avoiding even                     present qualitative results in our indoor application. Instead
                                                                                                                       of only focusing on mean intersection over union (mIoU)
                                               Authors are with Neuroinformatics and          Cognitive Robotics
                                        Lab,    Technische Universität Ilmenau, 98693        Ilmenau, Germany.        as evaluation metric for benchmarking, we also strive for
                                        daniel.seichter@tu-ilmenau.de                                                  fast inference on embedded hardware. However, rather than
                                              This work has received funding from the German Federal Ministry of       reporting the inference time on high-end GPUs, we mea-
                                        Education and Research (BMBF) to the project MORPHIA (grant agreement
                                        no. 16SV8426) and from the Carl Zeiss Foundation to the project E4SM           sure inference time on our robot’s NVIDIA Jetson AGX
                                        (grant agreement no. P2017-01-005).                                            Xavier. We designed our network architecture such that it
can be executed as a single optimized graph using NVIDIA           the last fusion at the end of both encoders. Using only one
TensorRT. Moreover, by evaluating on the outdoor dataset           decoder for the combined features reduces the computational
Cityscapes [14], we show that our approach can also be             effort. FuseNet [9] and RedNet [10] fuse the depth features
applied to other areas of application.                             into the RGB encoder, which follows the intuition that the
The main contributions of this paper are                           semantically richer RGB features can be further enhanced
 • an efficient RGB-D segmentation approach, which can             using complementary depth information. SA-Gate [22] com-
   serve as initial processing step to facilitate subsequent       bines RGB and depth features and fuses the recalibrated
   scene analysis tasks and is characterized by:                   features back into both encoders. In order to make the
   – a carefully designed architecture that can be optimized       two encoders independent of each other, ACNet [11] uses
      to a high degree using NVIDIA TensorRT and, thus,            an additional, virtual, third encoder that obtains modality-
      enables fast inference                                       specific features from the two encoders and processes the
   – an efficient ResNet-based encoder that utilizes a modi-       combined features. Instead of fusing in the encoder, the
      fied basic block that is computationally less expensive      modality-specific features can also be used to refine the
      while achieving higher accuracy                              features in the common decoder via skip connections as in
   – a decoder that utilizes a novel learned upsampling            RDFNet [23], SSMA [24] and MMAF-Net [25].
                                                                      However, none of the aforementioned methods focus on
 • a detailed ablation study to the fundamental parts of our
                                                                   efficient RGB-D segmentation for embedded hardware. Us-
   approach and their impact on segmentation performance
                                                                   ing deep encoders such as ResNets with 50, 101 or even 152
   and inference time
                                                                   layers results in high inference times and, therefore, makes
 • qualitative results in a complex system for robotic scene
                                                                   them inappropriate for deploying to mobile robots.
   analysis proving the applicability and robustness.
Our code as well as the trained networks are publicly              B. Efficient Semantic Segmentation
available at: https://github.com/TUI-NICR/ESANet
                                                                      In contrast to RGB-D segmentation, recent RGB ap-
                    II. R ELATED W ORK                             proaches [26], [27], [28], [29], [30], [31], [32] also address
   Common network architectures for semantic segmentation          reducing computational complexity to enable real-time seg-
follow an encoder-decoder design. The encoder extracts             mentation. Most efficient segmentation approaches propose
semantically rich features from the input and performs             specifically tailored network architectures, which reduce both
downsampling to reduce computational effort. The decoder           the number of operations and parameters to enable faster
restores the input resolution and, finally, assigns a semantic     inference while still retaining good segmentation perfor-
class to each input pixel.                                         mance. Approaches, such as ERFNet [26], LEDNet [27], or
                                                                   DABNet [28] introduce efficient encoder blocks by replacing
A. RGB-D Semantic Segmentation                                     expensive 3×3 convolutions with more light-weight variants
   Depth images provide complementary geometric informa-           such as factorized, grouped, or depth-wise separable con-
tion to RGB images and, thus, improve segmentation [9],            volutions. Nevertheless, although requiring more operations
[10]. However, incorporating depth information into RGB            and memory, SwiftNet [30] and BiSeNet [31] are still faster
segmentation architectures is challenging as depth introduces      than many other methods, while achieving higher segmen-
deviating statistics and characteristics from another modality.    tation performance by simply using a pretrained ResNet18
   In [15], depth information is used to project the RGB           as encoder. This can be deduced to utilizing early and
images into a 3D space. However, processing the resulting          high downsampling in the encoder, a light-weight decoder,
3D data, leads to significantly higher computational complex-      and using standard 3×3 convolutions, which are currently
ity. [16], [17], [18], [19], [20] design specifically tailored     implemented more efficiently than grouped or depth-wise
convolutions, taking into account depth information. Nev-          convolutions and have large representational power.
ertheless, these modified convolutions often lack optimized           Following SwiftNet and BiSeNet, our approach also uses
implementations and, thus, are slow and not applicable for         a ResNet-based encoder. However, in order to further reduce
real-time segmentation on embedded hardware.                       inference time, we exchange the basic block in all ResNet
   The majority of approaches for RGB-D segmentation [9],          layers with a more efficient block, based on factorized
[21], [10], [11], [22], [23], [24], [25] simply use two            convolutions.
branches, one for RGB and one for depth data and fuse the
feature representations later in the network. This way, each                III. E FFICIENT RGB-D S EGMENTATION
branch can focus on extracting modality-specific features,            The architecture of our Efficient Scene Analysis Net-
such as color and texture from RGB images and geometric,           work (ESANet) for RGB-D semantic segmentation is de-
illumination-independent features from depth images. Fusing        picted in Fig. 2 (top). It is inspired by the RGB segmentation
these modality-specific features leads to stronger feature         approach SwiftNet [30], i.e., a shallow encoder with a
representations. Instead of fusing only low-level or high-         pretrained ResNet18 backbone and large downsampling, a
level features, [9] shows that the segmentation performance        context module similar to the one in PSPNet [33], a shallow
increases if the features are fused at multiple stages. Typi-      decoder with skip connections from the encoder, and final
cally, the features are fused once at each resolution stage with   upsampling by a factor of 4. However, SwiftNet does not
                                                                                                                                                                                                                                                                                                           *: Number of channels for ResNet18
                                                                                                                                                                                                                                                                                                           and ResNet34 (w/ & w/o NBt1D).

                               BN, ReLU
                                                                                                                                                                                                                                                                                                           For ResNet50: ×4

                                                                                                                                                                                 RGB-D Fusion
                                                        RGB-D Fusion

                                                                                                            RGB-D Fusion

                                                                                                                                              RGB-D Fusion
                                                                                                                                     ResNet
                                                                                                                                     Layer2
                                                                                 ResNet

                                                                                                                                                              ResNet
                                                                                 Layer1

                                                                                                                                                                                                 ResNet
                                                                                                                                                              Layer3

                                                                                                                                                                                                 Layer4
                                                                                                                                                                                                                                                                      BN, ReLU    BN, ReLU      BN, ReLU

                                                                                                                                                                                                                                             Context Module
                                                                                                                                                                                                                    RGB-D Fusion

                                                                                                                                                                                                                                                                            Decoder

                                                                                                                                                                                                                                                                                        Decoder
                                                                                                                                                                                                                                                                            Module

                                                                                                                                                                                                                                                                                        Module
                                                                                                                                                                                                                                                                Mod
                                                                                                                                                                                                                                                                Dec
                               BN, ReLU

                                                                                                                                     ResNet

                                                                                                                                                              ResNet
                                                                                                                                     Layer2

                                                                                                                                                              Layer3

                                                                                                                                                                                                 ResNet
                                                                                                                                                                                                 Layer4
                                                                                 ResNet
                                                                                 Layer1
                                                                                                                                                                                                    Encoder                                                                                                       Decoder

                                                                                                                                                                                                                                   Learned Up. ×2
                             Depth                                               RGB

                                                                                                                                                               ...
                                                                                                                                                             b branches           Global                                                                                                     BN, Relu

                                                                                                                                                                                                                                                                                                           Non-Bottleneck-1D (NBt1D)
                    Global                                              Global                                                                                                   AvgPool                                                                                              NBt1D                                                       ReLU
                                                                                   Squeeze-and-Excitation
                               Squeeze-and-Excitation

                   AvgPool                                             AvgPool

                                                                                                                                                                                                                                                                                      NBt1D                                                       BN, ReLU
                                                                                                                                                 BN, ReLU                                       BN, ReLU

                                                                                                                                                                subglobal
                 ReLU                                              ReLU

                                                                                                                                                                                                           global

                                                                                                                                                                                                                                   Decoder Module
                                                                                                                             local

                                                                                                                                                                                                                                                                                      NBt1D
                                                                                                            Context Module

                                                                                                                                                                                                                                                                                                                                                  ReLU
 RGB-D Fusion

                Sigmoid                                    Sigmoid
                                                                                                                                                                                                                                                                                                                                                  BN

                                                                                                                                                                                                                                                              Multi-Scale
                                                                                                                                                                            BN, ReLU                                                                          Supervision                                                                         ReLU

 Legend: kw ×kh , C : Convolution with kernel size kw ×kh and C output channels, S2: Stride 2, BN: Batch Normalization, Up.: Upsampling, DW: Depthwise,                                                                                                                                                                                : Concatenation

 Fig. 2: Overview of our proposed ESANet for efficient RGB-D segmentation (top) and specific network parts (bottom).

incorporate depth information at all. Therefore, our ESANet                                                                                                                                       so-called Non-Bottleneck-1D-Block (NBt1D) is depicted in
uses an additional encoder for depth data. This depth encoder                                                                                                                                     Fig. 2 (violet) and was initially proposed in ERFNet [26] for
extracts complementary geometric information that is fused                                                                                                                                        another network architecture. In our experiments, we show
into the RGB encoder at several stages using an attention                                                                                                                                         that this block can also be used in ResNet and simultaneously
mechanism. Furthermore, both encoders use a revised archi-                                                                                                                                        reduces inference time and increases segmentation perfor-
tecture enabling faster inference. The decoder is comprised                                                                                                                                       mance.
of multiple modules, each is upsampling the resulting feature
maps by a factor of 2 and is refining the features using                                                                                                                                          B. RGB-D Fusion
convolutions as well as by incorporating encoder features.                                                                                                                                           At each of the five resolution stages in the encoders (see
Finally, the decoder maps the features to the classes and                                                                                                                                         Fig. 2), depth features are fused into the RGB encoder. The
rescales the class mapping to the input resolution.                                                                                                                                               features from both modalities are first reweighted with a
   Our entire network features simple components imple-                                                                                                                                           Squeeze and Excitation (SE) module [38] and then summed
mented in PyTorch [34]. We do not use complex structures                                                                                                                                          element-wisely, as shown in Fig. 2 (light green). Using this
or specifically tailored operations as these are often incom-                                                                                                                                     channel attention mechanism, the model can learn which fea-
patible for converting to ONNX [35] or NVIDIA TensorRT                                                                                                                                            tures of which modality to focus on and which to suppress,
and, thus, result in slower inference time.                                                                                                                                                       depending on the given input. In our experiments, we show
   In the following, we explain each part of our network                                                                                                                                          that this fusion mechanism notably improves segmentation.
design in detail as well as its motivation. Fig. 2 (bottom)
depicts the exact structure of our network modules.                                                                                                                                               C. Context Module
                                                                                                                                                                                                     Due to the limited receptive field of ResNet [33], we
A. Encoder                                                                                                                                                                                        additionally incorporate context information by aggregating
   The RGB and depth encoder both use a ResNet archi-                                                                                                                                             features at different scales using several branches in a context
tecture [36] as backbone. For efficiency reasons, we do not                                                                                                                                       module similar to the Pyramid Pooling Module in PSP-
replace strided convolutions by dilated convolutions as in                                                                                                                                        Net [33] (see Fig. 2 orange). Since NVIDIA TensorRT only
PSPNet [33] or DeepLabv3 [37]. Thus, the resulting feature                                                                                                                                        supports pooling with fixed sizes, we carefully designed the
maps at the end of the encoder are 32 times smaller than the                                                                                                                                      context module such that the pooling sizes are always a factor
input image. For a trade-off between speed and accuracy,                                                                                                                                          of the input resolution of the context module and no adaptive
we use ResNet34 but also show results for ResNet18 and                                                                                                                                            pooling is required. Note that, depending on the image
ResNet50. We replace the basic block in each layer of                                                                                                                                             resolution of the respective dataset, the number of existing
ResNet18 and ResNet34 with a spatially factorized version.                                                                                                                                        factors and, thus, the branches b and pooling sizes pbw ×pbh
More precisely, each 3×3 convolution is replaced by a                                                                                                                                             differ. Our experiments show that this additional context
3×1 and a 1×3 convolution with a ReLU in-between. The                                                                                                                                             module improves segmentation.
D. Decoder                                                                                           IV. E XPERIMENTS
                                                                                   We evaluate our approach on two commonly used RGB-D
   As shown in Fig 2, our decoder is comprised of three                         indoor datasets, namely SUNRGB-D [13] and NYUv2 [12]
decoder modules (depicted in red in Fig 2). Our decoder                         and present an ablation study to essential parts of our
module extends the one of SwiftNet [30], which is comprised                     network. In order to demonstrate that our approach is suitable
of a 3×3 convolution with a fixed number of 128 channels                        for other areas of application as well, we also show results
and a subsequent bilinear upsampling. However, our exper-                       on the Cityscapes [14] dataset, the most widely used outdoor
iments show that for indoor RGB-D segmentation a more                           dataset for semantic segmentation. Finally, instead of report-
complex decoder is required. Therefore, we use 512 channels                     ing benchmark results only, we present qualitative results
in the first decoder module and decrease the number of                          when using our approach in a robotic indoor application.
channels in each 3×3 convolution as the resolution increases.
Moreover, we incorporate three additional Non-Bottleneck-                       A. Implementation Details & Datasets
1D-blocks to further increase segmentation performance.                            We trained our networks using PyTorch [34] for 500
   Finally, we upsample the feature maps by a factor of 2.                      epochs with batches of size 8. For optimization, we used
We do not use transposed convolutions for upsampling                            both SGD with momentum of 0.9 and Adam [40] with
as they are computationally expensive and often introduce                       learning rates of {0.00125, 0.0025, 0.005, 0.01, 0.02, 0.04}
undesired gridding artifacts to the final segmentation, as                      and {0.0001, 0.0004}, respectively, and a small weight decay
shown in Fig. 3 (right). Moreover, instead of using bilin-                      of 0.0001. We adapted the learning rate using PyTorch’s one-
ear interpolation, we propose a novel light-weight learned                      cycle learning rate scheduler. To further increase the number
upsampling method (see Fig. 2 dark green), which achieves                       of training samples, we augmented the images using random
better segmentation results: In particular, we first use nearest                scaling, cropping, and flipping. For RGB images, we also
neighbor upsampling to enlarge the resolution. Afterwards,                      applied slight color jittering in HSV space.
a 3×3 depthwise convolution is applied to combine adjacent                         The best models were chosen based on the mean inter-
features. We initialize the kernels such that the whole learned                 section over union (mIoU). We used bilinear upsampling to
upsampling initially mimics bilinear interpolation. However,                    rescale the resulting class mapping to the size of the ground
our network is able to adapt the weights during training and,                   truth segmentation before computing the argmax for the final
thus, can learn how to combine adjacent features in a more                      segmentation mask.
useful manner, which improves segmentation performance.                            NYUv2 & SUNRGB-D: NYUv2 contains 1,449 indoor
                                                                                RGB-D images, of which 795 are used for training and
   Although being upscaled, the resulting feature maps still
                                                                                654 for testing. We used the common 40-class label setting.
lack fine-grained details that were lost during downsampling
                                                                                SUNRGB-D has 37 classes and consists of 10,335 indoor
in the encoders. Therefore, we design skip connections from
                                                                                RGB-D images, including all images of NYUv2. There are
encoder to decoder stages of the same resolution. To be
                                                                                5,285 training and 5,050 testing images. Our ablation study
precise, we take the fused RGB-D encoder feature maps,
                                                                                is based on NYUv2 as it is smaller and, thus, leads to
project them with a 1×1 convolution to the same number of
                                                                                faster trainings. However, according to [41], training on a
channels used in the decoder, and add them to the decoder
                                                                                subset is sufficient for a reliable model selection. For both
feature maps. Incorporating these skip connections results in
                                                                                datasets, we used a network input resolution of 640×480
more detailed semantic segmentations.
                                                                                and applied median frequency class balancing [42]. As the
   Similar to [30], [39], we only process feature maps in the                   input to the context module has a resolution of 20×15 due to
decoder until they are 4× smaller than the input images and                     the downsampling of 32, we used b = 2 branches, one with
use a 3×3 convolution to map the features to the classes of                     global average pooling and one with a pooling size of 4×3.
the respective dataset. Two final learned upsampling modules                       Cityscapes: This dataset contains 5,000 images with fine-
restore the resolution of the input image.                                      grained annotation for 19 classes. The images have a high
   Instead of calculating the training loss only at the final                   resolution of 2048×1024. There are 2,975 images for train-
output scale, we add supervision to each decoder module.                        ing, 500 for validation, and 1,525 for testing. Cityscapes also
At each scale, a 1×1 convolution computes a segmentation                        provides 20k coarsely annotated images, which we did not
of a smaller scale, which is supervised by the down-scaled                      use for training. We computed corresponding depth images
ground truth segmentation.                                                      from the disparity images. Since we set the network input
                                                                   picture       window
                                      door
                                                         wall

                                     table

                                                 chair                                    counter
                                                          table?

                                         floor                                            cabinet                                           bed

       RGB image                   Ground Truth                        Learned Up. (ours)           Bilinear Up.      Transp. Conv. (ACNet [11])
     Fig. 3: Qualitative comparison of upsampling methods on NYUv2 test set (same colors as in Fig. 1 and Fig. 6).
                                            ResNet50                                                                                51
                                                              ResNet34 NBt1D                                                                                              selected network
                                50
                                                                 selected network                                                                      learned
 Mean intersection over union

                                                                                                     Mean intersection over union
                                             ResNet34                                                                                                            3
                                                                              ResNet18 NBt1D                                        50
                                48                                                                                                                 4
                                                                                                                                                                              2
                                                                          ResNet18                                                                                                                 bilinear
                                                        Fig. 5
                                46                                                                                                            reversed                                   1
                                                                                                                                    49        encoder                                              nearest
                                            RGB-D
                                                                                                                                              layout
                                44          RGB                                                                                                                  CM
                                                                                                                                                                                         SE
                                            Depth
                                                                                                                                    48                                       Skip                      0
                                42          ResNet18
                                            ResNet18 NBt1D
                                                                                                                                                                                                    SE, Skip
                                40          ResNet34                                                                                47                                    CM, Skip       CM, SE                     SwiftNet
                                                                                                                                                                                                                    similar
                                            ResNet34 NBt1D
                                38          ResNet50                                                                                                                                              CM, SE, Skip

                                     20         25           30         35           40        45                                        28            29            30           31         32     33         34         35
                                          FPS (NVIDIA Jetson AGX Xavier, TensorRT 7.1, Float16)                                                 FPS (NVIDIA Jetson AGX Xavier, TensorRT 7.1, Float16)

Fig. 4: Comparison of RGB-D to RGB and depth networks                                               Fig. 5: Ablation Study on NYUv2 test. Each color indicates
(single encoder) and different backbones on NYUv2 test set.                                         modifying one aspect: purple: number of NBt1D blocks in
                                                                                                    decoder module, dark green: upsampling method, and gray:
resolution to 1024×512, the input to our context module has                                         usage of specific network parts with CM : no context module,
a resolution of 32×16, which allows b = 4 branches in the                                           Skip: no encoder-decoder skip connections, and SE : no
context module, one with global average pooling and the                                             Squeeze-and-Excitation before fusing RGB and depth.
others with pooling sizes of 16×8, 8×4, and 4×2.
   For further details and other hyperparameters, we refer to
our implementation available on GitHub.                                                             C. Ablation Study on NYUv2
                                                                                                       Fig. 5 shows the ablation study for fundamental parts of
B. Results on NYUv2 & SUNRGB-D
                                                                                                    our network architecture and justifies our design choices.
   Fig. 4 compares our RGB-D approach on NYUv2 to                                                   Furthermore, it indicates the impact of each part when it
single-modality baselines for RGB and depth (single en-                                             is necessary to adapt our selected network to deviating real-
coder) as well as evaluates different encoder backbones.                                            time requirements.
As expected, neither processing depth data nor RGB data                                                As shown in purple, a shallow decoder similar to Swift-
alone reach the segmentation performance of our proposed                                            Net [30] is not as good as more complex decoders. Therefore,
RGB-D network. Remarkably, the shallow ResNet18-based                                               we gradually increased the number of additional NBt1D
RGB-D network performs better than the much deeper                                                  blocks in the decoder module. Apparently, a fixed number of
ResNet50-based RGB network while still being faster. More-                                          three blocks in each decoder module performs better than a
over, replacing ResNet’s basic block with Non-Bottleneck-                                           different number or a reversed layout of the encoder’s design.
1D (NBt1D) block can further improve both segmentation                                                 In dark green, different upsampling methods in the de-
and inference time. Note that ResNet50 incorporates bottle-                                         coder are displayed. Although increasing inference time, the
neck blocks, which cannot be replaced the same way.                                                 learned upsampling improves mIoU by 0.9. Moreover, as
   Tab. I lists the results of our RGB-D approach for both                                          shown in Fig. 3, the obtained segmentation contains more
indoor datasets. For the larger SUNRGB-D dataset, a similar                                         fine-grained details compared to using bilinear interpolation.
trend can be observed. Compared to the state of the art, our                                        It further prevents gridding artifacts introduced by transposed
smaller ESANet achieves similar segmentation results as the                                         convolutions as used in ACNet [11] or RedNet [10].
often much deeper networks. Besides focusing on segmen-                                                As shown in gray in Fig. 5, a context module, encoder-
tation performance alone, we also strive for low inference                                          decoder skip connections, as well as reweighting modality-
time on the embedded hardware of our robots. Therefore,                                             specific features with Squeeze-and-Excitation before fusion,
we measured the inference time for all available approaches                                         independently improve segmentation performance. Incorpo-
on a NVIDIA Jetson AGX Xavier using NVIDIA TensorRT.                                                rating all three network parts leads to the best result.
For our carefully designed ESANet, NVIDIA TensorRT
enables up to 5× faster inference compared to PyTorch. As                                           D. Results on Cityscapes
shown in Tab. I (last column), our approach enables much                                               To demonstrate that our approach is applicable to other
faster inference while performing on par or even better than                                        areas such as outdoor environments as well, in Tab. II, we
other approaches. For our application, we choose ESANet                                             further present an evaluation on the Cityscapes dataset.
with ResNet34 backbone and Non-Bottleneck-1D (NBt1D)                                                   We first focus on the smaller resolution of 1024×512 as
block (printed in bold in Tab. I) as it offers the best trade-                                      it is commonly used for efficient segmentation. Moreover,
off between inference time and performance. The last row                                            since most approaches rely on RGB as input solely, we start
in Tab. I further indicates that additional pretraining on                                          by comparing a single-modality RGB version of our ap-
synthetic data, such as SceneNet [43], should be preferred to                                       proach. Efficient approaches with custom architectures such
deeper backbones, especially if the target dataset is small.                                        as ERFNet [26], LEDNet [27], and ESPNetv2 [32] are quite
                                                SUN-                                            1024×512              2048×1024
  Method                Backbone       NYUv2             FPS
                                               RGB-D                      Method              Val Test FPS         Val Test FPS
  FuseNet [9]           2× VGG16       -       37.29     †                ERFNet [26]          -    69.7    49.9     -       -         -
                                                                          LEDNet [27]          -   70.6*    38.5     -       -         -
  RedNet [10]           2× R34         -       46.8     26.0              ESPNetv2 [32]       66.4 66.2     47.4     -       -         -
  SSMA [24]             2× mod. R50    -       44.43    12.4              SwiftNet [30]       70.2   -      64.5    75.4    75.5     20.8

                                                                  RGB
  MMAF-Net [25]         2× R50         -       45.5     N/A               BiSeNet [31]         -     -       -      74.8    74.7     20.0
  RedNet [10]           2× R50         -       47.8     22.1              PSPNet [33]          -     -       -       -     81.2*      1.8
  RDFNet [23]           2× R50         47.7*   -         7.2              DeepLabv3 [37]       -     -       -      79.3   81.3*     0.9
  ACNet [11]            3× R50         48.3    48.1     16.5              ESANet-R18-NBt1D    71.48   -     37.2   77.95     -       9.8
  SA-Gate [22]          2× R50         50.4    49.4*    11.9              ESANet-R34-NBt1D    72.70 72.87   32.3   78.47   77.56     8.3
  SGNet [19]            R101           49.0    47.1    N/A O              ESANet-R50          73.88   -     24.9   79.23     -       6.5
  Idempotent [21]       2× R101        49.9    47.6    N/A O
                                                                          SSMA [24]             -    -       -     82.19* 82.31*     2.2
  2.5D Conv [16]        R101           48.5    48.2    N/A O
                                                                          SA-Gate [22]          -    -       -      81.7   82.8      2.1

                                                                  RGB-D
  MMAF-Net [25]         2× R152        44.8    47.0    N/A O              LDFNet [44]         68.48 71.3    25.3      -      -        -
  RDFNet [23]           2× R152        50.1*   47.7*    5.8               ESANet-R18-NBt1D    74.65   -     28.9   79.25     -       7.6
  ESANet-R18            2× R18         47.32   46.24    34.7              ESANet-R34-NBt1D    75.22 75.65   23.4   80.09   78.42     6.2
  ESANet-R18-NBt1D      2× R18 NBt1D   48.17   46.85    36.3              ESANet-R50          75.66   -     16.9   79.97     -       4.0
  ESANet-R34            2× R34         48.81   47.08    27.5
  ESANet-R34-NBt1D      2× R34 NBt1D   50.30   48.17    29.7      TABLE II: Mean intersection over union of our ESANet on
  ESANet-R50            2× R50         50.53   48.31    22.6
                                                                  Cityscapes for both common input resolutions compared to
  ESANet (pre. SceneNet) 2× R34 NBt1D 51.58    48.04    29.7      state-of-the-art methods. FPS is reported for NVIDIA Jetson
TABLE I: Mean intersection over union of our ESANet com-          AGX Xavier (Jetpack 4.4, TensorRT 7.1, Float16). Legend:
pared to state-of-the-art methods on NYUv2 and SUNRGB-            : test server result, *: trained with additional coarse data.
D test set ordered by SUNRGB-D performance and backbone
complexity. FPS is reported for NVIDIA Jetson AGX Xavier          accomplish the complex system for semantic scene analysis
(Jetpack 4.4, TensorRT 7.1, Float16). Legend: R: ResNet,          shown in Fig. 1. The obtained segmentation masks enrich the
*: additional test-time augmentation, i.e., flipping or multi-    robot’s visual perception enabling stronger person perception
scale (not timed), N/A: no implementation available, †: in-       and robust semantic mapping including a refined floor rep-
cludes operations, which are not supported by TensorRT, and       resentation which indicates free space. Fig. 6 provides an
O: expected to be slower due to complex backbone.                 insight into the entire system. For further qualitative results
                                                                  and a comparison to non-semantic scene perception, we refer
fast but also perform notably worse than our ESANet. Com-         to the attached video or our repository on GitHub.
pared to ERFNet, LEDNet, and ESPNetv2, SwiftNet [30]
is both faster and achieves higher mIoU. Nevertheless, with                                  V. C ONCLUSION
an input resolution of 1024×512, our ESANet-R34-NBt1D                In this paper, we have presented an efficient RGB-D
still exceed 30 FPS while outperforming all other efficient       segmentation approach, called ESANet, which is charac-
approaches by at least 2.2 mIoU. Incorporating depth further      terized by two enhanced ResNet-based encoders utilizing
increases segmentation performance. However, the perfor-          the Non-Bottleneck-1D block, an attention-based fusion for
mance gain is not as high as for the indoor dataset NYUv2.        incorporating depth information, and a decoder utilizing a
We assume that this can be deduced to the fact that the           novel learned upsampling. On the indoor datasets NYUv2
disparity images of Cityscapes are not as precise as the          and SUNRGB-D, our ESANet performs on par or even
indoor depth images of NYUv2 and SUNRGB-D. Compared               better while enabling much faster inference compared to
to the RGB-D approach LDFNet [44] with similar inference          other state-of-the-art methods. Thus, it is well suited for
time, we achieve notably higher mIoU.                             embedding in a complex system for scene analysis on mobile
   For completeness, we also evaluated our networks on the        robots given limited hardware.
full resolution of 2048×1024. Compared to other methods,
our ESANet lies in between mobile (SwiftNet, BiSeNet) and                                                                  Wall
                                                                                                                           Floor
non-mobile approaches for both mIoU and inference time.
                                                                                                                           Ceiling
   However, compared to SwiftNet (RGB, 2048×1024), our                                                                     Lamp
ESANet-R34-NBt1D achieves similar segmentation perfor-                                                                     Chair
mance and slightly faster inference while processing RGB-D                                                                 Table
inputs with the smaller input resolution of 1024×512.                                                                      Sofa
                                                                                                                           Picture
E. Application on our Robots                                                                                               Box
                                                                                                                           TV
   Instead of evaluating on benchmark datasets only, we                                                                    Bag
further present qualitative results with a Kinect2 sensor [45],                                                            Pillow
[46] in one of our indoor applications. We deployed our
proposed ESANet-R34-NBt1D to our robot in order to                    Fig. 6: Application in our robotic scene analysis system.
                             R EFERENCES                                        [24] A. Valada, et al., “Self-supervised model adaptation for multimodal
                                                                                     semantic segmentation,” Int. Journal of Computer Vision (IJCV), 2019.
 [1] H.-M. Gross, et al., “TOOMAS: Interactie shopping guide robots in          [25] F. Fooladgar and S. Kasaei, “Multi-Modal Attention-based Fusion
     everyday use – final implementation and experiences from long-term              Model for Semantic Segmentation of RGB-Depth Images,” arXiv
     field trials,” in IEEE/RSJ Int. Conf. on Intelligent Robots and Systems         preprint arXiv:1912.11691, pp. 1–12, 2019.
     (IROS). IEEE, 2009, pp. 2005–2012.                                         [26] E. Romera, et al., “ERFNet: Efficient Residual Factorized ConvNet for
 [2] B. Lewandowski, et al., “Socially compliant human-robot interaction             Real-Time Semantic Segmentation,” IEEE Transactions on Intelligent
     for autonomous scanning tasks in supermarket environments,” in IEEE             Transportation Systems (ITS), pp. 263–272, 2018.
     Int. Symp. on Robot and Human Interactive Communication (RO-               [27] Y. Wang, et al., “LEDnet: A Lightweight Encoder-Decoder Network
     MAN). IEEE, 2020, pp. 363–370.                                                  for Real-Time Semantic Segmentation,” in IEEE Int. Conference on
 [3] H.-M. Gross, et al., “Mobile robot companion for walking training               Image Processing (ICIP), 2019, pp. 1860–1864.
     of stroke patients in clinical post-stroke rehabilitation,” in IEEE Int.   [28] G. Li, et al., “DABNet: Depth-wise Asymmetric Bottleneck for Real-
     Conf. on Robotics and Automation (ICRA), 2017, pp. 1028–1035.                   time Semantic Segmentation,” British Machine Vision Conference
 [4] T. Q. Trinh, et al., “Autonomous mobile gait training robot for                 (BMVC), 2019.
     orthopedic rehabilitation in a clinical environment*,” in IEEE Int.        [29] S.-Y. Lo, et al., “Efficient dense modules of asymmetric convolution
     Conf. on Robot and Human Interactive Communication (RO-MAN),                    for real-time semantic segmentation,” in ACM Int. Conf. on Multimedia
     2020, pp. 580–587.                                                              in Asia, 2019, pp. 1–6.
 [5] H.-M. Gross, et al., “Robot companion for domestic health assistance:      [30] M. Oršić, et al., “In Defense of Pre-trained ImageNet Architectures
     Implementation, test and case study under everyday conditions in                for Real-time Semantic Segmentation of Road-driving Images,” IEEE
     private apartments,” in IEEE/RSJ Int. Conf. on Intelligent Robots and           Conf. on Computer Vision and Pattern Recognition (CVPR), pp.
     Systems (IROS). IEEE, 2015, pp. 5992–5999.                                      12 607–12 616, 2019.
 [6] H. M. Gross, et al., “Living with a mobile companion robot in your         [31] C. Yu, et al., “BiSeNet: Bilateral segmentation network for real-time
     own apartment - final implementation and results of a 20-weeks field            semantic segmentation,” in Europ. Conf. on Computer Vision (ECCV),
     study with 20 seniors,” in IEEE Int. Conf. on Robotics and Automation           2018, pp. 325–341.
     (ICRA), Montreal, Canada. IEEE, 2019, pp. 2253–2259.                       [32] S. Mehta, et al., “ESPNetv2: A Light-weight, Power Efficient, and
 [7] D. Seichter, et al., “Multi-task deep learning for depth-based person           General Purpose Convolutional Neural Network,” in IEEE Conf. on
     perception in mobile robotics,” in IEEE/RSJ Int. Conf. on Intelligent           Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9190–
     Robots and Systems (IROS). IEEE, 2020, pp. 10 497–10 504.                       9200.
 [8] E. Einhorn and H.-M. Gross, “Generic 2D/3D SLAM with NDT maps              [33] H. Zhao, et al., “Pyramid scene parsing network,” in IEEE Conf. on
     for lifelong application,” in Europ. Conf. on Mobile Robots (ECMR),             Computer Vision and Pattern Recognition (CVPR), 2017, pp. 2881–
     2013.                                                                           2890.
 [9] C. Hazirbas, et al., “FuseNet: Incorporating Depth into Semantic Seg-      [34] A. Paszke, et al., “Pytorch: An imperative style, high-performance
     mentation via Fusion-based CNN Architecture,” in Asian Conference               deep learning library,” in Advances in Neural Information Processing
     on Computer Vision (ACCV), 2016, pp. 213–228.                                   Systems (NIPS). Curran Associates, Inc., 2019, pp. 8024–8035.
[10] J. Jiang, et al., “RedNet: Residual Encoder-Decoder Network                [35] J. Bai, et al., “Onnx: Open neural network exchange,” https://github.
     for indoor RGB-D Semantic Segmentation,” arXiv preprint                         com/onnx/onnx, 2019.
     arXiv:1806.01054, 2018.                                                    [36] K. He, et al., “Deep residual learning for image recognition,” IEEE
[11] X. Hu, et al., “ACNet: Attention Based Network to Exploit Comple-               Conf. on Computer Vision and Pattern Recognition (CVPR), pp. 770–
     mentary Features for RGBD Semantic Segmentation,” IEEE Int. Conf.               778, 2016.
     on Image Processing (ICIP), 2019.                                          [37] L.-C. Chen, et al., “Rethinking Atrous Convolution for Semantic
[12] N. Silberman, et al., “Indoor Segmentation and Support Inference from           Image Segmentation,” arXiv preprint arXiv:1706.05587, 2017.
     RGBD Images,” in Europ. Conf. on Computer Vision (ECCV), 2012.             [38] J. Hu, et al., “Squeeze-and-excitation networks,” in IEEE Conf. on
[13] S. Song, et al., “SUN RGB-D: A RGB-D Scene Understanding                        Computer Vision and Pattern Recognition (CVPR), 2018, pp. 7132–
     Benchmark Suite,” in IEEE Conf. on Computer Vision and Pattern                  7141.
     Recognition (CVPR), 2015, pp. 567–576.                                     [39] L.-C. Chen, et al., “Encoder-Decoder with Atrous Separable Convolu-
[14] M. Cordts, et al., “The Cityscapes Dataset for Semantic Urban                   tion for Semantic Image Segmentation,” in Europ. Conf. on Computer
     Scene Understanding,” IEEE Conf. on Computer Vision and Pattern                 Vision (ECCV), 2018, pp. 801–818.
     Recognition (CVPR), pp. 3213–3223, 2016.                                   [40] D. P. Kingma and J. Ba, “Adam: A Method for Stochastic Optimiza-
[15] Y. Zhong, et al., “3D Geometry-Aware Semantic Labeling of Outdoor               tion,” in Int. Conf. Learning Representation (ICLR), 2015.
     Street Scenes,” in Int. Conf. on Pattern Recognition (ICPR), 2018, pp.     [41] J. Bornschein, et al., “Small Data, Big Decisions: Model Selection in
     2343–2349.                                                                      the Small-Data Regime,” in Int. Conf. on Machine Learning (ICML),
[16] Y. Xing, et al., “2.5D Convolution for RGB-D Semantic Segmen-                   2020.
     tation,” in IEEE Int. Conf. on Image Processing (ICIP), 2019, pp.          [42] D. Eigen and R. Fergus, “Predicting depth, surface normals and se-
     1410–1414.                                                                      mantic labels with a common multi-scale convolutional architecture,”
[17] Y. Xing, et al., “Malleable 2.5D Convolution: Learning Receptive                Int. Conf. on Computer Vision (ICCV), pp. 2650–2658, 2015.
     Fields along the Depth-axis for RGB-D Scene Parsing,” in Europ.            [43] J. McCormac, et al., “SceneNet RGB-D: Can 5M Synthetic Images
     Conf. on Computer Vision (ECCV), 2020, pp. 1–17.                                Beat Generic ImageNet Pre-training on Indoor Segmentation?” Int.
[18] W. Wang and U. Neumann, “Depth-Aware CNN for RGB-D Seg-                         Conf. on Computer Vision (ICCV), pp. 2697–2706, 2017.
     mentation,” in Europ. Conf. on Computer Vision (ECCV), 2018, pp.           [44] S.-W. Hung, et al., “Incorporating Luminance, Depth and Color
     144–161.                                                                        Information by a Fusion-Based Network for Semantic Segmentation,”
[19] L.-Z. Chen, et al., “Spatial Information Guided Convolution                     in IEEE Int. Conf. on Image Processing (ICIP), 2019, pp. 2374–2378.
     for Real-Time RGBD Semantic Segmentation,” arXiv preprint                  [45] Lingzhu Xiang, et al., “Libfreenect2: Release 0.2,” 2016. [Online].
     arXiv:2004.04534, pp. 1–11, 2020.                                               Available: https://zenodo.org/record/50641
[20] Y. Chen, et al., “3D Neighborhood Convolution: Learning Depth-             [46] F. J. Lawin, et al., “Efficient multi-frequency phase unwrapping
     Aware Features for RGB-D and RGB Semantic Segmentation,” in Int.                using kernel density estimation,” in Europ. Conf. on Computer Vi-
     Conf. on 3D Vision (3DV), 2019, pp. 173–182.                                    sion (ECCV), 2016, pp. 170–185.
[21] Y. Xing, et al., “Coupling Two-Stream RGB-D Semantic Segmentation
     Network by Idempotent Mappings,” in IEEE Int. Conf. on Image
     Processing (ICIP), 2019, pp. 1850–1854.
[22] X. Chen, et al., “Bi-directional Cross-Modality Feature Propagation
     with Separation-and-Aggregation Gate for RGB-D Semantic Segmen-
     tation,” in Europ. Conf. on Computer Vision (ECCV), 2020, pp. 561–
     577.
[23] S. Lee, et al., “RDFNet: RGB-D Multi-level Residual Feature Fusion
     for Indoor Semantic Segmentation,” Int. Conference on Computer
     Vision (ICCV), pp. 4990–4999, 2017.
