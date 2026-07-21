---
source_id: 043
bibtex_key: liu2021swinnet
title: SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection
year: 2022
domain_theme: RGB-D SOD
verified_pdf: 43_SwinNet.pdf
char_count: 86487
---

JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                     1

                                               SwinNet: Swin Transformer Drives Edge-Aware
                                                RGB-D and RGB-T Salient Object Detection
                                                                                 Zhengyi Liu*, Yacheng Tan, Qian He and Yun Xiao

                                            Abstract—Convolutional neural networks (CNNs) are good at                    or thermal infrared information as the supplementary modality
                                         extracting contexture features within certain receptive fields,                 has shown the advantages to SOD performance improvements,
                                         while transformers can model the global long-range dependency                   because the depth image can provide the more geometry
                                         features. By absorbing the advantage of transformer and the
arXiv:2204.05585v1 [cs.CV] 12 Apr 2022

                                         merit of CNN, Swin Transformer shows strong feature represen-                   information and the thermal image can capture the radiated
                                         tation ability. Based on it, we propose a cross-modality fusion                 heat of objects especially under adverse weather and lighting
                                         model, SwinNet, for RGB-D and RGB-T salient object detection.                   conditions. Nevertheless, how to effectively implement cross-
                                         It is driven by Swin Transformer to extract the hierarchical                    modality information fusion is still challenging, which can
                                         features, boosted by attention mechanism to bridge the gap                      significantly affect the achievement of robust performance.
                                         between two modalities, and guided by edge information to
                                         sharp the contour of salient object. To be specific, two-stream                    In the past few years, convolutional neural networks (CNNs)
                                         Swin Transformer encoder first extracts multi-modality features,                have achieved milestones in RGB-D and RGB-T SOD. How-
                                         and then spatial alignment and channel re-calibration mod-                      ever, CNN gathers information from neighborhood pixels and
                                         ule is presented to optimize intra-level cross-modality features.               loses spatial information due to pooling operation. It is not
                                         To clarify the fuzzy boundary, edge-guided decoder achieves                     easy to learn global long-range semantic information inter-
                                         inter-level cross-modality fusion under the guidance of edge
                                         features. The proposed model outperforms the state-of-the-                      action well. Recently, Swin Transformer[34] is proposed. It
                                         art models on RGB-D and RGB-T datasets, showing that it                         implements pairwise entity interactions within a local window
                                         provides more insight into the cross-modality complementarity                   by multi-head self-attention, and establishes long-range depen-
                                         task.https://github.com/liuzywen/SwinNet                                        dency across windows by shifted windowing scheme. Features
                                           Index Terms—transformer, salient object detection, RGB-D,                     extracted from transformer have more global attributes than
                                         RGB-T, multi-modality                                                           those from CNN. By absorbing the locality, translation invari-
                                                                                                                         ance and hierarchical merits of CNN, Swin Transformer can be
                                                                   I. I NTRODUCTION                                      used as backbone network to extract hierarchical information
                                                                                                                         of each modality. The features from different modalities show
                                            Salient object detection (SOD) simulates the visual attention
                                                                                                                         the different attribution. They consistently display the common
                                         mechanism to capture the prominent object. As described
                                                                                                                         salient position in the spatial aspect, and respectively show
                                         in the SOD review[1], SOD has been extended from RGB
                                                                                                                         the different salient content in the channel aspect, so spatial
                                         image[2], [3], [4] to RGB-D image[5], [6], a group of
                                                                                                                         alignment and channel re-calibration module is designed to
                                         images[7], [8] and video[9], [10]. Recently, SOD in RGB-
                                                                                                                         boost the extracted features based on attention mechanism. In
                                         T image[11], light field image[12], [13], [14], high-resolution
                                                                                                                         addition, SOD task is essentially a pixel-level dense prediction
                                         image[15], [16], optical remote sensing image[17], [18], [19]
                                                                                                                         task. After the feature extraction of encoder, the multi-level
                                         and 360◦ omnidirectional image[20], [21] have been gradually
                                                                                                                         features with different receptive field and spatial resolution
                                         researched. SOD can benefit many image and video processing
                                                                                                                         need to be progressively combined by upsampling and skip
                                         tasks, such as image segmentation [22], [23], tracking [24],
                                                                                                                         connection. In the decoding process, shallow-level features
                                         [25], [26], retrieval [27], compression [28], cropping [29],
                                                                                                                         exhibit the detailed boundary information, and meanwhile it
                                         [30], retargeting[31], quality assessment [32] and activity
                                                                                                                         also brings some background noises. Therefore, edge-aware
                                         prediction[33].
                                                                                                                         module is presented to extract the edge feature, and further to
                                            When the light is insufficient or the background is cluttered
                                                                                                                         guide the decoder for both suppressing the shallow-layer noise
                                         in a scene, SOD is still a challenge issue. With the widespread
                                                                                                                         and refining the contour of objects.
                                         use of depth cameras and infrared imaging devices, the depth
                                                                                                                            Our main contributions can be summarized as follows:
                                            This work was supported by National Natural Science Foundation of               • A novel SOD model (SwinNet) for both RGB-D and
                                         China (62006002) and Natural Science Foundation of Anhui Province                     RGB-T tasks built upon the Swin Transformer backbone
                                         (1908085MF182).(Corresponding author: Zhengyi Liu)
                                            Zhengyi Liu, Yacheng Tan and Qian He are with Key Laboratory of                    is proposed. It extracts discriminative features from Swin
                                         Intelligent Computing and Signal Processing of Ministry of Education, School          Transformer backbone which absorbs the local advantage
                                         of Computer Science and Technology, Anhui University, Hefei, China(e-mail:            of convolution neural network and the long-range depen-
                                         liuzywen@ahu.edu.cn,1084043983@qq.com,1819469871@qq.com).
                                            Yun Xiao is with Key Laboratory of Intelligent Computing and Signal                dency merit of transformer, outperforming the state-of-
                                         Processing of Ministry of Education, School of Artificial Intelligence, Anhui         the-art (SOTA) RGB-D and RGB-T SOD models.
                                         University, Hefei, China(e-mail: 280240406@qq.com).                                • A newly designed spatial alignment and channel re-
                                            Copyright ©2021 IEEE. Personal use of this material is permitted. However,
                                         permission to use this material for any other purposes must be obtained from          calibration module is used to optimize the features of each
                                         the IEEE by sending an email to pubs-permissions@ieee.org.                            modality based on attention mechanism, achieving intra-
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                     2

    layer cross-modality fusion from the spatial and channel      modalities. CSRNet[65] uses context-guided cross modality
    aspects.                                                      fusion module to fuse two modalities, and designs a stacked
  • The proposed edge-guided decoder achieves inter-layer         refinement network to refine the segmentation results. Pushed
    cross-modal fusion under the guidance of edge-aware           by the global merit of Transformer in computer vision, we
    module, generating the sharper contour.                       propose transformer based method to detect the salient object
                                                                  in RGB-T images.
                      II. R ELATED WORKS
A. RGB-D salient object detection
                                                                  C. Transformer
   Salient object detection has achieved the massive improve-
ment by combining the other modality with color modality.            Vaswani et al.[53] first proposes transformer with stacked
Depth image is exactly a good supplement, because it provides     multi-head self-attention and point-wise feed-forward layers
more reliable spatial structure information and insensitive to    in machine translation task. Recently, inspired by successful
the variations of the environment lights and colors.              ViT[66], transformer variants emerge explosively. T2T[66]
   Cong et al.[35] introduces depth information in the initial-   progressively structurizes the image to tokens by recursively
ization, refinement and optimization of saliency map, achiev-     aggregating neighboring tokens into one token. CvT[67]
ing transfer from existing RGB SOD models to RGB-D                adds convolutional layers into the multi-head self-attention.
SOD models. In these years, attention mechanism[36], [37],        PVT[68] introduces a progressive shrinking pyramid to reduce
[38], [39], [40], [41], multi-task learning[42], [43], [44],      the sequence length of the transformer. DPT[69] assembles
[45], knowledge distillation[46], graph neural networks[47],      tokens from multiple stages of the vision transformer and
neural architecture search[48], 3D convolutional neural           progressively combines them into full-resolution predictions
networks[49], self-supervised learning[50], generative adver-     using a convolutional decoder. Swin transformer[34] designs
sarial networks[51], disentanglement and reconstruction[52]       the shifted window-based multi-head attentions to reduce
are applied to solve SOD task. The intrinsic defect of CNN        the computation cost. CAT[70] alternately applies attention
limits above methods in learning global long-range depen-         inner patch and between patches to maintain the performance
dencies. Visual Saliency Transformer (VST)[6] propagates          with lower computational cost and builds a cross attention
long-range dependencies across modalities by Scaled Dot-          hierarchical network. Due to the perfect performance of Swin
Product Attention[53] between the queries from one modality       Transformer, it is used as the backbone network.
with the keys of the other modality. It also designs reverse
T2T to decode and introduces edge detection to improve the                          III. P ROPOSED METHOD
performance. Motivated by its success, we introduce Swin
Transformer as backbone to enhance the feature representa-        A. Overview
tion, and then use transformer encoder and CNN decoder to            The overall framework of the proposed model is illustrated
complete the SOD task.                                            in Fig.1, which consists of a two-stream backbone, a spatial
                                                                  alignment and channel re-calibration module, an edge-aware
B. RGB-T salient object detection                                 module and an edge-guided decoder. Note that since RGB-D
   The thermal image can capture the radiated heat of objects,    and RGB-T SOD are the same multi-modality fusion tasks, for
and it is insensitive to lighting and weather conditions, and     brevity, below we only elaborate the implementation detail of
suitable for handling scenes captured under adverse condi-        RGB-D SOD task, because that of RGB-T is the same.
tions, for example, total darkness environment, foggy weather,
and cluttered backgrounds. Therefore, thermal image is a
                                                                  B. Two-stream Swin Transformer backbone
promising supplement to the RGB image for SOD. In earlier
years, RGB-T SOD adopts machine learning methods, for                Swin Transformer has the flexibility to model at various
example, SVM[54], ranking models[55], [56], [57] and graph        scales and has linear computational complexity with respect
learning[58]. With the development of CNN, Tu et al.[59]          to image size[34]. We adopt two Swin Transformers to extract
propose a baseline model which combines CNN with attention        hierarchical features from multi-modality image pairs. Con-
mechanism. Zhang et al.[60], [61] propose two end-to-end          sidering the complexity and efficiency, Swin-B version[34] is
CNN based RGB-T SOD models to achieve multi-scale, multi-         adopted.
modality and multi-level fusion. ECFFNet[11] achieves more           Each Swin Transformer first splits the input single-modality
effectively cross-modality fusion, and enhances salient object    image into non-overlapping patches by a patch embedding.
boundaries by a bilateral reversal fusion of foreground and       The feature of each patch in color stream is set as a concate-
background information. MIDD[62] proposes multi-interactive       nation of the raw pixel RGB values, while that in depth stream
dual-decoder to integrate the multi-level interactions of dual    is set as a concatenation of three copied depth values. Then,
modalities and global contexts. MMNet[63] simulates visual        they are fed into the multi-stage feature transformation. With
color stage doctrine to fuse cross-modal features in stages,      the increasing depth of the network, the number of tokens
and designs bi-directional multi-scale decoder to capture both    is gradually reduced by patch merging layers to produce the
local and global information. CGFNet[64] adopts the guidance      hierarchical representation of each modality, which can be
manner of one modality on the other modality to fuse two          denoted as {STic }4i=1 and {STid }4i=1 , respectively.
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                                   3

Fig. 1. An overview of our proposed SwinNet. It consists of a two-stream backbone, a spatial alignment and channel re-calibration module, an edge-aware
module and an edge-guided decoder. Multi-modal hierarchical features from two-stream backbone will be fed into spatial alignment and channel re-calibration
modules to generate the enhanced features Fic and Fid (i=1,· · · , 4). Besides, edge feature is generated from edge-aware module which process the shallow-layer
features of the depth backbone. At last, in the edge-guided decoder, enhanced features and edge feature are combined to generate saliency map.

C. Spatial alignment and channel re-calibration module                              Next, the common spatial attention map is served as the
   On one hand, since the position of salient objects in multi-                  weight of color feature and depth feature to achieve the spatial
                                                                                 alignment of both modalities by:
modality image pairs should be the same, the features from
different modalities need to be aligned at first to show the                                                 ST 1ci = SAi × STic
                                                                                                                                                            (3)
common salient position. On the other hand, since RGB image                                                 ST 1di = SAi × STid
shows more appearance and texture information, and depth
image exhibits more spatial cue, the features from different                        Third, the aligned features in spatial part ST 1li (l ∈ {c, d})
modalities are different in the importance of feature channels,                  are performed channel attention respectively, to generate chan-
                                                                                 nel attention map which shows more weights on the more
and the multi-modality features need to be re-calibrated to em-                  salient content in each modality by:
phasize their respective salient content. Therefore, the spatial
alignment and channel re-calibration module is proposed. It                                                  CAci = CA(ST 1ci )
                                                                                                                                                            (4)
first aligns two modalities in spatial part, and then recalibrates                                           CAdi = CA(ST 1di )
respective channel part to pay more attention to the salient
                                                                                 where CA(·) denotes channel attention operation which is
content in each modality.                                                        defined as:
   Specifically, given the color features STic and depth feature
STid at a certain hierarchy i ∈ {1, · · · , 4}, we first compute                                 CA(x) = Sigmoid(Conv1 (GM P (x)))                          (5)
their common spatial attention map SAi as:
                        SAi = SA(STic × STid )                            (1)
                                                                                 where GM P (·) means the global max pooling operation,
                                                                                 Conv1 represents the convolution operation with the kernel
where “×” means element-wise multiplication operation, and
SA(·) denotes spatial attention operation which is defined as:                   size 1×1.
                                                                                    Last, each channel attention map is multiplied with original
              SA(x) = Sigmoid(Conv3 (CGM P (x)))                          (2)    feature to achieve the channel re-calibration.
                                                                                                              Fic = CAci × STic
                                                                                                                                                            (6)
where CGM P (·) means global max pooling operation along                                                     Fid = CAdi × STid
channel direction, Conv3 (·) represents the convolution oper-
ation with the kernel size 3×3, and Sigmoid(·) denotes the                          After the spatial alignment and channel re-calibration mod-
sigmoid activation function.                                                     ule, the enhanced features Fil (l ∈ {c, d}) achieve the position
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                        4

alignment and channel re-calibration, which show the stronger            F. Loss function
representation ability.                                                     The loss function L is defined as:
                                                                                                  L = Le (Se ) + Ls (S)                      (12)
D. Edge-aware module
   As we all known, high-layer features express more semantic            where Le and Ls denote edge loss and saliency loss, respec-
information, while shallow-layer features carry more details.            tively.
Meanwhile, salient objects are more likely to exhibit pop-                  1) Edge loss: The edge map is generated from edge-aware
out structure in the depth image[71]. It is easy to depict the           module. Specifically, edge feature Fe0 is fed into a convolution
object contours by depth contrast. Therefore, the shallow-layer          layer and a upsampling layer to generate edge map Se by:
features of the depth backbone are used to produce the edge                                      Se = U p4 (Conv3 (Fe0 ))                    (13)
feature.
   Specifically, STid (i = 1, 2, 3) are performed 1×1 convolu-
tional operation and upsampling operation to generate three                The edge ground truth can be easily got from saliency
features with the same size, and then they are concatenated to           map ground truth by Canny edge detector [73]. It is used to
generate edge feature.                                                   supervise the edge map Se . The edge loss Le adopts the cross-
                                                                         entropy loss, and it is defined as:
Fe = Concat(Conv1 (ST1d ), U p2 (Conv1 (ST2d )), U p4 (Conv1 (Std3 )))                   X                             X
                                                               (7)        Le (Se ) = −          logP r(yj = 1|Se ) −          logP r(yj = 0|Se )
                                                                                         j∈Z+                          j∈Z−
                                                                                                                                             (14)
where U px (·) denotes x×upsampling operation, and
Concat(·) means the concatenation operation.
   Next, the obtained edge feature is performed a channel                where Z+ and Z− denote the edge pixels set and background
attention and a residual connection to generate the clearer edge         pixels set respectively. P r(yj = 1|Se ) is the prediction map
information by:                                                          in which each value denotes the edge confidence for the pixel.
                                                                            2) Saliency loss: The final saliency map can be gener-
                Fe0 = Fe × CA(BConv(Fe )) + Fe                  (8)      ated from edge-guided decoder. Specifically, the edge-guided
                                                                         salient feature Fs is fed into a convolution layer and a
                                                                         upsampling layer to generate saliency map S by:
where BConv(·) represents convolutional operation with ker-
                                                                                                  S = U p4 (Conv3 (Fs ))                     (15)
nel size 3×3 followed by a batch normalization layer and
a ReLU activation function, and “+” means element-wise
addition operation.                                                         The saliency loss Ls adopts the cross-entropy loss, and it
  The edge-aware module outputs the edge features Fe0 which              is defined as:
                                                                                       X                           X
will be used to guide the decoding process of the model and               Ls (S) = −          logP r(yj = 1|S) −          logP r(yj = 0|S) (16)
enhance the details.                                                                   j∈Y+                        j∈Y−

                                                                         where Y+ and Y− denote the salient region pixels set and non-
E. Edge-guided decoder
                                                                         salient pixels set respectively. P r(yj = 1|S) is the prediction
   After spatial alignment and channel re-calibration and edge           map in which each value denotes the salient region confidence
feature extraction, decoder combines the enhanced hierarchical           for the pixel.
features of different modalities with the edge features to
produce the edge-guided salient feature.                                                          IV. E XPERIMENTS
   Specifically, the aligned and re-calibrated color and depth
features from two modalities Fic and Fid at a certain hierarchy          A. Datasets and evaluation metrics
i ∈ {1, · · · , 4} are fused by the addition, multiplication and            1) Datasets: For RGB-D SOD, we evaluate the pro-
concatenation operation by:
                                                                         posed method on several challenging RGB-D SOD datasets.
              Fi = Concat((Fid + Fic ), (Fid × Fic ))           (9)      NLPR [74] includes 1,000 images with single or multiple
                                                                         salient objects. NJU2K [75] consists of 2,003 stereo image
                                                                         pairs and ground-truth maps with different objects, complex
   Next, according to the decoding idea widely used in U-Net             and challenging scenes. STERE [76] incorporates 1,000 pairs
framework[72], the high-level fused feature is progressively
aggregated into the shallow-layer fused features by:                     of binocular images downloaded from the Internet. DES [77]
                                                                        has 135 indoor images collected by Microsoft Kinect. SIP [78]
                Fi + Conv3 (U p2 (F Fi+1 )),     i = 1, 2, 3             contains 1,000 high-resolution images of multiple salient per-
        F Fi =                                                 (10)
                           Fi ,                    i=4
                                                                         sons. DUT [79] contains 1,200 images captured by Lytro
                                                                         camera in real life scenes. For the sake of fair comparison, we
  At last, edge feature from edge-aware module is combined               use the same training dataset as in [78], [80], which consists
with fused feature to generate the edge-guided salient feature
Fs .                                                                     of 1,485 images from the NJU2K dataset and 700 images from
                     Fs = Concat(Fe0 , F F1 )                  (11)      the NLPR dataset. The remaining images are used for testing.
                                                                         In addition, on the DUT dataset, we follow the same protocols
                                                                         as in [79], [81], [46], [45], [44] to add additional 800 pairs
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                         5

from DUT for training and test on the remaining 400 pairs.         provided by the authors or generated by running source
In summary, our training set contains 2,185 paired RGB and         codes.
depth images, but when testing is conducted on DUT, our               Quantitative Evaluation. Fig.2 shows the comparison re-
training set contains 2,985 paired ones.                           sults on PR curve. Table.I shows the quantitative comparison
   For RGB-T SOD, we evaluate the proposed method on               results of four evaluation metrics. As can be clearly observed
three RGB-T SOD datasets. VT821[56] contains 821 manually          from figure that our curves are significant better than the others
registered image pairs. VT1000[58] contains 1,000 RGB-T            on NLPR, NJU2K, STERE, SIP and DUT datasets, slightly on
image pairs captured with highly aligned RGB and thermal           DES dataset. It benefits from the choose of backbone, spatial
cameras. VT5000[59] contains 5,000 pairs of high-resolution,       alignment and channel re-calibration of two modalities and
high-diversity and low-deviation RGB-T images. For the sake        edge guidance. Meanwhile, the table also gives the consistent
of fair comparison, we use the same training dataset as in [62],   results. The performance is improved with a large margin on
[82], [11], which consists of 2,500 image pairs in VT5000. The     NLPR, NJU2K, STERE, SIP and DUT datasets, and has a little
rest image pairs are used for testing.                             effectiveness on DES dataset. Compared with transformer-
   2) Evaluation Metrics: We adopt widely used metrics to          based method VST[6], S-measure, F-measure, E-measure and
evaluate the performance of our model and SOTA RGB-D               MAE are improved about 0.007, 0.017, 0.010 and 0.005 on
and RGB-T SOD models. They are the precision-recall (PR)           average. The PR curve and evaluation metrics all verify the
curve [83], S-measure [84], F-measure [85], E-measure [86]         effectiveness and advantages of our proposed method in RGB-
and mean absolute error (MAE) [87]. Specifically, the PR           D SOD task.
curve plots precision and recall values by setting a series           Qualitative Evaluation. To make the qualitative compar-
of thresholds on the saliency maps to get the binary masks         isons, we show some visual examples in Fig.3. It can be
and further comparing them with the ground truth maps. The         observed that our method has the better detection results than
S-measure can evaluate both region-aware and object-aware          other methods in some challenging cases: similar foreground
structural similarity between saliency map and ground truth.       and background (1st -2nd rows), complex scene (3rd -4th rows),
The F-measure is the weighted harmonic mean of precision           depth image with low quality (5th -6th rows), small object
and recall, which can evaluate the overall performance. The        (7th -8th rows) and multiple objects (9th -10th rows). In ad-
E-measure simultaneously captures global statistics and local      dition, our approach can produce more fine-grained details as
pixel matching information. The MAE measures the average           highlighted in the salient region (11th -12th rows). The visual
of the per-pixel absolute difference between the saliency maps     examples indicate that our approach can better locate salient
and the ground truth maps. In our experiment, E-measure and        objects and produce more accurate saliency maps.
F-measure adopt the adaptive values.
                                                                      2) RGB-T SOD: For RGB-T SOD, our model is
                                                                   compared with some SOTA RGB-T SOD algorithms,
B. Implementation details                                          including MTMR[56], M3S-NIR[55], SGDL[58], ADF[59],
   During the training and testing phase, the input RGB, depth     ECFFNet[11], MIDD[62], MMNet[63], CSRNet[65],
and thermal images are resized to 384×384. Since the depth         CGFNet[64]. To ensure the fairness of the comparison results,
image is single-channel data, it is copied to form three-channel   the saliency maps of the evaluation are provided by the
image which is the same as RGB and thermal images. Multiple        authors or generated by running source codes.
enhancement strategies are used for all training images, i.e.,        Quantitative Evaluation. Fig.4 shows the comparison re-
random flipping, rotating and border clipping. Parameters          sults on PR curve. Table.II shows the quantitative comparison
of the backbone network are initialized with the pretrained        results of four evaluation metrics. As can be clearly found
parameters of Swin-B network[34]. The rest of parameters are       from figure that our curves are very high, which means that
initialized to PyTorch default settings. We employ the Adam        our method is superior to the others with a large margin.
optimizer [88] to train our network with a batch size of 3         Furthermore, from the table, we can see that all the evaluation
and an initial learning rate 5e-5, and the learning rate will be   metrics are the best and our performance is significantly
divided by 10 every 100 epochs. Our model is trained on a          improved. The PR curve and evaluation metrics all verify the
machine with a single NVIDIA RTX 2080Ti GPU. The model             effectiveness and advantages of our proposed method in RGB-
converges within 200 epochs, which takes nearly 26 hours.          T SOD task.
                                                                      Qualitative Evaluation. To make the qualitative compar-
                                                                   isons, we show some visual examples in Fig.5. It can be
C. Comparisons with SOTAs                                          observed that our method has the better detection results than
   1) RGB-D SOD: For RGB-D SOD, our model is                       other methods in some challenging cases: similar foreground
compared with several SOTA RGB-D SOD algorithms,                   and background (1st row), complex scene (2nd row), poor
including D3Net [78], ASIF-Net[36], ICNet [89],                    illuminance (3rd row), low contrast of thermal image (4th
DCMF [52], DRLF [90], SSF [43], SSMA [38], A2dele [46],            row), small object (5th row) and multiple objects (6th row).
UC-Net [91], JL-DCF[92], CoNet [44], DANet [81],                   In addition, our approach is robust to noise disturbance, which
EBFSP[93],CDNet[94], HAINet[95], RD3D[49], DSA2F[48],              can be seen in the 7th row. These all indicate that our approach
MMNet[63] and VST[6]. To ensure the fairness of the                can better adapt to different scenes, and work well by cross-
comparison results, the saliency maps of the evaluation are        modality fusion.
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                                 6

                    (a) NLPR dataset                                      (b) NJU2K dataset                                        (c) STERE dataset

                     (d) DES dataset                                          (e) SIP dataset                                       (f) DUT dataset
Fig. 2. P-R curves comparison of different models on six RGB-D datasets. Our SwinNet represented by red solid line outperforms SOTA models.

                                                               TABLE I
 S- MEASURE , ADAPTIVE F- MEASURE , ADAPTIVE E- MEASURE , MAE COMPARISONS WITH DIFFERENT RGB-D MODELS . T HE BEST RESULT IS IN BOLD .

                   D3Net ASIF-Net ICNet DCMF DRLF SSF      SSMA A2dele UC-Net JL-DCF CoNet DANet EBFSP CDNet HAINet RD3D DSA2F MMNet VST SwinNet
Datasets Metric
                  TNNLS20 TCYB20 TIP20 TIP20 TIP20 CVPR20 CVPR20 CVPR20 CVPR20 CVPR20 ECCV20 ECCV20 TMM21 TIP21 TIP21 AAAI21 CVPR21 TCSVT21 arXiv Ours

         S↑         .912    .909    .923   .900   .903   .914   .915   .896    .920   .925      .908   .920   .915   .902   .924    .930   .918   .925    .931   .941
        Fβ ↑        .861    .869    .870   .839   .843   .875   .853   .878    .890   .878      .846   .875   .897   .848   .897    .892   .892   .889    .886   .908
NLPR
        Eξ ↑        .944    .944    .944   .933   .936   .949   .938   .945    .953   .953      .934   .951   .952   .935   .957    .958   .950    .950   .954   .967
        MAE↓        .030    .029    .028   .035   .032   .026   .030   .028    .025   .022      .031   .027   .026   .032   .024    .022   .024   .024    .023   .018

       S↑           .901     .891   .894   .889   .886   .899   .894   .869    .897   .902      .895   .899   .903   .885   .912    .916   .904   .911    .922   .935
      Fβ ↑          .865    .877    .868   .859   .849   .886   .865   .874    .889   .885      .872   .871   .894   .866   .900    .901   .898   .900    .899   .922
NJU2K
      Eξ ↑          .914    .907    .905   .897   .901   .913   .896   .897    .903   .913      .912   .908   .907   .911   .922    .918   .922   .919    .914   .934
      MAE↓          .046    .047    .052   .052   .055   .043   .053   .051    .043   .041      .046   .045   .039   .048   .038    .036   .039   .038    .034   .027

       S↑           .899    .874    .903   .883   .888   .887   .890   .878    .903   .903      .905   .901   .900   .896   .907    .911   .897   .891    .913   .919
      Fβ ↑          .859    .852    .865   .841   .845   .867   .855   .874    .885   .869      .884   .868   .870   .873   .885    .886   .893   .880    .878   .893
STERE
      Eξ ↑          .920    .908    .915   .904   .915   .921   .907   .915    .922   .919      .927   .921   .912   .922   .925    .927   .927    .924   .917   .929
      MAE↓          .046    .051    .045   .054   .050   .046   .051   .044    .039   .040      .037   .043   .045   .042   .040    .037   .039   .045    .038   .033

      S↑            .898    .934    .920   .877   .895   .905   .941   .885    .933   .931      .911   .924   .937   .875   .935    .935   .916   .830    .943   .945
     Fβ ↑           .870    .915    .889   .820   .868   .876   .906   .865    .917   .900      .861   .899   .913   .839   .924    .917   .901   .746    .917   .926
 DES
     Eξ ↑           .951    .974    .959   .923   .954   .948   .974   .922    .974   .969      .945   .968   .974   .921   .974    .975   .955   .893    .979   .980
     MAE↓           .031    .019    .027   .040   .030   .025   .021   .028    .018   .020      .027   .023   .018   .034   .018    .019   .023   .058    .017   .016

         S↑         .860    .857    .854   .859   .850   .868   .872   .826    .875   .880      .858   .875   .885   .823   .880    .885   .862   .836    .904   .911
        Fβ ↑        .835    .847    .836   .819   .813   .851   .854   .825    .868   .873      .842   .855   .869   .805   .875    .874   .865   .839    .895   .912
  SIP
        Eξ ↑        .902     .895   .899   .898   .891   .911   .911   .892    .913   .921      .909   .914   .917   .880   .919    .920   .908   .882    .937   .943
        MAE↓        .063    .061    .069   .068   .071   .056   .057   .070    .051   .049      .063   .054   .049   .076   .053    .048   .057   .075    .040   .035
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                              7

Fig. 3. Visual comparison with SOTA RGB-D models. Our SwinNet is outstanding in some challenging cases: similar foreground and background (1st -
2nd rows), complex scene (3rd -4th rows), depth image with low quality (5th -6th rows), small object (7th -8th rows), multiple objects (9th -10th rows) and
fine-grained object (11th -12th rows).

                (a) VT821 dataset                                     (b) VT1000 dataset                                    (c) VT5000 dataset
Fig. 4. P-R curves comparison of different models on three RGB-T datasets. Our SwinNet represented by red solid line outperforms SOTA models.

D. Ablation studies                                                            comparison of ResNet101 and Swin Transformer in Fig. 6.
                                                                               From the left to the right, there are RGB image, depth image,
   We conduct ablation studies on RGB-D SOD to verify all                      ground truth (GT), the color feature in the fourth layer of
of components.                                                                 ResNet (ResNet-C4), the color feature in the fourth layer of
   1) The effectiveness of Swin Transformer backbone: We                       Swin Transformer (Swin-C4), the depth feature in the fourth
replaces Swin Transformer backbone with some CNN back-                         layer of ResNet (ResNet-D4), the depth feature in the fourth
bones (e.g., ResNet-50[96], Res2Net-50[97], ResNet-101[96],                    layer of Swin Transformer (Swin-D4), the prediction saliency
Res50+ViT16[98]) and transformer backbones (e.g., T2T-                         map of ResNet (ResNet-Pred), the prediction saliency map of
14[66] and PVT-M[68]) to check the effectiveness of back-                      Swin Transformer (Swin-Pred). From the Fig. 6 (a)(b), we
bones. From Table. III, we can find that the use of Swin                       can discover that ResNet-C4 is interior to Swin-C4, so as to
Transformer significantly improves the detection performance.                  generate the blurry prediction saliency map. From the Fig. 6
It profits from the integration of locality merit of CNN and                   (c)(d), we can find that some small objects are ignored in
global-aware ability of transformer. We also give some visual
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                             8

                                                               TABLE II
 S- MEASURE , ADAPTIVE F- MEASURE , ADAPTIVE E- MEASURE , MAE COMPARISONS WITH DIFFERENT RGB-T MODELS . T HE BEST RESULT IS IN BOLD .

                    Datasets Metric MTMR M3S-NIR SGDL ADF MIDD ECFFNet MMNet CSRNet CGFNet SwinNet
                                    IGTA18 MIPR19 TMM19 Arxiv20 TIP21 TCSVT21 TCSVT21 TCSVT21 TCSVT21 Ours
                           Sα ↑        .725     .723      .765     .810    .871     .877       .875       .885      .881      .904
                           Fβ ↑        .662     .734      .730     .716    .804     .810       .798       .830      .845      .847
                     VT821 E ↑        .815     .859      .847     .842    .895     .902       .893       .908      .912      .926
                           MAE↓        .108     .140      .085     .077    .045     .034       .040       .038      .038      .030
                           Sα ↑        .706     .726      .787     .910    .915     .923       .917       .918      .923      .938
                           Fβ ↑        .715     .717      .764     .847    .882     .876       .863       .877      .906      .896
                    VT1000 E ↑        .836     .827      .856     .921    .933     .930       .924       .925      .944      .947
                           MAE↓        .119     .145      .090     .034    .027     .021       .027       .024      .023      .018
                           Sα ↑        .680     .652      .750     .863    .867     .874       .864       .868      .883      .912
                           Fβ ↑        .595     .575      .672     .778    .801     .806       .785       .810      .851      .865
                    VT5000 E ↑        .795     .780      .824     .891    .897     .906       .890       .905      .922      .942
                           MAE↓        .114     .168      .089     .048    .043     .038       .043       .042      .035      .026

Fig. 5. Visual comparison with SOTA RGB-T models. Our SwinNet is outstanding in some challenging cases: similar foreground and background (1st row),
complex scene (2nd row), poor illuminance (3rd row), low contrast of thermal image (4th row), small object (5th row), multiple objects (6th row) and noise
disturbance object (7th row).

ResNet-D4. It may be caused by the larger receptive field                     calibration are purified and the noises are obviously reduced,
in convolution neural network. Equipped with the long-range                   especially in the first column. From the comparison between
dependency merit, Swin-D4 shows salient features with more                    Fig. 7 (c) and (d), we find that the depth features with the help
integrity. Certainly, Swin-Pred shows the better result than                  of color features are close to ground truth, and salient region
ResNet-Pred.                                                                  are misjudged less, especially in the second and third column.
   2) The effectiveness of spatial alignment and channel re-                     Furthermore, we replace spatial alignment and channel re-
calibration module: Fig. 7 shows visual comparison of some                    calibration module with Depth-enhanced Module (DEM) in
ablation studies. From left to right, there are RGB image,                    BBS-Net [39] which consists of the similar channel attention
depth image, ground truth saliency map, prediction saliency                   and spatial attention but no alignment operation to verify the
map in the first line. In other lines, there are features in                  effectiveness of spatial alignment and channel re-calibration
different layers, corresponding with the color features from                  module. From Table. IV, we can see that our S-measure, F-
backbones {STic }4i=1 , the color features after spatial alignment            measure and E-measure and MAE wins about 0.006, 0.006,
and channel re-calibration module {Fic }4i=1 , the depth features             0.005 and 0.002 when compared with DEM. The proposed
from backbones {STid }4i=1 , the depth features after spatial                 spatial alignment and channel re-calibration module enhances
alignment and channel re-calibration module {Fid }4i=1 , the                  the feature representation of color and depth images by the
features from decoder {F Fi }4i=1 . Last, a group of features                 intra-layer interaction between two modalities and attentional
in the decoder without edge guidance are shown in the last                    weight assignment.
line.                                                                            3) The effectiveness of edge guidance: We remove the
   From the comparison between Fig. 7 (a) and (b), we find                    edge guidance in the decoder to verify its effectiveness. From
that the color features after spatial alignment and channel re-               Fig. 7 (e) and (f), we can find the use of edge features
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                                9

                                                               TABLE III
E FFECTIVENESS ANALYSIS OF BACKBONE NETWORK , INCLUDING R ES N ET-50, R ES 2N ET-50, R ES N ET-101, R ES N ET-50+V I T16, T2T-14, PVT-M AND
                                                S WIN -B. T HE BEST RESULT IS IN BOLD .

                                       NLPR                NJU2K               STERE                SIP
                    Backbone
                                S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓
                   ResNet-50 .925 .878 .948 .026 .911 .894 .916 .039 .896 .872 .920 .044 .892 .879 .926 .046
                   Res2Net-50 .905 .813 .924 .036 .897 .840 .891 .054 .880 .816 .892 .061 .870 .840 .905 .065
                   ResNet-101 .924 .884 .955 .024 .920 .904 .922 .034 .885 .861 .918 .049 .897 .888 .931 .043
                  Res-50+ViT16 .932 .892 .960 .021 .922 .904 .918 .033 .903 .869 .917 .041 .894 .891 .930 .046
                     T2T-14    .928 .880 .958 .022 .915 .893 .919 .037 .894 .856 .918 .044 .897 .887 .931 .045
                     PVT-M     .925 .879 .956 .023 .917 .898 .921 .036 .901 .869 .922 .042 .893 .888 .932 .043
                     Swin-B    .941 .908 .967 .018 .935 .922 .934 .027 .919 .893 .929 .033 .911 .912 .943 .035

Fig. 6. Visual comparison between ResNet and Swin Transformer. From the left to the right, there are RGB image, depth image, ground truth (GT), the
color feature in the fourth layer of ResNet (ResNet-C4), the color feature in the fourth layer of Swin Transformer (Swin-C4), the depth feature in the fourth
layer of ResNet (ResNet-D4), the depth feature in the fourth layer of Swin Transformer (Swin-D4), the prediction saliency map of ResNet (ResNet-Pred), the
prediction saliency map of Swin Transformer (Swin-Pred).

                                                             TABLE IV
 E FFECTIVENESS ANALYSIS OF SPATIAL ALIGNMENT AND CHANNEL RE - CALIBRATION MODULE . DEM DENOTES THE MODEL WITH D EPTH - ENHANCED
     M ODULE IN BBS-N ET [39] INSTEAD OF OUR SPATIAL ALIGNMENT AND CHANNEL RE - CALIBRATION MODULE . T HE BEST RESULT IS IN BOLD .

                                   NLPR                NJU2K               STERE                SIP
                      Variant
                            S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓
                      DEM .936 .903 .964 .019 .930 .918 .929 .028 .914 .888 .928 .034 .900 .901 .933 .040
                      Ours .941 .908 .967 .018 .935 .922 .934 .027 .919 .893 .929 .033 .911 .912 .943 .035

enhances the detail of detected objects. Meanwhile, from                          5) Model complexity analysis: Model size of SwinNet is
Table. V, we can also see that our S-measure, F-measure                         198.7M parameters. Its computation cost is about 124.3G
and E-measure and MAE are improved about 0.004, 0.009,                          FLOPs and inference speed is about 10 FPS including all
0.006 and 0.003, respectively. It can further illustrate that edge              the IO and preprocessing. Its complexity is high. From Ta-
guidance improves the performance of our proposed model to                      ble.VII, we can find the computation cost mainly exists in
some extend.                                                                    Swin Transformer backbone. SwinNet-fuse denotes SwinNet
                                                                                removing spatial alignment and channel re-calibration mod-
   4) The effectiveness of each modality: To verify the con-                    ule, SwinNet-edge denotes SwinNet removing edge-aware
tribution of each modality, we conduct the ablation study.                      module, SwinNet-decoder denotes SwinNet removing edge-
From Table.VI we can see that depth plays an obvious role                       guided decoder. Spatial alignment and channel re-calibration
in improving the performance from the first and third lines.                    module and edge-aware module nearly spend no computation
Meanwhile, we also observe that depth information is interior                   cost. Edge-guided decoder cost a little computation due to
to color cue in SOD performance when comparing the first and                    some convolution operations during upsampling process. The
second lines. Especially, in STERE dataset, depth information                   majority of cost exists in two Swin Transformer backbones.
plays a negative role because there are some depth images with
low quality. The third line denoted as fusion result achieves
the best results in a whole.
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                              10

                                                                     TABLE V
                                  E FFECTIVENESS ANALYSIS OF EDGE - GUIDED DECODER . T HE BEST RESULT IS IN BOLD .

                                       NLPR                NJU2K               STERE                SIP
                     Variant
                                S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓
                  Without edge .938 .901 .963 .020 .928 .911 .922 .031 .919 .887 .927 .034 .905 .900 .937 .040
                      Ours     .941 .908 .967 .018 .935 .922 .934 .027 .919 .893 .929 .033 .911 .912 .943 .035

                                                             TABLE VI
                         A BLATION STUDY ABOUT INDEPENDENT MODALITY IN RGB-D SOD. T HE BEST RESULT IS IN BOLD .

                                    NLPR                NJU2K               STERE                SIP
                     Variant
                             S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓ S↑ Fβ ↑ Eξ ↑ MAE↓
                    RGB     .932 .869 .955 .024 .921 .901 .919 .036 .923 .898 .926 .034 .902 .890 .933 .042
                    Depth   .896 .837 .937 .034 .888 .862 .899 .051 .768 .744 .855 .093 .884 .881 .923 .050
                  RGB+Depth .941 .908 .967 .018 .935 .922 .934 .027 .919 .893 .929 .033 .911 .912 .943 .035

                                                                                                    V. C ONCLUSIONS
                                                                                Inspired by the success of transformer, it is introduced to
                                                                             drive RGB-D and RGB-T SOD. SwinNet achieves SOTA per-
                                                                             formance, in which Swin Transformer absorbs the local merit
                                                                             of CNN and global advantage to encode hierarchical features,
                                                                             spatial alignment and channel re-calibration module enhances
                                                                             the intra-layer cross-modality features, edge-guided decoder
                                                                             strengths the inter-layer cross-modality fusion. Supervised by
                                                                             edge and saliency map, SwinNet works excellent on public
                                                                             databases. Increasing accuracy also brings about a reduction
                                                                             in speed. In the future, we will discuss the lightweight design.
                                                                                                           R EFERENCES
                                                                              [1] R. Cong, J. Lei, H. Fu, M.-M. Cheng, W. Lin, and Q. Huang, “Review
                                                                                  of visual saliency detection with comprehensive information,” IEEE
                                                                                  Transactions on circuits and Systems for Video Technology, vol. 29,
                                                                                  no. 10, pp. 2941–2959, 2018.
                                                                              [2] X. Hu, C.-W. Fu, L. Zhu, T. Wang, and P.-A. Heng, “SAC-Net: Spatial
                                                                                  attenuation context for salient object detection,” IEEE Transactions on
                                                                                  Circuits and Systems for Video Technology, vol. 31, no. 3, pp. 1079–
                                                                                  1090, 2020.
                                                                              [3] Z. Tu, Y. Ma, C. Li, J. Tang, and B. Luo, “Edge-guided non-local fully
                                                                                  convolutional network for salient object detection,” IEEE transactions
                                                                                  on circuits and systems for video technology, vol. 31, no. 2, pp. 582–593,
                                                                                  2020.
                                                                              [4] L. Wang, R. Chen, L. Zhu, H. Xie, and X. Li, “Deep sub-region network
                                                                                  for salient object detection,” IEEE Transactions on Circuits and Systems
                                                                                  for Video Technology, vol. 31, no. 2, pp. 728–741, 2020.
                                                                              [5] Z. Liu, S. Shi, Q. Duan, W. Zhang, and P. Zhao, “Salient object
                                                                                  detection for RGB-D image by single stream recurrent convolution
                                                                                  neural network,” Neurocomputing, vol. 363, pp. 46–57, 2019.
                                                                              [6] N. Liu, N. Zhang, K. Wan, J. Han, and L. Shao, “Visual Saliency
                                                                                  Transformer,” arXiv preprint arXiv:2104.12099, 2021.
                                                                              [7] G. Gao, W. Zhao, Q. Liu, and Y. Wang, “Co-Saliency Detection with Co-
                                                                                  Attention Fully Convolutional Network,” IEEE Transactions on Circuits
                                                                                  and Systems for Video Technology, vol. 31, no. 3, pp. 877–889, 2020.
Fig. 7. Visual comparison about the effectiveness of spatial alignment and
                                                                              [8] J. Han, G. Cheng, Z. Li, and D. Zhang, “A unified metric learning-based
channel re-calibration module and edge guidance.
                                                                                  framework for co-saliency detection,” IEEE Transactions on Circuits and
                                                                                  Systems for Video Technology, vol. 28, no. 10, pp. 2473–2483, 2017.
                                                                              [9] F. Guo, W. Wang, Z. Shen, J. Shen, L. Shao, and D. Tao, “Motion-
                                                                                  aware rapid video saliency detection,” IEEE Transactions on Circuits
                          TABLE VII                                               and Systems for Video Technology, vol. 30, no. 12, pp. 4887–4898, 2019.
    A BLATION STUDY ABOUT MODEL SIZE AND COMPUTATION COST.                   [10] M. Xu, B. Liu, P. Fu, J. Li, Y. H. Hu, and S. Feng, “Video salient
                                                                                  object detection via robust seeds extraction and multi-graphs manifold
      Methods SwinNet SwinNet-fuse SwinNet-edge SwinNet-decoder                   propagation,” IEEE Transactions on Circuits and Systems for Video
                                                                                  Technology, vol. 30, no. 7, pp. 2191–2206, 2019.
     Params(M) 198.7           198.3      198.4          173.6               [11] W. Zhou, Q. Guo, J. Lei, L. Yu, and J.-N. Hwang, “ECFFNet: effective
                                                                                  and consistent feature fusion network for RGB-T salient object detec-
     FLOPs(G) 124.3            124.3      122.4          88.9
                                                                                  tion,” IEEE Transactions on Circuits and Systems for Video Technology,
                                                                                  2021.
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                                  11

[12] Q. Zhang, S. Wang, X. Wang, Z. Sun, S. Kwong, and J. Jiang, “A multi-        [34] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and
     task collaborative network for light field salient object detection,” IEEE        B. Guo, “Swin transformer: Hierarchical vision transformer using shifted
     Transactions on Circuits and Systems for Video Technology, vol. 31,               windows,” arXiv preprint arXiv:2103.14030, 2021.
     no. 5, pp. 1849–1861, 2020.                                                  [35] R. Cong, J. Lei, H. Fu, J. Hou, Q. Huang, and S. Kwong, “Going from
[13] Y. Piao, Z. Rong, S. Xu, M. Zhang, and H. Lu, “DUT-LFSaliency:                    RGB to RGBD saliency: A depth-guided transformation model,” IEEE
     Versatile Dataset and Light Field-to-RGB Saliency Detection,” arXiv               transactions on cybernetics, vol. 50, no. 8, pp. 3627–3639, 2019.
     preprint arXiv:2012.15124, 2020.                                             [36] C. Li, R. Cong, S. Kwong, J. Hou, H. Fu, G. Zhu, D. Zhang, and
[14] Y. Zhang, L. Zhang, W. Hamidouche, and O. Deforges, “CMA-Net:                     Q. Huang, “ASIF-Net: Attention steered interweave fusion network for
     A Cascaded Mutual Attention Network for Light Field Salient Object                RGB-D salient object detection,” IEEE transactions on cybernetics,
     Detection,” arXiv preprint arXiv:2105.00949, 2021.                                vol. 51, no. 1, pp. 88–100, 2020.
[15] P. Zhang, W. Liu, Y. Zeng, Y. Lei, and H. Lu, “Looking for the               [37] N. Liu, N. Zhang, L. Shao, and J. Han, “Learning Selective Mutual
     detail and context devils: High-resolution salient object detection,” IEEE        Attention and Contrast for RGB-D Saliency Detection,” arXiv preprint
     Transactions on Image Processing, vol. 30, pp. 3204–3216, 2021.                   arXiv:2010.05537, 2020.
[16] Y. Zeng, P. Zhang, J. Zhang, Z. Lin, and H. Lu, “Towards high-resolution     [38] N. Liu, N. Zhang, and J. Han, “Learning Selective Self-Mutual Attention
     salient object detection,” in Proceedings of the IEEE/CVF International           for RGB-D Saliency Detection,” in Proceedings of the IEEE/CVF
     Conference on Computer Vision, 2019, pp. 7234–7243.                               Conference on Computer Vision and Pattern Recognition, 2020, pp.
[17] C. Li, R. Cong, C. Guo, H. Li, C. Zhang, F. Zheng, and Y. Zhao, “A                13 756–13 765.
     parallel down-up fusion network for salient object detection in optical      [39] D.-P. Fan, Y. Zhai, A. Borji, J. Yang, and L. Shao, “BBS-Net: RGB-D
     remote sensing images,” Neurocomputing, vol. 415, pp. 411–420, 2020.              salient object detection with a bifurcated backbone strategy network,” in
[18] C. Li, R. Cong, J. Hou, S. Zhang, Y. Qian, and S. Kwong, “Nested                  European Conference on Computer Vision. Springer, 2020, pp. 275–
     network with two-stream pyramid for salient object detection in optical           292.
     remote sensing images,” IEEE Transactions on Geoscience and Remote           [40] W. Zhang, Y. Jiang, K. Fu, and Q. Zhao, “BTS-Net: Bi-Directional
     Sensing, vol. 57, no. 11, pp. 9156–9166, 2019.                                    Transfer-And-Selection Network for RGB-D Salient Object Detection,”
[19] Q. Zhang, R. Cong, C. Li, M.-M. Cheng, Y. Fang, X. Cao, Y. Zhao,                  in 2021 IEEE International Conference on Multimedia and Expo
     and S. Kwong, “Dense attention fluid network for salient object detec-            (ICME). IEEE, 2021, pp. 1–6.
     tion in optical remote sensing images,” IEEE Transactions on Image           [41] Z. Chen, R. Cong, Q. Xu, and Q. Huang, “DPANet: Depth potentiality-
     Processing, vol. 30, pp. 1305–1317, 2020.                                         aware gated attention network for RGB-D salient object detection,” IEEE
[20] G. Ma, S. Li, C. Chen, A. Hao, and H. Qin, “Stage-wise salient object             Transactions on Image Processing, 2020.
     detection in 360◦ omnidirectional image via object-level semantical          [42] J. Wu, W. Zhou, T. Luo, L. Yu, and J. Lei, “Multiscale multilevel
     saliency ranking,” IEEE Transactions on Visualization and Computer                context and multimodal fusion for RGB-D salient object detection,”
     Graphics, vol. 26, no. 12, pp. 3535–3545, 2020.                                   Signal Processing, vol. 178, p. 107766, 2021.
[21] M. Huang, Z. Liu, G. Li, X. Zhou, and O. Le Meur, “FANet: Features           [43] M. Zhang, W. Ren, Y. Piao, Z. Rong, and H. Lu, “Select, Supplement and
     Adaptation Network for 360◦ Omnidirectional Salient Object Detec-                 Focus for RGB-D Saliency Detection,” in Proceedings of the IEEE/CVF
     tion,” IEEE Signal Processing Letters, vol. 27, pp. 1819–1823, 2020.              Conference on Computer Vision and Pattern Recognition, 2020, pp.
                                                                                       3472–3481.
[22] S. K. Yarlagadda, D. M. Montserrat, D. Guerra, C. J. Boushey, D. A.
                                                                                  [44] W. Ji, J. Li, M. Zhang, Y. Piao, and H. Lu, “Accurate RGB-D salient
     Kerr, and F. Zhu, “Saliency-Aware Class-Agnostic Food Image Segmen-
                                                                                       object detection via collaborative learning,” in Computer Vision–ECCV
     tation,” arXiv preprint arXiv:2102.06882, 2021.
                                                                                       2020: 16th European Conference, Glasgow, UK, August 23–28, 2020,
[23] H. Huang, M. Cai, L. Lin, J. Zheng, X. Mao, X. Qian, Z. Peng, J. Zhou,            Proceedings, Part XVIII 16. Springer, 2020, pp. 52–69.
     Y. Iwamoto, X.-H. Han et al., “Graph-based Pyramid Global Con-
                                                                                  [45] C. Li, R. Cong, Y. Piao, Q. Xu, and C. C. Loy, “RGB-D salient object
     text Reasoning with a Saliency-aware Projection for COVID-19 Lung
                                                                                       detection with cross-modality modulation and selection,” in European
     Infections Segmentation,” in ICASSP 2021-2021 IEEE International
                                                                                       Conference on Computer Vision. Springer, 2020, pp. 225–241.
     Conference on Acoustics, Speech and Signal Processing (ICASSP).
                                                                                  [46] Y. Piao, Z. Rong, M. Zhang, W. Ren, and H. Lu, “A2dele: Adaptive and
     IEEE, 2021, pp. 1050–1054.
                                                                                       Attentive Depth Distiller for Efficient RGB-D Salient Object Detection,”
[24] C. Ma, Z. Miao, X.-P. Zhang, and M. Li, “A saliency prior context                 in Proceedings of the IEEE/CVF Conference on Computer Vision and
     model for real-time object tracking,” IEEE Transactions on Multimedia,            Pattern Recognition, 2020, pp. 9060–9069.
     vol. 19, no. 11, pp. 2415–2424, 2017.
                                                                                  [47] A. Luo, X. Li, F. Yang, Z. Jiao, H. Cheng, and S. Lyu, “Cascade
[25] S. Hong, T. You, S. Kwak, and B. Han, “Online tracking by learning                graph neural networks for rgb-d salient object detection,” in European
     discriminative saliency map with convolutional neural network,” in                Conference on Computer Vision. Springer, 2020, pp. 346–364.
     International conference on machine learning, 2015, pp. 597–606.             [48] P. Sun, W. Zhang, H. Wang, S. Li, and X. Li, “Deep RGB-D Saliency
[26] P. Zhang, W. Liu, D. Wang, Y. Lei, H. Wang, and H. Lu, “Non-                      Detection with Depth-Sensitive Attention and Automatic Multi-Modal
     rigid object tracking via deep multi-scale spatial-temporal discriminative        Fusion,” in Proceedings of the IEEE/CVF Conference on Computer
     saliency maps,” Pattern Recognition, vol. 100, p. 107130, 2020.                   Vision and Pattern Recognition, 2021, pp. 1407–1417.
[27] Y. Gao, M. Shi, D. Tao, and C. Xu, “Database saliency for fast image         [49] Q. Chen, Z. Liu, Y. Zhang, K. Fu, Q. Zhao, and H. Du, “RGB-D Salient
     retrieval,” IEEE Transactions on Multimedia, vol. 17, no. 3, pp. 359–             Object Detection via 3D Convolutional Neural Networks,” AAAI, 2021.
     369, 2015.                                                                   [50] X. Zhao, Y. Pang, L. Zhang, H. Lu, and X. Ruan, “Self-Supervised
[28] Q.-G. Ji, Z.-D. Fang, Z.-H. Xie, and Z.-M. Lu, “Video abstraction based           Representation Learning for RGB-D Salient Object Detection,” arXiv
     on the visual attention model and online clustering,” Signal Processing:          preprint arXiv:2101.12482, 2021.
     Image Communication, vol. 28, no. 3, pp. 241–253, 2013.                      [51] B. Jiang, Z. Zhou, X. Wang, J. Tang, and B. Luo, “cmSalGAN: RGB-
[29] W. Wang, J. Shen, and H. Ling, “A deep network solution for attention             D Salient Object Detection with Cross-View Generative Adversarial
     and aesthetics aware photo cropping,” IEEE transactions on pattern                Networks,” IEEE Transactions on Multimedia, 2020.
     analysis and machine intelligence, vol. 41, no. 7, pp. 1531–1544, 2018.      [52] H. Chen, Y. Deng, Y. Li, T.-Y. Hung, and G. Lin, “RGBD salient object
[30] Y. Xu, W. Xu, M. Wang, L. Li, G. Sang, P. Wei, and L. Zhu, “Saliency              detection via disentangled cross-modal fusion,” IEEE Transactions on
     aware image cropping with latent region pair,” Expert Systems with                Image Processing, vol. 29, pp. 8407–8416, 2020.
     Applications, vol. 171, p. 114596, 2021.                                     [53] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
[31] M. Ahmadi, N. Karimi, and S. Samavi, “Context-aware saliency de-                  L. u. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances
     tection for image retargeting using convolutional neural networks,”               in Neural Information Processing Systems, vol. 30. Curran Associates,
     Multimedia Tools and Applications, vol. 80, no. 8, pp. 11 917–11 941,             Inc., 2017, p. 5998–6008.
     2021.                                                                        [54] Y. Ma, D. Sun, Q. Meng, Z. Ding, and C. Li, “Learning multiscale deep
[32] Q. Jiang, F. Shao, W. Lin, K. Gu, G. Jiang, and H. Sun, “Optimizing mul-          features and SVM regressors for adaptive RGB-T saliency detection,” in
     tistage discriminative dictionaries for blind image quality assessment,”          2017 10th International Symposium on Computational Intelligence and
     IEEE Transactions on Multimedia, vol. 20, no. 8, pp. 2035–2048, 2017.             Design (ISCID), vol. 1. IEEE, 2017, pp. 389–392.
[33] Z. Weng, W. Li, and Z. Jin, “Human activity prediction using saliency-       [55] Z. Tu, T. Xia, C. Li, Y. Lu, and J. Tang, “M3S-NIR: Multi-modal multi-
     aware motion enhancement and weighted LSTM network,” EURASIP                      scale noise-insensitive ranking for RGB-T saliency detection,” in 2019
     Journal on Image and Video Processing, vol. 2021, no. 1, pp. 1–23,                IEEE Conference on Multimedia Information Processing and Retrieval
     2021.                                                                             (MIPR). IEEE, 2019, pp. 141–146.
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, NOVEMBER 2021                                                                                                 12

[56] G. Wang, C. Li, Y. Ma, A. Zheng, J. Tang, and B. Luo, “RGB-T saliency      [79] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-
     detection benchmark: Dataset, baselines, analysis and a novel approach,”        scale recurrent attention network for saliency detection,” in Proceedings
     in Chinese Conference on Image and Graphics Technologies. Springer,             of the IEEE International Conference on Computer Vision, 2019, pp.
     2018, pp. 359–369.                                                              7254–7263.
[57] J. Tang, D. Fan, X. Wang, Z. Tu, and C. Li, “RGBT salient object           [80] S. Chen and Y. Fu, “Progressively guided alternate refinement network
     detection: benchmark and a novel cooperative ranking approach,” IEEE            for RGB-D salient object detection,” in European Conference on Com-
     Transactions on Circuits and Systems for Video Technology, vol. 30,             puter Vision. Springer, 2020, pp. 520–538.
     no. 12, pp. 4421–4433, 2019.                                               [81] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A single stream
[58] Z. Tu, T. Xia, C. Li, X. Wang, Y. Ma, and J. Tang, “RGB-T image                 network for robust and real-time RGB-D salient object detection,” in
     saliency detection via collaborative graph learning,” IEEE Transactions         European Conference on Computer Vision. Springer, 2020, pp. 646–
     on Multimedia, vol. 22, no. 1, pp. 160–173, 2019.                               662.
[59] Z. Tu, Y. Ma, Z. Li, C. Li, J. Xu, and Y. Liu, “RGBT salient               [82] Z. Tu, Z. Li, C. Li, and J. Tang, “Multi-interactive encoder-decoder net-
     object detection: A large-scale dataset and benchmark,” arXiv preprint          work for rgbt salient object detection,” arXiv preprint arXiv:2005.02315,
     arXiv:2007.03262, 2020.                                                         2020.
[60] Q. Zhang, N. Huang, L. Yao, D. Zhang, C. Shan, and J. Han, “RGB-           [83] A. Borji, M.-M. Cheng, H. Jiang, and J. Li, “Salient object detection:
     T salient object detection via fusing multi-level CNN features,” IEEE           A benchmark,” IEEE transactions on image processing, vol. 24, no. 12,
     Transactions on Image Processing, vol. 29, pp. 3321–3335, 2019.                 pp. 5706–5722, 2015.
                                                                                [84] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-measure:
[61] Q. Zhang, T. Xiao, N. Huang, D. Zhang, and J. Han, “Revisiting Feature
                                                                                     A new way to evaluate foreground maps,” in Proceedings of the IEEE
     Fusion for RGB-T Salient Object Detection,” IEEE Transactions on
                                                                                     international conference on computer vision, 2017, pp. 4548–4557.
     Circuits and Systems for Video Technology, 2020.
                                                                                [85] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned
[62] Z. Tu, Z. Li, C. Li, Y. Lang, and J. Tang, “Multi-Interactive Dual-
                                                                                     salient region detection,” in 2009 IEEE conference on computer vision
     Decoder for RGB-Thermal Salient Object Detection,” IEEE Transac-
                                                                                     and pattern recognition. IEEE, 2009, pp. 1597–1604.
     tions on Image Processing, vol. 30, pp. 5678–5691, 2021.
                                                                                [86] D.-P. Fan, C. Gong, Y. Cao, B. Ren, M.-M. Cheng, and A. Borji,
[63] W. Gao, G. Liao, S. Ma, G. Li, Y. Liang, and W. Lin, “Unified                   “Enhanced-alignment measure for binary foreground map evaluation,”
     Information Fusion Network for Multi-Modal RGB-D and RGB-T                      arXiv preprint arXiv:1805.10421, 2018.
     Salient Object Detection,” IEEE Transactions on Circuits and Systems       [87] F. Perazzi, P. Krähenbühl, Y. Pritch, and A. Hornung, “Saliency filters:
     for Video Technology, 2021.                                                     Contrast based filtering for salient region detection,” in 2012 IEEE
[64] J. Wang, K. Song, Y. Bao, L. Huang, and Y. Yan, “CGFNet: Cross-                 conference on computer vision and pattern recognition. IEEE, 2012,
     Guided Fusion Network for RGB-T Salient Object Detection,” IEEE                 pp. 733–740.
     Transactions on Circuits and Systems for Video Technology, 2021.           [88] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
[65] F. Huo, X. Zhu, L. Zhang, Q. Liu, and Y. Shu, “Efficient Context-Guided         arXiv preprint arXiv:1412.6980, 2014.
     Stacked Refinement Network for RGB-T Salient Object Detection,”            [89] G. Li, Z. Liu, and H. Ling, “ICNet: Information Conversion Network for
     IEEE Transactions on Circuits and Systems for Video Technology, 2021.           RGB-D Based Salient Object Detection,” IEEE Transactions on Image
[66] L. Yuan, Y. Chen, T. Wang, W. Yu, Y. Shi, F. E. Tay, J. Feng, and               Processing, vol. 29, pp. 4873–4884, 2020.
     S. Yan, “Tokens-to-token vit: Training vision transformers from scratch    [90] X. Wang, S. Li, C. Chen, Y. Fang, A. Hao, and H. Qin, “Data-level
     on imagenet,” arXiv preprint arXiv:2101.11986, 2021.                            recombination and lightweight fusion scheme for RGB-D salient object
[67] H. Wu, B. Xiao, N. Codella, M. Liu, X. Dai, L. Yuan, and L. Zhang,              detection,” IEEE Transactions on Image Processing, vol. 30, pp. 458–
     “Cvt: Introducing convolutions to vision transformers,” arXiv preprint          471, 2020.
     arXiv:2103.15808, 2021.                                                    [91] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. S. Saleh, T. Zhang, and
[68] W. Wang, E. Xie, X. Li, D.-P. Fan, K. Song, D. Liang, T. Lu, P. Luo, and        N. Barnes, “UC-Net: uncertainty inspired RGB-D saliency detection via
     L. Shao, “Pyramid vision transformer: A versatile backbone for dense            conditional variational autoencoders,” in Proceedings of the IEEE/CVF
     prediction without convolutions,” arXiv preprint arXiv:2102.12122,              Conference on Computer Vision and Pattern Recognition, 2020, pp.
     2021.                                                                           8582–8591.
[69] R. Ranftl, A. Bochkovskiy, and V. Koltun, “Vision transformers for dense   [92] K. Fu, D.-P. Fan, G.-P. Ji, and Q. Zhao, “JL-DCF: Joint learning and
     prediction,” arXiv preprint arXiv:2103.13413, 2021.                             densely-cooperative fusion framework for rgb-d salient object detection,”
[70] H. Lin, X. Cheng, X. Wu, F. Yang, D. Shen, Z. Wang, Q. Song, and                in Proceedings of the IEEE/CVF conference on computer vision and
     W. Yuan, “CAT: Cross Attention in Vision Transformer,” arXiv preprint           pattern recognition, 2020, pp. 3052–3062.
     arXiv:2106.05786, 2021.                                                    [93] N. Huang, Y. Yang, D. Zhang, Q. Zhang, and J. Han, “Employing
[71] D. Feng, N. Barnes, S. You, and C. McCarthy, “Local background                  Bilinear Fusion and Saliency Prior Information for RGB-D Salient
     enclosure for RGB-D salient object detection,” in Proceedings of the            Object Detection,” IEEE Transactions on Multimedia, 2021.
     IEEE conference on computer vision and pattern recognition, 2016, pp.      [94] W.-D. Jin, J. Xu, Q. Han, Y. Zhang, and M.-M. Cheng, “CDNet:
     2343–2350.                                                                      Complementary Depth Network for RGB-D Salient Object Detection,”
                                                                                     IEEE Transactions on Image Processing, vol. 30, pp. 3376–3390, 2021.
[72] O. Ronneberger, P. Fischer, and T. Brox, “U-Net: Convolutional net-
                                                                                [95] G. Li, Z. Liu, M. Chen, Z. Bai, W. Lin, and H. Ling, “Hierarchical
     works for biomedical image segmentation,” in International Confer-
                                                                                     Alternate Interaction Network for RGB-D Salient Object Detection,”
     ence on Medical image computing and computer-assisted intervention.
                                                                                     IEEE Transactions on Image Processing, vol. 30, pp. 3528–3542, 2021.
     Springer, 2015, pp. 234–241.
                                                                                [96] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
[73] J. Canny, “A computational approach to edge detection,” IEEE Trans-
                                                                                     recognition,” in Proceedings of the IEEE conference on computer vision
     actions on pattern analysis and machine intelligence, vol. 8, no. 6, pp.
                                                                                     and pattern recognition, 2016, pp. 770–778.
     679–698, 1986.
                                                                                [97] S. Gao, M.-M. Cheng, K. Zhao, X.-Y. Zhang, M.-H. Yang, and P. H. Torr,
[74] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “Rgbd salient object                “Res2Net: A new multi-scale backbone architecture,” IEEE transactions
     detection: a benchmark and algorithms,” in European conference on               on pattern analysis and machine intelligence, 2019.
     computer vision. Springer, 2014, pp. 92–109.                               [98] J. Chen, Y. Lu, Q. Yu, X. Luo, E. Adeli, Y. Wang, L. Lu, A. L. Yuille, and
[75] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based                 Y. Zhou, “Transunet: Transformers make strong encoders for medical
     on anisotropic center-surround difference,” in 2014 IEEE international          image segmentation,” arXiv preprint arXiv:2102.04306, 2021.
     conference on image processing (ICIP). IEEE, 2014, pp. 1115–1119.
[76] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency
     analysis,” in 2012 IEEE Conference on Computer Vision and Pattern
     Recognition. IEEE, 2012, pp. 454–461.
[77] Y. Cheng, H. Fu, X. Wei, J. Xiao, and X. Cao, “Depth enhanced
     saliency detection method,” in Proceedings of international conference
     on internet multimedia computing and service, 2014, pp. 23–27.
[78] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking
     RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale
     Benchmarks,” IEEE Transactions on Neural Networks and Learning
     Systems, 2020.
