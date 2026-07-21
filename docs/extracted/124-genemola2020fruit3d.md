---
source_id: 124
bibtex_key: genemola2020fruit3d
title: Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry
year: 2020
domain_theme: Pertanian
verified_pdf: 124_GeneMola_Fruit.pdf
char_count: 60911
---

Document downloaded from:

http://hdl.handle.net/10459.1/67802

The final publication is available at:

https://doi.org/10.1016/j.compag.2019.105165

Copyright

cc-by-nc-nd, (c) Elsevier, 2020

               Està subjecte a una llicència de
               Reconeixement-NoComercial-SenseObraDerivada 3.0 de Creative Commons
 1   Fruit detection and 3D location using instance segmentation neural
 2   networks and structure-from-motion photogrammetry

 3   Jordi Gené-Molaa,*, Ricardo Sanz-Cortiellaa, Joan R. Rosell-Poloa, Josep-Ramon Morrosb, Javier
 4   Ruiz-Hidalgob, Verónica Vilaplanab, Eduard Gregorioa
     a
 5    Research Group in AgroICT & Precision Agriculture, Department of Agricultural and Forest Engineering, Universitat de Lleida (UdL) – Agrotecnio

 6   Center, Lleida, Catalonia, Spain.
     b
 7    Department of Signal Theory and Communications, Universitat Politècnica de Catalunya, Barcelona, Catalonia, Spain.

 8   Abstract

 9   The development of remote fruit detection systems able to identify and 3D locate fruits provides opportunities to improve the efficiency

10   of agriculture management. Most of the current fruit detection systems are based on 2D image analysis. Although the use of 3D sensors

11   is emerging, precise 3D fruit location is still a pending issue. This work presents a new methodology for fruit detection and 3D location

12   consisting of: (1) 2D fruit detection and segmentation using Mask R-CNN instance segmentation neural network; (2) 3D point cloud

13   generation of detected apples using structure-from-motion (SfM) photogrammetry; (3) projection of 2D image detections onto 3D space;

14   (4) false positives removal using a trained support vector machine. This methodology was tested on 11 Fuji apple trees containing a total

15   of 1455 apples. Results showed that, by combining instance segmentation with SfM the system performance increased from an F1-score

16   of 0.816 (2D fruit detection) to 0.881 (3D fruit detection and location) with respect to the total amount of fruits. The main advantages of

17   this methodology are the reduced number of false positives and the higher detection rate, while the main disadvantage is the high

18   processing time required for SfM, which makes it presently unsuitable for real-time work. From these results, it can be concluded that the

19   combination of instance segmentation and SfM provides high performance fruit detection with high 3D data precision. The dataset has

20   been      made      publicly     available   and   an     interactive    visualization    of    fruit      detection   results   is   accessible   at

21   http://www.grap.udl.cat/documents/photogrammetry_fruit_detection.html

22   Keywords: Structure-from-motion; fruit detection; fruit location; Mask R-CNN; terrestrial remote sensing

23   1.     Introduction

24        The need to provide food for an increasingly large population, while at the same time minimizing the agricultural impact

25   on the environment, makes it essential to devote as much effort as possible to the development of techniques and methods

26   that can ensure the increased efficiency, quality, and sustainability of agricultural activities. To achieve this goal, precision

27   agriculture (PA) is establishing itself as a cornerstone approach which, based on crop information obtained with various

28   techniques, provides tools for optimizing crop management and making appropriate decisions (ISPA, 2019). The

          * Corresponding author.

          E-mail address: j.gene@eagrof.udl.cat
29   monitoring of crops through the combination of sensors, processing systems, and mobile platforms ‒terrestrial, airborne or

30   spaceborne‒ to carry this instrumentation, are key to providing precise and detailed crop information. Such questions are

31   usually the starting point of optimization processes.

32      Knowledge of the spatial (3D) distribution of fruits through their detection and location, with different levels of

33   resolution ‒within a specific tree and at plot level‒ is of enormous interest in agriculture. Having this information allows

34   harvest and production estimates to be made, which leads to better planning of harvesting, storage and marketing tasks

35   (Bargoti and Underwood, 2017; Nuske et al., 2014). With such information, it is also possible to know the spatial

36   distribution of fruits and yield, and to relate it to the rest of the variables and factors that influence the management of

37   plantations, such as the strategies of irrigation, fertilization and pruning, the characteristics and variability of the soil

38   composition, the topographic characteristics of the plot, the size and structure of the trees, pest and disease impact, and so

39   on. In addition, knowledge of the georeferenced distribution of fruits along the plot can be a starting point for robotized

40   harvesting, as the harvester robot would have the coordinates of each fruit and could primarily focus on the collection

41   process itself, with a resulting gain in speed and efficiency.

42      The characterization of the 3D spatial distribution of fruits, at both tree and plot scale, is a highly active research field.

43   Commonly used sensors include RGB, multispectral, hyperspectral and thermal cameras, as well as 3D sensor technology

44   such as LiDAR and depth cameras (RGB-D) (Li et al., 2014; Narvaez et al., 2017). Each of these sensors has its own

45   strengths and weaknesses when used in real-field conditions, with the best choice depending on the specific application.

46   Thus, while RGB cameras are economically affordable and user-friendly, they are severely affected by lighting conditions

47   (Gongal et al., 2015). Both multi and hyperspectral cameras add spectral information beyond RGB bands, allowing the

48   extraction of a rich set of parameters and vegetation indexes, but they are more expensive and time-consuming. In the case

49   of thermal cameras, which capture the temperature information of objects, the different thermal inertia between fruits and

50   background enables their differentiation. However, measurements are affected by the fruit size and the thermal evolution of

51   the environment along the day, leading to a narrow temporal range of operations in field measurements (Bulanon et al.,

52   2008; Gongal et al., 2015). Both LiDAR and RGB-D systems allow the 3D characteristics of fruits and plants to be directly

53   obtained by determining the sensor-target distance, with time-of-flight and structured-light the most common measuring

54   principles. Both systems allow the generation of high density 3D point clouds (coloured in the case of RGB-D sensors) of

55   plants and fruits. While LiDAR sensors are usually quite expensive and not user-friendly, RGB-D are commonly low-cost

56   plug-and-play sensors but they lose performance in high luminance environments, which is a drawback under real-field

57   conditions (Rosell-Polo et al., 2015). Finally, through the post-processing of digital images, photogrammetry techniques are
58   being used to obtain 3D representations of different scenarios in many fields, including agriculture (Torres-Sánchez et al.,

59   2018). One of the most successful and commonly used methods is called structure-from-motion (SfM), which identifies

60   common characteristics in the collected images to infer the camera positions and then build the 3D representation of the

61   scene (Westoby et al., 2012).

62      With respect to data processing, many state-of-the-art fruit detection systems use handcrafted features to encode the data

63   acquired with different sensors and subsequently apply algorithms to obtain the fruit detection and location (Bargoti and

64   Underwood, 2017; Gené-Mola et al., 2019c). More recently, remarkable progress has been achieved through the

65   introduction of deep learning, which is based on multiple layer artificial neural networks (Koirala et al., 2019). Most

66   approaches in fruit detection are based on the analysis of 2D images, although the processing of 3D images is quickly

67   emerging (Nguyen et al., 2016; Tao and Zhou, 2017). Due to the unstructured environment of tree crops, occlusions of

68   fruits with other vegetative organs and changing lighting conditions are the main problems that have to be dealt with

69   (Gongal et al., 2015). To increase fruit visibility, some authors have proposed the use of multi-view imaging (Hemming et

70   al., 2014), although it may lead to some fruits being counted twice if a proper image registration methodology is not used.

71   To do so, Stein et al. (2016) proposed the use of epipolar geometry combined with the Hungarian algorithm (Kuhn, 2010).

72   Similarly, Liu et al. (2018) used the Hungarian Algorithm refined with SfM to track fruits in video fruit counting. In

73   contrast, Gongal et al. (2016) identified duplicate apples by projecting 2D image detections onto 3D models generated

74   using RGB-D sensor data.

75      This work presents a new methodology for fruit detection and 3D location, combining the use of instance segmentation

76   neural networks and SfM photogrammetry. The Mask R-CNN (He et al., 2017) deep neural network was used to detect and

77   segment fruits in 2D RGB images. Then, SfM was used to generate an accurate 3D model and locate the detected fruits in

78   the space. The main advantages of using SfM are that: (1) it is a multi-view approach and, in consequence, presents a

79   reduced number of fruit occlusions; (2) the registration between images is automatically done, which ensures no double

80   counting of apples appearing in different images. The remainder of this paper is structured as follows: Section 2 presents

81   the experimental setup, the acquired dataset, and the methodology pipeline, including a description of the deep neural

82   network used for fruit detection, the SfM technique used to generate the 3D model, and the projection of 2D image

83   detections onto the 3D generated model; Section 3 evaluates the detections both in the 2D images and in the 3D model,

84   while Section 4 discusses the results; Finally, Section 5 presents the conclusions obtained in this study and proposes future

85   research directions.
 86   2.    Materials and Methods

 87   2.1. Data acquisition.

 88        Tests were carried out in a commercial Fuji apple orchard (Malus domestica Borkh. cv. Fuji) located in the municipality

 89   of Agramunt, Catalonia, Spain (latitude: 41º44’47.07”N; longitude: 1º01’52.23”E). Trees grown in the studied orchard

 90   were trained in a tall spindle system, with a plantation frame of 4 x 0.9 m and a maximum canopy height and width of

 91   approximately 3.5 m and 1.5 m, respectively. The studied section was formed by 11 consecutive trees from the same row of

 92   trees, containing a total of 1455 apples. Images were acquired at the end of September 2017, at BBCH phenological growth

 93   stage 85 ‒advanced ripening, increase in intensity of cultivar-specific color‒ (Meier, 2001).

 94        In the choice of photographic equipment and its setup, the quality of the photographs was prioritized. An EOS 60D

 95   DSLR Canon camera, with an 18 MP (5184 x 3456 px) CMOS APS-C sensor (22.3 x 14.9mm) was used (Canon Inc.

 96   Tokyo, Japan). Regarding the optics, a Canon EF-S 24mm f/2.8 STM lens was chosen, with a 35 mm film equivalent focal

 97   length of 38 mm and with a field of view of [59° 10 ', 50° 35'] (horizontal, vertical).

 98        A total of 582 photographs were taken, 291 images per row side. No artificial light was used. The photographs were

 99   taken freehand, which allowed an average shooting frequency of 8 photographs per minute. Thus, the lighting conditions

100   between the first and last photograph were very similar. The east face was photographed in the morning (11:53 - 12:26h)

101   and the west face in the afternoon (15:27 - 16:05h), with a similar illumination obtained in both faces.

102        Images were taken from 53 photographic positions (per side). In each position, a vertical sweep of 5-6 photographs was

103   taken (Fig. 1a) from the lower part (soil-trunk) to the upper part of the trees. The separation between two consecutive

104   positions was 22 cm (Fig. 1b). These photographic positions defined a line parallel with respect to the apple tree row. The

105   distance between the camera and the middle plane of the row was around 3 m and the height of the camera above the

106   ground was 1.7 m (Fig. 1a). With this configuration, the vertical and horizontal overlapping between neighbouring images

107   was higher than 30% and 90%, respectively (Fig. 2). This dataset has been made publicly available at

108   www.grap.udl.cat/en/publications/datasets.html (Fuji-SfM dataset).
109
110   Fig. 1. a) Transversal scheme of the layout and distances of the photographic process. b) Isometric view of three scanned trees showing the separation
111   between consecutive photographic positions.

                                                 (a)                                                                           (b)
112   Fig. 2. a) Vertical overlapping between two contiguous photographs. b) Horizontal displacement between two adjacent photographic positions.

113   2.2. Methodology pipeline

114      As shown in Fig. 3, the proposed fruit detection and location methodology includes the following processing steps: 1)

115   2D RGB image instance segmentation; 2) 3D point cloud generation using SfM photogrammetry; 3) Projection of 2D

116   detections onto the 3D point cloud.

117      Due to the large amount of apples per image and the fact that convolutional neural networks performance decreases

118   when detecting small objects, before applying the instance segmentation step the images were split into 24 sub-images of

119   1024x1024 pixels. Then, the convolutional neural network Mask R-CNN (He et al., 2017) was used to detect and segment

120   the apples (Section 2.2.1). Apple detections and masks in the cropped images were translated to the original images. These
121   masked images were used to generate a 3D model by means of SfM photogrammetry, thus, only the 3D model of the

122   objects of interest (apples) was generated (Section 2.2.2). To count the total number of fruits, and to know which 3D points

123   belong to each apple, the last step used the camera matrices obtained from SfM camera alignment to project 2D detections

124   onto 3D point clouds following the pinhole camera model (Section 2.2.3).

125     Image cropping step, the translation of detections to the original images, and the projection of 2D detections were

126   processed with a 64-bit operating system, with 8GB of RAM and an Intel ® Core(TM) i7-4500U processor (1.80 GHz,

127   boosted to 2.40 GHz). The instance segmentation step (Mask RCNN) was processed in a CPU+GPU machine with a

128   GeForce GTX TITAN X GPU. The 3D model generation (SfM) was tested in the mentioned CPU computer, as well as in a

129   a CPU+GPU machine with a GeForce GTX 1060. Further details of the implementation of these steps are described in the

130   following sub-sections.

131

132     Fig. 3. Fruit detection and location methodology flowchart. Hexagons represent data preparation steps while rectangles define data processing steps.

133

134            2.2.1. Instance segmentation

135     The Mask R-CNN (He et al., 2017) deep neural network was used for apple detection and segmentation (instance

136   segmentation) in acquired 2D RGB images. For an input image, this model provides 2D bounding boxes and semantic

137   masks for the objects in the scene. It is an extension of the Faster R-CNN (Ren et al., 2017) network that adds a branch for

138   predicting segmentation masks on each region of interest (RoI).
139      The operation is depicted in Fig. 4. Two parts can be differentiated in the architecture: the backbone, used for feature

140   extraction, and the network head for bounding-box recognition (classification and regression) and mask prediction, that is

141   applied separately to each RoI.

142

143                                               Fig. 4. Diagram of Mask R-CNN architecture.

144      The backbone is a feature pyramid network (FPN) (Lin et al., 2017), a type of fully convolutional network that exploits

145   the inherent multi-scale, pyramidal hierarchy of deep convolutional networks to construct a feature pyramid map that

146   provides RoI features from different levels of the feature pyramid according to their scale.

147      The Mask R-CNN network head is a small network that is slid over the feature map. Each sliding window is mapped to

148   a lower-dimensional feature. At each sliding-window location, multiple region proposals are simultaneously predicted. The

149   proposals are parameterized relative to a set of reference boxes, called anchors. An anchor is centred at the sliding window

150   in question, and is associated with a scale and aspect ratio. This anchor-based design improves computational efficiency

151   allowing features to be shared without an extra cost for addressing scales.

152      The obtained features are fed into two sibling fully connected layers—a box-regression layer and a box-classification

153   layer. The process can be described in two stages. The first stage employs a region proposal network (RPN) to scan the

154   feature pyramid map provided by the backbone and outputs a set of regions (region proposals) that are candidates to

155   contain objects. The RoIAlign layer shares the forward pass of a CNN for an image across its subregions. Then, the

156   features in each region are pooled using bilinear interpolation to maintain a precise alignment. The second stage classifies

157   the object inside each one of the proposed regions into a set of predetermined classes, refines the bounding box and

158   provides a pixel level mask for the object. The predictions of the class, bounding box and binary mask for each RoI are

159   performed in parallel.
160     We used an existing implementation of the Mask RCNN obtained from Abdulla (2017) with a ResNet-101-FPN

161   backbone. A model pre-trained in the COCO dataset (Lin et al., 2014) was adapted for Fuji apple detection by restricting

162   the number of classes to one and by fine-tuning the model using 12 images containing a total of 1749 apples that were

163   manually labelled using the VIA annotation software (Dutta and Zisserman, 2019). This small dataset used to train and

164   validate the Mask RCNN did not include images from trees assessed in the 3D location approach, ensuring that the data

165   used to test the system was not used for training. In order to have a better relation between image size and fruit size, and

166   due to the large number of fruits per image, each image was split into 24 sub-images of 1024x1024 pixels (6 horizontal and

167   4 vertical divisions). An overlap between neighbouring sub-images of 213 px in vertical and 192 px in horizontal was

168   applied to avoid the partially split of fruits at the boundaries in different partitions. Thus, the dataset used to train and

169   validate the Mask R-CNN consists of 288 sub-images, split into training and validation as shown in Table 1. Horizontal

170   flipping data augmentation was used to increase the number of training images. The learning rate was set to 0.001, with a

171   learning momentum of 0.9 and a weight decay of 0.0001. This dataset and the corresponding annotations have been made

172   publicly available at www.grap.udl.cat/en/publications/datasets.html (Fuji-SfM dataset).

173     Table 1. Dataset configuration.

                                          Mask R-CNN training - validation
                                          Raw image size Sub-image size
                                          5184 x 3456 px 1024x1024 px
                                          Training       Validation        No. of fruits (annotated)
                                          231 sub-images 57 sub-images     1749

                                          Data for 3D point cloud generation
                                          Raw image size No. of images
                                          5184 x 3456 px    582 (291 per row side)

                                          3D data
                                          No. of trees      No. of fruits     Training      Test
                                          11                1455              3 trees       8 trees

174     Instance segmentation results (Section 3.1) were assessed in terms of recall (R), precision (P), F1-score and average

175   precision (AP) (Zhang and Zhang, 2009), considering as true positives detections with a ground truth mask overlap higher

176   than 50% (IoU > 0.5).
177            2.2.2. 3D point cloud generation

178      To reconstruct the 3D information from the multiple 2D images, a classical multi-view SfM technique based on bundle

179   adjustment (Triggs et al., 2000) was employed in each row side. This approach aims to simultaneously determine the

180   structure (3D coordinates of scene points) and the calibration parameters of each of the cameras that minimize the total

181   reprojection error.

182      In particular, Agisoft Professional Photoscan software was employed to perform the 3D reconstruction (v1.4, Agisoft

183   LLC, St. Petersburg, Russia). The specific software configuration parameters set are detailed in Appendix A, Table A1.

184   The three main steps followed to generate the 3D point cloud are:

185           a.   Feature matching: where correspondences between points across different images are computed.

186           b.   Camera estimation: using the previous correspondences, camera parameters and locations are estimated for

187                each image.

188           c.   Dense reconstruction: camera parameters are used to project 2D image points into their corresponding 3D

189                locations.

190      The relationship between 2D image points and 3D locations is described following a pinhole camera model. Let 𝑥𝑥 be a

191   representation of a 3D point in homogeneous coordinates (a 4-dimensional vector), and let 𝑝𝑝 be a representation of the 2D

192   image of this point in the pinhole camera (a 3-dimensional vector in homogenous coordinates). Then, the relation between

193   them can be expressed as:

                                                                    𝑝𝑝 = 𝐶𝐶𝑖𝑖 · 𝑥𝑥 ,                                                (1)

194   where 𝐶𝐶𝑖𝑖 is the 3x4 camera matrix that represents the intrinsic (matrix 𝐾𝐾) and extrinsic (matrix [𝑅𝑅𝑖𝑖 𝑇𝑇𝑖𝑖 ]) camera parameters

195   for camera 𝑖𝑖:

                                                                 𝐶𝐶𝑖𝑖 = 𝐾𝐾 [𝑅𝑅𝑖𝑖 𝑇𝑇𝑖𝑖 ] ,                                           (2)

196

197      In our case, as all images were taken with the same camera, intrinsic camera parameters are shared between all images

198   (no 𝑖𝑖 subindex in matrix 𝐾𝐾). Extrinsic parameters, on the other hand, are different for each image. Thus, rotation matrices

199   𝑅𝑅𝑖𝑖 and translational vectors 𝑇𝑇𝑖𝑖 are defined for each image and related to the first image of the dataset (camera 𝑖𝑖 = 0 uses

200   𝑅𝑅0 = 𝐼𝐼 and 𝑇𝑇0 = [0 0 0]).

201      Fig. 5a represents the 3D point cloud generated using original RGB images. This point cloud was manually annotated,

202   placing rectangular bounding boxes around each apple (Fig. 5b). A total of 1455 apples were annotated in the point cloud,

203   which is similar to the total number of apples manually counted in the orchard (1444 apples). The small difference between
204   the number of annotations and the number of apples counted in the orchard can be attributed to human error during fruit

205   counting. Annotated 3D bounding boxes were used as ground truth to evaluate the performance of the system in Section

206   3.2.

207      By using a mask in the original images ‒obtained with the trained Mask R-CNN described in Section 2.2.1‒ only the

208   apples (not the entire trees) are reconstructed in Fig. 5c. Using masked images was desirable to only reconstruct the 3D

209   model of the objects of interest (apples) and to reduce the computational time. As the 3D reconstruction stage is scale

210   invariant, a set of known markers (depicted in Fig. 5d) separated by 85 cm were used to scale the resulting 3D point cloud

211   to a real-world scale.

212

213   Fig. 5. a) Illustration of the 3D point cloud obtained using original RGB images. Yellow rectangles show the positions where reference markers were
214   placed. b) Annotated point cloud with 3D rectangular bounding boxes placed around each apple. c) Apples 3D point cloud obtained using masked images.
215   d) Illustration of reference markers used to scale the resulting 3D point cloud.

216             2.2.3. Projection of 2D detections onto 3D point cloud

217      Although SfM photogrammetry with masked images allows generation of the 3D model of only the objects of interest

218   (apples), the resulting point cloud should be clustered in groups of 3D points per apple (3D apple detections) to count and

219   locate detected fruits.

220      Knowing the intrinsic camera parameters (matrix K), as well as the pose and orientation of all images (matrix [Ri Ti]),

221   2D image detections were projected onto the 3D point cloud using the pinhole camera model (Eqs. (1) and (2)). The main

222   issues to deal with during these projections were: (1) identification of objects (apples) behind detections; (2) unification of

223   detections of an object detected from different photos.
224     Fig. 6 illustrates the steps carried out to perform the 2D to 3D projection, showing an example with two images taken

225   from different positions. To assist visualization, Fig. 6a shows a small region of the scanned scene and Fig. 6b shows the

226   3D model obtained applying SfM photogrammetry with masked images. In Fig. 6c, detections from image 1 (img1) were

227   projected onto the 3D point cloud. Due to the position of the camera with respect to the scene, an apple was occluded

228   behind the green detection. In consequence, after projecting the 2D green detection, the detected and the occluded apples

229   were clustered within the same group of 3D points (plotted in green in the 3D model of Fig. 6c). To identify objects behind

230   a detection, a connected components labelling was applied to each 3D projection using the density-based scan algorithm

231   DBSCAN (Ester et al., 1996). The minimum distance between connected points was set to 3 cm. If more than one group of

232   connected points were found in a 3D detection, only the nearest (to the camera) was selected. Comparing Fig. 6c and Fig.

233   6d, it can be observed how the apple behind the green detection was released after applying DBSCAN. Having the

234   detections of img1 in the 3D point cloud, the next image (img2) was processed. Detections from img2 that presented an

235   overlap higher than 50% (IoU > 0.5) with previously detected apples were identified and unified (Fig. 6e), and new

236   detections with no overlap with previous detections or with IoU < 0.5 were projected onto the 3D point cloud (Fig. 6f). The

237   process was repeated for all the images used to generate the 3D point cloud.

238     In order to reduce the number of false positives, a linear support-vector-machine (SVM) was trained to identify and

239   remove false positive detections. This SVM was fed using 4 features per detection:

240          •   Number of points P that contain a 3D detection.

241          •   Detection volume V.

                                         𝑉𝑉
242          •   Detection density δ =        .
                                         𝑃𝑃

243          •   Geometric feature 𝛹𝛹 = 27 · λ1𝑛𝑛 · λ2𝑛𝑛 · λ3𝑛𝑛 , where [λ1𝑛𝑛 , λ2𝑛𝑛 , λ3𝑛𝑛 ] are the normalized eigenvalues (so that

244              λ1𝑛𝑛 + λ2𝑛𝑛 + λ3𝑛𝑛 = 1), obtained applying singular value decomposition (SVD) on the 3D points of a detection.

245              The applied coefficient of 27 allows 𝛹𝛹 to be bounded between 0 and 1, with 1 being for spherical detections.

246     The graphical representation of these features is shown in Appendix B, Fig. B 1. In order to train this SVM, 3 trees (out

247   of 11) containing a total of 434 apples were used as the training dataset. The result of identifying and removing false

248   positive detections can be observed in Fig. 6g, where the blue detection has been removed.
249

250   Fig. 6. Projection of 2D detections onto 3D point cloud. a) Data acquisition. b) 3D model obtained using structure-from-motion with segmented images. c)
251   Projection of detections from image 1 (img1) onto the 3D point cloud. d) Identification of apples behind detections. e) Identification of apples appearing in
252   a new image that were previously detected in other images. f) Projection of a new detection (coloured in purple) from image 2 (img2). g) False positive
253   removal.

254      3D fruit detection results (Section 3.2) were assessed in terms of detection rate (𝐷𝐷𝐷𝐷), recall (𝑅𝑅), precision (𝑃𝑃), false

255   positive rate (𝐹𝐹𝐹𝐹𝐹𝐹), muti-detection rate (𝑀𝑀𝑀𝑀𝑀𝑀), and F1-score, as follows:

                                                                             𝐿𝐿𝐿𝐿
                                                                  𝐷𝐷𝐷𝐷 =                                                                        (3)
                                                                             𝑇𝑇 ,

                                                                           𝑇𝑇𝑇𝑇
                                                                    𝑅𝑅 =                                                                        (4)
                                                                            𝑇𝑇 ,

                                                                           𝑇𝑇𝑇𝑇
                                                                    𝑃𝑃 =                                                                        (5)
                                                                           𝐷𝐷 ,

                                                                              𝐹𝐹𝐹𝐹
                                                                  𝐹𝐹𝐹𝐹𝐹𝐹 =                                                                      (6)
                                                                               𝐷𝐷 ,

                                                                              𝑀𝑀𝑀𝑀
                                                                 𝑀𝑀𝑀𝑀𝑀𝑀 =                                                                       (7)
                                                                                  𝐷𝐷 ,

                                                                             𝑅𝑅·𝑃𝑃
                                                                 𝐹𝐹1 = 2                                                                        (8)
                                                                             𝑅𝑅+𝑃𝑃 ,

256   where 𝑇𝑇 is the total number of fruits in the dataset, 𝐷𝐷 is the number of detections, 𝐿𝐿𝐿𝐿 is the number of labels detected

257   (annotations bounding boxes detected), 𝑇𝑇𝑇𝑇 is the number of true positives (detection with a ground truth overlap higher

258   than 50%), 𝐹𝐹𝐹𝐹 is the number of false positives (detection with a ground truth overlap lower than 50%), and 𝑀𝑀𝑀𝑀 is the

259   number of multi-detections produced when a single apple is detected multiple times.

260

261
262   3.    Results

263   3.1. 2D detection results

264        Table 2 presents instance segmentation results after training Mask R-CNN during 18 epochs (number of epochs not

265   presenting overfitting). Results show an AP of 0.8599, and an F1-score of 0.8573. Although the best balance between P and

266   R was achieved with a confidence threshold of 0.9, all detections classified as “apple” (confidence level > 0.5) where used

267   for the 3D point cloud generation. This is because an increase of false positives (lower precision) is not as critical as

268   decreasing the recall, since to build the 3D model an object has to be seen in, at least, two different images. Then, false

269   positive objects that are only detected in one image will be automatically removed when applying SfM photogrammetry.

270   Table 2. Instance segmentation results at different confidence levels. Best F1-score result is in bold type.

                                                      Confidence         R               P               F1
                                                      0.5                0.8779          0.7622          0.8160
                                                      0.55               0.8746          0.7737          0.8211
                                                      0.6                0.8746          0.7840          0.8268
                                                      0.65               0.8729          0.7991          0.8344
                                                      0.7                0.8680          0.8117          0.8389
                                                      0.75               0.8663          0.8242          0.8447
                                                      0.8                0.8663          0.8333          0.8495
                                                      0.85               0.8647          0.8465          0.8555
                                                      0.9                0.8597          0.8569          0.8583
                                                      0.95               0.8399          0.8761          0.8576
                                                      AP                 0.8599

271        Fig. 7 shows 6 selected images from the validation dataset and the corresponding fruit detections, allowing a qualitative

272   evaluation of instance segmentation results. As can be observed, most of the apples were successfully detected, including

273   highly occluded or shadowed ones. In addition, Mask-RCNN masked correctly the pixels belonging to an apple, even when

274   apples were visually split by branch or leaves, which is of interest to generate the 3D model of only apples when applying

275   SfM. It was also observed that some of the detections reported as false positive were actually apples miss-annotated due to

276   human error when labeling (green rectangles in Fig. 7 b-d,f). Other false positives were wrong detections at the image

277   borders, in parts of the image presenting a similar pattern to apples (red rectangles in Fig. 7 b-d), or multi-detections (blue

278   rectangles in Fig. 7 a,e-f). As for the apples not detected, it can be seen that false negatives (yellow rectangles in Fig. 7 a-

279   b,e) were apples cut at the image borders, highly occluded and/or small apples. To overcome the increase of false positives

280   and negatives at image borders, a certain overlap between sub-images was considered when splitting the original image into

281   sub-images (Section 2.2.1). Thus, detection failures at image borders did not affect the performance of the 3D model.
282

283   Fig. 7. Selected examples of instance segmentation results to show correct detections (colour masks), false positives due to network failures (red
284   rectangles), false positives due to miss-annotated apples (green rectangles), false positives due to multi-detections (blue rectangles), and false negatives
285   (yellow rectangles). For each capture, the original sub-image (left) and the corresponding detections (right) are shown.

286   3.2. 3D location results

287      This section evaluates quantitatively and qualitatively the performance of the proposed methodology for 3D fruit

288   detection and location. Table 3 presents the detection rates achieved in the training (3 trees, 434 apples) and test (8 trees,

289   1021 apples) datasets. Results show a high detection rate (DR=0.991) with low false detections (FDR=0.037). However,

290   because some apples were clustered in a unique detection (as shown in Fig. 9) and due to the presence of multi-detections

291   (MDR=0.106), the recall and precision decreased to 0.906 and 0.857, respectively, which represents an F1-score of 0.881.

292   Table 3. 3D fruit detection and location results from training and test datasets.

                                                                   DR       R         P      FDR     MDR F1-score
                                              Training dataset 0.984 0.905 0.881 0.038 0.081 0.893
                                              Test dataset         0.991 0.906 0.857 0.037 0.106 0.881
293      For yield prediction, the percentage of detected fruits and false positives is not as important as having a high correlation

294   between the number of detections (𝐷𝐷 = 𝑇𝑇𝑇𝑇 + 𝐹𝐹𝐹𝐹 + 𝑀𝑀𝑀𝑀) and the actual number of fruits in the trees (𝑇𝑇) (Linker, 2017).

295   Fig. 8 illustrates the correspondence between 𝐷𝐷 and 𝑇𝑇 in all trees of the dataset (11 trees). Results show the existence of a

296   linear correlation between these variables, presenting a coefficient of determination of R2=0.80 and a root mean square

297   deviation of 6.42% of fruits.

298

299                      Fig. 8. Linear regression between the number of detections (D) and the actual number of fruits per tree (T).

300      For a qualitative evaluation, the reader is referred to inspect an interactive 3D visualization of the test scene and the

301   corresponding      fruit        detections        by        opening         the        following         link        in       a   web-browser:

302   http://www.grap.udl.cat/documents/photogrammetry_fruit_detection.html. Using the side menu, the reader can either

303   visualize the scanned scene, the 3D point cloud of the apples obtained using SfM with masked images, or the apple

304   detections obtained after 2D-3D projection and false positive removal steps.

305      The obtained point cloud showed higher 3D data precision compared with data provided by other sensors used for fruit

306   detection, such as LiDAR or depth-cameras (Gené-Mola et al., 2019a, 2019b; Gongal et al., 2016; Nguyen et al., 2016; Tao

307   and Zhou, 2017; Williams et al., 2019). Moreover, most of the apples were correctly detected, identifying the 3D points

308   that belong to each apple. The presence of false positives is almost non-existent (FDR=0.037), while most of the multi-

309   detections appeared in apples seen from both sides of the row of trees, when the detection from one side did not overlap

310   sufficiently (they were not unified) with the detection from the other tree side. In contrast, as shown in Fig. 9, some groups

311   of apples were unified in a single detection, which explains the difference between the detection rate and the recall values

312   reported in Table 3. This is because when two apples were detected in a single detection, only one true positive is counted

313   to compute the recall metric.
314

315   Fig. 9. Illustration of 3D fruit detection and location results from the test dataset: a) 3D visualisation of the scanned scene. b) Test scene with coloured
316   fruit detections. A zoom view is shown to assist the visualization of the detections in the first tree of the dataset. Black circles show two examples where
317   two apples were unified in a single detection. The reader is referred to the following link for an interactive 3D visualization of test fruit detection results:
318   http://www.grap.udl.cat/documents/photogrammetry_fruit_detection.html

319   Regarding the computational cost of the presented methodology, Table 4 includes the inference time of different

320   processing steps implied in the presented methodology. The most computational expensive was the SfM photogrammetry,

321   which required around 500 min to generate the 3D point cloud of the apples contained in the 11 tested trees in a

322   conventional CPU computer. However, this processing time could be significantly reduced by processing this step in a

323   graphic processing unite (GPU). The projection of 2D detections onto the 3D point cloud was also a computational

324   expensive step, which required 260 min to process all images from the dataset. Since the code developed to project 2D

325   detections onto the 3D point cloud was not parallelized, this step could not be processed in the CPU+GPU machine.

326   Table 4. Computational cost of processing steps implied in the developed methodology. The reported processing time corresponds to the time required to
327   process all the dataset (11 trees, 582 images).

                                 Process                                                                     Processing time
                                                                                                          CPU          CPU+GPU
                                 Instance segmentation (Mask RCNN)                                         ---            35 min
                                 3D point cloud generation (SfM)                                         500 min          50 min
                                 Projection of 2D detections onto 3D point cloud                         260 min            ---
328
329   4.   Discussion

330        This paper proposes a combination of instance segmentation neural networks and SfM for fruit detection and 3D

331   location. By projecting 2D segmentation masks onto the 3D point cloud, results showed an increase of 2.8% in recall (from

332   0.878 to 0.906), 9.5% in precision (from 0.762 to 0.857) and 6.5% in F1-score (from 0.816 to 0.881). This difference could

333   be even larger because 2D instance segmentation results were evaluated with respect to the number of visible fruits in the

334   images –since it was not possible to estimate the number of occluded fruits in the 2D images–, while the 3D fruit detection

335   was evaluated with respect to the total number of fruits in the tree. The use of SfM helped to increase the detection rate

336   because of the multi-view approach of this technique. As stated by Hemming et al. (2014), due to the unstructured

337   environment of orchards most fruits are partially/fully occluded from a single viewpoint, and thus multi-view imaging

338   increases fruit detectability. When using multi-view imaging, an image registration is necessary to not double-count apples

339   appearing in different images. In this work, this registration was automatically done by projecting 2D detections onto the

340   3D point cloud; even so, results showed a 10.6% multi-detection rate. Other authors have proposed similar approaches:

341   Gongal et al. (2016) reported an error of 21.1% when identifying duplicate apples by projecting 2D image detections onto

342   3D models from RGB-D sensors, while Stein et al. (2016) used the 3D point cloud acquired from LiDAR-based sensors to

343   identify multi-detections, although they did not assess the performance of this multi-detection identification. Using SfM not

344   only helped to increase the detection rate, but also decreased the number of false detections, because, to build the 3D point

345   cloud, an object has to be detected in at least two different images, but the same false positive is not likely to be detected in

346   two different images. Then, false positives only detected in one image were automatically removed. This fact, combined

347   with the use of an SVM to identify false positives, explains the increase of 11.9% in precision, from 0.762 (2D image

348   detections) to 0.881 (3D detections).

349        Although it is difficult to compare results from different datasets, our implementation of Mask R-CNN (F1-

350   score=0.8583) performed similarly to other state-of-the-art fruit detection works based on deep convolutional neural

351   networks, which reported F1-score values between 0.73 and 0.97 (Koirala et al., 2019). Mask R-CNN is not as fast as other

352   object detection networks used for fruit detection ‒ such as YOLO (Redmon and Farhadi, 2018; Tian et al., 2019) ‒, but it

353   has the advantage of providing segmentation masks for each detection, which is necessary in our application to obtain the

354   proper 3D location when projecting 2D detections onto the 3D point cloud. As for the 3D apple location performance, few

355   works have provided 3D detection rates with respect to the total amount of fruits in trees. For instance, Stein et al. (2016)

356   reported a good correlation (R2=0.9) between the number of fruits detected and the actual number of fruits in the trees, but

357   the methodology was not assessed in terms of precision, recall and F1-score (or similar metrics). Tao and Zhou (2017)
358   reported a similar 3D detection performance to that of our methodology (F1-score = 0.921), but they tested the system on a

359   smaller dataset of 59 apples. Finally, comparing the presented methodology with respect to other computer vision systems

360   used in fruit harvesting robots, our system performed well compared to most of those presented in Bac et al. (2014) and

361   Williams et al. (2019), which reported detection rates below 85%. However, the presented methodology is not suitable for

362   harvesting robots because it cannot work at real-time due to the high amount of images to be processed and

363   computationally-intensive processing of SfM (Wang et al., 2019). Nevertheless, the evolution of computing hardware and

364   the development of efficient algorithms could overcome this limitation in the future.

365         From a qualitative/visual analysis of the 3D data, the point cloud obtained using SfM presented a higher precision

366   compared with other sensors used for 3D fruit location, such as LiDAR-based and depth cameras (Gené-Mola et al., 2019a;

367   Nguyen et al., 2016; Tao and Zhou, 2017). This suggests that the methodology could potentially be used to measure fruit

368   size, which, combined with the good correlation between the number of fruit detections and the number of total fruits in the

369   tree, would allow computation of fruit load in weight (yield estimation).

370        For yield prediction or yield mapping applications, the computational cost of the presented methodology is not a critical

371   issue, as data can be processed offline. However, in the tests carried out in this work, data was acquired manually, being a

372   labour and time consuming task when scanning larger areas. In order to automatize the data acquisition, some authors have

373   used RGB-D sensors integrated on mobile platforms (Milella et al., 2019). Similarly, to optimize the data acquisition of the

374   proposed methodology, future works should study the development of a compact system composed by different cameras

375   mounted on a terrestrial platform.

376   5.    Conclusions

377        This work proposes the combination of instance segmentation neural networks and structure-from-motion (SfM) for

378   apple detection and 3D location. Due to the multi-view approach on which SfM is based, results showed a small number of

379   fruit occlusions compared with other fruit detection systems, reporting a detection rate of 99.1%. However, 8.5% of the

380   apples were grouped in detections with more than one apple, with the result that the recall rate decreased to 0.906. Another

381   advantage of using SfM was the reduction of false positives. Since SfM only generates the 3D model of those objects

382   appearing in, at least, two different images, false positives only detected in one image were automatically discarded. This

383   false positive reduction from SfM, combined with the use of a support vector machine to identify false positive detections,

384   produced an increase in the precision metric from 0.762 (2D image detections) to 0.857 (3D detections). 3D location results

385   reported an F1-score of 0.881 with respect to the total amount of fruit on the trees, with the conclusion that the proposed
386   methodology performs well compared to other state-of-the-art 3D fruit location systems. The main disadvantage of this

387   methodology is that, due to the computationally-intensive operations of SfM, it cannot process the data in real-time, which

388   is an important limitation for its application in harvesting robots. However, the evolution of computing hardware and the

389   development of efficient algorithms could overcome this issue in the future. The dataset and the corresponding annotations

390   have been made publicly available, being the first dataset for 3D photogrammetric fruit detection and location. Due to the

391   high spatial precision obtained with SfM and the good correlation between the number of detections and the actual number

392   of fruits in the tree (R2=0.8), future works should extend the methodology to measure fruit size and, consequently, perform

393   fruit yield estimations.

394   Acknowledgements

395      This work was partly funded by the Secretaria d’Universitats i Recerca del Departament d’Empresa i Coneixement de la

396   Generalitat de Catalunya (grant 2017 SGR 646), the Spanish Ministry of Economy and Competitiveness (project

397   AGL2013-48297-C2-2-R) and the Spanish Ministry of Science, Innovation and Universities (project RTI2018-094222-B-

398   I00). Part of the work was also developed within the framework of the project TEC2016-75976-R, financed by the Spanish

399   Ministry of Economy, Industry and Competitiveness and the European Regional Development Fund (ERDF). The Spanish

400   Ministry of Education is thanked for Mr. J. Gené’s pre-doctoral fellowships (FPU15/03355). We would also like to thank

401   Nufri (especially Santiago Salamero and Oriol Morreres) and Vicens Maquinària Agrícola S.A. for their support during

402   data acquisition, and Ernesto Membrillo and Roberto Maturino for their support in dataset labelling.

403

404   Appendix A. Parameter values used for 3D point cloud generation

405   Table A1. Configuration set to perform the 3D reconstruction using Agisoft Professional Photoscan (v1.4, Agisoft LLC, St. Petersburg,
406   Russia).

           Step         Parameter          Configuration set    Description
                        Accuracy           High                 Images used in original size
           Camera
                        Key point limit    100000               Upper limit of feature points per image
           alignment
                        Tie point limit    10000                Upper limit of matching points per image
           Dense        Quality            Medium               Images downscaled by factor of 16 (4 times per side)
           cloud        Depth filtering    Mild                 Filter used to sort out outliers
407

408   Appendix B. False positive feature analysis
409   Fig. B 1 Graphical representation of apple detection features. The features analysed are the volume, number of points, the geometric parameter Ψ, and the
410   detection point density δ. False positives are represented in red crosses; true positives are represented in blue diamonds. This analysis was performed on
411   the training data set and was used to train the SVM for false positives identification (explained in Section 2.2.3).

412   REFERENCES

413   Abdulla, W., 2017. Mask R-CNN for object detection and instance segmentation on Keras and TensorFlow. GitHub Repos.

414   Bac, C.W., Van Henten, E.J., Hemming, J., Edan, Y., 2014. Harvesting Robots for High-value Crops: State-of-the-art Review and Challenges Ahead. J. F.

415          Robot. 31, 888–911. doi:10.1002/rob.21525

416   Bargoti, S., Underwood, J.P., 2017. Image Segmentation for Fruit Detection and Yield Estimation in Apple Orchards. J. F. Robot. 34, 1039–1060.

417          doi:10.1002/rob.21699

418   Bulanon, D.M., Burks, T.F., Alchanatis, V., 2008. Study on temporal variation in citrus canopy using thermal imaging for citrus fruit detection. Biosyst.

419          Eng. 101, 161–171. doi:10.1016/j.biosystemseng.2008.08.002

420   Dutta, A., Zisserman, A., 2019. The VIA Annotation Software for Images, Audio and Video, in: Proceedings of the 27th ACM International Conference

421          on Multimedia. ACM, New York, NY, USA. doi:10.1145/3343031.3350535

422   Ester, M., Kriegel, H.P., Sander, J., Xu, X., 1996. A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise. Proc. 2nd

423          Int. Conf. Knowl. Discov. Data Min. 96, 226–231. doi:10.1.1.71.1980

424   Gené-Mola, J., Gregorio, E., Guevara, J., Auat, F., Sanz-cortiella, R., Escolà, A., Llorens, J., Morros, J.-R., Ruiz-Hidalgo, J., Vilaplana, V., Rosell-Polo,

425          J.R., 2019a. Fruit detection in an apple orchard using a mobile terrestrial laser scanner. Biosyst. Eng. 187, 171–184.

426          doi:10.1016/j.biosystemseng.2019.08.017

427   Gené-Mola, J., Vilaplana, V., Rosell-Polo, J.R., Morros, J.-R., Ruiz-Hidalgo, J., Gregorio, E., 2019b. KFuji RGB-DS database: Fuji apple multi-modal

428          images for fruit detection with color, depth and range-corrected IR data. Data Br. 25, 104289. doi:10.1016/j.dib.2019.104289

429   Gené-Mola, J., Vilaplana, V., Rosell-Polo, J.R., Morros, J.R., Ruiz-Hidalgo, J., Gregorio, E., 2019c. Multi-modal deep learning for Fuji apple detection

430          using RGB-D cameras and their radiometric capabilities. Comput. Electron. Agric. 162, 689–698. doi:10.1016/j.compag.2019.05.016

431   Gongal, A., Amatya, S., Karkee, M., Zhang, Q., Lewis, K., 2015. Sensors and systems for fruit detection and localization: A review. Comput. Electron.

432          Agric. 116, 8–19. doi:10.1016/j.compag.2015.05.021

433   Gongal, A., Silwal, A., Amatya, S., Karkee, M., Zhang, Q., Lewis, K., 2016. Apple crop-load estimation with over-the-row machine vision system.
434          Comput. Electron. Agric. 120, 26–35. doi:10.1016/j.compag.2015.10.022

435   He, K., Gkioxari, G., Dollar, P., Girshick, R., 2017. Mask RCNN. Proc. IEEE Int. Conf. Comput. Vis. 2017, 2961–2969. doi:10.1109/ICCV.2017.322

436   Hemming, J., Ruizendaal, J., Willem Hofstee, J., van Henten, E.J., 2014. Fruit detectability analysis for different camera positions in sweet-pepper.

437          Sensors (Switzerland) 14, 6032–6044. doi:10.3390/s140406032

438   ISPA, (International Society of PrecisionAgriculture), 2019. ISPA Official Definition of Precision Agriculture. ISPA Newsl. 7 (7) July.

439   Koirala, A., Walsh, K.B., Wang, Z., McCarthy, C., 2019. Deep learning – Method overview and review of use for fruit detection and yield estimation.

440          Comput. Electron. Agric. 162, 219–234. doi:10.1016/j.compag.2019.04.017

441   Kuhn, H.W., 2010. The Hungarian method for the assignment problem, in: 50 Years of Integer Programming 1958-2008: From the Early Years to the

442          State-of-the-Art. doi:10.1007/978-3-540-68279-0_2

443   Li, L., Zhang, Q., Huang, D., 2014. A review of imaging techniques for plant phenotyping. Sensors (Switzerland) 14, 20078–20111.

444          doi:10.3390/s141120078

445   Lin, T.Y., Dollár, P., Girshick, R., He, K., Hariharan, B., Belongie, S., 2017. Feature pyramid networks for object detection, in: Proceedings - 30th IEEE

446          Conference on Computer Vision and Pattern Recognition, CVPR 2017. doi:10.1109/CVPR.2017.106

447   Lin, T.Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollár, P., Zitnick, C.L., 2014. Microsoft COCO: Common objects in context, in:

448          European Conference on Computer Vision. pp. 740–755. doi:10.1007/978-3-319-10602-1_48

449   Linker, R., 2017. A procedure for estimating the number of green mature apples in night-time orchard images using light distribution and its application to

450          yield estimation. Precis. Agric. 18, 59–75. doi:10.1007/s11119-016-9467-4

451   Liu, X., Chen, S.W., Aditya, S., Sivakumar, N., Dcunha, S., Qu, C., Taylor, C.J., Das, J., Kumar, V., 2018. Robust Fruit Counting: Combining Deep

452          Learning, Tracking, and Structure from Motion. IEEE Int. Conf. Intell. Robot. Syst. 1045–1052. doi:10.1109/IROS.2018.8594239

453   Meier, U., 2001. Growth stages of mono- and dicotyledonous plants, BBCH Monograph. doi:10.5073/bbch0515

454   Milella, A., Marani, R., Petitti, A., Reina, G., 2019. In-field high throughput grapevine phenotyping with a consumer-grade depth camera. Comput.

455          Electron. Agric. 156, 293–306. doi:10.1016/j.compag.2018.11.026

456   Narvaez, F.Y., Reina, G., Torres-Torriti, M., Kantor, G., Cheein, F.A., 2017. A survey of ranging and imaging techniques for precision agriculture

457          phenotyping. IEEE/ASME Trans. Mechatronics 22, 2428–2439. doi:10.1109/TMECH.2017.2760866

458   Nguyen, T.T., Vandevoorde, K., Wouters, N., Kayacan, E., De Baerdemaeker, J.G., Saeys, W., 2016. Detection of red and bicoloured apples on tree with

459          an RGB-D camera. Biosyst. Eng. 146, 33–44. doi:10.1016/j.biosystemseng.2016.01.007

460   Nuske, S., Wilshusen, K., Achar, S., Yoder, L., Singh, S., 2014. Automated visual yield estimation in vineyards. J. F. Robot. 31(5), 837–860.

461          doi:10.1002/rob.21541

462   Redmon, J., Farhadi, A., 2018. YOLOv3: An Incremental Improvement. Tech Report, arXiv1804.02767.

463   Ren, S., He, K., Girshick, R., Sun, J., 2017. Faster R-CNN: towards real-time object detection with region proposal networks. IEEE Trans. Pattern Anal.

464          Mach. Intell. 39, 1137–1149. doi:10.1109/TPAMI.2016.2577031

465   Rosell-Polo, J.R., Cheein, F.A., Gregorio, E., Andújar, D., Puigdomènech, L., Masip, J., Escolà, A., 2015. Advances in Structured Light Sensors

466          Applications in Precision Agriculture and Livestock Farming. Adv. Agron. 133, 71–112. doi:10.1016/bs.agron.2015.05.002

467   Stein, M., Bargoti, S., Underwood, J., 2016. Image Based Mango Fruit Detection, Localisation and Yield Estimation Using Multiple View Geometry.

468          Sensors 16, 1915. doi:10.3390/s16111915

469   Tao, Y., Zhou, J., 2017. Automatic apple recognition based on the fusion of color and 3D feature for robotic fruit picking. Comput. Electron. Agric. 142,
470          388–396. doi:10.1016/j.compag.2017.09.019

471   Tian, Y., Yang, G., Wang, Z., Wang, H., Li, E., Liang, Z., 2019. Apple detection during different growth stages in orchards using the improved YOLO-V3

472          model. Comput. Electron. Agric. 157, 417–426. doi:10.1016/j.compag.2019.01.012

473   Torres-Sánchez, J., de Castro, A.I., Peña, J.M., Jiménez-Brenes, F.M., Arquero, O., Lovera, M., López-Granados, F., 2018. Mapping the 3D structure of

474          almond trees using UAV acquired photogrammetric point clouds and object-based image analysis. Biosyst. Eng. 176, 172–184.

475          doi:10.1016/j.biosystemseng.2018.10.018

476   Triggs, B., McLauchlan, P.F., Hartley, R.I., Fitzgibbon, A.W., 2000. Bundle Adjustment — A Modern Synthesis Vision Algorithms: Theory and Practice.

477          Vis. Algorithms Theory Pract. 298–375. doi:10.1007/3-540-44480-7_21

478   Wang, X., Rottensteiner, F., Heipke, C., 2019. Structure from motion for ordered and unordered image sets based on random k-d forests and global pose

479          estimation. ISPRS J. Photogramm. Remote Sens. 147, 19–41. doi:10.1016/j.isprsjprs.2018.11.009

480   Westoby, M.J., Brasington, J., Glasser, N.F., Hambrey, M.J., Reynolds, J.M., 2012. “Structure-from-Motion” photogrammetry: A low-cost, effective tool

481          for geoscience applications. Geomorphology 179, 300–314. doi:10.1016/j.geomorph.2012.08.021

482   Williams, H.A.M., Jones, M.H., Nejati, M., Seabright, M.J., Bell, J., Penhall, N.D., Barnett, J.J., Duke, M.D., Scarfe, A.J., Seok, H., Lim, J., Macdonald,

483          B.A., 2019. Robotic kiwifruit harvesting using machine vision , convolutional neural networks , and robotic arms. Biosyst. Eng. 181, 140–156.

484          doi:10.1016/j.biosystemseng.2019.03.007

485   Zhang, E., Zhang, Y., 2009. Average Precision, in: LIU, L., ÖZSU, M.T. (Eds.), Encyclopedia of Database Systems. Springer US, Boston, MA, pp. 192–

486          193. doi:10.1007/978-0-387-39940-9_482

487
