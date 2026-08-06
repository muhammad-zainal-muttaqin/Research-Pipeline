---
source_id: 085
bibtex_key: zhang2023bcmfnet
title: Bilateral Cross-Modal Fusion Network for Robot Grasp Detection
year: 2023
domain_theme: Grasp Robotik
verified_pdf: 85_BCMFNet_Bilateral_Cross-Modal_Fusion.pdf
char_count: 198191
---

sensors
Article
Bilateral Cross-Modal Fusion Network for Robot Grasp Detection
Qiang Zhang 1,2, *            and Xueying Sun 1,2, *

                                         1   School of Automation, Jiangsu University of Science and Technology, No. 666 Changhui Road,
                                             Zhenjiang 212100, China
                                         2   Systems Science Laboratory, Jiangsu University of Science and Technology, No. 666 Changhui Road,
                                             Zhenjiang 212100, China
                                         *   Correspondence: qzhang@just.edu.cn (Q.Z.); sunxueying@just.edu.cn (X.S.)

                                         Abstract: In the field of vision-based robot grasping, effectively leveraging RGB and depth information
                                         to accurately determine the position and pose of a target is a critical issue. To address this challenge, we
                                         proposed a tri-stream cross-modal fusion architecture for 2-DoF visual grasp detection. This architecture
                                         facilitates the interaction of RGB and depth bilateral information and was designed to efficiently
                                         aggregate multiscale information. Our novel modal interaction module (MIM) with a spatial-wise
                                         cross-attention algorithm adaptively captures cross-modal feature information. Meanwhile, the channel
                                         interaction modules (CIM) further enhance the aggregation of different modal streams. In addition,
                                         we efficiently aggregated global multiscale information through a hierarchical structure with skipping
                                         connections. To evaluate the performance of our proposed method, we conducted validation experiments
                                         on standard public datasets and real robot grasping experiments. We achieved image-wise detection
                                         accuracy of 99.4% and 96.7% on Cornell and Jacquard datasets, respectively. The object-wise detection
                                         accuracy reached 97.8% and 94.6% on the same datasets. Furthermore, physical experiments using
                                         the 6-DoF Elite robot demonstrated a success rate of 94.5%. These experiments highlight the superior
                                         accuracy of our proposed method.

                                         Keywords: robot grasp detection; cross-modality fusion; channel interaction

                                         1. Introduction
Citation: Zhang, Q.; Sun, X. Bilateral
Cross-Modal Fusion Network for
                                               In the realm of robotics, the advancement of intelligence has significantly boosted the
Robot Grasp Detection. Sensors 2023,
                                         adoption of robots. As a result, the visual detection of targets has become an increasingly
23, 3340. https://doi.org/10.3390/       crucial area of focus in robotics research. A robot’s ability to grasp and transport objects,
s23063340                                either independently or in response to user commands, can enhance its ability to assimilate
                                         into the environment and broaden the range of potential robotic applications. Presently,
Academic Editors: Kechen Song and
                                         the utilization of RGB-D cameras is making remarkable strides in robot grasping, thanks to
Yunhui Yan
                                         the evolution of vision sensor technology.
Received: 20 February 2023                     Our work focuses on RGB-D data-driven robot grasp detection. Many pioneers in the
Revised: 19 March 2023                   field have achieved remarkable results. In the past decade, convolutional neural networks
Accepted: 21 March 2023                  (CNNs) [1–5] have become the most widely utilized solution for robot grasp detection due
Published: 22 March 2023                 to their superiority in feature representation, resulting in outstanding detection accuracy
                                         and high efficiency. While CNNs excel at local feature representation, they tend to lose
                                         information with global relevance. Recently, transformer-based approaches have gained
                                         significant popularity for visual tasks and have demonstrated comparable or superior per-
Copyright: © 2023 by the authors.
                                         formance in classification, semantic segmentation, and object detection. Some researchers,
Licensee MDPI, Basel, Switzerland.
This article is an open access article
                                         such as S. Wang et al. [6], have demonstrated the applicability of transformers in robot
distributed under the terms and
                                         grasp detection.
conditions of the Creative Commons
                                               Despite the impressive strides made by deep learning in solving the problem of
Attribution (CC BY) license (https://    visually detecting and grasping targets, the robustness of grasp detection still requires
creativecommons.org/licenses/by/         further improvement. This is because, while either RGB or depth images can provide some
4.0/).                                   information about the scene, they are only partial in nature and may not always be effective

Sensors 2023, 23, 3340. https://doi.org/10.3390/s23063340                                                   https://www.mdpi.com/journal/sensors
Sensors 2023, 23, 3340                                                                                              2 of 19

                         in obtaining reliable detection results across different scenarios. Therefore, it is essential to
                         leverage the information provided by both modalities to enhance grasp detection.
                               To address this issue, researchers in the field have developed early [3,7–9] and late [2,10]
                         multimodal fusion approaches for grasp detection. While these methods have yielded meaning-
                         ful results, the correlation between multimodal data has only been partially exploited. Recent
                         studies have focused on exploring the mechanisms of intermediate fusion [11,12]. Although
                         these methods have improved the efficiency of RGB and depth modalities in robot grasp
                         detection, making the most of the bilateral modal information still remains a challenge.
                               To solve the problem of multimodal fusion, we proposed a tri-stream cross-modal
                         fusion architecture to achieve bilateral information interaction. The key idea was to use the
                         proposed MIM approach to capture the global association information between modalities.
                         Subsequently, the aggregation of different modal streams was refined through adaptive
                         CIM units. The main contributions of our work can be summarized as follows:
                         •    We proposed a tri-stream cross-modal fusion architecture to facilitate the interaction of
                              RGB and depth bilateral information and efficiently aggregate multiscale information;
                         •    A novel spatial-wise cross-attention algorithm was developed to adaptively capture
                              cross-modal feature information. The channel interaction modules further enhanced
                              the aggregation of different modal streams;
                         •    The proposed method demonstrated state-of-the-art grasp detection accuracy on both
                              the Cornell and Jacquard datasets, with image-wise detection accuracy reaching 99.4%
                              and 96.7% on Cornell and Jacquard, respectively, with object-wise detection accuracy
                              reaching 97.8% and 94.6% on the same datasets;
                         •    The proposed method has also shown success in guiding gripping tasks in the real
                              world, achieving a 94.5% success rate on household items.
                              The remaining parts of the article are structured as follows. Section 2 presents the
                         deep regression model for detecting robot grasps. Section 3 describes the formulation of
                         grasp detection. The proposed method is elaborated in detail in Section 4. The performance
                         evaluation of the proposed method is presented in Section 5. Finally, Section 6 provides a
                         summary and conclusion of the article.

                         2. Related Works
                         2.1. Grasp Model Representation
                              The representation of the robot grasp model is a prerequisite for identifying the
                         gripping position. In vision-based approaches, the object grasp can be divided into the
                         2-DoF planar grasp and the 6-DoF grasp, based on various application scenarios. For
                         instance, 2-DoF planar grasp implies that the target object is positioned on a flat working
                         surface and is confined from one direction. Thus, the grasping information is reduced from
                         6D to 3D, specifically 2D in-plane position and 1D rotation angle. On the other hand, 6-DoF
                         grasping enables the gripper to hold objects from different angles in the 3D space.
                              In 2006, A. Saxena et al. [13] proposed a point-based model representation for 6-DoF
                         grasp detection. This representation considers the target location to be a point in 3D space.
                         The point is detected in the image, and the relative position of the point with respect to the
                         robot end effector is estimated using either a binocular camera or motion recovery structure,
                         enabling the robot to perform the grasp operation. In 2010, Q.V. Le et al. [14] proposed a
                         multi-points linkage approach to express the grasp position. Subsequent studies, such as
                         those outlined in references [14–17], have achieved significant progress in terms of detection
                         accuracy, reliability, and efficiency.
                              For 2-DoF planar grasp detection, Y. Jiang [18] proposed a rectangular representation
                         method for the robot grasp that bypasses the object detection and pose estimation process.
                         In this method, each grasp is represented by a rectangle with its central coordinates, width,
                         height, and rotation angle. This simplifies the model’s complexity significantly. Since then,
                         many researchers, such as [2–5,9,14,19,20], have focused on robot grasp detection using
                         the rectangular model, and these studies have made efforts to improve the robustness of
                         feature representation and the real-time performance of detection.
Sensors 2023, 23, 3340                                                                                              3 of 19

                         2.2. 2-DoF Planar Grasp Detection Approaches Based on Rectangular Representation
                               In recent years, convolutional neural networks [21] have become the most widely utilized
                         solution for vision tasks. When it comes to studies on robot grasp detection, many researchers
                         have focused on improving the quality of deep neural networks [22,23] in order to achieve
                         better detection results. One such method was proposed by I. Lenz et al. [1] in 2014, which
                         utilized a multilayer deep self-encoder for image feature extraction in combination with a
                         support vector machine classifier. J. Wei et al. [24] proposed a similar approach in 2017 using
                         the Deep Extreme Learning Machine for automatic encoding. Trottier et al. [25] also proposed
                         a detection method in the same year using a self-coding dictionary learning method with a
                         support vector machine classifier, although it was found to be slow and not well-suited for
                         robotic object grasping. Z. Wang et al. [26] proposed a unified model for object segmentation
                         and grasp detection in 2016. The method combined a grasping detection network with a
                         two-stage estimator to improve detection accuracy.
                               Due to the complexity of multi-stage detection methods, more researchers are focusing
                         on the end-to-end approach. In 2015, J. Redmon et al. [27] proposed a robot grasp detection
                         method based on multilayer convolutional neural networks, which allowed for end-to-end
                         training and reduced manual involvement in the training process. This approach also
                         significantly improved detection efficiency through direct regression.
                               In 2018, heatmap regression methods were first utilized by D. Morrison et al. [4] to
                         indirectly obtain grasp detection results. In their follow-up study, D. Morrison et al. [5]
                         introduced a generative convolutional neural network for robot grasp detection. In 2020, S.
                         Kumra et al. [8] proposed an antipodal robotic grasp detection method using a residual
                         convolutional neural network, achieving image-wise detection accuracy of 97.7% and 94.6%
                         on Cornell and Jacquard datasets. Their work was further improved upon in 2022 by the
                         same group [20]. H. Cao et al. [3] proposed an efficient convolutional neural network
                         using Gaussian-based grasp representation in 2021, which achieved image-wise detection
                         accuracy of 97.8% and 95.6% for Cornell and Jacquard datasets, respectively. Lastly, S.
                         Ainetter and F. Fraundorfer [28] proposed an end-to-end method for robot grasp detection
                         in 2021, using a semantic segmentation refinement engine to increase detection accuracy.
                               A recent development in the field of robot grasp detection is the transformer-based
                         method proposed by S. Wang et al. [6]. In their study, they made a preliminary attempt
                         to address the 2-DoF grasp detection problem using the transformer architecture, and
                         achieved impressive detection accuracy and efficiency, proving to be a competitive method
                         in the field.
                               Our work explored the effectiveness of hybrid models that integrate convolutional neural
                         networks and transformer architectures to detect 2-DoF robot grasping. This approach offers
                         new insights into the design of effective grasp detection systems.

                         2.3. Multiple Modality Fusion Based Grasp Detection
                              With the wide adoption of RGB-D sensors, an increasing number of studies have
                         turned their attention to the efficient fusion of multimodal data. Various approaches
                         for multimodality fusion have been proposed, including early-fusion, late-fusion, and
                         intermediate-fusion techniques.
                              In 2018, F. Chu et al. [7] introduced an early-fusion approach that integrated R, G,
                         and depth channels to predict multi-grasps for multiple objects. Two years later, in 2020,
                         S. Kumra et al. [8] presented a generative residual convolutional neural network for grasp
                         detection, utilizing an early-fusion strategy with both RGB and depth images. Similarly,
                         in 2022, H. Cao et al. [3] proposed a Gaussian-based grasp representation method using
                         a generative grasping detection model that incorporated both RGB and depth images as
                         inputs. Also in 2022, S. Yu et al. [9] introduced another approach using a residual neural
                         network and squeeze-and-excitation modules.
                              In 2017, Q. Zhang et al. [2] put forth a sturdy robot grasp detection method that integrated
                         RGB and depth features in the prediction head based on the YOLO architecture [29]. In 2022,
                         Y. Song et al. [10] also proposed a hierarchical late-fusion method for RGB-D data, utilizing
Sensors 2023, 23, 3340                                                                                              4 of 19

                         two CNN branches in the form of U-Net [30]. The decoding process hierarchically merged the
                         RGB and depth features.
                               In 2022, K. Song et al. [31] proposed a triple-modal fusion architecture for robotic
                         visual perception applications. In their work, a hierarchical weighted suppress interference
                         approach was introduced to achieve robust features. H. Tian et al. [11] introduced an
                         intermediate-fusion method for lightweight pixel-wise robot grasp detection, utilizing RGB
                         and depth information. In 2023, H. Tian et al. [12] extended their work by introducing a
                         rotation adaptive grasp detection approach, which also utilizes intermediate data fusion.
                         They achieved a remarkable state-of-the-art accuracy of 99.3% and 94.6% on the Cornell
                         and Jacquard datasets, respectively.
                               Research on multimodal fusion has yielded promising results. However, the effectiveness
                         of cross-modal fusion is still limited by the quality of bilateral mutual information support. To
                         address this issue, we propose a novel solution in this paper. Our approach offers an improved
                         framework for cross-modal fusion that enhances the mutual information support between
                         modalities and enables more effective integration of multimodal data. Our results demonstrate
                         the viability and superiority of our proposed method in achieving better performance in robot
                         grasp detection.

                         3. Problem Formulation
                               The robot is capable of using different types of grippers, including two-finger, three-
                         finger, or multi-finger grippers, to grasp objects. However, parallel two-finger grippers are
                         commonly preferred due to their simple design and cost-effectiveness. For 2-DoF grasp
                         applications, a grasp can be represented by a 5-dimensional tuple g = {x, y, θ, w, h} [1,8,27].
                         The tuple g describes a rectangle with the center coordinates (x, y), the gripper height size
                         (h), the gripper opening distance (w), and the orientation of the grasp rectangle (θ) with
                         respect to the horizontal axis. Typically, the gripper dimensions are known, which allows
                         the grasp representation to be simplified to g = (x, y, θ, w).
                               Instead of the 5-dimensional representation, D. Morrison et al. [5] provide an improved
                         version of a grasp described as follows:
                                                                        
                                                          Ge = Q,   e,W
                                                                  e ∅  e ∈ R3 × H × W                               (1)

                              In Equation (1), Qe i,j ∈ [0, 1] denotes the detection quality of each pixel in the image,
                         while ∅e i,j ∈ [−π/2, π/2] represents the rotation angle of the gripper, and W e i,j ∈ [0, Wmax ]
                         specifies the required width of the gripper’s opening. Our work involves the transformation
                         of the grasp detection problem into a pixel-level prediction. Specifically, we propose a
                         cross-modal fusion method to derive G    e from an RGB-D image of the environment in which
                         the grasping targets are located.
                              Equation (1) provides a comprehensive representation of the grasp image, but the
                         rotation angle of the grip is challenging to determine due to its symmetrical
                                                                                                             values. To
                         address this ambiguity, we encode the rotation angle using sin 2∅i,j and cos(2∅i,j ), which
                                                                                             e                e
                         helps eliminate any discontinuities that may arise during the calculation. The angle of the
                         grasp to be executed at each pixel can be obtained using Equation (2):
                                                                            "            #
                                                                 1            sin 2∅
                                                                                   e i,j
                                                          ∅i,j = × arctan
                                                           e                                                         (2)
                                                                 2            cos 2∅
                                                                                   e i,j

                              The optimal grasp within an image space is determined by identifying the pixel with
                         the highest quality score in G.
                                                      e Additionally, the grasp can be straightforwardly mapped to
                         physical space based on the internal and external parameters of the RGB-D camera.
    Sensors 2023, 23, x FOR PEER REVIEW                                                                                                                                                                                          5 of 20

                                                                   The optimal grasp within an image space is determined by identifying the pixel with
Sensors 2023, 23, 3340                                                                                                                               5 of 19
                                                              the highest quality score in 𝐺̃ . Additionally, the grasp can be straightforwardly mapped
                                                              to physical space based on the internal and external parameters of the RGB-D camera.

                                                            4. 4. Approach
                                                               Approach
                                                            4.1.  Overview
                                                               4.1. OverviewofofBilateral
                                                                                 BilateralCross-Modal
                                                                                           Cross-Modal Fusion
                                                                                                       Fusion Network
                                                                                                              Network
                                                                 Our
                                                                   Ourrobot
                                                                         robotgrasp
                                                                                graspdetection
                                                                                       detectionarchitecture
                                                                                                  architecture is illustrated
                                                                                                                   illustratedin inFigure
                                                                                                                                    Figure1.1.ItItcomprises
                                                                                                                                                   comprises    three
                                                                                                                                                             three
                                                              main
                                                            main    components:feature
                                                                  components:       featureextraction,
                                                                                             extraction,feature
                                                                                                          featureaggregation,
                                                                                                                  aggregation,and andgrasp
                                                                                                                                       graspprediction.
                                                                                                                                              prediction.To Toensure
                                                                                                                                                                en-
                                                              sure robust
                                                            robust featurefeature   extraction,
                                                                             extraction,        we employed
                                                                                           we employed      twotwo    strategies.
                                                                                                                 strategies.      First,
                                                                                                                              First,  wewe  tackledthe
                                                                                                                                          tackled    theproblem
                                                                                                                                                          problem of
                                                              of modality
                                                            modality        interaction
                                                                       interaction      in feature
                                                                                     in feature    fusion
                                                                                                 fusion   bybyassigning
                                                                                                               assigningadaptive
                                                                                                                           adaptive weights
                                                                                                                                     weightstotoRGB RGBand
                                                                                                                                                         anddepth
                                                                                                                                                               depth
                                                              image  features   during  the fused  feature   extraction  stage. Second,  we   adopted
                                                            image features during the fused feature extraction stage. Second, we adopted a channel      a channel
                                                              interaction
                                                            interaction    approachfor
                                                                         approach     forfeature
                                                                                          featureaggregation.
                                                                                                  aggregation.

             Patch        LMHSA
           Aggregation     block                                                                                                                   CIM                                                 F               F
                                                                                                                                                                                                GAP           RELU
                                                                                                                                                                                                       C               C
                          LMHCA                                                                                                                     Conv          Conv          Conv
           MIM
                           block                                                                                                                     1×1           3×3           1×1
                                                                                                                                                                                               Conv
             Patch        LMHSA                                                                                                                                                                 1×1
           Aggregation     block

                                                                                                                                                                                CIM
                    RSM                                                                                               Up                 Up                Up
                          cf0                  cf1                 cf2                cf3                 cf4
                                                                                                                              cf5             cf6               cf7
                                                                                                                                                                               TConv
                                                                                                                 RGB feature extraction stream
      RGB image                                                                                                                                                                f8    (112×112×46)
      (224×224×3)                                                                                                                                                                   BN

                                               ff1                 ff2                ff3                 ff4
                                                                                                                      Up                 Up                Up             ©
                                         MIM                 MIM                MIM                 MIM                        ff5            ff6               ff7             CIM

                                                                                                                 Fused feature extracion stream
                                                                                                                                                                               TConv
                                                                                                                                                                               f9    (224×224×32)
                                                                                                                             df5              df6               df7
                          df0                  df1                 df2                df3                 df4                                                                       BN
                    RSM                                                                                               Up                 Up                Up
                                                                                                                                                                  (56×56×46)
                          (112×112×16)

                                               (56×56×46)

                                                                   (28×28×92)

                                                                                      (14×14×184)

                                                                                                          (7×7×368)

                                                                                                                           (14×14×184)

                                                                                                                                              (28×28×92)

      Depth image                                                                                                                                                               CIM
      (224×224×1)
                                                                                                                 Depth image feature extraction stream

                                           Encoder                                                                                        Decoder

                                                                                 Feature                                                                                               Feature                  Grasp
                                                                                extraction                                                                                           aggregation              prediction

     RSM      : Residual connection based Stem Module                                                      Tconv : Transposed convolution                                                                  Multiplication
     MIM   : Module Interaction Module                                                                     BN    : Batch Normalization
     S-Up  : Skip connection based Up-sampling Module                                                                                                                                                      Pixel-wise addition
     CIM   : Channel Interaction Module                                                                    GAP : Global Average Pooling                                                                    Sigmoid function
     LMHSA : Light-weight Multi-Head Self Attention                                                        FC           : Fully Connection
     LMHCA : Light-weight Multi-Head Cross Attention                                                       RELU : Rectified Linear Activation Function                                                © Channel concatenation
                                                              Figure
                                                            Figure 1. 1. Bilateralcross-modal
                                                                      Bilateral     cross-modalfusion
                                                                                                fusionnetwork
                                                                                                      network architecture.
                                                                                                              architecture.

                                                                   The
                                                                 The     feature
                                                                      feature     extraction
                                                                               extraction     method
                                                                                           method     serves
                                                                                                   serves two two  purposes:
                                                                                                                purposes:     extracting
                                                                                                                           extracting    multi-scale
                                                                                                                                       multi-scale      features
                                                                                                                                                   features  from
                                                              from  the RGB    and  depth  scene images  and  constructing  fused  features from  the
                                                            the RGB and depth scene images and constructing fused features from the two modalities.    two  mo-
                                                              dalities.
                                                            This processThis  process is accomplished
                                                                           is accomplished              through
                                                                                              through three       threethe
                                                                                                             streams:   streams:  the RGB
                                                                                                                           RGB feature      feature extraction
                                                                                                                                         extraction   stream, the
                                                            depth feature extraction stream, and the fused feature extraction stream. Within each stream,
                                                            the feature extraction process comprises two key stages: feature encoding and decoding.
                                                                 The architecture of the RGB and depth feature extraction process, as shown in Figure 1,
                                                            is based on U-Net-like structures. Similar to the approach in [32], each stream consists of a
                                                            residual connection based stem module (RSM) and a series of modal interaction modules
                                                            (MIM) for encoding RGB and depth features. Down-sampling operations are used to
Sensors 2023, 23, 3340                                                                                              6 of 19

                         obtain multi-scale features. However, low-level features may contain more details but also
                         unnecessary information, while high-level features may have more semantic information
                         but may not represent small target features well. To obtain more robust features, we
                         employ feature decoders, which are composed of transposed convolution and up-sampling
                         processes with skip connections.
                               As depicted in Figure 1, the initial step in the feature extraction process involves the
                         utilization of the RSM on the RGB image, which is responsible for extracting fine-grained
                         features and generating the cf0 feature. To produce features at multiple scales, the cf0 feature
                         undergoes several stages of light-weight multi-head self-attention modules (LMHSA) to create
                         multi-scale features, including cf1, cf2, cf3, and cf4. These encoding procedures also involve
                         the fused features from using an addition operation. To ensure that the resulting feature map
                         is consistent with the size of the input image, a series of up-sampling modules are employed
                         at the decoding step. Additionally, concatenation operations are incorporated into these
                         processes to fully exploit the low-level and high-level features, leading to the production
                         of the cf5, cf6, and cf7 feature maps. The depth feature extraction stream is also capable of
                         generating corresponding feature maps, ranging from df0 to df7.
                               Compared to the encoding processes for RGB and depth features, the fused feature
                         maps (ff1, ff2, ff3, and ff4) are initially generated using light weight multi-head cross-
                         attention (LMHCA) strategy. During feature fusion, adaptive weights are assigned to
                         the RGB and depth information. Details about the LMHCA algorithm is described in
                         Section 4.2.2. To ensure the resulting fused features are robust, the same decoders used in
                         the RGB and depth feature decoding processes are employed. Consequently, ff7 is of the
                         same size as cf7 and df7.
                               As previously stated, the feature extraction process results in three distinct feature maps:
                         cf7, df7, and ff7. It is our hypothesis that the feature aggregation process should optimally
                         utilize useful information from all three features while minimizing the impact of irrelevant
                         information. Previous research, such as that conducted in [2,11], has made numerous attempts
                         to explore this topic. However, both studies employ equal-weight feature aggregation for each
                         channel. In an effort to enhance the efficacy of feature aggregation, we have implemented
                         a channel interaction strategy. As illustrated in Figure 1, the RGB, depth, and fused feature
                         maps are initially concatenated. CIM units are then utilized to assign adaptive weights to the
                         feature channels. Subsequent transposed convolution based up-sampling processes further
                         improve the resolution of the fused feature map.
                               The grasp prediction head is comprised   of several  convolution calculation modules and
                         is able to predict grasp quality, cos 2∅ e i,j , sin 2∅
                                                                               e i,j , and grasp opening width heatmaps,
                         which are employed to construct grasp rectangles.

                         4.2. Feature Extraction Pipeline
                         4.2.1. Residual Connection Based Stem Module (RSM)
                              In our previous study, we discovered that feeding raw data directly into the trans-
                         former layer and training the neural network with the stochastic gradient descent (SGD)
                         optimizer results in a high dependency on initialization seeds, resulting in challenging
                         training and slow convergence. Drawing upon the insights provided by articles [32,33], we
                         devised the RSM module, which renders the training process less sensitive to the pre-set
                         hyperparameters and fosters network convergence. Moreover, RSM can effectively reduce
                         data dimensionality with minimal computational overhead.
                              The residual network has proven to be highly effective in various applications such
                         as image classification, object detection, and moving object tracking. To capitalize on
                         its exceptional performance, we adopt a RSM module to generate a compact feature
                         representation, thereby addressing the inferior feature representation capability of the
                         linear projection.
                              Taking inspiration from [34], the stem module comprises two streams, as depicted in
                         Figure 2. The first stream is composed of a sequence of convolution, Gaussian error linear unit
                         (GELU) [35], and batch normalization (BN) [36] processes. The convolution modules utilize
                         as  image classification,
                          exceptional      performance,    object    detection,
                                                               we adopt       a RSM andmodule
                                                                                           movingtoobject        tracking.
                                                                                                          generate           To capitalize
                                                                                                                       a compact              on its
                                                                                                                                    feature repre-
                         exceptional      performance,        we    adopt    a  RSM       module      to generate
                          sentation, thereby addressing the inferior feature representation capability of the linear  a  compact   feature   repre-
                         sentation,
                          projection.thereby addressing the inferior feature representation capability of the linear
                         projection.
                                Taking inspiration from [34], the stem module comprises two streams, as depicted in
Sensors 2023, 23, 3340         Taking
                          Figure  2. The  inspiration
                                             first stream  from    [34], the stem
                                                              is composed        of a module
                                                                                        sequencecomprises          two streams,
                                                                                                       of convolution,             as depicted
                                                                                                                            Gaussian           7 ofin
                                                                                                                                       error linear 19
                         Figure   2. The [35],
                          unit (GELU)       first stream
                                                   and batch is composed
                                                                  normalization  of a sequence
                                                                                         (BN) [36]of     convolution,
                                                                                                       processes.     The Gaussian
                                                                                                                           convolutionerror  linear
                                                                                                                                          modules
                         unit  (GELU)
                          utilize          [35], and
                                  1 × 1 (stride         batch
                                                     = 1),  3 × 3normalization
                                                                     (stride = 2), and  (BN)1 [36]     processes.
                                                                                               × 1 (stride     = 1) The    convolution
                                                                                                                     kernels,            modules
                                                                                                                                respectively.   This
                         utilize
                          approach1  × 1  (stride
                                       ensures      =  1),
                                                    that    3
                                                           no ×  3  (stride
                                                                information   =  2),
                                                                                   is and   1  ×
                                                                                       neglected. 1  (stride
                                                                                                       The     = 1)
                                                                                                             second  kernels,
                                                                                                                        stream respectively.
                                                                                                                                 includes   a  This
                                                                                                                                               2  ×2
                          1 × 1 (stride = 1), 3 × 3 (stride = 2), and 1 × 1 (stride = 1) kernels, respectively. This approach
                         approach
                          (stride  =   ensures
                                      1) average   that   no information
                                                      pooling     stage,   a  1  ×is1 neglected.
                                                                                       (stride   =  1) The   second
                                                                                                        kernel          stream includes
                                                                                                                  convolution,    GELU,    a 2 ×BN
                                                                                                                                           and      2
                          ensures that no information is neglected. The second stream includes a 2 × 2 (stride = 1)
                         (stride
                          modules.=  1)  average
                                       This          pooling
                                                mechanism         stage,
                                                                 enables   a 1the× 1  (stride
                                                                                    expression   =  1)ofkernel   convolution,
                                                                                                          features
                          average pooling stage, a 1 × 1 (stride = 1) kernel convolution, GELU, and BN modules. This  while       GELU,
                                                                                                                              incurring   and
                                                                                                                                          minimalBN
                         modules.
                          computational
                          mechanism    This    mechanism
                                               costs.the
                                          enables       The      enablesof
                                                               outputs
                                                           expression      ofthe
                                                                               theseexpression
                                                                               features  two  streams
                                                                                           while      of features     while computational
                                                                                                           are combined
                                                                                                    incurring     minimal    incurring
                                                                                                                              to generateminimal
                                                                                                                                            thecosts.
                                                                                                                                                  en-
                         computational
                          coding   features,
                          The outputs          costs.
                                                 which
                                           of these    The
                                                      twoare  outputs
                                                                then fed
                                                             streams      of  these
                                                                         areinto        two   streams
                                                                                    the self-attention
                                                                              combined                     are
                                                                                             to generate and    combined     to  generate
                                                                                                                    cross-attention
                                                                                                              the encoding                 the
                                                                                                                                      procedures.
                                                                                                                               features,         en-
                                                                                                                                         which are
                         coding
                          then fedfeatures,
                                     into the which      are then
                                                 self-attention        fedcross-attention
                                                                     and    into the self-attention
                                                                                                 procedures. and cross-attention procedures.
                                               1×1 Conv             3×3 Conv             1×1 Conv
                                                 stride=1
                                               1×1   Conv             stride=2
                                                                    3×3   Conv             stride=1
                                                                                         1×1   Conv
                                                stride=1
                                               BN   GELU             stride=2
                                                                    BN   GELU             stride=1
                                                                                         BN   GELU
                             input             BN GELU              BN GELU              BN GELU                       output
                           features
                            input                                    1×1 Conv                                         features
                                                                                                                      output
                          features           2×2 AvgPool              stride=1
                                                                    1×1   Conv                                       features
                                             2×2stride=1
                                                  AvgPool            stride=1
                                                                    BN GELU
                                               stride=1                                     RSM
                                                                    BN GELU
                                                                                            RSM
                          AvgPool : Average pooling         BN   : Batch normalization                   pixel-level addition
                          Conv :: Average
                          AvgPool   2D convolution
                                            pooling         GELU: :Batch
                                                            BN      Gaussian Error Linear Unit
                                                                         normalization                   pixel-level addition
                          Conv    : 2D convolution          GELU : Gaussian Error Linear Unit
                         Figure 2. Input data feature extraction diagram using RSM.
                         Figure2.
                         Figure    Inputdata
                                2.Input  datafeature
                                              featureextraction
                                                      extraction diagram
                                                                 diagram using
                                                                         using RSM.
                                                                               RSM.
                         4.2.2. Cross-Modal Feature Encoding Based on MIM
                          4.2.2. Cross-Modal
                         4.2.2.  Cross-Modal Feature Encoding
                                                           Encoding Based
                                                                       Based on on MIM
                                                                                    MIM
                                The proposedFeatureMIM module is used        to execute     feature extraction and bilateral RGB
                                The proposed MIM module is used to execute feature extraction and bilateral RGB and
                         and depth cross-modal fusion strategies. As shown in Figure extraction
                               The   proposed     MIM   module    is used   to  execute    feature  3, Each MIM   and   bilateral
                                                                                                                      module       RGB
                                                                                                                               consists
                          depth cross-modal fusion strategies. As shown in Figure 3, Each MIM module consists of
                         and   depth  cross-modal     fusion  strategies.  As  shown    in  Figure  3,
                         of two patch embedding blocks, two LMHSA blocks, one LMHCA module and two sum-Each   MIM    module   consists
                          two patch embedding blocks, two LMHSA blocks, one LMHCA module and two summation
                         of two patch
                         mation     units.embedding
                                           The patch blocks,     two LMHSA
                                                        aggregation    module,blocks,
                                                                                   composed  one LMHCA
                                                                                                 by a 2 × 2module       and two
                                                                                                              convolution     with sum-
                                                                                                                                      the
                          units. The patch aggregation module, composed by a 2 × 2 convolution with the stride = 2
                         mation
                         stride   =units.
                                    2 and  The
                                            layerpatch  aggregation
                                                   normalization       module,
                                                                    block,  is    composed
                                                                               used   to         by a patches
                                                                                         aggregate     2 × 2 convolution
                                                                                                                 into  a      with
                                                                                                                         single      the
                                                                                                                                  image
                          and layer normalization block, is used to aggregate patches into a single image and produce
                         stride
                         and     = 2 and hierarchical
                               produce     layer normalization block, isThe    used  to aggregate     patches   into   a singlefeatures
                                                                                                                                 image
                          hierarchical  representation.representation.
                                                           The LMHSA module       LMHSA
                                                                                      is usedmodule      is used
                                                                                                to extract         to extract
                                                                                                            features   by spatial-wise
                         and
                         by    produce    hierarchical
                             spatial-wiseThe             representation.
                                              self-attention. The LMHCA     The   LMHSA
                                                                               modulefused    module
                                                                                          is to compute is used   to
                                                                                                            fused on  extract
                                                                                                                    features  features
                                                                                                                              based on
                          self-attention.         LMHCA module        is to compute             features based         cross-attention.
                         by  spatial-wise self-attention.
                         cross-attention.     The  summation  Theoperation
                                                                   LMHCAhelps  moduleto  is to compute
                                                                                         achieve   mutual  fused   features support.
                                                                                                             information     based on
                         The summation operation helps to achieve mutual information support.
                         cross-attention. The summation operation helps to achieve mutual information support.

                             input                Patch               LMHSA                   output
                          RGB  features
                            input              Aggregation
                                                 Patch                 block
                                                                      LMHSA                 RGB  features
                                                                                              output
                          RGB features         Aggregation             block                RGB features
                                                                      LMHCA                      output
                                               MIM
                                                                       block
                                                                      LMHCA                  fused features
                                                                                                output
                                               MIM
                                                                       block                fused features
                              input             Patch          LMHSA                            output
                         depth  features
                             input          Aggregation
                                                Patch            block
                                                               LMHSA                        depth  features
                                                                                               output
                         depth features     Aggregation          block                      depth features
                                             Pixel-wise addition
                                             Pixel-wise addition
                         Figure 3.
                         Figure    The structure
                                3. The  structure of
                                                  of the
                                                     the MIM
                                                         MIM module.
                                                              module.
                         Figure 3. The structure of the MIM module.
                          ••    Light weight
                                Light  weight multi-head
                                                 multi-head self-attention
                                                                self-attention (LMHSA)
                                                                                 (LMHSA) blockblock
                         •      Light
                                As     weight
                                As shown
                                    shown   in  multi-head
                                             in Figure
                                                Figure       theself-attention
                                                        4,4,the LMHSA
                                                                 LMHSAblock     (LMHSA)
                                                                            block contains
                                                                                   contains  block
                                                                                            three  parts,
                                                                                               three parts,which
                                                                                                             whichareare
                                                                                                                      local  perception,
                                                                                                                          local  percep-
                           LMHSA
                          tion,As    and IRFFN
                                    shownand
                                 LMHSA             modules.
                                            in Figure           The
                                                  IRFFN4,modules.
                                                            the LMHSApurpose  of
                                                                        Theblock  the local
                                                                                   contains
                                                                             purpose         perception
                                                                                        of thethree
                                                                                                localparts,module  [32]
                                                                                                                    are localequip
                                                                                                             which module
                                                                                                       perception        is to       isthe
                                                                                                                                 percep-
                                                                                                                                [32]    to
                           model
                         tion,     with
                          equipLMHSA    the  ability
                                          andwith
                                  the model          to
                                                 IRFFN   extract
                                                      themodules. local features
                                                            ability to The        while
                                                                            purpose
                                                                        extract  local of preserving
                                                                                           the local
                                                                                        features       its long-range
                                                                                                      perception
                                                                                                  while                capabilities.
                                                                                                                   module
                                                                                                           preserving                   To
                                                                                                                               [32] is to
                                                                                                                        its long-range
                           avoid the
                         equip    losing long-range
                                      model    with the information,     a shortcut
                                                           ability to extract   localmechanism      is incorporated.
                                                                                       features while                  This
                                                                                                          preserving its      particular
                                                                                                                            long-range
                           element is visually highlighted in Figure 4 using yellow annotations. Next, we apply LMHSA
                           computation to the feature transformation, represented in light green in Figure 4. To enhance
                           the representation ability of tokens, we introduce the inverted residual feed-forward network
                           module, or IRFFN, which can perform dimensional expansion and non-linear transformation
                           on each token.
                                      capabilities. To avoid losing long-range information, a shortcut mechanism is incorpo-
                                      rated. This particular element is visually highlighted in Figure 4 using yellow annotations.
                                      Next, we apply LMHSA computation to the feature transformation, represented in light
                                      green in Figure 4. To enhance the representation ability of tokens, we introduce the in-
Sensors 2023, 23, 3340                                                                                                       8 of 19
                                      verted residual feed-forward network module, or IRFFN, which can perform dimensional
                                      expansion and non-linear transformation on each token.

                                                       LMHSA Block

                                          input             3×3 DW-                                                  output
                                                             Conv                 LMHSA             IRFFN
                                        features                                                                    features

                                                       Pixel-wise addition

                                      Figure4.
                                      Figure   LMHSAblock
                                             4.LMHSA blockfor
                                                           forRGB
                                                              RGBand
                                                                  andDepth
                                                                     Depthfeatures
                                                                           features extraction.
                                                                                    extraction.

                                           Asdescribed
                                          As   describedinin[37],[37],the
                                                                        the    original
                                                                             original     self-attention
                                                                                       self-attention         module
                                                                                                          module          utilizes
                                                                                                                     utilizes        linear
                                                                                                                                linear        mapping
                                                                                                                                         mapping      to de- to
                                   derive
                                  rive   thethe   query
                                              query       matrix
                                                      matrix     𝑄, Q,
                                                                    keykey     matrix
                                                                            matrix   𝐾,K,andand    value
                                                                                               value       matrix𝑉.V.
                                                                                                        matrix        TheThe  dimensions
                                                                                                                           dimensions       ofof𝑄,Q,𝐾K and
                                                                                                                                                         and
                                  𝑉V are
                                       are given
                                             given byby H𝐻 ××𝑊 W×  × 𝑑d𝑘k,, H 𝐻× ×𝑊 W ××𝑑dk and
                                                                                           𝑘
                                                                                               and H  𝐻× ×𝑊 W ××𝑑dv, , respectively,
                                                                                                                    𝑣
                                                                                                                                           where H
                                                                                                                         respectively, where         𝐻× ×𝑊   W
                                  represents the number of image patches, and 𝑑𝑘k and 𝑑𝑣 are the dimensions of the tensorK
                                   represents     the  number     of   image     patches,   and    d  and   dv  are the   dimensions      of  the   tensor
                                  𝐾and andV. 𝑉.
                                              Subsequently,
                                                 Subsequently,  thethe
                                                                     self-attention
                                                                           self-attentionmodule
                                                                                             module  cancan
                                                                                                          be expressed
                                                                                                               be expressed as theas following
                                                                                                                                      the following formula:
                                                                                                                                                         for-
                                  mula:
                                                                                                               QK T
                                                                                                                    
                                                                        Attn( Q, K, V ) = So f tmax √           𝑄𝐾  𝑇 V                                     (3)
                                                                                                                 d
                                                                            𝐴𝑡𝑡𝑛(𝑄, 𝐾, 𝑉) = 𝑆𝑜𝑓𝑡𝑚𝑎𝑥 ( k ) 𝑉                                                (3)
                                                                                                                √𝑑𝑘
                                           While the original self-attention algorithm can effectively handle various visual tasks, it
                                          While the
                                   is associated      original
                                                    with   high self-attention
                                                                  computationalalgorithm
                                                                                       costs. As can     effectively
                                                                                                     such, numeroushandle         various
                                                                                                                          researchers        visual
                                                                                                                                          have        tasks,
                                                                                                                                                  dedicated
                                  itefforts
                                      is associated    with high
                                             to addressing           computational
                                                              this issue.     In our work, costs.   As such,
                                                                                             we adopt           numerous
                                                                                                           a similar          researchers
                                                                                                                        approach    to that inhave     dedi-
                                                                                                                                                 [37] which
                                  cated
                                   involves efforts
                                                the to   of k × k depth-wise
                                                    useaddressing       this issue.convolutional
                                                                                       In our work, operations
                                                                                                         we adopt awith  similar   approach
                                                                                                                               stride             to thatthe
                                                                                                                                        of s to reduce      in
                                   dimensionality
                                  [37]   which involves of thethe
                                                                keyuse
                                                                     and       𝑘 × 𝑘matrices,
                                                                           ofvalue     depth-wise thereby   mitigating the
                                                                                                       convolutional            computational
                                                                                                                           operations                burden.
                                                                                                                                           with stride      of
                                  𝑠The   computation
                                      to reduce           associated with
                                                   the dimensionality          ofthe
                                                                                  thedepth-wise
                                                                                      key and value   convolution
                                                                                                           matrices,can    be expressed
                                                                                                                        thereby    mitigating as follows:
                                                                                                                                                   the com-
                                  putational burden. The computation                  associated with the depth-wise convolution can be
                                  expressed as follows:                        
                                                                                       Q = Linear ( X )
                                                                                 K = Linear ( DWConv( X ))                                                  (4)
                                                                                        𝑄 = 𝐿𝑖𝑛𝑒𝑎𝑟(𝑋)
                                                                                 V𝐾==Linear     ( DWConv( X ))
                                                                               
                                                                                 {      𝐿𝑖𝑛𝑒𝑎𝑟(𝐷𝑊𝐶𝑜𝑛𝑣(𝑋))                                                  (4)
                                                                                   𝑉 = 𝐿𝑖𝑛𝑒𝑎𝑟(𝐷𝑊𝐶𝑜𝑛𝑣(𝑋))
                                           Equation (4) describes the lightweight self-attention mechanism used in our approach,
                                   where      X represents
                                          Equation             the input
                                                       (4) describes        thefeature,   DWConv(
                                                                                 lightweight            ·) denotesmechanism
                                                                                                   self-attention       the depth-wise usedconvolution
                                                                                                                                               in our ap-
                                   operation,
                                  proach,          and𝑋Linear(
                                               where              ·) is the
                                                           represents       the linear   feature, 𝐷𝑊𝐶𝑜𝑛𝑣(·)
                                                                                 input operation.         To further      enhance
                                                                                                                       denotes    theperformance,
                                                                                                                                        depth-wise con-    we
                                   incorporate
                                  volution          a position
                                                operation,    and bias   term. Then
                                                                     𝐿𝑖𝑛𝑒𝑎𝑟(·)           the lightweight
                                                                                     is the   linear operation.self-attention
                                                                                                                        To furthercan be   defined
                                                                                                                                        enhance        as:
                                                                                                                                                     perfor-
                                  mance, we incorporate a position bias term. Then thelightweight                            self-attention can be
                                                                                                                 QK   T
                                  defined as:                  LightAttn( Q, K, V, B) = So f tmax √ + B V                                                   (5)
                                                                                                                    di 𝑇
                                                                                                                  𝑄𝐾
                                                                   𝐿𝑖𝑔ℎ𝑡𝐴𝑡𝑡𝑛(𝑄, 𝐾, 𝑉, 𝐵) = 𝑆𝑜𝑓𝑡𝑚𝑎𝑥(                      + 𝐵)𝑉
                                           In the above formula, the dimensions of the query √𝑑                    (K)𝑖 and value (V) matrices (5)         are
                                   reduced     to 1/s 2 due to the application of stride s in the depth-wise convolution kernel. d is
Sensors 2023, 23, x FOR PEER REVIEW                                                                                                                   9 ofi 20
                                          In the above
                                   the dimension           formula,
                                                        of Q.             the dimensions
                                                               The structure                    of the query
                                                                                    of the lightweight            (𝐾) andself-attention
                                                                                                             multi-head       value (𝑉) matrices module   areis
                                                       2
                                  reduced      to  1/𝑠
                                   depicted in Figure 5.  due   to the    application     of stride    𝑠  in  the depth-wise       convolution       kernel.
                                  𝑑𝑖 is the dimension of 𝑄. The structure of the lightweight multi-head self-attention mod-
                                                          input features
                                  ule is depicted in Figure         5.

                                                               k×k DW-Conv k×k DW-Conv
                                                                  stride=s    stride=s             DW-Conv: Depth-wise convolution

                                                                                                    Linear: Fully connected layer
                                                   Linear            Linear         Linear
                                                       Q             K             V               MHSA: Multi-Head Self-Attention
                                                                     MHSA
                                                                                                       Pixel-wise addition

                                                               output features

                                       Figure 5. Lightweight multi-head self-attention block.

                                            In the robot grasp detection architecture, the IRFFN layer serves to expand and re-
                                       duce feature dimensions, allowing for non-linear transformation. However, unlike the
                                       structure proposed in [32], we utilize an improved IRFFN layer to boost the expressive-
                                       ness of the features. Figure 6 displays the structure of our proposed IRFFN layer which
                                                                                                 Pixel-wise addition

                                                          output features

Sensors 2023, 23, 3340              Figure 5. Lightweight multi-head self-attention block.                                                   9 of 19

                                         In the robot grasp detection architecture, the IRFFN layer serves to expand and re-
                                    duceInfeature  dimensions,
                                            the robot              allowing
                                                       grasp detection        for non-linear
                                                                         architecture,         transformation.
                                                                                       the IRFFN                 However,
                                                                                                    layer serves to          unlike
                                                                                                                     expand and      the
                                                                                                                                 reduce
                                    structure  proposed   in  [32], we  utilize an improved     IRFFN   layer to boost  the expressive-
                                    feature dimensions, allowing for non-linear transformation. However, unlike the structure
                                    ness of the
                                    proposed  in features. Figure
                                                 [32], we utilize an6improved
                                                                       displaysIRFFN
                                                                                 the structure
                                                                                        layer to of ourthe
                                                                                                 boost   proposed   IRFFNoflayer
                                                                                                           expressiveness         which
                                                                                                                            the features.
                                    consists of two  branches.
                                    Figure 6 displays the structure of our proposed IRFFN layer which consists of two branches.

                                                        1×1 Conv            3×3 Conv         1×1 Conv
                                                         stride=1            stride=2         stride=1
                                                       BN GELU             BN GELU          BN GELU
                                      input                                                                           output
                                     features                               1×1 Conv                                 features
                                                                             stride=1
                                                                           BN GELU
                                                                                               IRFFN

                                                Conv : 2D convolution          GELU : Gaussian Error Linear Unit
                                                BN : Batch normalization         pixel-level addition

                                    Figure 6. IRFFN block diagram.

                                    ••    Light weight multi-head cross-attention (LMHCA) module
                                         The fusion algorithm we developeddeveloped tackles
                                                                                       tackles the
                                                                                                 the challenge
                                                                                                      challenge of of how
                                                                                                                      how toto optimize
                                                                                                                               optimize thethe uti-
                                                                                                                                                uti-
                                  lization of information
                                                informationfrom fromRGB RGBandanddepth
                                                                                   depthmodalities,
                                                                                           modalities,     taking
                                                                                                         taking     into
                                                                                                                 into    account
                                                                                                                       account      their
                                                                                                                                 their     respec-
                                                                                                                                       respective
                                  importance.
                                  tive  importance.To further   enhance
                                                        To further          the robustness
                                                                       enhance                of theoffused
                                                                                 the robustness               features,
                                                                                                         the fused        we designed
                                                                                                                      features,            a cross-
                                                                                                                                 we designed      a
                                  attention   mechanism     and    a  modal   reweighting     strategy.   These   techniques
                                  cross-attention mechanism and a modal reweighting strategy. These techniques work in          work   in tandem
                                  to ensure
                                  tandem     to that  thethat
                                                 ensure   most thesalient   features
                                                                    most salient       from each
                                                                                    features    frommodality       are given
                                                                                                       each modality            the appropriate
                                                                                                                          are given   the appro-
                                  attention
                                  priate       and weight
                                           attention         in the final
                                                       and weight     in thefusion   result. result.
                                                                              final fusion
                                         The proposed
                                              proposedmodalmodalinteraction
                                                                     interactionstrategy
                                                                                   strategyis illustrated   in Figure
                                                                                               is illustrated           7. To7.address
                                                                                                                in Figure                the issue
                                                                                                                                 To address     the
                                  of missing
                                  issue         local associations
                                          of missing                  and structural
                                                       local associations               information
                                                                              and structural            during during
                                                                                                 information     cross-attention    computation,
                                                                                                                          cross-attention    com-
                                  we   incorporate
                                  putation,            local perception
                                               we incorporate                units into
                                                                  local perception        theinto
                                                                                        units   design.    Subsequently,
                                                                                                     the design.             multi-head
                                                                                                                    Subsequently,            cross-
                                                                                                                                     multi-head
                                  attention    operations   are   employed      to extract   high-level    semantic
                                  cross-attention operations are employed to extract high-level semantic features from
Sensors 2023, 23, x FOR PEER REVIEW
                                                                                                                       features   from   the  RGB
                                                                                                                                           10 ofthe
                                                                                                                                                 20
                                  and    depth    features.  Finally,    the  output   features    are  fed  into  the  IRFFN
                                  RGB and depth features. Finally, the output features are fed into the IRFFN unit to enable      unit  to  enable
                                  dimensional expansion
                                  dimensional       expansion andand non-linear
                                                                       non-linear transformation.
                                                                                    transformation.

                                                     LMHCA Block

                                       RGB              3×3 Conv
                                     features            stride=1
                                                                                                                      fused
                                                                                 LMHCA            IRFFN
                                                                                                                     features
                                      depth            3×3 Conv
                                     features           stride=1

                                                     Pixel-wise addition

                                    Figure 7.
                                    Figure    LMHCA block
                                           7. LMHCA block for
                                                          for fused
                                                              fused feature
                                                                    feature extraction.

                                          The token
                                          The  token compounding
                                                       compounding methodmethod proposed
                                                                                    proposed byby [38]
                                                                                                   [38] has
                                                                                                        has demonstrated       outstanding
                                                                                                            demonstrated outstanding
                                    performance in vision-and-language representation learning. Building uponapproach,
                                    performance    in  vision-and-language      representation  learning.  Building   upon   this  this ap-
                                    we propose
                                    proach,       a lightweight
                                             we propose            multi-head
                                                             a lightweight       cross-attention
                                                                             multi-head          method tomethod
                                                                                           cross-attention   facilitatetothe fusion of
                                                                                                                          facilitate  theRGB
                                                                                                                                          fu-
                                    and   depth  features   in  robotic  gripping    applications.   The lightweight     multi-head
                                    sion of RGB and depth features in robotic gripping applications. The lightweight multi-             cross-
                                    attention
                                    head       unit comprises
                                           cross-attention    unittwo parts: a multi-head
                                                                   comprises     two parts: cross-attention  component andcomponent
                                                                                             a multi-head cross-attention        a modality
                                    reweighting-based      feature  fusion  component.    Figure  8 presents a detailed
                                    and a modality reweighting-based feature fusion component. Figure 8 presents a detailedschematic   of the
                                    proposed    procedure.    Specifically, in the  cross-attention  module,  we   employ
                                    schematic of the proposed procedure. Specifically, in the cross-attention module, we em- linear  layer to
                                    acquire matrices Qrgb , Qd for RGB and depth streams, respectively. Depth-wise convolution
                                    ploy linear layer to acquire matrices 𝑄𝑟𝑔𝑏 , 𝑄𝑑 for RGB and depth streams, respectively.
                                    Depth-wise convolution and linear mapping are used to obtain the matrices 𝐾𝑟𝑔𝑏 , 𝑉𝑟𝑔𝑏 ,
                                    𝐾𝑑 , 𝑉𝑑 accordingly. Then, the lightweight cross-attention computation can be expressed
                                    as Equation (6).
                                                                                                                   𝑄𝑟𝑔𝑏 𝐾𝑑 𝑇
                                                          𝐿𝑖𝑔ℎ𝑡𝐶𝑟𝑜𝑠𝑠𝐴𝑡𝑡𝑒𝑛(𝑅𝐺𝐵2𝑑𝑒𝑝𝑡ℎ) = 𝑆𝑜𝑓𝑡𝑚𝑎𝑥(                                + 𝐵)𝑉𝑑
                                                                                                                     √𝑑𝑖
                                                                                                                                                (6)
                                                                                                               𝑄𝑑 𝐾𝑟𝑔𝑏 𝑇
                                                         𝐿𝑖𝑔ℎ𝑡𝐶𝑟𝑜𝑠𝑠𝐴𝑡𝑡𝑒𝑛(𝑑𝑒𝑝𝑡ℎ2𝑅𝐺𝐵) = 𝑆𝑜𝑓𝑡𝑚𝑎𝑥(                             + 𝐵)𝑉𝑟𝑔𝑏
                                              performance in vision-and-language representation learning. Building upon this ap-
                                              proach, we propose a lightweight multi-head cross-attention method to facilitate the fu-
                                              sion of RGB and depth features in robotic gripping applications. The lightweight multi-
                                              head cross-attention unit comprises two parts: a multi-head cross-attention component
Sensors 2023, 23, 3340                        and a modality reweighting-based feature fusion component. Figure 8 presents a detailed       10 of 19
                                              schematic of the proposed procedure. Specifically, in the cross-attention module, we em-
                                              ploy linear layer to acquire matrices 𝑄𝑟𝑔𝑏 , 𝑄𝑑 for RGB and depth streams, respectively.
                                              Depth-wise convolution and linear mapping are used to obtain the matrices 𝐾𝑟𝑔𝑏 , 𝑉𝑟𝑔𝑏 ,
                                           and𝐾𝑑linear mapping areThen,
                                                 , 𝑉𝑑 accordingly.   usedthe
                                                                          to obtain the matrices
                                                                             lightweight          Krgb , Vrgb
                                                                                          cross-attention     , Kd , Vd accordingly.
                                                                                                            computation                  Then, the
                                                                                                                                can be expressed
                                           lightweight   cross-attention
                                              as Equation (6).           computation   can  be expressed    as  Equation       (6).
                                                                                                                         T𝑇
                                                                                                                              
                                                                                                              Q𝑄rgb K𝐾
                                                                                                                  𝑟𝑔𝑏  d𝑑
                                                          
                                                          
                                                                𝐿𝑖𝑔ℎ𝑡𝐶𝑟𝑜𝑠𝑠𝐴𝑡𝑡𝑒𝑛(𝑅𝐺𝐵2𝑑𝑒𝑝𝑡ℎ)
                                                             LightCrossAtten  ( RGB2depth   ) = =So𝑆𝑜𝑓𝑡𝑚𝑎𝑥(
                                                                                                     f tmax      √          +
                                                                                                                            + B𝐵)𝑉V𝑑d
                                                                                                                   √d𝑑i 𝑖
                                                          
                                                                                                                          𝑇                   (6)(6)
                                                                                                             Q𝑄d𝑑K𝐾rgb
                                                                                                                      T
                                                                                                                               
                                                                                                                    𝑟𝑔𝑏
                                                                𝐿𝑖𝑔ℎ𝑡𝐶𝑟𝑜𝑠𝑠𝐴𝑡𝑡𝑒𝑛(𝑑𝑒𝑝𝑡ℎ2𝑅𝐺𝐵)     =  𝑆𝑜𝑓𝑡𝑚𝑎𝑥(                  + 𝐵)𝑉
                                                          
                                                          
                                                           LightCrossAtten  ( depth2RGB   ) =  So f tmax       √          + B   V𝑟𝑔𝑏
                                                                                                                                   rgb
                                                               {                                                 √d𝑑i 𝑖
                                                          

                         input RGB features                                input depth features

                                                                                                            MHCA: Multi-head cross attention computation
                           k×k DW-Conv        k×k DW-Conv       k×k DW-Conv   k×k DW-Conv
                              stride=s           stride=s          stride=s      stride=s
                                                                                                            DW-Conv: Depth-wise convolution

             Linear           Linear            Linear            Linear         Linear            Linear
                                                                                                            Linear: Fully connected layer

                  Qrgb          Kd                    Vd           Vrgb              Krgb         Qd                       Multi-head cross attention part

                              MHCA                                              MHCA

          RGB token                                                                          depth token                   Modal re-weighting part

                                                            ©
                                        1×1 Conv                       1×1 Conv                                 Pixel-wise multiplication
                                     out_channels=1                 out_channels=1
                                         stride=1                       stride=1
                                                            ©                                                   Pixel-wise addition

                                                                                                               Sigmoid function

                                                                                                            © Channel-wise concatenation
                                                 output fused features

                                              Figure
                                           Figure    8. Multi-head
                                                  8. Multi-head    cross-attentionblock
                                                                 cross-attention   blockdiagram.
                                                                                        diagram.

                                                RGB and depth tokens are exported according to the upper operation. These two
                                           tokens are concatenated and fed into the modality reweighting process to create fused
                                           features. Different from the strategy of [39], we developed a novel modal reweighting
                                           method and assign appropriate adaptive weights to RGB and depth tokens, respectively, to
                                           obtain effective fused features. The detailed structure of the modality reweighting strategy
                                           can be seen in the bottom half of Figure 8. First, we concatenate the RGB and depth tokens,
                                           followed by using 1 × 1 convolution and SoftMax functions to learn adaptive weights
                                           for both token types. The fused features are obtained by reweighting the RGB and depth
                                           tokens and adding them at the pixel level.

                                           4.3. Feature Aggregation Based on Channel Interaction Module (CIM)
                                                In Figure 1, three feature maps cf7, df7 and ff7 can be obtained after the feature extraction
                                           procedures. These feature maps are subsequently aggregated for grasp prediction.
                                                Since each of these maps contains both valuable and non-valuable information, we
                                           apply the channel interaction method to reweight each channel of the connected features
                                           accordingly. To accomplish this, we use an SE-block [40] to improve the sensitivity of
                                           valuable channels and suppress useless ones. The structure of the CIM unit is shown in
                                           Figure 9.
                              In Figure 1, three feature maps cf7, df7 and ff7 can be obtained after the feature ex-
                         traction procedures. These feature maps are subsequently aggregated for grasp prediction.
                              Since each of these maps contains both valuable and non-valuable information, we
                         apply the channel interaction method to reweight each channel of the connected features
                         accordingly. To accomplish this, we use an SE-block [40] to improve the sensitivity of val-
Sensors 2023, 23, 3340                                                                                            11 of 19
                         uable channels and suppress useless ones. The structure of the CIM unit is shown in Fig-
                         ure 9.

                                            CIM                                                   F                F
                                                                                       GAP               RELU
                                                                                                  C                C
                             C                                                                                                         C
                                            1×1 Conv     3×3 Conv       1×1 Conv
                         H                  stride=1      stride=1      stride=1
                                                                                                                                   H
                                                                                      1×1 Conv
                                 W                                                                                                         W
                                                                                       stride=1
                          multimodal                                                                                                    output
                           features                                                                                                    features

                                            Pixel-wise multiplication              Pixel-wise addition          Sigmoid function

                                    Channelinteraction
                         Figure9.9.Channel
                         Figure             interaction module.
                                                       module.

                              To generate
                              To generateaafeature
                                            featuremap
                                                    mapthat
                                                         that
                                                            is is
                                                               of of
                                                                  thethe  same
                                                                       same  sizesize as the
                                                                                   as the     input
                                                                                          input      image,
                                                                                                 image,       we employ
                                                                                                         we employ    the the
                         sameup-sampling
                         same  up-samplingtechniques
                                             techniques  used
                                                       used in in
                                                                thethe  feature
                                                                     feature     decoding
                                                                             decoding    stepstep  in final
                                                                                               in the the final stages
                                                                                                            stages      of the
                                                                                                                   of the
                         featureaggregation
                         feature aggregationprocess.
                                              process.

                         4.4. Robot
                         4.4. RobotGrasp
                                     GraspPrediction
                                           Prediction
                               Asoutlined
                               As  outlinedinin  Sections
                                              Sections 3 and3 and   4.1,neural
                                                               4.1, the     theneural
                                                                                     network  network      we designed
                                                                                                  we designed             is expected
                                                                                                                  is expected  to gen- to
                         generate
                         erate fourfour heatmaps,
                                    heatmaps,   namely  𝑄̃ , sin(2∅
                                                     namely   Q,   ̃ 𝑖,𝑗 ),
                                                               e sin     2∅ ecos(2∅  ̃ 𝑖,𝑗 )2∅
                                                                              i,j , cos             ̃ , toW,
                                                                                               i,j and
                                                                                             eand   𝑊        to facilitate
                                                                                                          efacilitate robotrobot  grasping.
                                                                                                                            grasping.
                             accomplishthis,
                         To accomplish    this,four
                                                fourseparate
                                                     separatebranches
                                                                branches     of of
                                                                                 2-D2-D     convolutions
                                                                                      convolutions        areare  constructed.
                                                                                                              constructed.

                         4.5. Loss
                         4.5. LossFunction
                                     Function
                                We   train
                               We train thetheneural
                                                neuralnetwork
                                                        network byby   minimizing
                                                                    minimizing         thethe    discrepancy
                                                                                            discrepancy              between
                                                                                                                  between         the predicted
                                                                                                                             the predicted
                         grasps(𝐺
                         grasps    (̃G) andthe
                                     ) and
                                     e      theground
                                                  ground  truth
                                                        truth   grasps
                                                              grasps    (𝐺).(G).
                                                                               To To    accomplish
                                                                                    accomplish         this,this,   we utilize
                                                                                                              we utilize         the smooth
                                                                                                                            the smooth  L1 L1
                         loss function
                         loss  function[41]
                                          [41]ininour
                                                   ourwork.
                                                       work.This
                                                              This   loss
                                                                  loss     function
                                                                        function          is defined
                                                                                      is defined            as follows:
                                                                                                       as follows:
                                                                      ∑𝑘∈{𝑄,∅,𝑊} 𝑠𝑚𝑜𝑜𝑡ℎ𝐿1 (𝐺̃
                                                    ̃             𝑁                                   𝑘  𝐺𝑘 )
                                                     𝐿(𝐺 − 𝐺) = ∑N                                      𝑖,𝑗 −                           (7)
                                                                                                                          
                                                  L Ge − G = ∑i𝑖 ∑        k ∈{ Q,∅,W }
                                                                                          smooth       L1   Gfk 𝑖,𝑗− G k
                                                                                                              i,j     i,j                    (7)
                               In Equation (7), N represents the number of pixels in the heatmap, and 𝑠𝑚𝑜𝑜𝑡ℎ𝐿1 (𝑥)
                                In Equation
                         is defined   as:      (7), N represents the number of pixels in the heatmap, and smoothL1 (x) is
                         defined as:                                                     𝑥2 2
                                                                                0.5
                                                                                  0.5××𝛽xβ, 𝑖𝑓|𝑥|
                                                                                              , i f | x<| <𝛽 β
                                                                             (
                                                         𝑠𝑚𝑜𝑜𝑡ℎ    (𝑥)   =
                                                                 𝐿1( x ) =   {                                                          (8) (8)
                                                         smooth L1
                                                                              |𝑥| − 0.5𝛽, 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
                                                                                | x | − 0.5β, otherwise
                              Here, the hyperparameter β controls the extent of smoothness and separates the
                         positive axis range into L1 loss and L2 loss parts. In our work, we set the parameter β to 1.

                         5. Evaluation
                         5.1. Experimental Methodology
                         5.1.1. Experiment Content
                                We designed four experiments to comprehensively evaluate the proposed method. The
                         first two experiments are comparison studies that aim to verify the performance of different
                         approaches on the Cornell and Jacquard datasets, respectively. The third experiment is an
                         ablation study that examines the effects of cross-attention and channel interaction strategies.
                         In this experiment, we evaluated the effectiveness of the modality adaptive reweighting
                         algorithm in the fused feature extraction stage and the effects of the channel interaction
                         algorithm in the feature aggregation stage. Additionally, we verified the effectiveness of
                         the proposed algorithm through a fourth physical experiment.

                         5.1.2. Datasets
                              We utilized two datasets, the Cornell dataset [1] and the Jacquard dataset [42], in our
                         experiments. The Cornell dataset is relatively small, comprising 240 distinct objects with
                         885 samples, while the Jacquard dataset is of medium size, consisting of 11,619 unique
                         objects and 54,485 different scenes. Both datasets provide RGB images and 3D dense cloud
                         data for each sample. Prior to training the neural network, we converted the 3D point
                         cloud data into depth images and adjusted their resolution to 224 × 224. We allocated 90%
                                          5.1.2. Datasets
                                              We utilized two datasets, the Cornell dataset [1] and the Jacquard dataset [42],
                                        experiments. The Cornell dataset is relatively small, comprising 240 distinct object
                                        885 samples, while the Jacquard dataset is of medium size, consisting of 11,619 u
Sensors 2023, 23, 3340                  objects and 54,485 different scenes. Both datasets provide RGB images12and
                                                                                                                 of 193D dense
                                        data for each sample. Prior to training the neural network, we converted the 3D
                                        cloud data into depth images and adjusted their resolution to 224 × 224. We allo
                                        90% of each dataset for training and the remaining 10% for testing. Given the sma
                         of each dataset for training and the remaining 10% for testing. Given the small size of the
                                        of the Cornell dataset, we augmented the dataset by performing augmentation oper
                         Cornell dataset, we augmented the dataset by performing augmentation operations such
                                        such as cropping and rotation.
                         as cropping and rotation.

                         5.1.3. Experiment5.1.3. Experiment Environment
                                              Environment
                               The training andThevalidation
                                                     training and    validation
                                                                 process          process was
                                                                          was conducted         conducted
                                                                                            on the  Ubuntuon      the operating
                                                                                                              20.04     Ubuntu 20.04 ope
                                          system,   utilizing  an  Intel  Core  i9-12900KF   CPU    clocked
                         system, utilizing an Intel Core i9-12900KF CPU clocked up to 5.20 GHz, 64 GB DDR4    up    to  5.20  GHz, 64 GB
                                          memory,     and  an  NVIDIA     GeForce   GTX   3090-Ti  graphics
                         memory, and an NVIDIA GeForce GTX 3090-Ti graphics card. This computing server is    card.    This  computing  se
                                          manufactured      by Kuankes
                         manufactured by Kuankes Co., Shanghai, China.    Co.,  Shanghai,  China.
                                               We set robot
                               We set up a real-world   up a real-world    robot
                                                               grasp scenario,  asgrasp  scenario,
                                                                                   depicted        as depicted
                                                                                            in Figure  10. For thisinexperiment,
                                                                                                                       Figure 10. For this
                         we gathered 30 iment,
                                          distinctwe   gathered
                                                   objects        30 distinct
                                                            on a desk.        objects
                                                                       An Orbbec       on a desk.
                                                                                     Femto-W  RGBD Ancamera
                                                                                                       Orbbecwas Femto-W
                                                                                                                      used asRGBD
                                                                                                                               the came
                                          usedaas
                         image sensor, while       the image
                                                 parallel       sensor,
                                                           gripper  was while   a parallel
                                                                         installed         gripper
                                                                                   at the end of thewas
                                                                                                     Eliteinstalled   at the end of the Eli
                                                                                                           EC-66 collaborative
                                          66 collaborative
                         robot to act as the                 robot to act
                                             clamping mechanism.           asto
                                                                       Prior  the  clamping
                                                                                 the          mechanism.
                                                                                     experiment,  a hand-eye Prior   to the experiment,
                                                                                                                calibration   was        a
                                          eye calibration   was   performed
                         performed to ensure proper operation of the system.   to ensure  proper  operation   of  the   system.

                           Femto-W
                         RGB-D camera

                                                                                                                    Elite EC-66
                                                                                                                       robot

                              Parallel
                              gripper

                         Figure 10. Physical experiment conditions. Experiment instruments include a Femto-W RGB-D
                         camera, an EC-66 collaborative robot, a parallel gripper, and some objects to be grasped.

                         5.1.4. Grasp Detection Metric
                              In all our experiments, we employ the grasp intersection over union (IoU) metric, which
                         is defined in Equation (9). The use of this metric allows for a quantitative evaluation of the
                         performance of our proposed method in terms of its ability to accurately predict grasps.

                                                                     Gdet ∩ GGT
                                                             IoU =              × 100%                                       (9)
                                                                     Gdet ∪ GGT

                              The Intersection over Union (IoU) metric is utilized in all experiments, as defined in
                         Equation (8). The numerator of the equation represents the area of overlap between the
                         detected grasp rectangle and the ground truth, while the denominator represents their union.
                         To be considered a valid detection, the detection results must exhibit the following properties:
                         •    IoU between the detection result and the ground truth should be above 25%;
                         •    The angle error between the detection result and the ground truth should be less than 30◦ .
                              In order to assess the overall detection accuracy, we conducted experiments on the
                         validation dataset whereby we tabulated the number of grasping rectangles that fulfilled
                         the specified criteria, as well as those that did not. This approach allowed for a thorough
                         and precise evaluation of the detection performance.
Sensors 2023, 23, 3340                                                                                                  13 of 19

                         5.1.5. Experiment Configuration
                              Our proposed architecture has input dimensions of 224 × 224 × 3 and 224 × 224 × 1
                         for RGB and depth images, respectively. The detailed size of each feature map is listed in
                         Table 1.

                         Table 1. Size of each feature map.

                          Feature Map                Size (H × W × C)              Feature Map           Size (H × W × C)
                          cf0, df0                     112 × 112 × 16               cf5, df5, ff5          14 × 14 × 184
                          cf1, df1, ff1                 56 × 56 × 46                cf6, df6, ff6          28 × 28 × 92
                          cf2, df2, ff2                 28 × 28 × 92                cf7, df7, ff7          56 × 56 × 46
                          cf3, df3, ff3                14 × 14 × 184                     f8               112 × 112 × 46
                          cf4, df4, ff4                  7 × 7 × 368                     f9               224 × 224 × 32

                              We utilized self-attention and cross-attention based feature encoders with 1, 2, 4, and
                         8 heads, and the corresponding number of block layers are 2, 2, 10, and 2, respectively.
                              To train the proposed neural network, AdamW stochastic gradient descent was used with
                         the batch size of 16. We implemented a warm-up and multi-step learning rate scheduler. The
                         maximum learning rate was configured to 1 × 10−4, with the learning rate being adjusted every
                         10 epochs. The multiplicative factor for the learning rate decay was set to 0.5, ensuring optimal
                         performance and stability during training. During the training process using the Jacquard
                         dataset, the neural network was initialized with random parameters and subsequently trained
                         over 15 epochs. Each epoch consisted of 3065 batches. In the subsequent training procedure
                         using the Cornell dataset, the neural network’s hyperparameters were initialized with the
                         parameters previously trained on the Jacquard dataset.

                         5.2. Experiement Results
                         5.2.1. Cornell Dataset Experiment Results
                              To compare the grasp detection performance of recent methods with our proposed
                         algorithm on the Cornell dataset, we conducted an experiment that evaluated image-wise
                         and object-wise grasp detection separately. Our algorithm achieved state-of-the-art accuracy
                         of 99.4% and 97.8% in image-wise and object-wise grasp detection, respectively, as shown
                         in Table 2. However, the average time expenditure is 17.7 ms, which is higher compared to
                         algorithms in [10–12] due to the complexity of our algorithm.

                         Table 2. Grasp detection results of different algorithms on Cornell dataset.

                                                                                 Accuracy (%)
                          Method                    Input                                                     Time (ms)
                                                                     Image-Wise            Object-Wise
                          Lenz [1]                 RGB-D                 73.9                   75.6             1350
                          Redmon [27]              RGB-D                   88                   87.1              76
                          Morrision [5]              D                     73                    69               19
                          Song [10]                RGB-D                  92.5                  90.3             17.2
                          Kumra [8]                RGB-D                  97.7                  96.6              20
                          Wang [6]                 RGB-D                 97.99                  96.7             41.6
                          Yu [9]                   RGB-D                 98.2                   97.1              25
                          Tian [11]                RGB-D                  98.9                    -               15
                          Tian [12]                RGB-D                  99.3                  91.1              12
                          Ours                     RGB-D                 99.4                   97.8             17.7

                             Figure 11 depicts some typical examples of heatmap regression results for quality,
                         angle, and width, as well as grasp detection results. As shown in the figure, the quality
                         heatmaps demonstrate the robustness of our proposed method, which contributes to the
                         superior performance of our grasp detection results.
                         Kumra [8]                   RGB-D                     97.7                  96.6                     20
                         Wang [6]                    RGB-D                    97.99                  96.7                    41.6
                         Yu [9]                      RGB-D                     98.2                  97.1                     25
                         Tian [11]                   RGB-D                     98.9                   -                       15
Sensors 2023, 23, 3340   Tian [12]                   RGB-D                     99.3                  91.1                     12 14 of 19
                         Ours                        RGB-D                     99.4                  97.8                    17.7

                                               RGB           Depth          Grasp          Qulity           Angle        Width

                         Kumra, 2020

                          Wang, 2022

                              Ours

                         Kumra, 2020

                          Wang, 2022

                              Ours

                          Figure 11.
                         Figure   11. Experiment
                                      Experiment results
                                                  results of
                                                          of the
                                                              the algorithms
                                                                  algorithms proposed
                                                                              proposedby byKumra
                                                                                            Kumraet   etal.
                                                                                                        al.[8]
                                                                                                            [8] in
                                                                                                                 in 2020,
                                                                                                                    2020, Wang
                                                                                                                           Wanget etal.
                                                                                                                                    al. [6]
                                                                                                                                         [6]
                          in 2022  and  our  method  on Cornell    dataset. The  1st and  2nd   columns    are  RGB
                         in 2022 and our method on Cornell dataset. The 1st and 2nd columns are RGB image and depth    image   and  depth
                          images. The
                         images.   The 3rd
                                        3rd column
                                            column shows
                                                    shows grasp
                                                            grasp detection
                                                                    detection results.
                                                                              results. The
                                                                                       The last
                                                                                           last three
                                                                                                 three columns
                                                                                                       columns illustrate
                                                                                                                   illustrate the
                                                                                                                              the quality,
                                                                                                                                  quality,
                          angle, and width heatmaps.
                         angle, and width heatmaps.

                         5.2.2. Jacquard Dataset Experiment Results
                               We also conducted a comparative analysis of our grasp detection algorithm with
                         that of several other methods [5,6,8–12] using the Jacquard dataset. Table 3 presents the
                         statistical results of our experiment with the Jacquard dataset. As is evident from the table,
                         our algorithm achieved the highest image-wise and object-wise detection accuracy of 96.7%
                         and 94.6%, respectively, on the Jacquard dataset. Figure 11 shows several detection cases.
                         Our algorithm offers superior quality heatmap prediction results.

                         Table 3. Grasp detection results of different algorithms on Jacquard dataset.

                                                                                                       Accuracy (%)
                          Method                                Input
                                                                                         Image-Wise                  Object-Wise
                          Morrison [5]                           D                             84                          -
                          Song [10]                            RGB-D                          93.2                         -
                          Kumra [8]                            RGB-D                          92.6                        87.7
                          Wang [6]                             RGB-D                          94.6                         -
                          Yu [9]                               RGB-D                          95.7                         -
                          Tian [11]                            RGB-D                           94                          -
                          Tian [12]                            RGB-D                          94.6                        92.8
                          Ours                                 RGB-D                          96.7                        94.6

                              The detection results presented in Table 3 and Figure 12 provide evidence that our
                         proposed method, which leverages cross-attention and channel interaction for RGB-D
                         feature fusion, can effectively utilize the information shared between the two modalities.
                                  Tian [11]                 RGB-D                      94                                 -
                                  Tian [12]                 RGB-D                     94.6                               92.8
                                  Ours                      RGB-D                     96.7                               94.6

                                       The detection results presented in Table 3 and Figure 12 provide evidence that our
 Sensors 2023, 23, 3340
                                  proposed method, which leverages cross-attention and channel interaction for RGB-D15    of 19
                                                                                                                        fea-
                                  ture fusion, can effectively utilize the information shared between the two modalities.

                                                      RGB          Depth         Grasp         Quality           Angle          Width

                                      Kumra, 2020

                                      Wang, 2022

                                         Ours

                                      Kumra, 2020

                                      Wang, 2022

                                         Ours

Sensors 2023, 23, x FOR PEER REVIEW                                                                                               16 of 20
                                  Figure
                                  Figure 12.
                                         12. Experiment
                                             Experimentresults
                                                        resultsof
                                                                ofalgorithms
                                                                   algorithmsproposed
                                                                              proposedbybyKumra
                                                                                           Kumraetet
                                                                                                   al.al.
                                                                                                       [8][8]
                                                                                                            inin
                                                                                                               2020, Wang
                                                                                                                 2020,    et et
                                                                                                                       Wang  al.al.
                                                                                                                                 [6][6]
                                                                                                                                     in in
                                  2022 and our method on Jacquard   dataset.
                                  2022 and our method on Jacquard dataset.
                                 5.2.3.
                                  5.2.3.Ablation
                                         AblationExperiment
                                                   Experiment
                                      Since
                                        Since the cross-attentionmodule
                                            the cross-attention   moduleisisonly
                                                                             onlyinvolved
                                                                                   involvedininthe
                                                                                                 thefused
                                                                                                      fusedfeature
                                                                                                             featureencoding
                                                                                                                     encodingstage,
                                                                                                                               stage,
                                 we
                                  we simplified our pipeline (shown in Figure 1) to produce the architecturedepicted
                                     simplified  our pipeline  (shown in  Figure   1) to produce     the architecture   depictedinin
                                 Figure
                                  Figure13.
                                          13.

                                                                                  C

                                                                                              C

                                                                                  C

                                                    (a) Architecture without MIM units.
                                                                                                  Up-sample

                                                            +                     C

                                                                                              C

                                                                     ...          C

                                                            +                     C

                                                    (b) Architecture without CIM units.
                                 Figure
                                  Figure13.13.
                                            Architectures in ablation
                                               Architectures          experiments:
                                                             in ablation           (a) has
                                                                         experiments:      no MIM
                                                                                       (a) has     blocks;
                                                                                               no MIM      and (b)
                                                                                                       blocks; andhas
                                                                                                                   (b)no CIM
                                                                                                                       has no blocks.
                                                                                                                              CIM blocks.

                                       InInthe
                                            theablation
                                                ablationexperiment,
                                                         experiment,weweevaluated
                                                                         evaluatedthetheobject-wise
                                                                                         object-wisegrasp
                                                                                                     graspdetection
                                                                                                             detectionaccuracy
                                                                                                                        accuracyon
                                                                                                                                 on
                                   boththe
                                 both    theCornell
                                             Cornelland
                                                      andJacquard
                                                           Jacquarddatasets.
                                                                    datasets.The
                                                                              Thecorresponding
                                                                                  correspondingstatistical
                                                                                                  statisticalresults
                                                                                                              resultsare
                                                                                                                      arepresented
                                                                                                                          presented
                                 ininTable
                                      Table4.4.

                                 Table 4. Object-wise grasp detection results of ablation experiment on Cornell and Jacquard da-
                                 tasets.

                                                                       Accuracy of                                Accuracy of
                                 Methods
                                                                    Cornell Dataset (%)                       Jacquard Dataset (%)
Sensors 2023, 23, 3340                                                                                                                     16 of 19

                                Table 4. Object-wise grasp detection results of ablation experiment on Cornell and Jacquard datasets.

                                                                                Accuracy of                            Accuracy of
                                 Methods
                                                                             Cornell Dataset (%)                   Jacquard Dataset (%)
                                 Without MIM                                           89.7                                  84.6
                                 Without CIM                                           96.4                                  92.6
                                 With MIM and CIM                                      97.8                                  94.6

                                      To validate the effectiveness of the different modules in the proposed approach, we
                                conducted several leave-one-out experiments on the Cornell and Jacquard datasets. Initially,
                                we removed the MIM and CIM modules from the proposed architecture. The generated
                                approaches are served as baseline approaches, shown in Figure 13a,b.
                                      The results of the ablation experiment demonstrate that the bilateral modality interaction
                                method based on cross-attention significantly enhances the accuracy of grasp detection.
                                Additionally, the feature aggregation method based on channel interaction strategy has a
                                fine-tuning effect on detection accuracy.

                                5.2.4. Physical Experiment
                                        The physical experiment was conducted on our in-house robotic platform, which
                                   comprises an Elite EC-66 robot with public open ROS interfaces, a parallel gripper, an
                                   Orbbec Femo-W RGB-D camera, and a computer server running Ubuntu. The experiment
Sensors 2023, 23, x FOR PEER REVIEW                                                                                   17 of 20
                                   involved 30 different unknown objects in the scene, with the camera positioned relative
                                   to the desktop similar to that in the Cornell dataset. RGB-D image data was captured by
                                   the camera, and the server detected the position and pose of potential grasps. Following a
                                  coordinate
                                   coordinatetransformation,
                                               transformation,the
                                                                therobot
                                                                    robotexecuted
                                                                          executedthe
                                                                                   thegrasping
                                                                                       graspingoperation
                                                                                                operationon
                                                                                                          onthe
                                                                                                             thetarget
                                                                                                                 targetobject.
                                                                                                                        object.
                                  The
                                   Thedetailed
                                        detailedgrasp
                                                 graspprocess
                                                       processisisdepicted
                                                                  depictedin
                                                                           inFigure
                                                                              Figure14.
                                                                                     14.

                                                       (a)                                                 (b)

                                                       (c)                                                 (d)
                               Figure
                                Figure14.14.Four
                                             Fourgrasp
                                                     graspstages
                                                             stages in
                                                                    in the physical experiment:
                                                                                     experiment: (a)
                                                                                                   (a) shows
                                                                                                        showsthetheinitial
                                                                                                                    initialposition
                                                                                                                            positionand
                                                                                                                                     andposture
                                                                                                                                          postureof
                               ofEC-66
                                   EC-66   robot.
                                        robot.  In Inthisthis stage,
                                                          stage, graspgrasp  detection
                                                                         detection      is performed.
                                                                                   is performed.   AfterAfter    detection,
                                                                                                          detection,         the parallel
                                                                                                                       the parallel       gripper
                                                                                                                                    gripper  moves
                               moves   to the  effective    grasping  position, which  can  be seen in  (b). The  gripper  then grasps
                                to the effective grasping position, which can be seen in (b). The gripper then grasps the target, which the target,
                               which  is shown
                                is shown    in (c). in (c).robot
                                                     The     The robot  completes
                                                                 completes         the target
                                                                             the target        grasping
                                                                                        grasping  task intask
                                                                                                            (d) in (d) finally.
                                                                                                                finally.

                                    During the experiment, we made a total of 200 attempts to grasp the target objects
                               and successfully grasped the objects in 189 of those attempts, resulting in an average suc-
                               cess rate of 94.5%. Figure 15 illustrates several examples of our grasp detection results.

                                     RGB              Depth              Grasps            Quality               Angle           Width
                                                        (c)                                               (d)
                                 Figure 14. Four grasp stages in the physical experiment: (a) shows the initial position and posture
                                 of EC-66 robot. In this stage, grasp detection is performed. After detection, the parallel gripper
 Sensors 2023, 23, 3340                                                                                                           17 of 19
                                 moves to the effective grasping position, which can be seen in (b). The gripper then grasps the target,
                                 which is shown in (c). The robot completes the target grasping task in (d) finally.

                                      During
                                       Duringthethe experiment,  we made
                                                    experiment, we   madeaatotal
                                                                               totalofof200
                                                                                         200attempts
                                                                                              attemptsto to grasp
                                                                                                          grasp thethe target
                                                                                                                    target    objects
                                                                                                                           objects and
                                 and  successfully  grasped  the objects  in 189 of those   attempts,  resulting  in an average
                                  successfully grasped the objects in 189 of those attempts, resulting in an average success     suc-
                                 cess
                                  raterate of 94.5%.
                                       of 94.5%.      Figure
                                                  Figure     15 illustrates
                                                         15 illustrates      several
                                                                        several       examples
                                                                                 examples         of our
                                                                                             of our  graspgrasp detection
                                                                                                            detection      results.
                                                                                                                       results.

                                       RGB              Depth            Grasps            Quality              Angle           Width

Sensors 2023, 23, x FOR PEER REVIEW                                                                                                   18 of 20

                                 Figure
                                  Figure15.
                                         15.Detection
                                             Detectionresults
                                                       resultsofofthe
                                                                   thephysical
                                                                       physicalexperiment.
                                                                                experiment.

                                 6.6.Conclusions
                                      Conclusions
                                         Thispaper
                                       This    paperaddressed
                                                       addressedthe  the2-DoF
                                                                          2-DoFrobot
                                                                                 robotgrasp
                                                                                          graspdetection
                                                                                                  detectionproblem
                                                                                                              problemby  byanalyzing
                                                                                                                             analyzingdata data
                                   fusion  issues  that  affect  grasp  detection   results.   Our   analysis  showed    that
                                 fusion issues that affect grasp detection results. Our analysis showed that fully utilizing   fully utilizing
                                   usefulinformation
                                 useful    information from
                                                          from each
                                                                 each modality
                                                                       modality and
                                                                                  andeliminating
                                                                                         eliminatinguseless
                                                                                                         uselessinformation
                                                                                                                  informationis isessential
                                                                                                                                    essential for
                                   achieving   high   accuracy    in grasp   detection.   In  response,    we  proposed
                                 for achieving high accuracy in grasp detection. In response, we proposed a cross-modality a cross-modality
                                   fusionmethod
                                 fusion    methodfor for2-DoF
                                                         2-DoFrobot
                                                                  robotgrasp
                                                                          graspdetection
                                                                                detectionthatthatused
                                                                                                   usedaaconvolutional
                                                                                                           convolutionalneural
                                                                                                                             neuralnetwork
                                                                                                                                      network
                                   andtransformer
                                 and    transformerstructure.
                                                        structure. ThisThis  method
                                                                         method        incorporated
                                                                                   incorporated      modalmodal   interaction
                                                                                                             interaction   and and    channel
                                                                                                                                 channel    in-
                                   interaction   strategies   to  adaptively   retain   essential   information     and
                                 teraction strategies to adaptively retain essential information and reduce the impact ofreduce    the impact
                                   of invalid
                                 invalid       information.
                                          information.           To validate
                                                           To validate         our approach,
                                                                          our approach,           we conducted
                                                                                            we conducted            a series
                                                                                                               a series       of comparison
                                                                                                                        of comparison      ex-
                                   experiments     with  other   methods    and  an  ablation    experiment.     Our
                                 periments with other methods and an ablation experiment. Our experimental results    experimental      results
                                   demonstratedthat
                                 demonstrated       thatthethe proposed
                                                             proposed       cross-modality
                                                                         cross-modality         fusion
                                                                                            fusion       method
                                                                                                     method        achieves
                                                                                                               achieves  highhigh    accuracy
                                                                                                                                accuracy   for
                                   for both   image-wise     and   object-wise   grasp    detection   and   is effective
                                 both image-wise and object-wise grasp detection and is effective in practical robot graspin practical    robot
                                   grasp detection
                                 detection            scenarios.
                                             scenarios.   However, However,    this method
                                                                       this method             is somewhat
                                                                                      is somewhat              time-consuming,
                                                                                                       time-consuming,     which which       is a
                                                                                                                                    is a limi-
                                   limitation
                                 tation        thatwill
                                         that we    weaddress
                                                         will address    in future
                                                                   in future  work.work.
                                         Our proposed algorithm has demonstrated applicability to the task of detecting targets
                                       Our proposed algorithm has demonstrated applicability to the task of detecting tar-
                                   for robotic grasping in vision-based scenarios. In addition, we anticipate that our work will
                                 gets for robotic grasping in vision-based scenarios. In addition, we anticipate that our
                                  yield valuable insights into RGB-D fusion, with potential applications in image semantic
                                 work will yield valuable insights into RGB-D fusion, with potential applications in image
                                   segmentation, target detection, and pose estimation.
                                 semantic segmentation, target detection, and pose estimation.
                                   Author Contributions: Conceptualization, Q.Z.; methodology, Q.Z. and X.S.; software, Q.Z. and X.S.;
                                 Author Contributions: Conceptualization, Q.Z.; methodology, Q.Z. and X.S.; software, Q.Z. and
                                   writing—original draft preparation, Q.Z.; writing—review and editing, X.S. All authors have read
                                 X.S.; writing—original draft preparation, Q.Z.; writing—review and editing, X.S. All authors have
                                   and agreed to the published version of the manuscript.
                                 read and agreed to the published version of the manuscript.
                                   Funding: This research was funded by the National Natural Science Foundation of China (grant
                                 Funding: This research was funded by the National Natural Science Foundation of China (grant
                                   number 61903162) and Jiangsu Province’s “Double Innovation Plan”: Research and development of
                                 number 61903162) and Jiangsu Province’s “Double Innovation Plan”: Research and development of
                                   flexible cooperative robot technology for intelligent manufacturing.
                                 flexible cooperative robot technology for intelligent manufacturing.
                                   Institutional Review Board Statement: Not applicable.
                                 Institutional Review Board Statement: Not applicable.
                                 Informed Consent Statement: Not applicable.
                                 Data Availability Statement: Cornell, Jacquard and multi-object multi-grasp RGB-D dataset exper-
                                 iment results are available on https://github.com/QZhSSLab/CrossModalityFusion4RobotGrasp,
Sensors 2023, 23, 3340                                                                                                            18 of 19

                                  Informed Consent Statement: Not applicable.
                                  Data Availability Statement: Cornell, Jacquard and multi-object multi-grasp RGB-D dataset experi-
                                  ment results are available on https://github.com/QZhSSLab/CrossModalityFusion4RobotGrasp, since
                                  9 February 2022. The code presented in this study is available on request from the corresponding author.
                                  Acknowledgments: The authors are very grateful for the suggestions from Mingmin Liu (lium-
                                  ingmin@siasun.com) and Zhiwei Fan (fanzhiwei@sia.cn) in the writing of this paper.
                                  Conflicts of Interest: The authors declare no conflict of interest.

References
1.    Lenz, I.; Lee, H.; Saxena, A. Deep Learning for Detecting Robotic Grasps. Int. J. Robot. Res. 2015, 34, 705–724. [CrossRef]
2.    Zhang, Q.; Qu, D.; Xu, F.; Zou, F. Robust Robot Grasp Detection in Multimodal Fusion. MATEC Web Conf. 2017, 139, 00060.
      [CrossRef]
3.    Cao, H.; Chen, G.; Li, Z.; Feng, Q.; Lin, J.; Knoll, A. Efficient Grasp Detection Network with Gaussian-Based Grasp Representation
      for Robotic Manipulation. IEEE ASME Trans. Mechatron. 2022, 1–11. [CrossRef]
4.    Morrison, D.; Corke, P.; Leitner, J. Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach. In
      Robotics; MIT Press: Cambridge, MA, USA, 2018.
5.    Morrison, D.; Corke, P.; Leitner, J. Learning Robust, Real-Time, Reactive Robotic Grasping. Int. J. Robot. Res. 2019, 39,
      027836491985906. [CrossRef]
6.    Wang, S.; Zhou, Z.; Kan, Z. When Transformer Meets Robotic Grasping: Exploits Context for Efficient Grasp Detection. IEEE
      Robot. Autom. Lett. 2022, 7, 8170–8177. [CrossRef]
7.    Chu, F.-J.; Xu, R.; Vela, P.A. Real-World Multiobject, Multigrasp Detection. IEEE Robot. Autom. Lett. 2018, 3, 3355–3362. [CrossRef]
8.    Kumra, S.; Joshi, S.; Sahin, F. Antipodal Robotic Grasping Using Generative Residual Convolutional Neural Network. In
      Proceedings of the 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Las Vegas, NV, USA,
      24 October 2020; pp. 9626–9633.
9.    Yu, S.; Zhai, D.-H.; Xia, Y.; Wu, H.; Liao, J. SE-ResUNet: A Novel Robotic Grasp Detection Method. IEEE Robot. Autom. Lett. 2022,
      7, 5238–5245. [CrossRef]
10.   Song, Y.; Wen, J.; Liu, D.; Yu, C. Deep Robotic Grasping Prediction with Hierarchical RGB-D Fusion. Int. J. Control Autom. Syst.
      2022, 20, 243–254. [CrossRef]
11.   Tian, H.; Song, K.; Li, S.; Ma, S.; Yan, Y. Lightweight Pixel-Wise Generative Robot Grasping Detection Based on RGB-D Dense
      Fusion. IEEE Trans. Instrum. Meas. 2022, 71, 1–12. [CrossRef]
12.   Tian, H.; Song, K.; Li, S.; Ma, S.; Yan, Y. Rotation Adaptive Grasping Estimation Network Oriented to Unknown Objects Based on
      Novel RGB-D Fusion Strategy. Eng. Appl. Artif. Intell. 2023, 120, 105842. [CrossRef]
13.   Saxena, A.; Driemeyer, J.; Kearns, J.; Ng, A. Robotic Grasping of Novel Objects. In Advances in Neural Information Processing
      Systems; MIT Press: Cambridge, MA, USA, 2006; Volume 19.
14.   Le, Q.V.; Kamm, D.; Kara, A.F.; Ng, A.Y. Learning to Grasp Objects with Multiple Contact Points. In Proceedings of the 2010 IEEE
      International Conference on Robotics and Automation, Anchorage, AK, USA, 8 May 2010; pp. 5062–5069.
15.   Liang, H.; Ma, X.; Li, S.; Gorner, M.; Tang, S.; Fang, B.; Sun, F.; Zhang, J. PointNetGPD: Detecting Grasp Configurations from
      Point Sets. In Proceedings of the 2019 International Conference on Robotics and Automation (ICRA), Montreal, QC, Canada,
      24 May 2019; pp. 3629–3635.
16.   Gou, M.; Fang, H.-S.; Zhu, Z.; Xu, S.; Wang, C.; Lu, C. RGB Matters: Learning 7-DoF Grasp Poses on Monocular RGBD Images.
      In Proceedings of the 2021 IEEE International Conference on Robotics and Automation (ICRA), Xi’an, China, 30 May 2021;
      pp. 13459–13466.
17.   Sundermeyer, M.; Mousavian, A.; Triebel, R.; Fox, D. Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes.
      In Proceedings of the 2021 IEEE International Conference on Robotics and Automation (ICRA), Xi’an, China, 30 May 2021;
      pp. 13438–13444.
18.   Jiang, Y.; Moseson, S.; Saxena, A. Efficient Grasping from RGBD Images: Learning Using a New Rectangle Representation.
      In Proceedings of the 2011 IEEE International Conference on Robotics and Automation, Shanghai, China, 9–13 May 2011;
      pp. 3304–3311.
19.   Shi, C.; Miao, C.; Zhong, X.; Zhong, X.; Hu, H.; Liu, Q. Pixel-Reasoning-Based Robotics Fine Grasping for Novel Objects with
      Deep EDINet Structure. Sensors 2022, 22, 4283. [CrossRef]
20.   Kumra, S.; Joshi, S.; Sahin, F. GR-ConvNet v2: A Real-Time Multi-Grasp Detection Network for Robotic Grasping. Sensors 2022,
      22, 6208. [CrossRef]
21.   Li, Z.; Liu, F.; Yang, W.; Peng, S.; Zhou, J. A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects.
      IEEE Trans. Neural Netw. Learn. Syst. 2021, 33, 6999–7019. [CrossRef]
22.   Caldera, S.; Rassau, A.; Chai, D. Review of Deep Learning Methods in Robotic Grasp Detection. Multimodal Technol. Interact. 2018,
      2, 57. [CrossRef]
Sensors 2023, 23, 3340                                                                                                               19 of 19

23.   Kumra, S.; Kanan, C. Robotic Grasp Detection Using Deep Convolutional Neural Networks. In Proceedings of the 2017 IEEE/RSJ
      international conference on intelligent robots and systems (IROS), Vancouver, BC, Canada, 24–28 September 2017; pp. 769–776.
      [CrossRef]
24.   Wei, J.; Liu, H.; Yan, G.; Sun, F. Robotic Grasping Recognition Using Multi-Modal Deep Extreme Learning Machine. Multidimens.
      Syst. Signal Process. 2017, 28, 817–833. [CrossRef]
25.   Trottier, L.; Giguère, P.; Chaib-draa, B. Dictionary Learning for Robotic Grasp Recognition and Detection. arXiv 1606, arXiv:160600538.
      [CrossRef]
26.   Wang, Z.; Li, Z.; Wang, B.; Liu, H. Robot Grasp Detection Using Multimodal Deep Convolutional Neural Networks. Adv. Mech.
      Eng. 2016, 8, 1687814016668077. [CrossRef]
27.   Redmon, J.; Angelova, A. Real-Time Grasp Detection Using Convolutional Neural Networks. In Proceedings of the 2015 IEEE
      International Conference on Robotics and Automation (ICRA), Seattle, Washington, USA, 26–30 May 2015; pp. 1316–1322.
28.   Ainetter, S.; Fraundorfer, F. End-to-End Trainable Deep Neural Network for Robotic Grasp Detection and Semantic Segmentation from
      Rgb. In Proceedings of the 2021 IEEE International Conference on Robotics and Automation (ICRA), Xi’an, China, 30 May–5 June 2021;
      pp. 13452–13458.
29.   Redmon, J.; Divvala, S.; Girshick, R.; Farhadi, A. You Only Look Once: Unified, Real-Time Object Detection. In Proceedings of the
      IEEE Conference on Computer Vision and Pattern Recognition, Las Vegas, NV, USA, 27–30 June 2016; pp. 779–788.
30.   Ronneberger, O.; Fischer, P.; Brox, T. U-Net: Convolutional Networks for Biomedical Image Segmentation. In Proceedings of the
      Medical Image Computing and Computer-Assisted Intervention—MICCAI 2015; Navab, N., Hornegger, J., Wells, W.M., Frangi, A.F.,
      Eds.; Springer International Publishing: Cham, Switzerland, 2015; pp. 234–241.
31.   Song, K.; Wang, J.; Bao, Y.; Huang, L.; Yan, Y. A Novel Visible-Depth-Thermal Image Dataset of Salient Object Detection for
      Robotic Visual Perception. IEEEASME Trans. Mechatron. 2022, 1–12. [CrossRef]
32.   Guo, J.; Han, K.; Wu, H.; Tang, Y.; Chen, X.; Wang, Y.; Xu, C. CMT: Convolutional Neural Networks Meet Vision Transformers. In
      Proceedings of the 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), New Orleans, LA, USA,
      18–24 June 2022; pp. 12165–12175.
33.   Xiao, T.; Singh, M.; Mintun, E.; Darrell, T.; Dollár, P.; Girshick, R. Early Convolutions Help Transformers See Better. In Proceedings
      of the Advances in Neural Information Processing Systems, Virtual, 6–14 December 2021; Volume 34.
34.   He, T.; Zhang, Z.; Zhang, H.; Zhang, Z.; Xie, J.; Li, M. Bag of Tricks for Image Classification with Convolutional Neural Networks.
      In Proceedings of the 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Long Beach, CA, USA,
      15–20 June 2019; pp. 558–567.
35.   Hendrycks, D.; Gimpel, K. Gaussian Error Linear Units (Gelus). arXiv 1606, arXiv:160608415. [CrossRef]
36.   Ioffe, S.; Szegedy, C. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. In
      Proceedings of the International Conference on Machine Learning, Lille, France, 7–9 July 2015; pp. 448–456.
37.   Dosovitskiy, A.; Beyer, L.; Kolesnikov, A.; Weissenborn, D.; Zhai, X.; Unterthiner, T.; Dehghani, M.; Minderer, M.; Heigold, G.;
      Gelly, S.; et al. An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale. arXiv 2010, arXiv:201011929.
      [CrossRef]
38.   Aladago, M.M.; Piergiovanni, A.J. Compound Tokens: Channel Fusion for Vision-Language Representation Learning. arXiv 2022,
      arXiv:221201447. [CrossRef]
39.   Zhang, Y.; Choi, S.; Hong, S. Spatio-Channel Attention Blocks for Cross-Modal Crowd Counting. In Proceedings of the Asian
      Conference on Computer Vision, Macau, China, 4–8 December 2022; pp. 90–107.
40.   Hu, J.; Shen, L.; Sun, G. Squeeze-and-Excitation Networks. In Proceedings of the IEEE Conference on Computer Vision and
      Pattern Recognition, Salt Lake City, UT, USA, 18–23 June 2018; pp. 7132–7141.
41.   Ren, S.; He, K.; Girshick, R.; Sun, J. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. In
      Proceedings of the Advances in Neural Information Processing Systems, Montreal, QC, Canada, 7–12 December 2015; Volume 28.
42.   Depierre, A.; Dellandréa, E.; Chen, L. Jacquard: A Large Scale Dataset for Robotic Grasp Detection. In Proceedings of the 2018
      IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, Spain, 1–5 October 2018; pp. 3511–3516.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
