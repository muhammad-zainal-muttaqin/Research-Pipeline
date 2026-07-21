---
source_id: 139
bibtex_key: wang2023uavyolo
title: UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios
year: 2023
domain_theme: Remote Sensing
verified_pdf: 139_UAV-YOLOv8_Small_Object.pdf
char_count: 277649
---

sensors
Article
UAV-YOLOv8: A Small-Object-Detection Model Based on
Improved YOLOv8 for UAV Aerial Photography Scenarios
Gang Wang, Yanfei Chen *, Pei An, Hanyu Hong, Jinghu Hu and Tiange Huang

                                         Hubei Key Laboratory of Optical Information and Pattern Recognition, School of Electrical and Information
                                         Engineering, Wuhan Institute of Technology, Wuhan 430205, China; wanggang@stu.wit.edu.cn (G.W.);
                                         anpei@wit.edu.cn (P.A.); hhyhong@wit.edu.cn (H.H.); jinhuhu@stu.wit.edu.cn (J.H.); huangtg@wit.edu.cn (T.H.)
                                         * Correspondence: cyf@wit.edu.cn

                                         Abstract: Unmanned aerial vehicle (UAV) object detection plays a crucial role in civil, commercial,
                                         and military domains. However, the high proportion of small objects in UAV images and the limited
                                         platform resources lead to the low accuracy of most of the existing detection models embedded
                                         in UAVs, and it is difficult to strike a good balance between detection performance and resource
                                         consumption. To alleviate the above problems, we optimize YOLOv8 and propose an object detec-
                                         tion model based on UAV aerial photography scenarios, called UAV-YOLOv8. Firstly, Wise-IoU
                                         (WIoU) v3 is used as a bounding box regression loss, and a wise gradient allocation strategy makes
                                         the model focus more on common-quality samples, thus improving the localization ability of the
                                         model. Secondly, an attention mechanism called BiFormer is introduced to optimize the backbone
                                         network, which improves the model’s attention to critical information. Finally, we design a feature
                                         processing module named Focal FasterNet block (FFNB) and propose two new detection scales based
                                         on this module, which makes the shallow features and deep features fully integrated. The proposed
                                         multiscale feature fusion network substantially increased the detection performance of the model
                                         and reduces the missed detection rate of small objects. The experimental results show that our model
                                         has fewer parameters compared to the baseline model and has a mean detection accuracy higher
                                         than the baseline model by 7.7%. Compared with other mainstream models, the overall performance
                                         of our model is much better. The proposed method effectively improves the ability to detect small
Citation: Wang, G.; Chen, Y.; An, P.;    objects. There is room to optimize the detection effectiveness of our model for small and feature-less
Hong, H.; Hu, J.; Huang, T.              objects (such as bicycle-type vehicles), as we will address in subsequent research.
UAV-YOLOv8: A
Small-Object-Detection Model Based       Keywords: UAVs; small-object detection; YOLOv8; WIoU; BiFormer; FasterNet
on Improved YOLOv8 for UAV
Aerial Photography Scenarios.
Sensors 2023, 23, 7190. https://
doi.org/10.3390/s23167190
                                         1. Introduction
Academic Editor: Pasquale Daponte              With the continuous reduction in the production cost of UAVs and the gradual maturity
Received: 23 July 2023
                                         of flight control techniques, the application of UAVs is becoming increasingly widespread
Revised: 8 August 2023                   in areas such as power line inspections [1], traffic monitoring [2], and crop analysis [3].
Accepted: 12 August 2023                 Object detection plays an increasingly important role as a key link in the missions carried
Published: 15 August 2023                out by UAVs and has very great research significance. The UAV has a wide field of view
                                         due to its high flying altitude, leading to problems such as a high proportion of small
                                         objects and complex backgrounds in the captured images, which increases the difficulty of
                                         the object detection task. Moreover, UAV platforms have limited resources, making it hard
Copyright: © 2023 by the authors.        to embed high computational and storage-demanding object detection models. Therefore,
Licensee MDPI, Basel, Switzerland.       enhancing the performance of object detection while considering the limited resources of
This article is an open access article   the hardware platform is one of the core issues in object detection in UAV aerial scenes.
distributed under the terms and
                                               The essential difference among object detection algorithms is that the features of the
conditions of the Creative Commons
                                         image are extracted differently. Most of the traditional object detection algorithms are
Attribution (CC BY) license (https://
                                         reusing classifiers, such as the deformable parts model (DPM) [4].The DPM first uses
creativecommons.org/licenses/by/
                                         classifiers to slide over the image, and then the output of the classifiers is aggregated as
4.0/).

Sensors 2023, 23, 7190. https://doi.org/10.3390/s23167190                                                   https://www.mdpi.com/journal/sensors
Sensors 2023, 23, 7190                                                                                            2 of 27

                         the object detection results. This detection method is very time-consuming and tedious,
                         and the detection effect is poor. The current mainstream object detection algorithms mainly
                         use deep learning methods, and we classify them into two categories: two-stage and
                         one-stage. The R-CNN family [5–7] is a very classical two-stage algorithm, which first
                         extracts candidate frames, then uses a classifier to filter them, and finally removes duplicate
                         boxes and finetunes the predicted boxes using non-maximal value suppression. The two-
                         stage detector has some advantages in terms of detection accuracy but has disadvantages
                         such as difficulty in training, slow detection speed, and difficulty in optimization. One-
                         stage detectors include methods such as the you only look once (YOLO) series [8–13]
                         and single-shot multibox detector (SSD) [14], which use a separate neural network for
                         one forward inference to generate the coordinates and category results of the prediction
                         boxes. The one-stage object detection algorithm improves the speed of detection but loses
                         some of the detection accuracy. In addition, thanks to the excellent performance of the
                         transformer [15] model in the field of natural language processing, Carion et al. introduced
                         the model into the field of computer vision and proposed the detection with transformers
                         (DETR) model [16], which achieved desirable results and provided a new research idea
                         for object detection. However, the objects in natural scenes are multiscale in form, and the
                         objects in the UAV viewpoint are mainly small. So, the mainstream detection algorithms
                         mentioned above are not feasible to be used directly for the object detection task in UAV
                         aerial photography scenes.
                              A large amount of research work has emerged in the field of object detection in
                         UAV aerial photography scenarios in recent years. Luo et al. [17] optimized the detection
                         performance by improving the network module in YOLOv5. The effectiveness of the
                         proposed strategy is verified by numerous datasets, but the detection of small objects is
                         inferior. Zhou et al. [18] solved the problem of monotonous backgrounds in UAV images by
                         using background replacement from the perspective of data enhancement. However, this
                         work was not effective in improving the detection accuracy of small objects. Du et al. [19]
                         designed sparse convolution to optimize the detection head from the perspective of a
                         lightweight model. The sparse convolution reduces the computational effort but decreases
                         the detection accuracy of the model. Deng et al. [20] proposed a lightweight network in
                         order to improve the efficiency of insulator fault detection in transmission lines by UAVs.
                         The method uses YOLOv4 as the baseline model. Firstly, the original backbone network is
                         replaced with MobileNetv3 [21], which effectively reduces the parameters of the model.
                         Secondly, the method also improves the generalization ability of the model by improving
                         the loss function. Finally, the binary particle swarm optimization idea is introduced to
                         reduce the delay of fault detection. Zheng et al. [22] proposed a multispecies oil palm tree
                         detection method called MOPAD, which can detect oil palm trees well and can accurately
                         monitor the growth of oil palm trees. The method combines Faster RCNN, Refined Pyramid
                         Feature (RPF), and Hybrid Balanced Loss Module. MOPAD achieves desirable observations
                         on three large oil palm tree datasets and the average F1 scores outperform other state-of-
                         the-art detection models. Liu et al. [23] proposed a small-target-detection method in the
                         UAV view to reduce the leakage and false detection rate of small targets. The method
                         uses YOLOv3 as the base model, and it optimizes the backbone network by introducing
                         ResNet [24] units and adding convolutional operations to enhance the receptive field
                         of the model. For the current situation of more and more illegal flights of multi-rotor
                         UAVs, Liu et al. [25] proposed a novel detection method to improve the detection accuracy
                         of multi-rotor UAVs. The method uses Efficientlite to replace the backbone network of
                         YOLOv5, which reduces the complexity of the model and improves the detection efficiency.
                         In addition, adaptive spatial feature fusion is used at the head of the baseline model to
                         optimize the detection accuracy of the model. To improve the detection performance of
                         UAV aerial images, Wang et al. [26] proposed a lightweight detection model called MFP-
                         YOLO by optimizing YOLOv5. Firstly, the method designs a multiplexed inverted residual
                         block (MIRB) and introduces the convolutional block attention module (CBAM) [27], which
                         effectively improves the model’s detection effect under an environment of scale variation
Sensors 2023, 23, 7190                                                                                          3 of 27

                         and background complexity. Secondly, the formula introduces a parallel convolutional
                         spatial pyramid pooling framework, which takes into account targets at different scales.
                         Finally, a lightweight decoupled detection header is applied to the baseline model, which
                         reduces the parameters of the model while maintaining its detection accuracy. Liu et al. [28]
                         proposed a multi-branch parallel feature pyramid network (MPFPN) to reduce the leakage
                         rate of small-target detection in UAV images. Meanwhile, supervised spatial attention
                         module (SSAM) was added to this network to suppress the interference of background
                         noise. Finally, the effectiveness of the method was demonstrated at the public data level.
                         Most of the current research methods generally have low accuracy for object detection in
                         UAV aerial photography scenarios, and it is difficult to balance the relationship between
                         the accuracy of the model and resource consumption.
                              To alleviate the above problems, we propose an object detection model based on UAV
                         aerial photography scenarios, called UAV-YOLOv8, using YOLOv8 as the backbone network.
                         This model not only improves the performance of target detection but also does so without
                         too much resource consumption. The main contributions of this paper are as follows:
                         •   We propose an efficient and fast feature processing module called the FFNB based
                             on the FasterNet block [29]. Utilizing this module, we design two new detection
                             scales that enable the comprehensive fusion of shallow and deep features, significantly
                             reducing the missed detection rate of small objects.
                         •   We introduce a low-computational-cost dynamic sparse attention mechanism BiFormer [30]
                             in the backbone network, which improves the model’s attention to the critical information
                             in the feature map and optimizes the detection performance of the model.
                         •   We incorporate WIoU v3 [31] in our bounding box regression loss, which employs a
                             dynamic non-monotonic mechanism to design a more reasonable gradient gain alloca-
                             tion strategy. WIoU v3 effectively reduces the gradient gain of high-quality samples
                             and low-quality samples, which enhances the model’s localization performance and
                             generalization ability.
                         •   Compared with some mainstream YOLO series models as well as six other classical
                             detection models, the experimental results demonstrate the superiority of our method.
                             In addition, we perform visual analysis from three perspectives to explain that our
                             proposed method effectively improves the detection performance for small objects.

                         2. YOLOv8 Detection Algorithm
                              The YOLO model has been a great success in the field of computer vision; based
                         on this, researchers have improved and added new modules to the method, proposing
                         many classical models. YOLOv8 is an algorithm released by the Ultralytics company on
                         10 January 2023. Compared to previous excellent models in the YOLO series (such as
                         YOLOv5 and YOLOv7), YOLOv8 is an advanced and cutting-edge model that offers higher
                         detection accuracy and speed.
                              The YOLOv8 network structure mainly consists of a backbone, neck, and head, as
                         shown in Figure 1.

                         2.1. Backbone
                              YOLOv8 uses modified CSPDarknet53 [10] as the backbone network, and the input
                         features are down-sampled five times to obtain five different scale features, in turn, which
                         we denote as B1–B5. The structure of the backbone network is shown in Figure 1a. The
                         Cross Stage Partial (CSP) module in the original backbone network is replaced by the
                         C2f module, and the structure of the C2f module is shown in Figure 1f (n denotes the
                         number of bottlenecks). The C2f module adopts a gradient shunt connection to enrich
                         the information flow of the feature extraction network while maintaining a light weight.
                         The CBS module performs a convolution operation on the input information, followed
                         by batch normalization, and finally activates the information stream using SiLU to obtain
                         the output result, as shown in Figure 1g. The backbone network finally uses the spatial
                         pyramid pooling fast (SPPF) module to pool the input feature maps to a fixed-size map for
Sensors 2023, 23, 7190                                                                                                                    4 of 27

                               adaptive size output. Compared with the structure of spatial pyramid pooling (SPP) [32],
       Sensors 2023, 23, x FOR PEER REVIEW
                                      SPPF reduces the computational effort and has lower latency by sequentially 4connecting
                                                                                                                    of 28

                               the three maximum pooling layers, as shown in Figure 1d.

                                  Figure
                               Figure    1. The
                                      1. The    networkstructure
                                              network     structure of
                                                                    of YOLOv8.
                                                                       YOLOv8.The Theww(width)
                                                                                         (width)andand
                                                                                                    r (ratio) in Figure
                                                                                                        r (ratio)       1 are parameters
                                                                                                                   in Figure  1 are parameters
                                  used to represent the size of the feature map. The size of the model can be controlled by setting the
                               used to represent  the  size  of the feature map.  The  size of the  model
                                  values of w and r to meet the needs of diﬀerent application scenarios.
                                                                                                            can   be controlled  by setting the
                               values of w and r to meet the needs of different application scenarios.
                                  2.1. Backbone
                               2.2. Neck
                                        YOLOv8 uses modified CSPDarknet53 [10] as the backbone network, and the input
                                     Inspired
                                   features areby   PANet [33], five
                                                down-sampled       YOLOv8      is obtain
                                                                        times to  designed
                                                                                         five with   a PAN-FPN
                                                                                               diﬀerent              structure
                                                                                                          scale features,         at which
                                                                                                                           in turn,  the neck, as
                               shown    in Figure   1b.  Compared       with  the  neck   structure    of  YOLOv5
                                   we denote as B1–B5. The structure of the backbone network is shown in Figure 1a. Theand   YOLOv7      models,
                               YOLOv8
                                   Cross Stage Partial (CSP) module in the original backbone network is replaced by the C2fwhich
                                          removes     the  convolution     operation   after up-sampling       in  the  PAN    structure,
                               maintains
                                   module, the
                                             andoriginal     performance
                                                 the structure               while achieving
                                                                  of the C2f module   is shown inaFigure
                                                                                                      lightweight      model.
                                                                                                              1f (n denotes   theWe    use P4-P5
                                                                                                                                   number
                               andofN4-N5
                                      bottlenecks).  The C2f
                                              to denote     themodule     adopts ascales
                                                                 two different      gradient   shunt connection
                                                                                           of features     in the PANto enrich   the infor-
                                                                                                                           structure    and FPN
                                   mationof
                               structure   flow
                                              theofYOLOv8
                                                    the feature   extraction
                                                              model,         network Conventional
                                                                        respectively.   while maintaining  FPNa uses
                                                                                                                  light aweight.
                                                                                                                          top-downThe CBS
                                                                                                                                        approach
                                   module deep
                               to convey    performs    a convolution
                                                   semantic               operation
                                                                information.     The on
                                                                                     FPN theenhances
                                                                                              input information,
                                                                                                          the semanticfollowed    by batch of the
                                                                                                                            information
                                   normalization,   and   finally activates the  information    stream  using
                               features by fusing B4-P4 and B3-P3, but some object localization information willSiLU   to obtain   the be
                                                                                                                                       out-
                                                                                                                                          lost. To
                                   put result, as shown in Figure 1g. The backbone network finally uses the spatial pyramid
                               alleviate this problem, PAN-FPN adds PAN to FPN. PAN enhances the learning of location
                                   pooling fast (SPPF) module to pool the input feature maps to a fixed-size map for adaptive
                               information by fusing P4-N4 and P5-N5 to realize path enhancement in a top-down form.
                                   size output. Compared with the structure of spatial pyramid pooling (SPP) [32], SPPF re-
                               PAN-FPN       constructs a top-down and bottom-up network structure, which realizes the
                                   duces the computational eﬀort and has lower latency by sequentially connecting the three
                               complementarity
                                   maximum pooling   of shallow
                                                         layers, aspositional   information
                                                                     shown in Figure    1d.     and deep semantic information through
                               feature fusion, resulting in feature diversity and completeness.
                                  2.2. Neck
                               2.3. Head
                                        Inspired by PANet [33], YOLOv8 is designed with a PAN-FPN structure at the neck,
                                  asThe
                                     shown detection  part
                                              in Figure 1b.of YOLOv8with
                                                            Compared     usesthe
                                                                               a decoupled    head
                                                                                 neck structure     structure,
                                                                                                 of YOLOv5     andas YOLOv7
                                                                                                                     shown inmod-
                                                                                                                                Figure 1e.
                               Theels,
                                    decoupled      head structure
                                       YOLOv8 removes                 uses two
                                                           the convolution       separate
                                                                             operation afterbranches
                                                                                             up-samplingfor in
                                                                                                             object   classification
                                                                                                                the PAN   structure, and
                                  which maintains
                               predicted    bounding  thebox
                                                          original  performance
                                                              regression,        while achieving
                                                                            and different          a lightweight
                                                                                            loss functions     are model.
                                                                                                                     used forWethese
                                                                                                                                use two
                                  P4-P5   and   N4-N5  to denote  the two diﬀerent  scales of features in the  PAN    structure
                               types of tasks. For the classification task, binary cross-entropy loss (BCE Loss) is used. For   and
                               theFPN    structure
                                   predicted    boxofbounding
                                                      the YOLOv8     model, task,
                                                                 regression  respectively. Conventional
                                                                                   distribution  focal lossFPN
                                                                                                             (DFL)uses[34]
                                                                                                                        a top-down
                                                                                                                           and CIoU [35]
                               are employed. This detection structure can improve detection accuracy andinfor-
                                  approach     to convey  deep  semantic  information.  The   FPN  enhances    the  semantic   accelerate
                                  mation of the features by fusing B4-P4 and B3-P3, but some object localization information
                               model   convergence. YOLOv8 is an anchor-free detection model that concisely specifies
                                  will be lost. To alleviate this problem, PAN-FPN adds PAN to FPN. PAN enhances the
                               positive and negative samples. It also uses the Task-Aligned Assigner [36] to dynamically
                                  learning of location information by fusing P4-N4 and P5-N5 to realize path enhancement
                               assign samples, which improves the detection accuracy and robustness of the model.
Sensors 2023, 23, 7190                                                                                                             5 of 27

                                    3. Method
                                              YOLOv8 is a state-of-the-art object detection model and takes into account the multi-
                                        scale nature of objects, using three scale-detection layers to accommodate objects of different
                                        scales. However, the images acquired by UAVs have the problems of complex backgrounds
                                        and a high proportion of small objects. This results in the detection structure of YOLOv8
                                        not meeting the detection requirements in UAV aerial photography scenarios. To mitigate
                                        the above problems, this paper uses YOLOv8 as the base model and optimizes the model
                                        from the perspectives of loss function, attention mechanism, and multiscale feature fusion.
                                        The main ideas of the improvement strategy are as follows:
                                              First, WIoU v3 is utilized as the bounding box regression loss. WIoU v3 incorporates
                                        a dynamic non-monotonic mechanism and designs a sensible gradient gain allocation
                                        strategy, which reduces the occurrence of large or harmful gradients from extreme samples.
                                        WIoU v3 focuses more on samples of ordinary quality, thereby improving the model’s
                                        generalization ability and overall performance.
                                              Then, the dynamic sparse attention mechanism BiFormer is introduced into the back-
                                        bone network. BiFormer reduces computation and memory consumption by filtering out
                                        most of the low-relevance regions in the feature graph and then applying attention to the
                                        high-relevance features. BiFormer improves the model’s attention to the key information
                                        in the input features and optimizes the detection performance of the model.
                                              Finally, the efficient feature processing module FFNB is proposed based on FasterNet.
                                        FFNB has fewer computation and memory accesses during feature processing. Based
                                        on FFNB, we design two new detection layers. Our proposed multiscale feature fusion
                                        network makes the shallow feature and deep feature fully complement each other, which
                                        effectively improves the detection effect of the model on small objects.
                                              We refer to the final improved network model as UAV-YOLOv8, and the overall
                                        framework of the model is shown in Figure 2. To show the structure of the improved model
                                        more concisely and intuitively, we omit the drawing of the C2f module and SPPF module
                                        in Figure 2. In Figure 2, large, medium, small, X-small, and XX-small are used to represent
                                        the size of the object. The improved model changes from the original 3-scale detection
                                        tox 5-scale
                         Sensors 2023, 23,  FOR PEERdetection,
                                                     REVIEW     which effectively improves the overall detection performance of 6the of 28
                                        model, especially for small objects.

                                                     Figure 2. The overall structure of the proposed improved model.
                                    Figure 2. The overall structure of the proposed improved model.
                                                          For ease of reading, we give a notation of the terms involved with the formulas in
                                                     this paper, as shown in Table 1.

                                                     Table 1. Explanation of notations.

                               Notation       Explanation
Sensors 2023, 23, 7190                                                                                                                        6 of 27

                                                  For ease of reading, we give a notation of the terms involved with the formulas in this
                                              paper, as shown in Table 1.

                                              Table 1. Explanation of notations.

                Notation                       Explanation
                                               Loss function
           (cbx , cby ), w, h                  Denote the coordinates of the center point of the prediction box, width, and height, respectively
           gt gt
         (cbx , cby ), w gt , h gt             Denote the coordinates of the center point of the real box, width, and height, respectively
        ρ(w, w gt ), ρ(h, h gt )               Denote the distance of width and height between the real box and the predicted box, respectively
                 cw , ch                       Denote the width and height of the smallest closed box enclosed by the real and predicted boxes
                L∗ IoU , r                     Monotonic focus coefficient and non-monotonic focus factor
                     β                         Degree of outliers
                 γ, δ, α                       Hyperparameters (we can adjust these hyperparameters to fit different models)
                                               BiFormer
                  Q, K, V                      Queries, keys, and values
                                               Linear transformation matrices corresponding to
            WQ, WK, WV
                                               Q, K, and V, respectively
                       dK                      Dimension of the matrix K
             X ∈ R H × E×C                     Dimension of the input feature map
                              2     2
              Ar ∈ R S × S                     Adjacency matrix
                              2
               I r ∈ N S ×k                    Routing index matrix
        I(ri,1) , I(ri,2) , . . . , I(ri,k)    Index values corresponding to the k routing regions with the highest correlation in region i
                 gather (·)                    Gathering key–value pairs
              Attention(·)                     Regular attention computation

                                              3.1. Improved Loss Function
                                                   The object detection task in the UAV aerial photography scene has a high proportion of
                                              small objects, so a reasonably designed loss function can significantly improve the detection
                                              performance of the model. YOLOv8 uses DFL and CIoU to calculate the regression loss of
                                              the bounding box, but CIoU has the following drawbacks: first, CIoU does not consider
                                              the balance of difficult and easy samples. Second, CIoU uses the aspect ratio as one of the
                                              penalty factors of the loss function, and if the aspect ratio of the real box and the predicted
                                              box are the same, but the values of width and height are different, the penalty term cannot
                                              reflect the real difference between these two boxes. Third, the calculation of the CIoU
                                              formula involves an inverse trigonometric function, which will increase the consumption
                                              of model arithmetic power. The formula of CIoU is shown in Equation (1):

                                                                                      ρ2 (b, b gt )           4        −1 w
                                                                                                                            gt        w
                                                             LCIoU = 1 − IoU +                            +      ( tan         − tan−1 )         (1)
                                                                                   ( c w )2 + ( c h )   2     π2          h gt        h

                                                   In Equation (1), Intersection over Union (IoU) denotes the intersection ratio of the
                                              prediction box and the real box. Some of the parameters involved in Equation (1) are shown
                                              in Figure 3. ρ(b, b gt ) denotes the Euclidean distance between the centroids of the real box
                                              and the prediction box; h and w denote the height and the prediction box; h gt and w gt
                                              denote the height and the width of the real box; ch and cw denote the height and the width
                                              of the minimum enclosing box formed by the prediction box and the real box.
Sensors
Sensors2023,
        2023,23,
             23, x7190
                   FOR PEER REVIEW                                                                                                             8 7ofof28
                                                                                                                                                       27

                                           Schematicdiagram
                                Figure3.3.Schematic
                                Figure              diagramof
                                                            ofthe
                                                               theparameters
                                                                  parametersof
                                                                             ofthe
                                                                                theloss
                                                                                    loss function.
                                                                                          function.

                                      EIoU[38]
                                     SIoU    [37]introduces
                                                  improves based       on between
                                                               the angle  CIoU by thetreating the length
                                                                                         predicted        and
                                                                                                    box and   width
                                                                                                            the       separately
                                                                                                                 real box        as
                                                                                                                          as a pen-
                                 penalty terms,   reflecting  the  difference in  width  and  height  between  the real box and
                                alty factor for the first time. Firstly, based on the magnitude of the angle (as in Figure 3,   the
                                θpredicted
                                    and α )box,   whichthe
                                              between     is predicted
                                                             more reasonable
                                                                         box andcompared      with
                                                                                   the real box, thethe penalty box
                                                                                                     predicted  term  of CIoU.
                                                                                                                    rapidly     The
                                                                                                                             moves
                                 formula  of  EIoU  is shown    in Equation  (2):
                                towards the nearest axis and then regresses towards the real box. SIoU reduces the degrees
                                of freedom of the regression and speeds               up the convergence            of the model.
                                                                                 ρ2 (b, b gt )         ρ2 (w, w gt ) ρ2 (h, h gt )
                                      While several  L EIoU   = 1 − IoU loss
                                                            mainstream     + functions           introduced
                                                                                                   +               above
                                                                                                                       + take2 a static focusing      (2)
                                mechanism, WIoU not only considers                 )2 +aspect,
                                                                              (cwthe       (ch )2 centroid(cw )2distance,(cand h ) overlap area but
                                also introduces a dynamic non-monotonic focusing mechanism. WIoU applies a reasona-
                                       Some of the parameters involved in Equation (2) are shown in Figure 3; ρ(w, w gt )
                                ble gradient    gain allocation strategy to evaluate the quality of the anchor box. Tong et al.
                                 and ρ(h, h gt ) denote the Euclidean distance of width and Euclidean distance of height
                                [31] proposed three versions of WIoU. WIoU v1 was designed with attention-based                         gt gt      pre-
                                 between the real box and the prediction box, respectively; (cbx , cby ) and (cbx , cby ) denote
                                dicted box loss, and WIoU v2 and WIoU v3 added focusing coeﬃcients.
                                 the coordinates      of the center
                                      WIoU v1 introduces               pointsasofathe
                                                                   distance             real box
                                                                                    metric            and the prediction
                                                                                                of attention.      When the box,       respectively.
                                                                                                                                  object  box and the
                                       SIoU   [38]  introduces    the  angle  between       the  predicted       box
                                predicted box overlap within a certain range, the penalty of reducing the geometric   and   the  real box  as a penalty
                                                                                                                                                 metric
                                 factor for  the first    time. Firstly, based   on  the   magnitude        of  the
                                makes the model obtain better generalization ability. The formula for calculating   angle    (as  in Figure  3, θ WIoU
                                                                                                                                                  and α)
                                 between
                                v1  is showntheinpredicted
                                                   Equations    box  and the real box, the predicted box rapidly moves towards the
                                                                  (3)–(5):
                                 nearest axis and then regresses towards the real box. SIoU reduces the degrees of freedom
                                 of the regression and speeds up theLconvergenceWIoUv1 = RWIoUof×the     LIoUmodel.                                  (3)
                                       While several mainstream loss functions introduced above take a static focusing
                                 mechanism, WIoU not only considers the             (bcgtxaspect,
                                                                                            − bcx ) 2centroid
                                                                                                       + (bcgty −distance,
                                                                                                                   bc y ) 2 and overlap area but
                                                                     WIoU = exp(
                                 also introduces a dynamicRnon-monotonic                                                   ) applies a reasonable
                                                                                       focusing2 mechanism.  2           WIoU                        (4)
                                 gradient gain allocation strategy to evaluate the quality
                                                                                               ( c w   +  c    )
                                                                                                           h of the anchor box. Tong et al. [31]

                                 proposed three versions of WIoU. WIoU v1 was designed with attention-based predicted
                                                                                  LIoU = 1 − IoU                                                     (5)
                                 box loss, and WIoU v2 and WIoU v3 added                    focusing coefficients.
                                       WIoUv2
                                      WIoU      v1isintroduces
                                                     applied to distance
                                                                    WIoU v1as   byaconstructing
                                                                                     metric of attention.           When focus
                                                                                                        the monotonic        the object    box andL∗ the
                                                                                                                                     coeﬃcient       IoU

                                ,predicted    box overlap
                                  which eﬀectively             within
                                                           reduces  theaweight
                                                                          certainofrange,
                                                                                     simple   the  penalty of
                                                                                                 examples       in reducing     the geometric
                                                                                                                   the loss value.     However,metric
                                                                                                                                                   con-
                                 makes the
                                sidering   thatmodelL∗ IoUobtain better generalization
                                                             decreases    as LIoU decreases   ability.during
                                                                                                         The formula
                                                                                                                   modelfor     calculating
                                                                                                                             training,        WIoU in
                                                                                                                                          resulting    v1
                                 is shown in Equations (3)–(5):
                                slower convergence, the average of LIoU is introduced to normalize L∗ IoU . The formula
                                of WIoU v2 is shown in EquationL(6):         W IoUv1 = RW IoU × L IoU                                                 (3)
                                                                                   L∗         γ 2
                                                                      LWIoUv 2 = ((bcgtxIoU
                                                                                          − )bcx×) L+ (bc1y, γ− >
                                                                                                                      2
                                                                                                                bcy0)
                                                                                                         gt
                                                                                                    WIoUv                                           (6)
                                                                 RW IoU = exp( IoU L              2      2
                                                                                                                        )                            (4)
                                                                             (cw + ch )
                                    WIoU v3 defines the outlier β to measure the quality of the anchor box, constructs
                                a non-monotonic focus factor r based  on =β1,−
                                                                   L IoU      and  applies r to WIoU v1. A small value
                                                                                 IoU                                   (5)
                                of β indicates a high anchor box quality, and a smaller r is assigned to it, reducing the
                                weight of high-quality anchor frames in the larger loss function. A large value of β
Sensors 2023, 23, 7190                                                                                               8 of 27

                             WIoU v2 is applied to WIoU v1 by constructing the monotonic focus coefficient L∗ IoU ,
                         which effectively reduces the weight of simple examples in the loss value. However,
                         considering that L∗ IoU decreases as L IoU decreases during model training, resulting in
                         slower convergence, the average of L IoU is introduced to normalize L∗ IoU . The formula of
                         WIoU v2 is shown in Equation (6):

                                                                    L∗ IoU γ
                                                     LW IoUv2 = (         ) × LW IoUv1 , γ > 0                          (6)
                                                                    L IoU

                              WIoU v3 defines the outlier β to measure the quality of the anchor box, constructs a
                         non-monotonic focus factor r based on β, and applies r to WIoU v1. A small value of β
                         indicates a high anchor box quality, and a smaller r is assigned to it, reducing the weight
                         of high-quality anchor frames in the larger loss function. A large value of β indicates a
                         low-quality anchor box, and a small gradient gain is assigned to it, which reduces the
                         harmful gradients generated by low-quality anchor boxes. WIoU v3 uses a reasonable
                         gradient gain allocation strategy to dynamically optimize the weight of high- and low-
                         quality anchor boxes in the loss, which makes the model focus on the average quality
                         samples and improves the overall performance of the model. The WIoU v3 formulas
                         are shown in Equations (7)–(9). δ and α in Equation (8) are hyperparameters that can be
                         adjusted to fit different models.

                                                              LW IoUv3 = r × LW IoUv1                                   (7)

                                                                            β
                                                                     r=                                                 (8)
                                                                          δα β−δ
                                                                    L∗ IoU
                                                              β=           ∈ [0, +∞)                                    (9)
                                                                    L IoU
                              By comparing the several mainstream loss functions above, we finally introduce
                         WIoU v3 in the object bounding box regression loss. On the one hand, WIoU v3 takes into
                         account some advantages of EIoU and SIoU, which is in line with the design concept of
                         the excellent loss function. On the other hand, WIoU v3 uses a dynamic non-monotonic
                         mechanism to evaluate the quality of anchor boxes, which makes the model focus more on
                         anchor boxes of ordinary quality and improves the model’s ability to localize objects. For
                         the object detection task in the UAV aerial photography scene, the high proportion of small
                         objects increases the detection difficulty, and WIoU v3 can dynamically optimize the loss
                         weights of small objects to improve the detection performance of the model.

                         3.2. Efficient Attention Mechanism
                               Due to the complex backgrounds and high proportion of small objects in images
                         captured by UAVs, many detection models have a poor ability to suppress background
                         information. To make the detection model focus more on the key information in the input
                         features and less on the background information, we introduce a dynamic sparse attention
                         mechanism called BiFormer in the backbone network of the model. BiFormer utilizes
                         query adaptation to first filter out the most irrelevant key–value pairs in coarse-grained
                         regions of the input feature graph, efficiently find key–value pairs with high relevance, and
                         then perform attention computation. This significantly reduces computation and storage
                         consumption and enhances the model’s perception of the input content.
                               YOLOv8 is a convolutional neural network (CNN) model, and a CNN is essentially
                         local processing, so the relationships between global features cannot be obtained. Compared
                         with traditional CNN models, the transformer uses an attention mechanism to obtain the
                         degree of correlation between data and other data, with the property of a global sensing
                         field. An effective attention mechanism can build robust and powerful data-driven models,
                         making the models more flexible when dealing with complex and large data. The attentional
                         mechanism works as follows: first, [ x1 , x2 , x3 , · · · , x T ] is acquired by encoding the input
Sensors 2023, 23, 7190                                                                                                                 9 of 27

                                        data sequence [ a1 , a2 , a3 , · · · , a T ]. Then, three matrices of queries Q, keys K, and values V
                                        are obtained by linear transformation matrices W Q , W K , and W V , respectively. The dot
                                        product between the query and the corresponding key is computed,         √       then normalized, and
                                        finally multiplied with matrix V to obtain the weighted sum. dK is introduced to prevent
                                        the gradient of the result from vanishing, and dK denotes the dimensionality of the matrix
                                        K. The
                   Sensors 2023, 23, x FOR  PEERformula
                                                 REVIEW for attention is shown in Equation (10):                                                   10 of

                                                                                                        QK T
                                                                 Attention( Q, K, V ) = so f tmax ( √ )V                                   (10)
                                                                                                          dK
                                                         However, the conventional attention mechanism              has the drawbacks of high comp
                                          However,tational   complexityattention
                                                    the conventional       and large    memory usage.
                                                                                      mechanism            Detection
                                                                                                     has the drawbacks models   deployed
                                                                                                                           of high  computa- on UAV pl
                                                   forms   are resource-constrained,      and  if  a conventional   attention
                                    tional complexity and large memory usage. Detection models deployed on UAV platforms       module    is introduced
                                                   rectly into the
                                    are resource-constrained,    andmodel,   it will occupy
                                                                      if a conventional       most ofmodule
                                                                                           attention     the platform   resources
                                                                                                                is introduced       and reduce
                                                                                                                                 directly  into the inf
                                    the model, it will occupy most of the platform resources and reduce the inference speed of research
                                                   ence  speed   of the  model.   To  ease  the  computational    and   memory     problems,
                                    the model. To have   proposed
                                                   ease the          to reduce
                                                             computational        resource
                                                                                and   memory consumption     by replacing
                                                                                                problems, researchers        global
                                                                                                                          have        queriestowith spa
                                                                                                                                 proposed
                                                   queries  that  focus   on only   some   key–value    pairs. Since  then,
                                    reduce resource consumption by replacing global queries with sparse queries that focus onmany    related  works bas
                                                   on  this research   idea  have    appeared,    such  as local attention,
                                    only some key–value pairs. Since then, many related works based on this research idea    deformable      attention, a
                                                   expansive    attention,  but  all of them   are   manually  produced     static
                                    have appeared, such as local attention, deformable attention, and expansive attention, but     patterns   and  conte
                                    all of them areindependent     sparsity. To
                                                     manually produced            solve
                                                                              static     these problems,
                                                                                      patterns               Lei Zhu et al. [30]sparsity.
                                                                                                 and content-independent           proposed  Toa novel d
                                                   namic   sparse  attention:  the  Bi-Level  Routing    Attention,  whose
                                    solve these problems, Lei Zhu et al. [30] proposed a novel dynamic sparse attention: the workflow     is shown in F
                                                   ure  4a.
                                    Bi-Level Routing Attention, whose workflow is shown in Figure 4a.

                                                                        (a)                                                     (b)
                                                     Figure 4.
                                    Figure 4. (a) Structure of(a)
                                                               theStructure
                                                                   Bi-Level of the Bi-Level
                                                                            Routing         Routing
                                                                                      Attention; (b) Attention; (b)the
                                                                                                     Structure of   Structure of block.
                                                                                                                       Biformer  the Biformer block.

                                         From Figure From
                                                      4a, it can be 4a,
                                                             Figure seen   thatbe
                                                                        it can  theseen
                                                                                     input
                                                                                         thatfeature    map
                                                                                                the input   feature R H ×WX×C∈ is
                                                                                                              X ∈ map          R Hfirstly
                                                                                                                                   ×W × C
                                                                                                                                          is firstly
                                                                                                      HW
                                    divided into S × S subregions, and each region contains S2 featureHW          vectors. We change
                                                 vided into S × S subregions,
                                                                      S2 × HW  ×C and each region contains          2
                                                                                                                        feature vectors. We chan
                                    the shape of X to obtain X r ∈ R        S2   . Then, the feature vectorsS are linearly trans-
                                                                                            HW
                                    formed to derive the three matrices, Q, K, and     S 2 ×The
                                                                                      V.       ×C calculation formulae are shown in
                                                 the shape of X to obtain X r ∈ R S
                                                                                             2
                                                                                                   . Then, the feature vectors are linearly tran
                                    Equations (11)–(13):
                                                 formed to derive the three matrices,r QQ , K , and V . The calculation formulae are show
                                                                              Q=XW                                                   (11)
                                                 in Equations (11)–(13):

                                                                                  K = Xr W k      Q = X rW Q                             (12)          (1

                                                                                          r   V
                                                                                                  K = X rW k                                           (1
                                                                                  V=XW                                                   (13)
                                         Then, the attention relation from region to region V     = X rW Vby constructing a directed
                                                                                               is obtained
                                                                                                                                                (1
                                    graph to locate its related regions
                                                         Then, the       for a relation
                                                                    attention  given region.  The specific
                                                                                        from region         implementation
                                                                                                     to region                 process
                                                                                                                  is obtained by       is
                                                                                                                                  constructing a
                                    as follows: Q and
                                                  rectedV for each
                                                           graph  toregion
                                                                     locate are  processed
                                                                            its related     by region
                                                                                        regions       averaging
                                                                                                for a given         to obtain
                                                                                                               region.        the region
                                                                                                                       The specific implementati
                                                    r ∈ RS2is
                                    level Qr and Kprocess    ×Cas
                                                                . Then,  theQdotand
                                                                  follows:            V forofeach
                                                                                  product     Qr and   K r isare
                                                                                                   region        processedtoby
                                                                                                               calculated       region
                                                                                                                              obtain theaveraging
                                                                                                   2
                                                    obtain the region level Q r and K r ∈ R S ×C . Then, the dot product of Q r and K r is c
                                                                                                             2   2
                                                    culated to obtain the adjacency matrix Ar ∈ R S ×S , which is used to measure the int
                                                    region correlation, and the formula is shown in Equation (14):
                                                                                                   r     r       r T
Sensors 2023, 23, 7190                                                                                                         10 of 27

                                                         2   2
                         adjacency matrix Ar ∈ RS ×S , which is used to measure the inter-region correlation, and
                         the formula is shown in Equation (14):

                                                                       Ar = Qr ( K r ) T                                          (14)

                              Next, Ar is pruned. The least relevant token in Ar is filtered out at the coarse-grained
                         level, and the top k most relevant regions in Ar are retained to obtain the routing index
                                          2
                         matrix, I r ∈ N S ×k . The calculation formula is shown in Equation (15):

                                                                    I r = topkIndex ( Ar )                                        (15)

                              Subsequently, token-to-token attention is used at the fine-grained level. For queries in
                         the region i, this attention is focused only on the k routing regions where I(ri,1) , I(ri,2) , . . . , I(ri,k)
                         are indexed and collects all the K and V tensors in these k regions to acquire K g and V g .
                         The calculated formula are shown in Equations (16)–(17):

                                                                    K g = gather (K, I r )                                        (16)

                                                                    V g = gather (V, I r )                                        (17)
                              Finally, the collected K g and V g are processed with attention, and a local context
                         enhancement term LCE(V ) is added to obtain the output tensor O. The formula is shown
                         in Equation (18):
                                                    O = Attention( Q, K g , V g ) + LCE(V )                   (18)
                              The BiFormer block is designed based on Bi-Level Routing Attention, as shown in
                         Figure 4b. The DWConv in this block denotes deep separable convolution, which can reduce
                         the number of parameters and computation of the model. LN denotes layer normalization
                         processing, which can accelerate the training and improve the generalization ability of the
                         model. MLP denotes a multilayer perceptron, which further processes and adjusts the
                         attention weights to enhance the model’s attention to different features. The add symbol in
                         Figure 4b indicates connecting two feature vectors.
                              In this paper, the BiFormer block is introduced into the backbone network. On the one
                         hand, BiFormer can take into account the limited computing power and storage resources
                         of the UAV hardware platform. On the other hand, the dynamic attention mechanism
                         in this block can improve the model’s attention to the vital information of the object and
                         optimize the detection performance of the model. To make full use of the efficient attention
                         mechanism in this block, we use the BiFormer block between B3 and B4 of the model’s
                         backbone network, replacing the original C2f block.

                         3.3. Multiscale Feature Fusion Network
                              Poor detection of small objects is one of the challenges in object detection tasks in the
                         context of UAV aerial photography. In many existing works [39–42], detection scales are
                         added to the model to reduce the missed detection rate of small objects, which is an effective
                         improvement method. However, this approach can complicate the structure of the model
                         and increase the consumption of computational and storage resources. To mitigate this
                         problem, a feature processing block called FFNB is proposed in this paper, and a multiscale
                         feature fusion network is designed based on this block. The detection accuracy of small
                         objects is greatly improved while reducing the excessive consumption of resources.
                              Object detection tasks for UAV platforms are limited by computational resources, and
                         models with simple structure, low latency, and high data throughput are sought. Some
                         classical lightweight networks, such as MobileNet [43], ShuffleNet [44], and GhostNet [45],
                         are using deep convolution or group convolution to extract the spatial features of images.
                         Deep convolution reduces the input of feature dimensions by convolving the input images
                         grouped in feature dimensions, reducing the number of parameters while keeping the
Sensors 2023, 23, 7190                                                                                                                   11 of 27

                                  feature information largely unchanged. Group convolution can be seen as a sparse form of
                                  traditional convolution, where the input channels are convolved one by one, which can be
                                  used to reduce the model parameters and achieve the purpose of lightweight models. Most
Sensors 2023, 23, x FOR PEER REVIEW
                                  of these lightweight models focus on reducing the number of floating-point operations           12 of 28
                                  (FLOPs), and very little related work considers the low floating-point operations per second
                                  (FLOPS) of the model. However, the reduction in model parameters does not translate
                                  exactly  intoper
                                  operations     an second
                                                    increase   in the computational
                                                             (FLOPS)                     speed of the
                                                                        of the model. However,     the reduction
                                                                                                       model. Therefore,
                                                                                                                   in model some    work
                                                                                                                              parameters
                                  using  deep
                                  does not      convolution
                                             translate         orinto
                                                         exactly  group   convolution
                                                                       an increase      in computational
                                                                                   in the   an attempt to design
                                                                                                            speed lightweight
                                                                                                                    of the model.and  fast
                                                                                                                                   There-
                                  neural  network
                                  fore, some    workblocks,
                                                        using in  some
                                                               deep      cases, does
                                                                      convolution    ornot
                                                                                        groupspeed up the model
                                                                                                 convolution   in anoperation
                                                                                                                      attempt and   even
                                                                                                                               to design
                                  exacerbates
                                  lightweight theandlatency.
                                                       fast neural network blocks, in some cases, does not speed up the model
                                        For an  input
                                  operation and even    feature          h × latency.
                                                                 of size the
                                                           exacerbates        w × c, the required FLOPs using regular convolution
                                  of size k ×  k
                                        For an input feature of size h × w × cThe
                                                 are  shown   in  Equation   (19). , thec required
                                                                                           in Equation  (19)using
                                                                                                    FLOPs    represents   theconvolution
                                                                                                                    regular   number of
                                  channels   of the  input  data.
                                  of size k × k are shown in Equation (19). The c in Equation (19) represents the number
                                  of channels of the input data.
                                                                       FLOPsConv = h × w × k2 × c2                       (19)
                                                                         FLOPsConv = h × w × k 2 × c 2                   (19)
                                       The deep convolution kernel performs a sliding operation on the input channel space
                                       The deep
                                  to derive      convolution
                                            the output       kernel
                                                       channel      performs
                                                               features,      a sliding
                                                                         and the FLOPsoperation  on the input are
                                                                                        for deep convolution  channel  space
                                                                                                                  calculated
                                  to derive the output channel
                                  as shown in Equation (20):   features, and the FLOPs  for deep convolution  are calculated
                                  as shown in Equation (20):
                                                               FLOPs DWConv = h × w × k2 ×
                                                                 FLOPsDWConv = h × w × k 2 ×cc                           (20)
                                                                                                                         (20)
                                        The
                                        The depth
                                            depth convolution
                                                  convolution computation
                                                              computation process
                                                                          process is
                                                                                   is shown
                                                                                      shown in
                                                                                             in Figure
                                                                                                Figure5a.
                                                                                                       5a.

                                 (a)                                                                      (b)
                                  Figure 5.
                                  Figure  5. Comparison
                                             Comparison of
                                                         of DWConv
                                                            DWConv and
                                                                     and PConv. (a) Structure
                                                                         PConv. (a)           diagram of
                                                                                    Structure diagram of deep
                                                                                                         deep convolution;
                                                                                                              convolution; (b)
                                                                                                                           (b) struc-
                                                                                                                               struc-
                                  ture diagram of partial convolution.
                                  ture diagram of partial convolution.

                                         The popular
                                        The   populardeepdeepconvolution
                                                                  convolutioneffectively
                                                                                 eﬀectivelyreduces
                                                                                               reducesthethe parameters
                                                                                                           parameters     of of
                                                                                                                             thethe  model.
                                                                                                                                  model.   ButBut
                                                                                                                                               in
                                   in practical   application,     depth   convolution    needs   to be  followed    by  additional
                                  practical application, depth convolution needs to be followed by additional point-by-point           point-by-
                                   point convolution
                                  convolution     or otherorcomputational
                                                               other computational
                                                                                costs tocosts   to compensate
                                                                                         compensate                for the reduction
                                                                                                        for the reduction               in accu-
                                                                                                                              in accuracy   after
                                   racy  after the  convolution      operation.   This introduces     additional    memory
                                  the convolution operation. This introduces additional memory access costs and increases      access  costs and
                                   increasesTo
                                  latency.     latency.
                                                  relieveTo therelieve
                                                                 abovethe    above problem,
                                                                          problem,   Chen et al. Chen
                                                                                                    [29]etproposed
                                                                                                           al. [29] proposed
                                                                                                                      a simple aand  simple  and
                                                                                                                                        efficient
                                   eﬃcient convolution:
                                  convolution:                partial convolution
                                                    partial convolution      (PConv). (PConv).
                                                                                        PConv PConv        uses regular
                                                                                                  uses regular             convolution
                                                                                                                   convolution            to per-
                                                                                                                                   to perform   a
                                   form a convolution
                                  convolution      operation operation
                                                                 on someon  ofsome   of the continuous
                                                                               the continuous      features features    in the
                                                                                                             in the input        input channel,
                                                                                                                             channel,   and the
                                   and the remaining
                                  remaining     features arefeatures    are processed
                                                                processed   by identityby    identitykeeping
                                                                                          mapping,     mapping, thekeeping
                                                                                                                     channel the    channel un-
                                                                                                                                unchanged.    We
                                   changed.    We   perform      the  convolution    calculation    for the  first  consecutive
                                  perform the convolution calculation for the first consecutive feature with channel number        feature   with
                                  cchannel
                                    p in the number      c p in the
                                             input features,           input features,
                                                                  as shown    in Figureas 5b,shown   in Figure
                                                                                              and derive         5b, and derive
                                                                                                            the formula             the formula
                                                                                                                            for calculating   the
                                  FLOPs    of  PConv    as  shown    in  Equation   (21):
                                   for calculating the FLOPs of PConv as shown in Equation (21):
                                                                                                      2         2
                                                                       FLOPs
                                                                     FLOPs       = h=×
                                                                              PConv
                                                                           PConv     h× ××k2k××c pc2p
                                                                                       ww                                                   (21)
                                                                                                                                            (21)
                                        If c pc pis 1/4
                                        If          is 1/4
                                                         ofof the
                                                            the   number
                                                                number  of of input
                                                                           input    feature
                                                                                 feature    channels
                                                                                         channels      c ,FLOPs
                                                                                                  c, the   the FLOPs   of PConv
                                                                                                                 of PConv         are 1/16
                                                                                                                            are only  only
                                  1/16
                                  of theofconventional
                                             the conventional       convolution.
                                                              convolution.         This convolution
                                                                            This convolution  reducesreduces    the number
                                                                                                       the number    of memoryof memory
                                                                                                                                 accesses
                                  accesses
                                  while        while reducing
                                           reducing                the parameters,
                                                          the parameters,            and eﬃciently
                                                                            and efficiently extractsextracts   the spatial
                                                                                                      the spatial  featuresfeatures of the
                                                                                                                             of the input
                                  input information. Chen et al. proposed the FasterNet block based on PConv, which is a
                                  module consisting of a PConv layer and two 1 1 convolutional layers connected sequen-
                                  tially, as shown in Figure 6a. The add symbol in Figure 6a indicates connecting two feature
                                  vectors. The overuse of normalization and activation layers may lead to a reduction in
  Sensors 2023, 23, 7190                                                                                                                               12 of 27

                                     information. Chen et al. proposed the FasterNet block based on PConv, which is a module
Sensors 2023, 23, x FOR PEER REVIEW
                                     consisting of a PConv layer and two 1 × 1 convolutional layers connected sequentially,
                                                                                                                       13 of 28
                                     as shown in Figure 6a. The add symbol in Figure 6a indicates connecting two feature
                                     vectors. The overuse of normalization and activation layers may lead to a reduction in
                                     feature diversity, which may affect the performance of the model. Therefore, the FasterNet
                                  FasterNet   block
                                     block uses     has a simpleand
                                                 normalization   structure andlayers
                                                                    activation  a low only
                                                                                      number   ofthe
                                                                                           after  parameters for faster opera-
                                                                                                     second convolutional   layer.
                                  tion.
                                     FasterNet block has a simple structure and a low number of parameters for faster operation.

                                            (a)                               (b)
                               Figure 6. Comparison
                                 Figure  6. Comparison of FasterNet  blockblock
                                                           of FasterNet    and Focal  FasterNet
                                                                                and Focal       block.block.
                                                                                           FasterNet   (a) Structure  diagramdiagram
                                                                                                               (a) Structure  of Fast- of
                               erNet block; block;
                                 FasterNet  (b) structure diagram
                                                   (b) structure    of our of
                                                                 diagram   proposed  module.
                                                                              our proposed  module.

                                      In Inthisthispaper,
                                                     paper,  we we revisit
                                                                     revisitthethestructure
                                                                                     structureofofthe theFasterNet       block.AA1 1× ×
                                                                                                           FasterNetblock.               1 convolutional
                                                                                                                                            1 convolutional
                                  layer
                               layer        is used
                                       is used          in this
                                                    in this   block,block,
                                                                       which which      can reduce
                                                                                can reduce              the number
                                                                                                the number               of parameters,
                                                                                                                 of parameters,      speed up  speed     up the
                                                                                                                                                   the train-
                               ingtraining
                                     and increaseand increase        the nonlinear
                                                          the nonlinear                  fittingofability
                                                                              fitting ability                of theHowever,
                                                                                                    the model.        model. However,
                                                                                                                                   the receptivethe receptive
                                                                                                                                                      field of
                               1 ×field   of 1 × 1 convolution
                                    1 convolution           is relativelyissmallrelatively    small
                                                                                       and lacks    in and    lacks in
                                                                                                        acquiring        acquiring
                                                                                                                      global            global
                                                                                                                                features.   It is features.
                                                                                                                                                   also con- It
                                  is  also    considered        that   the  FasterNet       block   uses    only   one
                               sidered that the FasterNet block uses only one shortcut connection, and the input featuresshortcut     connection,       and the
                                  input      features     are   convolved       through      three   layers,   in  turn,
                               are convolved through three layers, in turn, which may lead to network degradation and      which     may   lead    to  network
                                  degradation
                               feature                 and feature
                                           disappearance           as thedisappearance
                                                                            depth of the as      the depth
                                                                                              model            of thetomodel
                                                                                                        continues        deepen. continues
                                                                                                                                     To solvetothe deepen.
                                                                                                                                                        aboveTo
                                  solve thethe
                               problems,          above
                                                      FFNB problems,
                                                               is proposedthe FFNB
                                                                                 in thisispaper
                                                                                           proposedbased in on
                                                                                                            thisthe
                                                                                                                  paper    based block,
                                                                                                                     FasterNet      on the and
                                                                                                                                            FasterNet     block,
                                                                                                                                                  the struc-
                                  and
                               ture   is the
                                         shown  structure     is shown
                                                      in Figure     6b. in Figure 6b.
                                          First,
                                      First,        PConv
                                                 PConv      is is
                                                               usedused toto  replace
                                                                           replace     the    two1 1× ×
                                                                                         thetwo            1 convolutional
                                                                                                        1 convolutional           layers
                                                                                                                               layers   in in
                                                                                                                                            thethe   FasterNet
                                                                                                                                                  FasterNet
                                  block,      which     improves       the   receptive     field  while    making
                               block, which improves the receptive field while making the original module faster and   the   original   module       faster and
                                  more     efficient.      Second,     the  residual     concatenation       is added
                               more eﬃcient. Second, the residual concatenation is added to the last two convolutional    to  the  last two   convolutional
                                  layers
                               layers    in inthethe    block
                                                    block         to enrich
                                                             to enrich     the the    features
                                                                                features          of output
                                                                                             of the   the output      information,
                                                                                                                information,      reducereduce
                                                                                                                                            the lossthe of
                                                                                                                                                         loss
                                                                                                                                                           ef- of
                                  effective
                               fective           features,
                                          features,      andand      optimize
                                                                optimize           the detection
                                                                             the detection            performance
                                                                                                performance             of model.
                                                                                                                   of the   the model.
                                      Most of the current mainstream object detection models useconvolutional
                                          Most     of  the   current    mainstream       object   detection     models    use     convolutionalneural  neuralnet-
                                  works       to  extract     object   features.     As   the  number      of  convolutions
                               networks to extract object features. As the number of convolutions increases, the semantic         increases,     the   semantic
                                  information
                               information         of of
                                                       thethe   input
                                                             input       features
                                                                      features        gradually
                                                                                  gradually        becomes
                                                                                                becomes          richer,
                                                                                                             richer,   butbutthethe  detailed
                                                                                                                                  detailed       features
                                                                                                                                             features       will
                                                                                                                                                          will
                               become fewer and fewer, which is one of the main reasons for the low detection accuracy of
                                  become        fewer    and   fewer,    which    is  one  of the  main    reasons    for  the  low  detection     accuracy
                               of many
                                   manyobject objectdetection
                                                        detection   models
                                                                       models for for
                                                                                   small   objects.
                                                                                        small        Although
                                                                                                objects.   AlthoughYOLOv8YOLOv8uses auses
                                                                                                                                        multiscale     detection
                                                                                                                                              a multiscale
                                  method, it still cannot meet the detection needs of UAV aerial photography scenarios, which
                               detection method, it still cannot meet the detection needs of UAV aerial photography sce-
                                  leads to the unsatisfactory detection accuracy of the model for small objects.
                               narios, which leads to the unsatisfactory detection accuracy of the model for small objects.
                                          To improve the detection accuracy of small objects and consider the limited resources
                                      To improve the detection accuracy of small objects and consider the limited resources
                                  of the platform, this paper uses the efficient FFNB to design the feature fusion network. We
                               of the platform, this paper uses the eﬃcient FFNB to design the feature fusion network.
                                  add two new detection scales to the original three detection scales of YOLOv8 and fuse the
                               We add two new detection scales to the original three detection scales of YOLOv8 and
                                  shallow information of B1 and B2, which are richer in location information. The FFNB is
                               fuse the shallow information of B1 and B2, which are richer in location information. The
                                  added as a feature processing block between B1 and B2 of the backbone network, and then
                               FFNB is added as a feature processing block between B1 and B2 of the backbone network,
                                  the original C2f block between B2 and B3 is replaced using this block. The introduced FFNB
                               and then the original C2f block between B2 and B3 is replaced using this block. The intro-
                                  can ease the resource consumption caused by multiscale feature fusion. The improved
                               duced FFNB can ease the resource consumption caused by multiscale feature fusion. The
                                  model achieves a five-scale detection, as shown in Figure 7, which effectively improves the
                               improved model achieves a five-scale detection, as shown in Figure 7, which eﬀectively
                                  detection performance of the model.
                               improves the detection performance of the model.
  Sensors 2023, 23, x FOR PEER REVIEW                                                                                                        14 of 28
Sensors 2023,
   Sensors    23,23,
           2023, x FOR
                     7190PEER REVIEW                                                                                                      14 of
                                                                                                                                              1328
                                                                                                                                                of 27

                                                             (a)                                       (b)
                                                          (a)                                        (b)
                                       Figure 7. (a) Detection head of YOLOv8; (b) detection head of our proposed method.
                                  Figure 7. (a)
                                     Figure      Detection
                                             7. (a)        head
                                                    Detection   of YOLOv8;
                                                              head         (b)(b)
                                                                   of YOLOv8;  detection head
                                                                                  detection   of our
                                                                                            head     proposed
                                                                                                 of our       method.
                                                                                                        proposed method.
                                     4. Experiments
                                     4. Experiments
                                  4. Experiments
                                     4.1. Experiment Introduction
                                     4.1. Experiment Introduction
                                  4.1. Experiment    Introduction
                                           This section    first introduces the dataset used in this paper, then introduces the exper-
                                           This section first introduces the dataset used in this paper, then introduces the experi-
                                     imental    environment
                                        This section             and training
                                                        first introduces             strategy,
                                                                              the dataset        andinfinally
                                                                                              used             introduces
                                                                                                       this paper,           the evaluation
                                                                                                                    then introduces            metrics
                                                                                                                                         the exper-
                                     mental environment and training strategy, and finally introduces the evaluation metrics
                                     related
                                  imental      to the experimental
                                            environment       and training results.
                                                                                 strategy, and finally introduces the evaluation metrics
                                     related to the experimental results.
                                  related to the experimental results.
                                     4.1.1. Dataset
                                     4.1.1.  Dataset
                                  4.1.1. Dataset
                                           The VisDrone2019
                                           The   VisDrone2019 dataset dataset[46][46]isisone
                                                                                           oneofof
                                                                                                 thethe
                                                                                                      mainstream
                                                                                                         mainstream  UAVUAV aerial photography
                                                                                                                                aerial  photography da-
                                     tasets,
                                        The   which   was
                                              VisDrone2019  collected
                                                                 dataset  and  developed
                                                                            [46]  is one   of  by
                                                                                              the Tianjin   University
                                                                                                   mainstream     UAV    and
                                                                                                                        aerial
                                     datasets, which was collected and developed by Tianjin University and the data mining    the  data  mining
                                                                                                                                photography       team
                                                                                                                                                 da-
                                     AISKYEYE.
                                  tasets,
                                     team which
                                            AISKYEYE.Thecollected
                                                   was     dataset    is
                                                                      and
                                                            The dataset  framed     in more
                                                                            developed
                                                                             is framed         than athan
                                                                                           bymore
                                                                                           in  Tianjin dozen    diﬀerent
                                                                                                         University
                                                                                                            a dozen  and   cities in China
                                                                                                                           the data
                                                                                                                      different      mining
                                                                                                                                 cities      and
                                                                                                                                               team
                                                                                                                                        in China   uses
                                                                                                                                                   and
                                     a  variety
                                  AISKYEYE.      of
                                                 The UAVs    for
                                                       dataset     multi-angle,
                                                                  is framed     in    multiscene,
                                                                                    more    than  a  and
                                                                                                    dozen  multi-task
                                                                                                             diﬀerent   photography,
                                                                                                                       cities
                                     uses a variety of UAVs for multi-angle, multiscene, and multi-task photography, making thein China   making
                                                                                                                                          and   usesthe
                                     dataset
                                  a variety   ofvery
                                                 UAVs informative,
                                                          for            including
                                                               multi-angle,            the
                                                                                  multiscene,category
                                                                                                  and    of  detection
                                                                                                        multi-task      objects
                                                                                                                     photography,
                                     dataset very informative, including the category of detection objects (monotonous and rich), (monotonous
                                                                                                                                       making      and
                                                                                                                                                 the
                                     rich),
                                  dataset
                                     the     the number
                                            very
                                         number             of detection
                                                   informative,
                                                    of detection      objectsobjects
                                                                     including      the (fewer
                                                                                (fewer    category
                                                                                          and moreandofnumerous),
                                                                                                       more   numerous),
                                                                                                         detection   objects the  distribution
                                                                                                                               (monotonous
                                                                                                                     the distribution            of de-
                                                                                                                                                and
                                                                                                                                          of detection
                                     tection
                                  rich), the   objects
                                              number     (sparse
                                                         of         and
                                                            detection      dense),
                                                                           objects    and
                                                                                     (fewer the  light
                                                                                               and  moreintensity  (day
                                                                                                            numerous),    and
                                                                                                                          the
                                     objects (sparse and dense), and the light intensity (day and night). Some representative   night).  Some
                                                                                                                               distribution   of repre-
                                                                                                                                                 de-
                                     sentative
                                  tection
                                     images      images
                                            objects        in
                                               in the(sparse   the
                                                       datasetand   dataset    are
                                                                       dense),inand
                                                                 are shown           shown    in
                                                                                         the light
                                                                                     Figure   8.  Figure  8.
                                                                                                     intensity (day and night). Some repre-
                                  sentative images in the dataset are shown in Figure 8.

                        (a)                                            (b)                                                 (c)
                     (a)                                             (b)                                                (c)

                       (d)                                               (e)                                                  (f)
                     (d)                                              (e)                                               (f)
                                       Figure 8. Cont.
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                                         15 of 28

 Sensors 2023,
 Sensors 2023, 23,
               23, 7190
                   x FOR PEER REVIEW                                                                                                                          15
                                                                                                                                                               14of 28
                                                                                                                                                                 of 27

                    (g)                                                    (h)                                                         (i)
                                 Figure 8. Some representative images from the VisDrone2019 dataset. (a) Sparse object distribution;
                      (g)        (b) Dense object distribution; (c) Low(h) number of objects; (d) High number of objects;
                                                                                                                        (i)     (e) Many types
                                 ofFigure
                                    objects; (f) Objects
                                           8. Some        are very  small; (g)  Morning;  (h) Evening;  (i) Night.
                                   Figure 8.  Some representative
                                                    representative images
                                                                      images from
                                                                               from the
                                                                                    the VisDrone2019    dataset. (a)
                                                                                        VisDrone2019 dataset.    (a) Sparse
                                                                                                                     Sparse object
                                                                                                                             object distribution;
                                                                                                                                      distribution;
                                   (b) Dense
                                  (b)  Dense object
                                               object distribution;
                                                      distribution; (c)
                                                                     (c) Low
                                                                         Low number
                                                                              number ofof objects;
                                                                                          objects; (d)
                                                                                                   (d) High
                                                                                                       High number
                                                                                                             number ofof objects;
                                                                                                                         objects; (e)
                                                                                                                                  (e) Many
                                                                                                                                      Many types
                                                                                                                                             types
                                       VisDrone2019
                                   of objects; (f) Objectscontains    10 diﬀerent
                                                            are very small;          types(h)
                                                                             (g) Morning;   of Evening;
                                                                                                objects, such   as pedestrians, cars, bicy-
                                                                                                          (i) Night.
                                   of objects; (f) Objects are very small; (g) Morning; (h) Evening; (i) Night.
                                 cles, etc. Figure 9 shows the information related to the manual labeling of the objects in
                                          VisDrone2019
                                 this dataset.      We present
                                          VisDrone2019          contains
                                                                contains      10
                                                                              10 diﬀerent
                                                                      the subfigures
                                                                                   different in types
                                                                                                  Figureof
                                                                                                 types   of9objects,
                                                                                                              in ordersuch
                                                                                                             objects,     fromas
                                                                                                                        such    asleftpedestrians,
                                                                                                                                           to right and
                                                                                                                                      pedestrians,         cars,
                                                                                                                                                               topbicy-
                                                                                                                                                           cars,      to
                                                                                                                                                                   bicy-
                                 bottom.
                                   cles, etc.
                                   cles,     The
                                          etc.      first9subfigure
                                                Figure
                                               Figure     9shows
                                                              showsthe     shows
                                                                         the         the number
                                                                               information
                                                                            information                oftoobjects
                                                                                                  related
                                                                                               related      to
                                                                                                             thethe   of each
                                                                                                                      manual
                                                                                                                  manual         type
                                                                                                                                  labeling
                                                                                                                             labeling      in
                                                                                                                                            of the of dataset,
                                                                                                                                                 the             inand
                                                                                                                                                       the objects
                                                                                                                                                       objects          in
                                                                                                                                                                     this
                                 indicates
                                   dataset.    thatpresent
                                   this dataset.
                                               We     the present
                                                      We    objects     are
                                                                        the dominated
                                                                the subfiguressubfigures        byFigure
                                                                                               in
                                                                                       in Figure    cars   and
                                                                                                             9 inpedestrians.
                                                                                                    9 in order      orderleft
                                                                                                                   from     from     The
                                                                                                                                      left to
                                                                                                                               to right       second
                                                                                                                                               and    topsubfigure
                                                                                                                                                  right    and   top to
                                                                                                                                                            to bottom.
                                 shows
                                   bottom.
                                   The     theThe
                                         first   sizefirst
                                                        of the
                                                subfigure          object
                                                            subfigure
                                                               shows      thebounding
                                                                            shows
                                                                                number       boxes
                                                                                        the of
                                                                                            number    inofthe
                                                                                                objects         dataset,
                                                                                                          ofobjects
                                                                                                              each          and
                                                                                                                        of each
                                                                                                                      type  in the  the
                                                                                                                                    type    coordinates
                                                                                                                                             in theand
                                                                                                                                       dataset,                of the
                                                                                                                                                        dataset,     and
                                                                                                                                                             indicates
                                 centers
                                   indicatesof  all
                                                 thatobject
                                                        the   boxes
                                                              objects   are
                                                                          are fixed   at
                                                                                dominated one    point.
                                                                                                  by cars Theandsize   of the
                                                                                                                   pedestrians.
                                   that the objects are dominated by cars and pedestrians. The second subfigure shows the      object  The bounding
                                                                                                                                                second       box   size
                                                                                                                                                            subfigure
                                   shows
                                 shows
                                   size  ofthat
                                             thethesizedataset
                                                  object  ofbounding
                                                               thecontains
                                                                    objectboxesbounding
                                                                                 a large
                                                                                      in the   boxes
                                                                                            number
                                                                                                dataset,in  the dataset,
                                                                                                        of and
                                                                                                            small-area        and the
                                                                                                                           objects.
                                                                                                                  the coordinates         The
                                                                                                                                            ofcoordinates
                                                                                                                                                  third
                                                                                                                                                 the   centers   of
                                                                                                                                                          subfigureofthe
                                                                                                                                                                       all
                                 isobject
                                    the distribution
                                   centers    of allare
                                            boxes          of the
                                                       object
                                                          fixed    atcoordinates
                                                                boxes  oneare   fixedThe
                                                                             point.     of
                                                                                         atthe
                                                                                            one
                                                                                             sizecenter
                                                                                                   point.
                                                                                                    of thepoints
                                                                                                            The
                                                                                                            object  ofbounding
                                                                                                                  size the  object
                                                                                                                        of the   objectbounding
                                                                                                                                      box     bounding
                                                                                                                                             size        boxes,
                                                                                                                                                     shows    box
                                                                                                                                                               thatand
                                                                                                                                                                     size
                                                                                                                                                                      the
                                 itdataset
                                    can bethat
                                   shows      seenthe
                                              containsthata the
                                                         dataset
                                                             large center
                                                                     contains
                                                                     number  points     of the
                                                                                   a large
                                                                                  of              objects
                                                                                              number
                                                                                      small-area          ofare
                                                                                                     objects.    mainlythirdconcentrated
                                                                                                              small-area
                                                                                                                The          objects.
                                                                                                                              subfigure     The     in the
                                                                                                                                                    third
                                                                                                                                                is the        middle
                                                                                                                                                            subfigure
                                                                                                                                                         distribution
                                   is the
                                 and
                                   of  the distribution
                                        right   below theofarea
                                            coordinates          the coordinates
                                                                       center     imageofof
                                                                        of the points        the
                                                                                               thecenter
                                                                                            data.   The
                                                                                                    object  points
                                                                                                           fourth
                                                                                                              boundingof theboxes,
                                                                                                                     subfigureobject     abounding
                                                                                                                                     isand   scatter     beboxes,
                                                                                                                                               it can plot   seen    and
                                                                                                                                                                of the
                                                                                                                                                                    that
                                 corresponding
                                   it can
                                   the      be seen
                                        center    pointswidth
                                                        thatoftheand
                                                                the     height
                                                                    center
                                                                      objects      of the
                                                                                points
                                                                                 are      ofobject
                                                                                       mainly        bounding
                                                                                              theconcentrated
                                                                                                   objects          box,
                                                                                                              are mainly
                                                                                                                     in thewith    the darkest
                                                                                                                              concentrated
                                                                                                                              middle        and right incolor
                                                                                                                                                          the   at the
                                                                                                                                                                middle
                                                                                                                                                            below     the
                                 bottom
                                   area   ofleft
                                   and right      of
                                             thebelow  the the
                                                   image    plot.
                                                             data.   ItThe
                                                                  area  further
                                                                          of fourth shows
                                                                              the image        that the
                                                                                              data.
                                                                                        subfigure     is acurrent
                                                                                                      The              dataset
                                                                                                             fourth plot
                                                                                                            scatter    subfigure
                                                                                                                             of theis is
                                                                                                                                       dominated
                                                                                                                                            a scatter plot
                                                                                                                                        corresponding      by small
                                                                                                                                                                 of the
                                                                                                                                                                 width
                                   corresponding
                                 objects.
                                   and   height of the   width
                                                            object and    height ofbox,
                                                                       bounding          thewith
                                                                                              objectthebounding       box, with
                                                                                                          darkest color      at thethe bottomdarkest leftcolor
                                                                                                                                                           of theatplot.
                                                                                                                                                                      the
                                   It furtherleft
                                   bottom        shows
                                                     of thethat   theItcurrent
                                                               plot.       furtherdataset
                                                                                      showsisthat  dominated
                                                                                                       the current by small    objects.
                                                                                                                         dataset      is dominated by small
                                   objects.

                                  Figure 9. Information about the manually labeling of objects in VisDrone2019 dataset.
Sensors 2023, 23, 7190                                                                                              15 of 27

                              From the above introduction and analysis of the VisDrone2019 dataset, it can be
                         surmised that the dataset contains a large number of small objects, and they exist mainly
                         in a dense and uneven distribution. Compared with the dataset of traditional computer
                         vision tasks, this dataset is a large UAV dataset with multiple scales, scenes, and angles,
                         which is more challenging than the general computer vision tasks.

                         4.1.2. Experimental Environment and Training Strategies
                              The hardware platform and environmental parameters used in the experimental
                         training phase are shown in Table 2.

                         Table 2. Training environment and hardware platform parameters table.

                                           Parameters                                      Configuration
                                              CPU                                            i5-12490F
                                              GPU                                  NVIDIA GeForce RTX 3060
                                       GPU memory size                                          12G
                                       Operating systems                                       Win 10
                                    Deep learning architecture                 Pytorch1.9.2 + Cuda11.4 + cudnn11.4

                              To facilitate flexible deployment on hardware devices in various application scenarios,
                         the YOLOv8 model has been adapted to generate five different scaled models by adjusting
                         two parameters: width and depth. These models are referred to as YOLOv8n, YOLOv8s,
                         YOLOv8m, YOLOv8l, and YOLOv8x. The parameters and resource consumption of the
                         five models increase sequentially, and the detection performance becomes better and better.
                         The width, depth, and maximum number of channels corresponding to these five models
                         are shown in Table 3.

                         Table 3. Parameters corresponding to different sizes of YOLOv8.

                                 Model                    Depth                    Width                 Max Channels
                               YOLOv8n                     0.33                    0.25                      1024
                               YOLOv8s                     0.33                    0.50                      1024
                               YOLOv8m                     0.67                    0.75                       768
                               YOLOv8l                     1.00                    1.00                       512
                               YOLOv8x                     1.00                    1.25                       512

                            To better study and improve the models, we choose YOLOv8s as the baseline model.
                         Some of the key parameter settings during model training are shown in Table 4.

                         Table 4. Some key parameters set during model training.

                                           Parameters                                         Setup
                                             Epochs                                              200
                                          Momentum                                              0.932
                                      Initial learning rate                                     0.01
                                       Final learning rate                                     0.0001
                                          Weight decay                                         0.0005
                                           Batch size                                             4
                                          δ (WIoU v3)                                            1.9
                                          α (WIoU v3)                                             3
                                        Input image size                                     640 × 640
                                           Optimizer                                            SGD
                                   Data enhancement strategy                                  Mosaic

                              Under the dataset division rules of the VisDrone 2019 Challenge, this paper divides
                         the dataset into training sets (6471 images), testing sets (1610 images), and validation sets
Sensors 2023, 23, 7190                                                                                          16 of 27

                         (548 images). To accelerate the model convergence, Mosaic data enhancement is turned off
                         in the last 10 epochs of the training process.

                         4.1.3. Evaluation Indicators
                              To test the detection performance of our proposed improved model, we use precision,
                         recall, mAP0.5, mAP0.5:0.95, number of model parameters, model size, and detection
                         speed as evaluation metrics. The following parameters are used in the formulae for some
                         of the above evaluation metrics: TP (predicted as a positive sample and actually as a
                         positive sample as well), FP (predicted as a positive sample, though it is actually a negative
                         sample), and FN (predicted as a negative sample, though it is actually a positive sample).
                         Intersection over Union (IoU) represents the ratio of intersection and concatenation between
                         the bounding box and the true box.
                              Precision is the ratio of the number of positive samples predicted by the model to the
                         number of all detected samples and is calculated as shown in Equation (22):

                                                                                TP
                                                                Precision =                                        (22)
                                                                              TP + FP
                              Recall is the ratio of the number of positive samples correctly predicted by the model
                         to the number of positive samples that actually appeared. Recall is calculated as shown
                         in Equation (23):
                                                                           TP
                                                              Recall =                                          (23)
                                                                        TP + FN
                              The average precision (AP) is equal to the area under the precision–recall curve and is
                         calculated as shown in Equation (24):

                                                            Z1
                                                     AP =        Precision(Recall)d( Recall)                       (24)
                                                            0

                             Mean average precision (mAP) is the result obtained by the weighted average of AP
                         values of all sample categories, which is used to measure the detection performance of the
                         model in all categories, and the formula is shown in Equation (25):

                                                                        1 N
                                                                        N ∑ i =1
                                                                mAP =            APi                               (25)

                               The APi in Equation (25) denotes the AP value with category index value i, and N
                         denotes the number of categories of the samples in the training dataset (in this paper,
                         N is 10). mAP0.5 denotes the average accuracy when the IoU of the detection model is set
                         to 0.5, and mAP0.5:0.95 denotes the average accuracy when the IoU of the detection model
                         is set from 0.5 to 0.95 (with values taken at intervals of 0.5).

                         4.2. Experiment Results
                         4.2.1. Comparative Experiment of Loss Function
                              To verify the superiority of introducing WIoU v3, we conducted comparison exper-
                         iments on YOLOv8s using WIoU v3 and some mainstream loss functions, keeping the
                         other training conditions consistent. The experimental results are shown in Table 5. The
                         experimental results show that the model achieves the best detection performance when
                         using WIoU v3 as the bounding box regression loss. In addition, the model’s mAP50 when
                         using WIoU v3 is 0.7% higher than when using CIoU, demonstrating the effectiveness of
                         introducing WIoU v3.
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                      18 of 28

                                  using WIoU v3 is 0.7% higher than when using CIoU, demonstrating the eﬀectiveness of
Sensors 2023, 23, 7190                                                                                          17 of 27
                                  introducing WIoU v3.

                                  Table 5. Comparison of detection results for diﬀerent loss functions introduced by YOLOv8s. (The
                                        5. Comparison
                                  Tabledata
                                  bold                    of detection
                                            in the table indicate      results
                                                                  the best     for different loss functions introduced by YOLOv8s. (The
                                                                           results).
                                  bold data in the table indicate the best results).
                                       Metrics            Precision/%                  Recall/%            mAP0.5/%           mAP0.5:0.95/%
                                        Metrics
                                        CIoU               Precision/%
                                                              50.9                      Recall/%
                                                                                         38.2               mAP0.5/%
                                                                                                             39.3              mAP0.5:0.95/%
                                                                                                                                  23.5
                                      DIoU  [35]
                                         CIoU                 51.0
                                                               50.9                      38.3
                                                                                          38.2               39.5
                                                                                                              39.3                23.6
                                                                                                                                   23.5
                                       DIoU [47]
                                      GIoU   [35]              51.0
                                                              50.3                        38.3
                                                                                         38.4                 39.5
                                                                                                             39.6                  23.6
                                                                                                                                  23.6
                                       GIoU
                                        EIoU[47]               50.3
                                                              49.1                        38.4
                                                                                         38.0                 39.6
                                                                                                             38.7                  23.6
                                                                                                                                  23.4
                                         EIoU                  49.1                       38.0                38.7                 23.4
                                        SIoU
                                         SIoU                 51.5
                                                               51.5                      38.5
                                                                                          38.5               39.4
                                                                                                              39.4                23.4
                                                                                                                                   23.4
                                      WIoU
                                       WIoU v1v1              50.1
                                                               50.1                      38.5
                                                                                          38.5               39.3
                                                                                                              39.3                23.3
                                                                                                                                   23.3
                                      WIoU
                                       WIoU v2v2              50.6
                                                               50.6                      38.4
                                                                                          38.4               39.3
                                                                                                              39.3                23.2
                                                                                                                                   23.2
                                       WIoU
                                      WIoU v3 v3               51.3
                                                              51.3                        38.6
                                                                                         38.6                 40.0
                                                                                                             40.0                  23.6
                                                                                                                                  23.6

                                   4.2.2. Comparison
                                  4.2.2.  Comparisonwith  withYOLOv8
                                                                YOLOv8
                                         To demonstrate
                                        To   demonstratethe   thedetection performance
                                                                   detection  performance improvement
                                                                                              improvement effecteﬀect
                                                                                                                  of theofimproved    model,
                                                                                                                             the improved
                                   we conducted
                                  model,              comparison
                                            we conducted             experiments
                                                               comparison          betweenbetween
                                                                             experiments      the improved      model and
                                                                                                      the improved         modelthe and
                                                                                                                                    baseline
                                                                                                                                          the
                                   model    YOLOv8s.      Table  6 shows  the  AP  values  for each category     and
                                  baseline model YOLOv8s. Table 6 shows the AP values for each category and the mAP0.5the   mAP0.5    values
                                   for all for
                                  values   categories    for thefor
                                               all categories     improved    model
                                                                    the improved      and YOLOv8s.
                                                                                   model    and YOLOv8s.As shown
                                                                                                             As shown  in the   comparison
                                                                                                                            in the compar-
                                   results  in Table   6, the  mAP   value  of the improved     model  is  improved
                                  ison results in Table 6, the mAP value of the improved model is improved by 7.7%.      by   7.7%.  TheTheAP
                                   values   of all the categories   are improved    to different  degrees,  and   the  AP
                                  AP values of all the categories are improved to diﬀerent degrees, and the AP values of    values   of three
                                   categories
                                  three         (pedestrian,
                                          categories           people,
                                                       (pedestrian,     and motor)
                                                                      people,        are improved
                                                                               and motor)           by moreby
                                                                                             are improved       than  10%.
                                                                                                                   more       This10%.
                                                                                                                           than    indicates
                                                                                                                                        This
                                  indicates that the improved model can eﬀectively increase the detection accuracy ofobjects
                                   that  the improved      model   can effectively  increase  the detection   accuracy     of  small   small
                                   and improve
                                  objects           the detection
                                            and improve             performance.
                                                            the detection  performance.
                                  Table 6.
                                  Table     Comparisonof
                                         6. Comparison    ofthe
                                                             theproposed
                                                                proposedimproved
                                                                           improvedmodel
                                                                                       modelandandYOLOv8s
                                                                                                    YOLOv8sdetection
                                                                                                               detectionaccuracy.
                                                                                                                         accuracy. (The
                                                                                                                                    (Thebold
                                                                                                                                        bold
                                  data  in the table indicate the best results. All data units in the table are in percent.)
                                  data in the table indicate the best results. All data units in the table are in percent.)

  Models
  Models Pedestrian People People
            Pedestrian       Bicycle Bicycle
                                       Car   Van
                                               Car Truck
                                                      Van                   Tricycle
                                                                            Truck           Awning-Tricycle
                                                                                       Tricycle Awning-TricycleBus BusMotor
                                                                                                                         Motor mAP
                                                                                                                                mAP
                                             44.0   36.5                      28.1                 15.9          57.0
 YOLOv8s
  YOLOv8s   42.7     32.0
                     42.7     12.4
                                 32.0  79.1 12.4      79.1     44.0          36.5       28.1              15.9          57.0 44.9 44.9   39.3
                                                                                                                                           39.3
    Ours
   Ours         56.8 56.8 44.9   44.9
                                   18.8     18.8
                                            85.8    50.8
                                                      85.8   39.0
                                                               50.8           33.3
                                                                             39.0       33.3       19.7   19.7   64.3 64.3 56.2 56.2     47.0
                                                                                                                                           47.0

                                        Figure 10 shows the change curves of some important evaluation metrics of our pro-
                                         Figure 10 shows the change curves of some important evaluation metrics of our
                                  posed   model
                                   proposed   modelandand
                                                       YOLOv8s
                                                           YOLOv8s during
                                                                     duringthethe
                                                                                training  process.
                                                                                   training         From
                                                                                             process. FromFigure
                                                                                                            Figure10,
                                                                                                                   10,we
                                                                                                                       wecan
                                                                                                                           cansee
                                                                                                                               seethat
                                                                                                                                   that
                                  our
                                   our proposed
                                        proposed model
                                                    model outperforms
                                                            outperforms YOLOv8s
                                                                          YOLOv8sin    in three
                                                                                           three detection
                                                                                                 detection metrics:
                                                                                                           metrics: precision,
                                                                                                                      precision,recall,
                                                                                                                                 recall,
                                  and
                                   andmAP0.5
                                        mAP0.5after
                                                  afterabout
                                                       about15 15epochs
                                                                  epochsofoftraining
                                                                             trainingfrom
                                                                                       fromthethebeginning,
                                                                                                  beginning,and
                                                                                                              and our
                                                                                                                  ourmodel
                                                                                                                       modelstarts
                                                                                                                              startsto
                                                                                                                                     to
                                  stabilize
                                   stabilize after about 50 epochs of training. Compared with YOLOv8s, our method isfaster
                                             after about 50  epochs of training.  Compared      with YOLOv8s,   our  method   is faster
                                  to
                                   totrain
                                      train and
                                            and better
                                                 betterto
                                                        to detect.
                                                           detect.

                         (a)                                          (b)                                               (c)
                                  Figure
                                  Figure 10.
                                         10. (a)
                                              (a)Training
                                                 Trainingcurve
                                                          curveof
                                                                ofUAV-YOLOv8s
                                                                   UAV-YOLOv8sand    andYOLOv8s
                                                                                         YOLOv8sin inmAP;
                                                                                                     mAP;(b)
                                                                                                          (b)training
                                                                                                              trainingcurve
                                                                                                                       curveofofUAV-
                                                                                                                                 UAV-
                                  YOLOv8s    and  YOLOv8s  in precision; (c) training curve of UAV-YOLOv8s and   YOLOv8s
                                  YOLOv8s and YOLOv8s in precision; (c) training curve of UAV-YOLOv8s and YOLOv8s in       in recall.
                                                                                                                              recall.

                                      To further demonstrate the effectiveness of the proposed method, we compared the
                                  proposed model with some different sizes of YOLOv8 (YOLOv8n, YOLOv8s, YOLOv8m,
                                  and YOLOv8l) on the VisDrone2019 dataset. The experimental results are shown in Table 7.
Sensors 2023, 23, 7190                                                                                                           18 of 27

                                 According to the data in Table 7, compared with other models, the improved model has
                                 the highest values of the three evaluation indexes Recall, mAP0.5, and mAP0.5:0.95, and
                                 the detection performance is better than the model with a larger size than itself. From the
                                 experimental results, it can be seen that our proposed five-scale detection structure can
                                 improve the detection accuracy of small objects. In addition, the low-computing-power
                                 attention mechanism BiFormer, introduced by us, improves the detection performance of
                                 the model without consuming too many resources.

                                 Table 7. Comparative experimental results of the proposed model with four different sizes of YOLOv8.
                                 (The bold data in the table indicate the best results.)

    Models        Precision/%   Recall/%    mAP0.5/%       mAP0.5:0.95/% Model Size/MB           Detection Time/ms     Parameter/106
  YOLOv8n                43.8     33.0           33.3           19.3               6.6                   4.2                 3.0
  YOLOv8s                50.9     38.2           39.3           23.5              22.5                   7.7                11.1
  YOLOv8m                56.0     42.5           44.6           27.1              49.6                  16.6                25.9
  YOLOv8l                57.5     44.3           46.5           28.7              83.5                  25.6                43.7
    Ours                 54.4     45.6           47.0           29.2              21.5                  19.5                10.3

                                 4.2.3. Adding BiFormer Block
                                       To obtain the best performance and facilitate the subsequent ablation experiments
                                 after adding the BiFormer block to the model, the following comparison experiments were
                                 conducted in this study. We used YOLOv8s after the introduction of WIoU v3 as the
                                 baseline model and replaced the C2f module with the BiFormer block in different layers
                                 of the backbone network, and attained the experimental results shown in Table 8. The +
                                 in Table 8 indicates that the BiFormer block is added to the baseline model. B3-BiFormer
                                 indicates that the C2f module between layer B3 and layer B4 is replaced using the BiFormer
                                 block, and B4-BiFormer indicates that the C2f module between layer B4 and layer B5 is
                                 replaced using the BiFormer block. According to the experimental results in Table 8, the
                                 best detection performance is achieved when the C2f module between layers B4 and B5
                                 of the baseline model is replaced by the BiFormer module. Compared with the baseline
                                 model, mAP0.5 is improved by 0.5%. When adding the BiFormer block, the model can
                                 better focus on the essential information in the input features.

                                 Table 8. Experimental results after introducing the BiFormer block at different layers of the backbone
                                 network of the baseline model. (The bold data in the table indicate the best results.)

                                         Model           Precision/%           Recall/%           mAP0.5/%           mAP0.5:0.95/%
                                      Baseline               50.7                 38.7                40.0                23.6
                                   +B3-BiFormer              49.7                 38.6                39.7                23.5
                                   +B4-BiFormer              50.6                 39.2                40.5                24.1
                                   +B3-BiFormer+
                                                             50.3                 39.1                40.2                24.0
                                    B4-BiFormer

                                 4.2.4. Ablation Experiments
                                      To verify the effectiveness of each improvement strategy proposed in this paper, we
                                 performed ablation experiments on the baseline model using the VisDrone2019 dataset, and
                                 the experimental results are shown in Table 9. B2-FFNB and B1-FFNB in Table 9 indicate
                                 the use of FFNB module-based detection layers that fuse the shallow features of B2 and B1
                                                      √
                                 layers, respectively. indicates that this improved strategy was used.
Sensors 2023, 23, 7190                                                                                                                19 of 27

                                    Table 9. Detection results after the introduction of different improvement strategies. (The bold data
                                    in the table indicate the best results.)

                                                                                                            Model    Detection
 Baseline    WIoU v3     BiFormer   B1-FFNB   B2-FFNB    Precision/% Recall/%   mAP0.5/%   mAP0.5:0.95/%                         Parameter/106
                                                                                                           Size/MB   Time/ms

                √                                          50.9        38.2      39.3         23.5          22.5        7.7         11.1
                √          √                               50.7        38.7      40.0         23.6          22.5       7.2          11.1
 YOLOv8s        √          √          √                    50.6        39.2      40.5         24.1          22.1        7.8         10.9
                √          √          √          √         55.8        42.8      44.8         27.2          21.6       11.2         10.6
                                                           54.4        45.6      47.0         29.2          21.5       19.5         10.3

                                         The experimental results in Table 9 show that each improvement strategy improved the
                                    detection performance to different degrees when applied to the baseline model. WIoU v3 is
                                    introduced in the prediction box regression loss. WIoU v3 improves the localization ability
                                    of the model using a smarter sample allocation strategy, resulting in improved mAP50 by
                                    0.7%. BiFormer was introduced into the backbone network, replacing the C2f module in the
                                    original model. The efficient attention mechanism in BiFormer improves the attention to
                                    the key information in the feature map, which increases the mAP50 by 0.5%. The relatively
                                    simple structure of the BiFormer module reduces the size of the model by 0.4 MB and the
                                    parameters by about 0.2 M (million). The B2-FFNB detection layer was added to the baseline
                                    model, increasing the mAP by 4.3%. The currently used dataset contains a large number of
                                    small targets, so adding a detection scale to fuse the shallow (B2) feature information can
                                    effectively reduce the missed detection rate of small objects. Our proposed efficient and fast
                                    FFNB module alleviates the computational and memory burden of feature fusion and reduces
                                    the parameters of the model. The B1-FFNB detection layer was added to the baseline model,
                                    resulting in the growth of mAP by 2.2%. The model fuses the B1 layer features with richer
                                    detail information, which makes the shallow and deep information fully fused and further
                                    reduces the missed detection rate of small objects. Our proposed feature fusion network
                                    effectively improves the detection performance of the model.
                                         The average detection accuracy of the improved model is increased by 7.7%, most
                                    of the detection metrics are effectively improved, and the size and number of parameters
                                    of the model are lower than those of the baseline model. However, the addition of two
                                    detection layers causes the model structure to become complex and the inference time to
                                    become longer.

                                    4.2.5. Comparison Experiments
                                         To show the superiority and effectiveness of the improved algorithm proposed in this
                                    paper, we conducted two sets of comparison experiments. In the first set of comparison
                                    experiments, we compared the proposed model with some YOLO series algorithms. In
                                    the second set of comparison experiments, we compared the proposed model with other
                                    excellent models.
                                         The YOLO family of algorithms used in this paper are as follows: YOLOv3 [10], which
                                    uses multiscale detection for the first time, and its lightweight version, YOLOv3-tiny;
                                    YOLOv4 [11] uses the idea of CSPNet [48] to construct a new backbone network struc-
                                    ture called CSPDarknet53, which is lightweight while maintaining the detection accuracy;
                                    YOLOv5 uses Mosaic data augmentation to increase the model training speed and detection
                                    accuracy. In addition, YOLOv5 also uses the Focus structure, which reduces the compu-
                                    tation and parameter count of the model while maintaining the detection performance.
                                    YOLOv7 uses the efficient network architecture ELAN [13]. The results of the comparison
                                    experiments are shown in Table 10.
Sensors 2023, 23, 7190                                                                                                            20 of 27

                                   Table 10. Detection results of some YOLO series models and the proposed model. (The bold data in
                                   the table indicate the best results).

                                                                                          Model           Detection
       Models            Precision/%     Recall/%      mAP0.5/%       mAP0.5:0.95/%                                      Parameter/106
                                                                                         Size/MB          Time/ms
    YOLOv3                   54            43.6             41.9              23.3          213              18.3            103.7
  YOLOv3-Tiny               38.2           24.8             23.8              13.3          24.4              2.9             12.1
    YOLOv4                   36            48.6             42.1              25.7          245              25.3             64.4
    YOLOv5s                 46.4           34.6             34.4               19            14              12.0             7.2
    YOLOv7                  51.4           42.1             39.9              21.6           72               1.7              64
    YOLOv8s                 50.9           38.2             39.3              23.5          22.5              7.7             11.1
  UAV-YOLOv8s               54.4           45.6             47.0              29.2          21.5             19.5             10.3

                                        According to the experimental results in Table 10, the earlier YOLO series algorithms,
                                   such as YOLOv3 and YOLOv4, which have complex structures and large parameter counts,
                                   are not conducive to deployment on unmanned platforms and have relatively low detection
                                   accuracy. YOLOv3-Tiny achieves a lightweight model but loses a large portion of the
                                   detection accuracy. YOLOv5s and YOLOv8s have smaller model sizes, fewer parameters,
                                   and better detection performance than previous YOLO versions. However, both models
                                   use three-scale detection structures, which cannot fulfill the detection needs of a high
                                   proportion of small objects, and therefore result in lower model detection accuracy than
                                   the proposed method in this paper at the same size. Compared with UAV-YOLOv8s,
                                   YOLOv7 has an advantage in detection speed, but it is deficient in model size and detection
                                   performance. In the comparative experimental results, UAV-YOLOv8s has the highest
                                   average detection accuracy and the best overall detection performance. The inference time
                                   of the improved model increases, but real-time detection can still be achieved.
                                        In this study, a comparative experiment was conducted to evaluate the performance
                                   of UAV-YOLOv8s and other mainstream models. The following is a brief introduction
                                   to the models used in the comparative experiments: Faster R-CNN [7] optimizes the
                                   problems of high computational and structural complexity of R-CNN; Cascade R-CNN [49]
                                   proposes a multilevel detection architecture based on R-CNN; RetinaNet [50] proposes
                                   Focal loss; CenterNet [51] proposes anchorless frame detection; FSAF [52] algorithm solves
                                   the drawbacks of heuristic feature selection; ATSS [53] proposes an adaptive training
                                   sample selection mechanism. The experimental results are shown in Table 11.

                                   Table 11. Detection results of the classical model and the proposed model. (The bold data in the table
                                   indicate the best results.)

                                            Models                  AP0.5/%                  AP0.75/%                 AP0.5:0.95/%
                                        Faster R-CNN [7]               37.2                        22.8                   21.9
                                         RetinaNet [50]                19.1                        10.5                   10.6
                                       Cascade R-CNN [49]              39.1                        26.2                   24.3
                                         CenterNet [51]                33.7                        18.0                   18.8
                                            FSAF [52]                  36.5                        20.6                   20.9
                                            ATSS [53]                  36.4                        23.1                   22.3
                                         UAV-YOLOv8s                   47.0                        30.6                   29.2

                                        According to the comparative experimental results in Table 11, the model proposed in
                                   this paper has the best detection performance compared to other excellent models. Faster
                                   R-CNN, as a two-stage detection algorithm, has a slower detection speed compared to
                                   one-stage algorithms Moreover, the resolution of the feature map extracted by the backbone
                                   network is small, so it is relatively poor in accuracy for small-object detection. RetinaNet
                                   and ATSS focus on how to determine the positive and negative samples. CenterNet removes
                                   the computational effort due to the use of anchors, but there are situations such as dense
                                   scenes and occlusion of small objects that can lead to some items being missed if multiple
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                 22 of 28
Sensors 2023, 23, 7190                                                                                                               21 of 27

                                 proposed with Cascade R-CNN improves the overall detection performance of the model
                                 but increases
                                 prediction      computational
                                              centroids            complexity
                                                         are overlapping.     Theand    trainingdetection
                                                                                   multilevel      diﬃculty.architecture
                                                                                                                Both RetinaNet   and FSAF
                                                                                                                            proposed    with
                                 Cascade
                                 use        R-CNN
                                      multiscale     improves
                                                  feature   fusionthetooverall
                                                                        considerdetection
                                                                                   objects performance        of theHowever,
                                                                                              at diﬀerent scales.     model butinincreases
                                                                                                                                    the con-
                                 computational
                                 text             complexity
                                      of visual tasks            and training
                                                       where small              difficulty.
                                                                       objects are            Both RetinaNet
                                                                                     the primary                 and FSAF
                                                                                                     detection objects,      usetwo
                                                                                                                          these  multiscale
                                                                                                                                      model
                                 feature fusion
                                 structures       to consider
                                              cannot  address the objects  at different
                                                                      detection   needs.scales.      However,
                                                                                            This results   in bothin the contextand
                                                                                                                     RetinaNet     of visual
                                                                                                                                       FSAF
                                 tasks  where   small  objects   are  the primary     detection    objects,
                                 having poorer detection results than the methods proposed in this paper.    these  two  model   structures
                                 cannot  address the detection
                                       Summarizing     the resultsneeds.
                                                                     of theThis  results
                                                                             above         in both
                                                                                     two sets        RetinaNet and
                                                                                                 of comparison        FSAF having
                                                                                                                   experiments,   thepoorer
                                                                                                                                       UAV-
                                 detection results
                                 YOLOv8s            thaninthe
                                              proposed          methods
                                                              this paper proposed
                                                                            has betterindetection
                                                                                            this paper.performance compared to other
                                       Summarizing
                                 models.   Our proposedthe results   of thefeature
                                                              multiscale     above two     setsnetwork
                                                                                      fusion     of comparison
                                                                                                          achieves  experiments,   the UAV-
                                                                                                                      five-scale detection.
                                 YOLOv8s     proposed
                                 This structure         in this paperdetection
                                                  for small-object      has betterhas
                                                                                   detection    performanceover
                                                                                         some advantages        compared   to other
                                                                                                                     the models      models.
                                                                                                                                   involved
                                 Our  proposed    multiscale   feature  fusion  network    achieves   five-scale  detection.
                                 in the above comparison experiments, so our detection results are better than the other     This  structure
                                 for small-object
                                 models.           detection
                                           In addition,         has some advantages
                                                          we introduced     WIoU v3 and   overBiFormer
                                                                                                 the models    involved
                                                                                                           in the        in the
                                                                                                                   baseline     above
                                                                                                                            model       com-
                                                                                                                                     to opti-
                                 parison  experiments,   so  our  detection  results  are better  than  the other  models.
                                 mize the model’s localization ability and noise suppression. The improvement strategy      In addition,  we
                                 introduced   WIoU   v3  and   BiFormer   in the baseline    model   to optimize   the model’s
                                 we introduced takes into account the consumption of resources and achieves better detec-       localization
                                 ability
                                 tion    and noise suppression. The improvement strategy we introduced takes into account
                                      results.
                                 the consumption of resources and achieves better detection results.
                                 4.3. Visualization Analysis
                                 4.3. Visualization Analysis
                                       Deep learning models are characterized by poor interpretability, which somehow
                                       Deep learning models are characterized by poor interpretability, which somehow
                                 hinders the development and application of deep learning. To chart the detection eﬀect of
                                 hinders the development and application of deep learning. To chart the detection effect of
                                 the model proposed in this paper intuitively and conveniently, we conducted comparative
                                 the model proposed in this paper intuitively and conveniently, we conducted comparative
                                 experiments to analyze the detection performance of the model from three perspectives:
                                 experiments to analyze the detection performance of the model from three perspectives:
                                 confusion matrix, model inference results and heat map. Finally, to verify the generaliza-
                                 confusion matrix, model inference results and heat map. Finally, to verify the generalizabil-
                                 bility of our method, we conducted inference experiments on self-made data.
                                 ity of our method, we conducted inference experiments on self-made data.
                                       To
                                       To visualize
                                          visualize the
                                                     the ability
                                                          abilityofofour
                                                                      ourmethod
                                                                          methodtoto predict thethe
                                                                                       predict    object categories,
                                                                                                     object          we we
                                                                                                            categories,  plotted the
                                                                                                                            plotted
                                 confusion   matrices of UAV-YOLOv8s        and  YOLOv8s,    as shown   in Figure
                                 the confusion matrices of UAV-YOLOv8s and YOLOv8s, as shown in Figure 11. The    11. The rows  and
                                 columns
                                 rows andof    the confusion
                                            columns             matrices represent
                                                      of the confusion                the true and
                                                                          matrices represent         predicted
                                                                                                the true        categories,
                                                                                                         and predicted       respec-
                                                                                                                         categories,
                                 tively, and  the values in the  diagonal  region  indicate the  proportion  of correctly
                                 respectively, and the values in the diagonal region indicate the proportion of correctly predicted
                                 categories,  while the values
                                 predicted categories,    whileinthethevalues
                                                                        other regions  indicate
                                                                               in the other      the proportion
                                                                                              regions            of incorrectly
                                                                                                       indicate the   proportionpre-
                                                                                                                                  of
                                 dicted  categories.
                                 incorrectly predicted categories.

                                      (a)                                                          (b)
                                 Figure 11. (a)
                                 Figure 11. (a) Confusion
                                                Confusion matrix
                                                          matrix plot
                                                                 plot of
                                                                      of YOLOv8s; (b) confusion
                                                                         YOLOv8s; (b) confusion matrix
                                                                                                matrix plot
                                                                                                       plot of
                                                                                                            of our
                                                                                                               our model.
                                                                                                                   model.

                                      As can be seen from Figure 11, the diagonal
                                                                             diagonal region
                                                                                      region of
                                                                                              of the
                                                                                                 the confusion
                                                                                                     confusion matrix
                                                                                                                  matrixinin UAV-
                                                                                                                             UAV-
                                 YOLOv8s is darker in color than YOLOv8s, indicating that the ability of our model to
                                 correctly predict
                                           predict the
                                                    theobject
                                                         objectcategory
                                                                categoryhas
                                                                         hasbeen
                                                                             beenenhanced.
                                                                                   enhanced.However,
                                                                                             However,   forfor small
                                                                                                             small   objects
                                                                                                                   objects    such
                                                                                                                           such as
                                 as
                                 the the  bicycle,
                                     bicycle,       tricycle,
                                              tricycle,        and awning-tricycle,
                                                        and awning-tricycle,          the proportion
                                                                             the proportion              of objects
                                                                                            of objects judged          judged as
                                                                                                                as background    is
                                 higher, implying that a large portion of these categories are missed during the detection
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                23 of 28

Sensors 2023, 23, 7190                                                                                                              22 of 27

                                 background is higher, implying that a large portion of these categories are missed during
                                 the detection
                                 process.         process. The
                                            The improved         improved
                                                             model   reducesmodel     reduces
                                                                               the missed       the missed
                                                                                            detection        detection
                                                                                                        rate for          rate for these
                                                                                                                  these categories,    but
                                 categories,  but   the percentage   of them   being   correctly  predicted   is still
                                 the percentage of them being correctly predicted is still low. The bicycle category   low. The bicycle of
                                 category   of transportation
                                 transportation    is small andisusually
                                                                  small and   usually
                                                                          exists        existsand
                                                                                 in a dense    in aoccluded
                                                                                                    dense and    occluded
                                                                                                             form,   makingform,    mak-
                                                                                                                              it difficult
                                 ing it detected
                                 to be  diﬃcult toin be detected in environments
                                                      environments                     with complex backgrounds.
                                                                      with complex backgrounds.
                                      To   visually demonstrate
                                       To visually    demonstrate the    detection eﬀect
                                                                    the detection           of our
                                                                                     effect of our method,
                                                                                                     method, inference
                                                                                                               inference experiments
                                                                                                                           experiments
                                 using
                                 using UAV-YOLOv8s,
                                         UAV-YOLOv8s, YOLOv8s
                                                            YOLOv8s and and YOLOv5s
                                                                             YOLOv5s were were performed
                                                                                                 performed in in this
                                                                                                                 this study.
                                                                                                                       study. We
                                                                                                                               We chose
                                                                                                                                   chose
                                 four representative    scenarios, urban   roads,  public  facility places, market    intersections,
                                 four representative scenarios, urban roads, public facility places, market intersections,            and
                                 traﬃc   intersections,  as the experimental     data. These   scenarios  contain    numerous
                                 and traffic intersections, as the experimental data. These scenarios contain numerous and       and   di-
                                 verse
                                 diverse small objects, which are suitable for inference experiments. The detection results of
                                        small  objects, which   are suitable  for inference   experiments.    The  detection   results  of
                                 the three models are shown in Figure 12.

                 (a) YOLOv5s                                (b) YOLOv8s                                  (c) UAV-YOLOv8s
                                 Figure
                                 Figure 12.
                                        12. Inference
                                            Inference results
                                                       results of
                                                               of three
                                                                  three diﬀerent
                                                                         different models
                                                                                   models on
                                                                                           on VisDrone2019
                                                                                              VisDrone2019 dataset.
                                                                                                              dataset. (a)
                                                                                                                       (a) Inference
                                                                                                                           Inference results
                                                                                                                                     results
                                 of YOLOv5s;   (b) inference results  of YOLOv8s;   (c) inference results of our model.
                                 of YOLOv5s; (b) inference results of YOLOv8s; (c) inference results of our model.

                                      As shown in the results in Figure 12, compared with YOLOv8s and YOLOv5s, the
                                 method proposed
                                           proposed ininthis
                                                         thispaper
                                                               paperhas
                                                                     hasthe
                                                                          the optimal
                                                                            optimal   detection
                                                                                    detection    accuracy
                                                                                              accuracy for for  objects
                                                                                                           objects      at far
                                                                                                                    at the theend
                                                                                                                               far
                                 end  of the field of view.  In addition, our method  improves   the model’s   leakage  detection
                                 of the field of view. In addition, our method improves the model’s leakage detection rate
                                 for occluded and dense objects, which effectively improves the detection performance.
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                    24 of 28

Sensors 2023, 23, 7190                                                                                                                  23 of 27
                                rate for occluded and dense objects, which eﬀectively improves the detection perfor-
                                mance.
                                       Gradient-weighted class activation mapping (Grade CAM)
                                      Gradient-weighted                                                    CAM) waswas utilized
                                                                                                                         utilized to
                                                                                                                                   to generate
                                                                                                                                      generate
                                heat maps
                                heat   maps for
                                              for YOLOv8s
                                                  YOLOv8s and   and UAV-YOLOv8s
                                                                    UAV-YOLOv8s[54].     [54]. The
                                                                                               The heat
                                                                                                     heat maps
                                                                                                           maps visually
                                                                                                                  visually and
                                                                                                                            and easily
                                                                                                                                  easily reflect
                                                                                                                                         reflect
                                which areas
                                which    areasofof the
                                                    the feature
                                                         featuremap
                                                                  map the
                                                                       the model
                                                                           model is  is focusing
                                                                                        focusing on.on. The
                                                                                                         The gradient
                                                                                                              gradient values
                                                                                                                         values are
                                                                                                                                  are obtained
                                                                                                                                      obtained
                                by backpropagation
                                by  backpropagation of     of the
                                                              the confidence
                                                                  confidence of of the
                                                                                   the model
                                                                                         model output
                                                                                                 output categories
                                                                                                           categories byby Grade
                                                                                                                            Grade CAM,
                                                                                                                                    CAM, andand
                                the pixels
                                the  pixels with
                                              with higher
                                                     higher gradients
                                                              gradients in
                                                                         in the
                                                                            the feature
                                                                                 feature maps
                                                                                            maps areare represented
                                                                                                         represented by by deeper
                                                                                                                            deeper shades
                                                                                                                                     shades ofof
                                red ininthe
                                red       theheatmaps.
                                               heatmaps.      Conversely,
                                                           Conversely,   the the  pixels
                                                                             pixels   withwith
                                                                                             lowerlower     gradients
                                                                                                     gradients           are represented
                                                                                                                 are represented    by deeper by
                                deeper of
                                shades    shades
                                             blue. of  blue.
                                                     The       The experimental
                                                          experimental              results
                                                                          results are     shownare in
                                                                                                    shown
                                                                                                      Figure in13.
                                                                                                                Figure
                                                                                                                   From13.   From13,
                                                                                                                           Figure   Figure
                                                                                                                                       we can13,
                                we can surmise
                                surmise               that YOLOv8s
                                           that YOLOv8s        pays poorpays   poor attention
                                                                           attention     to smallto    small and
                                                                                                     objects   objects  and is insensitive
                                                                                                                   is insensitive   to distantto
                                objects.   The model
                                distant objects.     The proposed     in this paper
                                                           model proposed      in this has
                                                                                         paperbetter
                                                                                                 has suppression       of background
                                                                                                      better suppression                  noise
                                                                                                                               of background
                                and
                                noisepays
                                        andmore
                                              pays attention     to small
                                                     more attention        objects.
                                                                       to small       The model’s
                                                                                  objects.   The model’sattention   is more
                                                                                                              attention       focused
                                                                                                                         is more        on the
                                                                                                                                   focused   on
                                center  point
                                the center     of the
                                              point  ofobject,   which
                                                        the object,     makes
                                                                     which      the predicted
                                                                             makes                bounding
                                                                                      the predicted            box more
                                                                                                        bounding           accurate
                                                                                                                     box more         and thus
                                                                                                                                 accurate   and
                                improves
                                thus improvesthe overall   detection
                                                    the overall        performance
                                                                  detection  performance of theofmodel.
                                                                                                  the model.

              (a) original images                            (b) YOLOv8s                                   (c) UAV-YOLOv8s
                                 Figure 13.
                                 Figure 13. (a)
                                            (a) Original
                                                Original images;
                                                         images; (b)
                                                                 (b) heat
                                                                     heat maps
                                                                          maps of
                                                                               of YOLOv8s;
                                                                                  YOLOv8s; (c)
                                                                                            (c) heat
                                                                                                heat maps
                                                                                                     maps of
                                                                                                          of our
                                                                                                             our model.
                                                                                                                 model.

                                      To validate
                                     To    validate the
                                                      the generalizability
                                                           generalizability of of our
                                                                                   our proposed
                                                                                       proposed method,
                                                                                                    method, representative
                                                                                                              representative image
                                                                                                                                 image data
                                                                                                                                         data
                                werecollected
                                were   collectedfor forinference
                                                         inference    experiments
                                                                   experiments       in this
                                                                                  in this     study.
                                                                                          study.  TheThe   image
                                                                                                       image  datadata
                                                                                                                   werewere
                                                                                                                          mainly mainly   col-
                                                                                                                                    collected
                                from
                                lectedscenes
                                        from on    the campus
                                                scenes             of WuhanofInstitute
                                                          on the campus         Wuhan of    Technology
                                                                                          Institute        and various
                                                                                                      of Technology   andscenes   within
                                                                                                                            various       the
                                                                                                                                       scenes
                                Wuhan
                                within thecityWuhan
                                               area in city
                                                          HubeiareaProvince,
                                                                     in HubeiChina.    These
                                                                                Province,      scenes
                                                                                            China.      contain
                                                                                                     These      a large
                                                                                                            scenes       number
                                                                                                                    contain          of small
                                                                                                                               a large  num-
                                objects,  which
                                ber of small      are challenging
                                                 objects,   which arefor    the inference
                                                                         challenging    for experiments.
                                                                                            the inference The    results ofThe
                                                                                                             experiments.     the inference
                                                                                                                                   results of
                                experiments      are  shown      in Figure   14.   Among     them,    Figure  14a–c
                                the inference experiments are shown in Figure 14. Among them, Figure 14a–c show the  show    the   detection
                                results in the
                                detection        campus
                                             results        scenario,
                                                       in the   campusand    Figureand
                                                                          scenario,   14d–f  show14d–f
                                                                                           Figure    the detection
                                                                                                           show theresults   in the
                                                                                                                      detection       Wuhan
                                                                                                                                   results  in
                                downtown
                                the Wuhanscenario.
                                               downtown    Thescenario.
                                                                 results inThe
                                                                            Figure  14 show
                                                                                results        that our
                                                                                         in Figure    14 method  exhibits
                                                                                                         show that         good detection
                                                                                                                    our method       exhibits
                                results  in a variety
                                good detection            of representative
                                                    results   in a variety of scenes    such as scenes
                                                                               representative     streets,such
                                                                                                           campuses,    andcampuses,
                                                                                                               as streets,    intersections.
                                                                                                                                          and
                                Some   of   the  detection    results   in Figure   14 show     that our  model   has  almost
                                intersections. Some of the detection results in Figure 14 show that our model has almost          no  missed
                                detection. These experimental results effectively prove the generalizability of our method.
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                  25 of 28

Sensors 2023, 23, 7190                                                                                            24 of of
                                 no missed detection. These experimental results eﬀectively prove the generalizability  27

                                 our method.

                                (a)                                                                  (b)

                                (c)                                                                  (d)

                                (e)                                                                  (f)
                                 Figure
                                 Figure 14.
                                        14. Examples
                                            Examples of
                                                     of detection
                                                        detection results
                                                                  results on
                                                                          on self-made data.
                                                                             self-made data.

                                 5. Conclusions
                                 5. Conclusions
                                       For the
                                       For  the object
                                                object detection
                                                         detection task
                                                                      task in
                                                                            in UAV
                                                                               UAV aerial
                                                                                     aerial photography
                                                                                              photography scenarios,
                                                                                                             scenarios, there
                                                                                                                        there are
                                                                                                                                are problems
                                                                                                                                    problems
                                 such as
                                 such  as aa high
                                             high proportion
                                                    proportionofofsmallsmallobjects,
                                                                               objects,complex
                                                                                         complexbackgrounds,
                                                                                                    backgrounds, and  limited
                                                                                                                    and   limitedhardware
                                                                                                                                   hardware re-
                                 sources.   Most   existing  models     suffer  from  poor    detection  accuracy
                                 resources. Most existing models suﬀer from poor detection accuracy and struggle toand  struggle   to achieve
                                 a balance
                                 achieve      between
                                           a balance      detection
                                                        between         performance
                                                                   detection             and resource
                                                                                performance               consumption.
                                                                                                 and resource  consumption. To optimize    the
                                                                                                                                 To optimize
                                 detection   performance     of  the  model    while  considering    platform  resource
                                 the detection performance of the model while considering platform resource consump-      consumption,    this
                                 paperthis
                                 tion,   proposes    a UAV aerial
                                             paper proposes      a UAV scene   object
                                                                           aerial     detection
                                                                                  scene            model called
                                                                                          object detection       UAV-YOLOv8,
                                                                                                             model                  based on
                                                                                                                    called UAV-YOLOv8,
                                 YOLOv8.      Firstly, the  WIoU     v3  loss  function   is introduced,   which  incorporates
                                 based on YOLOv8. Firstly, the WIoU v3 loss function is introduced, which incorporates            a  dynamic a
                                 sample    allocation   strategy    to effectively  reduce     the model’s  attention  to
                                 dynamic sample allocation strategy to eﬀectively reduce the model’s attention to extreme  extreme   samples
                                 and improve
                                 samples          overall performance.
                                            and improve                        Secondly,Secondly,
                                                             overall performance.          the efficient
                                                                                                      thedynamic
                                                                                                           eﬃcient sparse
                                                                                                                    dynamic  attention
                                                                                                                                sparse mech-
                                                                                                                                        atten-
                                 anism    BiFormer     is integrated     into  the backbone      network,   enhancing
                                 tion mechanism BiFormer is integrated into the backbone network, enhancing the model’s  the  model’s   focus
                                 on  critical information     in  the  feature   maps   and   further  optimizing
                                 focus on critical information in the feature maps and further optimizing detectiondetection    performance.
                                 Finally, the fast and hardware-friendly FFNB is proposed, and two new detection scales are
                                 designed based on this block to realize five-scale detection, which fully integrates shallow
                                 and deep features and drastically reduces the missed detection rate of small objects. The
Sensors 2023, 23, 7190                                                                                                                 25 of 27

                                   improved model achieves an average detection accuracy improvement of 7.7% over the
                                   baseline model without increasing its size or parameters, leading to significant enhance-
                                   ments in object detection performance. Moreover, the improved model outperforms some
                                   classical algorithms of similar types in terms of detection accuracy.
                                         As the improved model adds two detection layers, the structure of the model becomes
                                   complex and the feature map size of the shallow layer is relatively large, resulting in
                                   different degrees of improvement in the computation and inference time of the model.
                                   The FLOPs value of YOLOv8s is 28.7 billion times and that of UAV-YOLOv8s is 53 billion
                                   times, which is nearly double the improvement, and there is still room for optimization
                                   of computational resource consumption. The detection accuracy of the improved model
                                   is still not high for very small objects such as bicycles, and the next major research focus
                                   is to continue to optimize the detection accuracy of the model while keeping resource
                                   consumption in mind.

                                   Author Contributions: Conceptualization, G.W. and H.H.; methodology, G.W.; software, G.W.;
                                   validation, G.W., H.H. and P.A.; formal analysis, G.W. and Y.C.; investigation, G.W.; resources, G.W.
                                   and J.H.; data curation, G.W. and T.H.; writing—original draft preparation, G.W.; writing—review
                                   and editing, G.W. and P.A.; visualization, G.W.; supervision, G.W. and Y.C.; project administration
                                   G.W. and Y.C. All authors have read and agreed to the published version of the manuscript.
                                   Funding: This study was funded by the Graduate Innovative Fund of Wuhan Institute of Technology
                                   (No: CX2022148).
                                   Institutional Review Board Statement: Not applicable.
                                   Informed Consent Statement: Not applicable.
                                   Data Availability Statement: Not applicable.
                                   Conflicts of Interest: The authors declare no conflict of interest.

References
1.    Li, Z.; Zhang, Y.; Wu, H.; Suzuki, S.; Namiki, A.; Wang, W. Design and Application of a UAV Autonomous Inspection System for
      High-Voltage Power Transmission Lines. Remote Sens. 2023, 15, 865. [CrossRef]
2.    Byun, S.; Shin, I.-K.; Moon, J.; Kang, J.; Choi, S.-I. Road Traffic Monitoring from UAV Images Using Deep Learning Networks.
      Remote Sens. 2021, 13, 4027. [CrossRef]
3.    Bouguettaya, A.; Zarzour, H.; Kechida, A.; Taberkit, A.M. A survey on deep learning-based identification of plant and crop
      diseases from UAV-based aerial images. Cluster. Comput. 2022, 26, 1297–1317. [CrossRef]
4.    Felzenszwalb, P.F.; Girshick, R.B.; McAllester, D.; Ramanan, D. Object Detection with Discriminatively Trained Part-Based Models.
      IEEE Trans. Pattern Anal. Mach. Intell. 2010, 32, 1627–1645. [CrossRef] [PubMed]
5.    Girshick, R.; Donahue, J.; Darrell, T.; Malik, J. Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation.
      In Proceedings of the 2014 IEEE Conference on Computer Vision and Pattern Recognition, Columbus, OH, USA, 23–28 June 2014;
      pp. 580–587.
6.    Girshick, R. Fast R-CNN. In Proceedings of the 2015 IEEE International Conference on Computer Vision (ICCV), Santiago, Chile,
      7–13 December 2015; pp. 1440–1448.
7.    Ren, S.; He, K.; Girshick, R.; Sun, J. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. IEEE
      Trans. Pattern Anal. Mach. Intell. 2017, 39, 1137–1149. [CrossRef]
8.    Redmon, J.; Divvala, S.; Girshick, R.; Farhadi, A. You Only Look Once: Unified, Real-Time Object Detection. In Proceedings of the
      2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 27–30 June 2016; pp. 779–788.
9.    Redmon, J.; Farhadi, A. YOLO9000: Better, Faster, Stronger. In Proceedings of the 2017 IEEE Conference on Computer Vision and
      Pattern Recognition (CVPR), Honolulu, HI, USA, 21–26 July 2017; pp. 6517–6525.
10.   Redmon, J.; Farhadi, A. YOLOv3: An Incremental Improvement. arXiv 2018, arXiv:1804.02767.
11.   Bochkovskiy, A.; Wang, C.Y.; Liao, H.Y.M. YOLOv4: Optimal Speed and Accuracy of Object Detection. arXiv 2020, arXiv:2004.10934.
12.   Li, C.; Li, L.; Jiang, H.; Weng, K.; Geng, Y.; Li, L.; Ke, Z.; Li, Q.; Cheng, M.; Nie, W.; et al. YOLOv6: A Single-Stage Object Detection
      Framework for Industrial Applications. arXiv 2022, arXiv:2209.02976.
13.   Wang, C.Y.; Bochkovskiy, A.; Liao, H.Y.M. YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object
      detectors. arXiv 2022, arXiv:2207.02696.
14.   Liu, W.; Anguelov, D.; Erhan, D.; Szegedy, C.; Reed, S.; Fu, C.Y.; Berg, A.C. SSD: Single Shot MultiBox Detector. arXiv 2016,
      arXiv:1512.02325.
Sensors 2023, 23, 7190                                                                                                             26 of 27

15.   Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, Ł.; Polosukhin, I. Attention is all you need. In
      Advances in Neural Information Processing Systems; MIT Press: Cambridge, MA, USA, 2017; pp. 5998–6008.
16.   Carion, N.; Massa, F.; Synnaeve, G.; Usunier, N.; Kirillov, A.; Zagoruyko, S. End-to-end object detection with transformers. arXiv
      2020, arXiv:2005.12872.
17.   Luo, X.; Wu, Y.; Wang, F. Target Detection Method of UAV Aerial Imagery Based on Improved YOLOv5. Remote Sens. 2022, 14, 5063.
      [CrossRef]
18.   Zhou, H.; Ma, A.; Niu, Y.; Ma, Z. Small-Object Detection for UAV-Based Images Using a Distance Metric Method. Drones 2022, 6, 308.
      [CrossRef]
19.   Du, B.; Huang, Y.; Chen, J.; Huang, D. Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster
      Object Detection on Drone Images. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
      Vancouver, BC, Canada, 18–22 June 2023; pp. 13435–13444.
20.   Deng, F.; Xie, Z.; Mao, W. Research on edge intelligent recognition method oriented to transmission line insulator fault detection.
      Int. J. Electr. Power Energy Syst. 2022, 139, 108054. [CrossRef]
21.   Howard, A.; Pang, R.; Adam, H.; Le, Q.; Sandler, M.; Chen, B.; Wang, W.; Chen, L.C.; Tan, M.; Chu, G.; et al. Searching for
      MobileNetV3. In Proceedings of the IEEE/CVF International Conference on Computer Vision, Seoul, Republic of Korea, 27
      October–2 November 2019; pp. 1314–1324.
22.   Zheng, J.; Fu, H.; Li, W.; Wu, W.; Yu, L.; Yuan, S.; Tao, W.Y.W.; Pang, T.K.; Kanniah, K.D. Growing status observation for oil palm
      trees using Unmanned Aerial Vehicle (UAV) images. ISPRS J. Photogramm. Remote Sens. 2021, 173, 95–121. [CrossRef]
23.   Liu, M.; Wang, X.; Zhou, A.; Fu, X.; Ma, Y.; Piao, C. UAV-YOLO: Small Object Detection on Unmanned Aerial Vehicle Perspective.
      Sensors 2020, 20, 2238. [CrossRef]
24.   He, K.M.; Zhang, X.Y.; Ren, S.Q.; Sun, J. Deep Residual Learning for Image Recognition. In Proceedings of the 2016 IEEE
      Conference on Computer Vision and Pattern Recognition (CVPR), Seattle, WA, USA, 27–30 June 2016; pp. 770–778.
25.   Liu, B.; Luo, H. An Improved Yolov5 for Multi-Rotor UAV Detection. Electronics 2022, 11, 2330. [CrossRef]
26.   Wang, J.; Zhang, F.; Zhang, Y.; Liu, Y.; Cheng, T. Lightweight Object Detection Algorithm for UAV Aerial Imagery. Sensors 2023,
      23, 5786. [CrossRef]
27.   Woo, S.; Park, J.; Lee, J.-Y.; Kweon, I.S. CBAM: Convolutional Block Attention Module. In Proceedings of the Computer
      Vision—ECCV 2018, Cham, Switzerland, 8–14 September 2018; pp. 3–19.
28.   Liu, Y.; Yang, F.; Hu, P. Small-object detection in UAV-captured images via multi-branch parallel feature pyramid networks. IEEE
      Access 2020, 8, 145740–145750. [CrossRef]
29.   Chen, J.; Kao, S.-H.; He, H.; Zhuo, W.; Wen, S.; Lee, C.-H.; Chan, S.-H.G. Run, Don’t walk: Chasing higher FLOPS for faster neural
      networks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Vancouver, BC, Canada,
      18–22 June 2023.
30.   Zhu, L.; Wang, X.; Ke, Z.; Zhang, W.; Lau, R. BiFormer: Vision Transformer with Bi-Level Routing Attention. arXiv 2023,
      arXiv:2303.08810.
31.   Tong, Z.; Chen, Y.; Xu, Z.; Yu, R. Wise-IoU: Bounding Box Regression Loss with Dynamic Focusing Mechanism. arXiv 2023,
      arXiv:2301.10051.
32.   He, K.; Zhang, X.; Ren, S.; Sun, J. Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition. IEEE Trans.
      Pattern Anal. Mach. Intell 2015, 37, 1904–1916. [CrossRef] [PubMed]
33.   Liu, S.; Qi, L.; Qin, H.; Shi, J.; Jia, J. Path Aggregation Network for Instance Segmentation. In Proceedings of the IEEE Conference
      on Computer Vision and Pattern Recognition, Salt Lake City, UT, USA, 18–23 June 2018; pp. 8759–8768.
34.   Li, X.; Wang, W.; Wu, L.; Chen, S.; Hu, X.; Li, J.; Tang, J.; Yang, J. Generalized Focal Loss: Learning Qualified and Distributed
      Bounding Boxes for Dense Object Detection. arXiv 2020, arXiv:2006.04388.
35.   Zheng, Z.; Wang, P.; Liu, W.; Li, J.; Ye, R.; Ren, D. Distance-IoU loss: Faster and better learning for bounding box regression. In
      Proceedings of the AAAI Conference on Artificial Intelligence, New York, NY, USA, 7–12 February 2020; pp. 12993–13000.
36.   Feng, C.; Zhong, Y.; Gao, Y.; Scott, M.R.; Huang, W. TOOD: Task-Aligned One-Stage Object Detection. In Proceedings of the 2021
      IEEE International Conference on Computer Vision (ICCV), Montreal, QC, Canada, 10–17 October 2021; pp. 3490–3499.
37.   Zhang, Y.F.; Ren, W.; Zhang, Z.; Jia, Z.; Wang, L.; Tan, T. Focal and efficient IOU loss for accurate bounding box regression.
      Neurocomputing 2022, 506, 146–157. [CrossRef]
38.   Gevorgyan, Z. SIoU Loss: More Powerful Learning for Bounding Box Regression. arXiv 2022, arXiv:2205.12740.
39.   Cao, X.; Zhang, Y.; Lang, S.; Gong, Y. Swin-Transformer-Based YOLOv5 for Small-Object Detection in Remote Sensing Images.
      Sensors 2023, 23, 3634. [CrossRef]
40.   Lu, S.; Lu, H.; Dong, J.; Wu, S. Object Detection for UAV Aerial Scenarios Based on Vectorized IOU. Sensors 2023, 23, 3061.
      [CrossRef]
41.   Zhang, T.; Zhang, Y.; Xin, M.; Liao, J.; Xie, Q. A Light-Weight Network for Small Insulator and Defect Detection Using UAV
      Imaging Based on Improved YOLOv5. Sensors 2023, 23, 5249. [CrossRef]
42.   Jiang, X.; Cui, Q.; Wang, C.; Wang, F.; Zhao, Y.; Hou, Y.; Zhuang, R.; Mei, Y.; Shi, G. A Model for Infrastructure Detection along
      Highways Based on Remote Sensing Images from UAVs. Sensors 2023, 23, 3847. [CrossRef]
43.   Howard, A.G.; Zhu, M.; Chen, B.; Kalenichenko, D.; Wang, W.; Weyand, T.; Andreetto, M.; Adam, H. MobileNets: Efficient
      Convolutional Neural Networks for Mobile Vision Applications. arXiv 2017, arXiv:1704.04861.
Sensors 2023, 23, 7190                                                                                                           27 of 27

44.   Zhang, X.; Zhou, X.; Lin, M.; Sun, J. ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices. arXiv
      2017, arXiv:1707.01083.
45.   Han, K.; Wang, Y.H.; Tian, Q.; Guo, J.Y.; Xu, C.J.; Xu, C. GhostNet: More Features from Cheap Operations. In Proceedings of the
      IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Seattle, WA, USA, 14–19 June 2020; pp. 1580–1589.
46.   Zhu, P.; Wen, L.; Du, D.; Bian, X.; Fan, H.; Hu, Q.; Ling, H. Detection and Tracking Meet Drones Challenge. IEEE Trans. Pattern
      Anal. Mach. Intell. 2021, 44, 7380–7399. [CrossRef] [PubMed]
47.   Rezatofighi, H.; Tsoi, N.; Gwak, J.; Sadeghian, A.; Reid, I.; Savarese, S. Generalized intersection over union: A metric and a loss
      for bounding box regression. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Long
      Beach, CA, USA, 15–20 June 2019; pp. 658–666.
48.   Wang, C.Y.; Liao, H.Y.M.; Wu, Y.H.; Chen, P.Y.; Hsieh, J.W.; Yeh, I.H. CSPNet: A new backbone that can enhance learning
      capability of CNN. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Seattle,
      WA, USA, 13–19 June 2020; pp. 390–391.
49.   Cai, Z.; Vasconcelos, N. Cascade R-CNN: Delving into High Quality Object Detection. In Proceedings of the 2018 IEEE/CVF
      Conference on Computer Vision and Pattern Recognition, Salt Lake City, UT, USA, 18–22 June 2018; pp. 6154–6162.
50.   Lin, T.; Goyal, P.; Girshick, R.; He, K.; Dollár, P. Focal Loss for Dense Object Detection. In Proceedings of the 2017 IEEE
      International Conference on Computer Vision (ICCV), Venice, Italy, 22–29 October 2017; pp. 2999–3007.
51.   Duan, K.; Bai, S.; Xie, L.; Qi, H.; Huang, Q.; Tian, Q. Centernet: Keypoint triplets for object detection. In Proceedings of the
      IEEE/CVF International Conference on Computer Vision, Seoul, Republic of Korea, 27 October–2 November 2019; pp. 6569–6578.
52.   Zhu, C.; He, Y.; Savvides, M. Feature Selective Anchor-Free Module for Single-Shot Object Detection. In Proceedings of the 2019
      IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA, 16–20 June 2019; pp. 840–849.
53.   Zhang, S.; Chi, C.; Yao, Y.; Lei, Z.; Li, S.Z. Bridging the Gap Between Anchor-Based and Anchor-Free Detection via Adaptive
      Training Sample Selection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Seattle,
      WA, USA, 14–19 June 2020; pp. 9759–9768.
54.   Selvaraju, R.R.; Cogswell, M.; Das, A.; Vedantam, R.; Parikh, D.; Batra, D. Grad-CAM: Visual Explanations from Deep Networks
      via Gradient-Based Localization. In Proceedings of the 2017 IEEE International Conference on Computer Vision (ICCV), Venice,
      Italy, 22–29 October 2017; pp. 618–626.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
