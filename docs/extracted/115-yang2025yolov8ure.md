---
source_id: 115
bibtex_key: yang2025yolov8ure
title: Research on a Fusion Technique of YOLOv8-URE-Based 2D Vision and Point Cloud for Robotic Grasping in Stacked Scenarios
year: 2025
domain_theme: YOLO plus RGB-D
verified_pdf: 115_YOLOv8-URE_2D_Point_Cloud_Grasping.pdf
char_count: 90687
---

Article

Research on a Fusion Technique of YOLOv8-URE-Based
2D Vision and Point Cloud for Robotic Grasping in
Stacked Scenarios
Xuhui Ye 1,2, Xiaoyang Qin 1,2, Leming Zhan 1,2, Jun Wang 1,2 and Yan Chen 3,*

                                          1 School of Mechanical Engineering, Hubei University of Technology, Wuhan 430068, China;
                                            yxh89@hbut.edu.cn (X.Y.); q118625@163.com (X.Q.); 102210114@hbut.edu.cn (L.Z.);
                                            17839792675@163.com (J.W.)
                                          2 Hubei Key Laboratory of Modern Manufacturing Quality Engineering, Wuhan 430068, China

                                          3 School of Mechanical and Electrical Engineering, Wuhan Donghu University, Wuhan 430212, China

                                          * Correspondence: qxy2001625@163.com

                                          Abstract: In industrial robotic grasping tasks, traditional 3D point cloud registration and
                                          pose estimation methods often struggle with low eﬃciency and limited accuracy in
                                          stacked and cluttered environments. To address these challenges, this paper proposes a
                                          grasp pose estimation algorithm that integrates 2D object detection based on YOLOv8-
                                          URE with 3D point cloud registration. In the detection stage, the method enhances object
                                          feature perception and localization by optimizing the receptive field structure and intro-
                                          ducing attention mechanisms. It also employs an eﬃcient multi-scale feature fusion strat-
                                          egy to improve bounding box regression accuracy. During point cloud processing, target
                                          centers predicted by the detector guide rapid segmentation, followed by robust registra-
                                          tion techniques to estimate precise object poses. Experimental results demonstrate that
                                          YOLOv8-URE improves detection accuracy by 9.21% compared to YOLOv8n, reduces
                                          registration time by 60.5%, and significantly increases grasp success rates, proving its re-
                                          liability and eﬀectiveness in industrial scenarios.

                                          Keywords: industrial robotic grasping; YOLOv8-URE; 2D visual detection; information
                                          fusion; stacked-scene grasping
Received: 14 April 2025
Revised: 1 June 2025
Accepted: 10 June 2025
Published: 11 June 2025
                                          1. Introduction
Citation: Ye, X.; Qin, X.; Zhan, L.;
Wang, J.; Chen, Y. Research on a                With the continuous advancement of automation technology, vision-based robots
Fusion Technique of YOLOv8-               have been increasingly applied in various domains such as industrial manufacturing [1],
URE-Based 2D Vision and Point             logistics and packaging [2], and intelligent agricultural harvesting [3]. Among these ap-
Cloud for Robotic Grasping in
                                          plications, object grasping and sorting are critical steps, as their eﬃciency and accuracy
Stacked Scenarios. Appl. Sci. 2025, 15,
                                          directly impact the overall productivity and quality of the workflow.
6583. https://doi.org/10.3390/
app15126583                                     Numerous studies have focused on enhancing the grasping capabilities of vision-
                                          based robots, yielding a range of significant advancements. For example, Lu Zhiliang et
Copyright: © 2025 by the authors.
                                          al. proposed an operational relationship reasoning algorithm based on the VLMRN neural
Licensee MDPI, Basel, Switzerland.
This article is an open access article    network model [4] and a real-time grasp region detection algorithm using the SE-
distributed under the terms and con-      RetinaGrasp network. They developed a grasping method specifically designed for
ditions of the Creative Commons At-       stacked object scenarios by integrating the two approaches. However, the grasping suc-
tribution (CC BY) license (https://cre-   cess rate and target recognition accuracy of this method in complex stacking scenarios still
ativecommons.org/licenses/by/4.0/).
                                          need to be improved. Li Xiuzhi et al. proposed an optimal grasping posture detection

Appl. Sci. 2025, 15, 6583                                                                                      https://doi.org/10.3390/app15126583
Appl. Sci. 2025, 15, 6583                                                                                          2 of 22

                            algorithm based on a dual-network architecture [5], which improves the detection speed
                            and enhances the recognition performance for small target objects by modifying the
                            YOLOv3 detection model. However, the algorithm relies on two deep learning networks,
                            resulting in a more complex structure and higher computational costs, making it diﬃcult
                            to meet real-time application requirements. Guo et al. proposed a grasping detection
                            method tailored for various fruit stacking scenarios [6], which can determine the grasping
                            parameters of the currently targeted object. However, it cannot perceive global scene in-
                            formation and grasp specific types of objects. Moreover, the relatively small size of the
                            dataset limits its generalizability to broader applications. Geng et al. combined the object
                            detection algorithm (YOLOv5) with the fully convolutional grasp detection network
                            (GDFCN) to propose a real-time grasp detection algorithm for robotic arms to handle un-
                            familiar objects [7]. This method eﬀectively achieves object classification under real-time
                            constraints and improves the stability and accuracy of grasp detection. Nevertheless, its
                            performance under complex stacked scenes still has room for improvement.
                                  Another line of research focuses on end-to-end object pose estimation methods that
                            learn to directly map input data to pose parameters, thereby eliminating the need for man-
                            ually designed features and complex multi-stage processing. Xiaoxin Zhao [8], Yajun
                            Zhang [9], Guan Qi [10], and Gu Wang [11] investigated the use of convolutional neural
                            networks (CNNs) to directly regress object poses from RGB images. By leveraging end-
                            to-end training on large-scale datasets, these networks can automatically learn the mapping
                            between image features and object pose. Such methods simplify the pose estimation pipe-
                            line and demonstrate strong performance under ideal conditions. However, end-to-end ap-
                            proaches still face several challenges, including a high dependency on the quality and di-
                            versity of training data, limited generalization ability in complex or cluttered environments,
                            and suboptimal pose estimation accuracy. Additionally, the black-box nature of these mod-
                            els makes it difficult to interpret and optimize their internal decision-making processes.
                                  In summary, existing algorithms often struggle to meet real-time requirements while
                            maintaining high detection accuracy. These limitations become even more pronounced in
                            complex stacked scenes, where increased algorithmic complexity and restricted computa-
                            tional resources hinder performance. Furthermore, current methods frequently suﬀer
                            from low grasp-success rates and inaccurate target recognition in such environments. To
                            address the inability of current robotic grasping algorithms to balance detection accuracy
                            and real-time performance, this paper proposes a novel approach that integrates deep
                            learning-based object detection with 3D point cloud processing. In the detection stage, the
                            accuracy and real-time performance of the object detector are enhanced through improve-
                            ments in the deep learning network architecture while also extracting the target’s center
                            coordinates. In the point cloud processing stage, 3D coordinate transformation and KD-
                            Tree search are employed to rapidly isolate the target point cloud. Subsequently, point
                            cloud alignment is refined using the sample consensus and normal distributions trans-
                            form (NDT) algorithms, thereby improving both registration accuracy and computational
                            eﬃciency. This integrated method oﬀers a real-time and accurate solution for object recog-
                            nition and grasping in vision-guided robotic systems.

                            2. Methodology
                                  Upon initialization, the depth camera module captures both RGB images and 3D
                            point cloud data, which are then forwarded to the deep learning and point cloud pro-
                            cessing modules, respectively.
                                  As shown in Figure 1, in the deep learning module, the input RGB image is passed
                            through the enhanced YOLOv8n network for object detection, whereby the object is iden-
                            tified and classified into four pose-based categories. During this process, a bounding box
                            is generated around the object, and the coordinates of the bounding box center are
Appl. Sci. 2025, 15, 6583                                                                                        3 of 22

                            extracted. These coordinates are then normalized and converted into 3D coordinates, in-
                            cluding horizontal and vertical positions along with the corresponding depth value. The
                            resulting 3D coordinates are subsequently passed to the point cloud processing module
                            for further analysis.
                                 In the point cloud processing module, the point cloud data captured by the depth
                            camera are first preprocessed, including voxel grid downsampling to reduce point cloud
                            density and background point removal through segmentation. Then, based on the 3D co-
                            ordinates obtained from the deep learning module, a KD-Tree is used to eﬃciently locate
                            and extract the target point cloud. Next, the target point cloud is aligned with a template
                            point cloud selected based on the preliminary pose classification result, yielding a homo-
                            geneous transformation matrix. This matrix is applied to the corresponding ideal grasp
                            pose of the template point cloud, resulting in the final grasp pose for the target object in
                            the camera coordinate system.
                                 In the grasp control module, the transformation matrix obtained from hand–eye cal-
                            ibration is used to perform coordinate transformation on the grasp pose, resulting in the
                            final grasp pose. Then, inverse kinematics is applied to calculate the corresponding joint
                            angles, which are sent to the robot controller to execute the target grasp.

                            Figure 1. Overall system framework of object detection and grasping.

                            2.1. YOLOv8-URE
                            2.1.1. Overview
                                 YOLOv8 is a relatively novel one-stage target detection algorithm in the YOLO series,
                            and has faster speed, accuracy, and performance compared with other mainstream target
                            detection algorithms. As a state-of-the-art (SOTA) model, YOLOv8 is released in five ver-
                            sions—YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l, and YOLOv8x—with the number of
                            parameters and floating-point operations (FLOPs) increasing progressively across the ver-
                            sions. Considering the requirements of real-time performance, computational eﬃciency,
                            and detection accuracy in industrial environments, we selected YOLOv8n as the baseline
                            model for our application. As illustrated in Figure 2, the YOLOv8-URE algorithm, mainly
                            comprises two key components: the backbone module (Figure 2a), responsible for extract-
                            ing feature information, and the neck module (Figure 2b), which further enhances the fea-
                            ture maps by introducing multi-scale feature fusion, thereby improving the model’s ca-
                            pability to perceive and localize targets accurately.
Appl. Sci. 2025, 15, 6583                                                                                         4 of 22

                            Figure 2. Structure of the YOLOv8-URE network: (a) backbone module; (b) neck module; (c) head
                            module; (d) SPPF module; (e) detection layer.

                                  In the backbone module, to enhance the feature extraction capability for stacked ob-
                            jects, the feature extraction network incorporates C2f_UniRepLKNetBlock. This structure
                            employs a small number of large convolutional kernels to ensure a broad and eﬀective
                            receptive field while leveraging small kernels to eﬃciently capture more complex spatial
                            patterns. Additionally, multiple lightweight blocks are used to increase network depth,
                            thereby further enhancing its representational capacity. Eﬃcient local attention (ELA) [12]
                            is introduced as an attention mechanism that addresses the limitations of traditional co-
                            ordinate attention methods. Specifically, it highlights the poor generalization capability
                            caused by batch normalization, the adverse eﬀects of dimensionality reduction on channel
                            attention, and the high computational complexity of conventional attention generation.
                            By combining 1D convolution with group normalization-based feature enhancement,
                            ELA eﬃciently encodes two 1D positional feature maps without dimensionality reduc-
                            tion. This enables precise localization of regions of interest while maintaining a light-
                            weight architecture.
                                  In the neck module, to enhance the feature fusion capability for stacked objects, this
                            paper redesigns the neck by integrating CSPStage and DySample mechanisms into a
                            newly designed CSPStage-Dy module. CSPStage employs diﬀerent channel numbers for
                            features at varying scales, allowing flexible control over the representation capacity of
                            both high-level and low-level features under lightweight computational constraints. Ad-
                            ditionally, the redundant upsampling operations in the original queen-fusion structure
                            are removed, which significantly reduces inference latency while maintaining only a
Appl. Sci. 2025, 15, 6583                                                                                               5 of 22

                            minimal drop in accuracy. Furthermore, the original convolution-based fusion method is
                            optimized using CSPNet connections, and the concepts of re-parameterization and the
                            ELAN structure are introduced to further enhance accuracy without significantly increas-
                            ing the computational load. Moreover, DySample learns pixel-wise weights, enabling the
                            network to adopt adaptive sampling strategies across diﬀerent regions, especially around
                            object boundaries, thus improving edge clarity and detection precision.
                                 Finally, Shape-IoU [13] is used to replace the original CIoU loss function to accelerate
                            model convergence and improve regression speed.

                            2.1.2. Backbone Module
                                  UniRepLKNet (unified re-parameterized large-kernel network), proposed by Xiao-
                            han Ding et al. [14], is a universal perception large-kernel convolutional neural network.
                            Compared to simply increasing the model depth, large convolutional kernels can more
                            eﬃciently expand the eﬀective receptive field, enabling the network to capture broader
                            contextual information and extract more complex features. To balance both local and
                            global feature extraction, this module combines large-kernel convolutions with small-ker-
                            nel convolutions: the small kernels help capture local patterns and improve training sta-
                            bility, while the large kernels are more eﬀective at modeling long-range dependencies
                            [15]. The outputs of these two convolutions are then added after each passes through its
                            own batch normalization (BN) layer [16]. During inference, structural re-parameterization
                            [17] is applied to merge the BN layers and small-kernel convolutions equivalently into the
                            large-kernel convolution. This approach maintains the functionality of the small-kernel
                            convolutions while optimizing inference eﬃciency and reducing computational cost. As
                            a result, the large kernels are better able to capture sparse patterns, allowing a pixel in the
                            feature map to be more strongly related to distant pixels than to its immediate neighbors,
                            thereby generating higher-quality feature representations.
                                  The model architecture is shown in Figure 3. The DW Conv module incorporates
                            both large-kernel and parallel dilated convolutions. Through structural re-parameteriza-
                            tion, the block is equivalently transformed into a single large-kernel convolution for eﬃ-
                            cient inference.

                            Figure 3. Architecture of UniRepLKNet: (a) overall structure of UniRepLKNet; (b) lark block module.

                                 This paper proposes C2f_UniRepLKNetBlock, which integrates the lark block con-
                            cept into the C2f structure, as shown in Figure 4. The core idea of the C2f structure lies in
                            progressive cross-layer fusion combined with a partial gradient transmission mechanism,
                            which eﬀectively enhances gradient flow and optimizes feature representation. This
Appl. Sci. 2025, 15, 6583                                                                                          6 of 22

                            design enables the model to achieve more eﬃcient gradient propagation and faster con-
                            vergence, all while maintaining a low parameter count. The SE block module within
                            UniRepLKNetBlock employs global average pooling and channel attention mechanisms
                            to dynamically adjust the importance of feature channels, thereby improving the model’s
                            focus on salient features. By combining C2f with UniRepLKNetBlock, the network not
                            only retains its lightweight and eﬃcient training advantages but also significantly
                            strengthens its multi-scale perception and representation capabilities.
                                 Specifically, the C2f_UniRepLKNetBlock module leverages large-kernel convolu-
                            tions to expand the global receptive field, facilitating a comprehensive understanding of
                            the overall stacked structure in cluttered scenes. In addition, the use of parallel convolu-
                            tions with varying dilation rates enables the network to penetrate occlusions and better
                            capture object edge details. Furthermore, the structural re-parameterization design allows
                            the network to learn rich features through multi-branch structures during training, which
                            are then fused into a single branch during inference, ensuring high computational eﬃ-
                            ciency without sacrificing performance.

                            Figure 4. Architecture of C2f_UniRepLKNetBlock: (a) overall structure of C2f_UniRepLKNetBlock;
                            (b) UniRepLKNetBlock module.

                                 Subsequently, the ELA (eﬃcient local attention) mechanism was introduced. ELA
                            applies strip pooling along the spatial dimensions to extract horizontal and vertical fea-
                            ture vectors, maintaining elongated kernel shapes to eﬀectively capture long-range de-
                            pendencies while avoiding interference from irrelevant regions during label prediction.
                            The mechanism independently processes the directional feature vectors to generate atten-
                            tion weights, which are then fused through multiplicative operations, thereby enabling
                            precise localization of the region of interest (ROI). To observe the improvement in recog-
                            nition ability of the model feature fusion network more intuitively, HiResCAM [18] (high-
                            resolution class activation mapping) was used to draw heat maps, which can be more
                            intuitively observed to show the learning of the network for diﬀerent targets. As can be
                            seen in Figure 5b, without the introduction of attention, the network pays more attention
                            to the edge of the label, and some areas of attention are more dispersed, while in Figure
                            5c, after the introduction of the ELA mechanism, the model’s perception of the correct
                            target is strengthened and the attention to the target is concentrated rather than dispersed,
                            which makes the model focus on the target features more accurately.
Appl. Sci. 2025, 15, 6583                                                                                            7 of 22

                            Figure 5. Heatmap comparison: (a) input image; (b) attention heatmap of the model with ELA; (c)
                            attention heatmap of the model without ELA. Color legend: Red denotes high attention, yellow de-
                            notes medium attention, and blue denotes low attention.

                            2.1.3. Improved Neck Module
                                 To redesign the neck, this paper combines the CSPStage (cross stage partial stage)
                            from Eﬃcient RepGFPN [19] with DySample (Dynamic Sampling) [20], proposing the
                            CSPStage-Dy module.
                                 As illustrated in Figure 6b, in the CSPStage module, the fused image features are
                            divided into two branches, each containing a standard Conv-BN-Act structure. One
                            branch incorporates the BasicBlock_Reverse module composed of a 3 × 3 RepConv and
                            BatchNorm2d layers, which are stacked repeatedly to enhance feature representation.
                            When Shortcut = True, a residual connection is applied to alleviate gradient vanishing and
                            improve training stability; otherwise, with Shortcut = False, the module simplifies to a
                            pure convolutional block. Moreover, as illustrated in Figure 6c, a simplified RepConv de-
                            sign is adopted that retains the original mechanism: multi-branch structures are used dur-
                            ing training to extract features at multiple scales, while during inference, structural re-
                            parameterization merges these branches into a single convolution. At the same time, the
                            branches have been streamlined and lightweight activation functions along with opti-
                            mized normalization strategies have been introduced, making CSPStage better suited for
                            real-time detection tasks.

                            Figure 6. Architecture of RepGFPN: (a) overall structure of RepGFPN; (b) CSPStage module; (c)
                            simplified RepConv module.

                                  DySample is an ultralightweight dynamic upsampling module that primarily con-
                            sists of two key steps: feature resampling and dynamic sampling point generation. As
                            illustrated in Figure 7, DySample performs accurate upsampling through grid sampling
                            operations combined with dynamic weight control, enabling it to retain critical region in-
                            formation. Compared to traditional methods, it oﬀers higher boundary sampling
Appl. Sci. 2025, 15, 6583                                                                                                    8 of 22

                            precision, making it particularly suitable for addressing object boundary ambiguity in
                            stacked scenes. Its lightweight design significantly reduces computational overhead and
                            eliminates the need for additional sub-networks to generate dynamic convolution kernels.

                            Figure 7. Architecture of Dysample.

                                In summary, CSPStage enhances feature interaction and multi-scale representation,
                            while DySample improves upsampling quality with eﬃcient resource utilization. When
                            combined, these modules enable eﬃcient feature fusion within the feature pyramid at
                            lower latency, oﬀering strong support for real-time object detection tasks.

                            2.2. Point Cloud Preprocessing
                            2.2.1. Point Cloud Filtering
                                 The large number of point sets in the point cloud data leads to slow computation
                            while processing the point cloud. Therefore, filtering with downsampling is used first to
                            remove the redundant points during the computation process. Three-dimensional voxel
                            grid filtering is used to significantly reduce the number of data points by dividing the
                            point cloud into voxels and replacing multiple points with one representative point in
                            each voxel. Also, 3D voxel grid filtering can eﬀectively remove isolated noise points.
                            Through voxelization, the point cloud is resampled to a consistent spatial resolution,
                            which facilitates subsequent surface segmentation or surface reconstruction. The filtering
                            eﬀect is shown in Figure 8.

                            Figure 8. Comparison of point clouds before and after filtering: (a) original point cloud of the desk;
                            (b) filtered point cloud of the desk; (c) original point cloud of the workpiece; (d) filtered point cloud
                            of the workpiece.
Appl. Sci. 2025, 15, 6583                                                                                                9 of 22

                                   To verify the eﬀectiveness of the filtering process, a comparison of the number of
                              points and point cloud loading time was conducted. As shown in Table 1, while preserv-
                              ing the essential geometric features, the point cloud becomes sparser after filtering, result-
                              ing in a significant reduction in the total number of points and a noticeable improvement
                              in loading speed, which is beneficial for subsequent processing.

                              Table 1. Comparison of point cloud size and loading time before and after filtering.

                                     Comparison Parameter                 Desk Point Cloud         Workpiece Point Cloud
                                    Number of Original Points                 460,400                      7197
                                    Number of Filtered Points                  41,049                      2126
                               Original Point Cloud Load Time (s)            0.562537 s                 0.0231155
                               Filtered Point Cloud Load Time (s)             0.052796                  0.0105605

                                   To further evaluate the acceleration effect of voxel filtering in point cloud processing,
                              we measured the total processing time for ground segmentation and ICP registration under
                              two conditions: without filtering and with 3D voxel grid filtering. As shown in Table 2, alt-
                              hough the filtering step introduces a slight computational overhead, it significantly reduces
                              the time required for subsequent processing (segmentation + registration). This demon-
                              strates that voxel filtering eﬀectively improves the overall eﬃciency of the algorithm.

                              Table 2. Runtime comparison before and after voxel filtering.

        Method              Original Points          Points After Filtering          Filtering Time            Total Time
      No Filtering              626,910                        -                             -                  6152 ms
     After Filtering            626,910                     233,783                      1681 ms                3677 ms

                              2.2.2. Point Cloud Image Segmentation
                                   As shown in Figure 9a, a large number of points—including the ground and back-
                              ground—are captured by the depth camera during image acquisition. These irrelevant
                              points have little correlation with the target object and may interfere with the point cloud
                              registration process, negatively aﬀecting the accuracy of subsequent processing. To ad-
                              dress this issue, sample consensus segmentation (SAC) is employed to segment the target
                              point cloud from the background. As illustrated in Figure 9b, after segmentation, the clut-
                              tered background points in the original scene are successfully removed, leaving only the
                              point cloud of the target object. This significantly improves the quality of the input data
                              and facilitates accurate and eﬃcient point cloud registration and pose estimation.

                              Figure 9. Comparison of scene point cloud before and after segmentation: (a) original point cloud;
                              (b) point cloud after SAC segmentation.
Appl. Sci. 2025, 15, 6583                                                                                        10 of 22

                            2.3. Fusion Processing
                                 The point cloud dataset collected by the depth camera is large. Even after pre-pro-
                            cessing, it is still dense, and if directly used for alignment, it will consume more time and
                            memory, making it diﬃcult to meet real-time requirements, so it is necessary to further
                            segment the scene point cloud. After locating the position of the target object through the
                            deep learning module, the coordinates of the center point of the detection rectangle box
                            are converted to 3D coordinates, and then the coordinates are used to perform a KD-Tree
                            search so as to achieve the positioning and segmentation of the target point cloud.

                            2.3.1. 3D Coordinate Transformation
                                 After the object detection is completed, the coordinate information obtained from the
                            detection can be used to quickly locate the target area, optimize the KD-Tree search pro-
                            cess, and improve the eﬃciency of target point cloud retrieval. To achieve this, the 2D
                            center coordinates need to be transformed into 3D coordinates. Since the coordinates of
                            the object are identified in the RGB image and the resolutions of the RGB and depth im-
                            ages are diﬀerent, the RGB image must first be normalized. This process requires the use
                            of the depth camera’s intrinsic matrix:
                                                                            fx            0       cx 
                                                                                                     
                                                        intrinsic matrix =  0             fy      cy  ,             (1)
                                                                           0              0       1 
                                                                           
                            where f x and     f y are the focal lengths in the x and y directions of the image plane
                            (measured in pixels), which determine the image scaling. c x and c y represent the co-
                            ordinates of the principal point, which is typically located at the center of the image.
                                Then, the 3D coordinate transformation is performed using the following equation:
                                                                              Depth(Cx  cx ) ,
                                                            TargetPoint x =                                           (2)
                                                                                f x  Depthscale
                                                                              Depth  (C y  c y ) ,
                                                           TargetPoint y =                                            (3)
                                                                                f y  Depthscale

                                                                                    Depth ,
                                                              TargetPoint_z =                                         (4)
                                                                                   Depthscale
                            where TargetPoint x , TargetPoint y , and TargetPoint z denote the 3D coordinates of the tar-
                            get point after coordinate transformation, corresponding to the horizontal, vertical, and
                            depth positions in the camera coordinate system, respectively; Depth denotes the raw
                            depth value acquired by the depth camera, typically measured in millimeters (mm);
                            Depthscale takes a value of 1000 and is used to convert the depth unit from millimeters to
                            meters to ensure consistency with the camera coordinate system; and C x represents the
                            horizontal and vertical coordinates (in pixels) of the center point of the detected bounding
                            box after alignment with the RGB image. The target point coordinates obtained from the
                            2D RGB image and the corresponding depth map can thus be accurately converted to 3D
                            coordinates using the intrinsic parameters of the depth camera.

                            2.3.2. KD-Tree Neighbor Search
                                 Based on the data structuring algorithm in NNL [21], KD-Tree (k-dimensional tree)
                            serves as an eﬃcient spatial indexing structure, widely adopted for its simplicity, low
                            memory overhead, and high computational eﬃciency. The core idea of the KD-Tree algo-
                            rithm is to select a dimension and split the set of points based on the median value along
Appl. Sci. 2025, 15, 6583                                                                                       11 of 22

                            that dimension, ensuring that the resulting subsets are approximately equal in size. This
                            binary partitioning process is repeated until the dataset can no longer be subdivided.
                                  Assuming a two-dimensional dataset, as illustrated in Figure 10, the construction be-
                            gins by computing the median of all points along the X-axis, which serves as the initial
                            splitting reference. This divides the dataset into left and right subsets. The median of the
                            Y-axis is then computed within each subset to further split them into upper and lower
                            partitions. This recursive partitioning continues, alternating between axes until each point
                            is individually isolated. The positions of the sample points are then visualized within the
                            2D coordinate system.

                            Figure 10. Binary tree diagram.

                                 Based on this structure, KD-Tree enables eﬃcient search operations. Compared with
                            a traditional linear search, its average time complexity is O(logn) , which is significantly
                            better than the O(n) of a linear search. To validate this conclusion, we performed radius-
                            based neighbor searches on point clouds with varying numbers of points and recorded
                            the search time. As shown in Table 3, for small-scale point clouds, the linear search per-
                            forms comparably to or even better than KD-Tree. However, as the point cloud size in-
                            creases, KD-Tree demonstrates significantly higher search eﬃciency, confirming its accel-
                            eration advantage in large-scale data scenarios.

                            Table 3. Comparison of radius neighborhood search time.

     Number of Points         Search Radius (m)          KD-Tree Radius Search Time (ms) Linear Search Time (ms)
          1000                       0.02                              74                           47
         10,000                      0.02                             184                           501
         50,000                      0.02                             774                          2387
        100,000                      0.02                             1752                         5141
        500,000                      0.02                             7383                        19,378

                                 As shown in Figure 11, this paper utilizes the neighbor search method of KD-Tree to
                            rapidly extract the region of interest around the 3D target point, enabling eﬃcient locali-
                            zation and segmentation of the target point cloud. By this method, the search range can
                            be reduced and the initialization accuracy of point cloud matching can be eﬀectively im-
                            proved, thus accelerating the convergence speed of the alignment algorithm and improv-
                            ing the robustness.
Appl. Sci. 2025, 15, 6583                                                                                            12 of 22

                            Figure 11. Target point cloud segmentation: (a) RGB target detection result; (b) segmented target
                            point cloud (the green part indicates the segmented target).

                            2.4. Point Cloud Registration
                                  After locating and segmenting the target point cloud, the corresponding template
                            point cloud is selected based on the pose classification results from YOLOv8-URE, and
                            registration is then performed between the template and target point clouds.
                                  Point cloud registration can be divided into two stages: coarse registration and fine
                            registration. Coarse registration is used when the relative positions of point clouds are
                            completely unknown. Its goal is to estimate an approximate rotation and translation ma-
                            trix to align the target point cloud into a common coordinate system, thereby providing a
                            reliable initial estimate for fine registration. Fine registration then refines this alignment
                            by minimizing the spatial discrepancy between point clouds to compute a more accurate
                            transformation matrix for precise alignment.
                                  In this study, the sample consensus algorithm is selected for coarse registration. This
                            algorithm handles outliers through random sampling, and its procedure includes the fol-
                            lowing steps:
                                  1. Random Sampling—Randomly select a subset of points from the source point
                            cloud.
                                  2. Transformation Estimation—Compute a rigid transformation matrix based on the
                            sampled points.
                                  3. Model Verification—Apply the transformation to the entire point cloud and eval-
                            uate its consistency.
                                  As can be seen in Figure 12, both the registration result of the sample and that of the
                            actual workpiece demonstrate that accurate alignment can still be achieved despite the
                            presence of surrounding outlier points, indicating the strong robustness of the algorithm,
                            which makes it more suitable for registration in industrial environments.

                            Figure 12. Sample consensus alignment results: (a) front view of the sample point cloud; (b) side
                            view of the sample point cloud; (c) front view of the workpiece point cloud; (d) side view of the
                            workpiece point cloud.
Appl. Sci. 2025, 15, 6583                                                                                                13 of 22

                                 To further improve the point cloud alignment accuracy and ensure computational
                            eﬃciency, this paper selects the NDT (normal distributions transform registration) algo-
                            rithm as the fine alignment stage algorithm. As shown in Figure 13, taking the workpiece
                            point cloud used in this paper as an example, a comparison is made between the proposed
                            registration algorithm and commonly used methods such as ICP and GICP in a single-
                            object scenario, which shows that the results of this paper’s alignment algorithm are more
                            accurate and have strong robustness to noise and outliers.

                            Figure 13. Comparison of ICP, GICP, and SAC + NDT registration results: (a) ICP registration front
                            view; (b) ICP registration side view; (c) GICP registration front view; (d) GICP registration side
                            view; (e) SAC + NDT registration front view; (f) SAC + NDT registration side view.

                            2.5. Grasp Pose Estimation
                                  After completing the registration between the target point cloud and the template
                            point cloud, a homogeneous transformation matrix T is obtained. This matrix represents
                            the rigid transformation between the two point clouds and is used to align the template
                            point cloud with the target point cloud. Subsequently, a homogeneous transformation
                            matrix is applied to the ideal grasp pose defined on the template, thereby deriving the
                            corresponding grasp pose for the target point cloud. This process enables the transfer of
                            known grasping strategies from the template to the real object. The transformation matrix
                            is a standard 4 × 4 homogeneous matrix, and is expressed as follows:
                                                                          R      t
                                                                       T  T      ,                                        (5)
                                                                          0      1
                            where R   rij   R 33 , is a rotation matrix, which describes the pose of the object, and
                                                     
                                                     T
                            t   t x , t y , t z  , is a translation vector, which describes the position of the object in 3D
                            space.
Appl. Sci. 2025, 15, 6583                                                                                         14 of 22

                                                                                      template
                                 Using this matrix, the predefined ideal grasp pose Tgrasp     of the template point
                                                                           target
                            cloud can be mapped to the actual grasp pose Tgrasp   of the target point cloud. The com-
                            putation is as follows:
                                                                     target
                                                                   Tgrasp    T Tgrasp
                                                                                   template
                                                                                            .                          (6)
                                The resulting grasp pose is still expressed in the camera coordinate system. Subse-
                            quently, it can be further transformed into the robot base coordinate system using the
                            known hand–eye calibration matrix Tcam 2 base :
                                                                  base
                                                                Tgrasp  Tcam 2base Tgrasp
                                                                                       t arg et
                                                                                                .                      (7)
                                 Finally, the grasp pose is processed through inverse kinematics based on the robot’s
                            DH model to solve for the joint angles. These computed joint values are subsequently used
                            to generate control commands for executing the grasping operation.

                            3. Experimental Results and Analysis
                            3.1. Experimental Setup for Object Detection
                                  The experimental setup for object detection in this study was as follows: an Nvidia
                            GeForce RTX 2080 Ti GPU with 16 GB of memory running on the Windows 10 operating
                            system. The programming language used was Python 3.8.18, with CUDA version 11.3.
                            The YOLOv8n model was implemented using the Ultralytics library (version 8.1.9). The
                            initial learning rate was set to 0.01, with three warm-up epochs. Data augmentation was
                            disabled during the final 10 training epochs. The detailed training parameters are sum-
                            marized in Table 4.

                            Table 4. Network training experiment parameters.

                                                  Training Parameter                                     Value
                                                   Input Image Size                                        640
                                                  Number of Epochs                                         100
                                                       Batch size                                           16
                                                       Optimizer                                          SGD
                                               Momentum of Optimizer                                      0.937
                                             Optimizer Weight Decay Factor                               0.0005

                            3.2. Dataset Description
                            3.2.1. Dataset of Reducing Tee Pipes
                                The dataset is a self-constructed collection of a reducing tee pipe, designed for robotic
                            arm grasping of stacked objects in industrial environments. A total of 3000 images were
                            captured, featuring the target object in various poses, quantities, and simulated stacking
                            scenarios. The dataset was divided into a training set and a validation set in a 9:1 ratio.

                            3.2.2. WiderPerson Dataset
                                 The WiderPerson dataset is a publicly available dataset designed for outdoor pedes-
                            trian detection. It is characterized by high target density and severe occlusion, especially
                            in crowded scenes with substantial target overlaps. These characteristics closely resemble
                            industrial environments, which often involve stacking, occlusions, and densely arranged
                            objects. Therefore, this dataset was selected in this study for training and evaluating the
                            object detection module. Considering that some images lack annotation information, the
                            original dataset was filtered and preprocessed, resulting in a total of 13,381 fully annotated
                            image samples. Among them, 7999 images were used for training, 1000 for validation, and
Appl. Sci. 2025, 15, 6583                                                                                           15 of 22

                            4385 for testing. This dataset provides strong support for evaluating detection algorithms
                            under complex scenarios.

                            3.3. Description of the Indicator Parameters
                                 In this paper, precision (P), recall (R), mean average precision (mAP), number of net-
                            work parameters, and floating-point operations (GFLOPs) are used as evaluation metrics
                            to assess the performance of the model. The definitions of precision, recall, and mAP are
                            as follows:
                                                                             Tp
                                                                    P                    100%                         (8)
                                                                           TP  FP                    ,
                                                                             Tp
                                                                    R                    100%                         (9)
                                                                           TP  FN                    ,
                                                                                  1
                                                                     AP   P ( r ) dr ,                               (10)
                                                                                  0

                                                                                      k

                                                                                       AP    i
                                                                                                                       (11)
                                                                      mAP  i 1                  .
                                                                                          k
                                In Equations (8) and (9), Tp (true positive) refers to correctly predicted positive sam-
                            ples, i.e., samples that are actual targets and correctly predicted as such; FP (false posi-
                            tive) refers to false positives, i.e., non-target samples that are incorrectly predicted as tar-
                            gets; and FN (false negative) refers to false negatives, i.e., target samples that are incor-
                            rectly predicted as non-targets. In Equation (10), AP (average precision) represents the
                            accuracy for a single category. In Equation (11), mAP (mean average precision) is ob-
                            tained by integrating the area under the precision–recall curve and represents the average
                            accuracy across all k categories.

                            3.4. Ablation Experiment
                                 To evaluate the impact of each proposed improvement module on overall perfor-
                            mance, systematic ablation experiments were conducted on a self-constructed dataset fea-
                            turing occlusion and stacking scenarios. The baseline was established using the basic ver-
                            sion of YOLOv8-URE basic version without any improvement modules (denoted Base).
                            Building upon this baseline, the modules were introduced sequentially: C2f_UniRepLK-
                            NetBlock (Base-1), ELA mechanism (Base-2), CSPStage-Dy enhanced neck (Base-3), and
                            ShapeIoU loss (Base-4). Furthermore, additional configurations—Base-5, Base-6, and
                            Base-7—were constructed by progressively combining ELA, the improved neck, and
                            ShapeIoU loss on top of Base-1.
                                 The experimental results, as shown in Table 5, indicate that the standalone introduc-
                            tion of the UniRepLKNetBlock significantly reduces the model parameters (by approxi-
                            mately 34.3%) and computational complexity (FLOPs decreased by 2.3%), albeit at the cost
                            of some accuracy loss. After incorporating the ELA mechanism, both recall and
                            mAP@0.5:0.95 show marked improvements, demonstrating its strong capability to en-
                            hance key regions in shallow features. The improved neck structure (including DySample)
                            significantly boosts the detection accuracy of primary targets (mAP@0.5 increased to
                            97.3%), highlighting its advantages in multi-scale fusion and feature consistency.
                                 Notably, when both ELA and the CSPStage-Dy enhanced neck are introduced simul-
                            taneously in Base-6, the mAP improvement is no longer dramatically higher compared to
                            individual modules. However, this combination maintains a lightweight architecture
Appl. Sci. 2025, 15, 6583                                                                                                    16 of 22

                               while achieving a more balanced and stable performance in recall and overall metrics. The
                               underlying mechanism is that ELA strengthens the front-end network’s perception of crit-
                               ical target regions, making target contour features more prominent, whereas DySample
                               enhances spatial consistency and contextual modeling in the neck’s multi-scale fusion.
                               Acting at diﬀerent network stages, these two modules complement each other under a
                               decoupled structure, improving overall perception and representation capabilities,
                               thereby exhibiting stronger robustness and detection stability in complex occlusion and
                               dense target environments.
                                     Finally, with the introduction of ShapeIoU loss (Base-7), the model’s convergence
                               speed further accelerates, bounding box regression becomes more precise, and detection
                               accuracy reaches its highest (mAP@0.5 of 98.3%). This validates the complementary value
                               and optimization potential of each module within the overall architecture.

                               Table 5. Results of ablation experiments.

Algorithm Uni ELA           Improved Neck ShapeIoU P (%) R (%) mAP@0.5 (%) Parameter (M) GFLOPs                               FPS
   Base    ×   ×                  ×          ×      96.5 90.3     96.5         3.15        8.9                                614
  Base-1   √   ×                  ×          ×      94.8 92.0     96.5         2.16        5.9                                660
  Base-2   ×   √                  ×          ×      96.8 94.0     95.9         3.07        8.2                                640
  Base-3   ×   ×                  √          ×      95.8 95.0     97.3         3.26        8.2                                605
  Base-4   ×   ×                  ×          √      94.9 94.2     96.3          3.0        8.0                                650
  Base-5   √   √                  ×          ×      91.5 94.8     96.7         2.09        5.9                                662
  Base-6   √   √                  √          ×      95.9 95.0     96.7         2.28        6.1                                632
  Base-7   √   √                  √          √      97.6 95.4     98.3         2.29        6.1                                639
                               The best results for each metric are highlighted in bold; FPS was evaluated with a batch size of 16.

                               3.5. Analysis of Object Detection Results
                               3.5.1. Comparison of Model Experimental Results
                                     To verify the detection accuracy of YOLOv8-URE in complex scenarios, a large num-
                               ber of workpieces were placed in the original environment, introducing complex stacking
                               relationships and dense occlusions. As shown in Figure 14, for a clear comparison of detec-
                               tion results, 20 workpieces were used as an example. The YOLOv8-URE network was able
                               to detect all the workpieces and classify them correctly, while YOLOv8n missed one target.
                                     To further demonstrate the detection accuracy of YOLOv8-URE, the number of work-
                               pieces was gradually increased to evaluate its performance under varying conditions. As
                               shown in Table 6, both YOLOv8-URE and YOLOv8n perform well with a small number
                               of targets. However, as the number of targets increases, YOLOv8n shows a clear rise in
                               missed and false detections. In contrast, YOLOv8-URE consistently maintains more accu-
                               rate detection results, demonstrating better robustness and overall performance in com-
                               plex, high-density, and occluded scenarios.

                               Figure 14. YOLOv8-URE and YOLOv8n detection results in the original scene: (a) YOLOv8-URE
                               detection results in the original scene; (b) YOLOv8n detection results in the original scene. Note: red
Appl. Sci. 2025, 15, 6583                                                                                                    17 of 22

                                   bounding boxes are generated by the algorithm; green boxes indicate missed detections; yellow
                                   boxes indicate false detections.

                                   Table 6. Comparison of original scene detection.

                                   Missed                   False                    Correct                  Detection
Number of Targets
                                 Detections             Detections                 Detections                  Accuracy
            15                    0 ± 0/0 ± 0            0 ± 0/0 ± 0              15 ± 0/15 ± 0      100% ± 0.00%/100% ± 0.00%
            20                 0 ± 0/0.4 ± 0.49        0 ± 0/0.2 ± 0.4         20 ± 0/19.4 ± 0.49      100% ± 0.00/97% ± 2.50%
            25              0.2 ± 0.4/3.2 ± 0.75    0.4 ± 0.49/0.6 ± 0.49    24.4 ± 0.49/21.2 ± 0.75 97.6% ± 1.96%/84.8% ± 2.99%
            30                2 ± 0.63/4 ± 0.89     0.8 ± 0.75/1.8 ± 0.4     27.2 ± 0.75/24.2 ± 0.75 90.67% ± 2.49/80.67% ± 2.49
            35               5.4 ± 0.49/8 ± 0.63    2.4 ± 0.5/3.2 ± 0.75      27.2 ± 0.8/23.8 ± 0.98    77.71% ± 2.14/68% ± 2.8
            40              8 ± 1.17/11.8 ± 0.75    3.8 ± 0.75/4.4 ± 0.8      27.4 ± 1.02/23.8 ± 0.4   68.5% ± 2.25/59.5% ± 1.00
                                   All values are presented in the format of YOLOv8-URE/YOLOv8n; all results are reported as means
                                   ± standard deviation over five independent experiments.

                                        To evaluate the robustness of the YOLOv8-URE model under conditions resembling
                                   real-world industrial environments, this study processed the original scenarios by adding
                                   random Gaussian noise and random black screen occlusion, so as to generate blurred sce-
                                   narios for testing and comparing with the YOLOv8n model.
                                        As shown in Figure 15, taking the detection of 20 workpieces as an example, both
                                   models experience increased missed and false detections in blurred scenarios. However,
                                   YOLOv8-URE consistently achieves a higher detection success rate than YOLOv8n. As
                                   shown in Table 7, as the number of targets increases, detection performance in the blurred
                                   scene declines more noticeably, especially for YOLOv8n. In contrast, YOLOv8-URE main-
                                   tains results closer to the actual target count with fewer errors, demonstrating stronger
                                   robustness and accuracy under visually degraded conditions.

                                   Figure 15. Comparison of detection results in blurred scenes between YOLOv8-URE and YOLOv8n:
                                   (a) detection results of YOLOv8-URE in blurred scenes; (b) detection results of YOLOv8n in blurred
                                   scenes. Note: red bounding boxes are generated by the algorithm, green boxes indicate missed de-
                                   tections, and yellow boxes indicate false detections.

                                   Table 7. Comparison of blurred scene detection.

  Number of                Missed                   False                    Correct                      Detection
   Targets               Detections              Detections                Detections                      Accuracy
     15                   0 ± 0/0 ± 0           0 ± 0/2 ± 0.5              15 ± 0/15 ± 0          100% ± 0.00%/100% ± 0.00%
     20              0.4 ± 0.49/2.6 ± 0.8    0.2 ± 0.4/1.6 ± 0.49     19.4 ± 0.49/15.8 ± 0.75      97% ± 2.45%/79% ± 3.70%
     25               1.4 ± 0.8/4 ± 0.89    2.4 ± 1.02/2.6 ± 0.49     21.2 ± 1.33/18.4 ± 1.02    84.8% ± 5.31%/73.6% ± 4.08%
     30             1.8 ± 0.75/5.2 ± 0.75   3.2 ± 0.75/2.8 ± 0.75       25 ± 1.1/22 ± 0.63      83.33% ± 3.65%/73.33% ± 2.11%
     35              5.2 ± 0.75/8 ± 0.63    3.4 ± 1.02/3.6 ± 0.49      26.4 ± 0.6/23.4 ± 0.8    75.43% ± 2.91%/66.86% ± 2.29%
     40              9 ± 0.75/13 ± 0.63     3.2 ± 0.75/4.2 ± 0.75      27 ± 0.63/22.8 ± 1.17      67.50% ± 1.5%/57% ± 2.92%
Appl. Sci. 2025, 15, 6583                                                                                                18 of 22

                            All values are presented in the format of YOLOv8-URE/YOLOv8n; all results are reported as means
                            ± standard deviation over five independent experiments.

                                 In summary, the detection performance of YOLOv8-URE is similar to that of
                            YOLOv8n when the number of targets is small, but with an increase in the number of
                            targets, the misses and false detection of YOLOv8n rise significantly, especially in blurred
                            scenes. In contrast, YOLOv8-URE exhibits higher accuracy and robustness under higher
                            target density and occlusion conditions, and the overall detection performance is better
                            than YOLOv8n.

                            3.5.2. Generalization Performance Comparison
                                 To verify the detection performance and generalization capability of YOLOv8-URE on
                            external datasets, the model was trained on the publicly available WiderPerson dataset and
                            compared with other mainstream algorithms. The experimental results show that the
                            YOLOv8-URE method achieves a recall of 80.4% on the test set, which is higher than other
                            mainstream algorithms. Moreover, YOLOv8-URE is the smallest, at only 4.46 MB, making it
                            highly suitable for lightweight deployment. The experimental results are shown in Table 8.

                            Table 8. Comparison of algorithm generalization.

                                 Algorithm               R%          mAP@0.5%           mAP@0.5:0.95%             Size (MB)
                                  YOLOv8n             79.7 ± 0.8      88.4 ± 0.6          62.3 ± 1.0                  6.5
                                YOLOv7-tiny           80.2 ± 0.7      86.9 ± 0.8          54.3 ± 1.2                 11.7
                                  YOLOv4              75.2 ± 0.9      84.9 ± 0.7          51.9 ± 1.3                17.76
                                  YOLOv3              70.3 ± 1.1      82.0 ± 1.0          47.6 ± 1.5                117.7
                                  YOLOv5s             74.1 ± 0.6      86.3 ± 0.7          55.2 ± 1.1                13.78
                                Faster R-CNN          71.3 ± 0.8      87.2 ± 0.6          56.9 ± 1.3                 108
                                     SSD              64.8 ± 1.2      75.9 ± 1.5          47.8 ± 1.4                 92.6
                                YOLOv8-URE            80.4 ± 0.5      88.3 ± 0.6          62.4 ± 0.8                 4.46
                            The best results for each metric are highlighted in bold; all results are reported as means ± standard
                            deviation over five independent experiments.

                            3.6. Grasping Algorithm Experiments
                                 The experiments were conducted on the Visual Studio 2019 platform with an R7-
                            5800H CPU. The robotic arm used was the SD-700E model from Xinshida. The grasping
                            environment is illustrated in Figure 16.

                            Figure 16. Grasping experimental environment: 1. STEP-700E; 2. pneumatic gripper; 3. Tuyang
                            depth camera module; 4. workpiece to be grasped.
Appl. Sci. 2025, 15, 6583                                                                                                  19 of 22

                            3.6.1. Registration Algorithm Experiment
                                  To verify the superiority of the proposed algorithm and evaluate the acceleration ef-
                            fect of integrating KD-Tree search on the overall process of point cloud processing, this
                            paper presents a comparative experiment. The experiment takes the entire point cloud
                            processing module as the evaluation object, with the version excluding KD-Tree-based
                            segmentation used as the control group. To comprehensively evaluate the performance of
                            the algorithms, three metrics are used for comparison:
                                  1. Program running time—to measure computational eﬃciency;
                                  2. Root mean square error (RMSE)—to reflect the overall level of point cloud regis-
                            tration error (see Equation (10));
                                  3. Mean absolute error (MAE)—to quantify the absolute deviation of registration er-
                            rors (see Equation (11)).

                                                                             1 n
                                                                               
                                                                                                  2
                                                                  RMSE =            T ( pi )  qi                             (12)
                                                                             n i 1

                                                                            1 N
                                                                  MAE        ‖T( pi )  q‖
                                                                            n i 1
                                                                                           i                                  (13)

                                In the equation, n denotes the number of point pairs involved in the registration
                            from the template point cloud, pi represents the i -th point in the template point cloud,
                            T ( pi ) is the transformed position of pi after registration, and qi is the corresponding
                            point in the target point cloud matched to pi .
                                 As shown in Table 9, the proposed algorithm rapidly locates the target point cloud
                            within a limited search space through KD-Tree search. This significantly improves the
                            processing speed and real-time performance, while also reducing RMSE and MAE to a
                            certain extent, thereby satisfying the requirements for point cloud registration.

                            Table 9. Algorithm comparison results.

                                  Algorithm                  Control Algorithm                        Proposed Algorithm
                                Running Time (s)                  10.5949                                   4.18396
                                    RMSE                         0.317391                                  0.052965
                                     MAE                         0.267475                                  0.051005
                            The best results for each metric are highlighted in bold.

                            3.6.2. Workpiece Grasping Experiment
                                 As shown in Figure 17, this is the main process for target object grasping.

                            Figure 17. Grasping process diagram: (a) original point cloud; (b) YOLOv8-URE detection result; (c)
                            illustration of target point cloud segmentation; (d) illustration of pose estimation for the registered
Appl. Sci. 2025, 15, 6583                                                                                                20 of 22

                            target point cloud; (e) Illustration of grasping pose. The green part represents the segmented target
                            point cloud.

                                 To evaluate the grasping performance of the proposed algorithm and verify its ro-
                            bustness, four distinct object poses were defined, as illustrated in Figure 18. For each pose,
                            25 grasping trials were conducted under consistent experimental conditions.

                            Figure 18. Workpiece placement pose for grasping: (a) Pose①; (b) Pose②; (c) Pose③; (d) Pose④.

                                The experimental results are shown in the Table 10. Postures 1 and 3 achieved higher
                            success rates, while postures 2 and 4 showed a noticeable drop in grasp success rates. An
                            analysis of the failed cases reveals two main causes:
                            1. In Postures 2 and 4, occlusions in the point cloud led to insuﬃcient feature points,
                                resulting in reduced pose estimation accuracy.
                            2. Under these postures, the gripper was more likely to collide with the object, which
                                caused grasp failures.

                            Table 10. Results of the grasping experiment.

                                  Object Pose                Grasp Attempts                Failures          Success Rate
                                   Pose①                           25                          3                 88%
                                   Pose②                           25                          4                 84%
                                   Pose③                           25                          2                 92%
                                   Pose④                           25                          5                 80%

                            4. Conclusions and Future Work
                            4.1. Conclusions
                                 (1) In this study, the YOLOv8n algorithm was improved and redesigned by enhanc-
                            ing feature extraction and reconstructing the feature fusion network. In the feature extrac-
                            tion stage, large-kernel convolutions are introduced to expand the receptive field and en-
                            hance object perception, while a lightweight ELA mechanism is integrated to eﬀectively
                            reduce the number of parameters and floating-point operations. In the feature fusion
                            stage, the network is redesigned to improve detection accuracy without significantly in-
                            creasing computational cost, thus reducing both false positives and false negatives. Abla-
                            tion experiments show that compared to the original YOLOv8n, the improved YOLOv8-
                            URE reduces the number of parameters by 27.3% and increases precision by 1.1%, recall
                            by 5.1%, and mAP@0.5 by 1.8%, while reducing FLOPs by 2.7 GFLOPs and improving
                            inference speed by 25 FPS. In generalization comparison experiments, YOLOv8-URE
                            achieved 0.7% higher recall than YOLOv8n, with a nearly identical AP value, and the
                            overall model size was reduced by 31.1%. These results demonstrate that YOLOv8-URE
                            achieves improved accuracy while maintaining a lightweight design and strong generali-
                            zation, making it a practical and versatile solution.
                                 (2) In the point cloud processing module, this paper proposes a point cloud segmen-
                            tation algorithm that integrates 3D coordinate transformation and KD-Tree search. By
                            transforming coordinates to provide initial target points for KD-Tree, the method eﬀec-
                            tively enables fast localization and segmentation of the target point cloud, reduces the
Appl. Sci. 2025, 15, 6583                                                                                                        21 of 22

                                  number of points involved in computation, and accelerates subsequent alignment. At the
                                  alignment stage, combining sample consensus with the NDT algorithm achieves higher
                                  alignment accuracy and robustness in complex environments compared to traditional
                                  methods, providing a more reliable positional basis for subsequent workpiece grasping.
                                       (3) Grasping experiments were conducted on the target workpiece under various
                                  poses. The results demonstrate that the system maintains a high success rate across diﬀer-
                                  ent orientations, indicating strong robustness and reliable performance in completing the
                                  grasping tasks.

                                  4.2. Future Work
                                       (1) Since the object detection module relies on deep learning algorithms, its perfor-
                                  mance is to some extent constrained by the size of the dataset. Additionally, when switch-
                                  ing to new target objects, the process of recollecting and annotating data remains labor-
                                  intensive. Therefore, future work should further explore methods such as adaptive fine-
                                  tuning, incremental learning, and transfer learning to enhance the model’s performance
                                  and generalization capabilities.
                                       (2) In the process of feature fusion between RGB information and point cloud data,
                                  issues such as viewpoint diﬀerences, resolution mismatch, and occlusion may arise dur-
                                  ing data acquisition, aﬀecting the quality of fusion. Therefore, future research should con-
                                  sider incorporating transformer-based feature alignment mechanisms to improve the ac-
                                  curacy and robustness of multi-modal feature fusion.
                                       (3) In practical grasping tasks, the complex geometry of certain workpiece poses may
                                  cause collisions between the gripper and the object, leading to grasp failures. Conse-
                                  quently, future research will focus on optimizing the grasp path to further improve grasp
                                  success rate and stability, and we will conduct a quantitative comparison with the state-
                                  of-the-art GraspNet framework under the same experimental conditions to comprehen-
                                  sively evaluate the proposed improvements.

                                  Author Contributions: Conceptualization, X.Y. and X.Q.; methodology, X.Y. and X.Q.; software,
                                  X.Y.; validation, X.Q. and L.Z.; formal analysis, L.Z.; investigation, J.W.; data curation, J.W.; writ-
                                  ing—original draft preparation, X.Q.; writing—review and editing, X.Y. and Y.C.; supervision, Y.C.
                                  All authors have read and agreed to the published version of the manuscript. All authors have read
                                  and agreed to the published version of the manuscript.

                                  Funding: This research was funded by the Natural Science Foundation of Hubei Province (Youth
                                  Program) (2023AFB381), the Hubei Agricultural Machinery Equipment Shortcomings Tackling Pro-
                                  ject “Research, Development, and Promotion of Key Technologies and Equipment for Aquatic Prod-
                                  uct Processing” (HBSNYT202221), and the Youth Talent Project of the Science and Technology Re-
                                  search Program of the Hubei Provincial Department of Education (Project Number Q20231412).

                                  Institutional Review Board Statement: Not applicable.

                                  Informed Consent Statement: Not applicable.

                                  Data Availability Statement: The data presented in this study are available from the corresponding
                                  author upon reasonable request. The data are not publicly available due to privacy restrictions.

                                  Conflicts of Interest: The authors declare no conflicts of interest.

References
1.    Liu, C.; Yang, T. Application and industrial development of machine vision in intelligent manufacturing. Mach. Tool Hydraul.
      2021, 49, 172–178. (in Chinese)
2.    Li, C.; Wei, X.; Zhou, Y.; Li H. Research on control of intelligent logistics sorting robot based on laser vision guidance. Laser J.
      2022, 43, 217–222. (in Chinese)
Appl. Sci. 2025, 15, 6583                                                                                                        22 of 22

3.    Xue, L.; Zhou, J. Visual servo control of agricultural robot parallel picking arm. Sens. Microsyst. 2017, 36, 123–126.
      https://doi.org/10.13873/j.1000-9787(2017)05-0123-04. (in Chinese)
4.    Lu, Z. Research on stacking object grasping method based on deep learning. Master’s Thesis, Guangdong University of Tech-
      nology, Guangzhou, China, 2020. https://doi.org/10.27029/d.cnki.ggdgu.2020.000350. (in Chinese)
5.    Li, X.; Li, J.; Zhang, X.; Peng, X. Optimal grasp posture detection method for robots based on deep learning. Chin. J. Sci. Instrum.
      2020, 41, 108–117. https://doi.org/10.19650/j.cnki.cjsi.J2006162. (in Chinese)
6.    Guo, D.; Kong, T.; Sun, F.; Liu, H. Object discovery and grasp detection with a shared convolutional neural network. In Pro-
      ceedings of the 2016 IEEE International Conference on Robotics and Automation, Stockholm, Sweden, 16–21 May 2016; IEEE:
      New York, NY, USA, 2016; pp. 1234–1239.
7.    Geng, Z.; Chen, G. A novel real-time grasping method combined with YOLO and GDFCN. In Proceedings of the 2022 IEEE 10th
      Joint International Information Technology and Artificial Intelligence Conference (ITAIC), Beijing, China, 27–29 October 2022;
      IEEE: New York, NY, USA, 2022; pp. 500–505.
8.    Xiao, X.; Zheng, Y.; Sai, Q.; Fu, D. Lightweight model-based 6D pose estimation of drones. Control Eng. 2025, 24, 1–10.
      https://doi.org/10.14107/j.cnki.kzgc.20240037. (in Chinese)
9.    Zhang, Y.; Yi, J.; Chen, Y.; Dai, Z.; Han, F.; Cao, S. Pose estimation for workpieces in complex stacking industrial scene based
      on RGB images. Appl. Intell. 2022, 1, 1–3.
10.   Guan, Q.; Sheng, Z.; Xue, S. HRPose: Real-time high-resolution 6D pose estimation network using knowledge distillation. Chin.
      J. Electron. 2023, 32, 189–198.
11.   Wang, G.; Manhardt, F.; Tombari, F.; Ji, X. GDR-Net: Geometry-guided direct regression network for monocular 6D object pose
      estimation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, TN,
      USA, 19–25 June 2021; IEEE: Los Alamitos, CA, USA, 2021; pp. 16611–16621.
12.   Xu, W.; Wan, Y. ELA: Eﬃcient local attention for deep convolutional neural networks, arXiv 2024, arXiv:2403.01123.
13.   Zhang, H.; Zhang, S. Shape-Iou: More accurate metric considering bounding box shape and scale. arXiv 2023, arXiv:2312.17663.
14.   Ding, X.; Zhang, Y.; Ge, Y.; Zhao, S.; Song, L.; Yue, X.; Shan, Y. UniRepLKNet: A universal perception large-kernel convNet for
      audio, video, point cloud, time-series, and image recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision
      and Pattern Recognition (CVPR), Seattle, WA, USA, 17–21 June 2024; IEEE: Los Alamitos, CA, USA, 2024; pp. 5513–5524.
15.   Ding, X.; Zhang, X.; Ma, N.; Han, J.; Ding, G.; Sun, J. RepVGG: Making VGG-style ConvNets great again. In Proceedings of the
      IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville, TN, USA, 19–25 June 2021; IEEE: Los
      Alamitos, CA, USA, 2021; pp. 13733–13742.
16.   Ioﬀe, S.; Szegedy, C. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In Proceed-
      ings of the 32nd International Conference on Machine Learning (ICML), Lille, France, 6–11 July 2015; PMLR: Cambridge, MA,
      USA, 2015; pp. 448–456.
17.   Ding, X.; Zhang, X.; Han, J.; Ding, G. Scaling up your kernels to 31×31: Revisiting large kernel design in CNNs. In Proceedings
      of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),New Orleans, LA, USA, 19–24 June 2022;
      IEEE: Los Alamitos, CA, USA, 2022; pp. 11963–11975.
18.   Draelos, R.L.; Carin, L. Use HiResCAM instead of Grad-CAM for faithful explanations of convolutional neural networks. arXiv
      2020, arXiv:2011.08891.
19.   Xu, X.; Jiang, Y.; Chen, W.; Huang, Y.; Zhang, Y.; Sun, X. Damo-YOLO: A report on real-time object detection design. arXiv 2022,
      arXiv:2211.15444.
20.   Liu, W.; Lu, H.; Fu, H.; Cao, Z. Learning to upsample by learning to sample. In Proceedings of the IEEE/CVF International
      Conference on Computer Vision (ICCV), Paris, France, 2–7 October 2023; IEEE: Los Alamitos, CA, USA, 2023; pp. 6027–6037.
21.   Baranchuk, D.; Babenko, A.; Malkov, Y. Revisiting the inverted indices for billion-scale approximate nearest neighbors. In Pro-
      ceedings of the European Conference on Computer Vision (ECCV), Munich, Germany, 8–14 September, 2018; Springer: Cham,
      Switzerland, 2018; pp. 202–216.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual au-
thor(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
