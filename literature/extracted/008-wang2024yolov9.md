---
source_id: 008
bibtex_key: wang2024yolov9
title: YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
year: 2024
domain_theme: Fondasi RGB
verified_pdf: 8_YOLOv9.pdf
char_count: 119464
---

YOLOv9: Learning What You Want to Learn
                                                                      Using Programmable Gradient Information
                                                             Chien-Yao Wang1,2 , I-Hau Yeh2 , and Hong-Yuan Mark Liao1,2,3
                                                               1
                                                                 Institute of Information Science, Academia Sinica, Taiwan
                                                                    2
                                                                      National Taipei University of Technology, Taiwan
                                            3
                                              Department of Information and Computer Engineering, Chung Yuan Christian University, Taiwan
arXiv:2402.13616v2 [cs.CV] 29 Feb 2024

                                                        kinyiu@iis.sinica.edu.tw, ihyeh@emc.com.tw, and liao@iis.sinica.edu.tw

                                                                  Abstract
                                            Today’s deep learning methods focus on how to design
                                         the most appropriate objective functions so that the pre-
                                         diction results of the model can be closest to the ground
                                         truth. Meanwhile, an appropriate architecture that can
                                         facilitate acquisition of enough information for prediction
                                         has to be designed. Existing methods ignore a fact that
                                         when input data undergoes layer-by-layer feature extrac-
                                         tion and spatial transformation, large amount of informa-
                                         tion will be lost. This paper will delve into the important is-
                                         sues of data loss when data is transmitted through deep net-
                                         works, namely information bottleneck and reversible func-
                                         tions. We proposed the concept of programmable gradi-
                                         ent information (PGI) to cope with the various changes
                                         required by deep networks to achieve multiple objectives.
                                         PGI can provide complete input information for the tar-               Figure 1. Comparisons of the real-time object detecors on MS
                                         get task to calculate objective function, so that reliable            COCO dataset. The GELAN and PGI-based object detection
                                         gradient information can be obtained to update network                method surpassed all previous train-from-scratch methods in terms
                                         weights. In addition, a new lightweight network architec-             of object detection performance. In terms of accuracy, the new
                                         ture – Generalized Efficient Layer Aggregation Network                method outperforms RT DETR [43] pre-trained with a large
                                         (GELAN), based on gradient path planning is designed.                 dataset, and it also outperforms depth-wise convolution-based de-
                                                                                                               sign YOLO MS [7] in terms of parameters utilization.
                                         GELAN’s architecture confirms that PGI has gained su-
                                         perior results on lightweight models. We verified the pro-            in the field of deep learning have mainly focused on how
                                         posed GELAN and PGI on MS COCO dataset based ob-                      to develop more powerful system architectures and learn-
                                         ject detection. The results show that GELAN only uses                 ing methods, such as CNNs [21–23, 42, 55, 71, 72], Trans-
                                         conventional convolution operators to achieve better pa-              formers [8, 9, 40, 41, 60, 69, 70], Perceivers [26, 26, 32, 52,
                                         rameter utilization than the state-of-the-art methods devel-          56, 81, 81], and Mambas [17, 38, 80]. In addition, some
                                         oped based on depth-wise convolution. PGI can be used                 researchers have tried to develop more general objective
                                         for variety of models from lightweight to large. It can be            functions, such as loss function [5, 45, 46, 50, 77, 78], la-
                                         used to obtain complete information, so that train-from-              bel assignment [10, 12, 33, 67, 79] and auxiliary supervi-
                                         scratch models can achieve better results than state-of-the-          sion [18, 20, 24, 28, 29, 51, 54, 68, 76]. The above studies
                                         art models pre-trained using large datasets, the compari-             all try to precisely find the mapping between input and tar-
                                         son results are shown in Figure 1. The source codes are at:           get tasks. However, most past approaches have ignored that
                                         https://github.com/WongKinYiu/yolov9.                                 input data may have a non-negligible amount of informa-
                                                                                                               tion loss during the feedforward process. This loss of in-
                                         1. Introduction                                                       formation can lead to biased gradient flows, which are sub-
                                            Deep learning-based models have demonstrated far bet-              sequently used to update the model. The above problems
                                         ter performance than past artificial intelligence systems in          can result in deep networks to establish incorrect associa-
                                         various fields, such as computer vision, language process-            tions between targets and inputs, causing the trained model
                                         ing, and speech recognition. In recent years, researchers             to produce incorrect predictions.

                                                                                                           1
Figure 2. Visualization results of random initial weight output feature maps for different network architectures: (a) input image, (b)
PlainNet, (c) ResNet, (d) CSPNet, and (e) proposed GELAN. From the figure, we can see that in different architectures, the information
provided to the objective function to calculate the loss is lost to varying degrees, and our architecture can retain the most complete
information and provide the most reliable gradient information for calculating the objective function.
    In deep networks, the phenomenon of input data losing             built on auxiliary branch, so there is no additional cost.
information during the feedforward process is commonly                Since PGI can freely select loss function suitable for the
known as information bottleneck [59], and its schematic di-           target task, it also overcomes the problems encountered by
agram is as shown in Figure 2. At present, the main meth-             mask modeling. The proposed PGI mechanism can be ap-
ods that can alleviate this phenomenon are as follows: (1)            plied to deep neural networks of various sizes and is more
The use of reversible architectures [3, 16, 19]: this method          general than the deep supervision mechanism, which is only
mainly uses repeated input data and maintains the informa-            suitable for very deep neural networks.
tion of the input data in an explicit way; (2) The use of                In this paper, we also designed generalized ELAN
masked modeling [1, 6, 9, 27, 71, 73]: it mainly uses recon-          (GELAN) based on ELAN [65], the design of GELAN si-
struction loss and adopts an implicit way to maximize the             multaneously takes into account the number of parameters,
extracted features and retain the input information; and (3)          computational complexity, accuracy and inference speed.
Introduction of the deep supervision concept [28,51,54,68]:           This design allows users to arbitrarily choose appropriate
it uses shallow features that have not lost too much impor-           computational blocks for different inference devices. We
tant information to pre-establish a mapping from features             combined the proposed PGI and GELAN, and then de-
to targets to ensure that important information can be trans-         signed a new generation of YOLO series object detection
ferred to deeper layers. However, the above methods have              system, which we call YOLOv9. We used the MS COCO
different drawbacks in the training process and inference             dataset to conduct experiments, and the experimental results
process. For example, a reversible architecture requires ad-          verified that our proposed YOLOv9 achieved the top perfor-
ditional layers to combine repeatedly fed input data, which           mance in all comparisons.
will significantly increase the inference cost. In addition,             We summarize the contributions of this paper as follows:
since the input data layer to the output layer cannot have a
                                                                        1. We theoretically analyzed the existing deep neural net-
too deep path, this limitation will make it difficult to model
                                                                           work architecture from the perspective of reversible
high-order semantic information during the training pro-
                                                                           function, and through this process we successfully ex-
cess. As for masked modeling, its reconstruction loss some-
                                                                           plained many phenomena that were difficult to explain
times conflicts with the target loss. In addition, most mask
                                                                           in the past. We also designed PGI and auxiliary re-
mechanisms also produce incorrect associations with data.
                                                                           versible branch based on this analysis and achieved ex-
For the deep supervision mechanism, it will produce error
                                                                           cellent results.
accumulation, and if the shallow supervision loses informa-
tion during the training process, the subsequent layers will            2. The PGI we designed solves the problem that deep su-
not be able to retrieve the required information. The above                pervision can only be used for extremely deep neu-
phenomenon will be more significant on difficult tasks and                 ral network architectures, and therefore allows new
small models.                                                              lightweight architectures to be truly applied in daily
    To address the above-mentioned issues, we propose a                    life.
new concept, which is programmable gradient information                 3. The GELAN we designed only uses conventional con-
(PGI). The concept is to generate reliable gradients through               volution to achieve a higher parameter usage than the
auxiliary reversible branch, so that the deep features can                 depth-wise convolution design that based on the most
still maintain key characteristics for executing target task.              advanced technology, while showing great advantages
The design of auxiliary reversible branch can avoid the se-                of being light, fast, and accurate.
mantic loss that may be caused by a traditional deep super-
                                                                        4. Combining the proposed PGI and GELAN, the object
vision process that integrates multi-path features. In other
                                                                           detection performance of the YOLOv9 on MS COCO
words, we are programming gradient information propaga-
                                                                           dataset greatly surpasses the existing real-time object
tion at different semantic levels, and thereby achieving the
                                                                           detectors in all aspects.
best training results. The reversible architecture of PGI is

                                                                  2
2. Related work                                                      2.3. Auxiliary Supervision
2.1. Real-time Object Detectors                                          Deep supervision [28, 54, 68] is the most common auxil-
   The current mainstream real-time object detectors are the         iary supervision method, which performs training by insert-
YOLO series [2, 7, 13–15, 25, 30, 31, 47–49, 61–63, 74, 75],         ing additional prediction layers in the middle layers. Es-
and most of these models use CSPNet [64] or ELAN [65]                pecially the application of multi-layer decoders introduced
and their variants as the main computing units. In terms of          in the transformer-based methods is the most common one.
feature integration, improved PAN [37] or FPN [35] is of-            Another common auxiliary supervision method is to utilize
ten used as a tool, and then improved YOLOv3 head [49] or            the relevant meta information to guide the feature maps pro-
FCOS head [57, 58] is used as prediction head. Recently              duced by the intermediate layers and make them have the
some real-time object detectors, such as RT DETR [43],               properties required by the target tasks [18, 20, 24, 29, 76].
which puts its fundation on DETR [4], have also been pro-            Examples of this type include using segmentation loss or
posed. However, since it is extremely difficult for DETR             depth loss to enhance the accuracy of object detectors. Re-
series object detector to be applied to new domains without          cently, there are many reports in the literature [53, 67, 82]
a corresponding domain pre-trained model, the most widely            that use different label assignment methods to generate dif-
used real-time object detector at present is still YOLO se-          ferent auxiliary supervision mechanisms to speed up the
ries. This paper chooses YOLOv7 [63], which has been                 convergence speed of the model and improve the robustness
proven effective in a variety of computer vision tasks and           at the same time. However, the auxiliary supervision mech-
                                                                     anism is usually only applicable to large models, so when
various scenarios, as a base to develop the proposed method.
We use GELAN to improve the architecture and the training            it is applied to lightweight models, it is easy to cause an
process with the proposed PGI. The above novel approach              under parameterization phenomenon, which makes the per-
makes the proposed YOLOv9 the top real-time object de-               formance worse. The PGI we proposed designed a way to
tector of the new generation.                                        reprogram multi-level semantic information, and this design
                                                                     allows lightweight models to also benefit from the auxiliary
2.2. Reversible Architectures                                        supervision mechanism.
    The operation unit of reversible architectures [3, 16, 19]
must maintain the characteristics of reversible conversion,          3. Problem Statement
so it can be ensured that the output feature map of each
                                                                         Usually, people attribute the difficulty of deep neural net-
layer of operation unit can retain complete original informa-
                                                                     work convergence problem due to factors such as gradient
tion. Before, RevCol [3] generalizes traditional reversible
                                                                     vanish or gradient saturation, and these phenomena do ex-
unit to multiple levels, and in doing so can expand the se-
                                                                     ist in traditional deep neural networks. However, modern
mantic levels expressed by different layer units. Through
                                                                     deep neural networks have already fundamentally solved
a literature review of various neural network architectures,
                                                                     the above problem by designing various normalization and
we found that there are many high-performing architectures
                                                                     activation functions. Nevertheless, deep neural networks
with varying degree of reversible properties. For exam-
                                                                     still have the problem of slow convergence or poor conver-
ple, Res2Net module [11] combines different input parti-
                                                                     gence results.
tions with the next partition in a hierarchical manner, and
                                                                         In this paper, we explore the nature of the above issue
concatenates all converted partitions before passing them
                                                                     further. Through in-depth analysis of information bottle-
backwards. CBNet [34, 39] re-introduces the original in-
                                                                     neck, we deduced that the root cause of this problem is that
put data through composite backbone to obtain complete
                                                                     the initial gradient originally coming from a very deep net-
original information, and obtains different levels of multi-
                                                                     work has lost a lot of information needed to achieve the
level reversible information through various composition
                                                                     goal soon after it is transmitted. In order to confirm this
methods. These network architectures generally have ex-
                                                                     inference, we feedforward deep networks of different archi-
cellent parameter utilization, but the extra composite layers
                                                                     tectures with initial weights, and then visualize and illus-
cause slow inference speeds. DynamicDet [36] combines
                                                                     trate them in Figure 2. Obviously, PlainNet has lost a lot of
CBNet [34] and the high-efficiency real-time object detec-
                                                                     important information required for object detection in deep
tor YOLOv7 [63] to achieve a very good trade-off among
                                                                     layers. As for the proportion of important information that
speed, number of parameters, and accuracy. This paper in-
                                                                     ResNet, CSPNet, and GELAN can retain, it is indeed posi-
troduces the DynamicDet architecture as the basis for de-
                                                                     tively related to the accuracy that can be obtained after train-
signing reversible branches. In addition, reversible infor-
                                                                     ing. We further design reversible network-based methods to
mation is further introduced into the proposed PGI. The
                                                                     solve the causes of the above problems. In this section we
proposed new architecture does not require additional con-
                                                                     shall elaborate our analysis of information bottleneck prin-
nections during the inference process, so it can fully retain
                                                                     ciple and reversible functions.
the advantages of speed, parameter amount, and accuracy.

                                                                 3
3.1. Information Bottleneck Principle                                deep learning methods are architectures that conform to the
                                                                     reversible property, such as Eq. 4.
   According to information bottleneck principle, we know
that data X may cause information loss when going through
                                                                                      X l+1 = X l + fθl+1 (X l ),               (4)
transformation, as shown in Eq. 1 below:
                                                                     where l indicates the l-th layer of a PreAct ResNet and
                                                                     f is the transformation function of the l-th layer. PreAct
      I(X, X) ≥ I(X, fθ (X)) ≥ I(X, gϕ (fθ (X))),         (1)        ResNet [22] repeatedly passes the original data X to sub-
where I indicates mutual information, f and g are transfor-          sequent layers in an explicit way. Although such a design
mation functions, and θ and ϕ are parameters of f and g,             can make a deep neural network with more than a thousand
respectively.                                                        layers converge very well, it destroys an important reason
    In deep neural networks, fθ (·) and gϕ (·) respectively          why we need deep neural networks. That is, for difficult
represent the operations of two consecutive layers in deep           problems, it is difficult for us to directly find simple map-
neural network. From Eq. 1, we can predict that as the num-          ping functions to map data to targets. This also explains
ber of network layer becomes deeper, the original data will          why PreAct ResNet performs worse than ResNet [21] when
be more likely to be lost. However, the parameters of the            the number of layers is small.
deep neural network are based on the output of the network              In addition, we tried to use masked modeling that al-
as well as the given target, and then update the network after       lowed the transformer model to achieve significant break-
generating new gradients by calculating the loss function.           throughs. We use approximation methods, such as Eq. 5,
As one can imagine, the output of a deeper neural network            to try to find the inverse transformation v of r, so that the
is less able to retain complete information about the pre-           transformed features can retain enough information using
diction target. This will make it possible to use incomplete         sparse features. The form of Eq. 5 is as follows:
information during network training, resulting in unreliable
gradients and poor convergence.                                                         X = vζ (rψ (X) · M ),                   (5)
    One way to solve the above problem is to directly in-            where M is a dynamic binary mask. Other methods that
crease the size of the model. When we use a large number             are commonly used to perform the above tasks are diffusion
of parameters to construct a model, it is more capable of            model and variational autoencoder, and they both have the
performing a more complete transformation of the data. The           function of finding the inverse function. However, when
above approach allows even if information is lost during the         we apply the above approach to a lightweight model, there
data feedforward process, there is still a chance to retain          will be defects because the lightweight model will be under
enough information to perform the mapping to the target.             parameterized to a large amount of raw data. Because of
The above phenomenon explains why the width is more im-              the above reason, important information I(Y, X) that maps
portant than the depth in most modern models. However,               data X to target Y will also face the same problem. For this
the above conclusion cannot fundamentally solve the prob-            issue, we will explore it using the concept of information
lem of unreliable gradients in very deep neural network.             bottleneck [59]. The formula for information bottleneck is
Below, we will introduce how to use reversible functions             as follows:
to solve problems and conduct relative analysis.
3.2. Reversible Functions                                             I(X, X) ≥ I(Y, X) ≥ I(Y, fθ (X)) ≥ ... ≥ I(Y, Ŷ ). (6)
   When a function r has an inverse transformation func-
tion v, we call this function reversible function, as shown in       Generally speaking, I(Y, X) will only occupy a very small
Eq. 2.                                                               part of I(X, X). However, it is critical to the target mis-
                                                                     sion. Therefore, even if the amount of information lost in
                     X = vζ (rψ (X)),                     (2)        the feedforward stage is not significant, as long as I(Y, X)
                                                                     is covered, the training effect will be greatly affected. The
where ψ and ζ are parameters of r and v, respectively. Data          lightweight model itself is in an under parameterized state,
X is converted by reversible function without losing infor-          so it is easy to lose a lot of important information in the
mation, as shown in Eq. 3.                                           feedforward stage. Therefore, our goal for the lightweight
                                                                     model is how to accurately filter I(Y, X) from I(X, X). As
      I(X, X) = I(X, rψ (X)) = I(X, vζ (rψ (X))).         (3)        for fully preserving the information of X, that is difficult to
                                                                     achieve. Based on the above analysis, we hope to propose a
When the network’s transformation function is composed               new deep neural network training method that can not only
of reversible functions, more reliable gradients can be ob-          generate reliable gradients to update the model, but also be
tained to update the model. Almost all of today’s popular            suitable for shallow and lightweight neural networks.

                                                                 4
Figure 3. PGI and related network architectures and methods. (a) Path Aggregation Network (PAN)) [37], (b) Reversible Columns
(RevCol) [3], (c) conventional deep supervision, and (d) our proposed Programmable Gradient Information (PGI). PGI is mainly composed
of three components: (1) main branch: architecture used for inference, (2) auxiliary reversible branch: generate reliable gradients to supply
main branch for backward transmission, and (3) multi-level auxiliary information: control main branch learning plannable multi-level of
semantic information.

4. Methodology                                                           pose the maintenance of complete information by introduc-
                                                                         ing reversible architecture, but adding main branch to re-
4.1. Programmable Gradient Information                                   versible architecture will consume a lot of inference costs.
   In order to solve the aforementioned problems, we pro-                We analyzed the architecture of Figure 3 (b) and found that
pose a new auxiliary supervision framework called Pro-                   when additional connections from deep to shallow layers
grammable Gradient Information (PGI), as shown in Fig-                   are added, the inference time will increase by 20%. When
ure 3 (d). PGI mainly includes three components, namely                  we repeatedly add the input data to the high-resolution com-
(1) main branch, (2) auxiliary reversible branch, and (3)                puting layer of the network (yellow box), the inference time
multi-level auxiliary information. From Figure 3 (d) we                  even exceeds twice the time.
see that the inference process of PGI only uses main branch                 Since our goal is to use reversible architecture to ob-
and therefore does not require any additional inference cost.            tain reliable gradients, “reversible” is not the only neces-
As for the other two components, they are used to solve or               sary condition in the inference stage. In view of this, we
slow down several important issues in deep learning meth-                regard reversible branch as an expansion of deep supervi-
ods. Among them, auxiliary reversible branch is designed                 sion branch, and then design auxiliary reversible branch, as
to deal with the problems caused by the deepening of neural              shown in Figure 3 (d). As for the main branch deep fea-
networks. Network deepening will cause information bot-                  tures that would have lost important information due to in-
tleneck, which will make the loss function unable to gener-              formation bottleneck, they will be able to receive reliable
ate reliable gradients. As for multi-level auxiliary informa-            gradient information from the auxiliary reversible branch.
tion, it is designed to handle the error accumulation problem            These gradient information will drive parameter learning to
caused by deep supervision, especially for the architecture              assist in extracting correct and important information, and
and lightweight model of multiple prediction branch. Next,               the above actions can enable the main branch to obtain fea-
we will introduce these two components step by step.                     tures that are more effective for the target task. Moreover,
                                                                         the reversible architecture performs worse on shallow net-
4.1.1   Auxiliary Reversible Branch                                      works than on general networks because complex tasks re-
                                                                         quire conversion in deeper networks. Our proposed method
In PGI, we propose auxiliary reversible branch to gener-                 does not force the main branch to retain complete origi-
ate reliable gradients and update network parameters. By                 nal information but updates it by generating useful gradient
providing information that maps from data to targets, the                through the auxiliary supervision mechanism. The advan-
loss function can provide guidance and avoid the possibil-               tage of this design is that the proposed method can also be
ity of finding false correlations from incomplete feedfor-               applied to shallower networks.
ward features that are less relevant to the target. We pro-

                                                                     5
Figure 4. The architecture of GELAN: (a) CSPNet [64], (b) ELAN [65], and (c) proposed GELAN. We imitate CSPNet and extend ELAN
into GELAN that can support any computational blocks.
   Finally, since auxiliary reversible branch can be removed         4.2. Generalized ELAN
during the inference phase, the inference capabilities of the
                                                                        In this Section we describe the proposed new network
original network can be retained. We can also choose any
                                                                     architecture – GELAN. By combining two neural network
reversible architectures in PGI to play the role of auxiliary
                                                                     architectures, CSPNet [64] and ELAN [65], which are de-
reversible branch.
                                                                     signed with gradient path planning, we designed gener-
4.1.2 Multi-level Auxiliary Information                              alized efficient layer aggregation network (GELAN) that
In this section we will discuss how multi-level auxiliary in-        takes into account lighweight, inference speed, and accu-
formation works. The deep supervision architecture includ-           racy. Its overall architecture is shown in Figure 4. We gen-
ing multiple prediction branch is shown in Figure 3 (c). For         eralized the capability of ELAN [65], which originally only
object detection, different feature pyramids can be used to          used stacking of convolutional layers, to a new architecture
perform different tasks, for example together they can de-           that can use any computational blocks.
tect objects of different sizes. Therefore, after connecting
to the deep supervision branch, the shallow features will be         5. Experiments
guided to learn the features required for small object detec-        5.1. Experimental Setup
tion, and at this time the system will regard the positions
of objects of other sizes as the background. However, the               We verify the proposed method with MS COCO dataset.
above deed will cause the deep feature pyramids to lose a lot        All experimental setups follow YOLOv7 AF [63], while the
of information needed to predict the target object. Regard-          dataset is MS COCO 2017 splitting. All models we men-
ing this issue, we believe that each feature pyramid needs           tioned are trained using the train-from-scratch strategy, and
to receive information about all target objects so that subse-       the total number of training times is 500 epochs. In setting
quent main branch can retain complete information to learn           the learning rate, we use linear warm-up in the first three
predictions for various targets.                                     epochs, and the subsequent epochs set the corresponding
    The concept of multi-level auxiliary information is to in-       decay manner according to the model scale. As for the last
sert an integration network between the feature pyramid hi-          15 epochs, we turn mosaic data augmentation off. For more
erarchy layers of auxiliary supervision and the main branch,         settings, please refer to Appendix.
and then uses it to combine returned gradients from differ-
                                                                     5.2. Implimentation Details
ent prediction heads, as shown in Figure 3 (d). Multi-level
auxiliary information is then to aggregate the gradient infor-          We built general and extended version of YOLOv9 based
mation containing all target objects, and pass it to the main        on YOLOv7 [63] and Dynamic YOLOv7 [36] respectively.
branch and then update parameters. At this time, the charac-         In the design of the network architecture, we replaced
teristics of the main branch’s feature pyramid hierarchy will        ELAN [65] with GELAN using CSPNet blocks [64] with
not be dominated by some specific object’s information. As           planned RepConv [63] as computational blocks. We also
a result, our method can alleviate the broken information            simplified downsampling module and optimized anchor-
problem in deep supervision. In addition, any integrated             free prediction head. As for the auxiliary loss part of PGI,
network can be used in multi-level auxiliary information.            we completely follow YOLOv7’s auxiliary head setting.
Therefore, we can plan the required semantic levels to guide         Please see Appendix for more details.
the learning of network architectures of different sizes.

                                                                 6
                               Table 1. Comparison of state-of-the-art real-time object detectors.
     Model                #Param. (M)   FLOPs (G)   APval
                                                      50:95 (%)     APval
                                                                      50 (%)   APval
                                                                                 75 (%)     APval
                                                                                              S (%)   APval
                                                                                                        M (%)     APval
                                                                                                                    L (%)
     YOLOv5-N r7.0 [14]       1.9           4.5         28.0          45.7          –           –          –           –
     YOLOv5-S r7.0 [14]       7.2          16.5         37.4          56.8          –           –          –           –
     YOLOv5-M r7.0 [14]      21.2          49.0         45.4          64.1          –           –          –           –
     YOLOv5-L r7.0 [14]      46.5         109.1         49.0          67.3          –           –          –           –
     YOLOv5-X r7.0 [14]      86.7         205.7         50.7          68.9          –           –          –           –
     YOLOv6-N v3.0 [30]       4.7          11.4         37.0          52.7          –           –          –           –
     YOLOv6-S v3.0 [30]      18.5          45.3         44.3          61.2          –           –          –           –
     YOLOv6-M v3.0 [30]      34.9          85.8         49.1          66.1          –           –          –           –
     YOLOv6-L v3.0 [30]      59.6         150.7         51.8          69.2          –           –          –           –
     YOLOv7 [63]             36.9         104.7         51.2          69.7        55.9         31.8      55.5        65.0
     YOLOv7-X [63]           71.3         189.9         52.9          71.1        51.4         36.9      57.7        68.6
     YOLOv7-N AF [63]         3.1           8.7         37.6          53.3        40.6         18.7      41.7        52.8
     YOLOv7-S AF [63]        11.0          28.1         45.1          61.8        48.9         25.7      50.2        61.2
     YOLOv7 AF [63]          43.6         130.5         53.0          70.2        57.5         35.8      58.7        68.9
     YOLOv8-N [15]            3.2           8.7         37.3          52.6         –            –         –           –
     YOLOv8-S [15]           11.2          28.6         44.9          61.8         –            –         –           –
     YOLOv8-M [15]           25.9          78.9         50.2          67.2         –            –         –           –
     YOLOv8-L [15]           43.7         165.2         52.9          69.8        57.5         35.3      58.3        69.8
     YOLOv8-X [15]           68.2         257.8         53.9          71.0        58.7         35.7      59.3        70.7
     DAMO YOLO-T [75]         8.5         18.1          42.0          58.0        45.2         23.0      46.1        58.5
     DAMO YOLO-S [75]        12.3         37.8          46.0          61.9        49.5         25.9      50.6        62.5
     DAMO YOLO-M [75]        28.2         61.8          49.2          65.5        53.0         29.7      53.1        66.1
     DAMO YOLO-L [75]        42.1         97.3          50.8          67.5        55.5         33.2      55.7        66.6
     Gold YOLO-N [61]         5.6          12.1         39.6          55.7          –          19.7      44.1        57.0
     Gold YOLO-S [61]        21.5          46.0         45.4          62.5          –          25.3      50.2        62.6
     Gold YOLO-M [61]        41.3          87.5         49.8          67.0          –          32.3      55.3        66.3
     Gold YOLO-L [61]        75.1         151.7         51.8          68.9          –          34.1      57.4        68.2
     YOLO MS-N [7]            4.5         17.4          43.4          60.4        47.6         23.7      48.3        60.3
     YOLO MS-S [7]            8.1         31.2          46.2          63.7        50.5         26.9      50.5        63.0
     YOLO MS [7]             22.2         80.2          51.0          68.6        55.7         33.1      56.1        66.5
     GELAN-S (Ours)           7.1          26.4         46.7          63.0        50.7         25.9      51.5        64.0
     GELAN-M (Ours)          20.0          76.3         51.1          67.9        55.7         33.6      56.4        67.3
     GELAN-C (Ours)          25.3         102.1         52.5          69.5        57.3         35.8      57.6        69.4
     GELAN-E (Ours)          57.3         189.0         55.0          71.9        60.0         38.0      60.6        70.9
     YOLOv9-S (Ours)          7.1          26.4         46.8          63.4        50.7         26.6      56.0        64.5
     YOLOv9-M (Ours)         20.0          76.3         51.4          68.1        56.1         33.6      57.0        68.0
     YOLOv9-C (Ours)         25.3         102.1         53.0          70.2        57.8         36.2      58.5        69.3
     YOLOv9-E (Ours)         57.3         189.0         55.6          72.8        60.6         40.2      61.0        71.4

5.3. Comparison with state-of-the-arts                              improved in all aspects compared with existing methods.
    Table 1 lists comparison of our proposed YOLOv9 with               On the other hand, we also include ImageNet pretrained
other train-from-scratch real-time object detectors. Over-          model in the comparison, and the results are shown in Fig-
all, the best performing methods among existing methods             ure 5. We compare them based on the parameters and the
are YOLO MS-S [7] for lightweight models, YOLO MS [7]               amount of computation respectively. In terms of the num-
for medium models, YOLOv7 AF [63] for general mod-                  ber of parameters, the best performing large model is RT
els, and YOLOv8-X [15] for large models. Compared with              DETR [43]. From Figure 5, we can see that YOLOv9 using
lightweight and medium model YOLO MS [7], YOLOv9                    conventional convolution is even better than YOLO MS us-
has about 10% less parameters and 5∼15% less calcula-               ing depth-wise convolution in parameter utilization. As for
tions, but still has a 0.4∼0.6% improvement in AP. Com-             the parameter utilization of large models, it also greatly sur-
pared with YOLOv7 AF, YOLOv9-C has 42% less pa-                     passes RT DETR using ImageNet pretrained model. Even
rameters and 22% less calculations, but achieves the same           better is that in the deep model, YOLOv9 shows the huge
AP (53%). Compared with YOLOv8-X, YOLOv9-E has                      advantages of using PGI. By accurately retaining and ex-
16% less parameters, 27% less calculations, and has sig-            tracting the information needed to map the data to the tar-
nificant improvement of 1.7% AP. The above comparison               get, our method requires only 66% of the parameters while
results show that our proposed YOLOv9 has significantly             maintaining the accuracy as RT DETR-X.

                                                                7
Figure 5. Comparison of state-of-the-art real-time object detectors. The methods participating in the comparison all use ImageNet as
pre-trained weights, including RT DETR [43], RTMDet [44], and PP-YOLOE [74], etc. The YOLOv9 that uses train-from-scratch method
clearly surpasses the performance of other methods.

    As for the amount of computation, the best existing mod-            Next, we conduct ELAN block-depth and CSP block-
els from the smallest to the largest are YOLO MS [7], PP             depth experiments on GELAN of different sizes, and dis-
YOLOE [74], and RT DETR [43]. From Figure 5, we can                  play the results in Table 3. We can see that when the depth
see that YOLOv9 is far superior to the train-from-scratch            of ELAN is increased from 1 to 2, the accuracy is signif-
methods in terms of computational complexity. In addi-               icantly improved. But when the depth is greater than or
tion, if compared with those based on depth-wise convo-              equal to 2, no matter it is improving the ELAN depth or the
lution and ImageNet-based pretrained models, YOLOv9 is               CSP depth, the number of parameters, the amount of com-
also very competitive.                                               putation, and the accuracy will always show a linear rela-
                                                                     tionship. This means GELAN is not sensitive to the depth.
5.4. Ablation Studies                                                In other words, users can arbitrarily combine the compo-
5.4.1     Generalized ELAN                                           nents in GELAN to design the network architecture, and
                                                                     have a model with stable performance without special de-
For GELAN, we first do ablation studies for computational            sign. In Table 3, for YOLOv9-{S,M,C}, we set the pairing
blocks. We used Res blocks [21], Dark blocks [49], and               of the ELAN depth and the CSP depth to {{2, 3}, {2, 1},
CSP blocks [64] to conduct experiments, respectively. Ta-            {2, 1}}.
ble 2 shows that after replacing convolutional layers in
ELAN with different computational blocks, the system can                    Table 3. Ablation study on ELAN and CSP depth.
maintain good performance. Users are indeed free to re-                Model       DELAN      DCSP     #Param.    FLOPs    APval
                                                                                                                             50:95
place computational blocks and use them on their respective
                                                                       GELAN-S         2         1       5.9M     22.4G     45.5%
inference devices. Among different computational block re-             GELAN-S         2         2       6.5M     24.4G     46.0%
placements, CSP blocks perform particularly well. They                 GELAN-S         3         1       7.1M     26.3G     46.5%
not only reduce the amount of parameters and computation,              GELAN-S         2         3       7.1M     26.4G     46.7%
but also improve AP by 0.7%. Therefore, we choose CSP-                 GELAN-M         2         1      20.0M     76.3G     51.1%
ELAN as the component unit of GELAN in YOLOv9.                         GELAN-M         2         2      22.2M     85.1G     51.7%
                                                                       GELAN-M         3         1      24.3M     93.5G     51.8%
    Table 2. Ablation study on various computational blocks.           GELAN-M         2         3      24.4M     94.0G     52.3%

        Model       CB type         #Param.   FLOPs   APval            GELAN-C         1         1      18.9M      77.5G    50.7%
                                                        50:95
                                                                       GELAN-C         2         1      25.3M     102.1G    52.5%
        GELAN-S     Conv             6.2M     23.5G   44.8%            GELAN-C         2         2      28.6M     114.4G    53.0%
        GELAN-S    Res [21]          5.4M     21.0G   44.3%            GELAN-C         3         1      31.7M     126.8G    53.2%
        GELAN-S    Dark [49]         5.7M     21.8G   44.5%            GELAN-C         2         3      31.9M     126.7G    53.3%
        GELAN-S    CSP [64]          5.9M     22.4G   45.5%          1D
                                                                         ELAN and DCSP respectively nedotes depth of ELAN and CSP.
   1 CB type nedotes as computational block type.                    2 -{S, M, C} indicate small, medium, and compact models.
   2 -S nedotes small size model.

                                                                 8
5.4.2     Programmable Gradient Information                                               Table 5. Ablation study on PGI.
                                                                           Model          APval
                                                                                             50:95           APval
                                                                                                                50            APval
                                                                                                                                 75
In terms of PGI, we performed ablation studies on auxiliary                GELAN-S         46.7%             63.0%            50.7%
reversible branch and multi-level auxiliary information on                 + DS            46.5%      -0.2   62.9%    -0.1    50.5%     -0.2
the backbone and neck, respectively. We designed auxiliary                 + PGI           46.8%      +0.1   63.4%    +0.4    50.7%      =
reversible branch ICN to use DHLC [34] linkage to obtain                   GELAN-M        51.1%              67.9%            55.7%
multi-level reversible information. As for multi-level aux-                + DS           51.2%       +0.1   68.2%    +0.3    55.7%      =
                                                                           + PGI          51.4%       +0.3   68.1%    +0.2    56.1%     +0.4
iliary information, we use FPN and PAN for ablation stud-
ies and the role of PFH is equivalent to the traditional deep              GELAN-C        52.5%              69.5%            57.3%
                                                                           + DS           52.5%        =     69.9%    +0.4    57.1%     -0.2
supervision. The results of all experiments are listed in Ta-
                                                                           + PGI          53.0%       +0.5   70.3%    +0.8    57.8%     +0.5
ble 4. From Table 4, we can see that PFH is only effective in
                                                                           GELAN-E        55.0%              71.9%            60.0%
deep models, while our proposed PGI can improve accuracy
                                                                           + DS           55.3%       +0.3   72.3%    +0.4    60.2%     +0.2
under different combinations. Especially when using ICN,                   + PGI          55.6%       +0.6   72.8%    +0.9    60.6%     +0.6
we get stable and better results. We also tried to apply the             1 DS indicates deep supervision.
lead-head guided assignment proposed in YOLOv7 [63] to                   2 -{S, M, C, E} indicate small, medium, compact, and extended models.
the PGI’s auxiliary supervision, and achieved much better
performance.
                                                                            Finally, we show in the table the results of gradually in-
        Table 4. Ablation study on PGI of backbone and neck.             creasing components from baseline YOLOv7 to YOLOv9-
 Model   Gbackbone Gneck APval
                            50:95           APval
                                               S    APval
                                                       M    APval
                                                               L
                                                                         E. The GELAN and PGI we proposed have brought all-
 GELAN-C     –       –    52.5%             35.8%   57.6%   69.4%        round improvement to the model.
 GELAN-C   PFH       –    52.5%             35.3%   58.1%   68.9%
 GELAN-C   FPN       –    52.6%             35.3%   58.1%   68.9%                  Table 6. Ablation study on GELAN and PGI.
 GELAN-C     –      ICN   52.7%             35.3%   58.4%   68.9%
 GELAN-C   FPN      ICN   52.8%             35.8%   58.2%   69.1%         Model       #Param. FLOPs APval
                                                                                                       50:95          APval
                                                                                                                         S    APval
                                                                                                                                 M     APval
                                                                                                                                          L
 GELAN-C   ICN       –    52.9%             35.2%   58.7%   68.6%         YOLOv7 [63]   36.9   104.7 51.2%            31.8%   55.5%    65.0%
 GELAN-C LHG-ICN     –    53.0%             36.3%   58.5%   69.1%         + AF [63]     43.6   130.5 53.0%            35.8%   58.7%    68.9%
                                                                          + GELAN       41.2   126.4 53.2%            36.2%   58.5%    69.9%
 GELAN-E           –        –      55.0%    38.0%   60.6%   70.9%
                                                                          + DHLC [34]   57.3   189.0 55.0%            38.0%   60.6%    70.9%
 GELAN-E          PFH       –      55.3%    38.3%   60.3%   71.6%
                                                                          + PGI         57.3   189.0 55.6%            40.2%   61.0%    71.4%
 GELAN-E          FPN       –      55.6%    40.2%   61.0%   71.4%
 GELAN-E          PAN       –      55.5%    39.0%   61.1%   71.5%
 GELAN-E          FPN      ICN     55.6%    39.8%   60.9%   71.9%
1D
   ELAN and DCSP respectively nedotes depth of ELAN and CSP.
                                                                         5.5. Visualization
2 LHG indicates lead head guided training proposed by YOLOv7 [63].
                                                                            This section will explore the information bottleneck is-
                                                                         sues and visualize them. In addition, we will also visualize
    We further implemented the concepts of PGI and deep
                                                                         how the proposed PGI uses reliable gradients to find the
supervision on models of various sizes and compared the
                                                                         correct correlations between data and targets. In Figure 6
results, these results are shown in Table 5. As analyzed at
                                                                         we show the visualization results of feature maps obtained
the beginning, introduction of deep supervision will cause
                                                                         by using random initial weights as feedforward under dif-
a loss of accuracy for shallow models. As for general mod-
                                                                         ferent architectures. We can see that as the number of lay-
els, introducing deep supervision will cause unstable perfor-
                                                                         ers increases, the original information of all architectures
mance, and the design concept of deep supervision can only
                                                                         gradually decreases. For example, at the 50th layer of the
bring gains in extremely deep models. The proposed PGI
                                                                         PlainNet, it is difficult to see the location of objects, and all
can effectively handle problems such as information bottle-
                                                                         distinguishable features will be lost at the 100th layer. As
neck and information broken, and can comprehensively im-
                                                                         for ResNet, although the position of object can still be seen
prove the accuracy of models of different sizes. The concept
                                                                         at the 50th layer, the boundary information has been lost.
of PGI brings two valuable contributions. The first one is to
                                                                         When the depth reached to the 100th layer, the whole image
make the auxiliary supervision method applicable to shal-
                                                                         becomes blurry. Both CSPNet and the proposed GELAN
low models, while the second one is to make the deep model
                                                                         perform very well, and they both can maintain features that
training process obtain more reliable gradients. These gra-
                                                                         support clear identification of objects until the 200th layer.
dients enable deep models to use more accurate information
                                                                         Among the comparisons, GELAN has more stable results
to establish correct correlations between data and targets.
                                                                         and clearer boundary information.

                                                                     9
Figure 6. Feature maps (visualization results) output by random initial weights of PlainNet, ResNet, CSPNet, and GELAN at different
depths. After 100 layers, ResNet begins to produce feedforward output that is enough to obfuscate object information. Our proposed
GELAN can still retain quite complete information up to the 150th layer, and is still sufficiently discriminative up to the 200th layer.
                                                                           ject boundaries, and it also produced unexpected responses
                                                                           in some background areas. This experiment confirms that
                                                                           PGI can indeed provide better gradients to update parame-
                                                                           ters and enable the feedforward stage of the main branch to
                                                                           retain more important features.

                                                                           6. Conclusions
                                                                               In this paper, we propose to use PGI to solve the infor-
                                                                           mation bottleneck problem and the problem that the deep
                                                                           supervision mechanism is not suitable for lightweight neu-
                                                                           ral networks. We designed GELAN, a highly efficient
                                                                           and lightweight neural network. In terms of object detec-
                                                                           tion, GELAN has strong and stable performance at different
                                                                           computational blocks and depth settings. It can indeed be
Figure 7. PAN feature maps (visualization results) of GELAN                widely expanded into a model suitable for various inference
and YOLOv9 (GELAN + PGI) after one epoch of bias warm-up.                  devices. For the above two issues, the introduction of PGI
GELAN originally had some divergence, but after adding PGI’s               allows both lightweight models and deep models to achieve
reversible branch, it is more capable of focusing on the target ob-        significant improvements in accuracy. The YOLOv9, de-
ject.                                                                      signed by combining PGI and GELAN, has shown strong
    Figure 7 is used to show whether PGI can provide more                  competitiveness. Its excellent design allows the deep model
reliable gradients during the training process, so that the                to reduce the number of parameters by 49% and the amount
parameters used for updating can effectively capture the                   of calculations by 43% compared with YOLOv8, but it still
relationship between the input data and the target. Fig-                   has a 0.6% AP improvement on MS COCO dataset.
ure 7 shows the visualization results of the feature map of
GELAN and YOLOv9 (GELAN + PGI) in PAN bias warm-                           7. Acknowledgements
up. From the comparison of Figure 7(b) and (c), we can
                                                                              The authors wish to thank National Center for High-
clearly see that PGI accurately and concisely captures the
                                                                           performance Computing (NCHC) for providing computa-
area containing objects. As for GELAN that does not use
                                                                           tional and storage resources.
PGI, we found that it had divergence when detecting ob-

                                                                      10
References                                                                [14] Jocher Glenn. YOLOv5 release v7.0. https://github.
                                                                               com/ultralytics/yolov5/releases/tag/v7.
 [1] Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. BEiT:                    0, 2022. 3, 7
     BERT pre-training of image transformers. In International
                                                                          [15] Jocher Glenn.       YOLOv8 release v8.1.0.          https :
     Conference on Learning Representations (ICLR), 2022. 2
                                                                               / / github . com / ultralytics / ultralytics /
 [2] Alexey Bochkovskiy, Chien-Yao Wang, and Hong-                             releases/tag/v8.1.0, 2024. 3, 7
     Yuan Mark Liao. YOLOv4: Optimal speed and accuracy of
                                                                          [16] Aidan N Gomez, Mengye Ren, Raquel Urtasun, and Roger B
     object detection. arXiv preprint arXiv:2004.10934, 2020. 3
                                                                               Grosse. The reversible residual network: Backpropagation
 [3] Yuxuan Cai, Yizhuang Zhou, Qi Han, Jianjian Sun, Xiang-
                                                                               without storing activations. Advances in Neural Information
     wen Kong, Jun Li, and Xiangyu Zhang. Reversible column
                                                                               Processing Systems (NeurIPS), 2017. 2, 3
     networks. In International Conference on Learning Repre-
                                                                          [17] Albert Gu and Tri Dao. Mamba: Linear-time sequence
     sentations (ICLR), 2023. 2, 3, 5
                                                                               modeling with selective state spaces.         arXiv preprint
 [4] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas
                                                                               arXiv:2312.00752, 2023. 1
     Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-
     to-end object detection with transformers. In Proceedings            [18] Chaoxu Guo, Bin Fan, Qian Zhang, Shiming Xiang, and
     of the European Conference on Computer Vision (ECCV),                     Chunhong Pan.        AugFPN: Improving multi-scale fea-
     pages 213–229, 2020. 3                                                    ture learning for object detection. In Proceedings of the
                                                                               IEEE/CVF Conference on Computer Vision and Pattern
 [5] Kean Chen, Weiyao Lin, Jianguo Li, John See, Ji Wang, and
                                                                               Recognition (CVPR), pages 12595–12604, 2020. 1, 3
     Junni Zou. AP-loss for accurate one-stage object detection.
     IEEE Transactions on Pattern Analysis and Machine Intelli-           [19] Qi Han, Yuxuan Cai, and Xiangyu Zhang. RevColV2: Ex-
     gence (TPAMI), 43(11):3782–3798, 2020. 1                                  ploring disentangled representations in masked image mod-
                                                                               eling. Advances in Neural Information Processing Systems
 [6] Yabo Chen, Yuchen Liu, Dongsheng Jiang, Xiaopeng Zhang,
                                                                               (NeurIPS), 2023. 2, 3
     Wenrui Dai, Hongkai Xiong, and Qi Tian. SdAE: Self-
     distillated masked autoencoder. In Proceedings of the Euro-          [20] Zeeshan Hayder, Xuming He, and Mathieu Salzmann.
     pean Conference on Computer Vision (ECCV), pages 108–                     Boundary-aware instance segmentation. In Proceedings of
     124, 2022. 2                                                              the IEEE/CVF Conference on Computer Vision and Pattern
 [7] Yuming Chen, Xinbin Yuan, Ruiqi Wu, Jiabao Wang, Qibin                    Recognition (CVPR), pages 5696–5704, 2017. 1, 3
     Hou, and Ming-Ming Cheng. YOLO-MS: rethinking multi-                 [21] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     scale representation learning for real-time object detection.             Deep residual learning for image recognition. In Proceed-
     arXiv preprint arXiv:2308.05480, 2023. 1, 3, 7, 8                         ings of the IEEE/CVF Conference on Computer Vision and
 [8] Mingyu Ding, Bin Xiao, Noel Codella, Ping Luo, Jingdong                   Pattern Recognition (CVPR), pages 770–778, 2016. 1, 4, 8
     Wang, and Lu Yuan. DaVIT: Dual attention vision trans-               [22] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     formers. In Proceedings of the European Conference on                     Identity mappings in deep residual networks. In Proceedings
     Computer Vision (ECCV), pages 74–92, 2022. 1                              of the European Conference on Computer Vision (ECCV),
 [9] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                    pages 630–645. Springer, 2016. 1, 4
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,                  [23] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kil-
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-                  ian Q Weinberger. Densely connected convolutional net-
     vain Gelly, et al. An image is worth 16x16 words: Trans-                  works. In Proceedings of the IEEE/CVF Conference on
     formers for image recognition at scale. In International Con-             Computer Vision and Pattern Recognition (CVPR), pages
     ference on Learning Representations (ICLR), 2021. 1, 2                    4700–4708, 2017. 1
[10] Chengjian Feng, Yujie Zhong, Yu Gao, Matthew R Scott,                [24] Kuan-Chih Huang, Tsung-Han Wu, Hung-Ting Su, and Win-
     and Weilin Huang. TOOD: Task-aligned one-stage object                     ston H Hsu. MonoDTR: Monocular 3D object detection with
     detection. In Proceedings of the IEEE/CVF International                   depth-aware transformer. In Proceedings of the IEEE/CVF
     Conference on Computer Vision (ICCV), pages 3490–3499,                    Conference on Computer Vision and Pattern Recognition
     2021. 1                                                                   (CVPR), pages 4012–4021, 2022. 1, 3
[11] Shang-Hua Gao, Ming-Ming Cheng, Kai Zhao, Xin-Yu                     [25] Lin Huang, Weisheng Li, Linlin Shen, Haojie Fu, Xue Xiao,
     Zhang, Ming-Hsuan Yang, and Philip Torr. Res2Net: A                       and Suihan Xiao. YOLOCS: Object detection based on dense
     new multi-scale backbone architecture. IEEE Transac-                      channel compression for feature spatial solidification. arXiv
     tions on Pattern Analysis and Machine Intelligence (TPAMI),               preprint arXiv:2305.04170, 2023. 3
     43(2):652–662, 2019. 3                                               [26] Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals,
[12] Zheng Ge, Songtao Liu, Zeming Li, Osamu Yoshie, and Jian                  Andrew Zisserman, and Joao Carreira. Perceiver: General
     Sun. OTA: Optimal transport assignment for object detec-                  perception with iterative attention. In International Confer-
     tion. In Proceedings of the IEEE/CVF Conference on Com-                   ence on Machine Learning (ICML), pages 4651–4664, 2021.
     puter Vision and Pattern Recognition (CVPR), pages 303–                   1
     312, 2021. 1                                                         [27] Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina
[13] Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, and Jian                     Toutanova. BERT: Pre-training of deep bidirectional trans-
     Sun. YOLOX: Exceeding YOLO series in 2021. arXiv                          formers for language understanding. In Proceedings of
     preprint arXiv:2107.08430, 2021. 3                                        NAACL-HLT, volume 1, page 2, 2019. 2

                                                                     11
[28] Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou                [40] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
     Zhang, and Zhuowen Tu. Deeply-supervised nets. In Ar-                     Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, et al.
     tificial Intelligence and Statistics, pages 562–570, 2015. 1,             Swin transformer v2: Scaling up capacity and resolution. In
     2, 3                                                                      Proceedings of the IEEE/CVF Conference on Computer Vi-
[29] Alex Levinshtein, Alborz Rezazadeh Sereshkeh, and Kon-                    sion and Pattern Recognition (CVPR), 2022. 1
     stantinos Derpanis. DATNet: Dense auxiliary tasks for ob-            [41] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng
     ject detection. In Proceedings of the IEEE/CVF Winter Con-                Zhang, Stephen Lin, and Baining Guo. Swin transformer:
     ference on Applications of Computer Vision (WACV), pages                  Hierarchical vision transformer using shifted windows. In
     1419–1427, 2020. 1, 3                                                     Proceedings of the IEEE/CVF International Conference on
[30] Chuyi Li, Lulu Li, Yifei Geng, Hongliang Jiang, Meng                      Computer Vision (ICCV), pages 10012–10022, 2021. 1
     Cheng, Bo Zhang, Zaidan Ke, Xiaoming Xu, and Xiangx-                 [42] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feicht-
     iang Chu. YOLOv6 v3.0: A full-scale reloading. arXiv                      enhofer, Trevor Darrell, and Saining Xie. A ConvNet for the
     preprint arXiv:2301.05586, 2023. 3, 7, 2, 4                               2020s. In Proceedings of the IEEE/CVF Conference on Com-
[31] Chuyi Li, Lulu Li, Hongliang Jiang, Kaiheng Weng, Yifei                   puter Vision and Pattern Recognition (CVPR), pages 11976–
     Geng, Liang Li, Zaidan Ke, Qingyuan Li, Meng Cheng,                       11986, 2022. 1
     Weiqiang Nie, et al. YOLOv6: A single-stage object de-               [43] Wenyu Lv, Shangliang Xu, Yian Zhao, Guanzhong Wang,
     tection framework for industrial applications. arXiv preprint             Jinman Wei, Cheng Cui, Yuning Du, Qingqing Dang, and
     arXiv:2209.02976, 2022. 3                                                 Yi Liu. DETRs beat YOLOs on real-time object detection.
[32] Hao Li, Jinguo Zhu, Xiaohu Jiang, Xizhou Zhu, Hongsheng                   arXiv preprint arXiv:2304.08069, 2023. 1, 3, 7, 8, 2, 4
     Li, Chun Yuan, Xiaohua Wang, Yu Qiao, Xiaogang Wang,                 [44] Chengqi Lyu, Wenwei Zhang, Haian Huang, Yue Zhou,
     Wenhai Wang, et al. Uni-perceiver v2: A generalist model                  Yudong Wang, Yanyi Liu, Shilong Zhang, and Kai Chen.
     for large-scale vision and vision-language tasks. In Proceed-             RTMDet: An empirical study of designing real-time object
     ings of the IEEE/CVF Conference on Computer Vision and                    detectors. arXiv preprint arXiv:2212.07784, 2022. 8, 2, 3, 4
     Pattern Recognition (CVPR), pages 2691–2700, 2023. 1
                                                                          [45] Kemal Oksuz, Baris Can Cam, Emre Akbas, and Sinan
[33] Shuai Li, Chenhang He, Ruihuang Li, and Lei Zhang. A                      Kalkan. A ranking-based, balanced loss function unify-
     dual weighting label assignment scheme for object detection.              ing classification and localisation in object detection. Ad-
     In Proceedings of the IEEE/CVF Conference on Computer                     vances in Neural Information Processing Systems (NeurIPS),
     Vision and Pattern Recognition (CVPR), pages 9387–9396,                   33:15534–15545, 2020. 1
     2022. 1
                                                                          [46] Kemal Oksuz, Baris Can Cam, Emre Akbas, and Sinan
[34] Tingting Liang, Xiaojie Chu, Yudong Liu, Yongtao Wang,
                                                                               Kalkan. Rank & sort loss for object detection and instance
     Zhi Tang, Wei Chu, Jingdong Chen, and Haibin Ling. CB-
                                                                               segmentation. In Proceedings of the IEEE/CVF Interna-
     Net: A composite backbone network architecture for object
                                                                               tional Conference on Computer Vision (ICCV), pages 3009–
     detection. IEEE Transactions on Image Processing (TIP),
                                                                               3018, 2021. 1
     2022. 3, 9
                                                                          [47] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali
[35] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
                                                                               Farhadi. You only look once: Unified, real-time object detec-
     Bharath Hariharan, and Serge Belongie. Feature pyra-
                                                                               tion. In Proceedings of the IEEE/CVF Conference on Com-
     mid networks for object detection. In Proceedings of the
                                                                               puter Vision and Pattern Recognition (CVPR), pages 779–
     IEEE/CVF Conference on Computer Vision and Pattern
                                                                               788, 2016. 3
     Recognition (CVPR), pages 2117–2125, 2017. 3
[36] Zhihao Lin, Yongtao Wang, Jinhe Zhang, and Xiaojie Chu.              [48] Joseph Redmon and Ali Farhadi. YOLO9000: better, faster,
     DynamicDet: A unified dynamic architecture for object de-                 stronger. In Proceedings of the IEEE/CVF Conference on
     tection. In Proceedings of the IEEE/CVF Conference on                     Computer Vision and Pattern Recognition (CVPR), pages
     Computer Vision and Pattern Recognition (CVPR), pages                     7263–7271, 2017. 3
     6282–6291, 2023. 3, 6, 2, 4                                          [49] Joseph Redmon and Ali Farhadi. YOLOv3: An incremental
[37] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.                 improvement. arXiv preprint arXiv:1804.02767, 2018. 3, 8
     Path aggregation network for instance segmentation. In Pro-          [50] Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak, Amir
     ceedings of the IEEE/CVF Conference on Computer Vision                    Sadeghian, Ian Reid, and Silvio Savarese. Generalized in-
     and Pattern Recognition (CVPR), pages 8759–8768, 2018.                    tersection over union: A metric and a loss for bounding box
     3, 5                                                                      regression. In Proceedings of the IEEE/CVF Conference
[38] Yue Liu, Yunjie Tian, Yuzhong Zhao, Hongtian Yu, Lingxi                   on Computer Vision and Pattern Recognition (CVPR), pages
     Xie, Yaowei Wang, Qixiang Ye, and Yunfan Liu. Vmamba:                     658–666, 2019. 1
     Visual state space model. arXiv preprint arXiv:2401.10166,           [51] Zhiqiang Shen, Zhuang Liu, Jianguo Li, Yu-Gang Jiang,
     2024. 1                                                                   Yurong Chen, and Xiangyang Xue. Object detection from
[39] Yudong Liu, Yongtao Wang, Siwei Wang, TingTing Liang,                     scratch with deep supervision. IEEE Transactions on Pattern
     Qijie Zhao, Zhi Tang, and Haibin Ling. CBNet: A novel                     Analysis and Machine Intelligence (TPAMI), 42(2):398–412,
     composite backbone network architecture for object detec-                 2019. 1, 2
     tion. In Proceedings of the AAAI Conference on Artificial            [52] Mohit Shridhar, Lucas Manuelli, and Dieter Fox. Perceiver-
     Intelligence (AAAI), pages 11653–11660, 2020. 3                           actor: A multi-task transformer for robotic manipulation.

                                                                     12
     In Conference on Robot Learning (CoRL), pages 785–799,                   In Proceedings of the IEEE/CVF Conference on Computer
     2023. 1                                                                  Vision and Pattern Recognition Workshops (CVPRW), pages
[53] Peize Sun, Yi Jiang, Enze Xie, Wenqi Shao, Zehuan Yuan,                  390–391, 2020. 3, 6, 8
     Changhu Wang, and Ping Luo. What makes for end-to-end               [65] Chien-Yao Wang, Hong-Yuan Mark Liao, and I-Hau Yeh.
     object detection? In International Conference on Machine                 Designing network design strategies through gradient path
     Learning (ICML), pages 9934–9944, 2021. 3                                analysis. Journal of Information Science and Engineering
[54] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet,               (JISE), 39(4):975–995, 2023. 2, 3, 6
     Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent               [66] Chien-Yao Wang, I-Hau Yeh, and Hong-Yuan Mark Liao.
     Vanhoucke, and Andrew Rabinovich. Going deeper with                      You only learn one representation: Unified network for mul-
     convolutions. In Proceedings of the IEEE/CVF Conference                  tiple tasks. Journal of Information Science & Engineering
     on Computer Vision and Pattern Recognition (CVPR), pages                 (JISE), 39(3):691–709, 2023. 2, 3, 4
     1–9, 2015. 1, 2, 3                                                  [67] Jianfeng Wang, Lin Song, Zeming Li, Hongbin Sun, Jian
[55] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon                  Sun, and Nanning Zheng. End-to-end object detection
     Shlens, and Zbigniew Wojna. Rethinking the inception archi-              with fully convolutional network. In Proceedings of the
     tecture for computer vision. In Proceedings of the IEEE/CVF              IEEE/CVF Conference on Computer Vision and Pattern
     Conference on Computer Vision and Pattern Recognition                    Recognition (CVPR), pages 15849–15858, 2021. 1, 3
     (CVPR), pages 2818–2826, 2016. 1                                    [68] Liwei Wang, Chen-Yu Lee, Zhuowen Tu, and Svetlana
[56] Zineng Tang, Jaemin Cho, Jie Lei, and Mohit Bansal.                      Lazebnik. Training deeper convolutional networks with deep
     Perceiver-VL: Efficient vision-and-language modeling with                supervision. arXiv preprint arXiv:1505.02496, 2015. 1, 2, 3
     iterative latent attention. In Proceedings of the IEEE/CVF          [69] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao
     Winter Conference on Applications of Computer Vision                     Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao.
     (WACV), pages 4410–4420, 2023. 1                                         Pyramid vision transformer: A versatile backbone for dense
[57] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:                     prediction without convolutions. In Proceedings of the
     Fully convolutional one-stage object detection. In Proceed-              IEEE/CVF International Conference on Computer Vision
     ings of the IEEE/CVF International Conference on Com-                    (ICCV), pages 568–578, 2021. 1
     puter Vision (ICCV), pages 9627–9636, 2019. 3                       [70] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao
[58] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:                     Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao. PVT
     A simple and strong anchor-free object detector. IEEE                    v2: Improved baselines with pyramid vision transformer.
     Transactions on Pattern Analysis and Machine Intelligence                Computational Visual Media, 8(3):415–424, 2022. 1
     (TPAMI), 44(4):1922–1933, 2022. 3                                   [71] Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei
[59] Naftali Tishby and Noga Zaslavsky. Deep learning and the                 Chen, Zhuang Liu, In So Kweon, and Saining Xie. Con-
     information bottleneck principle. In IEEE Information The-               vNeXt v2: Co-designing and scaling convnets with masked
     ory Workshop (ITW), pages 1–5, 2015. 2, 4                                autoencoders. In Proceedings of the IEEE/CVF Conference
[60] Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang,                     on Computer Vision and Pattern Recognition (CVPR), pages
     Peyman Milanfar, Alan Bovik, and Yinxiao Li. MaxVIT:                     16133–16142, 2023. 1, 2
     Multi-axis vision transformer. In Proceedings of the Euro-          [72] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
     pean Conference on Computer Vision (ECCV), pages 459–                    Kaiming He. Aggregated residual transformations for deep
     479, 2022. 1                                                             neural networks. In Proceedings of the IEEE/CVF Confer-
[61] Chengcheng Wang, Wei He, Ying Nie, Jianyuan Guo,                         ence on Computer Vision and Pattern Recognition (CVPR),
     Chuanjian Liu, Kai Han, and Yunhe Wang. Gold-YOLO:                       pages 1492–1500, 2017. 1
     Efficient object detector via gather-and-distribute mecha-          [73] Zhenda Xie, Zheng Zhang, Yue Cao, Yutong Lin, Jianmin
     nism. Advances in Neural Information Processing Systems                  Bao, Zhuliang Yao, Qi Dai, and Han Hu. SimMIM: A simple
     (NeurIPS), 2023. 3, 7, 2, 4                                              framework for masked image modeling. In Proceedings of
[62] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-                            the IEEE/CVF Conference on Computer Vision and Pattern
     Yuan Mark Liao. Scaled-YOLOv4: Scaling cross stage                       Recognition (CVPR), pages 9653–9663, 2022. 2
     partial network. In Proceedings of the IEEE/CVF Confer-             [74] Shangliang Xu, Xinxin Wang, Wenyu Lv, Qinyao Chang,
     ence on Computer Vision and Pattern Recognition (CVPR),                  Cheng Cui, Kaipeng Deng, Guanzhong Wang, Qingqing
     pages 13029–13038, 2021. 3                                               Dang, Shengyu Wei, Yuning Du, et al. PP-YOLOE: An
[63] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-                            evolved version of YOLO. arXiv preprint arXiv:2203.16250,
     Yuan Mark Liao. YOLOv7: Trainable bag-of-freebies                        2022. 3, 8, 2, 4
     sets new state-of-the-art for real-time object detectors. In        [75] Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang,
     Proceedings of the IEEE/CVF Conference on Computer                       Yuan Zhang, and Xiuyu Sun.           DAMO-YOLO: A re-
     Vision and Pattern Recognition (CVPR), pages 7464–7475,                  port on real-time object detection design. arXiv preprint
     2023. 3, 6, 7, 9, 1                                                      arXiv:2211.15444, 2022. 3, 7, 2, 4
[64] Chien-Yao Wang, Hong-Yuan Mark Liao, Yueh-Hua Wu,                   [76] Renrui Zhang, Han Qiu, Tai Wang, Ziyu Guo, Ziteng Cui, Yu
     Ping-Yang Chen, Jun-Wei Hsieh, and I-Hau Yeh. CSPNet: A                  Qiao, Hongsheng Li, and Peng Gao. MonoDETR: Depth-
     new backbone that can enhance learning capability of CNN.                guided transformer for monocular 3D object detection. In

                                                                    13
     Proceedings of the IEEE/CVF International Conference on
     Computer Vision (ICCV), pages 9155–9166, 2023. 1, 3
[77] Zhaohui Zheng, Ping Wang, Wei Liu, Jinze Li, Rongguang
     Ye, and Dongwei Ren. Distance-IoU loss: Faster and bet-
     ter learning for bounding box regression. In Proceedings of
     the AAAI Conference on Artificial Intelligence (AAAI), vol-
     ume 34, pages 12993–13000, 2020. 1
[78] Dingfu Zhou, Jin Fang, Xibin Song, Chenye Guan, Junbo
     Yin, Yuchao Dai, and Ruigang Yang. IoU loss for 2D/3D
     object detection. In International Conference on 3D Vision
     (3DV), pages 85–94, 2019. 1
[79] Benjin Zhu, Jianfeng Wang, Zhengkai Jiang, Fuhang Zong,
     Songtao Liu, Zeming Li, and Jian Sun. AutoAssign: Differ-
     entiable label assignment for dense object detection. arXiv
     preprint arXiv:2007.03496, 2020. 1
[80] Lianghui Zhu, Bencheng Liao, Qian Zhang, Xinlong Wang,
     Wenyu Liu, and Xinggang Wang. Vision mamba: Efficient
     visual representation learning with bidirectional state space
     model. arXiv preprint arXiv:2401.09417, 2024. 1
[81] Xizhou Zhu, Jinguo Zhu, Hao Li, Xiaoshi Wu, Hongsheng
     Li, Xiaohua Wang, and Jifeng Dai. Uni-perceiver: Pre-
     training unified architecture for generic perception for zero-
     shot and few-shot tasks. In Proceedings of the IEEE/CVF
     Conference on Computer Vision and Pattern Recognition
     (CVPR), pages 16804–16815, 2022. 1
[82] Zhuofan Zong, Guanglu Song, and Yu Liu. DETRs with
     collaborative hybrid assignments training. In Proceedings of
     the IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR), pages 6748–6758, 2023. 3

                                                                      14
                                                        Appendix
A. Implementation Details                                                    Table 2. Network configurations of YOLOv9.
                                                                     Index Module    Route        Filters   Depth Size Stride
                                                                     0       Conv        –           64       –    3     2
        Table 1. Hyper parameter settings of YOLOv9.
                                                                     1       Conv        0          128       –    3     2
          hyper parameter                   value                    2    CSP-ELAN       1      256, 128, 64 2, 1 –      1
                                                                     3     DOWN          2          256       –    3     2
          epochs                             500
                                                                     4    CSP-ELAN       3     512, 256, 128 2, 1 –      1
          optimizer                         SGD                      5     DOWN          4          512       –    3     2
          initial learning rate              0.01                    6    CSP-ELAN       5     512, 512, 256 2, 1 –      1
          finish learning rate             0.0001                    7     DOWN          6          512       –    3     2
          learning rate decay              linear                    8    CSP-ELAN       7     512, 512, 256 2, 1 –      1
          momentum                          0.937                    9    SPP-ELAN       8     512, 256, 256 3, 1 –      1
          weight decay                     0.0005                    10       Up         9          512       –    –     2
          warm-up epochs                       3                     11     Concat     10, 6       1024       –    –     1
          warm-up momentum                    0.8                    12   CSP-ELAN      11     512, 512, 256 2, 1 –      1
          warm-up bias learning rate          0.1                    13       Up        12          512       –    –     2
          box loss gain                      7.5                     14     Concat     13, 4       1024       –    –     1
                                                                     15   CSP-ELAN      14     256, 256, 128 2, 1 –      1
          class loss gain                    0.5
                                                                     16    DOWN         15          256       –    3     2
          DFL loss gain                      1.5                     17     Concat    16, 12        768       –    –     1
          HSV saturation augmentation         0.7                    18   CSP-ELAN      17     512, 512, 256 2, 1 –      1
          HSV value augmentation              0.4                    19    DOWN         18          512       –    3     2
          translation augmentation            0.1                    20     Concat     19, 9       1024       –    –     1
          scale augmentation                  0.9                    21   CSP-ELAN      20     512, 512, 256 2, 1 –      1
          mosaic augmentation                 1.0                    22     Predict 15, 18, 21        –       –    –     –
          MixUp augmentation                 0.15
          copy & paste augmentation           0.3                       The network topology of YOLOv9 completely follows
          close mosaic epochs                 15                    YOLOv7 AF [63], that is, we replace ELAN with the pro-
                                                                    posed CSP-ELAN block. As listed in Table 2, the depth
   The training parameters of YOLOv9 are shown in Ta-               parameters of CSP-ELAN are represented as ELAN depth
ble 1. We fully follow the settings of YOLOv7 AF [63],              and CSP depth, respectively. As for the parameters of CSP-
which is to use SGD optimizer to train 500 epochs. We first         ELAN filters, they are represented as ELAN output fil-
warm-up for 3 epochs and only update the bias during the            ter, CSP output filter, and CSP inside filter. In the down-
warm-up stage. Next we step down from the initial learning          sampling module part, we simplify CSP-DOWN module to
rate 0.01 to 0.0001 in linear decay manner, and the data aug-       DOWN module. DOWN module is composed of a pooling
mentation settings are listed in the bottom part of Table 1.        layer with size 2 and stride 1, and a Conv layer with size 3
We shut down mosaic data augmentation operations on the             and stride 2. Finally, we optimized the prediction layer and
last 15 epochs.                                                     replaced top, left, bottom, and right in the regression branch
                                                                    with decoupled branch.

                                                                1
                                          Table 3. Comparison of state-of-the-art object detectors with different training settings.
                               Model                #Param. (M)   FLOPs (G)    AP50:95 (%)    AP50 (%)    AP75 (%)    APS (%)    APM (%)      APL (%)
                               Dy-YOLOv7 [36]           –            181.7          53.9         72.2        58.7        35.3          57.6    66.4
      Train-from-scratch

                               Dy-YOLOv7-X [36]         –            307.9          55.0         73.2        60.0        36.6          58.7    68.5
                               YOLOv9-S (Ours)         7.1           26.4           46.8         63.4        50.7        26.6          56.0    64.5
                               YOLOv9-M (Ours)         20.0           76.3          51.4         68.1        56.1        33.6          57.0    68.0
                               YOLOv9-C (Ours)         25.3          102.1          53.0         70.2        57.8        36.2          58.5    69.3
                               YOLOv9-E (Ours)         34.7          147.1          54.5         71.7        59.2        38.1          59.9    70.3
                               YOLOv9-E (Ours)         44.0          183.9          55.1         72.3        60.7        38.7          60.6    71.4
                               YOLOv9-E (Ours)         57.3          189.0          55.6         72.8        60.6        40.2          61.0    71.4
                               RTMDet-T [44]           4.8           12.6           41.1         57.9         –           –             –       –
                               RTMDet-S [44]           9.0           25.6           44.6         61.9         –           –             –       –
                               RTMDet-M [44]           24.7           78.6          49.4         66.8         –           –             –       –
                               RTMDet-L [44]           52.3          160.4          51.5         68.8         –           –             –       –
                               RTMDet-X [44]           94.9          283.4          52.8         70.4         –           –             –       –
                               PPYOLOE-S [74]          7.9           14.4           43.0         60.5        46.6        23.2          46.4    56.9
      ImageNet Pretrained

                               PPYOLOE-M [74]          23.4           49.9          49.0         66.5        53.0        28.6          52.9    63.8
                               PPYOLOE-L [74]          52.2          110.1          51.4         68.9        55.6        31.4          55.3    66.1
                               PPYOLOE-X [74]          98.4          206.6          52.3         69.5        56.8        35.1          57.0    68.6
                               RT DETR-L [43]           32            110           53.0         71.6        57.3        34.6          57.3    71.2
                               RT DETR-X [43]           67            234           54.8         73.1        59.4        35.7          59.6    72.9
                               RT DETR-R18 [43]         20             60           46.5         63.8         –           –             –       –
                               RT DETR-R34 [43]         31             92           48.9         66.8         –           –             –       –
                               RT DETR-R50M [43]        36            100           51.3         69.6         –           –             –       –
                               RT DETR-R50 [43]         42            136           53.1         71.3        57.7        34.8          58.0    70.0
                               RT DETR-R101 [43]        76            259           54.3         72.7        58.6        36.0          58.8    72.1
                               Gold YOLO-S [61]        21.5           46.0          45.5         62.2         –           –             –       –
                               Gold YOLO-M [61]        41.3           57.5          50.2         67.5         –           –             –       –
                               Gold YOLO-L [61]        75.1          151.7          52.3         69.6         –           –             –       –
                               YOLOv6-N v3.0 [30]      4.7           11.4           37.5         53.1         –           –             –       –
                               YOLOv6-S v3.0 [30]      18.5           45.3          45.0         61.8         –           –             –       –
      Knowledge Distillation

                               YOLOv6-M v3.0 [30]      34.9           85.8          50.0         66.9         –           –             –       –
                               YOLOv6-L v3.0 [30]      59.6          150.7          52.8         70.3         –           –             –       –
                               DAMO YOLO-T [75]        8.5           18.1           43.6         59.4        46.6        23.3          47.4    61.0
                               DAMO YOLO-S [75]        16.3           37.8          47.7         63.5        51.1        26.9          51.7    64.9
                               DAMO YOLO-M [75]        28.2           61.8          50.4         67.2        55.1        31.6          55.3    67.1
                               DAMO YOLO-L [75]        42.1           97.3          51.9         68.5        56.7        33.3          57.0    67.6
                               Gold YOLO-N [61]        5.6           12.1           39.9         55.9         –           –             –       –
                               Gold YOLO-S [61]        21.5           46.0          46.1         63.3         –           –             –       –
                               Gold YOLO-M [61]        41.3           57.5          50.9         68.2         –           –             –       –
                               Gold YOLO-L [61]        75.1          151.7          53.2         70.5         –           –             –       –
                               Gold YOLO-S [61]        21.5           46.0          46.4         63.4         –           –             –       –
                               Gold YOLO-M [61]        41.3           57.5          51.1         68.5         –           –             –       –
      Complex Setting

                               Gold YOLO-L [61]        75.1          151.7          53.3         70.9         –           –             –       –
                               YOLOR-CSP [66]          52.9          120.4          52.8         71.2        57.6         –             –       –
                               YOLOR-CSP-X [66]        96.9          226.8          54.8         73.1        59.7         –             –       –
                               PPYOLOE+-S [74]         7.9           14.4           43.7         60.6        47.9        23.2          46.4    56.9
                               PPYOLOE+-M [74]         23.4           49.9          49.8         67.1        54.5        31.8          53.9    66.2
                               PPYOLOE+-L [74]         52.2          110.1          52.9         70.1        57.9        35.2          57.5    69.1
                               PPYOLOE+-X [74]         98.4          206.6          54.7         72.0        59.9        37.9          59.3    70.4

B. More Comparison                                                                         pleted; and (4) a more complex training process: a combi-
   We compare YOLOv9 to state-of-the-art real-time object                                  nation of steps including pretrained by ImageNet, knowl-
detectors trained with different methods. It mainly includes                               edge distillation, DAMO-YOLO and even additional pre-
four different training methods: (1) train-from-scratch: we                                trained large object detection dataset. We show the results
have completed most of the comparisons in the text. Here                                   in Table 3. From this table, we can see that our proposed
are only list of additional data of DynamicDet [36] for com-                               YOLOv9 performed better than all other methods. Com-
parisons; (2) Pretrained by ImageNet: this includes two                                    pared with PPYOLOE+-X trained using ImageNet and Ob-
methods of using ImageNet for supervised pretrain and self-                                jects365, our method still reduces the number of parame-
supervised pretrain; (3) knowledge distillation: a method                                  ters by 55% and the amount of computation by 11%, and
to perform additional self-distillation after training is com-                             improving 0.4% AP.

                                                                                      2
        Table 4. Comparison of state-of-the-art object detectors with different training settings (sorted by number of parameters).
     Model                           #Param. (M)     FLOPs (G)      APval
                                                                      50:95 (%)      APval
                                                                                       50 (%)      APval
                                                                                                     75 (%)       APval
                                                                                                                    S (%)       APval
                                                                                                                                  M (%)      APval
                                                                                                                                               L (%)
     YOLOv6-N v3.0 [30] (D)                4.7            11.4           37.5           53.1            –             –                –        –
     RTMDet-T [44] (I)                     4.8            12.6           41.1           57.9            –             –                –        –
     Gold YOLO-N [61] (D)                  5.6            12.1           39.9           55.9            –             –                –        –
     YOLOv9-S (S)                          7.1            26.4           46.8           63.4           50.7          26.6             56.0     64.5
     PPYOLOE+-S [74] (C)                   7.9            14.4           43.7           60.6           47.9          23.2             46.4     56.9
     PPYOLOE-S [74] (I)                    7.9            14.4           43.0           60.5           46.6          23.2             46.4     56.9
     DAMO YOLO-T [75] (D)                  8.5            18.1           43.6           59.4           46.6          23.3             47.4     61.0
     RTMDet-S [44] (I)                     9.0            25.6           44.6           61.9            –             –                –        –
     DAMO YOLO-S [75] (D)                 16.3            37.8           47.7           63.5           51.1          26.9             51.7     64.9
     YOLOv6-S v3.0 [30] (D)               18.5            45.3           45.0           61.8            –             –                –        –
     RT DETR-R18 [43] (I)                  20              60            46.5           63.8            –             –                –        –
     YOLOv9-M (S)                         20.0            76.3           51.4           68.1           56.1          33.6             57.0     68.0
     Gold YOLO-S [61] (C)                 21.5            46.0           46.4           63.4            –             –                –        –
     Gold YOLO-S [61] (D)                 21.5            46.0           46.1           63.3            –             –                –        –
     Gold YOLO-S [61] (I)                 21.5            46.0           45.5           62.2            –             –                –        –
     PPYOLOE+-M [74] (C)                  23.4            49.9           49.8           67.1           54.5          31.8             53.9     66.2
     PPYOLOE-M [74] (I)                   23.4            49.9           49.0           66.5           53.0          28.6             52.9     63.8
     RTMDet-M [44] (I)                    24.7            78.6           49.4           66.8            –             –                –        –
     YOLOv9-C (S)                         25.3           102.1           53.0           70.2           57.8          36.2             58.5     69.3
     DAMO YOLO-M [75] (D)                 28.2            61.8           50.4           67.2           55.1          31.6             55.3     67.1
     RT DETR-R34 [43] (I)                  31              92            48.9           66.8            –             –                –        –
     RT DETR-L [43] (I)                    32             110            53.0           71.6           57.3          34.6             57.3     71.2
     YOLOv9-E (S)                         34.7           147.1           54.5           71.7           59.2          38.1             59.9     70.3
     YOLOv6-M v3.0 [30] (D)               34.9            85.8           50.0           66.9            –             –                –        –
     RT DETR-R50M [43] (I)                 36             100            51.3           69.6            –             –                –        –
     Gold YOLO-M [61] (C)                 41.3            57.5           51.1           68.5            –             –                –        –
     Gold YOLO-M [61] (D)                 41.3            57.5           50.9           68.2            –             –                –        –
     Gold YOLO-M [61] (I)                 41.3            57.5           50.2           67.5            –             –                –        –
     RT DETR-R50 [43] (I)                  42             136            53.1           71.3           57.7          34.8             58.0     70.0
     DAMO YOLO-L [75] (D)                 42.1            97.3           51.9           68.5           56.7          33.3             57.0     67.6
     YOLOv9-E (S)                         44.0           183.9           55.1           72.3           60.7          38.7             60.6     71.4
     PPYOLOE+-L [74] (C)                  52.2           110.1           52.9           70.1           57.9          35.2             57.5     69.1
     PPYOLOE-L [74] (I)                   52.2           110.1           51.4           68.9           55.6          31.4             55.3     66.1
     RTMDet-L [44] (I)                    52.3           160.4           51.5           68.8            –             –                –        –
     YOLOR-CSP [66] (C)                   52.9           120.4           52.8           71.2           57.6           –                –        –
     YOLOv9-E (S)                         57.3           189.0           55.6           72.8           60.6          40.2             61.0     71.4
     YOLOv6-L v3.0 [30] (D)               59.6           150.7           52.8           70.3            –             –                –        –
     RT DETR-X [43] (I)                    67             234            54.8           73.1           59.4          35.7             59.6     72.9
     Gold YOLO-L [61] (C)                 75.1           151.7           53.3           70.9            –             –                –        –
     Gold YOLO-L [61] (D)                 75.1           151.7           53.2           70.5            –             –                –        –
     Gold YOLO-L [61] (I)                 75.1           151.7           52.3           69.6            –             –                –        –
     RT DETR-R101 [43] (I)                 76             259            54.3           72.7           58.6          36.0             58.8     72.1
     RTMDet-X [44] (I)                    94.9           283.4           52.8           70.4            –             –                –        –
     YOLOR-CSP-X [66] (C)                 96.9           226.8           54.8           73.1           59.7           –                –        –
     PPYOLOE+-X [74] (C)                  98.4           206.6           54.7           72.0           59.9          37.9             59.3     70.4
     PPYOLOE-X [74] (I)                   98.4           206.6           52.3           69.5           56.8          35.1             57.0     68.6
  1 (S), (I), (D), (C) indicate train-from-scratch, ImageNet pretrained, knowledge distillation, and complex setting, respectively.

   Table 4 shows the performance of all models sorted by                             Shown in Table 5 is the performance of all participat-
parameter size. Our proposed YOLOv9 is Pareto optimal                             ing models sorted by the amount of computation. Our pro-
in all models of different sizes. Among them, we found no                         posed YOLOv9 is Pareto optimal in all models with differ-
other method for Pareto optimal in models with more than                          ent scales. Among models with more than 60 GFLOPs, only
20M parameters. The above experimental data shows that                            ELAN-based DAMO-YOLO and DETR-based RT DETR
our YOLOv9 has excellent parameter usage efficiency.                              can rival the proposed YOLOv9. The above comparison
                                                                                  results show that YOLOv9 has the most outstanding per-
                                                                                  formance in the trade-off between computation complexity
                                                                                  and accuracy.

                                                                              3
      Table 5. Comparison of state-of-the-art object detectors with different training settings (sorted by amount of computation).
   Model                           #Param. (M)     FLOPs (G)      APval
                                                                    50:95 (%)      APval
                                                                                     50 (%)      APval
                                                                                                   75 (%)       APval
                                                                                                                  S (%)       APval
                                                                                                                                M (%)      APval
                                                                                                                                             L (%)
   YOLOv6-N v3.0 [30] (D)                4.7            11.4           37.5           53.1            –             –                –        –
   Gold YOLO-N [61] (D)                  5.6            12.1           39.9           55.9            –             –                –        –
   RTMDet-T [44] (I)                     4.8            12.6           41.1           57.9            –             –                –        –
   PPYOLOE+-S [74] (C)                   7.9            14.4           43.7           60.6           47.9          23.2             46.4     56.9
   PPYOLOE-S [74] (I)                    7.9            14.4           43.0           60.5           46.6          23.2             46.4     56.9
   DAMO YOLO-T [75] (D)                  8.5            18.1           43.6           59.4           46.6          23.3             47.4     61.0
   RTMDet-S [44] (I)                     9.0            25.6           44.6           61.9            –             –                –        –
   YOLOv9-S (S)                          7.1            26.4           46.8           63.4           50.7          26.6             56.0     64.5
   DAMO YOLO-S [75] (D)                 16.3            37.8           47.7           63.5           51.1          26.9             51.7     64.9
   YOLOv6-S v3.0 [30] (D)               18.5            45.3           45.0           61.8            –             –                –        –
   Gold YOLO-S [61] (C)                 21.5            46.0           46.4           63.4            –             –                –        –
   Gold YOLO-S [61] (D)                 21.5            46.0           46.1           63.3            –             –                –        –
   Gold YOLO-S [61] (I)                 21.5            46.0           45.5           62.2            –             –                –        –
   PPYOLOE+-M [74] (C)                  23.4            49.9           49.8           67.1           54.5          31.8             53.9     66.2
   PPYOLOE-M [74] (I)                   23.4            49.9           49.0           66.5           53.0          28.6             52.9     63.8
   Gold YOLO-M [61] (C)                 41.3            57.5           51.1           68.5            –             –                –        –
   Gold YOLO-M [61] (D)                 41.3            57.5           50.9           68.2            –             –                –        –
   Gold YOLO-M [61] (I)                 41.3            57.5           50.2           67.5            –             –                –        –
   RT DETR-R18 [43] (I)                  20              60            46.5           63.8            –             –                –        –
   DAMO YOLO-M [75] (D)                 28.2            61.8           50.4           67.2           55.1          31.6             55.3     67.1
   YOLOv9-M (S)                         20.0            76.3           51.4           68.1           56.1          33.6             57.0     68.0
   RTMDet-M [44] (I)                    24.7            78.6           49.4           66.8            –             –                –        –
   YOLOv6-M v3.0 [30] (D)               34.9            85.8           50.0           66.9            –             –                –        –
   RT DETR-R34 [43] (I)                  31              92            48.9           66.8            –             –                –        –
   DAMO YOLO-L [75] (D)                 42.1            97.3           51.9           68.5           56.7          33.3             57.0     67.6
   RT DETR-R50M [43] (I)                 36             100            51.3           69.6            –             –                –        –
   YOLOv9-C (S)                         25.3           102.1           53.0           70.2           57.8          36.2             58.5     69.3
   RT DETR-L [43] (I)                    32             110            53.0           71.6           57.3          34.6             57.3     71.2
   PPYOLOE+-L [74] (C)                  52.2           110.1           52.9           70.1           57.9          35.2             57.5     69.1
   PPYOLOE-L [74] (I)                   52.2           110.1           51.4           68.9           55.6          31.4             55.3     66.1
   YOLOR-CSP [66] (C)                   52.9           120.4           52.8           71.2           57.6           –                –        –
   RT DETR-R50 [43] (I)                  42             136            53.1           71.3           57.7          34.8             58.0     70.0
   YOLOv9-E (S)                         34.7           147.1           54.5           71.7           59.2          38.1             59.9     70.3
   YOLOv6-L v3.0 [30] (D)               59.6           150.7           52.8           70.3            –             –                –        –
   Gold YOLO-L [61] (C)                 75.1           151.7           53.3           70.9            –             –                –        –
   Gold YOLO-L [61] (D)                 75.1           151.7           53.2           70.5            –             –                –        –
   Gold YOLO-L [61] (I)                 75.1           151.7           52.3           69.6            –             –                –        –
   RTMDet-L [44] (I)                    52.3           160.4           51.5           68.8            –             –                –        –
   Dy-YOLOv7 [36] (S)                     –            181.7           53.9           72.2           58.7          35.3             57.6     66.4
   YOLOv9-E (S)                         44.0           183.9           55.1           72.3           60.7          38.7             60.6     71.4
   YOLOv9-E (S)                         57.3           189.0           55.6           72.8           60.6          40.2             61.0     71.4
   PPYOLOE+-X [74] (C)                  98.4           206.6           54.7           72.0           59.9          37.9             59.3     70.4
   PPYOLOE-X [74] (I)                   98.4           206.6           52.3           69.5           56.8          35.1             57.0     68.6
   YOLOR-CSP-X [66] (C)                 96.9           226.8           54.8           73.1           59.7           –                –        –
   RT DETR-X [43] (I)                    67             234            54.8           73.1           59.4          35.7             59.6     72.9
   RT DETR-R101 [43] (I)                 76             259            54.3           72.7           58.6          36.0             58.8     72.1
   RTMDet-X [44] (I)                    94.9           283.4           52.8           70.4            –             –                –        –
   Dy-YOLOv7-X [36] (S)                   –            307.9           55.0           73.2           60.0          36.6             58.7     68.5
1 (S), (I), (D), (C) indicate train-from-scratch, ImageNet pretrained, knowledge distillation, and complex setting, respectively.

                                                                              4
